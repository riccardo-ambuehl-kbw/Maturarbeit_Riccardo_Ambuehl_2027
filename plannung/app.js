const STORAGE_KEY = "maturarbeit-todos-v1";

const state = {
  todos: [],
  query: "",
  status: "alle",
  sort: "createdDesc",
};

const relevanceWeight = {
  hoch: 3,
  mittel: 2,
  niedrig: 1,
};

const form = document.querySelector("#todoForm");
const todoId = document.querySelector("#todoId");
const titleInput = document.querySelector("#titleInput");
const descriptionInput = document.querySelector("#descriptionInput");
const relevanceInput = document.querySelector("#relevanceInput");
const statusInput = document.querySelector("#statusInput");
const dueInput = document.querySelector("#dueInput");
const categoryInput = document.querySelector("#categoryInput");
const submitBtn = document.querySelector("#submitBtn");
const cancelEditBtn = document.querySelector("#cancelEditBtn");
const todoList = document.querySelector("#todoList");
const emptyState = document.querySelector("#emptyState");
const template = document.querySelector("#todoTemplate");
const searchInput = document.querySelector("#searchInput");
const statusFilter = document.querySelector("#statusFilter");
const sortInput = document.querySelector("#sortInput");
const exportBtn = document.querySelector("#exportBtn");
const importInput = document.querySelector("#importInput");

const totalCount = document.querySelector("#totalCount");
const openCount = document.querySelector("#openCount");
const doneCount = document.querySelector("#doneCount");

function loadTodos() {
  try {
    const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
    state.todos = Array.isArray(saved) ? saved : [];
  } catch {
    state.todos = [];
  }
}

function saveTodos() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(state.todos));
}

function createId() {
  return crypto.randomUUID ? crypto.randomUUID() : String(Date.now());
}

function normalizeTodo(raw) {
  return {
    id: raw.id || createId(),
    title: String(raw.title || "").trim(),
    description: String(raw.description || "").trim(),
    relevance: ["hoch", "mittel", "niedrig"].includes(raw.relevance) ? raw.relevance : "mittel",
    status: ["offen", "in-arbeit", "erledigt"].includes(raw.status) ? raw.status : "offen",
    due: String(raw.due || ""),
    category: String(raw.category || "").trim(),
    createdAt: raw.createdAt || new Date().toISOString(),
    updatedAt: new Date().toISOString(),
  };
}

function getVisibleTodos() {
  const query = state.query.toLowerCase();

  return state.todos
    .filter((todo) => {
      const matchesStatus = state.status === "alle" || todo.status === state.status;
      const searchable = `${todo.title} ${todo.description} ${todo.category}`.toLowerCase();
      return matchesStatus && searchable.includes(query);
    })
    .sort((a, b) => {
      if (state.sort === "dueAsc") {
        return (a.due || "9999-12-31").localeCompare(b.due || "9999-12-31");
      }

      if (state.sort === "relevanceDesc") {
        return relevanceWeight[b.relevance] - relevanceWeight[a.relevance];
      }

      return new Date(b.createdAt) - new Date(a.createdAt);
    });
}

function formatStatus(status) {
  return {
    offen: "Offen",
    "in-arbeit": "In Arbeit",
    erledigt: "Erledigt",
  }[status];
}

function formatDate(date) {
  if (!date) return "Keine";
  return new Intl.DateTimeFormat("de-CH").format(new Date(`${date}T12:00:00`));
}

function render() {
  const visibleTodos = getVisibleTodos();
  todoList.replaceChildren();

  totalCount.textContent = state.todos.length;
  openCount.textContent = state.todos.filter((todo) => todo.status !== "erledigt").length;
  doneCount.textContent = state.todos.filter((todo) => todo.status === "erledigt").length;
  emptyState.hidden = visibleTodos.length > 0;

  for (const todo of visibleTodos) {
    const node = template.content.firstElementChild.cloneNode(true);

    node.dataset.id = todo.id;
    node.querySelector("h3").textContent = todo.title;
    node.querySelector(".description").textContent = todo.description || "Keine Beschreibung";
    node.querySelector(".due").textContent = formatDate(todo.due);
    node.querySelector(".category").textContent = todo.category || "Keine";

    const relevance = node.querySelector(".relevance");
    relevance.textContent = `Relevanz: ${todo.relevance}`;
    relevance.dataset.level = todo.relevance;

    const status = node.querySelector(".status");
    status.textContent = formatStatus(todo.status);
    status.dataset.status = todo.status;

    node.querySelector(".edit-btn").addEventListener("click", () => startEdit(todo.id));
    node.querySelector(".delete-btn").addEventListener("click", () => deleteTodo(todo.id));
    todoList.append(node);
  }
}

function resetForm() {
  form.reset();
  todoId.value = "";
  relevanceInput.value = "mittel";
  statusInput.value = "offen";
  submitBtn.textContent = "Hinzufügen";
  cancelEditBtn.hidden = true;
}

function startEdit(id) {
  const todo = state.todos.find((item) => item.id === id);
  if (!todo) return;

  todoId.value = todo.id;
  titleInput.value = todo.title;
  descriptionInput.value = todo.description;
  relevanceInput.value = todo.relevance;
  statusInput.value = todo.status;
  dueInput.value = todo.due;
  categoryInput.value = todo.category;
  submitBtn.textContent = "Speichern";
  cancelEditBtn.hidden = false;
  titleInput.focus();
}

function deleteTodo(id) {
  const todo = state.todos.find((item) => item.id === id);
  if (!todo) return;

  const confirmed = confirm(`Aufgabe "${todo.title}" wirklich löschen?`);
  if (!confirmed) return;

  state.todos = state.todos.filter((item) => item.id !== id);
  saveTodos();
  render();
}

function exportTodos() {
  const payload = {
    app: "maturarbeit-todo",
    version: 1,
    exportedAt: new Date().toISOString(),
    todos: state.todos,
  };
  const blob = new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" });
  const link = document.createElement("a");
  const stamp = new Date().toISOString().slice(0, 10);

  link.href = URL.createObjectURL(blob);
  link.download = `maturarbeit-todos-${stamp}.json`;
  link.click();
  URL.revokeObjectURL(link.href);
}

function importTodos(file) {
  const reader = new FileReader();

  reader.addEventListener("load", () => {
    try {
      const parsed = JSON.parse(reader.result);
      const imported = Array.isArray(parsed) ? parsed : parsed.todos;

      if (!Array.isArray(imported)) {
        throw new Error("Keine Todo-Liste gefunden.");
      }

      state.todos = imported
        .map(normalizeTodo)
        .filter((todo) => todo.title.length > 0);
      saveTodos();
      resetForm();
      render();
    } catch (error) {
      alert(`Import fehlgeschlagen: ${error.message}`);
    } finally {
      importInput.value = "";
    }
  });

  reader.readAsText(file);
}

form.addEventListener("submit", (event) => {
  event.preventDefault();

  const id = todoId.value;
  const existing = state.todos.find((todo) => todo.id === id);
  const todo = normalizeTodo({
    id: id || createId(),
    title: titleInput.value,
    description: descriptionInput.value,
    relevance: relevanceInput.value,
    status: statusInput.value,
    due: dueInput.value,
    category: categoryInput.value,
    createdAt: existing?.createdAt,
  });

  if (!todo.title) return;

  if (existing) {
    state.todos = state.todos.map((item) => (item.id === id ? todo : item));
  } else {
    state.todos.unshift(todo);
  }

  saveTodos();
  resetForm();
  render();
});

cancelEditBtn.addEventListener("click", resetForm);

searchInput.addEventListener("input", () => {
  state.query = searchInput.value.trim();
  render();
});

statusFilter.addEventListener("change", () => {
  state.status = statusFilter.value;
  render();
});

sortInput.addEventListener("change", () => {
  state.sort = sortInput.value;
  render();
});

exportBtn.addEventListener("click", exportTodos);

importInput.addEventListener("change", () => {
  const file = importInput.files[0];
  if (file) importTodos(file);
});

loadTodos();
render();
