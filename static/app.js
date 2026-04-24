// VECO CRM client-side JS — kanban drag/drop only.
(function () {
  const cards = document.querySelectorAll(".kanban-card");
  const cols = document.querySelectorAll(".kanban-col");
  if (!cards.length) return;

  let draggingId = null;

  cards.forEach((card) => {
    card.addEventListener("dragstart", (e) => {
      draggingId = card.dataset.id;
      card.classList.add("dragging");
      e.dataTransfer.effectAllowed = "move";
      e.dataTransfer.setData("text/plain", draggingId);
    });
    card.addEventListener("dragend", () => {
      card.classList.remove("dragging");
      draggingId = null;
      cols.forEach((c) => c.classList.remove("drop-target"));
    });
  });

  cols.forEach((col) => {
    col.addEventListener("dragover", (e) => {
      e.preventDefault();
      col.classList.add("drop-target");
    });
    col.addEventListener("dragleave", (e) => {
      // Only remove if leaving the column entirely
      if (!col.contains(e.relatedTarget)) col.classList.remove("drop-target");
    });
    col.addEventListener("drop", async (e) => {
      e.preventDefault();
      col.classList.remove("drop-target");
      const id = e.dataTransfer.getData("text/plain") || draggingId;
      const stage = col.dataset.stage;
      if (!id || !stage) return;
      try {
        const res = await fetch(`/api/opportunities/${id}/stage`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ stage }),
        });
        if (res.ok) {
          window.location.reload();
        } else {
          alert("Couldn't update stage.");
        }
      } catch (err) {
        alert("Network error: " + err.message);
      }
    });
  });
})();
