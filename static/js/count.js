(function () {
  const KEY = "empireReads";
  // Merge existing stored counts into current page's bucket for the chapter slug.
  const slug = (document.body && document.body.getAttribute("data-chapter")) || "";
  if (!slug) return;

  function getStored() {
    try { return JSON.parse(localStorage.getItem(KEY) || "{}"); } catch {
      return {};
    }
  }
  function setStored(v) {
    try { localStorage.setItem(KEY, JSON.stringify(v)); } catch {}
  }

  const data = getStored();
  if (!data[slug]) data[slug] = 0;
  data[slug] += 1;
  setStored(data);
})();
