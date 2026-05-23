(function () {
  const root = document.documentElement;
  const button = document.querySelector(".theme-toggle");
  const storageKey = "mod30-residue-lanes-theme";

  function applyTheme(theme) {
    root.setAttribute("data-theme", theme);

    if (button) {
      button.textContent = theme === "dark" ? "light mode" : "dark mode";
      button.setAttribute(
        "aria-label",
        theme === "dark" ? "Switch to light mode" : "Switch to dark mode"
      );
    }
  }

  const savedTheme = localStorage.getItem(storageKey);
  const prefersDark = window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches;

  applyTheme(savedTheme || (prefersDark ? "dark" : "light"));

  if (button) {
    button.addEventListener("click", function () {
      const current = root.getAttribute("data-theme") || "light";
      const next = current === "dark" ? "light" : "dark";
      localStorage.setItem(storageKey, next);
      applyTheme(next);
    });
  }
})();
