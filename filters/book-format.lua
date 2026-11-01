-- Promote existing, manually numbered HTML headings without rewriting notebooks.
-- Their visible numbers are retained; unnumbered prevents a second writer number.
-- Style existing numbered HTML headings without editing notebook sources.
-- Keep their printed numbers; native Markdown headings keep Quarto numbering.
local function numbered_header(level, content, attributes)
  local number = pandoc.utils.stringify(content):match("^(%d+%.%d+[%.%d]*)%s")
  if not number then return nil end
  local attr = attributes or pandoc.Attr()
  if attr.identifier == "" then
    attr.identifier = "abschnitt-" .. number:gsub("%.", "-")
  end
  if not attr.classes:includes("unnumbered") then
    attr.classes:insert("unnumbered")
  end
  return pandoc.Header(tonumber(level), content, attr)
end

function Blocks(blocks)
  local result = pandoc.List()
  local i = 1
  while i <= #blocks do
    local b = blocks[i]
    local level, attrs
    if b.t == "RawBlock" and b.format == "html" then
      level, attrs = b.text:match("^%s*<h([234])([^>]*)>%s*$")
    end
    if level and blocks[i + 1] and blocks[i + 2]
      and (blocks[i + 1].t == "Plain" or blocks[i + 1].t == "Para")
      and blocks[i + 2].t == "RawBlock"
      and blocks[i + 2].format == "html"
      and blocks[i + 2].text:match("^%s*</h" .. level .. ">%s*$") then
      local id = attrs:match('id="([^"]+)"') or attrs:match("id='([^']+)'") or ""
      local h = numbered_header(level, blocks[i + 1].content, pandoc.Attr(id))
      if h then
        result:insert(h)
        i = i + 3
      else
        result:insert(b)
        i = i + 1
      end
    elseif b.t == "RawBlock" and b.format == "html" then
      local opening, text, closing = b.text:match("^%s*<h([234])[^>]*>(.-)</h([234])>%s*$")
      local h
      if opening and opening == closing then
        local parsed = pandoc.read(b.text, "html")
        if #parsed.blocks == 1 and parsed.blocks[1].t == "Header" then
          h = numbered_header(opening, parsed.blocks[1].content, parsed.blocks[1].attr)
        end
      end
      result:insert(h or b)
      i = i + 1
    else
      result:insert(b)
      i = i + 1
    end
  end
  return result
end

-- Existing xurl handles long filenames without changing their visible text.
function Code(code)
  if FORMAT:match("latex") and code.identifier == "" and #code.text >= 18
    and code.text:match("^[%w%._/%\\:%-]+$") then
    return pandoc.RawInline("latex", "\\nolinkurl{" .. code.text .. "}")
  end
end

-- Front matter remains Roman; the first text chapter starts at page one.
function Header(header)
  if FORMAT:match("latex") and header.level == 1
    and pandoc.utils.stringify(header.content) == "Überblick" then
    return {pandoc.RawBlock("latex", "\\clearpage\n\\pagenumbering{arabic}"), header}
  end
end

function Table(tbl)
  -- Only the wide seven-column result comparisons need a smaller print style.
  if FORMAT:match("latex") and #tbl.colspecs >= 7 then
    return {
      pandoc.RawBlock("latex", "{\\small\\setlength{\\tabcolsep}{4pt}"),
      tbl,
      pandoc.RawBlock("latex", "}"),
    }
  end
end
