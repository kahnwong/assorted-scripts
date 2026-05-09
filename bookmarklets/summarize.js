javascript:(async function () {
    /* 1. Create and show Spinner */
    const loader = document.createElement('div');
    loader.id = 'bm-loader';
    loader.innerHTML = `
    <div style="position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.5);z-index:999999;display:flex;flex-direction:column;align-items:center;justify-content:center;color:white;font-family:sans-serif;">
      <div style="width:50px;height:50px;border:5px solid #f3f3f3;border-top:5px solid #3498db;border-radius:50%;animation:spin 1s linear infinite;"></div>
      <p style="margin-top:15px;font-weight:bold;">Bonsai is thinking...</p>
      <style>@keyframes spin{0%{transform:rotate(0deg)}100%{transform:rotate(360deg)}}</style>
    </div>`;
    document.body.appendChild(loader);

    const article = document.querySelector('article') || document.querySelector('[role="main"]') || document.body;
    const articleText = article.innerText || article.textContent;

    try {
        const response = await fetch('http://localhost:13305/v1/responses', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            targetAddressSpace: 'local',
            body: JSON.stringify({
                model: "Bonsai-1.7B-gguf",
                input: "Please summarize the text using precise and concise language. Use headers and bulleted lists in the summary, to make it scannable. Maintain the meaning and factual accuracy. " + articleText,
                stream: false
            })
        });

        if (!response.ok) throw new Error('API request failed');

        const data = await response.json();
        const resultMarkdown = data.output[0].content[0].text;

        /* 2. Build HTML with Markdown Parser (Marked.js) */
        const html = `
      <!DOCTYPE html>
      <html>
      <head>
        <title>Summarized Content</title>
        <meta charset="UTF-8">
        <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
        <style>
          body { box-sizing: border-box; min-width: 200px; max-width: 980px; margin: 0 auto; padding: 45px; }
          @media (max-width: 767px) { body { padding: 15px; } }
        </style>
      </head>
      <body class="markdown-body">
        <div id="content"></div>
        <script>
          /* Inject the markdown into the container */
          document.getElementById('content').innerHTML = marked.parse(\`${resultMarkdown.replace(/\\/g, '\\\\').replace(/`/g, '\\`').replace(/\${/g, '\\${')}\`);
        </script>
      </body>
      </html>
    `;

        const blob = new Blob([html], {type: 'text/html'});
        window.open(URL.createObjectURL(blob), '_blank');

    } catch (err) {
        alert('Error: ' + err.message);
    } finally {
        /* 3. Remove Spinner */
        const el = document.getElementById('bm-loader');
        if (el) el.remove();
    }
})();