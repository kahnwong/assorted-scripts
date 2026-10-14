javascript: (function () {
  const linksSelector = "div#content.content div.bookmark-card div.bookmark-card--title h3 a";
  const links = document.querySelectorAll(linksSelector);

  links.forEach((link) => {
    window.open(link.href, "_blank");
  });
})();
