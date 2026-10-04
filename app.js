// app.js - Fast Offline Math Formatter, Interactive Checkpoints & Simulators

// Balanced delimiter helper for nested braces { ... }
function parseBalanced(str, startIdx) {
  let depth = 0;
  let start = -1;
  for (let i = startIdx; i < str.length; i++) {
    if (str[i] === '{') {
      if (depth === 0) start = i;
      depth++;
    } else if (str[i] === '}') {
      depth--;
      if (depth === 0) return { start, end: i, content: str.substring(start + 1, i) };
    }
  }
  return null;
}

function parseFractions(str) {
  let idx = str.indexOf('\\frac');
  let safeguard = 0;
  while (idx !== -1 && safeguard++ < 100) {
    const firstArg = parseBalanced(str, idx);
    if (!firstArg) break;
    const secondArg = parseBalanced(str, firstArg.end + 1);
    if (!secondArg) break;

    const num = parseFractions(firstArg.content);
    const den = parseFractions(secondArg.content);
    const replacement = `<span class="m-frac"><span class="m-num">${num}</span><span class="m-den">${den}</span></span>`;
    str = str.substring(0, idx) + replacement + str.substring(secondArg.end + 1);
    idx = str.indexOf('\\frac');
  }
  return str;
}

function parseRoots(str) {
  let idx = str.indexOf('\\sqrt');
  let safeguard = 0;
  while (idx !== -1 && safeguard++ < 100) {
    const arg = parseBalanced(str, idx);
    if (!arg) break;
    const inner = parseRoots(arg.content);
    const replacement = `<span class="m-sqrt">&radic;<span class="m-rad">${inner}</span></span>`;
    str = str.substring(0, idx) + replacement + str.substring(arg.end + 1);
    idx = str.indexOf('\\sqrt');
  }
  return str;
}

function parseEnvironments(str) {
  // bmatrix, matrix, pmatrix, cases
  return str.replace(/\\begin\{(bmatrix|matrix|pmatrix|cases)\}([\s\S]*?)\\end\{\1\}/g, (match, env, body) => {
    const rows = body.trim().split(/\\\\|\\cr/).map(r => r.trim()).filter(r => r.length > 0);
    const trs = rows.map(r => {
      const cells = r.split('&').map(c => `<td style="padding:2px 8px; text-align:left;">${nativeRenderMath(c.trim())}</td>`).join('');
      return `<tr>${cells}</tr>`;
    }).join('');

    let borderStyle = 'border-left:2px solid #111; border-right:2px solid #111; border-radius:3px;';
    if (env === 'pmatrix') borderStyle = 'border-left:1px solid #666; border-right:1px solid #666; border-radius:8px;';
    if (env === 'cases') borderStyle = 'border-left:2px solid #111; border-radius:0; padding-left:4px;';
    return `<table class="math-matrix" style="display:inline-table; ${borderStyle} margin:0 4px; vertical-align:middle;"><tbody>${trs}</tbody></table>`;
  });
}

function parseBinom(str) {
  let idx = str.indexOf('\\binom');
  let safeguard = 0;
  while (idx !== -1 && safeguard++ < 50) {
    const nArg = parseBalanced(str, idx);
    if (!nArg) break;
    const kArg = parseBalanced(str, nArg.end + 1);
    if (!kArg) break;

    const n = nativeRenderMath(nArg.content);
    const k = nativeRenderMath(kArg.content);
    const replacement = `<span class="m-frac">(<span class="m-num" style="font-size:0.85em;">${n}</span><span class="m-den" style="border:none; font-size:0.85em;">${k}</span>)</span>`;
    str = str.substring(0, idx) + replacement + str.substring(kArg.end + 1);
    idx = str.indexOf('\\binom');
  }
  return str;
}

function parseStacked(str) {
  let idx = str.indexOf('\\stackrel');
  let safeguard = 0;
  while (idx !== -1 && safeguard++ < 50) {
    const topArg = parseBalanced(str, idx);
    if (!topArg) break;
    const baseArg = parseBalanced(str, topArg.end + 1);
    if (!baseArg) break;

    const top = nativeRenderMath(topArg.content);
    const base = nativeRenderMath(baseArg.content);
    const replacement = `<span class="m-frac"><span class="m-num" style="font-size:0.75em;">${top}</span><span class="m-den" style="border:none;">${base}</span></span>`;
    str = str.substring(0, idx) + replacement + str.substring(baseArg.end + 1);
    idx = str.indexOf('\\stackrel');
  }
  return str;
}

function parseArrows(str) {
  let idx = str.indexOf('\\xrightarrow');
  let safeguard = 0;
  while (idx !== -1 && safeguard++ < 50) {
    const arg = parseBalanced(str, idx);
    if (!arg) break;
    const content = nativeRenderMath(arg.content);
    const replacement = `<span class="m-arr" style="display:inline-flex; flex-direction:column; align-items:center; vertical-align:middle;"><span style="font-size:0.75em;">${content}</span><span>&rarr;</span></span>`;
    str = str.substring(0, idx) + replacement + str.substring(arg.end + 1);
    idx = str.indexOf('\\xrightarrow');
  }
  return str;
}

function parseAccents(str) {
  ['hat', 'bar', 'tilde'].forEach(acc => {
    let tag = acc === 'hat' ? '&#770;' : (acc === 'bar' ? '&#772;' : '&#771;');
    let idx = str.indexOf('\\' + acc);
    let safeguard = 0;
    while (idx !== -1 && safeguard++ < 100) {
      const arg = parseBalanced(str, idx);
      if (arg) {
        const inner = nativeRenderMath(arg.content);
        const replacement = `<span class="m-accent">${inner}${tag}</span>`;
        str = str.substring(0, idx) + replacement + str.substring(arg.end + 1);
      } else {
        const nextChar = str[idx + acc.length + 1];
        if (nextChar && nextChar !== ' ' && nextChar !== '\\') {
          str = str.substring(0, idx) + nextChar + tag + str.substring(idx + acc.length + 2);
        } else {
          break;
        }
      }
      idx = str.indexOf('\\' + acc);
    }
  });
  return str;
}

function nativeRenderMath(formula) {
  if (!formula) return "";
  let s = String(formula).trim();

  // 1. Matrix & cases environments first
  s = parseEnvironments(s);

  // 2. Normalize double backslashes
  s = s.replace(/\\\\+/g, '\\');

  // 3. Normalize escapes
  s = s.replace(/[\r\n]+(nabla|nu)/g, '\\$1');
  s = s.replace(/[\r\n\t]+(to|theta|times|tau)/g, '\\$1');
  s = s.replace(/[\x0c]+(frac)/g, '\\$1');
  s = s.replace(/[\x08]+(beta)/g, '\\$1');

  // 4. Balanced parsers
  s = parseFractions(s);
  s = parseRoots(s);
  s = parseBinom(s);
  s = parseStacked(s);
  s = parseArrows(s);
  s = parseAccents(s);

  // 5. Nested formatting tags
  for (let k = 0; k < 3; k++) {
    s = s.replace(/\\text\{([^}]+)\}/g, '<span class="m-text">$1</span>');
    s = s.replace(/\\mathbf\{([^}]+)\}/g, '<strong>$1</strong>');
    s = s.replace(/\\boldsymbol\{([^}]+)\}/g, '<strong><em>$1</em></strong>');
  }

  // 6. Blackboard bold & Calligraphic
  s = s.replace(/\\mathbb\{R\}/g, '&#8477;');
  s = s.replace(/\\mathbb\{N\}/g, '&#8469;');
  s = s.replace(/\\mathbb\{E\}/g, '&#120124;');
  s = s.replace(/\\mathbb\{I\}/g, '&#120128;');
  s = s.replace(/\\mathbb\{Z\}/g, '&#8484;');
  s = s.replace(/\\mathbb\{P\}/g, '&#8473;');
  s = s.replace(/\\mathbb\{([A-Z])\}/g, '<strong>$1</strong>');

  s = s.replace(/\\mathcal\{L\}/g, '&#8466;');
  s = s.replace(/\\mathcal\{D\}/g, '&#119967;');
  s = s.replace(/\\mathcal\{N\}/g, '&#119977;');
  s = s.replace(/\\mathcal\{T\}/g, '&#119983;');
  s = s.replace(/\\mathcal\{X\}/g, '&#119987;');
  s = s.replace(/\\mathcal\{Y\}/g, '&#119988;');
  s = s.replace(/\\mathcal\{H\}/g, '&#8459;');
  s = s.replace(/\\mathcal\{([A-Za-z]+)\}/g, '<em style="font-family:serif; font-style:italic;">$1</em>');

  // 7. Delimiters
  s = s.replace(/\\left[.|(\[]?/g, '');
  s = s.replace(/\\right[.|)\]]?/g, '');
  s = s.replace(/\\(big|Big|bigg|Bigg)[lmr]?/g, '');
  s = s.replace(/\\\{/g, '{');
  s = s.replace(/\\\}/g, '}');
  s = s.replace(/\\\|/g, '‖');

  // 8. Symbol dictionary
  const dict = [
    [/\\Longleftrightarrow/g, '&hArr;'],
    [/\\iff/g, '&hArr;'],
    [/\\implies/g, '&rArr;'],
    [/\\longrightarrow/g, '&rarr;'],
    [/\\rightarrow|\\to/g, '&rarr;'],
    [/\\leftarrow/g, '&larr;'],

    [/\\vdots/g, '&#8942;'],
    [/\\ddots/g, '&#8945;'],
    [/\\dots|\\cdots|\\ldots/g, '&hellip;'],

    [/\\approx/g, '&asymp;'],
    [/\\sim/g, '&sim;'],
    [/\\propto/g, '&prop;'],
    [/\\equiv/g, '&equiv;'],
    [/\\triangleq/g, '&#8796;'],
    [/\\le/g, '&le;'],
    [/\\ge/g, '&ge;'],
    [/\\ll/g, '&#8810;'],
    [/\\gg/g, '&#8811;'],
    [/\\neq|\\ne/g, '&ne;'],
    [/\\in/g, '&isin;'],
    [/\\notin/g, '&notin;'],
    [/\\cap/g, '&cap;'],
    [/\\cup/g, '&cup;'],
    [/\\subset/g, '&sub;'],
    [/\\subseteq/g, '&sube;'],
    [/\\forall/g, '&forall;'],
    [/\\exists/g, '&exist;'],
    [/\\neg/g, '&not;'],
    [/\\land/g, '&and;'],
    [/\\lor/g, '&or;'],
    [/\\parallel/g, '&#8741;'],
    [/\\mid/g, '|'],
    [/\\circ/g, '&#9702;'],
    [/\\ell/g, '&#8467;'],

    [/\\nabla/g, '&nabla;'],
    [/\\partial/g, '&part;'],
    [/\\Delta/g, '&Delta;'],
    [/\\Sigma/g, '&Sigma;'],
    [/\\Pi/g, '&Pi;'],
    [/\\Phi/g, '&Phi;'],
    [/\\Omega/g, '&Omega;'],
    [/\\alpha/g, '&alpha;'],
    [/\\beta/g, '&beta;'],
    [/\\gamma/g, '&gamma;'],
    [/\\delta/g, '&delta;'],
    [/\\epsilon|\\varepsilon/g, '&epsilon;'],
    [/\\theta/g, '&theta;'],
    [/\\eta/g, '&eta;'],
    [/\\lambda/g, '&lambda;'],
    [/\\mu/g, '&mu;'],
    [/\\xi/g, '&xi;'],
    [/\\pi/g, '&pi;'],
    [/\\sigma/g, '&sigma;'],
    [/\\tau/g, '&tau;'],
    [/\\phi/g, '&phi;'],

    [/\\times/g, '&times;'],
    [/\\cdot/g, '&sdot;'],
    [/\\odot/g, '&#8857;'],
    [/\\pm/g, '&plusmn;'],
    [/\\sum/g, '<span class="m-op">&sum;</span>'],
    [/\\prod/g, '<span class="m-op">&prod;</span>'],
    [/\\int/g, '<span class="m-op">&int;</span>'],
    [/\\infty/g, '&infin;'],

    [/\\log/g, 'log'],
    [/\\ln/g, 'ln'],
    [/\\exp/g, 'exp'],
    [/\\max/g, 'max'],
    [/\\min/g, 'min'],
    [/\\arg/g, 'arg'],
    [/\\cos/g, 'cos'],
    [/\\sin/g, 'sin'],
    [/\\tan/g, 'tan'],
    [/\\tanh/g, 'tanh'],
    [/\\det/g, 'det'],
    [/\\dim/g, 'dim'],
    [/\\lim/g, 'lim'],
    [/\\inf/g, 'inf'],

    [/\\lceil/g, '⌈'],
    [/\\rceil/g, '⌉'],
    [/\\lfloor/g, '⌊'],
    [/\\rfloor/g, '⌋'],
    [/\\quad/g, '&emsp;'],
    [/\\qquad/g, '&emsp;&emsp;'],
    [/\\[,; ]/g, '&nbsp;']
  ];

  for (const [re, rep] of dict) {
    s = s.replace(re, rep);
  }

  // 9. Subscripts & Superscripts
  s = s.replace(/_\{([^}]+)\}/g, '<sub>$1</sub>');
  s = s.replace(/\^\{([^}]+)\}/g, '<sup>$1</sup>');
  s = s.replace(/_([a-zA-Z0-9\+\-\*])/g, '<sub>$1</sub>');
  s = s.replace(/\^([a-zA-Z0-9\+\-\*])/g, '<sup>$1</sup>');

  return `<span class="math">${s}</span>`;
}

// Master Math Formatter: uses KaTeX if available, otherwise bulletproof native engine
function renderMathFormula(formula) {
  if (!formula) return "";
  const s = String(formula).trim();
  if (typeof window !== "undefined" && window.katex && typeof window.katex.renderToString === "function") {
    try {
      return window.katex.renderToString(s, { throwOnError: false, displayMode: false });
    } catch (e) {
      // fallback
    }
  }
  return nativeRenderMath(s);
}

// Helper to escape HTML in code blocks
function escapeHtml(str) {
  return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
}

// Single-pass Python Syntax Highlighter (Lightweight, Zero-Dependency, High-Contrast)
function highlightPython(code) {
  if (!code) return "";
  const tokenRegex = /("""[\s\S]*?"""|'''[\s\S]*?'''|f?"(?:\\.|[^"\\])*"|f?'(?:\\.|[^'\\])*'|#[^\n]*|@\w+|\b\d+(?:\.\d+)?(?:[eE][+-]?\d+)?\b|\b(?:def|class|return|if|elif|else|for|while|in|is|not|and|or|import|from|as|try|except|finally|with|yield|lambda|pass|break|continue|raise|True|False|None)\b|\b(?:torch|nn|optim|F|tf|keras|layers|models|sklearn|np|pd|plt|Linear|Conv2d|Conv2D|BatchNorm2d|BatchNormalization|Dropout|Sequential|LinearRegression|Ridge|Lasso|SGDRegressor|LogisticRegression|DecisionTreeClassifier|RandomForestClassifier|SVC|KNeighborsClassifier|KMeans|PCA|CountVectorizer|TfidfVectorizer|StandardScaler|MinMaxScaler|GridSearchCV|MultinomialNB|CosineSimilarity|Adam|SGD|RMSprop|CrossEntropyLoss|MSELoss|BCEWithLogitsLoss|Softmax|Sigmoid|ReLU|LeakyReLU|DataLoader|Dataset)\b|\b(?:print|len|range|enumerate|zip|map|filter|sum|min|max|abs|round|int|float|str|list|dict|set|tuple|type|isinstance|shape|dtype|device|squeeze|unsqueeze|reshape|item|numpy|tensor|cat|stack|fit|predict|predict_proba|fit_transform|transform|score|backward|step|zero_grad|toarray|mean|var|std|dot|cos|sin|exp|log|sqrt|zeros|ones|eye|arange|linspace|matmul)\b)/g;

  let lastIndex = 0;
  let html = "";
  let match;

  while ((match = tokenRegex.exec(code)) !== null) {
    const preText = code.slice(lastIndex, match.index);
    if (preText) html += escapeHtml(preText);

    const token = match[0];
    if (token.startsWith("#")) {
      html += '<span class="tok-comment">' + escapeHtml(token) + '</span>';
    } else if (token.startsWith('"') || token.startsWith("'") || token.startsWith('f"') || token.startsWith("f'")) {
      html += '<span class="tok-string">' + escapeHtml(token) + '</span>';
    } else if (token.startsWith("@")) {
      html += '<span class="tok-decorator">' + escapeHtml(token) + '</span>';
    } else if (/^\d/.test(token)) {
      html += '<span class="tok-number">' + escapeHtml(token) + '</span>';
    } else if (/^(?:def|class|return|if|elif|else|for|while|in|is|not|and|or|import|from|as|try|except|finally|with|yield|lambda|pass|break|continue|raise|True|False|None)$/.test(token)) {
      html += '<span class="tok-keyword">' + escapeHtml(token) + '</span>';
    } else if (/^(?:torch|nn|optim|F|tf|keras|layers|models|sklearn|np|pd|plt|Linear|Conv2d|Conv2D|BatchNorm2d|BatchNormalization|Dropout|Sequential|LinearRegression|Ridge|Lasso|SGDRegressor|LogisticRegression|DecisionTreeClassifier|RandomForestClassifier|SVC|KNeighborsClassifier|KMeans|PCA|CountVectorizer|TfidfVectorizer|StandardScaler|MinMaxScaler|GridSearchCV|MultinomialNB|CosineSimilarity|Adam|SGD|RMSprop|CrossEntropyLoss|MSELoss|BCEWithLogitsLoss|Softmax|Sigmoid|ReLU|LeakyReLU|DataLoader|Dataset)$/.test(token)) {
      html += '<span class="tok-type">' + escapeHtml(token) + '</span>';
    } else {
      html += '<span class="tok-builtin">' + escapeHtml(token) + '</span>';
    }

    lastIndex = tokenRegex.lastIndex;
  }

  const remaining = code.slice(lastIndex);
  if (remaining) html += escapeHtml(remaining);

  return html;
}

function renderHighlightedCodeBlock(code, lang = "python") {
  const codeId = "code-" + Math.random().toString(36).substring(2, 9);
  const cleanLang = (lang || "python").toLowerCase().trim();
  const displayLang = cleanLang === "py" ? "PYTHON" : (cleanLang ? cleanLang.toUpperCase() : "PYTHON");

  let highlighted = cleanLang === "output" || cleanLang === "text" || cleanLang === "bash" 
    ? escapeHtml(code.trim()) 
    : highlightPython(code.trim());

  return `
    <div class="code-block-wrap">
      <div class="code-block-header">
        <div class="code-header-left">
          <div class="code-mac-dots">
            <span class="code-mac-dot red"></span>
            <span class="code-mac-dot yellow"></span>
            <span class="code-mac-dot green"></span>
          </div>
          <span class="code-lang-label">${displayLang}</span>
        </div>
        <button class="copy-code-btn" data-target="${codeId}">
          <span>📋 Sao chép</span>
        </button>
      </div>
      <pre class="code-block" id="${codeId}"><code>${highlighted}</code></pre>
    </div>
  `;
}

function formatContent(text) {
  if (!text) return "";
  let s = Array.isArray(text) ? text.join("\n\n") : String(text);

  // 1. Protect multi-line code blocks from inline Markdown & Math parsers
  const codeBlocks = [];
  s = s.replace(/```([a-zA-Z0-9_-]*)\s*\n([\s\S]*?)```/g, (m, lang, code) => {
    const placeholder = `@@@ML_CODE_BLOCK_${codeBlocks.length}@@@`;
    codeBlocks.push(renderHighlightedCodeBlock(code, lang));
    return placeholder;
  });

  // 2. Protect display math ($$ ... $$)
  const mathBlocks = [];
  s = s.replace(/\$\$([\s\S]+?)\$\$/g, (m, formula) => {
    const placeholder = `@@@ML_MATH_BLOCK_${mathBlocks.length}@@@`;
    mathBlocks.push(`<div class="formula-block">${renderMathFormula(formula)}</div>`);
    return placeholder;
  });

  // 3. Inline Markdown code `...`
  s = s.replace(/`([^`\n]+)`/g, '<code>$1</code>');

  // 4. Markdown Bold
  s = s.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');

  // 5. Markdown Italic
  s = s.replace(/(^|[^\*])\*([^\*\n]+)\*([^\*]|$)/g, '$1<em>$2</em>$3');

  // 6. Inline Math ($ ... $)
  s = s.replace(/\$([^$\n]+?)\$/g, (m, formula) => {
    return renderMathFormula(formula);
  });

  // 7. Restore protected math blocks
  mathBlocks.forEach((block, idx) => {
    s = s.replace(`@@@ML_MATH_BLOCK_${idx}@@@`, block);
  });

  // 8. Restore protected code blocks
  codeBlocks.forEach((block, idx) => {
    s = s.replace(`@@@ML_CODE_BLOCK_${idx}@@@`, block);
  });

  return s;
}

// Markdown block parser for deep pedagogical text
function renderMarkdownBlock(text) {
  if (!text) return "";
  const lines = String(text).trim().split("\n");
  let out = [];
  let i = 0;

  while (i < lines.length) {
    const rawLine = lines[i];
    const trimmed = rawLine.trim();

    if (!trimmed) {
      i++;
      continue;
    }

    // 1. Multi-line Code Block: ```lang ... ```
    if (trimmed.startsWith("```")) {
      const lang = trimmed.substring(3).trim() || "python";
      let codeLines = [];
      i++;
      while (i < lines.length && !lines[i].trim().startsWith("```")) {
        codeLines.push(lines[i]);
        i++;
      }
      i++; // skip closing ```
      out.push(renderHighlightedCodeBlock(codeLines.join("\n"), lang));
      continue;
    }

    // 2. Markdown Table: starts and ends with |
    if (trimmed.startsWith("|") && trimmed.endsWith("|")) {
      let tableLines = [];
      while (i < lines.length && lines[i].trim().startsWith("|") && lines[i].trim().endsWith("|")) {
        tableLines.push(lines[i].trim());
        i++;
      }
      if (tableLines.length >= 2) {
        const parseRow = (row) => row.slice(1, -1).split("|").map(c => c.trim());
        const headers = parseRow(tableLines[0]);
        let startRow = 1;
        // Check if row 1 is separator |---|---|
        if (tableLines[1].includes("---")) {
          startRow = 2;
        }
        let ths = headers.map(h => `<th>${formatContent(h)}</th>`).join("");
        let trs = "";
        for (let r = startRow; r < tableLines.length; r++) {
          const cells = parseRow(tableLines[r]);
          const tds = cells.map(c => `<td>${formatContent(c)}</td>`).join("");
          trs += `<tr>${tds}</tr>`;
        }
        out.push(`<div class="table-responsive"><table class="table-minimal"><thead><tr>${ths}</tr></thead><tbody>${trs}</tbody></table></div>`);
        continue;
      }
    }

    // 3. Blockquote: starts with >
    if (trimmed.startsWith(">")) {
      let quoteLines = [];
      while (i < lines.length && lines[i].trim().startsWith(">")) {
        quoteLines.push(lines[i].trim().replace(/^>\s?/, ""));
        i++;
      }
      out.push(`<blockquote class="deep-quote">${formatContent(quoteLines.join("<br>"))}</blockquote>`);
      continue;
    }

    // 4. Subheadings: ### or ####
    if (trimmed.startsWith("### ")) {
      out.push(`<h3 class="deep-h3">${formatContent(trimmed.substring(4))}</h3>`);
      i++;
      continue;
    }
    if (trimmed.startsWith("#### ")) {
      out.push(`<h4 class="deep-h4">${formatContent(trimmed.substring(5))}</h4>`);
      i++;
      continue;
    }

    // 5. Unordered List: starts with - or *
    if (trimmed.startsWith("- ") || trimmed.startsWith("* ")) {
      let items = [];
      while (i < lines.length && (lines[i].trim().startsWith("- ") || lines[i].trim().startsWith("* "))) {
        items.push(`<li>${formatContent(lines[i].trim().substring(2))}</li>`);
        i++;
      }
      out.push(`<ul class="deep-ul">${items.join("")}</ul>`);
      continue;
    }

    // 6. Ordered List: starts with 1. 2.
    if (/^\d+\.\s/.test(trimmed)) {
      let items = [];
      while (i < lines.length && /^\d+\.\s/.test(lines[i].trim())) {
        const itemContent = lines[i].trim().replace(/^\d+\.\s+/, "");
        items.push(`<li>${formatContent(itemContent)}</li>`);
        i++;
      }
      out.push(`<ol class="deep-ol">${items.join("")}</ol>`);
      continue;
    }

    // 7. Regular paragraph
    out.push(`<p class="deep-p">${formatContent(trimmed)}</p>`);
    i++;
  }

  return out.join("\n");
}

const renderMath = formatContent;

function initVAIOApp() {
  // Safe localStorage helper for file:// and cross-origin environments
  const safeStorage = {
    getItem: (key) => {
      try { return localStorage.getItem(key); } catch (e) { return null; }
    },
    setItem: (key, val) => {
      try { localStorage.setItem(key, val); } catch (e) {}
    },
    removeItem: (key) => {
      try { localStorage.removeItem(key); } catch (e) {}
    }
  };

  // Persistent States
  let currentLessonIndex = 0;
  let currentView = "lesson";
  let completedLessons = JSON.parse(safeStorage.getItem("ml_completed_lessons") || safeStorage.getItem("vaio_completed") || "[]");
  let checkpointAnswers = JSON.parse(safeStorage.getItem("ml_checkpoint_answers") || "{}");
  let quizAnswers = JSON.parse(safeStorage.getItem("ml_quiz_answers") || "{}");

  // DOM Elements
  const lessonNavEl = document.getElementById("lessonNav");
  const articleContainerEl = document.getElementById("articleContainer");
  const quizContainerEl = document.getElementById("quizContainer");
  const breadcrumbEl = document.getElementById("breadcrumbText");
  const progressTextEl = document.getElementById("progressText");
  const progressBarFillEl = document.getElementById("progressBarFill");
  const searchInputEl = document.getElementById("searchInput");
  const toggleQuizBtn = document.getElementById("toggleQuizBtn");
  const sidebarEl = document.getElementById("sidebar");
  const sidebarToggleBtn = document.getElementById("sidebarToggleBtn");
  const sidebarCloseBtn = document.getElementById("sidebarCloseBtn");
  const sidebarBackdropEl = document.getElementById("sidebarBackdrop");
  const resetProgressBtn = document.getElementById("resetProgressBtn");

  function closeMobileSidebar() {
    if (sidebarEl) sidebarEl.classList.remove("open");
    if (sidebarBackdropEl) sidebarBackdropEl.classList.remove("active");
  }

  function openMobileSidebar() {
    if (sidebarEl) sidebarEl.classList.add("open");
    if (sidebarBackdropEl) sidebarBackdropEl.classList.add("active");
  }

  // Desktop & Mobile Sidebar Toggle
  if (sidebarToggleBtn) {
    sidebarToggleBtn.addEventListener("click", () => {
      if (window.innerWidth > 860) {
        document.body.classList.toggle("sidebar-collapsed");
        const isCollapsed = document.body.classList.contains("sidebar-collapsed");
        safeStorage.setItem("ml_sidebar_collapsed", isCollapsed ? "1" : "0");
        sidebarToggleBtn.setAttribute("title", isCollapsed ? "Hiện danh mục bài học (Sidebar)" : "Ẩn danh mục bài học (Sidebar)");
      } else {
        if (sidebarEl && sidebarEl.classList.contains("open")) {
          closeMobileSidebar();
        } else {
          openMobileSidebar();
        }
      }
    });
  }

  if (sidebarCloseBtn) {
    sidebarCloseBtn.addEventListener("click", () => {
      if (window.innerWidth > 860) {
        document.body.classList.add("sidebar-collapsed");
        safeStorage.setItem("ml_sidebar_collapsed", "1");
        if (sidebarToggleBtn) sidebarToggleBtn.setAttribute("title", "Hiện danh mục bài học (Sidebar)");
      } else {
        closeMobileSidebar();
      }
    });
  }

  // Restore desktop sidebar collapsed state
  if (window.innerWidth > 860 && safeStorage.getItem("ml_sidebar_collapsed") === "1") {
    document.body.classList.add("sidebar-collapsed");
    if (sidebarToggleBtn) sidebarToggleBtn.setAttribute("title", "Hiện danh mục bài học (Sidebar)");
  }

  if (sidebarBackdropEl) {
    sidebarBackdropEl.addEventListener("click", closeMobileSidebar);
  }

  // Diagram Modal Close Handlers
  const diagramModal = document.getElementById("diagramModal");
  const diagramModalClose = document.getElementById("diagramModalClose");
  const diagramModalBackdrop = document.getElementById("diagramModalBackdrop");

  function closeDiagramModal() {
    if (diagramModal) {
      diagramModal.classList.remove("active");
      document.body.style.overflow = "";
    }
  }

  if (diagramModalClose) diagramModalClose.addEventListener("click", closeDiagramModal);
  if (diagramModalBackdrop) diagramModalBackdrop.addEventListener("click", closeDiagramModal);
  window.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeDiagramModal();
  });

  // Scroll to Top FAB Handler
  const scrollTopBtn = document.getElementById("scrollTopBtn");
  if (scrollTopBtn) {
    scrollTopBtn.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
    window.addEventListener("scroll", () => {
      if (window.scrollY > 300) {
        scrollTopBtn.style.opacity = "0.92";
        scrollTopBtn.style.pointerEvents = "auto";
      } else {
        scrollTopBtn.style.opacity = "0";
        scrollTopBtn.style.pointerEvents = "none";
      }
    });
  }

  // Font Scale Adjuster (A- / A+)
  const fontScaleDownBtn = document.getElementById("fontScaleDown");
  const fontScaleUpBtn = document.getElementById("fontScaleUp");
  let currentFontScale = parseFloat(safeStorage.getItem("ml_font_scale") || "1.0");

  function applyFontScale(scale) {
    currentFontScale = Math.min(1.4, Math.max(0.85, Math.round(scale * 100) / 100));
    document.documentElement.style.setProperty("--font-scale", currentFontScale.toString());
    safeStorage.setItem("ml_font_scale", currentFontScale.toString());
  }

  // Apply saved font scale immediately
  applyFontScale(currentFontScale);

  if (fontScaleDownBtn) {
    fontScaleDownBtn.addEventListener("click", () => {
      applyFontScale(currentFontScale - 0.08);
    });
  }

  if (fontScaleUpBtn) {
    fontScaleUpBtn.addEventListener("click", () => {
      applyFontScale(currentFontScale + 0.08);
    });
  }

  if (resetProgressBtn) {
    resetProgressBtn.addEventListener("click", () => {
      if (confirm("Bạn có muốn đặt lại toàn bộ tiến trình học và các bài tập trắc nghiệm không?")) {
        safeStorage.removeItem("ml_completed_lessons");
        safeStorage.removeItem("vaio_completed");
        safeStorage.removeItem("ml_current_lesson");
        safeStorage.removeItem("ml_checkpoint_answers");
        safeStorage.removeItem("ml_quiz_answers");
        completedLessons = [];
        checkpointAnswers = {};
        quizAnswers = {};
        updateProgress();
        renderSidebar();
        loadLesson(0);
      }
    });
  }

  // Global Event Delegation for Copy Code & Hands-On Exercises
  document.addEventListener("click", (e) => {
    // 1. Copy Code Button
    const copyBtn = e.target.closest(".copy-code-btn");
    if (copyBtn) {
      const targetId = copyBtn.getAttribute("data-target");
      const targetEl = document.getElementById(targetId);
      if (targetEl) {
        const textToCopy = targetEl.textContent || targetEl.innerText || "";
        navigator.clipboard.writeText(textToCopy).then(() => {
          copyBtn.innerHTML = "<span>✓ Đã chép</span>";
          copyBtn.classList.add("copied");
          setTimeout(() => {
            copyBtn.innerHTML = "<span>📋 Sao chép</span>";
            copyBtn.classList.remove("copied");
          }, 1800);
        }).catch(() => {
          copyBtn.innerHTML = "<span>Lỗi chép</span>";
        });
      }
      return;
    }

    // 2. Exercise Solution Toggle
    const exBtn = e.target.closest(".code-exercise-toggle-btn");
    if (exBtn) {
      const targetId = exBtn.getAttribute("data-ex-id");
      const solBox = document.getElementById(targetId);
      if (solBox) {
        const isHidden = solBox.style.display === "none";
        solBox.style.display = isHidden ? "block" : "none";
        exBtn.textContent = isHidden ? "✕ Ẩn Code Lời Giải" : "📖 Xem Code Lời Giải & Hướng Dẫn Mẫu";
      }
      return;
    }
  });

  function renderSidebar(filtered = null) {
    const list = filtered || LESSONS_DATA;
    let html = "";

    list.forEach((lesson) => {
      const realIndex = LESSONS_DATA.findIndex(l => l.id === lesson.id);
      const isActive = currentView === "lesson" && realIndex === currentLessonIndex;
      const isDone = completedLessons.includes(lesson.id);

      html += `
        <div class="nav-item ${isActive ? 'active' : ''}" data-index="${realIndex}">
          <span>${lesson.title}</span>
          ${isDone ? '<span class="nav-done-check" title="Đã hoàn thành">✓</span>' : ''}
        </div>
      `;
    });

    html += `
      <div class="nav-item quiz-entry ${currentView === 'quiz' ? 'active' : ''}" id="sidebarQuizEntry">
        <span>★ Đề Thi Trắc Nghiệm</span>
        <span class="quiz-badge">${QUIZ_DATA.length} Câu</span>
      </div>
    `;

    lessonNavEl.innerHTML = html;

    lessonNavEl.querySelectorAll(".nav-item").forEach(item => {
      item.addEventListener("click", () => {
        if (item.id === "sidebarQuizEntry") {
          switchView("quiz");
        } else {
          const idx = parseInt(item.getAttribute("data-index"), 10);
          switchView("lesson");
          loadLesson(idx);
        }
        if (window.innerWidth <= 860) {
          closeMobileSidebar();
        }
      });
    });
  }

  function updateProgress() {
    const doneCount = completedLessons.length;
    const totalCount = LESSONS_DATA.length;
    if (progressTextEl) {
      progressTextEl.textContent = `${doneCount}/${totalCount} bài`;
    }
    if (progressBarFillEl) {
      const pct = Math.round((doneCount / totalCount) * 100);
      progressBarFillEl.style.width = `${pct}%`;
    }
  }

  function loadLesson(index) {
    if (index < 0 || index >= LESSONS_DATA.length) return;
    currentLessonIndex = index;
    safeStorage.setItem("ml_current_lesson", index);
    safeStorage.setItem("ml_current_view", "lesson");

    const lesson = LESSONS_DATA[index];

    if (breadcrumbEl) {
      breadcrumbEl.textContent = lesson.title;
    }
    renderSidebar();

    // Calculate reading time estimate (~200 wpm)
    const totalWords = (lesson.summary + " " + (lesson.sections || []).map(s => (s.content || "") + " " + (s.deepDive || "")).join(" ")).split(/\s+/).length;
    const estMinutes = Math.max(10, Math.round(totalWords / 200));

    let html = `
      <header class="article-header">
        <div class="article-meta-badges">
          <span class="meta-pill">Bài ${index + 1} / ${LESSONS_DATA.length}</span>
          <span class="meta-pill">⏱️ ~${estMinutes} phút đọc</span>
          <span class="meta-pill">6 Chuyên đề & Checkpoints</span>
        </div>
        <h1 class="article-title">${lesson.title}</h1>
        <p class="article-summary">${formatContent(lesson.summary)}</p>
      </header>

      <nav class="lesson-quick-toc" aria-label="Mục lục bài học">
        <div class="toc-header">
          <span class="toc-title">📋 CẤU TRÚC 6 CHUYÊN ĐỀ</span>
          <span class="toc-subtitle">Chạm để cuộn nhanh</span>
        </div>
        <div class="toc-grid">
          ${(lesson.sections || []).map((sec, i) => `
            <button type="button" class="toc-item" data-sec-idx="${i}">
              <span class="toc-num">${index + 1}.${i + 1}</span>
              <span class="toc-text">${formatContent(sec.heading.replace(/^\d+\.\d+\.\s*/, ''))}</span>
            </button>
          `).join("")}
        </div>
      </nav>
    `;

    if (lesson.intuition && (lesson.intuition.title || lesson.intuition.content)) {
      const overviewDiag = lesson.overviewDiagram || lesson.intuition.diagram;
      let diagHtml = "";
      if (overviewDiag) {
        const svgContent = typeof overviewDiag === "object" ? overviewDiag.svg : overviewDiag;
        const caption = typeof overviewDiag === "object" ? overviewDiag.caption : "";
        if (svgContent) {
          diagHtml = `
            <div class="diagram-wrapper overview-diagram-wrapper" title="Bấm vào để phóng to chi tiết">
              ${svgContent}
              ${caption ? `<div class="diagram-caption" style="text-align:center; font-size:0.88rem; color:var(--text-muted); margin-top:10px; font-style:italic;">${formatContent(caption)}</div>` : ""}
              <div class="diagram-zoom-hint">🔍 Nhấp vào sơ đồ để phóng to toàn màn hình</div>
            </div>
          `;
        }
      }

      html += `
        <section class="intuition-card">
          <span class="intuition-label">Trực giác thực tế</span>
          <p><strong>${formatContent(lesson.intuition.title || '')}:</strong> ${formatContent(lesson.intuition.content || '')}</p>
          ${diagHtml}
        </section>
      `;
    }

    // Render Subsections
    (lesson.sections || []).forEach((sec, secIdx) => {
      html += `
        <section class="content-section" id="sec-${secIdx}">
          <div class="sec-index-pill">CHUYÊN ĐỀ ${index + 1}.${secIdx + 1}</div>
          <h2 class="section-heading">${formatContent(sec.heading || '')}</h2>
      `;

      if (sec.content) {
        html += `<p class="sec-lead">${formatContent(sec.content)}</p>`;
      }

      if (sec.formula) {
        html += `
          <div class="formula-block">
            ${renderMathFormula(sec.formula)}
          </div>
        `;
      }

      // Math Explainer for Learners
      if (sec.mathExplainer && sec.mathExplainer.length > 0) {
        html += `
          <div class="math-explainer-box">
            <div class="math-explainer-title">
              <span>📐 Giải Mã Ký Hiệu Toán Học</span>
            </div>
            <div class="math-explainer-grid">
              ${sec.mathExplainer.map(item => {
                const sym = item.sym ? renderMathFormula(item.sym) : '';
                const name = item.name ? formatContent(item.name) : '';
                const mean = item.mean ? formatContent(item.mean) : '';
                return `
                  <div class="math-explainer-item">
                    <div class="math-sym">${sym}</div>
                    <div class="math-mean">${name ? `<strong>${name}:</strong> ` : ''}${mean}</div>
                  </div>
                `;
              }).join("")}
            </div>
          </div>
        `;
      }

      // Pedagogical SVG Diagram (Single or Multiple)
      const rawDiagrams = sec.diagrams || (sec.diagram ? [sec.diagram] : (sec.diagramSvg ? [sec.diagramSvg] : []));
      if (rawDiagrams && rawDiagrams.length > 0) {
        rawDiagrams.forEach((diagramObj) => {
          const svgContent = typeof diagramObj === "object" ? diagramObj.svg : diagramObj;
          const caption = typeof diagramObj === "object" ? diagramObj.caption : "";
          if (svgContent) {
            html += `
              <div class="diagram-wrapper" title="Bấm vào để phóng to chi tiết">
                ${svgContent}
                ${caption ? `<div class="diagram-caption" style="text-align:center; font-size:0.86rem; color:var(--text-muted); margin-top:10px; font-style:italic;">${formatContent(caption)}</div>` : ""}
                <div class="diagram-zoom-hint">🔍 Nhấp vào sơ đồ để phóng to toàn màn hình</div>
              </div>
            `;
          }
        });
      }

      // Deep Dive Explanation
      if (sec.deepDive) {
        html += `
          <div class="deepdive-box">
            ${renderMarkdownBlock(sec.deepDive)}
          </div>
        `;
      }

      // Exam Pitfall
      const pitfallText = sec.commonPitfalls || sec.pitfall;
      if (pitfallText) {
        html += `
          <div class="pitfall-box">
            <div class="pitfall-header">⚠️ Cạm Bẫy Phòng Thi & Sai Lầm Thường Gặp</div>
            <div class="pitfall-content">${renderMarkdownBlock(pitfallText)}</div>
          </div>
        `;
      }

      // Interactive Checkpoint
      if (sec.practiceQuestion) {
        const q = sec.practiceQuestion;
        const savedAnswer = checkpointAnswers[`${lesson.id}_${secIdx}`];
        const isAnswered = savedAnswer !== undefined;

        html += `
          <div class="checkpoint-card" id="cp-${secIdx}">
            <div class="checkpoint-header">
              <span class="checkpoint-tag">KIỂM TRA HIỂU BÀI PHẦN ${secIdx + 1}</span>
              ${q.level ? `<span class="checkpoint-level">${formatContent(q.level)}</span>` : ''}
            </div>
            <div class="checkpoint-q-text">${formatContent(q.question)}</div>
            <div class="checkpoint-options">
              ${(q.options || []).map((opt, optIdx) => {
                let optClass = "cp-opt-btn";
                if (isAnswered) {
                  if (optIdx === q.correctIndex) optClass += " correct";
                  else if (optIdx === savedAnswer) optClass += " wrong";
                }
                return `
                  <button class="${optClass}" data-sec="${secIdx}" data-opt="${optIdx}">
                    <span class="cp-opt-label">${['A', 'B', 'C', 'D'][optIdx] || optIdx + 1}</span>
                    <span class="cp-opt-content">${formatContent(opt)}</span>
                  </button>
                `;
              }).join("")}
            </div>
            <div class="checkpoint-feedback" id="cp-feedback-${secIdx}" style="display: ${isAnswered ? 'block' : 'none'};">
              ${isAnswered ? (savedAnswer === q.correctIndex ? '<strong>✓ Chính xác!</strong> Bạn đã làm chủ kiến thức phần này.' : '<strong>✗ Chưa chính xác.</strong> Hãy xem lại lý thuyết hoặc bấm xem lời giải để ôn tập!') : ''}
            </div>
            <div class="checkpoint-actions">
              ${q.hint ? `<button class="btn btn-sm cp-hint-btn" data-sec="${secIdx}">💡 Xem gợi ý</button>` : ''}
              ${q.solution ? `<button class="btn btn-sm cp-solution-btn" data-sec="${secIdx}">📖 Lời giải chi tiết</button>` : ''}
            </div>
            ${q.hint ? `<div class="cp-hint-box" id="cp-hint-${secIdx}" style="display:none;"><strong>Gợi ý:</strong> ${formatContent(q.hint)}</div>` : ''}
            ${q.solution ? `
              <div class="cp-solution-box" id="cp-sol-${secIdx}" style="display: ${isAnswered && savedAnswer === q.correctIndex ? 'block' : 'none'};">
                <strong>Lời giải chuẩn:</strong>
                ${q.solution.explanation ? `<p>${formatContent(q.solution.explanation)}</p>` : ''}
                ${q.solution.steps ? `<ol>${q.solution.steps.map(s => `<li>${formatContent(s)}</li>`).join("")}</ol>` : ''}
              </div>
            ` : ''}
          </div>
        `;
      }

      html += `</section>`;
    });

    // Mount Interactive Simulator Placeholder
    html += `<div id="interactive-widget-mount"></div>`;

    // Hands-On Code Lab: Thực hành Lập trình & Scikit-Learn (Vừa học lý thuyết vừa học thực hành)
    if (lesson.codeLab) {
      const lab = lesson.codeLab;
      html += `
        <section class="code-lab-section">
          <div class="code-lab-header">
            <div class="code-lab-header-left">
              <span class="code-lab-badge">LAB</span>
              <h2 class="code-lab-title">${lab.title || 'Thực Hành Lập Trình & Huấn Luyện Mô Hình'}</h2>
            </div>
          </div>
          ${lab.description ? `<div class="code-lab-desc">${formatContent(lab.description)}</div>` : ''}

          ${(lab.steps || []).map((step, sIdx) => `
            <div class="code-step-card">
              <div class="code-step-header">
                <span class="code-step-num">${sIdx + 1}</span>
                <span>${step.title}</span>
              </div>
              ${step.explanation ? `<div class="code-step-desc">${formatContent(step.explanation)}</div>` : ''}
              ${step.code ? renderHighlightedCodeBlock(step.code, step.lang || 'python') : ''}
              ${step.output ? `
                <div class="code-output-wrap">
                  <div class="code-output-title">▶ Kết Quả Thực Thi (Console Output):</div>
                  <pre style="margin:0; font-family:inherit; color:inherit;">${escapeHtml(step.output.trim())}</pre>
                </div>
              ` : ''}
            </div>
          `).join("")}

          ${lab.exercise ? `
            <div class="code-exercise-card">
              <div class="code-exercise-header">
                <div class="code-exercise-title">
                  <span>🎯 Bài Tập Tự Luyện Thực Chiến:</span>
                  <strong>${lab.exercise.title || 'Tự code & Huấn luyện'}</strong>
                </div>
              </div>
              <div class="code-exercise-task">${formatContent(lab.exercise.task)}</div>
              ${lab.exercise.hint ? `
                <div class="code-exercise-hint">
                  <strong>💡 Gợi ý tư duy:</strong> ${formatContent(lab.exercise.hint)}
                </div>
              ` : ''}
              <div style="margin-top:14px;">
                <button class="code-exercise-toggle-btn" data-ex-id="${lesson.id}-ex">
                  📖 Xem Code Lời Giải & Hướng Dẫn Mẫu
                </button>
              </div>
              <div class="exercise-solution-box" id="${lesson.id}-ex" style="display:none;">
                <div style="font-weight:700; color:#b45309; margin-bottom:10px;">Lời giải chuẩn & Hướng dẫn từng dòng code:</div>
                ${lab.exercise.solutionDesc ? `<div style="margin-bottom:10px; line-height:1.65;">${formatContent(lab.exercise.solutionDesc)}</div>` : ''}
                ${lab.exercise.solutionCode ? renderHighlightedCodeBlock(lab.exercise.solutionCode, 'python') : ''}
              </div>
            </div>
          ` : ''}
        </section>
      `;
    }

    // Exam Connection
    if (lesson.examConnection) {
      html += `
        <section class="content-section">
          <h2 class="section-heading">${lesson.examConnection.questionTitle || 'Phân Tích Dạng Bài Thi Thực Tế'}</h2>
          ${(lesson.examConnection.items || []).map(item => `
            <div class="exam-card">
              <span class="exam-tag">${item.code || 'BÀI TẬP'}</span>
              <div class="exam-q">${formatContent(item.problem || '')}</div>
              <div class="exam-steps">
                <div style="font-weight:700; margin-bottom:8px; color:var(--text);">Lời giải chi tiết & Chiến lược phòng thi:</div>
                ${Array.isArray(item.solution) 
                  ? item.solution.map(s => `<div class="exam-step-line" style="margin-top:8px; line-height:1.65;">${formatContent(s)}</div>`).join("")
                  : `<div style="line-height:1.65;">${formatContent(item.solution || '')}</div>`
                }
              </div>
            </div>
          `).join("")}
        </section>
      `;
    }

    // Key Takeaways
    if (lesson.takeaways && lesson.takeaways.length > 0) {
      html += `
        <div class="takeaways-box">
          <div class="takeaways-header">ĐIỂM CỐT LÕI CẦN GHI NHỚ</div>
          <ul>
            ${lesson.takeaways.map(t => `<li>${formatContent(t)}</li>`).join("")}
          </ul>
        </div>
      `;
    }

    // Navigation Buttons
    const isDone = completedLessons.includes(lesson.id);
    html += `
      <div class="nav-buttons">
        <button class="btn ${isDone ? 'active' : ''}" id="doneBtn">${isDone ? '✓ Đã hoàn thành bài này' : 'Đánh dấu đã học xong'}</button>
        <div class="nav-buttons-row">
          <button class="btn" id="prevBtn" ${index === 0 ? 'disabled' : ''}>← Bài Trước</button>
          <button class="btn" id="nextBtn" ${index === LESSONS_DATA.length - 1 ? 'disabled' : ''}>Bài Sau →</button>
        </div>
      </div>
    `;

    articleContainerEl.innerHTML = html;
    window.scrollTo({ top: 0, behavior: "smooth" });

    // Attach Quick TOC Smooth Scroll Handlers
    articleContainerEl.querySelectorAll(".toc-item").forEach(btn => {
      btn.addEventListener("click", (e) => {
        e.preventDefault();
        const secIdx = btn.getAttribute("data-sec-idx");
        const targetEl = document.getElementById(`sec-${secIdx}`);
        if (targetEl) {
          const topBar = document.querySelector(".top-bar");
          const topBarHeight = topBar ? topBar.offsetHeight : 56;
          const targetRect = targetEl.getBoundingClientRect();
          const offsetPosition = targetRect.top + window.pageYOffset - (topBarHeight + 14);
          window.scrollTo({
            top: Math.max(0, offsetPosition),
            behavior: "smooth"
          });
        }
      });
    });

    // Attach Checkpoint Option Handlers
    articleContainerEl.querySelectorAll(".cp-opt-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const secIdx = parseInt(btn.getAttribute("data-sec"), 10);
        const optIdx = parseInt(btn.getAttribute("data-opt"), 10);
        const sec = lesson.sections[secIdx];
        if (!sec || !sec.practiceQuestion) return;

        const q = sec.practiceQuestion;
        const parentCard = document.getElementById(`cp-${secIdx}`);
        const feedbackEl = document.getElementById(`cp-feedback-${secIdx}`);
        const solEl = document.getElementById(`cp-sol-${secIdx}`);

        // Save progress to local storage
        checkpointAnswers[`${lesson.id}_${secIdx}`] = optIdx;
        safeStorage.setItem("ml_checkpoint_answers", JSON.stringify(checkpointAnswers));

        parentCard.querySelectorAll(".cp-opt-btn").forEach((b, idx) => {
          b.classList.remove("correct", "wrong");
          if (idx === q.correctIndex) {
            b.classList.add("correct");
          } else if (idx === optIdx && optIdx !== q.correctIndex) {
            b.classList.add("wrong");
          }
        });

        if (optIdx === q.correctIndex) {
          feedbackEl.style.display = "block";
          feedbackEl.innerHTML = "<strong>✓ Chính xác!</strong> Bạn đã làm chủ kiến thức phần này.";
          if (solEl) solEl.style.display = "block";
        } else {
          feedbackEl.style.display = "block";
          feedbackEl.innerHTML = "<strong>✗ Chưa chính xác.</strong> Hãy xem lại lý thuyết hoặc bấm xem lời giải để ôn tập!";
        }
      });
    });

    // Attach Hint & Solution Toggle Handlers
    articleContainerEl.querySelectorAll(".cp-hint-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const secIdx = btn.getAttribute("data-sec");
        const hintEl = document.getElementById(`cp-hint-${secIdx}`);
        if (hintEl) {
          hintEl.style.display = (hintEl.style.display === "none") ? "block" : "none";
        }
      });
    });

    articleContainerEl.querySelectorAll(".cp-solution-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const secIdx = btn.getAttribute("data-sec");
        const solEl = document.getElementById(`cp-sol-${secIdx}`);
        if (solEl) {
          solEl.style.display = (solEl.style.display === "none") ? "block" : "none";
        }
      });
    });

    if (lesson.interactiveWidget) {
      mountInteractiveWidget(lesson.interactiveWidget);
    }

        // Attach Diagram Zoom Lightbox Handlers
    articleContainerEl.querySelectorAll(".diagram-wrapper").forEach(wrapper => {
      wrapper.addEventListener("click", (e) => {
        const svgEl = wrapper.querySelector("svg");
        const captionEl = wrapper.querySelector(".diagram-caption");
        const modal = document.getElementById("diagramModal");
        const modalBody = document.getElementById("diagramModalBody");
        const modalCaption = document.getElementById("diagramModalCaption");
        if (modal && modalBody && svgEl) {
          modalBody.innerHTML = svgEl.outerHTML;
          if (modalCaption) {
            modalCaption.textContent = captionEl ? captionEl.textContent : "";
          }
          modal.classList.add("active");
          document.body.style.overflow = "hidden";
        }
      });
    });

    // Attach Copy Code Handlers
    articleContainerEl.querySelectorAll(".copy-code-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        const targetId = btn.getAttribute("data-target");
        const el = document.getElementById(targetId);
        if (el) {
          navigator.clipboard.writeText(el.textContent).then(() => {
            btn.textContent = "✓ Đã chép";
            setTimeout(() => { btn.textContent = "Sao chép"; }, 1800);
          }).catch(() => {
            btn.textContent = "Lỗi chép";
          });
        }
      });
    });

    document.getElementById("prevBtn").addEventListener("click", () => {
      if (currentLessonIndex > 0) loadLesson(currentLessonIndex - 1);
    });
    document.getElementById("nextBtn").addEventListener("click", () => {
      if (currentLessonIndex < LESSONS_DATA.length - 1) loadLesson(currentLessonIndex + 1);
    });
    document.getElementById("doneBtn").addEventListener("click", (e) => {
      const idx = completedLessons.indexOf(lesson.id);
      if (idx > -1) {
        completedLessons.splice(idx, 1);
        e.target.textContent = "Đánh dấu xong";
        e.target.classList.remove("active");
      } else {
        completedLessons.push(lesson.id);
        e.target.textContent = "✓ Đã xong";
        e.target.classList.add("active");
      }
      safeStorage.setItem("ml_completed_lessons", JSON.stringify(completedLessons));
      safeStorage.setItem("vaio_completed", JSON.stringify(completedLessons));
      updateProgress();
      renderSidebar();
    });
  }

  function switchView(view) {
    currentView = view;
    safeStorage.setItem("ml_current_view", view);
    if (view === "lesson") {
      articleContainerEl.style.display = "block";
      quizContainerEl.style.display = "none";
      toggleQuizBtn.textContent = "Đề Thi (24 Câu)";
      toggleQuizBtn.classList.remove("active");
      loadLesson(currentLessonIndex);
    } else {
      articleContainerEl.style.display = "none";
      quizContainerEl.style.display = "block";
      toggleQuizBtn.textContent = "← Xem Bài Học";
      toggleQuizBtn.classList.add("active");
      if (breadcrumbEl) breadcrumbEl.textContent = "Bộ Đề Thi Trắc Nghiệm Học Máy";
      renderSidebar();
      renderQuiz();
    }
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function renderQuizExplanation(text) {
    if (!text) return "";
    const paras = String(text).split(/\n\s*\n/);
    return paras.map(p => {
      p = p.trim();
      if (!p) return "";
      return `<div class="quiz-exp-para" style="margin-top:8px; line-height:1.65;">${formatContent(p.replace(/\n/g, '<br>'))}</div>`;
    }).join("");
  }

  function renderQuiz(filterCat = "all") {
    const cats = ["all", "Deep Learning", "Computer Vision", "Machine Learning", "NLP & LLM", "Calculus", "Clustering", "Evaluation"];

    // Compute live stats
    const totalQ = QUIZ_DATA.length;
    const answeredKeys = Object.keys(quizAnswers);
    let correctCount = 0;
    answeredKeys.forEach(qid => {
      const q = QUIZ_DATA.find(it => it.id === parseInt(qid, 10));
      if (q && quizAnswers[qid] === q.correctIndex) {
        correctCount++;
      }
    });

    let html = `
      <header class="article-header">
        <h1 class="article-title">Bộ Đề Thi Trắc Nghiệm Học Máy</h1>
        <p class="article-summary">${totalQ} câu hỏi thực chiến chuẩn đề thi Olympic AI (VAIO 2025 & VAIC 2026), bao quát toàn diện các chủ đề từ Đạo hàm, Hồi quy, Cây quyết định đến CNN, Transformer và Diffusion. Chọn đáp án để chấm điểm ngay và xem lời giải phân tích cặn kẽ.</p>
        <div class="quiz-score-banner">
          <div class="quiz-score-info">
            <strong>Tiến độ làm bài:</strong> Đã trả lời <strong>${answeredKeys.length}/${totalQ}</strong> câu (${correctCount} câu đúng)
          </div>
          <button class="btn btn-sm" id="resetQuizBtn">Làm lại từ đầu</button>
        </div>
      </header>
      <div class="quiz-filter-bar">
    `;

    cats.forEach(c => {
      html += `<button class="btn ${filterCat === c ? 'active' : ''}" data-cat="${c}">${c === 'all' ? 'Tất cả' : c}</button>`;
    });
    html += `</div><div id="quizList"></div>`;

    quizContainerEl.innerHTML = html;

    const resetBtn = document.getElementById("resetQuizBtn");
    if (resetBtn) {
      resetBtn.addEventListener("click", () => {
        if (confirm("Bạn có muốn xóa toàn bộ câu trả lời để làm lại từ đầu không?")) {
          quizAnswers = {};
          safeStorage.removeItem("ml_quiz_answers");
          renderQuiz(filterCat);
        }
      });
    }

    quizContainerEl.querySelectorAll(".quiz-filter-bar button").forEach(b => {
      b.addEventListener("click", () => renderQuiz(b.getAttribute("data-cat")));
    });

    const filtered = filterCat === "all" ? QUIZ_DATA : QUIZ_DATA.filter(q => q.category === filterCat || q.category.includes(filterCat));
    let cardsHtml = "";
    filtered.forEach(q => {
      const savedSel = quizAnswers[q.id];
      const isAnswered = savedSel !== undefined;

      cardsHtml += `
        <div class="quiz-card" id="qcard-${q.id}">
          <div class="quiz-card-header">
            <span class="quiz-cat-tag">${q.category}</span>
          </div>
          <div class="quiz-q-title">${formatContent(q.question)}</div>
          <div class="quiz-options">
            ${q.options.map((opt, i) => {
              let optClass = "quiz-opt";
              if (isAnswered) {
                if (i === q.correctIndex) optClass += " correct";
                else if (i === savedSel) optClass += " incorrect";
              }
              return `
                <div class="${optClass}" data-qid="${q.id}" data-idx="${i}">
                  <strong>[${['A','B','C','D'][i]}]</strong>
                  <span>${formatContent(opt.substring(3))}</span>
                </div>
              `;
            }).join("")}
          </div>
          <div class="quiz-exp ${isAnswered ? 'show' : ''}" id="qexp-${q.id}">
            <strong style="color:var(--text); font-size:0.95rem;">Đáp án & Giải thích chi tiết từ đề thi:</strong>
            <div class="quiz-exp-body" style="margin-top:6px;">${renderQuizExplanation(q.explanation)}</div>
          </div>
        </div>
      `;
    });

    document.getElementById("quizList").innerHTML = cardsHtml;

    document.querySelectorAll(".quiz-opt").forEach(opt => {
      opt.addEventListener("click", () => {
        const qid = parseInt(opt.getAttribute("data-qid"), 10);
        const selIdx = parseInt(opt.getAttribute("data-idx"), 10);
        const q = QUIZ_DATA.find(it => it.id === qid);
        const card = document.getElementById(`qcard-${qid}`);
        const allOpts = card.querySelectorAll(".quiz-opt");
        const exp = document.getElementById(`qexp-${qid}`);

        // Save to storage
        quizAnswers[qid] = selIdx;
        safeStorage.setItem("ml_quiz_answers", JSON.stringify(quizAnswers));

        allOpts.forEach((o, i) => {
          o.classList.remove("correct", "incorrect");
          if (i === q.correctIndex) o.classList.add("correct");
          else if (i === selIdx) o.classList.add("incorrect");
        });

        exp.classList.add("show");
        renderQuiz(filterCat);
      });
    });
  }

  // Search
  searchInputEl.addEventListener("input", (e) => {
    const q = e.target.value.toLowerCase().trim();
    if (!q) {
      renderSidebar();
      return;
    }
    const filtered = LESSONS_DATA.filter(l => 
      l.title.toLowerCase().includes(q) ||
      l.summary.toLowerCase().includes(q) ||
      (l.examConnection && l.examConnection.items && l.examConnection.items.some(it => it.code.toLowerCase().includes(q) || it.problem.toLowerCase().includes(q)))
    );
    renderSidebar(filtered);
  });

  toggleQuizBtn.addEventListener("click", () => {
    switchView(currentView === "lesson" ? "quiz" : "lesson");
  });

  // Mount Interactive Widgets with matching IDs
  function mountInteractiveWidget(type) {
    const mount = document.getElementById("interactive-widget-mount");
    if (!mount) return;

    if (type === "widget-gradient-descent") {
      mount.innerHTML = `
        <div class="interactive-widget">
          <div class="widget-header">
            <span class="widget-title">Mô Phỏng Gradient Descent</span>
            <span style="font-family:var(--font-mono); font-size:0.75rem;">f(x) = (x - 2)² + 1</span>
          </div>
          <div class="widget-controls">
            <div class="control-group">
              <label>Tốc độ học (η): <span id="lrVal">0.15</span></label>
              <input type="range" id="lrRange" min="0.02" max="1.15" step="0.01" value="0.15">
            </div>
            <div class="control-group">
              <label>Điểm bắt đầu (x₀): <span id="x0Val">-2.5</span></label>
              <input type="range" id="x0Range" min="-4.0" max="0.5" step="0.1" value="-2.5">
            </div>
            <button class="btn" id="stepGDBtn">Bước Tiếp</button>
            <button class="btn" id="autoGDBtn">Tự Động</button>
            <button class="btn" id="resetGDBtn">Đặt Lại</button>
          </div>
          <div class="canvas-wrapper">
            <canvas id="gdCanvas" width="680" height="240"></canvas>
          </div>
          <div class="widget-output" id="gdOutput">Đang khởi tạo...</div>
        </div>
      `;
      initGDWidget();
    } else if (type === "widget-cosine-similarity") {
      mount.innerHTML = `
        <div class="interactive-widget">
          <div class="widget-header">
            <span class="widget-title">Mô Phỏng Cosine Similarity & Vector Không Gian Ngữ Nghĩa</span>
          </div>
          <div class="widget-controls">
            <div class="control-group">
              <label>Góc Vector A: <span id="angleAVal">30°</span></label>
              <input type="range" id="angleARange" min="0" max="360" value="30">
            </div>
            <div class="control-group">
              <label>Góc Vector B: <span id="angleBVal">80°</span></label>
              <input type="range" id="angleBRange" min="0" max="360" value="80">
            </div>
          </div>
          <div class="canvas-wrapper">
            <canvas id="cosCanvas" width="680" height="260"></canvas>
          </div>
          <div class="widget-output" id="cosOutput">Đang tính...</div>
        </div>
      `;
      initCosWidget();
    } else if (type === "widget-naive-bayes") {
      mount.innerHTML = `
        <div class="interactive-widget">
          <div class="widget-header">
            <span class="widget-title">Mô Phỏng Bộ Lọc Naive Bayes & Làm Mịn Laplace</span>
          </div>
          <div class="widget-controls" style="flex-wrap: wrap; gap: 12px;">
            <div class="control-group" style="flex: 2; min-width: 260px;">
              <label>Chọn văn bản thử nghiệm:</label>
              <select id="nbPresetSelect" style="width: 100%; padding: 6px 10px; font-family: Georgia; font-size: 13px; border: 1px solid #111; background: #fff;">
                <option value="d1">Email 1: 'ưu đãi dự án tiền thưởng' (Hỗn hợp Spam & Ham)</option>
                <option value="d2">Email 2: 'tiền thưởng miễn phí ưu đãi' (Đặc sệt Spam)</option>
                <option value="d3">Email 3: 'báo cáo dự án họp lương' (Đặc sệt Ham)</option>
                <option value="d4">Email 4: 'bitcoin khuyến mãi trúng thưởng' (Chứa từ CHƯA TỪNG GẶP)</option>
              </select>
            </div>
            <div class="control-group" style="flex: 1; min-width: 180px;">
              <label>Chế độ làm mịn:</label>
              <label style="display: flex; align-items: center; gap: 8px; font-weight: normal; cursor: pointer; margin-top: 6px;">
                <input type="checkbox" id="nbLaplaceToggle" checked style="width: 16px; height: 16px; accent-color: #111;">
                <span>Bật Laplace (Add-1)</span>
              </label>
            </div>
          </div>
          <div class="canvas-wrapper" style="padding: 16px; background: #fff; border: 1px solid #111; border-top: none;">
            <div id="nbDetailsBox" style="font-family: Georgia; font-size: 13px; line-height: 1.6;"></div>
          </div>
          <div class="widget-output" id="nbOutput">Đang tính toán Naive Bayes...</div>
        </div>
      `;
      initNaiveBayesWidget();
    } else if (type === "widget-linear-regression") {
      mount.innerHTML = `
        <div class="interactive-widget">
          <div class="widget-header">
            <span class="widget-title">Mô Phỏng Hồi Quy Tuyến Tính & Co Rút Regularization</span>
          </div>
          <div class="widget-controls" style="flex-wrap: wrap; gap: 12px;">
            <div class="control-group" style="flex: 1; min-width: 160px;">
              <label>Loại Mô Hình:</label>
              <select id="lrModelType" style="width: 100%; padding: 5px 8px; font-family: Georgia; font-size: 13px; border: 1px solid #111; background: #fff;">
                <option value="ols">Hồi quy OLS Chuẩn (λ = 0)</option>
                <option value="ridge">Ridge Regression (L2)</option>
                <option value="lasso">Lasso Regression (L1)</option>
              </select>
            </div>
            <div class="control-group" style="flex: 1; min-width: 160px;">
              <label>Độ Phạt Regularization λ: <span id="lrLambdaVal">1.0</span></label>
              <input type="range" id="lrLambdaRange" min="0" max="10" step="0.5" value="1.0">
            </div>
            <div class="control-group" style="flex: 1; min-width: 140px; justify-content: flex-end;">
              <label style="display: flex; align-items: center; gap: 8px; font-weight: normal; cursor: pointer; margin-top: 6px;">
                <input type="checkbox" id="lrOutlierToggle" style="width: 16px; height: 16px; accent-color: #111;">
                <span>Thêm Điểm Dị Biệt (Outlier)</span>
              </label>
            </div>
          </div>
          <div class="canvas-wrapper">
            <canvas id="lrCanvas" width="680" height="260"></canvas>
          </div>
          <div class="widget-output" id="lrOutput">Đang tính toán Hồi quy...</div>
        </div>
      `;
      initLinearRegressionWidget();
    } else if (type === "widget-confusion-matrix") {
      mount.innerHTML = `
        <div class="interactive-widget">
          <div class="widget-header">
            <span class="widget-title">Bảng Nhầm Lẫn & Các Chỉ Số Đánh Giá (Confusion Matrix & Metrics)</span>
          </div>
          <div class="widget-controls">
            <div class="control-group">
              <label>Số mẫu Lành (Negative): <span id="tnVal">990</span></label>
              <input type="range" id="tnRange" min="500" max="2000" step="50" value="990">
            </div>
            <div class="control-group">
              <label>Số mẫu Bệnh (Positive): <span id="tpVal">10</span></label>
              <input type="range" id="tpRange" min="5" max="100" step="5" value="10">
            </div>
            <div class="control-group">
              <label>Recall của Model (%): <span id="recVal">80%</span></label>
              <input type="range" id="recRange" min="10" max="100" step="5" value="80">
            </div>
          </div>
          <div class="widget-output" id="cmOutput">Đang tính...</div>
        </div>
      `;
      initCMWidget();
    } else if (type === "widget-entropy-calculator") {
      mount.innerHTML = `
        <div class="interactive-widget">
          <div class="widget-header">
            <span class="widget-title">Máy Tính Entropy Nhị Phân & Information Gain (Decision Tree)</span>
          </div>
          <div class="widget-controls">
            <div class="control-group">
              <label>Xác suất p₁: <span id="p1Val">0.50</span></label>
              <input type="range" id="p1Range" min="0.01" max="0.99" step="0.01" value="0.50">
            </div>
          </div>
          <div class="canvas-wrapper">
            <canvas id="entropyCanvas" width="680" height="200"></canvas>
          </div>
          <div class="widget-output" id="entropyOutput">Đang tính...</div>
        </div>
      `;
      initEntropyWidget();
    } else if (type === "widget-knn-classifier") {
      mount.innerHTML = `
        <div class="interactive-widget">
          <div class="widget-header">
            <span class="widget-title">Mô Phỏng Phân Lớp k-NN Tương Tác</span>
          </div>
          <div class="widget-controls">
            <div class="control-group">
              <label>Giá trị k: <span id="kVal">3</span></label>
              <select id="knnK">
                <option value="1">k = 1</option>
                <option value="3" selected>k = 3</option>
                <option value="5">k = 5</option>
              </select>
            </div>
            <button class="btn" id="resetKnn">Đặt Lại Điểm Q</button>
            <span style="font-size:0.8rem; color:var(--text-muted); margin-left:auto;">(Bấm chuột lên canvas để di chuyển điểm kiểm tra Q)</span>
          </div>
          <div class="canvas-wrapper">
            <canvas id="knnCanvas" width="680" height="260" style="cursor:crosshair;"></canvas>
          </div>
          <div class="widget-output" id="knnOutput">Bấm chuột vào ô đồ thị để dự đoán nhãn điểm mới.</div>
        </div>
      `;
      initKnnWidget();
    } else if (type === "widget-cnn-calculator") {
      mount.innerHTML = `
        <div class="interactive-widget">
          <div class="widget-header">
            <span class="widget-title">Máy Tính Conv2D (Câu 2, 27, 35) & Mô Phỏng NMS (Câu 10)</span>
            <span style="font-family:var(--font-mono); font-size:0.75rem;">Conv2D Output & Bounding Box NMS</span>
          </div>
          <div class="widget-controls" style="flex-wrap: wrap; gap: 10px;">
            <div class="control-group">
              <label>Ảnh Rộng W:</label>
              <input type="number" id="cW" value="32" style="width:55px; padding:3px;">
            </div>
            <div class="control-group">
              <label>Kênh Cin:</label>
              <input type="number" id="cCin" value="3" style="width:50px; padding:3px;">
            </div>
            <div class="control-group">
              <label>Kernel K:</label>
              <input type="number" id="cK" value="5" style="width:45px; padding:3px;">
            </div>
            <div class="control-group">
              <label>Stride S:</label>
              <input type="number" id="cS" value="2" style="width:45px; padding:3px;">
            </div>
            <div class="control-group">
              <label>Kênh Cout:</label>
              <input type="number" id="cCout" value="32" style="width:55px; padding:3px;">
            </div>
            <div class="control-group">
              <label>Padding:</label>
              <select id="cPad" style="padding:3px; font-family:Georgia;">
                <option value="same" selected>same</option>
                <option value="valid">valid</option>
              </select>
            </div>
            <div class="control-group">
              <label>Ngưỡng NMS IoU: <span id="nmsThreshVal">0.40</span></label>
              <input type="range" id="nmsThresh" min="0.10" max="0.90" step="0.05" value="0.40">
            </div>
          </div>
          <div class="canvas-wrapper">
            <canvas id="nmsCanvas" width="680" height="150"></canvas>
          </div>
          <div class="widget-output" id="cnnOut">Đang tính...</div>
        </div>
      `;
      initCnnWidget();
    } else if (type === "widget-attention-matrix") {
      mount.innerHTML = `
        <div class="interactive-widget">
          <div class="widget-header">
            <span class="widget-title">Trọng Số Chú Ý Self-Attention (Câu 23, 74)</span>
          </div>
          <div style="display:flex; gap:6px; margin-bottom:12px;">
            <button class="btn active" data-w="it">Query: "it"</button>
            <button class="btn" data-w="cross">Query: "cross"</button>
            <button class="btn" data-w="street">Query: "street"</button>
          </div>
          <div class="canvas-wrapper">
            <canvas id="attCanvas" width="680" height="180"></canvas>
          </div>
          <div class="widget-output" id="attOut">Đang tính...</div>
        </div>
      `;
      initAttWidget();
    } else if (type === "widget-mlp-simulator") {
      mount.innerHTML = `
        <div class="interactive-widget">
          <div class="widget-header">
            <span class="widget-title">Mô Phỏng Mạng Nơ-ron MLP & Lan Truyền Ngược (Câu 1, 56 & 70)</span>
            <span style="font-family:var(--font-mono); font-size:0.75rem;">MLP 2-Layer (Forward & Backward)</span>
          </div>
          <div class="widget-controls" style="flex-wrap: wrap; gap: 10px;">
            <div class="control-group">
              <label>Đầu vào x₁: <span id="mlpX1Val">1.0</span></label>
              <input type="range" id="mlpX1" min="-2.0" max="2.0" step="0.1" value="1.0">
            </div>
            <div class="control-group">
              <label>Đầu vào x₂: <span id="mlpX2Val">0.5</span></label>
              <input type="range" id="mlpX2" min="-2.0" max="2.0" step="0.1" value="0.5">
            </div>
            <div class="control-group">
              <label>Nhãn thật (y):</label>
              <select id="mlpTarget" style="padding:4px; font-family:Georgia;">
                <option value="1" selected>y = 1.0</option>
                <option value="0">y = 0.0</option>
              </select>
            </div>
            <div class="control-group">
              <label>Hàm kích hoạt:</label>
              <select id="mlpAct" style="padding:4px; font-family:Georgia;">
                <option value="sigmoid" selected>Sigmoid (σ)</option>
                <option value="relu">ReLU (max(0,z))</option>
                <option value="tanh">Tanh</option>
              </select>
            </div>
            <div class="control-group">
              <label>Khởi tạo Trọng số:</label>
              <select id="mlpInit" style="padding:4px; font-family:Georgia;">
                <option value="random" selected>Ngẫu nhiên (Xavier/He)</option>
                <option value="zeros">Bằng 0 (W = 0: Lỗi đối xứng!)</option>
              </select>
            </div>
            <div class="control-group">
              <label>Tốc độ học (η): <span id="mlpLrVal">0.10</span></label>
              <input type="range" id="mlpLr" min="0.01" max="0.50" step="0.01" value="0.10">
            </div>
            <button class="btn" id="mlpStepFwd">Lan Truyền Tiến</button>
            <button class="btn" id="mlpStepBack">Lan Truyền Ngược</button>
            <button class="btn" id="mlpTrainEpoch">Lặp 10 Bước</button>
            <button class="btn" id="mlpReset">Đặt Lại</button>
          </div>
          <div class="canvas-wrapper">
            <canvas id="mlpCanvas" width="680" height="230"></canvas>
          </div>
          <div class="widget-output" id="mlpOut">Đang khởi tạo mạng nơ-ron...</div>
        </div>
      `;
      initMlpWidget();
    } else if (type === "widget-generative-diffusion") {
      mount.innerHTML = `
        <div class="interactive-widget">
          <div class="widget-header">
            <span class="widget-title">Mô Phỏng Mô Hình Khuếch Tán (Diffusion Denoising) & GAN Mode Collapse (Câu 61, 95)</span>
            <span style="font-family:var(--font-mono); font-size:0.75rem;">DDPM & Latent Denoising Simulator</span>
          </div>
          <div class="widget-controls" style="flex-wrap: wrap; gap: 10px;">
            <div class="control-group">
              <label>Bước thời gian t (0 → 1000): <span id="diffTVal">1000</span></label>
              <input type="range" id="diffT" min="0" max="1000" step="50" value="1000">
            </div>
            <div class="control-group">
              <label>Chế độ:</label>
              <select id="diffMode" style="padding:4px; font-family:Georgia;">
                <option value="diffusion" selected>Diffusion (U-Net khử nhiễu)</option>
                <option value="gan_healthy">GAN Lành mạnh (Đa dạng)</option>
                <option value="gan_collapse">GAN Sụp đổ (Mode Collapse - Câu 61)</option>
              </select>
            </div>
            <button class="btn" id="diffDenoiseBtn">Chạy Khử Nhiễu (Reverse Step-by-Step)</button>
            <button class="btn" id="diffAddNoiseBtn">+ Thêm Nhiễu (Forward Process)</button>
            <button class="btn" id="diffResetBtn">Đặt Lại</button>
          </div>
          <div class="canvas-wrapper">
            <canvas id="diffCanvas" width="680" height="200"></canvas>
          </div>
          <div class="widget-output" id="diffOut">Đang khởi tạo mô hình...</div>
        </div>
      `;
      initDiffusionWidget();
    }
  }

  // Widget 1: Gradient Descent
  function initGDWidget() {
    const canvas = document.getElementById("gdCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const lrR = document.getElementById("lrRange");
    const lrV = document.getElementById("lrVal");
    const x0R = document.getElementById("x0Range");
    const x0V = document.getElementById("x0Val");
    const stepB = document.getElementById("stepGDBtn");
    const autoB = document.getElementById("autoGDBtn");
    const resetB = document.getElementById("resetGDBtn");
    const out = document.getElementById("gdOutput");
    if (!lrR || !x0R || !out) return;

    let curX = parseFloat(x0R.value);
    let stepCount = 0;
    let timer = null;

    function f(x) { return Math.pow(x - 2, 2) + 1; }
    function df(x) { return 2 * (x - 2); }

    function toC(x, y) {
      const pad = 40;
      return {
        x: pad + ((x - (-4.5)) / 9.0) * (canvas.width - pad * 2),
        y: canvas.height - pad - ((y - 0) / 45.0) * (canvas.height - pad * 2)
      };
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.strokeStyle = "#eee"; ctx.lineWidth = 1;
      for (let x = -4; x <= 4; x += 2) {
        const p1 = toC(x, 0), p2 = toC(x, 45);
        ctx.beginPath(); ctx.moveTo(p1.x, p1.y); ctx.lineTo(p2.x, p2.y); ctx.stroke();
      }

      ctx.strokeStyle = "#111"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let x = -4.5; x <= 4.5; x += 0.1) {
        const p = toC(x, f(x));
        if (x === -4.5) ctx.moveTo(p.x, p.y); else ctx.lineTo(p.x, p.y);
      }
      ctx.stroke();

      const cp = toC(curX, f(curX));
      ctx.fillStyle = "#111"; ctx.beginPath(); ctx.arc(cp.x, cp.y, 6, 0, Math.PI * 2); ctx.fill();

      const grad = df(curX);
      const slopeLen = 25;
      const angle = Math.atan(grad * (canvas.height / 45.0) / (canvas.width / 9.0));
      ctx.strokeStyle = "#888"; ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(cp.x - Math.cos(angle) * slopeLen, cp.y + Math.sin(angle) * slopeLen);
      ctx.lineTo(cp.x + Math.cos(angle) * slopeLen, cp.y - Math.sin(angle) * slopeLen);
      ctx.stroke();

      out.innerHTML = `Bước: <strong>${stepCount}</strong> | Vị trí: <strong>x = ${curX.toFixed(3)}</strong> | Đạo hàm f'(x): <strong>${grad.toFixed(3)}</strong> | f(x): <strong>${f(curX).toFixed(3)}</strong>`;
    }

    function step() {
      const lr = parseFloat(lrR.value);
      const grad = df(curX);
      curX = curX - lr * grad;
      stepCount++;
      draw();
      if (Math.abs(curX - 2.0) < 0.005 && timer) {
        clearInterval(timer); timer = null; autoB.textContent = "Tự Động";
      }
    }

    lrR.addEventListener("input", () => { lrV.textContent = lrR.value; });
    x0R.addEventListener("input", () => {
      x0V.textContent = x0R.value; curX = parseFloat(x0R.value); stepCount = 0; draw();
    });
    if (stepB) stepB.addEventListener("click", step);
    if (resetB) resetB.addEventListener("click", () => {
      if (timer) { clearInterval(timer); timer = null; if (autoB) autoB.textContent = "Tự Động"; }
      curX = parseFloat(x0R.value); stepCount = 0; draw();
    });
    if (autoB) autoB.addEventListener("click", () => {
      if (timer) {
        clearInterval(timer); timer = null; autoB.textContent = "Tự Động";
      } else {
        autoB.textContent = "Dừng Lại";
        timer = setInterval(step, 200);
      }
    });

    draw();
  }

  // Widget 2: Cosine Similarity
  function initCosWidget() {
    const canvas = document.getElementById("cosCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const aR = document.getElementById("angleARange");
    const bR = document.getElementById("angleBRange");
    const aV = document.getElementById("angleAVal");
    const bV = document.getElementById("angleBVal");
    const out = document.getElementById("cosOutput");
    if (!aR || !bR || !out) return;

    function draw() {
      const aDeg = parseFloat(aR.value);
      const bDeg = parseFloat(bR.value);
      if (aV) aV.textContent = `${aDeg}°`;
      if (bV) bV.textContent = `${bDeg}°`;

      const radA = (aDeg * Math.PI) / 180.0;
      const radB = (bDeg * Math.PI) / 180.0;
      const cosSim = Math.cos(radA - radB);

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const cx = canvas.width / 2, cy = canvas.height / 2, r = 100;

      ctx.strokeStyle = "#e5e5e5"; ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI * 2); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx - r - 20, cy); ctx.lineTo(cx + r + 20, cy); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(cx, cy - r - 20); ctx.lineTo(cx, cy + r + 20); ctx.stroke();

      const ax = cx + r * Math.cos(radA), ay = cy - r * Math.sin(radA);
      ctx.strokeStyle = "#111"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(ax, ay); ctx.stroke();
      ctx.font = "bold 12px Georgia"; ctx.fillStyle = "#111"; ctx.fillText("A", ax + 8, ay);

      const bx = cx + r * Math.cos(radB), by = cy - r * Math.sin(radB);
      ctx.strokeStyle = "#777"; ctx.lineWidth = 2.5;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(bx, by); ctx.stroke();
      ctx.fillStyle = "#777"; ctx.fillText("B", bx + 8, by);

      const deltaDeg = Math.abs(aDeg - bDeg) % 360;
      const minAngle = deltaDeg > 180 ? 360 - deltaDeg : deltaDeg;
      let relation = "Độc lập (Vuông góc, cos = 0)";
      if (cosSim > 0.95) relation = "Gần như trùng khớp hoàn toàn (Cực kỳ tương đồng)";
      else if (cosSim > 0.5) relation = "Tương đồng tích cực (Cùng hướng)";
      else if (cosSim < -0.95) relation = "Đối nghịch hoàn toàn (Ngược hướng 180°)";
      else if (cosSim < 0) relation = "Tương đồng tiêu cực (Ngược hướng)";

      out.innerHTML = `Góc giữa 2 vector: <strong>${minAngle.toFixed(1)}°</strong> | <strong>Cosine Similarity: ${cosSim.toFixed(3)}</strong><br><span style="color:#555;">⇒ Nhận xét ngữ nghĩa: ${relation}</span>`;
    }

    aR.addEventListener("input", draw);
    bR.addEventListener("input", draw);
    draw();
  }

  // Widget: Naive Bayes Simulator
  function initNaiveBayesWidget() {
    const presetSelect = document.getElementById("nbPresetSelect");
    const laplaceToggle = document.getElementById("nbLaplaceToggle");
    const detailsBox = document.getElementById("nbDetailsBox");
    const out = document.getElementById("nbOutput");
    if (!presetSelect || !laplaceToggle || !detailsBox || !out) return;

    const presets = {
      d1: { title: "Email 1: 'ưu đãi dự án tiền thưởng'", tokens: ["ưu đãi", "dự án", "tiền", "thưởng"] },
      d2: { title: "Email 2: 'tiền thưởng miễn phí ưu đãi'", tokens: ["tiền", "thưởng", "miễn phí", "ưu đãi"] },
      d3: { title: "Email 3: 'báo cáo dự án họp lương'", tokens: ["báo cáo", "dự án", "họp", "lương"] },
      d4: { title: "Email 4: 'bitcoin khuyến mãi trúng thưởng'", tokens: ["bitcoin", "khuyến mãi", "trúng thưởng"] }
    };

    const vocabSize = 9;
    const spamWordCounts = { "tiền": 3, "thưởng": 2, "miễn phí": 2, "ưu đãi": 2, "mặt": 1 };
    const hamWordCounts = { "họp": 1, "dự án": 2, "tiền": 1, "lương": 1, "báo cáo": 1 };
    const totalSpamWords = 10;
    const totalHamWords = 6;
    const priorSpam = 0.6;
    const priorHam = 0.4;

    function render() {
      const selectedKey = presetSelect.value || "d1";
      const preset = presets[selectedKey] || presets.d1;
      const useLaplace = laplaceToggle.checked;

      let pSpamProduct = priorSpam;
      let pHamProduct = priorHam;
      let logSpam = Math.log(priorSpam);
      let logHam = Math.log(priorHam);
      let hasZeroSpam = false;
      let hasZeroHam = false;

      let tableRows = "";

      preset.tokens.forEach(token => {
        const cSpam = spamWordCounts[token] || 0;
        const cHam = hamWordCounts[token] || 0;

        let pWSpam, pWHam, pSpamStr, pHamStr;

        if (useLaplace) {
          pWSpam = (cSpam + 1) / (totalSpamWords + vocabSize);
          pWHam = (cHam + 1) / (totalHamWords + vocabSize);
          pSpamStr = `${cSpam + 1}/${totalSpamWords + vocabSize} (${(pWSpam * 100).toFixed(1)}%)`;
          pHamStr = `${cHam + 1}/${totalHamWords + vocabSize} (${(pWHam * 100).toFixed(1)}%)`;
        } else {
          pWSpam = cSpam / totalSpamWords;
          pWHam = cHam / totalHamWords;
          pSpamStr = cSpam === 0 ? '<span style="color:#c00; font-weight:bold;">0 / 10 (0%)</span>' : `${cSpam}/10 (${(pWSpam * 100).toFixed(1)}%)`;
          pHamStr = cHam === 0 ? '<span style="color:#c00; font-weight:bold;">0 / 6 (0%)</span>' : `${cHam}/6 (${(pWHam * 100).toFixed(1)}%)`;
          if (cSpam === 0) hasZeroSpam = true;
          if (cHam === 0) hasZeroHam = true;
        }

        pSpamProduct *= pWSpam;
        pHamProduct *= pWHam;

        if (pWSpam > 0) logSpam += Math.log(pWSpam);
        else logSpam = -Infinity;

        if (pWHam > 0) logHam += Math.log(pWHam);
        else logHam = -Infinity;

        tableRows += `
          <tr style="border-bottom: 1px solid #e5e5e5;">
            <td style="padding: 6px 10px; font-weight: bold;">"${token}"</td>
            <td style="padding: 6px 10px; text-align: center;">${cSpam} lần</td>
            <td style="padding: 6px 10px; text-align: center;">${pSpamStr}</td>
            <td style="padding: 6px 10px; text-align: center;">${cHam} lần</td>
            <td style="padding: 6px 10px; text-align: center;">${pHamStr}</td>
          </tr>
        `;
      });

      let alertHtml = "";
      if (!useLaplace && (hasZeroSpam || hasZeroHam)) {
        alertHtml = `
          <div style="background: #fff0f0; border-left: 3px solid #111; padding: 8px 12px; margin-bottom: 12px; font-size: 12px;">
            <strong>⚠️ Thảm họa Tần suất = 0 (Zero-Frequency):</strong> Có từ vựng chưa từng xuất hiện trong tập huấn luyện của một lớp! Khi nhân dồn, số 0 này sẽ triệt tiêu toàn bộ tích xác suất của lớp đó về 0. Hãy bật <em>'Làm mịn Laplace'</em> để khắc phục!
          </div>
        `;
      }

      detailsBox.innerHTML = `
        ${alertHtml}
        <table style="width: 100%; border-collapse: collapse; font-size: 12px; margin-bottom: 12px; border: 1px solid #111;">
          <thead>
            <tr style="background: #f0f0f0; border-bottom: 1px solid #111;">
              <th style="padding: 6px 10px; text-align: left;">Từ khóa</th>
              <th style="padding: 6px 10px; text-align: center;">Số lần trong Spam</th>
              <th style="padding: 6px 10px; text-align: center;">P(từ | Spam)</th>
              <th style="padding: 6px 10px; text-align: center;">Số lần trong Ham</th>
              <th style="padding: 6px 10px; text-align: center;">P(từ | Ham)</th>
            </tr>
          </thead>
          <tbody>
            ${tableRows}
          </tbody>
        </table>
        <div style="font-size: 12px; color: #555;">
          • Prior: P(Spam) = 0.60 | P(Ham) = 0.40 | Kích thước từ điển: |V| = ${vocabSize}<br>
          • Điểm số Spam (Score): ${pSpamProduct === 0 ? "0.0" : pSpamProduct.toExponential(4)} (Log-score: ${logSpam === -Infinity ? "-∞" : logSpam.toFixed(2)})<br>
          • Điểm số Ham (Score): ${pHamProduct === 0 ? "0.0" : pHamProduct.toExponential(4)} (Log-score: ${logHam === -Infinity ? "-∞" : logHam.toFixed(2)})
        </div>
      `;

      if (pSpamProduct === 0 && pHamProduct === 0) {
        out.innerHTML = `<strong>Kết luận: Không thể phân loại do cả hai lớp đều bị triệt tiêu xác suất về 0.0! Hãy bật Laplace Smoothing!</strong>`;
      } else {
        const sum = pSpamProduct + pHamProduct;
        const confSpam = sum > 0 ? (pSpamProduct / sum) * 100 : 50;
        const confHam = sum > 0 ? (pHamProduct / sum) * 100 : 50;
        const isSpam = pSpamProduct > pHamProduct;

        out.innerHTML = `
          Dự đoán MAP: <strong>${isSpam ? "THƯ RÁC (SPAM)" : "THƯ HỢP LỆ (HAM)"}</strong> | 
          Độ tin cậy: <strong>${(isSpam ? confSpam : confHam).toFixed(1)}%</strong>
          <span style="display:inline-block; margin-left: 10px; font-size: 12px; color: #444;">
            (Spam: ${confSpam.toFixed(1)}% vs Ham: ${confHam.toFixed(1)}%)
          </span>
        `;
      }
    }

    presetSelect.addEventListener("change", render);
    laplaceToggle.addEventListener("change", render);
    render();
  }

  // Widget: Linear Regression & Regularization Simulator
  function initLinearRegressionWidget() {
    const canvas = document.getElementById("lrCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const modelSelect = document.getElementById("lrModelType");
    const lambdaRange = document.getElementById("lrLambdaRange");
    const lambdaVal = document.getElementById("lrLambdaVal");
    const outlierToggle = document.getElementById("lrOutlierToggle");
    const out = document.getElementById("lrOutput");
    if (!modelSelect || !lambdaRange || !outlierToggle || !out) return;

    function render() {
      const model = modelSelect.value || "ols";
      const lambda = parseFloat(lambdaRange.value) || 0;
      const hasOutlier = outlierToggle.checked;
      if (lambdaVal) lambdaVal.textContent = lambda.toFixed(1);

      // Base points
      const points = [
        { x: 1.0, y: 2.2 },
        { x: 2.0, y: 3.1 },
        { x: 3.0, y: 4.8 },
        { x: 4.0, y: 5.9 },
        { x: 5.0, y: 7.3 }
      ];

      if (hasOutlier) {
        points.push({ x: 2.0, y: 9.5, isOutlier: true });
      }

      const N = points.length;
      let sumX = 0, sumY = 0;
      points.forEach(p => { sumX += p.x; sumY += p.y; });
      const meanX = sumX / N;
      const meanY = sumY / N;

      let varX = 0, covXY = 0, totY = 0;
      points.forEach(p => {
        const dx = p.x - meanX;
        const dy = p.y - meanY;
        varX += dx * dx;
        covXY += dx * dy;
        totY += dy * dy;
      });

      const wOLS = covXY / varX;
      let w = wOLS;
      let b = meanY - w * meanX;

      if (model === "ridge") {
        // Ridge penalty shrinks slope
        w = covXY / (varX + lambda * 2.5);
        b = meanY - w * meanX;
      } else if (model === "lasso") {
        // Soft-thresholding operator for Lasso
        const threshold = (lambda * 0.4);
        if (Math.abs(wOLS) <= threshold) {
          w = 0;
        } else {
          w = Math.sign(wOLS) * (Math.abs(wOLS) - threshold);
        }
        b = meanY - w * meanX;
      }

      // Calculate Metrics
      let sse = 0, sae = 0;
      points.forEach(p => {
        const yPred = w * p.x + b;
        const err = p.y - yPred;
        sse += err * err;
        sae += Math.abs(err);
      });
      const mse = sse / N;
      const mae = sae / N;
      const r2 = totY > 0 ? 1 - (sse / totY) : 1;

      // Draw Canvas
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const padLeft = 50, padBottom = 40, padTop = 20, padRight = 30;
      const plotW = canvas.width - padLeft - padRight;
      const plotH = canvas.height - padTop - padBottom;

      const minX = 0, maxX = 6;
      const minY = 0, maxY = 11;

      function toScreenX(x) { return padLeft + ((x - minX) / (maxX - minX)) * plotW; }
      function toScreenY(y) { return canvas.height - padBottom - ((y - minY) / (maxY - minY)) * plotH; }

      // Grid & Axes
      ctx.strokeStyle = "#e5e5e5";
      ctx.lineWidth = 1;
      for (let x = 1; x <= 5; x++) {
        const sx = toScreenX(x);
        ctx.beginPath(); ctx.moveTo(sx, padTop); ctx.lineTo(sx, canvas.height - padBottom); ctx.stroke();
      }
      for (let y = 2; y <= 10; y += 2) {
        const sy = toScreenY(y);
        ctx.beginPath(); ctx.moveTo(padLeft, sy); ctx.lineTo(canvas.width - padRight, sy); ctx.stroke();
      }

      // Main Axes
      ctx.strokeStyle = "#111";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(padLeft, padTop);
      ctx.lineTo(padLeft, canvas.height - padBottom);
      ctx.lineTo(canvas.width - padRight, canvas.height - padBottom);
      ctx.stroke();

      // Axis labels
      ctx.fillStyle = "#111";
      ctx.font = "11px Georgia";
      ctx.textAlign = "center";
      for (let x = 0; x <= 6; x++) {
        ctx.fillText(x.toString(), toScreenX(x), canvas.height - padBottom + 16);
      }
      ctx.textAlign = "right";
      for (let y = 0; y <= 10; y += 2) {
        ctx.fillText(y.toString(), padLeft - 8, toScreenY(y) + 4);
      }

      // Draw Regression Line
      const xStart = 0, xEnd = 6;
      const yStart = w * xStart + b;
      const yEnd = w * xEnd + b;

      ctx.strokeStyle = "#111";
      ctx.lineWidth = 2.5;
      ctx.beginPath();
      ctx.moveTo(toScreenX(xStart), toScreenY(yStart));
      ctx.lineTo(toScreenX(xEnd), toScreenY(yEnd));
      ctx.stroke();

      // Draw Points
      points.forEach(p => {
        const sx = toScreenX(p.x);
        const sy = toScreenY(p.y);
        if (p.isOutlier) {
          ctx.strokeStyle = "#111";
          ctx.lineWidth = 2;
          ctx.beginPath(); ctx.arc(sx, sy, 7, 0, Math.PI * 2); ctx.stroke();
          ctx.fillStyle = "#fff";
          ctx.fill();
          ctx.fillStyle = "#111";
          ctx.beginPath(); ctx.arc(sx, sy, 3.5, 0, Math.PI * 2); ctx.fill();
          ctx.font = "bold 10px Georgia";
          ctx.fillText("Outlier", sx + 22, sy + 3);
        } else {
          ctx.fillStyle = "#111";
          ctx.beginPath(); ctx.arc(sx, sy, 4.5, 0, Math.PI * 2); ctx.fill();
        }
      });

      // Commentary
      let comment = "";
      if (hasOutlier && model === "ols") {
        comment = "⚠️ <strong>Điểm dị biệt (Outlier)</strong> đã kéo đường hồi quy OLS lệch dốc hẳn lên trên!";
      } else if (model === "ridge") {
        comment = `🔒 <strong>Ridge L2 (λ = ${lambda.toFixed(1)})</strong> co rút hệ số góc w về ${w.toFixed(2)}, giúp đường thẳng ổn định bớt bị giật lệch.`;
      } else if (model === "lasso") {
        if (w === 0) {
          comment = `🎯 <strong>Lasso L1 (λ = ${lambda.toFixed(1)})</strong> đã triệt tiêu hoàn toàn hệ số góc w về 0.0 (Feature Selection)! Mô hình biến thành đường ngang ŷ = b.`;
        } else {
          comment = `🎯 <strong>Lasso L1</strong> ép hệ số góc w co rút mạnh về ${w.toFixed(2)} nhờ toán tử soft-thresholding.`;
        }
      } else {
        comment = "Đường hồi quy OLS chuẩn mực khớp êm ái trên tập dữ liệu sạch.";
      }

      out.innerHTML = `
        Phương trình: <strong>ŷ = ${w.toFixed(3)}x + ${b.toFixed(3)}</strong> | 
        MSE: <strong>${mse.toFixed(2)}</strong> | 
        MAE: <strong>${mae.toFixed(2)}</strong> | 
        R²: <strong>${(Math.max(-1, r2) * 100).toFixed(1)}%</strong>
        <br><span style="color:#444; font-size:12px;">${comment}</span>
      `;
    }

    modelSelect.addEventListener("change", render);
    lambdaRange.addEventListener("input", render);
    outlierToggle.addEventListener("change", render);
    render();
  }

  // Widget 3: Confusion Matrix
  function initCMWidget() {
    const tnR = document.getElementById("tnRange");
    const tpR = document.getElementById("tpRange");
    const recR = document.getElementById("recRange");
    const tnV = document.getElementById("tnVal");
    const tpV = document.getElementById("tpVal");
    const recV = document.getElementById("recVal");
    const out = document.getElementById("cmOutput");
    if (!tnR || !tpR || !recR || !out) return;

    function calc() {
      const neg = parseInt(tnR.value, 10);
      const pos = parseInt(tpR.value, 10);
      const rec = parseInt(recR.value, 10) / 100.0;

      if (tnV) tnV.textContent = neg;
      if (tpV) tpV.textContent = pos;
      if (recV) recV.textContent = `${Math.round(rec * 100)}%`;

      const tp = Math.round(pos * rec);
      const fn = pos - tp;
      const fp = Math.round(neg * 0.02);
      const tn = neg - fp;

      const total = tp + fn + fp + tn;
      const acc = (tp + tn) / total;
      const prec = (tp + fp) > 0 ? tp / (tp + fp) : 0;
      const f1 = (prec + rec) > 0 ? (2 * prec * rec) / (prec + rec) : 0;

      out.innerHTML = `
        TP = ${tp}, FN = ${fn}, FP = ${fp}, TN = ${tn} | 
        <strong>Accuracy: ${(acc * 100).toFixed(1)}%</strong> | 
        <strong>Recall: ${(rec * 100).toFixed(1)}%</strong> | 
        Precision: ${(prec * 100).toFixed(1)}% | 
        <strong>F1: ${f1.toFixed(3)}</strong>
        <br><em style="font-size:0.8rem; color:#666;">(Mẫu hiếm: dù Accuracy đạt ${(acc * 100).toFixed(1)}% nhưng bỏ sót ${fn} ca bệnh! Bắt buộc dùng Recall & Macro-F1).</em>
      `;
    }

    [tnR, tpR, recR].forEach(el => el.addEventListener("input", calc));
    calc();
  }

  // Widget 4: Entropy Calculator
  function initEntropyWidget() {
    const canvas = document.getElementById("entropyCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const p1R = document.getElementById("p1Range");
    const p1V = document.getElementById("p1Val");
    const out = document.getElementById("entropyOutput");
    if (!p1R || !out) return;

    function H(p) {
      if (p <= 0 || p >= 1) return 0;
      return - (p * Math.log2(p) + (1 - p) * Math.log2(1 - p));
    }

    function draw() {
      const p = parseFloat(p1R.value);
      if (p1V) p1V.textContent = p.toFixed(2);
      const hVal = H(p);

      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const m = 40, w = canvas.width - m * 2, h = canvas.height - m * 2;

      ctx.strokeStyle = "#ddd"; ctx.lineWidth = 1;
      ctx.beginPath(); ctx.moveTo(m, canvas.height - m); ctx.lineTo(m + w, canvas.height - m); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(m, canvas.height - m); ctx.lineTo(m, m); ctx.stroke();

      ctx.strokeStyle = "#111"; ctx.lineWidth = 2;
      ctx.beginPath();
      for (let x = 0.001; x <= 0.999; x += 0.01) {
        const px = m + x * w, py = canvas.height - m - H(x) * h;
        if (x === 0.001) ctx.moveTo(px, py); else ctx.lineTo(px, py);
      }
      ctx.stroke();

      const curX = m + p * w;
      const curY = canvas.height - m - hVal * h;
      ctx.fillStyle = "#111";
      ctx.beginPath(); ctx.arc(curX, curY, 5, 0, Math.PI * 2); ctx.fill();

      out.innerHTML = `p₁ = ${p.toFixed(2)}, p₂ = ${(1 - p).toFixed(2)} ⇒ <strong>Entropy H = ${hVal.toFixed(3)} bit</strong> ${p === 0.5 ? '(Cực đại: 50-50 hỗn loạn nhất)' : ''}`;
    }

    p1R.addEventListener("input", draw);
    draw();
  }

  // Widget 5: k-NN Classifier
  function initKnnWidget() {
    const canvas = document.getElementById("knnCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const kSel = document.getElementById("knnK");
    const resetB = document.getElementById("resetKnn");
    const out = document.getElementById("knnOutput");
    if (!kSel || !out) return;

    const pts = [
      { id: "S1", x: 2, y: 0, l: "Đỏ", f: "#111" },
      { id: "S2", x: 1, y: 1, l: "Đỏ", f: "#111" },
      { id: "S3", x: 0, y: 2, l: "Đỏ", f: "#111" },
      { id: "S4", x: 8, y: 7, l: "Xanh dương", f: "#777" },
      { id: "S5", x: 9, y: 6, l: "Xanh dương", f: "#777" },
      { id: "S6", x: 7, y: 8, l: "Xanh dương", f: "#777" },
      { id: "S7", x: 5, y: 5, l: "Xanh lá", f: "#fff" },
      { id: "S8", x: 6, y: 4, l: "Xanh lá", f: "#fff" }
    ];

    let Q = { x: 6.0, y: 6.0 };

    function toC(x, y) {
      const m = 40;
      return {
        x: m + (x / 10.0) * (canvas.width - m * 2),
        y: canvas.height - m - (y / 10.0) * (canvas.height - m * 2)
      };
    }

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const k = parseInt(kSel.value || "3", 10);

      const dists = pts.map(p => ({
        ...p,
        d: Math.sqrt(Math.pow(p.x - Q.x, 2) + Math.pow(p.y - Q.y, 2))
      })).sort((a, b) => a.d - b.d);

      const kNear = dists.slice(0, k);
      const qPt = toC(Q.x, Q.y);

      kNear.forEach(n => {
        const nP = toC(n.x, n.y);
        ctx.strokeStyle = "#888";
        ctx.beginPath(); ctx.moveTo(qPt.x, qPt.y); ctx.lineTo(nP.x, nP.y); ctx.stroke();
      });

      pts.forEach(p => {
        const cp = toC(p.x, p.y);
        ctx.fillStyle = p.f;
        ctx.strokeStyle = "#111";
        ctx.lineWidth = 1.5;
        ctx.beginPath(); ctx.arc(cp.x, cp.y, 5, 0, Math.PI * 2); ctx.fill(); ctx.stroke();
        ctx.font = "10px Georgia"; ctx.fillStyle = "#111";
        ctx.fillText(p.id, cp.x + 6, cp.y + 3);
      });

      ctx.fillStyle = "#111";
      ctx.fillRect(qPt.x - 5, qPt.y - 5, 10, 10);
      ctx.fillStyle = "#fff"; ctx.font = "bold 9px Georgia";
      ctx.fillText("Q", qPt.x - 3, qPt.y + 3);

      const votes = {};
      kNear.forEach(n => votes[n.l] = (votes[n.l] || 0) + 1);
      const vKeys = Object.keys(votes);
      let win = vKeys.length > 0 ? vKeys.reduce((a, b) => votes[a] > votes[b] ? a : b) : "Chưa xác định";

      out.innerHTML = `Q(${Q.x.toFixed(1)}, ${Q.y.toFixed(1)}) → Gần nhất: <strong>${kNear.map(n => `${n.id} (${n.l})`).join(', ')}</strong> ⇒ Dự đoán: <strong>${win}</strong>`;
    }

    function handleKnnPointer(clientX, clientY) {
      const rect = canvas.getBoundingClientRect();
      const scaleX = canvas.width / rect.width;
      const scaleY = canvas.height / rect.height;
      const cx = (clientX - rect.left) * scaleX;
      const cy = (clientY - rect.top) * scaleY;
      const m = 40;
      Q.x = Math.max(0, Math.min(10, ((cx - m) / (canvas.width - m * 2)) * 10.0));
      Q.y = Math.max(0, Math.min(10, ((canvas.height - m - cy) / (canvas.height - m * 2)) * 10.0));
      draw();
    }

    canvas.addEventListener("click", (e) => {
      handleKnnPointer(e.clientX, e.clientY);
    });

    canvas.addEventListener("touchstart", (e) => {
      if (e.touches && e.touches[0]) {
        handleKnnPointer(e.touches[0].clientX, e.touches[0].clientY);
        e.preventDefault();
      }
    }, { passive: false });

    kSel.addEventListener("change", draw);
    if (resetB) resetB.addEventListener("click", () => { Q = { x: 6.0, y: 6.0 }; draw(); });
    draw();
  }

  // Widget 6: CNN Dimension Calculator & NMS Simulation
  function initCnnWidget() {
    const w = document.getElementById("cW");
    const cin = document.getElementById("cCin");
    const k = document.getElementById("cK");
    const s = document.getElementById("cS");
    const cout = document.getElementById("cCout");
    const pad = document.getElementById("cPad");
    const nmsThreshInput = document.getElementById("nmsThresh");
    const nmsThreshVal = document.getElementById("nmsThreshVal");
    const canvas = document.getElementById("nmsCanvas");
    const out = document.getElementById("cnnOut");
    if (!w || !cin || !k || !s || !cout || !pad || !out) return;
    const ctx = canvas ? canvas.getContext("2d") : null;

    function calc() {
      const W = parseInt(w.value, 10) || 32;
      const Cin = parseInt(cin.value, 10) || 3;
      const K = parseInt(k.value, 10) || 3;
      const S = parseInt(s.value, 10) || 1;
      const Cout = parseInt(cout.value, 10) || 32;
      const P = pad.value === "same" ? Math.floor((K - 1) / 2) : 0;

      const Wout = pad.value === "same" ? Math.ceil(W / S) : Math.floor((W - K + 2 * P) / S) + 1;
      const params = (K * K * Cin + 1) * Cout; // Filter weights + biases (Câu 2 VAIO)
      const macs = Wout * Wout * Cout * (K * K * Cin);
      const flops = 2 * macs;

      const thresh = nmsThreshInput ? parseFloat(nmsThreshInput.value) : 0.40;
      if (nmsThreshVal) nmsThreshVal.innerText = thresh.toFixed(2);

      // NMS simulation for 3 boxes from Câu 10 VAIO:
      // B1: (0, 0, 100, 100) conf 0.95
      // B2: (10, 10, 90, 90) conf 0.90
      // B3: (105, 105, 200, 200) conf 0.85
      const b2Kept = 0.64 <= thresh;
      const keptList = b2Kept ? "B₁, B₂ và B₃" : "B₁ và B₃";

      out.innerHTML = `
        <div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:8px;">
          <div>Kích thước đầu ra: <strong>(1, ${Wout}, ${Wout}, ${Cout})</strong> [W_out = ⌊(${W} - ${K} + 2·${P})/${S}⌋ + 1 = ${Wout}]</div>
          <div>Tham số học được: <strong>${params.toLocaleString()} params</strong> [(${K}²·${Cin} + 1)·${Cout}] | FLOPs: <strong>${(flops / 1e6).toFixed(2)} MFLOPs</strong></div>
        </div>
        <div style="margin-top:6px; font-size:0.8rem; border-top:1px solid #eee; padding-top:4px;">
          <strong>Mô phỏng NMS (Câu 10 VAIO 2025):</strong> B₁ (conf 0.95), B₂ (conf 0.90, IoU với B₁ = 0.64), B₃ (conf 0.85, IoU = 0.0).<br>
          Với ngưỡng IoU = <strong>${thresh.toFixed(2)}</strong>: Hộp B₂ ${b2Kept ? '<span style="color:#111; font-weight:bold;">ĐƯỢC GIỮ LẠI (vì 0.64 ≤ ' + thresh.toFixed(2) + ')</span>' : '<span style="color:#555; text-decoration:line-through; font-weight:bold;">BỊ LOẠI BỎ (vì 0.64 > ' + thresh.toFixed(2) + ')</span>'}. Kết quả giữ lại: <strong>${keptList}</strong>.
        </div>
      `;

      if (ctx && canvas) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const scale = 0.62;
        const offX = 40, offY = 15;

        // B1
        ctx.fillStyle = "rgba(0,0,0,0.06)";
        ctx.fillRect(offX, offY, 100 * scale, 100 * scale);
        ctx.strokeStyle = "#111";
        ctx.lineWidth = 2;
        ctx.strokeRect(offX, offY, 100 * scale, 100 * scale);
        ctx.fillStyle = "#111";
        ctx.font = "bold 9px Georgia";
        ctx.fillText("B₁ (0.95) [GIỮ]", offX + 4, offY + 14);

        // B2
        if (b2Kept) {
          ctx.strokeStyle = "#111";
          ctx.lineWidth = 1.8;
          ctx.setLineDash([]);
          ctx.strokeRect(offX + 10 * scale, offY + 10 * scale, 80 * scale, 80 * scale);
          ctx.fillStyle = "#111";
          ctx.fillText("B₂ (0.90) [GIỮ]", offX + 14 * scale, offY + 28 * scale);
        } else {
          ctx.strokeStyle = "#888";
          ctx.lineWidth = 1.5;
          ctx.setLineDash([3, 3]);
          ctx.strokeRect(offX + 10 * scale, offY + 10 * scale, 80 * scale, 80 * scale);
          ctx.fillStyle = "#888";
          ctx.fillText("B₂ (0.90) [LOẠI]", offX + 14 * scale, offY + 28 * scale);
          ctx.setLineDash([]);
        }

        // B3
        const b3X = offX + 130 * scale;
        const b3Y = offY + 15 * scale;
        const b3W = 95 * scale;
        const b3H = 95 * scale;
        ctx.fillStyle = "rgba(0,0,0,0.06)";
        ctx.fillRect(b3X, b3Y, b3W, b3H);
        ctx.strokeStyle = "#111";
        ctx.lineWidth = 2;
        ctx.strokeRect(b3X, b3Y, b3W, b3H);
        ctx.fillStyle = "#111";
        ctx.fillText("B₃ (0.85) [GIỮ]", b3X + 4, b3Y + 14);

        // Text summary
        ctx.fillStyle = "#111";
        ctx.font = "bold 11px Georgia";
        ctx.fillText("Minh họa thuật toán NMS (Câu 10 VAIO):", 240, 30);
        ctx.font = "10px Georgia";
        ctx.fillStyle = "#333";
        ctx.fillText("• Hộp B₁ có điểm cao nhất 0.95 ⇒ Chọn đầu tiên", 240, 52);
        ctx.fillText(`• IoU(B₁, B₂) = 6,400 / 10,000 = 0.64 ${b2Kept ? '≤ ' + thresh.toFixed(2) + ' ⇒ Giữ' : '> ' + thresh.toFixed(2) + ' ⇒ Triệt tiêu'}`, 240, 72);
        ctx.fillText("• IoU(B₁, B₃) = 0.0 ≤ " + thresh.toFixed(2) + " ⇒ Không chạm nhau ⇒ Luôn giữ B₃", 240, 92);
        ctx.font = "bold 10px Georgia";
        ctx.fillStyle = "#111";
        ctx.fillText(`⇒ KẾT QUẢ CUỐI CÙNG: ${keptList}!`, 240, 115);
      }
    }

    [w, cin, k, s, cout, pad].forEach(el => el.addEventListener("input", calc));
    if (nmsThreshInput) nmsThreshInput.addEventListener("input", calc);
    calc();
  }

  // Widget 7: Self-Attention Matrix
  function initAttWidget() {
    const canvas = document.getElementById("attCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const out = document.getElementById("attOut");
    if (!out) return;

    const words = ["The", "animal", "didn't", "cross", "the", "street", "because", "it", "was", "too", "tired"];
    const map = {
      "it": { "animal": 0.62, "street": 0.08, "cross": 0.12, "tired": 0.14 },
      "cross": { "street": 0.45, "animal": 0.30, "didn't": 0.15 },
      "street": { "cross": 0.45, "street": 0.35, "the": 0.12 }
    };

    let curW = "it";

    document.querySelectorAll("[data-w]").forEach(btn => {
      btn.addEventListener("click", () => {
        document.querySelectorAll("[data-w]").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        curW = btn.getAttribute("data-w");
        draw();
      });
    });

    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const n = words.length;
      const cellW = canvas.width / n;

      words.forEach((w, i) => {
        const weight = (map[curW] && map[curW][w]) ? map[curW][w] : 0.02;
        const alpha = Math.min(1.0, weight * 1.5);
        ctx.fillStyle = `rgba(0,0,0,${alpha.toFixed(2)})`;
        ctx.fillRect(i * cellW, 20, cellW - 4, 80);

        ctx.fillStyle = alpha > 0.4 ? "#fff" : "#111";
        ctx.font = "10px Georgia";
        ctx.textAlign = "center";
        ctx.fillText(`${(weight * 100).toFixed(0)}%`, i * cellW + cellW / 2, 65);

        ctx.fillStyle = "#111";
        ctx.font = w === curW ? "bold 11px Georgia" : "11px Georgia";
        ctx.fillText(w, i * cellW + cellW / 2, 125);
      });

      const topTarget = map[curW] ? Object.keys(map[curW]).reduce((a, b) => map[curW][a] > map[curW][b] ? a : b) : "none";
      out.innerHTML = `Query "<strong>${curW}</strong>" liên kết mạnh nhất tới token: "<strong>${topTarget}</strong>" (${((map[curW][topTarget] || 0) * 100).toFixed(0)}% attention weight).`;
    }

    draw();
  }

  // Widget 10: MLP & Backpropagation Simulator
  function initMlpWidget() {
    const canvas = document.getElementById("mlpCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");

    const x1Slider = document.getElementById("mlpX1");
    const x2Slider = document.getElementById("mlpX2");
    const x1Val = document.getElementById("mlpX1Val");
    const x2Val = document.getElementById("mlpX2Val");
    const targetSel = document.getElementById("mlpTarget");
    const actSel = document.getElementById("mlpAct");
    const initSel = document.getElementById("mlpInit");
    const lrSlider = document.getElementById("mlpLr");
    const lrVal = document.getElementById("mlpLrVal");

    const btnFwd = document.getElementById("mlpStepFwd");
    const btnBack = document.getElementById("mlpStepBack");
    const btnEpoch = document.getElementById("mlpTrainEpoch");
    const btnReset = document.getElementById("mlpReset");
    const out = document.getElementById("mlpOut");

    // Network parameters (matches Section 10.6 hand calculation)
    let W1 = [[0.2, 0.4], [-0.3, 0.5]];
    let b1 = [0.1, -0.2];
    let W2 = [0.6, -0.4];
    let b2 = 0.3;

    let z1 = [0, 0];
    let a1 = [0, 0];
    let z2 = 0;
    let yHat = 0.5;
    let loss = 0;
    let delta2 = 0;
    let delta1 = [0, 0];
    let gradW2 = [0, 0];
    let gradB2 = 0;
    let gradW1 = [[0, 0], [0, 0]];
    let gradB1 = [0, 0];
    let stepCount = 0;
    let lastAction = "Khởi tạo mạng";

    function act(z, type) {
      if (type === "sigmoid") return 1 / (1 + Math.exp(-Math.max(-15, Math.min(15, z))));
      if (type === "relu") return Math.max(0, z);
      if (type === "tanh") return Math.tanh(z);
      return z;
    }

    function actDeriv(z, a, type) {
      if (type === "sigmoid") return a * (1 - a);
      if (type === "relu") return z > 0 ? 1 : 0;
      if (type === "tanh") return 1 - a * a;
      return 1;
    }

    function resetParams() {
      const mode = initSel.value;
      if (mode === "zeros") {
        W1 = [[0, 0], [0, 0]];
        b1 = [0, 0];
        W2 = [0, 0];
        b2 = 0;
      } else {
        W1 = [[0.2, 0.4], [-0.3, 0.5]];
        b1 = [0.1, -0.2];
        W2 = [0.6, -0.4];
        b2 = 0.3;
      }
      stepCount = 0;
      lastAction = mode === "zeros" ? "Khởi tạo W = 0 (Lỗi đối xứng)" : "Khởi tạo ngẫu nhiên Xavier/He";
      forward();
    }

    function forward() {
      const x1 = parseFloat(x1Slider.value);
      const x2 = parseFloat(x2Slider.value);
      const target = parseFloat(targetSel.value);
      const type = actSel.value;

      // Hidden layer
      z1[0] = W1[0][0] * x1 + W1[0][1] * x2 + b1[0];
      z1[1] = W1[1][0] * x1 + W1[1][1] * x2 + b1[1];
      a1[0] = act(z1[0], type);
      a1[1] = act(z1[1], type);

      // Output layer (Sigmoid for binary classification)
      z2 = W2[0] * a1[0] + W2[1] * a1[1] + b2;
      yHat = 1 / (1 + Math.exp(-Math.max(-15, Math.min(15, z2))));

      // Binary Cross-Entropy Loss
      const eps = 1e-7;
      loss = - (target * Math.log(Math.max(eps, yHat)) + (1 - target) * Math.log(Math.max(eps, 1 - yHat)));

      lastAction = "Lan truyền tiến (Forward Pass)";
      render();
    }

    function backwardAndUpdate() {
      forward(); // ensure up to date
      const x1 = parseFloat(x1Slider.value);
      const x2 = parseFloat(x2Slider.value);
      const target = parseFloat(targetSel.value);
      const type = actSel.value;
      const lr = parseFloat(lrSlider.value);

      // Output error: delta^[2] = yHat - y
      delta2 = yHat - target;
      gradW2[0] = delta2 * a1[0];
      gradW2[1] = delta2 * a1[1];
      gradB2 = delta2;

      // Hidden errors: delta^[1] = (W2^T * delta2) * g'(z^[1])
      const dAct0 = actDeriv(z1[0], a1[0], type);
      const dAct1 = actDeriv(z1[1], a1[1], type);
      delta1[0] = (W2[0] * delta2) * dAct0;
      delta1[1] = (W2[1] * delta2) * dAct1;

      // Hidden gradients
      gradW1[0][0] = delta1[0] * x1;
      gradW1[0][1] = delta1[0] * x2;
      gradB1[0] = delta1[0];

      gradW1[1][0] = delta1[1] * x1;
      gradW1[1][1] = delta1[1] * x2;
      gradB1[1] = delta1[1];

      // Update weights via Gradient Descent
      W2[0] -= lr * gradW2[0];
      W2[1] -= lr * gradW2[1];
      b2 -= lr * gradB2;

      W1[0][0] -= lr * gradW1[0][0];
      W1[0][1] -= lr * gradW1[0][1];
      b1[0] -= lr * gradB1[0];

      W1[1][0] -= lr * gradW1[1][0];
      W1[1][1] -= lr * gradW1[1][1];
      b1[1] -= lr * gradB1[1];

      stepCount++;
      lastAction = `Lan truyền ngược & Cập nhật bước #${stepCount}`;
      forward();
    }

    function render() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      const isZeros = initSel.value === "zeros";

      // Node coordinates
      const nx = [60, 60];
      const ny = [70, 160];

      const hx = [250, 250];
      const hy = [70, 160];

      const ox = 450;
      const oy = 115;

      const lx = 590;
      const ly = 115;

      // Connections: x -> h
      for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 2; j++) {
          const w = W1[j][i];
          ctx.beginPath();
          ctx.moveTo(nx[i], ny[i]);
          ctx.lineTo(hx[j], hy[j]);
          ctx.lineWidth = Math.min(4, Math.max(1, Math.abs(w) * 3));
          ctx.strokeStyle = w >= 0 ? "#111" : "#888";
          ctx.stroke();

          // weight label
          const midX = nx[i] + (hx[j] - nx[i]) * 0.45;
          const midY = ny[i] + (hy[j] - ny[i]) * 0.45 + (i === j ? -6 : 6);
          ctx.fillStyle = "#333";
          ctx.font = "8px Georgia";
          ctx.fillText(`w=${w.toFixed(2)}`, midX, midY);
        }
      }

      // Connections: h -> out
      for (let j = 0; j < 2; j++) {
        const w = W2[j];
        ctx.beginPath();
        ctx.moveTo(hx[j], hy[j]);
        ctx.lineTo(ox, oy);
        ctx.lineWidth = Math.min(4, Math.max(1, Math.abs(w) * 3));
        ctx.strokeStyle = w >= 0 ? "#111" : "#888";
        ctx.stroke();

        const midX = hx[j] + (ox - hx[j]) * 0.45;
        const midY = hy[j] + (oy - hy[j]) * 0.45 + (j === 0 ? -6 : 6);
        ctx.fillStyle = "#333";
        ctx.font = "8px Georgia";
        ctx.fillText(`w=${w.toFixed(2)}`, midX, midY);
      }

      // Connection: out -> Loss
      ctx.beginPath();
      ctx.setLineDash([3, 3]);
      ctx.moveTo(ox, oy);
      ctx.lineTo(lx, ly);
      ctx.lineWidth = 1.5;
      ctx.strokeStyle = "#555";
      ctx.stroke();
      ctx.setLineDash([]);

      // Draw input nodes
      const x1 = parseFloat(x1Slider.value);
      const x2 = parseFloat(x2Slider.value);
      const inputs = [x1, x2];
      for (let i = 0; i < 2; i++) {
        ctx.beginPath();
        ctx.arc(nx[i], ny[i], 18, 0, Math.PI * 2);
        ctx.fillStyle = "#fafafa";
        ctx.fill();
        ctx.strokeStyle = "#111";
        ctx.lineWidth = 1.5;
        ctx.stroke();
        ctx.fillStyle = "#111";
        ctx.font = "bold 9px Georgia";
        ctx.textAlign = "center";
        ctx.fillText(`x${i+1}=${inputs[i].toFixed(1)}`, nx[i], ny[i] + 3);
      }

      // Draw hidden nodes
      for (let j = 0; j < 2; j++) {
        ctx.beginPath();
        ctx.arc(hx[j], hy[j], 22, 0, Math.PI * 2);
        ctx.fillStyle = isZeros ? "#333" : "#fff";
        ctx.fill();
        ctx.strokeStyle = "#111";
        ctx.lineWidth = 1.5;
        ctx.stroke();

        ctx.fillStyle = isZeros ? "#fff" : "#111";
        ctx.font = "bold 8px Georgia";
        ctx.textAlign = "center";
        ctx.fillText(`z=${z1[j].toFixed(2)}`, hx[j], hy[j] - 3);
        ctx.font = "8px Georgia";
        ctx.fillText(`a=${a1[j].toFixed(2)}`, hx[j], hy[j] + 8);
      }

      // Draw output node
      ctx.beginPath();
      ctx.arc(ox, oy, 24, 0, Math.PI * 2);
      ctx.fillStyle = "#111";
      ctx.fill();
      ctx.fillStyle = "#fff";
      ctx.font = "bold 9px Georgia";
      ctx.textAlign = "center";
      ctx.fillText(`z=${z2.toFixed(2)}`, ox, oy - 4);
      ctx.fillText(`ŷ=${yHat.toFixed(3)}`, ox, oy + 8);

      // Draw Loss box
      ctx.fillStyle = "#fff";
      ctx.fillRect(lx - 35, ly - 22, 70, 44);
      ctx.strokeStyle = "#111";
      ctx.lineWidth = 1.5;
      ctx.strokeRect(lx - 35, ly - 22, 70, 44);
      ctx.fillStyle = "#111";
      ctx.font = "bold 9px Georgia";
      ctx.fillText("Hàm Loss 𝓛", lx, ly - 6);
      ctx.font = "9px Georgia";
      ctx.fillText(loss.toFixed(4), lx, ly + 10);

      // Node column headers
      ctx.fillStyle = "#555";
      ctx.font = "10px Georgia";
      ctx.fillText("Đầu vào x", 60, 25);
      ctx.fillText("Tầng ẩn h", 250, 25);
      ctx.fillText("Đầu ra ŷ", 450, 25);
      ctx.fillText("Mất mát", 590, 25);

      // Warning banner if W = 0
      if (isZeros) {
        ctx.fillStyle = "rgba(0, 0, 0, 0.85)";
        ctx.fillRect(110, 195, 460, 25);
        ctx.fillStyle = "#fff";
        ctx.font = "bold 9px Georgia";
        ctx.fillText("⚠️ CÂU 56 VAIO: KHI W = 0, CÁC NƠ-RON CÙNG TẦNG CÓ a₁=a₂ VÀ NHẬN GRADIENT GIỐNG HỆT NHAU!", 340, 211);
      }

      // Update text output
      const target = parseFloat(targetSel.value);
      let outHtml = `
        <div style="display:flex; justify-content:space-between; flex-wrap:wrap; gap:8px;">
          <div><strong>Trạng thái:</strong> ${lastAction} | <strong>Số bước cập nhật:</strong> ${stepCount}</div>
          <div><strong>Dự đoán:</strong> ŷ = ${yHat.toFixed(4)} | <strong>Nhãn thật:</strong> y = ${target.toFixed(1)} | <strong>Loss:</strong> ${loss.toFixed(4)}</div>
        </div>
        <div style="margin-top:6px; font-size:0.8rem; line-height:1.4;">
          <strong>Tầng ẩn (l=1):</strong> z₁ = ${z1[0].toFixed(3)}, a₁ = ${a1[0].toFixed(3)} | z₂ = ${z1[1].toFixed(3)}, a₂ = ${a1[1].toFixed(3)}<br>
          <strong>Truyền ngược:</strong> Sai số tầng ra: δ^[2] = (ŷ - y) = ${delta2.toFixed(4)} | Sai số tầng ẩn: δ₁^[1] = ${delta1[0].toFixed(4)}, δ₂^[1] = ${delta1[1].toFixed(4)}<br>
          ${isZeros ? '<span style="color:#111; font-weight:bold; background:#e0e0e0; padding:2px 4px;">⚠️ HIỆN TƯỢNG ĐỐI XỨNG (CÂU 56): Vì W = 0, z₁ = z₂ = 0 và δ₁ = δ₂! Cả hai nơ-ron h₁ và h₂ cập nhật trọng số y hệt nhau, suy biến thành 1 nơ-ron! Hãy chuyển sang "Ngẫu nhiên (Xavier/He)" để phá vỡ đối xứng.</span>' : '<span style="color:#333;">✓ Trọng số ngẫu nhiên phá vỡ đối xứng thành công (Symmetry Broken). Các nơ-ron học độc lập các đặc trưng khác nhau!</span>'}
        </div>
      `;
      out.innerHTML = outHtml;
    }

    // Event listeners
    x1Slider.addEventListener("input", () => { x1Val.innerText = parseFloat(x1Slider.value).toFixed(1); forward(); });
    x2Slider.addEventListener("input", () => { x2Val.innerText = parseFloat(x2Slider.value).toFixed(1); forward(); });
    lrSlider.addEventListener("input", () => { lrVal.innerText = parseFloat(lrSlider.value).toFixed(2); });
    targetSel.addEventListener("change", () => { forward(); });
    actSel.addEventListener("change", () => { forward(); });
    initSel.addEventListener("change", () => { resetParams(); });

    btnFwd.addEventListener("click", () => { forward(); });
    btnBack.addEventListener("click", () => { backwardAndUpdate(); });
    btnEpoch.addEventListener("click", () => {
      for (let i = 0; i < 10; i++) backwardAndUpdate();
    });
    btnReset.addEventListener("click", () => { resetParams(); });

    resetParams();
  }

  // Widget 11: Generative AI & Diffusion Simulator
  function initDiffusionWidget() {
    const canvas = document.getElementById("diffCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");

    const tSlider = document.getElementById("diffT");
    const tVal = document.getElementById("diffTVal");
    const modeSel = document.getElementById("diffMode");
    const btnDenoise = document.getElementById("diffDenoiseBtn");
    const btnAddNoise = document.getElementById("diffAddNoiseBtn");
    const btnReset = document.getElementById("diffResetBtn");
    const out = document.getElementById("diffOut");
    if (!tSlider || !modeSel || !out) return;

    let animTimer = null;

    // Create an ideal 28x28 clean target image: a crisp circle and letter "AI"
    const size = 28;
    const cleanImg = new Float32Array(size * size);
    for (let y = 0; y < size; y++) {
      for (let x = 0; x < size; x++) {
        const dx = x - 14, dy = y - 14;
        const dist = Math.sqrt(dx * dx + dy * dy);
        let val = 0.05;
        // Ring
        if (dist > 9 && dist < 12) val = 0.85;
        // Center text AI pattern
        if (x >= 9 && x <= 13 && y >= 9 && y <= 19) {
          if (x === 9 || x === 13 || y === 9 || y === 14) val = 0.95;
        }
        if (x >= 16 && x <= 18 && y >= 9 && y <= 19) {
          if (x === 17 || y === 9 || y === 19) val = 0.95;
        }
        cleanImg[y * size + x] = val;
      }
    }

    // Static random noise buffer so noise looks consistent as t moves
    const noiseBuf = new Float32Array(size * size);
    for (let i = 0; i < size * size; i++) {
      const u1 = Math.max(1e-6, Math.random());
      const u2 = Math.random();
      noiseBuf[i] = Math.sqrt(-2.0 * Math.log(u1)) * Math.cos(2.0 * Math.PI * u2) * 0.45;
    }

    function render() {
      const t = parseInt(tSlider.value);
      tVal.innerText = t;
      const mode = modeSel.value;

      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Background
      ctx.fillStyle = "#fafafa";
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.strokeStyle = "#111";
      ctx.strokeRect(0, 0, canvas.width, canvas.height);

      // Box 1: Image view
      const imgPixelSize = 5;
      const startX = 35;
      const startY = 30;

      // Draw border
      ctx.fillStyle = "#fff";
      ctx.fillRect(startX - 2, startY - 2, size * imgPixelSize + 4, size * imgPixelSize + 4);
      ctx.strokeStyle = "#111";
      ctx.strokeRect(startX - 2, startY - 2, size * imgPixelSize + 4, size * imgPixelSize + 4);

      if (mode === "gan_collapse") {
        for (let y = 0; y < size; y++) {
          for (let x = 0; x < size; x++) {
            const grayVal = Math.floor(128 + (Math.random() - 0.5) * 6);
            ctx.fillStyle = `rgb(${grayVal},${grayVal},${grayVal})`;
            ctx.fillRect(startX + x * imgPixelSize, startY + y * imgPixelSize, imgPixelSize, imgPixelSize);
          }
        }
      } else {
        const alphaBar = Math.cos((t / 1000) * (Math.PI / 2)) ** 2;
        const sqrtAlpha = Math.sqrt(alphaBar);
        const sqrtOneMinusAlpha = Math.sqrt(Math.max(0, 1 - alphaBar));

        for (let y = 0; y < size; y++) {
          for (let x = 0; x < size; x++) {
            const idx = y * size + x;
            let pixelVal;
            if (mode === "diffusion") {
              pixelVal = sqrtAlpha * cleanImg[idx] + sqrtOneMinusAlpha * (noiseBuf[idx] + 0.5);
            } else {
              pixelVal = cleanImg[idx] * (1 - (t / 1000) * 0.4) + (noiseBuf[idx] * (t / 1000) * 0.4);
            }
            pixelVal = Math.min(1.0, Math.max(0.0, pixelVal));
            const c = Math.floor(pixelVal * 255);
            ctx.fillStyle = `rgb(${255 - c},${255 - c},${255 - c})`;
            ctx.fillRect(startX + x * imgPixelSize, startY + y * imgPixelSize, imgPixelSize, imgPixelSize);
          }
        }
      }

      // Image label
      ctx.fillStyle = "#111";
      ctx.font = "bold 11px Georgia";
      ctx.textAlign = "center";
      ctx.fillText(mode === "gan_collapse" ? "Ảnh Sinh Ra (Mode Collapse)" : `Tensor x_${t} (Bước t = ${t})`, startX + (size * imgPixelSize) / 2, startY + size * imgPixelSize + 18);

      // Middle Column: Metrics & Architecture Flow
      const midX = 220;
      ctx.textAlign = "left";
      ctx.font = "bold 11px Georgia";
      ctx.fillText("Thông Số Khuếch Tán & U-Net:", midX, 35);

      if (mode === "diffusion") {
        const alphaBar = (Math.cos((t / 1000) * (Math.PI / 2)) ** 2).toFixed(3);
        const noiseRatio = (Math.sqrt(1 - alphaBar) * 100).toFixed(1);
        const signalRatio = (Math.sqrt(alphaBar) * 100).toFixed(1);

        ctx.font = "10px Georgia";
        ctx.fillText(`• Hệ số tích lũy ᾱ_t: ${alphaBar}`, midX, 58);
        ctx.fillText(`• Tỉ lệ tín hiệu sạch: ${signalRatio}%`, midX, 76);
        ctx.fillText(`• Tỉ lệ nhiễu Gauss: ${noiseRatio}%`, midX, 94);

        ctx.fillStyle = "#eee";
        ctx.fillRect(midX, 105, 180, 12);
        ctx.fillStyle = "#111";
        ctx.fillRect(midX, 105, 180 * (signalRatio / 100), 12);
        ctx.strokeStyle = "#111";
        ctx.strokeRect(midX, 105, 180, 12);
        ctx.font = "8.5px Georgia";
        ctx.fillStyle = "#555";
        ctx.fillText("Độ sắc nét (Signal-to-Noise Ratio)", midX, 130);

        ctx.fillStyle = "#111";
        ctx.font = "10px Georgia";
        ctx.fillText(`Mục tiêu U-Net: Dự đoán vector nhiễu ε_θ(x_t, t)`, midX, 150);
        ctx.fillText(`Hàm mất mát: L_simple = ||ε - ε_θ||² (Ổn định 100%)`, midX, 168);
      } else if (mode === "gan_collapse") {
        ctx.fillStyle = "#b00";
        ctx.font = "bold 11px Georgia";
        ctx.fillText("PHÁT HIỆN SỰ CỐ: MODE COLLAPSE!", midX, 58);
        ctx.fillStyle = "#111";
        ctx.font = "10px Georgia";
        ctx.fillText("• Discriminator học quá nhanh, D(x) → 1, D(G(z)) → 0.", midX, 78);
        ctx.fillText("• Gradient truyền về Generator bị triệt tiêu hoàn toàn!", midX, 98);
        ctx.fillText("• Generator bỏ cuộc, sinh ảnh xám xịt hoặc lặp lại 1 mẫu.", midX, 118);
        ctx.font = "bold 9.5px Georgia";
        ctx.fillText("⇒ Trọng tâm Câu 61 Đề thi chính thức VAIO 2025!", midX, 142);
      } else {
        ctx.fillStyle = "#111";
        ctx.font = "10px Georgia";
        ctx.fillText("• GAN hoạt động ở điểm cân bằng Nash D(x) ≈ 0.5.", midX, 58);
        ctx.fillText("• Generator sinh ra mẫu đa dạng khi có gradient tốt.", midX, 78);
        ctx.fillText("• Huấn luyện 2 mạng đối kháng theo hàm Minimax V(D, G).", midX, 98);
      }

      // Right Column: Theory diagram / Comparison
      const rightX = 430;
      ctx.fillStyle = "#fff";
      ctx.fillRect(rightX, 22, 230, 155);
      ctx.strokeStyle = "#111";
      ctx.strokeRect(rightX, 22, 230, 155);

      ctx.fillStyle = "#111";
      ctx.font = "bold 10px Georgia";
      ctx.textAlign = "center";
      ctx.fillText("So Sánh GAN vs Diffusion (Olympic)", rightX + 115, 38);

      ctx.textAlign = "left";
      ctx.font = "9px Georgia";
      ctx.fillText("1. Độ ổn định:", rightX + 10, 58);
      ctx.fillText("• GAN: Dễ mất cân bằng, Mode Collapse.", rightX + 15, 72);
      ctx.fillText("• Diffusion: Hội tụ tối ưu lồi, không collapse.", rightX + 15, 86);

      ctx.fillText("2. Bản chất dự đoán:", rightX + 10, 104);
      ctx.fillText("• U-Net đoán nhiễu ε (chứ KHÔNG đoán ảnh x₀).", rightX + 15, 118);

      ctx.fillText("3. Triển khai thực tế:", rightX + 10, 136);
      ctx.fillText("• OOM GPU → Gradient Accumulation (Câu 51).", rightX + 15, 150);
      ctx.fillText("• Suy luận → ONNX & TensorRT (Câu 86).", rightX + 15, 164);

      // Output text
      if (mode === "diffusion") {
        if (t === 1000) {
          out.innerHTML = `Bước t = <strong>1000</strong>: Nhiễu trắng Gauss thuần túy $x_T \\sim \\mathcal{N}(0, \\mathbf{I})$. Mọi thông tin ban đầu đã bị xóa sạch hoàn toàn. Bấm <strong>'Chạy Khử Nhiễu'</strong> để quan sát U-Net trừ nhiễu!`;
        } else if (t === 0) {
          out.innerHTML = `Bước t = <strong>0</strong>: Hoàn tất 1000 bước khử nhiễu! Bức ảnh sạch $x_0$ đạt độ sắc nét tuyệt đối. Mạng U-Net đã bóc tách chính xác toàn bộ lượng nhiễu $\\boldsymbol{\\epsilon}_\\theta$ từng bước.`;
        } else {
          out.innerHTML = `Bước t = <strong>${t}</strong>: Trạng thái trung gian $x_t = \\sqrt{\\bar{\\alpha}_t} x_0 + \\sqrt{1 - \\bar{\\alpha}_t} \\boldsymbol{\\epsilon}$. U-Net quan sát $x_t$ và bước $t$ để dự đoán $\\boldsymbol{\\epsilon}_\\theta(x_t, t)$.`;
        }
      } else if (mode === "gan_collapse") {
        out.innerHTML = `<span style="color:#b00; font-weight:bold;">CÂU 61 VAIO:</span> Hiện tượng <strong>Mode Collapse</strong> xảy ra do mất cân bằng giữa Discriminator và Generator. Discriminator quá mạnh làm triệt tiêu gradient, khiến Generator chỉ sinh ra ảnh toàn màu xám hoặc lặp lại một mẫu duy nhất!`;
      } else {
        out.innerHTML = `<span style="font-weight:bold;">CÂU 95 VAIO:</span> Mạng GAN gồm <strong>Generator</strong> (tạo ảnh giả) và <strong>Discriminator</strong> (phân biệt thật giả) thi đấu đối kháng Minimax. Trong pha suy luận thực tế (Inference), ta vứt bỏ Discriminator và chỉ dùng Generator!`;
      }
    }

    tSlider.addEventListener("input", () => {
      clearInterval(animTimer);
      render();
    });

    modeSel.addEventListener("change", () => {
      clearInterval(animTimer);
      render();
    });

    btnDenoise.addEventListener("click", () => {
      clearInterval(animTimer);
      modeSel.value = "diffusion";
      tSlider.value = 1000;
      animTimer = setInterval(() => {
        let cur = parseInt(tSlider.value);
        if (cur <= 0) {
          clearInterval(animTimer);
          tSlider.value = 0;
          render();
        } else {
          tSlider.value = cur - 50;
          render();
        }
      }, 70);
    });

    btnAddNoise.addEventListener("click", () => {
      clearInterval(animTimer);
      modeSel.value = "diffusion";
      tSlider.value = 0;
      animTimer = setInterval(() => {
        let cur = parseInt(tSlider.value);
        if (cur >= 1000) {
          clearInterval(animTimer);
          tSlider.value = 1000;
          render();
        } else {
          tSlider.value = cur + 50;
          render();
        }
      }, 70);
    });

    btnReset.addEventListener("click", () => {
      clearInterval(animTimer);
      tSlider.value = 1000;
      modeSel.value = "diffusion";
      render();
    });

    render();
  }

  renderSidebar();
  updateProgress();

  const savedView = safeStorage.getItem("ml_current_view");
  if (savedView === "quiz") {
    switchView("quiz");
  } else {
    const savedLesson = safeStorage.getItem("ml_current_lesson");
    let startIdx = 0;
    if (savedLesson !== null) {
      const parsed = parseInt(savedLesson, 10);
      if (!isNaN(parsed) && parsed >= 0 && parsed < LESSONS_DATA.length) {
        startIdx = parsed;
      }
    }
    loadLesson(startIdx);
  }
}

if (typeof document !== 'undefined') {
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initVAIOApp);
  } else {
    initVAIOApp();
  }
}
