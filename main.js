
  (async () => {
    try {
    const params = new URLSearchParams(location.search);
    const story = params.get('story') || 'legend';
    const chapterNum = parseInt(params.get('chapter') || '1', 10);

    let STORY_NAMES = {};
    let PREFIXES = {};
    try {
      const cfg = await fetch('/empire-chronicle/stories-config.json?v=' + Date.now());
      if (cfg.ok) {
        const j = await cfg.json();
        STORY_NAMES = j.names || {};
        PREFIXES = j.prefixes || {};
      }
    } catch (e) { /* ignore */ }

    // Fix back-button based on current story
    document.getElementById('idx-btn').href = '/empire-chronicle/stories/' + story + '/index.html';
    document.getElementById('footer-idx-btn').href = '/empire-chronicle/stories/' + story + '/index.html';
    // story title

    document.getElementById('story-title').textContent = STORY_NAMES[story] || story;

    const shortLabel = (t) => {
      if (!t) return '';
      const s = String(t);
      const m = s.match(/第[^·:：]*[章篇][^:：]*/);   // 抓中文「第X章/篇…」
      if (m) return m[0];
      const m2 = s.match(/\bChapter\s+\d+\b/i);       // 英文 Chapter N
      if (m2) return m2[0];
      return s;
    };

    let chapters = [];
    try {
      const r = await fetch('/empire-chronicle/stories/' + story + '/chapters.json?v=' + Date.now());
      if (r.ok) chapters = await r.json();
    } catch (e) { /* ignore */ }

    const cur = chapters.find(c => parseInt(c.chapter, 10) === chapterNum);
    const chapterLabel = cur ? cleanTitle(cur.title) : 'no title';
    document.getElementById('chapter-label').textContent = chapterLabel;
    document.title = (STORY_NAMES[story] || story) + ' — ' + chapterLabel;

    const prefix = PREFIXES[story] || 'ch';
    const fileName = prefix + String(chapterNum).padStart(2, '0') + '.md';

    let text = '';
    try {
      const res = await fetch('https://raw.githubusercontent.com/benextralife/empire-chronicle/main/stories/' + story + '/' + fileName + '?v=' + Date.now());
      if (!res.ok) {
        document.getElementById('article').textContent = '本章尚未釋出或檔案不存在 (HTTP ' + res.status + ')';
        return;
      }
      text = await res.text();
    } catch (e) {
      document.getElementById('article').textContent = '載入失敗 (fetch): ' + e.message;
      return;
    }

    let body = text.replace(/^---[\s\S]*?---/, '').trim();

    function cleanTitle(t) {
      if (!t || !t.trim()) return 'no title';
      t = t.trim();
      // If title starts with chapter marker, return as-is
      if (t.startsWith('第') || /^Chapter\s/i.test(t)) return t;
      // Strip leading story-name prefix (everything before the first 第 or Chapter N)
      var i = t.indexOf('第');
      var j = t.search(/Chapter\s+\d+/i);
      if (j >= 0 && (i < 0 || j < i)) i = j;
      if (i >= 0) return t.substring(i);
      // Fallback: strip up to first dot or colon
      var s = t;
      var dot = s.indexOf('·');
      var colon = s.indexOf(':');
      if (dot >= 0 && (colon < 0 || dot < colon)) s = s.substring(dot + 1).trim();
      else if (colon >= 0) s = s.substring(colon + 1).trim();
      return s || 'no title';
    }

    function mdToHtml(md) {
      let h = md.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
      h = h.replace(/^### (.+)$/gm, '<h3>$1</h3>');
      h = h.replace(/^## (.+)$/gm, '<h2>$1</h2>');
      h = h.replace(/^# (.+)$/gm, '<h1>$1</h1>');
      h = h.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
      // author uses *X* as word-rhythm punctuation: strip quotes, no extra space
      h = h.replace(/\*([^*\n]+?)\*/g, '$1'); // strip *word*, no extra space
      h = h.replace(/^---$/gm, '<hr>');
      h = h.replace(/^> (.+)$/gm, '<blockquote>$1</blockquote>');
      h = h.replace(/```([\s\S]*?)```/g, '<pre><code>$1</code></pre>');
      h = h.replace(/^\* (.+)$/gm, '<li>$1</li>');
      return h.split(/\n\n+/).map(p => {
        p = p.trim();
        if (!p) return '';
        if (p.startsWith('<h') || p.startsWith('<hr') || p.startsWith('<pre') || p.startsWith('<blockquote') || p.startsWith('<li')) {
          if (p.startsWith('<li>')) return '<ul>' + p + '</ul>';
          return p;
        }
        return '<p>' + p.replace(/\n/g, '<br>') + '</p>';
      }).join('');
    }

    try {
      document.getElementById('article').innerHTML = mdToHtml(body) || '<div class="empty">本篇尚無正文內容敬請期待。</div>';
    } catch (e) {
      document.getElementById('article').textContent = '渲染失敗: ' + e.message;
    }

    const nav = document.getElementById('nav');
    const prevCh = chapters.find(c => parseInt(c.chapter, 10) === chapterNum - 1);
    const nextCh = chapters.find(c => parseInt(c.chapter, 10) === chapterNum + 1);
    if (prevCh) {
      const a = document.createElement('a');
      a.className = 'ch-btn';
      a.href = '?story=' + story + '&chapter=' + prevCh.chapter;
      a.textContent = '← ' + cleanTitle(prevCh.title);
      nav.appendChild(a);
    }
    if (nextCh) {
      const a = document.createElement('a');
      a.className = 'ch-btn';
      a.href = '?story=' + story + '&chapter=' + nextCh.chapter;
      a.textContent = cleanTitle(nextCh.title) + ' →';
      nav.appendChild(a);
    }
    } catch (err) {
      const art = document.getElementById('article');
      if (art) art.textContent = 'Error: ' + err.message;
      console.error(err);
    }
  })();
  