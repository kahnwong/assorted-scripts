javascript: (function () {
    const linksSelector = 'div#bookmark-list-container ul.bookmark-list li div.content div.title a';
    const links = document.querySelectorAll(linksSelector);

    links.forEach(link => {
        window.open(link.href, '_blank');
    });
})();
