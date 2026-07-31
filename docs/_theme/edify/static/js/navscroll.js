(function () {
  var containers = document.querySelectorAll(".sidenav, .api-nav");
  for (var i = 0; i < containers.length; i++) {
    var container = containers[i];
    var active =
      container.querySelector("a.current") ||
      container.querySelector("li.current > a") ||
      container.querySelector(".current");
    if (!active) continue;
    var containerBox = container.getBoundingClientRect();
    var activeBox = active.getBoundingClientRect();
    var alreadyVisible =
      activeBox.top >= containerBox.top && activeBox.bottom <= containerBox.bottom;
    if (alreadyVisible) continue;
    container.scrollTop += activeBox.top - containerBox.top - containerBox.height / 3;
  }
})();
