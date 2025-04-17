javascript: (function () {
    const linksSelector = 'html.dark-theme body.index div#main main div#content ol.entries.collection li div.card-stacked div.card-content a.card-title.dot-ellipsis.dot-resize-update';
    const links = document.querySelectorAll(linksSelector);

    links.forEach(link => {
        window.open(link.href, '_blank');
    });
})();
