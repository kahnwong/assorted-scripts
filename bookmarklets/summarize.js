javascript:(async function () {
    const article = document.querySelector('article') || document.querySelector('[role="main"]') || document.body;
    const articleText = article.innerText || article.textContent;

    /* 1. Open output window immediately with streaming container */
    const html = `
      <!DOCTYPE html>
      <html>
      <head>
        <title>Summarized Content</title>
        <meta charset="UTF-8">
        <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"><\/script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.2.0/github-markdown.min.css">
        <style>
          body { box-sizing: border-box; min-width: 200px; max-width: 980px; margin: 0 auto; padding: 45px; }
          @media (max-width: 767px) { body { padding: 15px; } }
          #streaming-cursor { display: inline-block; width: 8px; height: 1em; background: #3498db; animation: blink 0.7s infinite; vertical-align: text-bottom; margin-left: 2px; }
          @keyframes blink { 0%,100% { opacity: 1; } 50% { opacity: 0; } }
        </style>
      </head>
      <body class="markdown-body">
        <div id="content"></div>
        <span id="streaming-cursor"></span>
        <script>
          window.appendText = function(text) {
            var el = document.getElementById('content');
            el.textContent += text;
          };
          window.finalRender = function() {
            var el = document.getElementById('content');
            var raw = el.textContent;
            el.innerHTML = marked.parse(raw);
            var cursor = document.getElementById('streaming-cursor');
            if (cursor) cursor.remove();
          };
        <\/script>
      </body>
      </html>
    `;

    const blob = new Blob([html], {type: 'text/html'});
    const outputWin = window.open(URL.createObjectURL(blob), '_blank');

    if (!outputWin) {
        alert('Popup blocked. Please allow popups for this site.');
        return;
    }

    /* Wait for the output window to load */
    await new Promise(resolve => {
        const check = setInterval(() => {
            if (outputWin.document && outputWin.document.readyState === 'complete') {
                clearInterval(check);
                resolve();
            }
        }, 50);
    });

    try {
        /* 2. Send streaming request */
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

        /* 3. Read SSE stream and append text deltas */
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';

        while (true) {
            const {done, value} = await reader.read();
            if (done) break;

            buffer += decoder.decode(value, {stream: true});
            const lines = buffer.split('\n');
            buffer = lines.pop();

            for (const line of lines) {
                if (!line.startsWith('data: ')) continue;
                const data = line.slice(6).trim();
                if (data === '[DONE]') continue;

                try {
                    const event = JSON.parse(data);
                    if (event.type === 'response.output_text.delta' && event.delta) {
                        if (outputWin && !outputWin.closed && outputWin.appendText) {
                            outputWin.appendText(event.delta);
                        }
                    }
                } catch (e) {
                    /* skip unparseable lines */
                }
            }
        }

        /* 4. Final markdown render */
        if (outputWin && !outputWin.closed && outputWin.finalRender) {
            outputWin.finalRender();
        }

    } catch (err) {
        if (outputWin && !outputWin.closed) {
            outputWin.document.getElementById('content').textContent = 'Error: ' + err.message;
            var cursor = outputWin.document.getElementById('streaming-cursor');
            if (cursor) cursor.remove();
        } else {
            alert('Error: ' + err.message);
        }
    }
})();
