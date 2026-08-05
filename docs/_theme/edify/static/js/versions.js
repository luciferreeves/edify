(function () {
  "use strict";

  var DISPLAY_NAMES = { latest: "Latest" };

  var switcher = document.querySelector(".version-switcher");
  var button = switcher && switcher.querySelector(".version-button");
  var name = switcher && switcher.querySelector(".version-name");
  var menu = switcher && switcher.querySelector(".version-menu");
  var list = switcher && switcher.querySelector(".version-list");
  var credit = document.querySelector(".footer-rtd");

  if (!switcher || !button || !name || !menu || !list) {
    return;
  }

  document.addEventListener("readthedocs-addons-data-ready", function (event) {
    var data = event.detail.data();
    var versions = (data.versions && data.versions.active) || [];
    var current = data.versions && data.versions.current;
    if (!versions.length) {
      return;
    }
    render(versions, current ? current.slug : null);
    if (credit) {
      credit.hidden = false;
    }
  });

  function displayName(slug) {
    return DISPLAY_NAMES[slug] || slug;
  }

  function render(versions, currentSlug) {
    name.textContent = displayName(currentSlug || versions[0].slug);
    list.replaceChildren();
    versions.forEach(function (version) {
      list.appendChild(itemFor(version, version.slug === currentSlug));
    });
    switcher.hidden = false;
  }

  function itemFor(version, isCurrent) {
    var item = document.createElement("li");
    var link = document.createElement("a");
    link.href = version.urls.documentation;
    link.textContent = displayName(version.slug);
    if (isCurrent) {
      link.classList.add("current");
      link.setAttribute("aria-current", "true");
    }
    item.appendChild(link);
    return item;
  }

  function setOpen(open) {
    menu.hidden = !open;
    button.setAttribute("aria-expanded", open ? "true" : "false");
  }

  button.addEventListener("click", function (event) {
    event.stopPropagation();
    setOpen(menu.hidden);
  });

  document.addEventListener("click", function (event) {
    if (!menu.hidden && !switcher.contains(event.target)) {
      setOpen(false);
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && !menu.hidden) {
      setOpen(false);
      button.focus();
    }
  });
})();
