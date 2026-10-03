# -*- coding: utf-8 -*-
"""
bundle_index_html.py - Bundles styles.css, lessons.js, quiz.js, and app.js
into a single, 100% self-contained, offline-compatible index.html file.
"""

def main():
    print("Reading styles.css...")
    with open("styles.css", "r", encoding="utf-8") as f:
        styles_css = f.read()

    print("Reading lessons.js...")
    with open("lessons.js", "r", encoding="utf-8") as f:
        lessons_js = f.read()

    print("Reading quiz.js...")
    with open("quiz.js", "r", encoding="utf-8") as f:
        quiz_js = f.read()

    print("Reading app.js...")
    with open("app.js", "r", encoding="utf-8") as f:
        app_js = f.read()

    html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>Sổ Tay Học Máy: Từ Con Số 0 Đến Chuyên Gia</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<style>
{styles_css}
</style>
</head>
<body>
<div class="app-container">
  <div class="sidebar-backdrop" id="sidebarBackdrop"></div>
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-header">
      <div class="brand">
        <h1>Sổ Tay Học Máy</h1>
        <span class="brand-subtitle">Machine Learning & Deep Learning</span>
      </div>
      <button class="sidebar-close-btn" id="sidebarCloseBtn" aria-label="Đóng menu">✕</button>
    </div>
    <div class="search-wrap">
      <input type="text" id="searchInput" class="search-input" placeholder="Tìm kiếm bài học, khái niệm...">
    </div>
    <nav class="nav-menu" id="lessonNav"></nav>
    <div class="sidebar-footer">
      <div class="progress-wrap">
        <div class="progress-info">
          <span>Tiến trình hoàn thành</span>
          <span id="progressText">0/13 bài</span>
        </div>
        <div class="progress-bar-bg">
          <div class="progress-bar-fill" id="progressBarFill" style="width: 0%;"></div>
        </div>
      </div>
      <button class="btn-text-subtle" id="resetProgressBtn" title="Đặt lại toàn bộ tiến trình học">Đặt lại</button>
    </div>
  </aside>
  <main class="main-content">
    <header class="top-bar">
      <div class="top-bar-left">
        <button class="sidebar-toggle-btn" id="sidebarToggleBtn" aria-label="Mở danh mục">☰</button>
        <div class="breadcrumb" id="breadcrumbText">Bài 1: Đạo Hàm, Đạo Hàm Riêng & Vector Gradient</div>
      </div>
      <div class="top-actions">
        <button class="btn" id="toggleQuizBtn">Đề Thi (24 Câu)</button>
        <button class="btn btn-print" onclick="window.print()">In</button>
      </div>
    </header>
    <article class="article-container" id="articleContainer"></article>
    <div class="article-container quiz-container" id="quizContainer"></div>
  </main>
  <!-- Fullscreen Diagram Zoom Lightbox Modal -->
  <div class="diagram-modal" id="diagramModal">
    <div class="diagram-modal-backdrop" id="diagramModalBackdrop"></div>
    <div class="diagram-modal-content">
      <button class="diagram-modal-close" id="diagramModalClose" aria-label="Đóng">✕</button>
      <div class="diagram-modal-body" id="diagramModalBody"></div>
      <div class="diagram-modal-caption" id="diagramModalCaption"></div>
    </div>
  </div>

</div>
<script>
{lessons_js}
</script>
<script>
{quiz_js}
</script>
<script>
{app_js}
</script>
</body>
</html>
"""

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template)

    print(f"index.html successfully compiled ({len(html_template)} bytes).")

if __name__ == "__main__":
    main()
