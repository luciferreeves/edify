(function () {
  var main = document.querySelector("main.content");
  if (!main) return;
  var url = main.getAttribute("data-api-url");
  if (!url) return;
  var h1 = main.querySelector("h1");
  if (!h1) return;
  var row = document.createElement("div");
  row.className = "title-row";
  h1.parentNode.insertBefore(row, h1);
  row.appendChild(h1);
  var pill = document.createElement("a");
  pill.className = "api-pill";
  pill.setAttribute("href", url);
  pill.textContent = "API reference";
  row.appendChild(pill);
})();
