function Str(element)
  if element.text ~= ":date:" then
    return nil
  end

  if FORMAT:match("html") then
    return pandoc.RawInline(
      "html",
      '<span class="date-marker" aria-label="Datum">&#128197;</span>'
    )
  end

  if FORMAT:match("latex") then
    return pandoc.RawInline("latex", "\\faIcon{calendar-alt}")
  end

  return pandoc.Str("Datum:")
end
