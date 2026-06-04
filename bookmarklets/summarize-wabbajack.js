javascript:(async function () {
    const article = document.querySelector('article') || document.querySelector('[role="main"]') || document.body;
    const articleText = article.innerText || article.textContent;

    const encodedText = encodeURIComponent(articleText);
    window.location.href = `http://localhost:3000/?text=${encodedText}&summarize=1`;
})();
