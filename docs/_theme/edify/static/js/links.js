(function () {
  var links = document.querySelectorAll("main a.reference.external");
  for (var i = 0; i < links.length; i++) {
    var link = links[i];
    link.setAttribute("target", "_blank");
    link.setAttribute("rel", "noopener noreferrer");
    link.classList.add("ext-link");
  }
})();
