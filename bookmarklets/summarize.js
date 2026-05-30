javascript:(async function () {
    /* 1. Request notification permission early */
    if (typeof Notification !== 'undefined' && Notification.permission === 'default') {
        Notification.requestPermission();
    }

    /* 2. Create and show Spinner */
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
                stream: true
            })
        });

        if (!response.ok) throw new Error('API request failed');

        /* 3. Open output window immediately for streaming */
        const html = `<!DOCTYPE html>
<html>
<head>
  <title>Summarized Content</title>
  <meta charset="UTF-8">
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"><\/script>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
  <style>
    body { box-sizing: border-box; min-width: 200px; max-width: 980px; margin: 0 auto; padding: 45px; }
    @media (max-width: 767px) { body { padding: 15px; } }
    @keyframes blink { 0%, 100% { opacity: 1; } 50% { opacity: 0; } }
    #cursor { display: inline-block; width: 2px; height: 1em; background: #333; margin-left: 2px; vertical-align: text-bottom; animation: blink 1s step-end infinite; }
  </style>
</head>
<body class="markdown-body">
  <div id="content"></div><span id="cursor"></span>
  <script>
    window.rawText = '';
    window.updateContent = function(text) {
      window.rawText = text;
      document.getElementById('content').innerHTML = marked.parse(text);
    };
    window.streamDone = function() {
      var cursor = document.getElementById('cursor');
      if (cursor) cursor.remove();
    };
  <\/script>
</body>
</html>`;

        const blob = new Blob([html], {type: 'text/html'});
        const win = window.open(URL.createObjectURL(blob), '_blank');

        /* 4. Parse SSE stream */
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let accumulated = '';
        let buffer = '';

        while (true) {
            const {done, value} = await reader.read();
            if (done) break;

            buffer += decoder.decode(value, {stream: true});
            const lines = buffer.split('\n');
            buffer = lines.pop();

            for (const line of lines) {
                if (!line.startsWith('data: ')) continue;
                const payload = line.slice(6).trim();
                if (payload === '[DONE]') break;
                try {
                    const event = JSON.parse(payload);
                    if (event.type === 'response.output_text.delta' && event.delta) {
                        accumulated += event.delta;
                        if (win && !win.closed && win.updateContent) {
                            win.updateContent(accumulated);
                        }
                    }
                } catch (e) { /* skip unparseable lines */ }
            }
        }

        /* 5. Finalize rendering */
        if (win && !win.closed) {
            if (win.updateContent) win.updateContent(accumulated);
            if (win.streamDone) win.streamDone();
        }

        /* 6. Send browser notification */
        if (typeof Notification !== 'undefined' && Notification.permission === 'granted') {
            new Notification('Summary Ready', { body: 'Your summary has been generated.' });
        }

    } catch (err) {
        alert('Error: ' + err.message);
    } finally {
        /* 7. Remove Spinner */
        const el = document.getElementById('bm-loader');
        if (el) el.remove();
    }
})();
