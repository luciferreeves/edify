(function () {
  "use strict";

  var navToggle = document.querySelector(".nav-toggle");
  var navLinks = document.querySelector(".navlinks");
  var sidenavToggle = document.querySelector(".sidenav-toggle");
  var sidenav = document.querySelector(".sidenav");

  function wire(button, target, openClass) {
    if (!button || !target) {
      return null;
    }
    function setOpen(open) {
      target.classList.toggle(openClass, open);
      button.setAttribute("aria-expanded", open ? "true" : "false");
    }
    button.addEventListener("click", function (event) {
      event.stopPropagation();
      setOpen(!target.classList.contains(openClass));
    });
    return setOpen;
  }

  var toggleLabel = document.querySelector(".sidenav-toggle-label");
  var currentEntry = sidenav && sidenav.querySelector("a.current");
  if (toggleLabel && currentEntry) {
    toggleLabel.textContent = currentEntry.textContent.trim();
  }

  var setNavOpen = wire(navToggle, navLinks, "navlinks-open");
  var setSideOpen = wire(sidenavToggle, sidenav, "sidenav-open");

  function closeAll() {
    if (setNavOpen) {
      setNavOpen(false);
    }
    if (setSideOpen) {
      setSideOpen(false);
    }
  }

  document.addEventListener("click", function (event) {
    if (navLinks && navLinks.contains(event.target)) {
      return;
    }
    if (sidenav && sidenav.contains(event.target) && event.target.tagName !== "A") {
      return;
    }
    closeAll();
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      closeAll();
    }
  });

  window.addEventListener("resize", closeAll);
})();
