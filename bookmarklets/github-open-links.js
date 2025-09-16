javascript: (function () {
    const linksSelector = 'article a';
    const links = document.querySelectorAll(linksSelector);

    links.forEach(link => {
        let newHref = link.href;
        if (newHref.startsWith('https://github.com')) {
            newHref = newHref.replace('https://github.com', 'http://192.168.1.36:3000');
        }
        window.open(newHref, '_blank');
    });
})();
