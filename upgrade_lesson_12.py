# -*- coding: utf-8 -*-
"""
upgrade_lesson_12.py - Masterpiece Lesson 12 for VAIO 2025 AI Olympiad
Chủ đề: Xử Lý Ngôn Ngữ Tự Nhiên (NLP), Attention & LLMs
Toàn diện từ con số 0 đến làm chủ sâu sắc.

Tuân thủ nghiêm ngặt chuẩn sư phạm:
Trực giác đời sống -> Bản chất toán học -> Cách thức hoạt động ->
Giải mã ký hiệu cho học sinh lớp 12 -> Ví dụ tính toán bằng số từng bước ->
Cạm bẫy phòng thi -> Câu hỏi trắc nghiệm kiểm tra độ hiểu có lời giải chi tiết.
"""

def get_masterpiece_lesson_12():
    return {
        "id": "lesson-12",
        "title": "12. Xử Lý Ngôn Ngữ Tự Nhiên (NLP), Attention & LLMs",
        "syllabusBadge": "BUỔI 10 & 11: NLP, ATTENTION & LARGE LANGUAGE MODELS (LLMs)",
        "summary": "Chinh phục thế giới Xử Lý Ngôn Ngữ Tự Nhiên (NLP) và Trí Tuệ Nhân Tạo Tạo Sinh từ con số 0: Nắm vững thứ tự 4 bước tiền xử lý văn bản chuẩn mực và quy luật từ dừng Zipf (Câu 14 VAIO); giải mã không gian nhúng từ ngữ nghĩa Word2Vec (CBOW vs Skip-gram) và GloVe từ ma trận đồng xuất hiện toàn cục (Câu 19 & 91 VAIO); phân tích mạng nơ-ron chuỗi hồi quy RNN, LSTM và công thức đếm tham số mô hình (Câu 4 VAIO); thấu suốt cơ chế Tự Chú Ý (Self-Attention), bộ ba Query-Key-Value và lý do chia căn bậc hai d_k (Câu 74 VAIO); so sánh toàn diện kiến trúc Transformer Encoder-only (BERT - Câu 20 & 65) vs Decoder-only (GPT); cùng kỹ thuật Prompt Engineering và chuỗi suy luận Chain-of-Thought (CoT - Câu 16 VAIO).",
        "intuition": {
            "title": "Trực giác thực tế: Bữa tiệc ồn ào Cocktail Party & Chiếc kính lúp ngữ cảnh soi thấu từ ngữ",
            "content": r"""Để thấu hiểu tại sao ngành Trí Tuệ Nhân Tạo lại tạo nên cơn địa chấn toàn cầu với ChatGPT, Claude hay Gemini, hãy cùng xuất phát từ hai câu chuyện đời sống mộc mạc sau:

**1. Hiệu ứng tiệc Cocktail (Cocktail Party Effect) & Cơ chế Tự Chú Ý (Self-Attention):**
- Hãy tưởng tượng bạn đang đứng giữa một hội trường dạ tiệc với 500 người đang nâng ly và trò chuyện ầm ĩ. Màng nhĩ của bạn tiếp nhận một mớ âm thanh hỗn độn, nếu bạn cố gắng lắng nghe tất cả cùng lúc một cách cào bằng, bạn sẽ không hiểu được bất kỳ ai nói gì.
- Thế nhưng, khi một người bạn ở góc xa khẽ cất tiếng gọi tên bạn: *"Bảo ơi!"*, ngay lập tức bộ não của bạn kích hoạt một cơ chế kỳ diệu: **Sự chú ý có chọn lọc (Selective Attention)**! Bạn dồn 90% thính giác về hướng người bạn đó, trong khi toàn bộ tiếng ồn của 499 người còn lại tự động bị đẩy xuống làm nền mờ nhạt.
- Trong ngôn ngữ học máy tính cũng y hệt như vậy! Hãy đọc câu sau:
  $$\text{"Con gấu không thể trèo qua hàng rào gỗ vì NÓ quá nặng."}$$
  Làm sao máy tính biết từ **"NÓ"** đang ám chỉ **"con gấu"** hay **"hàng rào"**?
  - Các mô hình nơ-ron thế hệ cũ đọc từng từ một theo thứ tự thời gian, đến cuối câu chúng thường "quên mất" đầu câu và nhầm lẫn tai hại.
  - Cơ chế **Self-Attention (Tự Chú Ý)** của kiến trúc Transformer cho phép từ **"NÓ"** phóng ánh nhìn tới TẤT CẢ các từ khác trong câu cùng một lúc, phát hiện ra sự liên kết mạnh mẽ với cụm từ *"quá nặng"* và gán trọng số chú ý lên tới **85% vào "con gấu"**! Máy tính hiểu trọn vẹn ngữ cảnh tự nhiên như một con người thông thái.

---

**2. Người thợ gốm và nhà văn tạo sinh: Từ chiếc bình tĩnh Word2Vec đến dòng chảy biến ảo Transformer:**
- Trước kỷ nguyên Transformer, các nhà khoa học biểu diễn từ ngữ bằng **Word2Vec**: mỗi từ vựng được gán cho một vector cố định trong không gian. Từ *"ngân hàng"* trong *"ngân hàng thương mại"* hay *"ngân hàng máu"* đều bị ép dùng chung một vector bất biến, giống như một chiếc bình gốm đã nung cứng không thể biến đổi hình dạng.
- Transformer và các Mô Hình Ngôn Ngữ Lớn (LLMs) ngày nay hoạt động như dòng nước linh hoạt: vector biểu diễn của một từ được **nhào nặn liên tục theo các từ đứng xung quanh nó**. Cùng một từ *"sao"*, khi đứng cạnh *"bầu trời"* nó biến thành ngôi sao thiên văn, khi đứng cạnh *"tại"* nó biến thành từ để hỏi nghi vấn!"""
        },
        "sections": [
            # =================================================================
            # MỤC 12.1: TIỀN XỬ LÝ VĂN BẢN 4 BƯỚC & TỪ DỪNG (CÂU 14 VAIO)
            # =================================================================
            {
                "heading": "12.1. Khởi Đầu Từ Con Số 0: Máy Tính 'Đọc' Chữ Như Thế Nào? Thứ Tự 4 Bước Tiền Xử Lý Chuẩn (Câu 14 VAIO) & Bài Toán Từ Dừng",
                "content": "Khám phá cách thức máy tính tiếp nhận chuỗi ký tự thô; quy trình 4 bước tiền xử lý văn bản chuẩn mực trong đề thi Olympic AI; thách thức tách từ tiếng Việt và định luật Zipf giải thích bản chất của việc loại bỏ từ dừng.",
                "deepDive": r"""**1. Máy tính 'nhìn' văn bản như thế nào?**
Con người chúng ta nhìn thấy câu chữ và lập tức liên tưởng đến hình ảnh, cảm xúc và ý niệm trong đời thực. Nhưng bộ vi xử lý máy tính (CPU/GPU) bản chất chỉ là những mạch bán dẫn số học, nó **HOÀN TOÀN MÙ CHỮ**. Máy tính không hề biết *"mèo"*, *"chó"*, *"yêu"* hay *"ghét"* nghĩa là gì, nó chỉ thao tác được trên các con số nguyên (integers) và số thực (floats).

Văn bản thô (Raw text) thu thập từ Internet, báo chí, mạng xã hội luôn là mớ hỗn độn phi cấu trúc: lẫn lộn chữ hoa chữ thường, dấu câu sai quy chuẩn, mã HTML, đường dẫn link, biểu tượng cảm xúc (emojis) và các lỗi chính tả. Nếu đưa trực tiếp đống rác dữ liệu này vào mô hình học máy, mô hình sẽ hoàn toàn sụp đổ. Do đó, bước đi đầu tiên bắt buộc của mọi bài toán NLP là **Quy Trình Tiền Xử Lý Văn Bản (Text Preprocessing Pipeline)**.

---

**2. Quy trình 4 bước tiền xử lý văn bản chuẩn mực (CÂU 14 ĐỀ THI CHÍNH THỨC VAIO 2025):**
Trong đề thi Olympic AI, thứ tự thực hiện các bước là một câu hỏi lý thuyết then chốt. Quy trình chuẩn mực quốc tế diễn ra tuần tự theo đúng 4 bước logic sau:

```
[Văn bản thô] 
     │
     ▼ (Bước 1)
[Chuẩn Hóa Văn Bản (Normalization)] 
     │   • Hạ chữ thường (Lowercasing)
     │   • Xóa dấu câu, HTML, ký tự đặc biệt, chuẩn hóa Unicode
     ▼ (Bước 2)
[Tách Từ (Tokenization)]
     │   • Cắt chuỗi thành danh sách token rời rạc: [t₁, t₂, ..., tₙ]
     ▼ (Bước 3)
[Rút Gọn Từ (Stemming & Lemmatization)]
     │   • Đưa các biến thể từ về dạng gốc cốt lõi
     ▼ (Bước 4)
[Gán Nhãn Từ Loại (POS Tagging)]
         • Xác định vai trò ngữ pháp (Danh từ, Động từ, Tính từ, ...)
```

Hãy cùng mổ xẻ chi tiết từng bước:

- **Bước 1: Chuẩn hóa văn bản (Text Normalization):**
  - **Hạ chữ thường (Lowercasing):** Máy tính phân biệt ký tự theo mã ASCII/Unicode. Nếu không chuẩn hóa, chữ `'Học'` (mã 72) và `'học'` (mã 104) sẽ bị coi là hai từ vựng hoàn toàn xa lạ nhau! Việc hạ toàn bộ về chữ thường giúp gom chúng về cùng một biểu diễn duy nhất.
  - **Làm sạch ký tự (Cleaning):** Loại bỏ dấu câu (`. , ! ? : ;`), thẻ HTML (`<br>`, `<p>`), đường dẫn web (`http://...`) và khoảng trắng thừa.
  - **Chuẩn hóa Unicode tiếng Việt:** Tiếng Việt có hai kiểu gõ dấu thanh: **Unicode tổ hợp (NFD)** (ký tự gốc ghép với ký tự dấu) và **Unicode dựng sẵn (NFC)** (ký tự có sẵn dấu). Cùng chữ `'á'`, dựng sẵn là 1 ký tự (`\u00E1`), tổ hợp là 2 ký tự (`a` + `\u0301`). Chuẩn hóa về NFC là bắt buộc để tránh phân mảnh từ điển!

- **Bước 2: Tách từ (Tokenization):**
  - Là thao tác bẻ gãy chuỗi ký tự dài thành các đơn vị ngữ nghĩa nhỏ nhất gọi là **Token** (có thể là từ, từ con subword hoặc ký tự).
  - *Thách thức đặc thù của Tiếng Việt:* Tiếng Anh là ngôn ngữ phân tích tách rời bằng dấu cách (Space-delimited: *"Machine learning"* có 2 từ rõ ràng). Tiếng Việt là ngôn ngữ đơn lập đa âm tiết, ranh giới từ không trùng với dấu cách!
    - Ví dụ: Cụm từ *"học sinh học sinh học"*. Nếu chỉ cắt theo dấu cách, ta được các tiếng rời rạc: `['học', 'sinh', 'học', 'sinh', 'học']` $\to$ mất sạch ngữ nghĩa!
    - Công cụ tách từ tiếng Việt (như `pyvi`, `underthesea`, `VnCoreNLP`) phải nhận diện được từ ghép:
      $$\text{"Học sinh (học sinh) học (học) sinh học (sinh học)"} \implies \text{['học_sinh', 'học', 'sinh_học']}$$
  - *Kỷ nguyên Subword Tokenization (BPE, WordPiece):* Các mô hình hiện đại (như BERT, GPT) sử dụng kỹ thuật tách từ con để xử lý triệt để bài toán **Từ ngoài từ điển (OOV - Out of Vocabulary)**. Từ hiếm *"unhappiness"* được tách thành `['un', '##happi', '##ness']`.

- **Bước 3: Rút gọn từ (Stemming & Lemmatization):**
  - Trong ngôn ngữ biến hình (như tiếng Anh), một từ có rất nhiều biến thể chia thì hay số nhiều: *"study", "studying", "studies", "studied"*. Rút gọn từ giúp đưa chúng về cùng một gốc để giảm độ phình to của từ điển.
  - **Stemming (Cắt gốc từ kinh nghiệm):** Dùng thuật toán luật thô sơ (như Porter Stemmer, Snowball) chặt bỏ đuôi từ (`-ing`, `-ed`, `-es`). Ưu điểm: Rất nhanh. Nhược điểm: Có thể tạo ra chuỗi vô nghĩa trong từ điển (Ví dụ: *"troubled"* $\to$ *"troubl"*, *"crying"* $\to$ *"cri"*).
  - **Lemmatization (Đưa về từ nguyên mẫu từ điển):** Dựa trên phân tích hình thái học chuyên sâu và từ điển ngữ pháp để đưa từ về dạng nguyên mẫu hợp lệ (Lemma). Ví dụ: *"better"* $\to$ *"good"*, *"was"* $\to$ *"be"*, *"mice"* $\to$ *"mouse"*. Chính xác tuyệt đối nhưng tốn thời gian tính toán hơn.

- **Bước 4: Gán nhãn từ loại (POS Tagging - Part-of-Speech Tagging):**
  - Gán nhãn ngữ pháp cho từng token trong câu: Danh từ (NOUN), Động từ (VERB), Tính từ (ADJ), Đại từ (PRON), v.v.
  - Đóng vai trò then chốt để giải nghĩa các từ đồng âm khác nghĩa (Ví dụ trong tiếng Anh: *"I can (AUX) buy a can (NOUN) of soda"*).

---

**3. Khái niệm Từ Dừng (Stopwords) & Định Luật Zipf (Câu 99):**
- **Từ dừng (Stopwords):** Là những từ ngữ xuất hiện với mật độ cực kỳ dày đặc trong mọi văn bản nhưng hầu như không mang giá trị ngữ nghĩa phân loại chuyên biệt (Ví dụ trong tiếng Việt: *"và", "của", "thì", "là", "những", "các", "ở"*; trong tiếng Anh: *"the", "is", "at", "which", "on"*).
- **Định luật Zipf (Zipf's Law):** Trong bất kỳ kho ngữ liệu ngôn ngữ tự nhiên nào, tần suất xuất hiện $f(r)$ của một từ tỉ lệ nghịch với thứ hạng tần suất $r$ của nó:
  $$f(r) \propto \frac{1}{r}$$
  Từ đứng hạng 1 (`"the"`) xuất hiện nhiều gấp đôi từ đứng hạng 2 (`"of"`), gấp 10 lần từ đứng hạng 10! Một nhóm nhỏ vài chục từ dừng chiếm tới hơn 30% - 50% tổng số lượng từ của toàn bộ kho văn bản.
- **Tại sao cần loại bỏ từ dừng trong NLP truyền thống?**
  - Thu nhỏ kích thước ma trận và không gian đặc trưng (giảm chiều vector từ).
  - Giảm thiểu tài nguyên bộ nhớ RAM và thời gian huấn luyện.
  - Tránh để các từ đệm vô thưởng vô phạt lấn át tín hiệu của các từ khóa đặc trưng (keywords) trong các bài toán phân loại văn bản (như Naive Bayes, TF-IDF).
- *Lưu ý quan trọng trong kỷ nguyên Deep Learning & LLM:* Với Transformer và LLMs hiện đại, người ta **KHÔNG CÒN LOẠI BỎ TỪ DỪNG** nữa, vì các từ nối như *"not", "never", "and", "but"* mang ý nghĩa cú pháp và đảo ngược logic sống còn đối với sự hiểu của mô hình!""" ,
                "formula": r"\text{Pipeline: Normalization} \xrightarrow{} \text{Tokenization} \xrightarrow{} \text{Stemming} \xrightarrow{} \text{POS Tagging}, \quad f(r) \propto \frac{1}{r}",
                "mathExplainer": [
                    { "sym": r"\text{Normalization}", "name": "Chuẩn hóa văn bản", "mean": "Đưa văn bản về dạng thống nhất: hạ chữ thường, xóa dấu câu và ký tự rác." },
                    { "sym": r"\text{Tokenization}", "name": "Tách từ", "mean": "Bẻ gãy chuỗi văn bản thành danh sách các token rời rạc để máy tính xử lý." },
                    { "sym": r"\text{Stemming vs Lemmatization}", "name": "Rút gọn gốc từ", "mean": "Stemming cắt đuôi từ bằng luật kinh nghiệm; Lemmatization đưa về nguyên mẫu từ điển." },
                    { "sym": r"\text{POS Tagging}", "name": "Gán nhãn từ loại", "mean": "Xác định vai trò cú pháp ngữ pháp của token (Danh từ, Động từ, Tính từ,...)." },
                    { "sym": r"f(r) \propto 1/r", "name": "Định luật Zipf", "mean": "Tần suất xuất hiện của từ tỉ lệ nghịch với thứ hạng tần suất; cơ sở lọc từ dừng (stopwords)." }
                ],
                "diagram": {
                    "svg": r"""<svg viewBox="0 0 660 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
                      <rect width="660" height="170" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(15, 18)">
                        <text x="315" y="14" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Quy Trình 4 Bước Tiền Xử Lý Văn Bản Chuẩn Mực (Câu 14 VAIO)</text>
                        <!-- Step 1 -->
                        <rect x="0" y="35" width="135" height="52" fill="#fff" stroke="#111" stroke-width="1.5" rx="3"/>
                        <text x="67" y="55" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">1. Chuẩn Hóa</text>
                        <text x="67" y="69" font-family="Georgia" font-size="8" text-anchor="middle">(Normalization)</text>
                        <text x="67" y="80" font-family="Georgia" font-size="7.5" fill="#555" text-anchor="middle">Hạ thường, xóa dấu câu</text>
                        <!-- Arrow 1-2 -->
                        <line x1="135" y1="61" x2="160" y2="61" stroke="#111" stroke-width="1.5"/>
                        <polygon points="160,61 154,58 154,64" fill="#111"/>
                        <!-- Step 2 -->
                        <rect x="160" y="35" width="135" height="52" fill="#fff" stroke="#111" stroke-width="1.5" rx="3"/>
                        <text x="227" y="55" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">2. Tách Từ</text>
                        <text x="227" y="69" font-family="Georgia" font-size="8" text-anchor="middle">(Tokenization)</text>
                        <text x="227" y="80" font-family="Georgia" font-size="7.5" fill="#555" text-anchor="middle">Cắt thành mảng token</text>
                        <!-- Arrow 2-3 -->
                        <line x1="295" y1="61" x2="320" y2="61" stroke="#111" stroke-width="1.5"/>
                        <polygon points="320,61 314,58 314,64" fill="#111"/>
                        <!-- Step 3 -->
                        <rect x="320" y="35" width="140" height="52" fill="#fff" stroke="#111" stroke-width="1.5" rx="3"/>
                        <text x="390" y="55" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">3. Rút Gọn Từ</text>
                        <text x="390" y="69" font-family="Georgia" font-size="8" text-anchor="middle">(Stemming/Lemma)</text>
                        <text x="390" y="80" font-family="Georgia" font-size="7.5" fill="#555" text-anchor="middle">Đưa về gốc từ cốt lõi</text>
                        <!-- Arrow 3-4 -->
                        <line x1="460" y1="61" x2="485" y2="61" stroke="#111" stroke-width="1.5"/>
                        <polygon points="485,61 479,58 479,64" fill="#111"/>
                        <!-- Step 4 -->
                        <rect x="485" y="35" width="145" height="52" fill="#111" rx="3"/>
                        <text x="557" y="55" font-family="Georgia" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">4. Gán Nhãn Từ Loại</text>
                        <text x="557" y="69" font-family="Georgia" font-size="8" fill="#ddd" text-anchor="middle">(POS Tagging)</text>
                        <text x="557" y="80" font-family="Georgia" font-size="7.5" fill="#bbb" text-anchor="middle">Gán nhãn NOUN, VERB...</text>
                        <!-- Bottom illustrative box -->
                        <rect x="0" y="102" width="630" height="42" fill="#f0f0f0" stroke="#ccc" stroke-dasharray="3,3" rx="2"/>
                        <text x="15" y="118" font-family="Georgia" font-size="9" font-weight="bold">Ví dụ minh họa:</text>
                        <text x="95" y="118" font-family="Georgia" font-size="8.5">"Học sinh đang học AI!"  →  [Hạ thường, bỏ !] "học sinh đang học ai"</text>
                        <text x="95" y="132" font-family="Georgia" font-size="8.5">→  [Tokenize &amp; Lọc từ dừng &quot;đang&quot;] ['học_sinh', 'học', 'ai']  →  [POS] ['học_sinh'/N, 'học'/V, 'ai'/N]</text>
                      </g>
                    </svg>""",
                    "caption": "Sơ đồ dòng chảy 4 bước chuẩn mực tiền xử lý văn bản NLP: Chuẩn hóa -> Tách từ -> Rút gọn từ -> Gán nhãn từ loại."
                },
                "commonPitfalls": r"""Cạm bẫy phòng thi Câu 14 Đề thi chính thức VAIO 2025:
1. **Lỗi đảo lộn thứ tự Tách từ và Chuẩn hóa:** Rất nhiều thí sinh chọn Tách từ trước Chuẩn hóa. SAI! Nếu chưa chuẩn hóa (chưa xóa dấu chấm, phẩy, chưa hạ chữ thường), thao tác tách từ sẽ bị nhiễu loạn nặng nề (Ví dụ từ `'cuối.'` bị dính liền dấu chấm thành một token lạ).
2. **Lỗi xóa từ dừng trước khi tách từ:** Muốn so khớp một từ với danh sách từ dừng (Stopwords list), văn bản bắt buộc phải được cắt thành từng token độc lập ở Bước 2!
3. **Ghi nhớ thứ tự chuẩn mực Câu 14:** 2 (Chuẩn hóa) → 1 (Tách từ) → 3 (Rút gọn từ) → 4 (Gán nhãn từ loại).""",
                "practiceQuestion": {
                    "level": "Cơ bản (Câu 14 Đề Thi Chính Thức VAIO 2025)",
                    "question": "Trong xử lý ngôn ngữ tự nhiên (NLP), đâu là thứ tự đúng của các bước xử lý cơ bản? (1. Tách từ; 2. Chuẩn hóa; 3. Rút gọn từ; 4. Gán nhãn từ loại)",
                    "options": [
                        "A. 2 (Chuẩn hóa) → 1 (Tách từ) → 4 (Gán nhãn từ loại) → 3 (Rút gọn từ)",
                        "B. 2 (Chuẩn hóa) → 1 (Tách từ) → 3 (Rút gọn từ) → 4 (Gán nhãn từ loại)",
                        "C. 1 (Tách từ) → 3 (Rút gọn từ) → 2 (Chuẩn hóa) → 4 (Gán nhãn từ loại)",
                        "D. 1 (Tách từ) → 2 (Chuẩn hóa) → 4 (Gán nhãn từ loại) → 3 (Rút gọn từ)"
                    ],
                    "correctIndex": 1,
                    "hint": "Phải chuẩn hóa văn bản trước tiên (hạ thường, bỏ ký tự lạ), sau đó tách thành từng từ, rồi mới rút gọn gốc từ và cuối cùng gán nhãn ngữ pháp.",
                    "solution": [
                        "Bước 1: Chuẩn hóa văn bản (Normalization - bước số 2 trong đề bài) nhằm đồng nhất định dạng ký tự, hạ chữ thường, làm sạch dấu câu.",
                        "Bước 2: Tách từ (Tokenization - bước số 1 trong đề bài) để chia nhỏ chuỗi thành danh sách các token rời rạc.",
                        "Bước 3: Rút gọn từ (Stemming/Lemmatization - bước số 3 trong đề bài) để đưa các từ biến thể về dạng gốc.",
                        "Bước 4: Gán nhãn từ loại (POS Tagging - bước số 4 trong đề bài) để xác định vai trò cú pháp ngữ pháp của token trong câu.",
                        "Trình tự logic chuẩn xác là: 2 → 1 → 3 → 4. Đáp án chính xác là B."
                    ]
                }
            },

            # =================================================================
            # MỤC 12.2: KHÔNG GIAN NHÚNG TỪ: WORD2VEC & GLOVE (CÂU 19 & 91 VAIO)
            # =================================================================
            {
                "heading": "12.2. Không Gian Ngữ Nghĩa (Word Embeddings): Từ Thất Bại Của One-Hot Đến Word2Vec (CBOW vs Skip-gram) & GloVe (Câu 19, 91 VAIO)",
                "content": "Khám phá nguyên nhân thất bại chí mạng của mã hóa One-Hot; giả thuyết phân bố ngôn ngữ học; kiến trúc Word2Vec (CBOW đoán từ trung tâm, Skip-gram đoán ngữ cảnh); kỹ thuật Negative Sampling và mô hình GloVe huấn luyện từ ma trận đồng xuất hiện toàn cục.",
                "deepDive": r"""**1. Thất bại chí mạng của Mã Hóa One-Hot (One-Hot Encoding):**
Cách trực giác đơn giản nhất để biến một từ thành con số là đánh số thứ tự từ điển: từ điển có $|V|$ từ vựng (ví dụ $|V| = 50,000$), từ thứ $i$ sẽ được biểu diễn bằng một vector kích thước $50,000$ chiều với duy nhất số $1$ tại vị trí $i$ và $49,999$ số $0$ ở các vị trí còn lại.

Phương pháp ngây thơ này vấp phải hai bức tường bế tắc:
- **Bùng nổ số chiều và lãng phí bộ nhớ (Curse of Dimensionality & Extreme Sparsity):** Vector kích thước 50,000 phần tử mà có tới 99.998% là số 0 vô dụng. Lưu trữ một văn bản ngắn tốn hàng chục Megabytes ma trận thưa.
- **Tính trực giao triệt tiêu ngữ nghĩa (Complete Orthogonality):**
  - Tích vô hướng giữa hai vector one-hot bất kỳ $\mathbf{w}_i$ và $\mathbf{w}_j$ ($i \neq j$) luôn luôn bằng 0:
    $$\mathbf{w}_i^T \mathbf{w}_j = 0$$
  - Khoảng cách Euclid giữa hai từ bất kỳ luôn luôn bằng hằng số cố định:
    $$d(\mathbf{w}_i, \mathbf{w}_j) = \sqrt{(1 - 0)^2 + (0 - 1)^2} = \sqrt{2} \approx 1.414$$
  - *Hậu quả tai hại:* Máy tính coi từ *"chó"* và từ *"mèo"* xa lạ nhau y hệt như từ *"chó"* và *"tàu ngầm"*! Mọi mối quan hệ tương đồng ngữ nghĩa, đồng nghĩa hay trái nghĩa bị xóa sổ hoàn toàn.

---

**2. Giả thuyết phân bố (Distributional Hypothesis) & Ý niệm Không Gian Nhúng (Word Embeddings):**
Năm 1957, nhà ngôn ngữ học lừng danh J.R. Firth đã đưa ra một châm ngôn kinh điển làm thay đổi lịch sử AI:
$$\text{"You shall know a word by the company it keeps" (Bạn sẽ hiểu nghĩa của một từ thông qua những người bạn đi cùng nó!)}$$
Nếu từ *"cam"*, *"táo"*, *"xoài"* đều thường xuyên xuất hiện cạnh các từ *"ngọt"*, *"chua"*, *"ăn"*, *"nước ép"*, thì bộ não và máy tính hoàn toàn có thể suy luận rằng chúng thuộc cùng nhóm "trái cây"!

**Word Embedding (Nhúng từ ngữ nghĩa):**
Thay vì dùng vector thưa 50,000 chiều, ta chiếu mỗi từ vào một **vector đậm đặc (Dense Vector)** số thực trong không gian $d$ chiều khiêm tốn ($d \in [100, 300]$). Trong không gian này:
- Các từ có ngữ nghĩa tương đồng sẽ nằm gần nhau (khoảng cách Euclid nhỏ, Cosine Similarity gần $1.0$).
- Các trục tọa độ tự động học được các khái niệm trừu tượng như: Giới tính, Giống loài, Thì thời gian, Địa vị xã hội.

---

**3. Mô hình Word2Vec (Tomas Mikolov et al., Google 2013):**
Word2Vec là một mạng nơ-ron nông 2 tầng (không có phi tuyến tính ẩn) huấn luyện tự giám sát (self-supervised) trên hàng tỷ câu văn bản. Có hai kiến trúc đối trọng nhau:

- **Kiến trúc CBOW (Continuous Bag-of-Words - CÂU 91 ĐỀ THI VAIO 2025):**
  - **Mục tiêu:** Sử dụng **các từ ngữ cảnh xung quanh (Context words)** để dự đoán **từ trung tâm (Target word $w_t$)**!
  - Cho cửa sổ ngữ cảnh kích thước $C$: $\{w_{t-c}, \dots, w_{t-1}, w_{t+1}, \dots, w_{t+c}\}$.
  - Mô hình lấy trung bình cộng các vector của các từ ngữ cảnh:
    $$\mathbf{h} = \frac{1}{2c} \sum_{-c \le j \le c, j \neq 0} \mathbf{v}_{w_{t+j}}$$
  - Sau đó nhân với ma trận chiếu đầu ra $W'$ để tính điểm số logits và qua hàm Softmax để tối đa hóa xác suất có điều kiện $P(w_t \mid \text{Context})$.
  - *Ưu điểm:* Tốc độ huấn luyện cực nhanh, biểu diễn rất mượt mà và chính xác cho các từ thông dụng có tần suất cao.

- **Kiến trúc Skip-gram:**
  - **Mục tiêu:** Sử dụng **DUY NHẤT 1 từ trung tâm ($w_t$)** để dự đoán **tất cả các từ ngữ cảnh xung quanh** trong cửa sổ trượt!
  - *Ưu điểm:* Do mỗi từ đơn lẻ buộc phải dự đoán nhiều từ ngữ cảnh, Skip-gram học cực kỳ xuất sắc biểu diễn cho các **từ hiếm gặp (Rare words)**.

- **Kỹ thuật Lấy Mẫu Âm (Negative Sampling - Câu 28, 41):**
  - Hàm Softmax truyền thống có mẫu số tính tổng qua toàn bộ từ điển: $\sum_{w=1}^{|V|} \exp(\mathbf{v}'_w \cdot \mathbf{h})$. Với $|V| = 100,000$, việc tính mẫu số này ở mỗi bước cập nhật trọng số là thảm họa tính toán.
  - Negative Sampling biến bài toán phân loại đa lớp $|V|$ nhãn thành bài toán phân loại nhị phân (Logistic Regression):
    - Với cặp từ thật $(w_t, c)$, mô hình tối đa hóa xác suất nhãn $1$: $\log \sigma(\mathbf{v}'_c \cdot \mathbf{v}_{w_t})$.
    - Đồng thời, mô hình bốc ngẫu nhiên $K$ từ giả (negative words, $K \approx 5 - 20$) từ từ điển và tối thiểu hóa xác suất của chúng: $\sum_{k=1}^K \log \sigma(-\mathbf{v}'_{w_{\text{neg}}} \cdot \mathbf{v}_{w_t})$.
    - Phân phối bốc từ âm: Sử dụng phân phối Unigram lũy thừa $\alpha = 0.75$: $P_n(w) \propto U(w)^{0.75}$ để giúp các từ hiếm cũng có cơ hội được chọn làm mẫu âm.
    - Giảm chi phí tính toán từ $O(|V|)$ xuống $O(K)$, tăng tốc độ huấn luyện lên hàng trăm lần!

- **Phép toán đại số vector kỳ diệu của Word2Vec:**
  $$\mathbf{v}_{\text{King}} - \mathbf{v}_{\text{Man}} + \mathbf{v}_{\text{Woman}} \approx \mathbf{v}_{\text{Queen}}$$
  $$\mathbf{v}_{\text{Hà Nội}} - \mathbf{v}_{\text{Việt Nam}} + \mathbf{v}_{\text{Pháp}} \approx \mathbf{v}_{\text{Paris}}$$
  Vector khoảng cách giữa hai từ mã hóa chính xác mối quan hệ ngữ nghĩa (Quan hệ Giới tính, Quan hệ Thủ đô - Quốc gia)!

---

**4. Mô hình GloVe (Global Vectors for Word Representation - Pennington et al., Stanford 2014 - CÂU 19 ĐỀ THI VAIO 2025):**
- Điểm yếu của Word2Vec: Chỉ nhìn cục bộ trong từng cửa sổ trượt hẹp $C$ từ, hoàn toàn lãng phí thông tin thống kê vĩ mô của toàn bộ kho ngữ liệu.
- **Bản chất của GloVe (Câu 19 VAIO):** Được huấn luyện từ **Ma trận đồng xuất hiện toàn cục (Global Co-occurrence Matrix) $X$** của toàn bộ kho ngữ liệu!
  - Phần tử $X_{ij}$ là tổng số lần từ $i$ và từ $j$ xuất hiện cùng nhau trong toàn bộ kho văn bản khổng lồ.
  - Tỉ số xác suất đồng xuất hiện giải mã ngữ nghĩa: Xét từ $i = \text{"ice"}$ (băng) và $j = \text{"steam"}$ (hơi nước). Với từ thăm dò $k = \text{"solid"}$ (rắn), tỉ số $\frac{P(k \mid \text{ice})}{P(k \mid \text{steam})}$ sẽ rất lớn ($\gg 1$); với $k = \text{"gas"}$ (khí), tỉ số sẽ rất nhỏ ($\ll 1$).
- **Hàm mất mát hồi quy bình phương tối thiểu có trọng số (Weighted Least Squares):**
  $$J = \sum_{i,j=1}^{|V|} f(X_{ij}) \left( \mathbf{w}_i^T \mathbf{\tilde{w}}_j + b_i + \tilde{b}_j - \log X_{ij} \right)^2$$
  trong đó $f(X_{ij}) = \min\left(1, \left(\frac{X_{ij}}{x_{\max}}\right)^\alpha\right)$ (thường chọn $\alpha = 0.75, x_{\max} = 100$) là hàm trọng số làm mềm để tránh việc các từ quá phổ biến (như từ dừng) lấn át hoàn toàn hàm mất mát.""" ,
                "formula": r"\text{CBOW: } P(w_t \mid w_{\text{context}}), \quad \text{GloVe: } J = \sum_{i,j=1}^{|V|} f(X_{ij}) \left( \mathbf{w}_i^T \mathbf{\tilde{w}}_j + b_i + \tilde{b}_j - \log X_{ij} \right)^2",
                "mathExplainer": [
                    { "sym": r"\text{CBOW}", "name": "Continuous Bag-of-Words", "mean": "Kiến trúc dùng trung bình cộng các từ ngữ cảnh xung quanh để dự đoán từ trung tâm." },
                    { "sym": r"\text{Skip-gram}", "name": "Skip-gram", "mean": "Kiến trúc dùng 1 từ trung tâm để dự đoán các từ ngữ cảnh xung quanh; học tốt từ hiếm." },
                    { "sym": r"X_{ij}", "name": "Ma trận đồng xuất hiện toàn cục", "mean": "Số lần từ i và từ j cùng xuất hiện trong toàn bộ kho ngữ liệu (Corpus)." },
                    { "sym": r"f(X_{ij})", "name": "Hàm trọng số cắt", "mean": "Hàm làm mềm ngăn các cặp từ xuất hiện quá nhiều làm méo mó hàm mất mát GloVe." },
                    { "sym": r"\mathbf{w}_i, \mathbf{\tilde{w}}_j", "name": "Vector nhúng từ và ngữ cảnh", "mean": "Hai vector biểu diễn của từ i và từ j trong không gian d chiều liên tục." }
                ],
                "diagram": {
                    "svg": r"""<svg viewBox="0 0 660 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
                      <rect width="660" height="170" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Left: CBOW -->
                      <g transform="translate(20, 20)">
                        <text x="80" y="14" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">CBOW (Câu 91 VAIO)</text>
                        <!-- Context boxes -->
                        <rect x="0" y="30" width="55" height="22" fill="#fff" stroke="#111" stroke-width="1.2" rx="2"/>
                        <text x="27" y="44" font-family="Georgia" font-size="8.5" text-anchor="middle">w(t-1)</text>
                        <rect x="0" y="60" width="55" height="22" fill="#fff" stroke="#111" stroke-width="1.2" rx="2"/>
                        <text x="27" y="74" font-family="Georgia" font-size="8.5" text-anchor="middle">w(t+1)</text>
                        <!-- Projection / Sum -->
                        <line x1="55" y1="41" x2="80" y2="56" stroke="#111" stroke-width="1.2"/>
                        <line x1="55" y1="71" x2="80" y2="56" stroke="#111" stroke-width="1.2"/>
                        <circle cx="90" cy="56" r="12" fill="#e0e0e0" stroke="#111" stroke-width="1.2"/>
                        <text x="90" y="60" font-family="Georgia" font-size="9" font-weight="bold" text-anchor="middle">∑</text>
                        <!-- Target output -->
                        <line x1="102" y1="56" x2="125" y2="56" stroke="#111" stroke-width="1.2"/>
                        <rect x="125" y="45" width="50" height="22" fill="#111" rx="2"/>
                        <text x="150" y="59" font-family="Georgia" font-size="9" fill="#fff" font-weight="bold" text-anchor="middle">w(t)</text>
                        <text x="80" y="105" font-family="Georgia" font-size="8" text-anchor="middle">Ngữ cảnh → Đoán từ giữa</text>
                      </g>
                      <!-- Divider -->
                      <line x1="210" y1="20" x2="210" y2="150" stroke="#ccc" stroke-dasharray="2,2"/>
                      <!-- Center: Skip-Gram -->
                      <g transform="translate(230, 20)">
                        <text x="80" y="14" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Skip-gram (Word2Vec)</text>
                        <!-- Input Target -->
                        <rect x="0" y="45" width="50" height="22" fill="#111" rx="2"/>
                        <text x="25" y="59" font-family="Georgia" font-size="9" fill="#fff" font-weight="bold" text-anchor="middle">w(t)</text>
                        <!-- Projection line -->
                        <line x1="50" y1="56" x2="80" y2="56" stroke="#111" stroke-width="1.2"/>
                        <circle cx="85" cy="56" r="6" fill="#111"/>
                        <line x1="85" y1="56" x2="115" y2="41" stroke="#111" stroke-width="1.2"/>
                        <line x1="85" y1="56" x2="115" y2="71" stroke="#111" stroke-width="1.2"/>
                        <!-- Output context -->
                        <rect x="115" y="30" width="55" height="22" fill="#fff" stroke="#111" stroke-width="1.2" rx="2"/>
                        <text x="142" y="44" font-family="Georgia" font-size="8.5" text-anchor="middle">w(t-1)</text>
                        <rect x="115" y="60" width="55" height="22" fill="#fff" stroke="#111" stroke-width="1.2" rx="2"/>
                        <text x="142" y="74" font-family="Georgia" font-size="8.5" text-anchor="middle">w(t+1)</text>
                        <text x="85" y="105" font-family="Georgia" font-size="8" text-anchor="middle">Từ giữa → Đoán ngữ cảnh</text>
                      </g>
                      <!-- Divider -->
                      <line x1="430" y1="20" x2="430" y2="150" stroke="#ccc" stroke-dasharray="2,2"/>
                      <!-- Right: GloVe -->
                      <g transform="translate(450, 20)">
                        <text x="90" y="14" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">GloVe (Câu 19 VAIO)</text>
                        <rect x="15" y="30" width="55" height="55" fill="#fff" stroke="#111" stroke-width="1.2"/>
                        <!-- matrix grid -->
                        <line x1="33" y1="30" x2="33" y2="85" stroke="#ccc"/>
                        <line x1="51" y1="30" x2="51" y2="85" stroke="#ccc"/>
                        <line x1="15" y1="48" x2="70" y2="48" stroke="#ccc"/>
                        <line x1="15" y1="66" x2="70" y2="66" stroke="#ccc"/>
                        <text x="42" y="60" font-family="Georgia" font-size="9" font-weight="bold" text-anchor="middle">X_ij</text>
                        <text x="85" y="60" font-family="Georgia" font-size="12" font-weight="bold">→</text>
                        <rect x="105" y="42" width="70" height="30" fill="#fff" stroke="#111" stroke-width="1.2" rx="2"/>
                        <text x="140" y="55" font-family="Georgia" font-size="8" font-weight="bold" text-anchor="middle">W·Wᵀ ≈ log X</text>
                        <text x="140" y="66" font-family="Georgia" font-size="7" fill="#555" text-anchor="middle">Bình phương TT</text>
                        <text x="90" y="105" font-family="Georgia" font-size="8" text-anchor="middle">Ma trận đồng xuất hiện</text>
                      </g>
                      <!-- Bottom text equation -->
                      <g transform="translate(0, 130)">
                        <rect x="20" y="0" width="620" height="28" fill="#f0f0f0" stroke="#ddd" rx="3"/>
                        <text x="330" y="18" font-family="Georgia" font-size="9" font-weight="bold" text-anchor="middle">Đại số ngữ nghĩa Word2Vec: Vector("King") - Vector("Man") + Vector("Woman") ≈ Vector("Queen")</text>
                      </g>
                    </svg>""",
                    "caption": "So sánh 3 trụ cột biểu diễn từ ngữ: CBOW (dự đoán từ giữa), Skip-gram (dự đoán từ xung quanh) và GloVe (ma trận đồng xuất hiện toàn cục)."
                },
                "commonPitfalls": r"""Cạm bẫy phòng thi Câu 19 & 91 Đề thi chính thức VAIO 2025:
1. **Nhầm lẫn mục tiêu của CBOW và Skip-gram (Câu 91):**
   - CBOW: Dùng ngữ cảnh xung quanh để suy luận từ ở giữa ($P(w_t \mid \text{context})$).
   - Skip-gram: Dùng từ ở giữa để suy luận ngữ cảnh xung quanh ($P(\text{context} \mid w_t)$).
2. **Nguồn gốc dữ liệu của GloVe (Câu 19):** Đề thi hỏi mô hình GloVe được xây dựng từ đâu? Luôn chọn ngay: **Ma trận đồng xuất hiện toàn cục (Co-occurrence matrix)** của toàn bộ ngữ liệu bằng phương pháp hồi quy bình phương tối thiểu có trọng số!
3. **Hiểu lầm về One-Hot vector:** Nhớ rằng tích vô hướng giữa hai vector One-Hot khác nhau luôn bằng $0$ (trực giao) và khoảng cách Euclid luôn bằng $\sqrt{2}$.""",
                "practiceQuestion": {
                    "level": "Vận dụng (Câu 19 & 91 Đề Thi Chính Thức VAIO 2025)",
                    "question": "Mục tiêu huấn luyện của mô hình CBOW (Continuous Bag-of-Words) và mô hình GloVe được xây dựng như thế nào? (Câu 19 & 91 Đề thi chính thức VAIO 2025)",
                    "options": [
                        "A. CBOW dùng từ trung tâm để đoán các từ xung quanh; GloVe dùng ma trận chú ý Self-Attention",
                        "B. CBOW dùng các từ ngữ cảnh xung quanh để dự đoán từ trung tâm; GloVe được huấn luyện từ ma trận đồng xuất hiện toàn cục (Co-occurrence matrix)",
                        "C. CBOW dùng ma trận đồng xuất hiện; GloVe dùng bộ mã hóa tự hồi quy 1 chiều",
                        "D. Cả hai mô hình đều là các vector One-Hot có số chiều bằng kích thước từ điển"
                    ],
                    "correctIndex": 1,
                    "hint": "CBOW là 'Túi từ liên tục' lấy trung bình ngữ cảnh để đoán từ ở giữa; GloVe viết tắt của Global Vectors dựa trên thống kê đồng xuất hiện toàn bộ văn bản.",
                    "solution": [
                        "Phân tích CBOW (Câu 91 VAIO): CBOW lấy tổng hợp các từ ngữ cảnh xung quanh trong một cửa sổ trượt để tối đa hóa xác suất dự đoán từ đích ở giữa.",
                        "Phân tích GloVe (Câu 19 VAIO): GloVe (Global Vectors) của Stanford kết hợp ưu điểm của đếm tần suất toàn cục và học máy, bằng cách khớp tích vô hướng vector với logarit của ma trận đồng xuất hiện toàn cục (co-occurrence matrix).",
                        "Do đó, phát biểu chuẩn xác nhất là phương án B."
                    ]
                }
            },

            # =================================================================
            # MỤC 12.3: MÔ HÌNH CHUỖI RNN, LSTM & ĐẾM THAM SỐ (CÂU 4 VAIO)
            # =================================================================
            {
                "heading": "12.3. Mô Hình Chuỗi Tuần Tự: RNN, LSTM & Công Thức Đếm Tham Số Mô Hình (Câu 4 VAIO)",
                "content": "Khám phá bản chất dữ liệu tuần tự có thứ tự thời gian; cấu trúc mạng nơ-ron hồi quy RNN; nguyên nhân tiêu biến gradient qua thời gian (BPTT); giải pháp 4 cổng của tế bào LSTM và công thức đếm số lượng tham số kinh điển trong phòng thi Olympic AI.",
                "deepDive": r"""**1. Tại sao ngôn ngữ cần Mô Hình Tuần Tự (Sequential Models)?**
Một câu văn không chỉ là tập hợp các từ rời rạc. Thứ tự sắp xếp trước - sau của các từ mang tính sống còn quyết định toàn bộ ngữ nghĩa:
$$\text{"Anh ta yêu cô ấy"} \quad \neq \quad \text{"Cô ấy yêu anh ta"}$$
$$\text{"Không phải tôi không thích môn Toán"} \quad (\text{nghĩa là: Tôi thích môn Toán!})$$
Nếu dùng mạng nơ-ron kết nối đầy đủ (MLP), ta phải ép câu văn thành một vector có chiều dài cố định, làm mất sạch thông tin thứ tự và không thể xử lý những câu có độ dài tùy biến linh hoạt. Đó là lý do **Mạng nơ-ron Hồi Quy (RNN - Recurrent Neural Network)** ra đời.

---

**2. Mạng nơ-ron hồi quy RNN & Hiện tượng Tiêu biến Gradient (Vanishing Gradient):**
- **Cơ chế hoạt động:** RNN duyệt qua chuỗi văn bản từng bước thời gian $t = 1, 2, \dots, T$.
- Tại mỗi bước thời gian $t$, nơ-ron tiếp nhận vector từ hiện tại $x_t$ và kết hợp với **Trạng thái ẩn trước đó $h_{t-1}$** (đóng vai trò như ký ức của quá khứ) để tạo ra trạng thái ẩn mới $h_t$:
  $$h_t = \tanh(W_{xh} x_t + W_{hh} h_{t-1} + b_h)$$
  $$y_t = \text{Softmax}(W_{hy} h_t + b_y)$$
- **Chia sẻ trọng số (Weight Sharing):** Cùng một bộ ma trận $W_{xh}, W_{hh}, b_h$ được tái sử dụng ở TẤT CẢ các bước thời gian từ đầu đến cuối câu!
- **Tử huyệt của RNN:**
  1. *Nghẽn tuần tự (Sequential Bottleneck):* Muốn tính bước $t$, bắt buộc phải chờ bước $t-1$ tính xong. Không thể tận dụng hàng nghìn nhân tính toán song song của GPU!
  2. *Tiêu biến Gradient khi lan truyền ngược qua thời gian (BPTT):* Khi chuỗi dài hơn 15 - 20 từ, gradient truyền ngược từ cuối câu về đầu câu phải nhân liên tiếp qua chuỗi đạo hàm của hàm $\tanh$ (có giá trị tối đa là $1.0$) và ma trận $W_{hh}$. Đạo hàm giảm theo cấp số nhân về $0$. RNN mắc chứng "não cá vàng": đọc đến cuối câu là quên sạch chủ ngữ ở đầu câu!

---

**3. Mạng LSTM (Long Short-Term Memory - Hochreiter & Schmidhuber, 1997):**
LSTM giải quyết triệt để vấn đề tiêu biến gradient bằng cách tách bộ nhớ thành 2 luồng:
- **Trạng thái tế bào $C_t$ (Cell State - Băng chuyền ký ức dài hạn):** Chạy xuyên suốt qua thời gian bằng các phép tính cộng tuyến tính, cho phép gradient phóng thẳng về quá khứ mà không bị suy hao!
- **Trạng thái ẩn $h_t$ (Hidden State - Ký ức ngắn hạn):** Xuất ra thông tin cần dùng tại bước hiện tại.

Luồng thông tin được điều tiết bởi **4 cổng van thông minh (Gates)** sử dụng hàm kích hoạt Sigmoid $\sigma \in [0, 1]$ (0: khóa van hoàn toàn, 1: mở van tối đa):
1. **Cổng quên (Forget Gate $f_t$):** Quyết định bao nhiêu % ký ức cũ trong $C_{t-1}$ sẽ bị xóa bỏ:
   $$f_t = \sigma(W_f [h_{t-1}, x_t] + b_f)$$
2. **Cổng nạp (Input Gate $i_t$):** Quyết định bao nhiêu % thông tin mới sẽ được nạp vào bộ nhớ:
   $$i_t = \sigma(W_i [h_{t-1}, x_t] + b_i)$$
3. **Ứng viên cập nhật ($\tilde{C}_t$):** Nội dung thông tin mới được đề xuất:
   $$\tilde{C}_t = \tanh(W_c [h_{t-1}, x_t] + b_c)$$
   *Cập nhật Cell State tuyến tính (Phép cộng giải phóng gradient!):*
   $$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$$
4. **Cổng xuất (Output Gate $o_t$):** Quyết định bao nhiêu % ký ức dài hạn được xuất ra trạng thái ẩn $h_t$:
   $$o_t = \sigma(W_o [h_{t-1}, x_t] + b_o)$$
   $$h_t = o_t \odot \tanh(C_t)$$

---

**4. Kỹ thuật Đếm Số Lượng Tham Số Mô Hình (CÂU 4 ĐỀ THI VAIO 2025):**
Dạng bài tính số lượng tham số có thể học (Weights và Biases) của các tầng nơ-ron chuỗi là câu hỏi tính toán cốt lõi trong đề thi.

Quy ước ký hiệu chuẩn:
- $D = d_x$: Số chiều của vector đầu vào $x_t$ (Input dimension).
- $H = d_h$: Số chiều của vector trạng thái ẩn $h_t$ (Hidden dimension).

- **1. Công thức tham số của một tầng RNN cơ bản:**
  - Ma trận trọng số kết nối đầu vào với trạng thái ẩn $W_{xh}$: kích thước $H \times D \implies H \times D$ tham số.
  - Ma trận trọng số kết nối trạng thái ẩn trước với hiện tại $W_{hh}$: kích thước $H \times H \implies H \times H$ tham số.
  - Vector độ lệch bias $b_h$: kích thước $H \times 1 \implies H$ tham số.
  $$\text{Params}_{\text{RNN}} = H \times D + H \times H + H = H(D + H + 1)$$

- **2. Công thức tham số của một tầng LSTM (CỰC KỲ QUAN TRỌNG - NHỚ NHÂN 4!):**
  - Một tế bào LSTM bao gồm đúng **4 bộ tính toán tuyến tính độc lập** ứng với 4 cổng:
    1. Cổng quên $f_t$
    2. Cổng nạp $i_t$
    3. Trạng thái ứng viên $\tilde{C}_t$
    4. Cổng xuất $o_t$
  - Mỗi cổng đều sở hữu một ma trận trọng số kích thước $H \times (D + H)$ và một vector bias kích thước $H$!
  - Do đó, số tham số của một tầng LSTM gấp đúng **4 LẦN** một tầng RNN:
    $$\text{Params}_{\text{LSTM}} = 4 \times [H \times D + H \times H + H] = 4 \times H(D + H + 1)$$

- **3. Công thức tham số của một tầng GRU (Gated Recurrent Unit):**
  - GRU tối giản tế bào chỉ còn **3 cổng** (Reset gate $r_t$, Update gate $z_t$, Candidate state $\tilde{h}_t$):
    $$\text{Params}_{\text{GRU}} = 3 \times H(D + H + 1)$$

---

**Ví dụ tính toán số học từng bước trong phòng thi:**
*Đề bài:* Cho một tầng LSTM đơn với chiều vector đầu vào $D = 100$ và số nơ-ron trạng thái ẩn $H = 128$. Hãy tính tổng số lượng tham số có thể huấn luyện của tầng này.
- *Bước 1:* Tính số tham số của một cổng đơn lẻ:
  $$\text{Params}_{\text{cổng}} = H \times D + H \times H + H = (128 \times 100) + (128 \times 128) + 128 = 12,800 + 16,384 + 128 = 29,312$$
- *Bước 2:* Nhân 4 cho toàn bộ tế bào LSTM:
  $$\text{Params}_{\text{LSTM}} = 4 \times 29,312 = 117,248 \text{ tham số!}$$
(Nếu đề bài hỏi tầng RNN đơn giản thì đáp án sẽ là đúng $29,312$).""" ,
                "formula": r"\text{Params}_{\text{RNN}} = H(D + H + 1), \quad \text{Params}_{\text{LSTM}} = 4 \times H(D + H + 1), \quad \text{Params}_{\text{GRU}} = 3 \times H(D + H + 1)",
                "mathExplainer": [
                    { "sym": "D", "name": "Input Dimension", "mean": "Số chiều của vector đặc trưng đầu vào x_t tại mỗi bước thời gian." },
                    { "sym": "H", "name": "Hidden Dimension", "mean": "Số chiều của vector trạng thái ẩn h_t (số nơ-ron của tầng hồi quy)." },
                    { "sym": "W_{xh}, W_{hh}", "name": "Ma trận trọng số", "mean": "W_xh nối đầu vào với trạng thái ẩn; W_hh nối trạng thái ẩn trước với hiện tại." },
                    { "sym": "C_t, h_t", "name": "Cell State & Hidden State", "mean": "C_t là băng chuyền ký ức dài hạn của LSTM; h_t là ký ức làm việc ngắn hạn." },
                    { "sym": r"\text{Params}_{\text{LSTM}}", "name": "Số tham số LSTM", "mean": "Bằng 4 lần số tham số RNN do có 4 cổng độc lập (Forget, Input, Candidate, Output)." }
                ],
                "diagram": {
                    "svg": r"""<svg viewBox="0 0 660 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
                      <rect width="660" height="170" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Left: LSTM Cell Diagram -->
                      <g transform="translate(20, 20)">
                        <text x="140" y="14" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Kiến Trúc Tế Bào LSTM (4 Cổng Van)</text>
                        <rect x="0" y="25" width="280" height="110" fill="#fff" stroke="#111" stroke-width="1.5" rx="4"/>
                        <!-- Top conveyor Cell state C_t-1 to C_t -->
                        <line x1="15" y1="45" x2="265" y2="45" stroke="#111" stroke-width="2"/>
                        <circle cx="75" cy="45" r="9" fill="#e0e0e0" stroke="#111" stroke-width="1.2"/>
                        <text x="75" y="48.5" font-family="Georgia" font-size="9" font-weight="bold" text-anchor="middle">∗</text>
                        <circle cx="160" cy="45" r="9" fill="#e0e0e0" stroke="#111" stroke-width="1.2"/>
                        <text x="160" y="48.5" font-family="Georgia" font-size="9" font-weight="bold" text-anchor="middle">+</text>
                        <text x="15" y="38" font-family="Georgia" font-size="8.5">C_{t-1}</text>
                        <text x="260" y="38" font-family="Georgia" font-size="8.5">C_t</text>
                        <!-- 4 Gates -->
                        <!-- Forget gate f_t -->
                        <rect x="65" y="75" width="20" height="20" fill="#111" rx="2"/>
                        <text x="75" y="89" font-family="Georgia" font-size="8" fill="#fff" font-weight="bold" text-anchor="middle">σ</text>
                        <line x1="75" y1="75" x2="75" y2="54" stroke="#111" stroke-width="1.2"/>
                        <text x="75" y="106" font-family="Georgia" font-size="7" text-anchor="middle">Forget</text>
                        <!-- Input gate i_t -->
                        <rect x="125" y="75" width="20" height="20" fill="#111" rx="2"/>
                        <text x="135" y="89" font-family="Georgia" font-size="8" fill="#fff" font-weight="bold" text-anchor="middle">σ</text>
                        <text x="135" y="106" font-family="Georgia" font-size="7" text-anchor="middle">Input</text>
                        <!-- Candidate gate ~C_t -->
                        <rect x="165" y="75" width="22" height="20" fill="#e0e0e0" stroke="#111" rx="2"/>
                        <text x="176" y="89" font-family="Georgia" font-size="8" font-weight="bold" text-anchor="middle">tanh</text>
                        <text x="176" y="106" font-family="Georgia" font-size="7" text-anchor="middle">Cand</text>
                        <!-- Merge input * candidate -->
                        <line x1="135" y1="75" x2="155" y2="60" stroke="#111" stroke-width="1.2"/>
                        <line x1="176" y1="75" x2="160" y2="54" stroke="#111" stroke-width="1.2"/>
                        <!-- Output gate o_t -->
                        <rect x="220" y="75" width="20" height="20" fill="#111" rx="2"/>
                        <text x="230" y="89" font-family="Georgia" font-size="8" fill="#fff" font-weight="bold" text-anchor="middle">σ</text>
                        <text x="230" y="106" font-family="Georgia" font-size="7" text-anchor="middle">Output</text>
                        <!-- Input bottom -->
                        <line x1="40" y1="120" x2="230" y2="120" stroke="#ccc"/>
                        <text x="35" y="132" font-family="Georgia" font-size="8" fill="#333">[h_{t-1}, x_t]</text>
                      </g>
                      <!-- Right: Parameter counting panel -->
                      <g transform="translate(330, 20)">
                        <rect x="0" y="0" width="310" height="135" fill="#fff" stroke="#111" stroke-width="1" rx="3"/>
                        <text x="155" y="20" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Bảng Đếm Tham Số (Câu 4 VAIO)</text>
                        <!-- Table header -->
                        <rect x="10" y="32" width="290" height="20" fill="#f0f0f0"/>
                        <text x="20" y="46" font-family="Georgia" font-size="9" font-weight="bold">Mô hình</text>
                        <text x="100" y="46" font-family="Georgia" font-size="9" font-weight="bold">Công thức tham số</text>
                        <text x="225" y="46" font-family="Georgia" font-size="9" font-weight="bold">Số cổng</text>
                        <!-- Row 1: RNN -->
                        <text x="20" y="70" font-family="Georgia" font-size="9">RNN Đơn</text>
                        <text x="100" y="70" font-family="monospace" font-size="9">H × (D + H + 1)</text>
                        <text x="235" y="70" font-family="Georgia" font-size="9">1</text>
                        <line x1="10" y1="78" x2="300" y2="78" stroke="#eee"/>
                        <!-- Row 2: LSTM -->
                        <text x="20" y="96" font-family="Georgia" font-size="9" font-weight="bold">LSTM</text>
                        <text x="100" y="96" font-family="Georgia" font-size="9" font-weight="bold">4 × H × (D + H + 1)</text>
                        <text x="235" y="96" font-family="Georgia" font-size="9" font-weight="bold">4 cổng</text>
                        <line x1="10" y1="104" x2="300" y2="104" stroke="#eee"/>
                        <!-- Row 3: GRU -->
                        <text x="20" y="122" font-family="Georgia" font-size="9">GRU</text>
                        <text x="100" y="122" font-family="monospace" font-size="9">3 × H × (D + H + 1)</text>
                        <text x="235" y="122" font-family="Georgia" font-size="9">3 cổng</text>
                      </g>
                    </svg>""",
                    "caption": "Sơ đồ tế bào LSTM với băng chuyền Cell State và bảng công thức đếm số lượng tham số học được của RNN, LSTM, GRU."
                },
                "commonPitfalls": r"""Cạm bẫy phòng thi Câu 4 Đề thi chính thức VAIO 2025:
1. **Quên vector Bias ($+1$):** Nhiều thí sinh chỉ tính $H \times D + H \times H$ mà quên mất vector bias $b$ có $H$ tham số! Công thức chuẩn là $H(D + H + 1)$.
2. **Quên hệ số 4 đối với LSTM:** Tế bào LSTM có 4 cổng hoạt động song song độc lập. Đề thi hỏi số tham số của tầng LSTM thì BẮT BUỘC phải nhân $4$ vào kết quả của tầng RNN!
3. **Nhầm lẫn giữa GRU và LSTM:** GRU chỉ có 3 cổng (nhân 3), LSTM có 4 cổng (nhân 4).""",
                "practiceQuestion": {
                    "level": "Vận dụng (Câu 4 Đề Thi Chính Thức VAIO 2025)",
                    "question": "Một tầng nơ-ron hồi quy RNN đơn giản có kích thước vector đầu vào D = 100 và kích thước trạng thái ẩn H = 128. Tổng số lượng tham số có thể huấn luyện (Weights và Biases) của tầng này là bao nhiêu?",
                    "options": [
                        "A. 12,800",
                        "B. 29,312",
                        "C. 16,384",
                        "D. 117,248"
                    ],
                    "correctIndex": 1,
                    "hint": "Tổng tham số = Ma trận trọng số đầu vào W_xh (H × D) + Ma trận trọng số hồi quy W_hh (H × H) + Vector bias (H).",
                    "solution": [
                        "Bước 1: Tính số tham số của ma trận trọng số đầu vào: W_xh có kích thước H × D = 128 × 100 = 12,800 tham số.",
                        "Bước 2: Tính số tham số của ma trận trọng số hồi quy: W_hh có kích thước H × H = 128 × 128 = 16,384 tham số.",
                        "Bước 3: Tính số tham số của vector độ lệch bias: b có kích thước H = 128 tham số.",
                        "Bước 4: Tổng số tham số = 12,800 + 16,384 + 128 = 29,312 tham số.",
                        "(Lưu ý: Nếu đây là tầng LSTM thì đáp án sẽ là 4 × 29,312 = 117,248 ở phương án D). Đáp án chính xác cho RNN là B (29,312)."
                    ]
                }
            },

            # =================================================================
            # MỤC 12.4: CƠ CHẾ SELF-ATTENTION & TẠI SAO CHIA CĂN D_K (CÂU 74 VAIO)
            # =================================================================
            {
                "heading": "12.4. Trái Tim Của Cuộc Cách Mạng AI: Cơ Chế Tự Chú Ý (Self-Attention) & Bộ Ba Kỳ Diệu Query, Key, Value (Câu 23 & 74 VAIO)",
                "content": "Giải mã bài báo lịch sử 'Attention Is All You Need'; trực giác tra cứu video YouTube với bộ ba Query-Key-Value; công thức Scaled Dot-Product Attention và chứng minh toán học tại sao bắt buộc phải chia cho căn bậc hai d_k (Câu 74 VAIO); cùng cơ chế Multi-Head Attention.",
                "deepDive": r"""**1. Bước ngoặt lịch sử năm 2017: 'Attention Is All You Need':**
Năm 2017, nhóm nghiên cứu Google Brain đã công bố bài báo mang tính biểu tượng làm thay đổi hoàn toàn cục diện Trí Tuệ Nhân Tạo. Họ mạnh dạn đưa ra một tuyên bố chấn động: **VỨT BỎ HOÀN TOÀN RNN VÀ LSTM!** Không cần duyệt tuần tự từng bước thời gian nữa!

Thay vào đó, kiến trúc **Transformer** ra đời dựa trên cơ chế duy nhất: **Self-Attention (Tự Chú Ý)**:
- Mọi từ trong câu được nạp đồng thời vào GPU và có thể nhìn thấy, giao tiếp với MỌI TỪ KHÁC cùng một lúc.
- Khoảng cách đường truyền thông tin giữa hai từ cách xa nhau 1,000 từ được rút ngắn từ $O(N)$ xuống đúng **$O(1)$**!
- Cho phép tính toán song song 100% trên phần cứng ma trận GEMM hiện đại, mở đường cho việc mở rộng quy mô dữ liệu khổng lồ.

---

**2. Trực giác đời sống: Bộ ba Query, Key, Value & Hệ thống tra cứu YouTube:**
Để hiểu sâu sắc cơ chế Attention mà không bị choáng ngợp bởi ma trận, hãy liên tưởng đến thao tác tìm kiếm video trên YouTube:
1. **Query ($Q$ - Câu hỏi truy vấn):** Bạn gõ vào thanh tìm kiếm dòng chữ: *"hướng dẫn làm bánh mì Việt Nam"*. Đây chính là vector $Q$ thể hiện nhu cầu thông tin bạn đang tìm kiếm.
2. **Key ($K$ - Từ khóa so khớp):** YouTube có hàng triệu video, mỗi video có tiêu đề và nhãn thẻ (tags): *"cách nướng bánh mì"*, *"làm sushi Nhật Bản"*, *"review xe hơi"*. Đây chính là vector $K$ của các đối tượng trong cơ sở dữ liệu.
3. **Độ tương đồng (Attention Weight):** Hệ thống lấy tích vô hướng giữa $Q$ của bạn với $K$ của từng video. Video *"cách nướng bánh mì"* có độ tương đồng cực cao ($0.92$), video *"sushi"* thấp ($0.05$), video *"xe hơi"* gần bằng $0$.
4. **Value ($V$ - Nội dung giá trị thực tế):** Khi bạn bấm vào video, bạn nhận được hình ảnh, âm thanh hướng dẫn chi tiết. Đây chính là vector $V$.
5. **Kết quả bạn nhận được:** Một bức tranh tổng hợp các thông tin hữu ích được lấy từ các video ($V$), trong đó video nào có điểm tương đồng giữa $Q$ và $K$ cao nhất sẽ đóng góp nhiều phần trăm nội dung nhất!

---

**3. Bản chất toán học của Scaled Dot-Product Attention (CÂU 74 ĐỀ THI VAIO 2025):**
Cho một câu văn bản gồm $N$ từ, mỗi từ đã được nhúng thành vector kích thước $d_{\text{model}}$ tạo thành ma trận đầu vào $X \in \mathbb{R}^{N \times d_{\text{model}}}$.

- **Bước 1: Chiếu tuyến tính tạo $Q, K, V$:**
  Ta nhân ma trận đầu vào $X$ với 3 ma trận trọng số có thể học được $W_Q, W_K, W_V \in \mathbb{R}^{d_{\text{model}} \times d_k}$:
  $$Q = X W_Q, \quad K = X W_K, \quad V = X W_V$$
- **Bước 2: Tính ma trận điểm số thô (Raw Attention Scores):**
  Lấy tích vô hướng giữa Query và Key của mọi cặp từ:
  $$S = Q K^T \in \mathbb{R}^{N \times N}$$
  Phần tử $S_{ij} = q_i \cdot k_j$ thể hiện mức độ tương quan liên kết giữa từ thứ $i$ và từ thứ $j$.
- **Bước 3: Thu nhỏ tỉ lệ (Scaling) và chuẩn hóa xác suất bằng Softmax:**
  Chia cho căn bậc hai của số chiều $\sqrt{d_k}$ và đưa qua hàm Softmax trên từng hàng:
  $$A = \text{Softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) \in \mathbb{R}^{N \times N}$$
  Mỗi hàng của ma trận $A$ là một phân phối xác suất có tổng bằng $1.0$ thể hiện phần trăm sự chú ý của từ $i$ tới từng từ khác.
- **Bước 4: Tổng hợp thông tin đầu ra:**
  Nhân ma trận trọng số chú ý $A$ với ma trận nội dung Value $V$:
  $$\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$$

---

**4. CHỨNG MINH TOÁN HỌC: Tại sao bắt buộc phải chia cho $\sqrt{d_k}$? (CÂU HỎI KINH ĐIỂN CỦA ĐỀ THI VAIO & CÁC KỲ THI AI):**
Tại sao các tác giả không dùng công thức đơn giản $\text{Softmax}(Q K^T) V$ mà bắt buộc phải thêm mẫu số $\sqrt{d_k}$?

*Chứng minh xác suất:*
- Giả sử các phần tử của vector truy vấn $q$ và khóa $k$ là các biến ngẫu nhiên độc lập có kỳ vọng $\mathbb{E}[q_i] = \mathbb{E}[k_i] = 0$ và phương sai chuẩn hóa $\text{Var}(q_i) = \text{Var}(k_i) = 1$.
- Tích vô hướng của chúng là tổng của $d_k$ tích thành phần:
  $$q \cdot k = \sum_{i=1}^{d_k} q_i k_i$$
- Kỳ vọng của tích vô hướng: $\mathbb{E}[q \cdot k] = \sum_{i=1}^{d_k} \mathbb{E}[q_i] \mathbb{E}[k_i] = 0$.
- Do các thành phần độc lập, phương sai của tổng bằng tổng các phương sai:
  $$\text{Var}(q \cdot k) = \sum_{i=1}^{d_k} \text{Var}(q_i k_i) = \sum_{i=1}^{d_k} \left( \mathbb{E}[q_i^2 k_i^2] - (\mathbb{E}[q_i k_i])^2 \right) = \sum_{i=1}^{d_k} (1 \times 1) = d_k$$
- **Hậu quả khi số chiều $d_k$ lớn (ví dụ $d_k = 64$ hoặc $512$):**
  - Phương sai của tích vô hướng bằng $d_k$, đồng nghĩa với **độ lệch chuẩn bằng $\sqrt{d_k}$** ($\sqrt{64} = 8$).
  - Giá trị của tích vô hướng $q \cdot k$ sẽ dao động rất mạnh, thường xuyên vọt lên những con số cực lớn (như $+25$ hoặc $-30$).
  - Khi nạp các giá trị cực lớn này vào hàm Softmax: $\frac{e^{z_i}}{\sum e^{z_j}}$, hàm Softmax bị đẩy sâu vào **vùng bão hòa (Saturation region)**! Một phần tử lớn nhất sẽ chiếm xác suất áp đảo $\approx 1.0$, trong khi tất cả các phần tử còn lại bị đè bẹp về $\approx 0.0$.
  - Đạo hàm của hàm Softmax ở vùng bão hòa cực kỳ nhỏ, tiến sát về $0$! Dẫn đến hiện tượng **TIÊU BIẾN GRADIENT (Vanishing Gradient)** nghiêm trọng, khiến mô hình bị tê liệt và hoàn toàn ngừng học!
- **Tác dụng cứu cánh của phép chia cho $\sqrt{d_k}$:**
  $$\text{Var}\left(\frac{q \cdot k}{\sqrt{d_k}}\right) = \frac{\text{Var}(q \cdot k)}{(\sqrt{d_k})^2} = \frac{d_k}{d_k} = 1.0$$
  Phép chia đưa phương sai của tích vô hướng trở về đúng $1.0$, giữ cho các giá trị đầu vào của Softmax nằm gọn trong vùng có đạo hàm lớn nhất, đảm bảo gradient truyền ngược luôn thông suốt!

---

**5. Cơ chế Chú Ý Đa Đầu (Multi-Head Attention) & Mã Hóa Vị Trí (Positional Encoding):**
- **Multi-Head Attention:** Thay vì chỉ tính 1 ma trận Attention duy nhất, Transformer chia vector thành $h$ "đầu" độc lập (ví dụ $h = 8$ heads, mỗi head có chiều $d_k = d_{\text{model}} / h = 512 / 8 = 64$).
  - Head 1 chuyên chú ý đến mối quan hệ ngữ pháp (Chủ ngữ - Vị ngữ).
  - Head 2 chuyên chú ý đến quan hệ đại từ thay thế (*"nó"* liên kết với *"con gấu"*).
  - Head 3 chuyên chú ý đến bối cảnh thời gian, địa điểm.
  - Kết quả của $h$ heads được ghép nối (Concat) lại và nhân qua ma trận $W_O$:
    $$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_h) W_O$$
- **Mã Hóa Vị Trí (Positional Encoding):** Vì phép tính Self-Attention hoàn toàn không phụ thuộc vào thứ tự trước sau của các từ (tính chất giao hoán hoán vị - Permutation Equivariant), nếu không có cơ chế đánh dấu vị trí thì hai câu: *"Mèo bắt chuột"* và *"Chuột bắt mèo"* sẽ cho ra ma trận chú ý y hệt nhau! Transformer khắc phục điều này bằng cách cộng trực tiếp một vector tọa độ vị trí $PE$ (dùng hàm $\sin$ và $\cos$) vào vector nhúng từ ban đầu.""" ,
                "formula": r"\text{Attention}(Q, K, V) = \text{Softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V, \quad \text{Var}\left(\frac{Q K^T}{\sqrt{d_k}}\right) = 1.0",
                "mathExplainer": [
                    { "sym": "Q, K, V", "name": "Query, Key, Value", "mean": "Ba ma trận được chiếu từ đầu vào: Q là truy vấn, K là khóa so khớp, V là giá trị nội dung." },
                    { "sym": r"\sqrt{d_k}", "name": "Hệ số tỉ lệ thu nhỏ", "mean": "Chia căn bậc hai số chiều để đưa phương sai tích vô hướng về 1, tránh bão hòa Softmax." },
                    { "sym": r"\text{Softmax}", "name": "Hàm làm mềm xác suất", "mean": "Chuyển điểm số thô thành phân phối xác suất trọng số chú ý có tổng bằng 1 trên mỗi hàng." },
                    { "sym": r"\text{MultiHead}", "name": "Chú ý đa đầu", "mean": "Chia nhiều không gian con song song giúp mô hình học đa dạng góc nhìn ngữ cảnh." },
                    { "sym": r"\text{Positional Encoding}", "name": "Mã hóa vị trí", "mean": "Vector hàm sin/cos bù đắp thông tin thứ tự từ cho cơ chế Self-Attention." }
                ],
                "diagram": {
                    "svg": r"""<svg viewBox="0 0 660 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
                      <rect width="660" height="170" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Left: Scaled Dot-Product Flow -->
                      <g transform="translate(30, 15)">
                        <text x="110" y="14" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Scaled Dot-Product Attention (Câu 74 VAIO)</text>
                        <!-- Q, K, V inputs -->
                        <rect x="20" y="28" width="40" height="20" fill="#fff" stroke="#111" stroke-width="1.2" rx="2"/>
                        <text x="40" y="42" font-family="Georgia" font-size="9.5" font-weight="bold" text-anchor="middle">Q</text>
                        <rect x="75" y="28" width="40" height="20" fill="#fff" stroke="#111" stroke-width="1.2" rx="2"/>
                        <text x="95" y="42" font-family="Georgia" font-size="9.5" font-weight="bold" text-anchor="middle">K</text>
                        <rect x="160" y="28" width="40" height="20" fill="#fff" stroke="#111" stroke-width="1.2" rx="2"/>
                        <text x="180" y="42" font-family="Georgia" font-size="9.5" font-weight="bold" text-anchor="middle">V</text>
                        <!-- Q x K^T -->
                        <line x1="40" y1="48" x2="67" y2="62" stroke="#111" stroke-width="1.2"/>
                        <line x1="95" y1="48" x2="67" y2="62" stroke="#111" stroke-width="1.2"/>
                        <rect x="35" y="62" width="65" height="20" fill="#fff" stroke="#111" stroke-width="1.2" rx="2"/>
                        <text x="67" y="75" font-family="Georgia" font-size="8.5" text-anchor="middle">MatMul (Q·Kᵀ)</text>
                        <!-- Scale / sqrt(d_k) -->
                        <line x1="67" y1="82" x2="67" y2="92" stroke="#111" stroke-width="1.2"/>
                        <rect x="30" y="92" width="75" height="20" fill="#e0e0e0" stroke="#111" stroke-width="1.2" rx="2"/>
                        <text x="67" y="105" font-family="Georgia" font-size="8.5" font-weight="bold" text-anchor="middle">Scale (÷ √d_k)</text>
                        <!-- Softmax -->
                        <line x1="67" y1="112" x2="67" y2="122" stroke="#111" stroke-width="1.2"/>
                        <rect x="25" y="122" width="85" height="20" fill="#111" rx="2"/>
                        <text x="67" y="135" font-family="Georgia" font-size="8.5" fill="#fff" font-weight="bold" text-anchor="middle">Softmax</text>
                        <!-- MatMul with V -->
                        <line x1="110" y1="132" x2="150" y2="132" stroke="#111" stroke-width="1.2"/>
                        <line x1="180" y1="48" x2="180" y2="122" stroke="#111" stroke-width="1.2"/>
                        <rect x="150" y="122" width="60" height="20" fill="#fff" stroke="#111" stroke-width="1.5" rx="2"/>
                        <text x="180" y="135" font-family="Georgia" font-size="9" font-weight="bold" text-anchor="middle">Output</text>
                      </g>
                      <!-- Right: The "Why divide by sqrt(d_k)" box -->
                      <g transform="translate(290, 20)">
                        <rect x="0" y="0" width="345" height="135" fill="#fff" stroke="#111" stroke-width="1" rx="3"/>
                        <text x="172" y="20" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Tại Sao Chia Cho Căn Bậc Hai d_k?</text>
                        <text x="15" y="42" font-family="Georgia" font-size="9">• Tích vô hướng Q·Kᵀ có phương sai = d_k.</text>
                        <text x="15" y="60" font-family="Georgia" font-size="9">• Nếu d_k lớn (vd 64, 512) → giá trị bùng nổ cực lớn.</text>
                        <text x="15" y="78" font-family="Georgia" font-size="9">• Đẩy hàm Softmax vào <tspan font-weight="bold">vùng bão hòa (Saturation)</tspan>.</text>
                        <text x="15" y="96" font-family="Georgia" font-size="9">• Đạo hàm Softmax bị triệt tiêu ≈ 0 → <tspan font-weight="bold" fill="#111">Tiêu biến gradient!</tspan></text>
                        <rect x="12" y="106" width="320" height="22" fill="#f0f0f0" rx="2"/>
                        <text x="172" y="120" font-family="Georgia" font-size="8.5" font-weight="bold" text-anchor="middle">⇒ Chia √d_k đưa phương sai về chuẩn 1.0, ổn định đạo hàm!</text>
                      </g>
                    </svg>""",
                    "caption": "Sơ đồ khối tính toán Scaled Dot-Product Attention và giải thích bản chất toán học tại sao phải chia cho căn bậc hai của d_k."
                },
                "commonPitfalls": r"""Cạm bẫy phòng thi Câu 74 & 23 Đề thi chính thức VAIO 2025:
1. **Hiểu sai lý do chia cho $\sqrt{d_k}$:**
   - Đề thi thường đưa các đáp án bẫy như: *"Để giảm số phép nhân ma trận"*, *"Để biến ma trận thành đối xứng"*, *"Để loại bỏ từ dừng"*.
   - ĐÁP ÁN ĐÚNG DUY NHẤT: Để ngăn tích vô hướng quá lớn đẩy hàm Softmax vào vùng bão hòa gradient (gradient gần bằng 0 gây tiêu biến gradient)!
2. **Kích thước ma trận Attention:** Ma trận $QK^T$ luôn có kích thước $N \times N$ (với $N$ là độ dài chuỗi token). Đây là lý do độ phức tạp tính toán và bộ nhớ của Self-Attention tiêu chuẩn là $O(N^2)$ theo độ dài văn bản!""",
                "practiceQuestion": {
                    "level": "Nâng cao (Câu 74 Đề Thi Chính Thức VAIO 2025)",
                    "question": "Trong công thức Scaled Dot-Product Attention của mô hình Transformer, mục đích chính của việc chia tích vô hướng Q·K^T cho hệ số căn bậc hai của d_k là gì?",
                    "options": [
                        "A. Để giảm số lượng phép nhân ma trận giữa các vector từ",
                        "B. Để ngăn giá trị tích vô hướng quá lớn khiến hàm softmax bị bão hòa gradient (gradient tiến sát về 0 gây tiêu biến gradient)",
                        "C. Để đảm bảo ma trận attention trở thành ma trận đường chéo",
                        "D. Để tự động loại bỏ các từ dừng và ký tự đặc biệt"
                    ],
                    "correctIndex": 1,
                    "hint": "Khi số chiều d_k lớn, phương sai của tích vô hướng bằng d_k, khiến giá trị đầu vào của Softmax rất lớn, đẩy đạo hàm của Softmax về 0.",
                    "solution": [
                        "Phân tích xác suất: Giả sử q và k có phương sai bằng 1, tích vô hướng của chúng có phương sai bằng đúng số chiều d_k.",
                        "Khi d_k lớn, tích vô hướng nhận các giá trị rất lớn, đẩy hàm Softmax vào vùng cực biên (bão hòa), nơi mà đạo hàm gần như bằng 0.",
                        "Điều này gây ra hiện tượng tiêu biến gradient (vanishing gradient), cản trở việc cập nhật trọng số trong quá trình tối ưu hóa.",
                        "Việc chia cho căn bậc hai của d_k giúp chuẩn hóa phương sai về lại 1.0, giữ cho gradient luôn ổn định và dòng chảy thông suốt.",
                        "Đáp án chính xác là B."
                    ]
                }
            },

            # =================================================================
            # MỤC 12.5: ĐỐI ĐẦU BERT VS GPT & CAUSAL MASKING (CÂU 20 & 65 VAIO)
            # =================================================================
            {
                "heading": "12.5. Kiến Trúc Transformer Toàn Diện: Đối Đầu Encoder-Only (BERT) vs Decoder-Only (GPT) & Cơ Chế Causal Masking (Câu 20 & 65 VAIO)",
                "content": "Phân tích cấu trúc khối Transformer chuẩn (LayerNorm, Residual Connection, FFN); giải mã 3 thành phần đầu vào của BERT (Câu 20 VAIO) và token [CLS] (Câu 65 VAIO); cơ chế Causal Masking tạo sinh của GPT và bảng so sánh đối đầu toàn diện.",
                "deepDive": r"""**1. Cấu trúc một khối Transformer chuẩn mực (Transformer Block):**
Mỗi khối Transformer được ghép từ hai tầng con cốt lõi (Sub-layers):
1. **Tầng Multi-Head Attention:** Cho phép các token giao tiếp và tổng hợp thông tin từ nhau.
2. **Tầng Mạng Nơ-ron Truyền Thẳng (Feed-Forward Network - FFN):** Gồm 2 tầng kết nối đầy đủ (Linear) với hàm kích hoạt phi tuyến tính (như ReLU hoặc GELU) xử lý độc lập trên từng vị trí token:
   $$\text{FFN}(x) = \max(0, x W_1 + b_1) W_2 + b_2$$

Bao bọc quanh mỗi tầng con là cơ chế **Kết nối tắt (Residual Connection) & Chuẩn hóa tầng (Layer Normalization)**:
$$\text{Output} = \text{LayerNorm}(x + \text{SubLayer}(x))$$
*Tại sao Transformer dùng Layer Normalization (LayerNorm) thay vì Batch Normalization (BatchNorm) của CNN?*
- BatchNorm chuẩn hóa qua toàn bộ các mẫu trong cùng một mini-batch. Trong NLP, mỗi câu văn có độ dài khác nhau, và kích thước batch khi suy luận có thể chỉ là 1 câu $\to$ BatchNorm hoạt động rất kém.
- LayerNorm chuẩn hóa qua tất cả các đặc trưng của **cùng một token đơn lẻ**, hoàn toàn độc lập với kích thước mini-batch và độ dài chuỗi!

---

**2. Nhánh Encoder-Only: Mô hình BERT (Devlin et al., Google 2018 - CÂU 20 & 65 VAIO):**
BERT viết tắt của **Bidirectional Encoder Representations from Transformers**. Đây là mô hình chuyên gia về **Hiểu Ngôn Ngữ Tự Nhiên (NLU - Natural Language Understanding)**.

- **Cơ chế Chú Ý Hai Chiều (Bidirectional Attention):**
  Khi đọc một từ, BERT được phép nhìn thấy cả các từ đứng trước nó (bên trái) và các từ đứng sau nó (bên phải) cùng một lúc. Giống như một học sinh đọc đi đọc lại cả đoạn văn để hiểu trọn vẹn ngữ nghĩa.
- **3 THÀNH PHẦN ĐẦU VÀO HOÀN CHỈNH CỦA BERT (CÂU 20 ĐỀ THI CHÍNH THỨC VAIO 2025):**
  Để đưa dữ liệu vào BERT, ta không chỉ đưa văn bản thô mà phải chuẩn bị đúng **3 Tensor đầu vào đồng thời**:
  1. **Token IDs (Vector chỉ số từ):** Danh sách các số nguyên định danh vị trí của từng token trong từ điển WordPiece (gồm token đặc biệt `[CLS]` ở đầu câu và `[SEP]` ở cuối câu hoặc ngăn cách hai câu).
  2. **Attention Mask (Mặt nạ chú ý):** Tensor nhị phân gồm các số $1$ và $0$:
     - Giá trị $1$: Vị trí chứa token từ ngữ thực sự (mô hình cần chú ý).
     - Giá trị $0$: Vị trí của các token đệm `[PAD]` (mô hình phải bỏ qua, không tính attention).
  3. **Token Type IDs (Segment Embeddings - Chỉ số loại token):** Phân biệt câu thứ nhất (mang giá trị $0$) và câu thứ hai (mang giá trị $1$) khi đưa một cặp câu vào mô hình (như trong bài toán Hỏi - Đáp hoặc Suy luận ngữ nghĩa).
- **Hai nhiệm vụ tiền huấn luyện (Pre-training Objectives):**
  1. *Masked Language Modeling (MLM - Điền từ vào chỗ trống):* Che ngẫu nhiên 15% token bằng ký hiệu `[MASK]` và bắt mô hình đoán từ bị che dựa trên ngữ cảnh 2 chiều.
  2. *Next Sentence Prediction (NSP - Dự đoán câu kế tiếp):* Cho cặp câu (A, B), dự đoán B có phải câu nối tiếp tự nhiên của A hay không.
- **Quy trình Tinh Chỉnh (Fine-tuning - CÂU 65 VAIO):**
  Để fine-tune BERT cho bài toán phân loại văn bản (như phân tích cảm xúc tích cực/tiêu cực):
  - Ta đặt một lớp phân loại tuyến tính (Classification Head) gắn trực tiếp vào vector biểu diễn đầu ra của **token đặc biệt `[CLS]`** (Classification Token)!
  - Vector của `[CLS]` đã tích lũy và tóm tắt toàn bộ thông tin ngữ nghĩa của toàn bộ câu qua các tầng Self-Attention hai chiều.

---

**3. Nhánh Decoder-Only: Mô hình GPT (OpenAI - Generative Pre-trained Transformer):**
GPT là mô hình chuyên gia về **Tạo Sinh Ngôn Ngữ Tự Nhiên (NLG - Natural Language Generation)**, nền tảng của ChatGPT.

- **Cơ chế Chú Ý Tự Hồi Quy Một Chiều (Autoregressive & Causal Masking):**
  - Khác với BERT, GPT sinh văn bản từ trái sang phải, từng từ một.
  - Khi đang dự đoán từ thứ $t$, mô hình **TUYỆT ĐỐI KHÔNG ĐƯỢC PHÉP NHÌN LÉN** các từ tương lai $t+1, t+2, \dots$!
- **Mặt nạ nhân quả (Causal Mask / Look-ahead Mask):**
  Trong ma trận chú ý $QK^T$, tất cả các vị trí tương lai ở góc tam giác trên ($j > i$) bị ép gán bằng $-\infty$ trước khi đưa vào Softmax:
  $$\text{Mask}_{ij} = \begin{cases} 0 & \text{nếu } j \le i \\ -\infty & \text{nếu } j > i \end{cases}$$
  Vì $e^{-\infty} = 0$, trọng số chú ý tới các từ tương lai bị triệt tiêu hoàn toàn về $0.0$.
- **Nhiệm vụ huấn luyện:** Dự đoán từ tiếp theo (Next Token Prediction / Causal Language Modeling) bằng hàm mất mát Cross-Entropy.

---

**4. Bảng So Sánh Đối Đầu Kinh Điển: BERT vs GPT:**

| Tiêu Chí | BERT (Encoder-Only) | GPT (Decoder-Only) |
| :--- | :--- | :--- |
| **Hướng Chú Ý** | **Hai chiều (Bidirectional)**: Nhìn cả trái và phải | **Một chiều (Unidirectional / Causal)**: Chỉ nhìn bên trái |
| **Cơ Chế Mask** | Che ngẫu nhiên 15% token (`[MASK]`) | Che toàn bộ tam giác trên bằng $-\infty$ (Causal Mask) |
| **Đầu Vào (Câu 20)** | **Token IDs, Attention Mask, Token Type IDs** | Token IDs, Attention Mask (tùy chọn) |
| **Mục Tiêu Huấn Luyện**| MLM (Masked LM) + NSP (Next Sentence) | Next Token Prediction (Tự hồi quy) |
| **Fine-tune Phân Loại (Câu 65)** | Gắn lớp phân loại vào token **`[CLS]`** | Lấy token cuối cùng của chuỗi |
| **Điểm Mạnh Cốt Lõi** | Đọc hiểu, phân loại văn bản, trích xuất thực thể (NER) | **Sinh văn bản tự do, viết luận, lập trình, Chatbot hội thoại** |""" ,
                "formula": r"\text{BERT Input} = \{ \text{Token IDs}, \text{Attention Mask}, \text{Token Type IDs} \}, \quad \text{Mask}_{ij} = -\infty \text{ (if } j > i \text{)}",
                "mathExplainer": [
                    { "sym": r"\text{Token IDs}", "name": "Chỉ số từ vựng", "mean": "Mã số định danh các token trong bảng từ điển WordPiece (kèm [CLS], [SEP])." },
                    { "sym": r"\text{Attention Mask}", "name": "Mặt nạ chú ý", "mean": "Tensor nhị phân 1/0 phân biệt token nội dung thật và khoảng đệm padding [PAD]." },
                    { "sym": r"\text{Token Type IDs}", "name": "Chỉ số loại token", "mean": "Tensor phân biệt câu A (giá trị 0) và câu B (giá trị 1) trong cặp câu đầu vào." },
                    { "sym": r"\text{[CLS]}", "name": "Classification Token", "mean": "Token đặc biệt đứng đầu câu BERT dùng để gắn Classification Head khi fine-tune." },
                    { "sym": r"\text{Causal Mask}", "name": "Mặt nạ nhân quả GPT", "mean": "Che các vị trí tương lai bằng trừ vô cùng để mô hình không nhìn lén khi tạo sinh." }
                ],
                "diagram": {
                    "svg": r"""<svg viewBox="0 0 660 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
                      <rect width="660" height="170" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Left: BERT Bidirectional Attention -->
                      <g transform="translate(25, 20)">
                        <text x="130" y="14" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">BERT (Encoder - Hai Chiều)</text>
                        <!-- 4x4 Full Attention Grid -->
                        <g transform="translate(15, 30)">
                          <rect x="0" y="0" width="80" height="80" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <!-- all cells active (gray fill) -->
                          <rect x="0" y="0" width="80" height="80" fill="#333"/>
                          <line x1="20" y1="0" x2="20" y2="80" stroke="#fff" stroke-width="0.8"/>
                          <line x1="40" y1="0" x2="40" y2="80" stroke="#fff" stroke-width="0.8"/>
                          <line x1="60" y1="0" x2="60" y2="80" stroke="#fff" stroke-width="0.8"/>
                          <line x1="0" y1="20" x2="80" y2="20" stroke="#fff" stroke-width="0.8"/>
                          <line x1="0" y1="40" x2="80" y2="40" stroke="#fff" stroke-width="0.8"/>
                          <line x1="0" y1="60" x2="80" y2="60" stroke="#fff" stroke-width="0.8"/>
                          <text x="40" y="44" font-family="Georgia" font-size="9" fill="#fff" font-weight="bold" text-anchor="middle">Full 2 Chiều</text>
                        </g>
                        <!-- Explanation -->
                        <g transform="translate(110, 32)">
                          <text x="0" y="15" font-family="Georgia" font-size="9" font-weight="bold">Đầu vào BERT (Câu 20):</text>
                          <text x="5" y="30" font-family="Georgia" font-size="8">• 1. Token IDs</text>
                          <text x="5" y="44" font-family="Georgia" font-size="8">• 2. Attention Mask</text>
                          <text x="5" y="58" font-family="Georgia" font-size="8">• 3. Token Type IDs</text>
                          <text x="0" y="75" font-family="Georgia" font-size="8.5" font-weight="bold">Fine-tune: Token [CLS]</text>
                        </g>
                      </g>
                      <!-- Divider -->
                      <line x1="330" y1="20" x2="330" y2="155" stroke="#ccc" stroke-dasharray="2,2"/>
                      <!-- Right: GPT Causal Masking -->
                      <g transform="translate(355, 20)">
                        <text x="130" y="14" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">GPT (Decoder - Causal Mask 1 Chiều)</text>
                        <!-- 4x4 Triangular Mask Grid -->
                        <g transform="translate(15, 30)">
                          <rect x="0" y="0" width="80" height="80" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <!-- Upper triangle masked (-inf, white/pattern) -->
                          <!-- Lower triangle active (dark) -->
                          <rect x="0" y="0" width="20" height="80" fill="#333"/>
                          <rect x="20" y="20" width="20" height="60" fill="#333"/>
                          <rect x="40" y="40" width="20" height="40" fill="#333"/>
                          <rect x="60" y="60" width="20" height="20" fill="#333"/>
                          <!-- Grid lines -->
                          <line x1="20" y1="0" x2="20" y2="80" stroke="#ccc" stroke-width="0.8"/>
                          <line x1="40" y1="0" x2="40" y2="80" stroke="#ccc" stroke-width="0.8"/>
                          <line x1="60" y1="0" x2="60" y2="80" stroke="#ccc" stroke-width="0.8"/>
                          <line x1="0" y1="20" x2="80" y2="20" stroke="#ccc" stroke-width="0.8"/>
                          <line x1="0" y1="40" x2="80" y2="40" stroke="#ccc" stroke-width="0.8"/>
                          <line x1="0" y1="60" x2="80" y2="60" stroke="#ccc" stroke-width="0.8"/>
                          <text x="55" y="25" font-family="Georgia" font-size="8" fill="#999" text-anchor="middle">-∞</text>
                          <text x="65" y="45" font-family="Georgia" font-size="8" fill="#999" text-anchor="middle">-∞</text>
                        </g>
                        <!-- Explanation -->
                        <g transform="translate(110, 32)">
                          <text x="0" y="15" font-family="Georgia" font-size="9" font-weight="bold">Mặt Nạ Causal (-∞):</text>
                          <text x="5" y="30" font-family="Georgia" font-size="8">• Che các từ tương lai</text>
                          <text x="5" y="44" font-family="Georgia" font-size="8">• Không được nhìn lén</text>
                          <text x="5" y="58" font-family="Georgia" font-size="8">• Dự đoán Next Token</text>
                          <text x="0" y="75" font-family="Georgia" font-size="8.5" font-weight="bold">Mô hình Tạo Sinh (NLG)</text>
                        </g>
                      </g>
                      <!-- Bottom summary line -->
                      <g transform="translate(0, 135)">
                        <rect x="25" y="0" width="610" height="24" fill="#f0f0f0" rx="3"/>
                        <text x="330" y="16" font-family="Georgia" font-size="8.5" font-weight="bold" text-anchor="middle">BERT: Đọc hiểu 2 chiều (NLU)  |  GPT: Tự hồi quy 1 chiều tạo sinh từ trái sang phải (NLG)</text>
                      </g>
                    </svg>""",
                    "caption": "So sánh ma trận Attention: BERT chú ý toàn phần 2 chiều vs GPT dùng mặt nạ Causal Masking che góc tam giác trên bằng trừ vô cùng."
                },
                "commonPitfalls": r"""Cạm bẫy phòng thi Câu 20 & 65 Đề thi chính thức VAIO 2025:
1. **Thành phần đầu vào của BERT (Câu 20):**
   - Đề thi thường đưa các đáp án bẫy như: *"Chỉ văn bản thô"*, *"Cặp câu với nhúng"*, *"Từ rời rạc"*.
   - ĐÁP ÁN CHÍNH XÁC: Phải đủ bộ ba: **Vector ID (Token ID), Mặt nạ chú ý (Attention mask), ID loại token (Token type ID)**!
2. **Vị trí tinh chỉnh của BERT (Câu 65):** Token dùng để gắn Classification Head khi fine-tune phân loại chuỗi luôn luôn là token đặc biệt **`[CLS]`** đặt ở đầu câu!
3. **Cơ chế Causal Mask của GPT:** Chú ý rằng các vị trí tương lai bị gán bằng $-\infty$ (chứ không phải $0$), để sau khi qua hàm Softmax ($e^{-\infty}$) nó mới biến thành xác suất bằng $0$!""",
                "practiceQuestion": {
                    "level": "Cơ bản (Câu 20 Đề Thi Chính Thức VAIO 2025)",
                    "question": "Mô hình BERT nhận các thành phần tensor đầu vào hoàn chỉnh là gì? (Câu 20 Đề thi chính thức VAIO 2025)",
                    "options": [
                        "A. Vector ID (Token ID), Mặt nạ chú ý (Attention mask), ID loại token (Token type ID)",
                        "B. Chỉ văn bản thô (raw text)",
                        "C. Cặp câu với nhúng từ (word embeddings)",
                        "D. Danh sách các từ rời rạc đã được hạ chữ thường"
                    ],
                    "correctIndex": 0,
                    "hint": "BERT cần biết mã số từ, vị trí nào là padding cần bỏ qua, và ranh giới phân biệt giữa câu thứ nhất và câu thứ hai.",
                    "solution": [
                        "Đầu vào chuẩn của mô hình BERT bao gồm 3 tensor kết hợp:",
                        "1. Token IDs: Chỉ số nhận diện token trong từ điển WordPiece.",
                        "2. Attention Mask: Mặt nạ nhị phân đánh dấu token thật (1) và token đệm padding (0).",
                        "3. Token Type IDs (Segment IDs): Đánh dấu phân biệt câu A (0) và câu B (1) trong bài toán cặp câu.",
                        "Đáp án chính xác là A."
                    ]
                }
            },

            # =================================================================
            # MỤC 12.6: LLMS, PROMPT ENGINEERING & CHAIN-OF-THOUGHT (CÂU 16 VAIO)
            # =================================================================
            {
                "heading": "12.6. Kỷ Nguyên Mô Hình Ngôn Ngữ Lớn (LLMs), Kỹ Thuật Prompt Engineering & Chuỗi Suy Luận Chain-of-Thought (CoT - Câu 16 VAIO)",
                "content": "Khám phá định luật tỉ lệ Scaling Laws và năng lực bộc phát của LLMs; quy trình căn chỉnh RLHF 3 giai đoạn; nghệ thuật Prompt Engineering; bản chất đột phá của kỹ thuật Chuỗi Suy Luận Chain-of-Thought (Câu 16 VAIO) và giải pháp thích ứng tham số hiệu quả PEFT (LoRA).",
                "deepDive": r"""**1. Kỷ nguyên Mô Hình Ngôn Ngữ Lớn (Large Language Models - LLMs):**
Khi các kỹ sư tiếp tục tăng kích thước mô hình Transformer từ vài trăm triệu tham số lên hàng chục, hàng trăm tỷ tham số và nạp vào hàng nghìn tỷ token văn bản, một hiện tượng kỳ vĩ đã xảy ra:
- **Định luật tỉ lệ (Scaling Laws - Kaplan et al., OpenAI 2020):** Hiệu năng của mô hình tăng trưởng theo hàm mũ mượt mà tỉ lệ thuận với 3 yếu tố: Số lượng tham số ($N$), Kích thước tập dữ liệu ($D$) và Lượng tính toán ($C$).
- **Năng lực bộc phát (Emergent Abilities):** Khi mô hình vượt qua một ngưỡng quy mô nhất định (thường trên 10 tỷ - 50 tỷ tham số), nó đột ngột sở hữu những khả năng kỳ diệu mà các mô hình nhỏ hoàn toàn không có: Giải toán học nhiều bước, Lập trình mã nguồn phức tạp, Hiểu sự châm biếm, Suy luận bắc cầu và Dịch thuật đa ngôn ngữ!

---

**2. Quy trình Căn Chỉnh RLHF 3 giai đoạn (Reinforcement Learning from Human Feedback):**
Một mô hình ngôn ngữ sau giai đoạn Pre-training (huấn luyện trước) chỉ đơn thuần là một cỗ máy dự đoán từ tiếp theo. Nó có thể nói huyên thuyên, bịa đặt thông tin (Ảo giác - Hallucination) hoặc sinh ra nội dung độc hại. Để biến nó thành một trợ lý AI hữu ích, an toàn và trung thực, OpenAI đã áp dụng quy trình **RLHF 3 giai đoạn**:
1. **Giai đoạn 1: Tinh chỉnh có giám sát (SFT - Supervised Fine-Tuning):** Thu thập hàng chục nghìn cặp (Prompt của người dùng, Câu trả lời mẫu mực do chuyên gia con người biên soạn) để dạy mô hình cách trả lời lễ phép và đúng trọng tâm.
2. **Giai đoạn 2: Mô hình hóa phần thưởng (Reward Modeling - RM):** Cho mô hình sinh ra 4 câu trả lời khác nhau cho cùng một câu hỏi. Con người xếp hạng từ tốt nhất đến tệ nhất ($A > B > C > D$). Huấn luyện một mạng nơ-ron chấm điểm (Reward Model) để dự đoán sở thích của con người.
3. **Giai đoạn 3: Tối ưu hóa chính sách PPO (Proximal Policy Optimization):** Dùng điểm số của Reward Model làm tín hiệu phần thưởng để tinh chỉnh LLM bằng thuật toán học tăng cường PPO, kèm theo hàm phạt KL-Divergence để mô hình không bị lệch quá xa khỏi phân phối ngôn ngữ gốc.

---

**3. Nghệ thuật Kỹ Thuật Gợi Ý (Prompt Engineering):**
Prompt là câu lệnh hoặc hướng dẫn đầu vào mà người dùng cung cấp cho LLM.
- **Zero-shot Prompting:** Đặt câu hỏi trực tiếp không kèm theo bất kỳ ví dụ mẫu nào:
  $$\text{Prompt: "Hãy dịch câu sau sang tiếng Pháp: Tôi yêu trí tuệ nhân tạo."}$$
- **Few-shot Prompting (In-Context Learning):** Cung cấp 2 - 3 cặp ví dụ minh họa (mẫu câu hỏi và lời giải) ngay trong ngữ cảnh trước khi đưa ra câu hỏi chính. Mô hình tự động nhận diện quy luật và bắt chước khuôn mẫu mà không cần cập nhật bất kỳ trọng số nào!

---

**4. KỸ THUẬT CHUỖI SUY LUẬN CHAIN-OF-THOUGHT (CoT - CÂU 16 ĐỀ THI CHÍNH THỨC VAIO 2025):**
Năm 2022, bài báo chấn động của Jason Wei và nhóm Google Research đã công bố kỹ thuật **Chain-of-Thought (CoT)**.

- **Vấn đề của phương pháp Prompting truyền thống (Standard Prompting):**
  Khi gặp các bài toán đố nhiều bước, toán học hoặc suy luận logic, nếu ép mô hình đưa ra ngay đáp án cuối cùng, mô hình Transformer tự hồi quy thường đoán mò và đưa ra kết quả sai bét. Lý do: Mô hình không có "không gian bộ nhớ nháp" để thực hiện các phép tính trung gian!
- **Bản chất của Chain-of-Thought (Câu 16 VAIO):**
  Thúc đẩy mô hình giải quyết bài toán phức tạp bằng cách **LIỆT KÊ TỪNG BƯỚC SUY LUẬN TRUNG GIAN (Intermediate reasoning steps)** trước khi đưa ra kết luận cuối cùng!
- **Sức mạnh kỳ diệu của Zero-shot CoT (Kojima et al., 2022):**
  Chỉ cần thêm một câu thần chú ngắn ngủi vào cuối prompt:
  $$\text{"Hãy suy nghĩ từng bước một (Let's think step by step)"}$$
  Độ chính xác của mô hình trên tập bài toán đố tiểu học GSM8K tăng vọt ngoạn mục từ **17.7% lên tới 78.7%**!

*Tại sao Chain-of-Thought lại hiệu quả đến mức thần kỳ như vậy?*
- Về bản chất toán học, mô hình Transformer dự đoán token tiếp theo dựa trên tất cả các token xuất hiện trước đó.
- Khi mô hình tự viết ra bước suy luận 1, các token của bước 1 trở thành ngữ cảnh đầu vào mới. Cơ chế Self-Attention dùng các token này để tính toán bước suy luận 2.
- CoT đã phân rã một bài toán hóc búa có độ phức tạp cao thành một chuỗi các bước suy luận đơn giản, cho phép mạng nơ-ron phân bổ năng lực tính toán tương xứng với độ khó của bài toán!

---

**5. Thách thức tài nguyên tính toán & Kỹ thuật Tinh chỉnh hiệu quả tham số (PEFT - LoRA):**
- *Liên hệ Câu 4 VAIO:* Các mô hình LLM ngày nay có từ 7 tỷ đến 70 tỷ tham số. Việc fine-tune toàn bộ trọng số (Full Fine-tuning) đòi hỏi cụm siêu máy tính hàng trăm GPU chuyên dụng với dung lượng VRAM khổng lồ $\to$ Hầu như bất khả thi đối với học sinh hay doanh nghiệp vừa và nhỏ!
- **Giải pháp LoRA (Low-Rank Adaptation - Hu et al., 2021):**
  Đóng băng 100% trọng số của mô hình gốc $W_0 \in \mathbb{R}^{d \times k}$. Khi huấn luyện, ta chỉ gắn thêm hai ma trận tích hạng thấp kích thước siêu nhỏ $A \in \mathbb{R}^{d \times r}$ và $B \in \mathbb{R}^{r \times k}$ (với hạng $r \ll d$, thường chọn $r = 8$ hoặc $16$):
  $$W = W_0 + \Delta W = W_0 + B \cdot A$$
  Số lượng tham số cần cập nhật giảm hơn **99.9%**, cho phép tinh chỉnh các mô hình ngôn ngữ lớn mạnh mẽ ngay trên một chiếc máy tính cá nhân!""" ,
                "formula": r"\text{Chain-of-Thought: Input} \xrightarrow{} \text{Step 1} \xrightarrow{} \text{Step 2} \xrightarrow{} \dots \xrightarrow{} \text{Final Answer}, \quad W = W_0 + B \cdot A",
                "mathExplainer": [
                    { "sym": r"\text{Chain-of-Thought (CoT)}", "name": "Chuỗi suy luận trung gian", "mean": "Thúc đẩy LLM giải bài toán bằng cách phân tích từng bước lập luận trước khi chốt đáp án." },
                    { "sym": r"\text{Zero-shot CoT}", "name": "CoT không mẫu", "mean": "Thêm câu lệnh 'Hãy suy nghĩ từng bước một' để kích hoạt năng lực suy luận tự nhiên của LLM." },
                    { "sym": r"\text{Few-shot Prompting}", "name": "Gợi ý kèm ví dụ mẫu", "mean": "Cung cấp một vài cặp mẫu (hỏi - đáp) để mô hình học theo ngữ cảnh (In-Context Learning)." },
                    { "sym": r"\text{RLHF}", "name": "Học tăng cường từ phản hồi người", "mean": "Quy trình căn chỉnh 3 bước (SFT -> Reward Model -> PPO) giúp AI an toàn và hữu ích." },
                    { "sym": r"\text{LoRA } (B \cdot A)", "name": "Thích ứng tích hạng thấp", "mean": "Phương pháp PEFT đóng băng mô hình gốc, chỉ học ma trận hạng nhỏ giúp tiết kiệm 99% VRAM." }
                ],
                "diagram": {
                    "svg": r"""<svg viewBox="0 0 660 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
                      <rect width="660" height="170" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Left: Standard Prompting (Fails) -->
                      <g transform="translate(25, 20)">
                        <text x="135" y="14" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Standard Prompting (Đoán Mò)</text>
                        <rect x="0" y="28" width="270" height="42" fill="#fff" stroke="#111" stroke-width="1.2" rx="3"/>
                        <text x="10" y="44" font-family="Georgia" font-size="8.5" font-weight="bold">Câu hỏi:</text>
                        <text x="55" y="44" font-family="Georgia" font-size="8">Mai có 5 quả táo, mẹ cho thêm 3 quả,</text>
                        <text x="10" y="58" font-family="Georgia" font-size="8">Mai ăn mất 2 quả. Hỏi Mai còn mấy quả?</text>
                        <!-- Arrow down -->
                        <line x1="135" y1="70" x2="135" y2="85" stroke="#111" stroke-width="1.2"/>
                        <polygon points="135,85 131,79 139,79" fill="#111"/>
                        <!-- Output Direct Answer -->
                        <rect x="35" y="85" width="200" height="35" fill="#f5f5f5" stroke="#111" rx="3"/>
                        <text x="135" y="102" font-family="Georgia" font-size="9" fill="#999" text-anchor="middle">Đáp án: 7 quả (SAI! Ảo giác)</text>
                        <text x="135" y="114" font-family="Georgia" font-size="7.5" fill="#555" text-anchor="middle">Thiếu bước tính trung gian</text>
                      </g>
                      <!-- Divider -->
                      <line x1="320" y1="20" x2="320" y2="155" stroke="#ccc" stroke-dasharray="2,2"/>
                      <!-- Right: Chain-of-Thought (Succeeds) -->
                      <g transform="translate(345, 20)">
                        <text x="145" y="14" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Chain-of-Thought (Câu 16 VAIO)</text>
                        <rect x="0" y="28" width="290" height="42" fill="#fff" stroke="#111" stroke-width="1.2" rx="3"/>
                        <text x="10" y="44" font-family="Georgia" font-size="8.5" font-weight="bold">Prompt:</text>
                        <text x="55" y="44" font-family="Georgia" font-size="8">... (Cùng bài toán trên) ...</text>
                        <text x="10" y="58" font-family="Georgia" font-size="8" font-weight="bold" fill="#111">"Hãy suy nghĩ từng bước một"</text>
                        <!-- Arrow down -->
                        <line x1="145" y1="70" x2="145" y2="80" stroke="#111" stroke-width="1.2"/>
                        <polygon points="145,80 141,74 149,74" fill="#111"/>
                        <!-- Step by step box -->
                        <rect x="0" y="80" width="290" height="52" fill="#111" rx="3"/>
                        <text x="10" y="95" font-family="Georgia" font-size="8" fill="#fff">• Bước 1: Sau khi mẹ cho: 5 + 3 = 8 quả.</text>
                        <text x="10" y="108" font-family="Georgia" font-size="8" fill="#fff">• Bước 2: Sau khi ăn 2 quả: 8 - 2 = 6 quả.</text>
                        <text x="10" y="122" font-family="Georgia" font-size="8.5" font-weight="bold" fill="#fff">⇒ Đáp án cuối cùng: 6 quả (ĐÚNG 100%!)</text>
                      </g>
                      <!-- Bottom summary -->
                      <g transform="translate(0, 142)">
                        <text x="330" y="15" font-family="Georgia" font-size="8.5" font-weight="bold" text-anchor="middle">CoT mở khóa năng lực suy luận logic bằng cách liệt kê từng bước trung gian!</text>
                      </g>
                    </svg>""",
                    "caption": "So sánh Standard Prompting (đoán mò đáp án trực tiếp dễ sai) vs Chain-of-Thought (lập luận từng bước trung gian giải quyết bài toán phức tạp)."
                },
                "commonPitfalls": r"""Cạm bẫy phòng thi Câu 16 Đề thi chính thức VAIO 2025:
1. **Hiểu sai định nghĩa của Chain-of-Thought (Câu 16):**
   - Đề thi thường đưa các đáp án bẫy như: *"Yêu cầu mô hình trả lời càng ngắn gọn càng tốt để tiết kiệm tài nguyên"*, *"Huấn luyện mô hình sinh câu hỏi thay vì câu trả lời"*, *"Dự đoán từ tiếp theo bằng dữ liệu song ngữ"*.
   - ĐÁP ÁN ĐÚNG DUY NHẤT: Thúc đẩy mô hình giải bài toán bằng cách **liệt kê từng bước suy luận trung gian (Intermediate reasoning steps)**!
2. **Khái niệm Few-shot Prompting:** Không phải là cập nhật lại trọng số (fine-tuning) mà là đưa các ví dụ mẫu trực tiếp vào trong ngữ cảnh gợi ý (In-Context Learning).""",
                "practiceQuestion": {
                    "level": "Cơ bản (Câu 16 Đề Thi Chính Thức VAIO 2025)",
                    "question": "Kỹ thuật Chain-of-Thought (CoT) trong các mô hình ngôn ngữ lớn (LLM) là gì? (Câu 16 Đề thi chính thức VAIO 2025)",
                    "options": [
                        "A. Yêu cầu mô hình trả lời càng ngắn gọn càng tốt để tiết kiệm tài nguyên tính toán",
                        "B. Huấn luyện mô hình dự đoán từ tiếp theo bằng dữ liệu văn bản song ngữ",
                        "C. Yêu cầu mô hình sinh câu hỏi thay vì sinh câu trả lời",
                        "D. Thúc đẩy mô hình giải bài toán bằng cách liệt kê từng bước suy luận trung gian"
                    ],
                    "correctIndex": 3,
                    "hint": "Chain-of-Thought có nghĩa là 'chuỗi suy nghĩ' - hướng dẫn mô hình tư duy từng bước như con người giải toán.",
                    "solution": [
                        "Kỹ thuật Chain-of-Thought (CoT - Chuỗi suy nghĩ) hướng dẫn mô hình phân tích bài toán thành các bước lập luận trung gian từng bước một trước khi đưa ra kết luận cuối cùng.",
                        "Điều này giúp mô hình phân bổ không gian tính toán và sử dụng cơ chế Self-Attention nhìn lại các kết quả trung gian, làm tăng vượt bậc độ chính xác trong giải toán và suy luận logic.",
                        "Đáp án chính xác là D."
                    ]
                }
            }
        ],
        "interactiveWidget": "widget-attention-matrix",
        "examConnection": {
            "questionTitle": "Tổng Hợp Các Dạng Bài Thi Olympic AI Về NLP, Attention & LLMs",
            "items": [
                {
                    "code": "Câu 14 (Đề Chính Thức)",
                    "problem": "Thứ tự 4 bước tiền xử lý văn bản thô chuẩn mực trong bài toán NLP.",
                    "solution": [
                        "Quy trình chuẩn: 2. Chuẩn hóa văn bản (Lowercasing, xóa ký tự lạ) → 1. Tách từ (Tokenization) → 3. Rút gọn từ (Stemming/Lemmatization) → 4. Gán nhãn từ loại (POS Tagging). Đáp án B."
                    ]
                },
                {
                    "code": "Câu 19 & 91 (Đề Chính Thức)",
                    "problem": "Mục tiêu huấn luyện của mô hình Word2Vec CBOW và GloVe.",
                    "solution": [
                        "CBOW: Dùng các từ ngữ cảnh xung quanh để dự đoán từ trung tâm P(w_t | context).",
                        "GloVe: Được huấn luyện từ Ma trận đồng xuất hiện toàn cục (Co-occurrence matrix) bằng phương pháp hồi quy bình phương tối thiểu có trọng số. Đáp án B."
                    ]
                },
                {
                    "code": "Câu 4 (Đề Chính Thức)",
                    "problem": "Tính số lượng tham số có thể huấn luyện của tầng mạng hồi quy RNN và LSTM.",
                    "solution": [
                        "RNN: Params = H × D + H × H + H = H(D + H + 1). Với D = 100, H = 128 ⇒ Params = 29,312.",
                        "LSTM (4 cổng độc lập): Params = 4 × H(D + H + 1) = 4 × 29,312 = 117,248 tham số."
                    ]
                },
                {
                    "code": "Câu 74 (Đề Chính Thức)",
                    "problem": "Mục đích của việc chia cho căn bậc hai d_k trong công thức Scaled Dot-Product Attention.",
                    "solution": [
                        "Để ngăn giá trị tích vô hướng quá lớn khiến hàm Softmax bị bão hòa gradient (gradient triệt tiêu về 0 gây tiêu biến gradient). Chia căn d_k đưa phương sai về chuẩn 1.0."
                    ]
                },
                {
                    "code": "Câu 20 & 65 (Đề Chính Thức)",
                    "problem": "3 thành phần tensor đầu vào của BERT và vị trí token dùng để fine-tune phân loại.",
                    "solution": [
                        "Đầu vào BERT gồm: Token IDs (chỉ số từ), Attention Mask (mặt nạ padding), Token Type IDs (phân biệt cặp câu A và B). Đáp án A (Câu 20).",
                        "Fine-tune: Đặt lớp phân loại lên vector đại diện của token đặc biệt [CLS] ở đầu câu (Câu 65)."
                    ]
                },
                {
                    "code": "Câu 16 (Đề Chính Thức)",
                    "problem": "Bản chất và định nghĩa của kỹ thuật Chain-of-Thought (CoT) trong LLMs.",
                    "solution": [
                        "Thúc đẩy mô hình giải bài toán phức tạp bằng cách liệt kê từng bước suy luận trung gian (Intermediate reasoning steps). Đáp án D."
                    ]
                }
            ]
        },
        "takeaways": [
            "Tiền xử lý văn bản chuẩn mực: Chuẩn hóa → Tách từ (Tokenization) → Rút gọn từ (Stemming/Lemma) → Gán nhãn từ loại (POS Tagging). Bắt buộc tokenize xong mới lọc từ dừng!",
            "Biểu diễn từ: One-Hot thất bại vì thưa thớt và trực giao; Word2Vec CBOW dùng ngữ cảnh đoán từ giữa; Skip-gram dùng từ giữa đoán ngữ cảnh; GloVe khớp ma trận đồng xuất hiện toàn cục.",
            "Đếm tham số mạng chuỗi: RNN có Params = H(D + H + 1); LSTM có 4 cổng van nên Params = 4 × H(D + H + 1); GRU có 3 cổng nên nhân 3.",
            "Scaled Dot-Product Attention: Softmax(QK^T / √d_k)V. Bắt buộc chia căn d_k để kiểm soát phương sai bằng 1.0, ngăn bão hòa Softmax và triệt tiêu gradient.",
            "BERT vs GPT: BERT đọc hiểu 2 chiều (nhận 3 đầu vào Token IDs, Attention mask, Token type IDs; fine-tune trên [CLS]); GPT tự hồi quy 1 chiều tạo sinh dùng Causal Masking che góc trên bằng -inf.",
            "Kỷ nguyên LLM & CoT: Thêm câu lệnh 'Hãy suy nghĩ từng bước một' thúc đẩy mô hình liệt kê các bước suy luận trung gian, tăng vọt độ chính xác giải toán và logic."
        ]
    }
