javascript: (function () {
    const linksSelector = 'div#main main div#content form ol.entries.collection div.card-preview a';
    const links = document.querySelectorAll(linksSelector);

    links.forEach(link => {
        window.open(link.href, '_blank');
    });
})();
