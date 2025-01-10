javascript: (function () {
    const linksSelector = 'li.item-meta-icons-external-url a';
    const links = document.querySelectorAll(linksSelector);

    // Open each valid link in a new tab
    links.forEach(link => {
        window.open(link.href, '_blank');
    });

    // // Show feedback about how many links were opened
    // alert(`Opened ${links.length} links in new tabs`);
})();
