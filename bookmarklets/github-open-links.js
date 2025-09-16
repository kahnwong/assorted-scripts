javascript: (function () {
    const linksSelector = 'article a';
    const links = document.querySelectorAll(linksSelector);

    links.forEach(link => {
        window.open(link.href, '_blank');
    });
})();
