javascript: (function () {
  const linksSelector = "div.vp-doc li a";
  const links = document.querySelectorAll(linksSelector);

  links.forEach((link) => {
    window.open(link.href, "_blank");
  });
})();
