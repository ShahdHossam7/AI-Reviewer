<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>AI Code Reviewer — README</title>
  <style>
    :root{
      --bg:#0f1720; --card:#0b1220; --muted:#9aa7bf; --accent:#4A90E2; --glass: rgba(255,255,255,0.03);
      --container: 900px;
      color-scheme: dark;
    }
    html,body{height:100%; margin:0; font-family:Inter,ui-sans-serif,system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial; background:linear-gradient(180deg,#071022 0%, #08142a 100%); color:#e6eef8}
    .wrap{max-width:var(--container); margin:48px auto; padding:28px; background:linear-gradient(180deg, rgba(255,255,255,0.02), rgba(255,255,255,0.01)); border-radius:12px; box-shadow: 0 6px 30px rgba(2,6,23,0.6); border:1px solid rgba(255,255,255,0.03)}
    header{display:flex; gap:16px; align-items:center}
    .logo{
      width:64px; height:64px; border-radius:8px; display:flex; align-items:center; justify-content:center; background:linear-gradient(135deg,#1b2b4a,#103358);
      box-shadow: inset 0 -6px 18px rgba(0,0,0,0.4);
      font-weight:700; font-size:18px; color:#fff;
    }
    h1{margin:0; font-size:26px}
    p.lead{margin:6px 0 20px; color:var(--muted); max-width:70%}
    .badges{display:flex; gap:8px; flex-wrap:wrap; margin-top:10px}
    .badge{background:var(--glass); padding:6px 10px; border-radius:999px; color:var(--muted); font-size:13px; border:1px solid rgba(255,255,255,0.02)}
    section{margin-top:22px}
    h2{font-size:16px; margin:0 0 12px; color:#d9ecff}
    pre.code{background:#071226; padding:16px; border-radius:8px; overflow:auto; border:1px solid rgba(255,255,255,0.02); color:#cfe8ff}
    ul{margin:8px 0 0 20px; color:var(--muted)}
    .grid{display:grid; grid-template-columns:1fr 260px; gap:18px}
    .card{background:linear-gradient(180deg, rgba(255,255,255,0.012), transparent); padding:16px; border-radius:10px; border:1px solid rgba(255,255,255,0.02)}
    a.link{color:var(--accent); text-decoration:none; font-weight:600}
    footer{margin-top:26px; color:var(--muted); font-size:13px}
    @media (max-width:900px){ .grid{grid-template-columns:1fr} p.lead{max-width:100%} }
  </style>
</head>
<body>
  <div class="wrap">
    <header>
      <div class="logo">AI</div>
      <div>
        <h1>AI Code Reviewer</h1>
        <p class="lead">A Streamlit web application that reviews Python code using an LLM model and returns structured JSON issues with line references and suggestions.</p>
        <div class="badges">
          <div class="badge">Streamlit</div>
          <div class="badge">Hugging Face</div>
          <div class="badge">Python</div>
          <div class="badge">MIT License</div>
        </div>
      </div>
    </header>

    <div class="grid" style="margin-top:20px">
      <main>
        <section>
          <h2>Features</h2>
          <ul>
            <li>Upload or paste Python code for review</li>
            <li>Automated code review powered by an LLM model</li>
            <li>Strict JSON-formatted output only (issue list with line numbers and suggestions)</li>
            <li>Raw model output available for debugging</li>
            <li>Easy deployment on Streamlit Cloud</li>
          </ul>
        </section>

        <section>
          <h2>Installation</h2>
          <pre class="code">git clone https://github.com/your-username/ai-code-reviewer.git
cd ai-code-reviewer
pip install -r requirements.txt</pre>
        </section>

        <section>
          <h2>Run Locally</h2>
          <pre class="code">streamlit run app.py

# Open: http://localhost:8501</pre>
        </section>

        <section>
          <h2>Deployment (Streamlit Cloud)</h2>
          <ol style="color:var(--muted); margin:0 0 0 20px; padding:0">
            <li>Push this repository to GitHub</li>
            <li>Go to <a class="link" href="https://share.streamlit.io" target="_blank" rel="noopener">share.streamlit.io</a></li>
            <li>Create a new app and select your repository</li>
            <li>Set the main file path to <code>app.py</code> and deploy</li>
          </ol>
        </section>

        <section>
          <h2>Project Structure</h2>
          <pre class="code">ai-code-reviewer/
├─ app.py
├─ requirements.txt
└─ README.html</pre>
        </section>

        <section>
          <h2>Model</h2>
          <p style="color:var(--muted)">This app uses the <code>Qwen/Qwen2.5-Coder-1.5B-Instruct</code> model via Hugging Face Transformers. Adjust the model identifier in <code>app.py</code> as needed.</p>
        </section>

        <section>
          <h2>License</h2>
          <p style="color:var(--muted)">MIT License — feel free to use, modify, and share.</p>
        </section>
      </main>

      <aside>
        <div class="card">
          <h2>Quick Commands</h2>
          <pre class="code"># Install
pip install -r requirements.txt

# Run
streamlit run app.py</pre>

          <h2 style="margin-top:14px">Environment</h2>
          <p style="color:var(--muted)">Recommended Python 3.9+ and a CUDA-enabled environment if using GPU with PyTorch.</p>

          <h2 style="margin-top:14px">Notes</h2>
          <ul>
            <li>Ensure <code>requirements.txt</code> is present for deployment.</li>
            <li>Streamlit Cloud will install dependencies automatically from <code>requirements.txt</code>.</li>
          </ul>
        </div>
      </aside>
    </div>

    <footer>
      <div>Created for <strong>AI Code Reviewer</strong>. Replace repository links and badges with actual values before publishing.</div>
    </footer>
  </div>
</body>
</html>
