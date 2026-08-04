(function () {
  var btn = document.querySelector(".theme-toggle");
  if (!btn) return;
  btn.addEventListener("click", function () {
    var cur = document.documentElement.getAttribute("data-theme");
    var next = cur === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    try { localStorage.setItem("edify-theme", next); } catch (e) {}
  });
})();
