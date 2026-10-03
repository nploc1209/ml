# -*- coding: utf-8 -*-
"""
upgrade_lesson_3.py - Masterpiece Lesson 3 for VAIO 2025 AI Olympiad
Chủ đề: Xác Suất Nền Tảng & Bộ Phân Loại Naive Bayes (Toàn diện, từ số 0 đến làm chủ)

Tuân thủ nghiêm ngặt chuẩn sư phạm:
Trực giác đời sống -> Bản chất toán học -> Cách thức hoạt động ->
Giải mã ký hiệu cho học sinh lớp 12 -> Ví dụ tính toán bằng số từng bước ->
Cạm bẫy phòng thi -> Câu hỏi trắc nghiệm kiểm tra độ hiểu có lời giải chi tiết.
"""

def get_masterpiece_lesson_3():
    return {
        "id": "lesson-3",
        "title": "3. Xác Suất & Bộ Phân Loại Naive Bayes",
        "syllabusBadge": "BUỔI 2: XÁC SUẤT & GIẢ ĐỊNH NAIVE TRONG NLP",
        "summary": "Nền tảng xác suất của Trí tuệ nhân tạo: Đi từ trực giác không gian mẫu, xác suất có điều kiện, định lý Bayes cập nhật niềm tin, đến bộ phân loại Naive Bayes kinh điển trong xử lý ngôn ngữ tự nhiên. Làm chủ kỹ thuật làm mịn Laplace và Log-Likelihood tránh tràn số.",
        "intuition": {
            "title": "Trực giác thực tế: Bác sĩ chẩn đoán bệnh & Bộ lọc thư rác trong hộp thư",
            "content": """Hãy tưởng tượng bạn mở hộp thư điện tử Gmail vào buổi sáng. Trong số 100 email gửi đến, tại sao Gmail có thể tống ngay một email có tiêu đề 'CHÚC MỪNG BẠN TRÚNG THƯỞNG 10 TỶ NHẬN NGAY BITCOIN MIỄN PHÍ' vào hòm Thư rác (Spam) trong chưa đầy 1 phần nghìn giây?

Gmail không có trí thông minh ma thuật. Nó hoạt động y hệt một người bác sĩ giàu kinh nghiệm chẩn đoán bệnh:
1. **Niềm tin ban đầu (Xác suất tiên nghiệm - Prior):** Bác sĩ biết rằng trong mùa lạnh, tỷ lệ một người ngẫu nhiên mắc bệnh Cúm A là 5% ($P(\\text{Cúm}) = 0.05$). Tương tự, Gmail biết rằng trong toàn bộ thư từ trên Internet, thông thường có khoảng 20% là thư rác ($P(\\text{Spam}) = 0.20$).
2. **Quan sát bằng chứng mới (Dữ liệu quan sát - Evidence):** Bệnh nhân bước vào phòng khám với triệu chứng: Sốt cao và Ho dữ dội. Email gửi đến chứa các từ: 'trúng thưởng', 'bitcoin', 'miễn phí'.
3. **Độ hợp lý của triệu chứng (Likelihood):** Bác sĩ tự hỏi: 'Nếu một người thực sự bị Cúm A, xác suất họ bị sốt và ho là bao nhiêu?' - Rất cao, lên tới 90%! Tương tự, Gmail tự hỏi: 'Nếu một email thực sự là thư rác, xác suất nó chứa các từ trúng thưởng, bitcoin là bao nhiêu?' - Cực kỳ cao!
4. **Cập nhật niềm tin (Xác suất hậu nghiệm - Posterior):** Kết hợp niềm tin ban đầu và bằng chứng thực tế, bác sĩ kết luận: 'Xác suất bệnh nhân này bị cúm đã vọt từ 5% lên 88%!'. Gmail kết luận: 'Xác suất email này là Spam đã vọt từ 20% lên 99.9% -> Đẩy ngay vào thùng rác!'.

Đây chính là bản chất kỳ diệu của **Định Lý Bayes**: Khả năng cập nhật niềm tin của chúng ta về một giả thuyết sau khi thu thập thêm bằng chứng thực tế!"""
        },
        "sections": [
            # =================================================================
            # MỤC 3.1: NỀN TẢNG XÁC SUẤT DÀNH CHO NGƯỜI MỚI BẮT ĐẦU
            # =================================================================
            {
                "heading": "3.1. Nền Tảng Xác Suất Từ Con Số 0: Không Gian Mẫu, Biến Cố & Xác Suất Có Điều Kiện",
                "content": "Trước khi chạm vào AI hay Machine Learning, ta phải trả lời câu hỏi căn bản nhất: Xác suất là gì? Tại sao xác suất của một sự kiện lại thay đổi ngay khi ta có thêm thông tin mới?",
                "deepDive": r"""**1. Không gian mẫu và Biến cố (Nền móng toán học):**

- **Phép thử ngẫu nhiên (Random Experiment):** Một hành động mà kết quả không thể đoán trước chính xác, nhưng ta biết trước tất cả các kết quả có thể xảy ra. Ví dụ: Tung một con xúc xắc 6 mặt.
- **Không gian mẫu (Sample Space - ký hiệu $\Omega$ hoặc $S$):** Tập hợp chứa toàn bộ mọi kết quả có thể xảy ra của phép thử.
  $$\Omega = \{1, 2, 3, 4, 5, 6\} \implies |\Omega| = 6$$
- **Biến cố (Event - ký hiệu $A, B$):** Một tập con của không gian mẫu ($A \subseteq \Omega$).
  - Ví dụ biến cố $A$: 'Gieo được mặt chẵn' $\implies A = \{2, 4, 6\}$.
  - Xác suất cổ điển của biến cố $A$:
    $$P(A) = \frac{|A|}{|\Omega|} = \frac{3}{6} = 0.5 \quad (50\%)$$

**2. Các phép toán biến cố quan trọng:**
- **Biến cố giao ($A \cap B$ hoặc $AB$):** Cả $A$ và $B$ cùng đồng thời xảy ra.
- **Biến cố hợp ($A \cup B$):** Ít nhất một trong hai biến cố $A$ hoặc $B$ xảy ra. Công thức cộng xác suất:
  $$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$
- **Biến cố xung khắc (Mutually Exclusive):** $A$ và $B$ không thể cùng xảy ra ($A \cap B = \emptyset \implies P(A \cap B) = 0$). Khi đó: $P(A \cup B) = P(A) + P(B)$.

**3. Xác suất có điều kiện (Conditional Probability $P(A|B)$):**
Hãy đọc ký hiệu $P(A|B)$ là: **'Xác suất của biến cố $A$ khi ĐÃ BIẾT biến cố $B$ đã xảy ra'**.
- Khi biết $B$ đã xảy ra, thế giới thu nhỏ lại: Không gian mẫu không còn là toàn bộ $\Omega$ nữa, mà bị thu hẹp hoàn toàn về đúng tập $B$!
- Phần kết quả vừa thuộc $A$ vừa nằm trong thế giới mới $B$ chính là phần giao $A \cap B$.
- **Định nghĩa toán học:**
  $$P(A|B) = \frac{P(A \cap B)}{P(B)} \quad (\text{với } P(B) > 0)$$

*Ví dụ minh họa trực quan:* Gieo con xúc xắc 6 mặt ($\Omega = \{1, 2, 3, 4, 5, 6\}$).
- Gọi biến cố $A$: 'Được số lớn hơn hoặc bằng 4' $\implies A = \{4, 5, 6\} \implies P(A) = 3/6 = 0.5$.
- Bây giờ, người bạn che xúc xắc lại và tiết lộ thông tin biến cố $B$: 'Tao thấy nó là một số CHẴN rồi đấy!' $\implies B = \{2, 4, 6\}$.
- Hỏi xác suất số đó $\ge 4$ bây giờ là bao nhiêu ($P(A|B)$)?
  - Trong tập số chẵn $B = \{2, 4, 6\}$, chỉ có hai số $\{4, 6\}$ là thỏa mãn điều kiện $A$.
  - Vậy: $P(A|B) = \frac{|A \cap B|}{|B|} = \frac{2}{3} \approx 66.7\%$.
  - Thông tin mới $B$ đã đẩy xác suất từ $50\%$ vọt lên $66.7\%$!

**4. Quy tắc nhân xác suất và Khái niệm Độc Lập Thống Kê:**
- Từ công thức có điều kiện, ta suy ra quy tắc nhân xác suất tổng quát:
  $$P(A \cap B) = P(B) \cdot P(A|B) = P(A) \cdot P(B|A)$$
- **Hai biến cố Độc Lập (Independent) khi nào?**
  Khi việc biến cố $B$ xảy ra hoàn toàn không làm thay đổi xác suất xảy ra của $A$:
  $$P(A|B) = P(A) \iff P(A \cap B) = P(A) \cdot P(B)$$
  *Ví dụ:* Tung đồng xu lần 1 ra ngửa ($A$) và tung lần 2 ra sấp ($B$). Lần 1 không ảnh hưởng gì tới lần 2 $\implies$ Hai biến cố độc lập!

**5. Công thức Xác Suất Toàn Phần (Law of Total Probability):**
Nếu không gian mẫu được chia thành các mảnh ghép rời nhau $B_1, B_2, \dots, B_k$ (ví dụ: Thư rác và Thư thường), thì xác suất của một biến cố quan sát $A$ bất kỳ được tính bằng tổng các nhánh:
$$P(A) = \sum_{j=1}^k P(B_j) \cdot P(A|B_j)$$""",
                "formula": r"P(A|B) = \frac{P(A \cap B)}{P(B)} \quad \Longleftrightarrow \quad P(A \cap B) = P(B) \cdot P(A|B)",
                "mathExplainer": [
                    { "sym": r"P(A|B)", "name": "Xác suất có điều kiện", "mean": "Xác suất của biến cố A trong điều kiện biến cố B ĐÃ XẢY RA rồi (B là thông tin đã biết)." },
                    { "sym": r"P(A \cap B)", "name": "Xác suất đồng thời (Joint)", "mean": "Xác suất cả hai biến cố A và B cùng xảy ra đồng thời." },
                    { "sym": r"P(A \cup B)", "name": "Xác suất hợp (Union)", "mean": "Xác suất có ít nhất một trong hai biến cố A hoặc B xảy ra: P(A) + P(B) - P(A ∩ B)." },
                    { "sym": r"P(A \cap B) = P(A)P(B)", "name": "Điều kiện độc lập", "mean": "Hai biến cố độc lập nếu và chỉ nếu xác suất xảy ra đồng thời bằng tích hai xác suất riêng rẽ." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Outer space Omega -->
                      <rect x="25" y="20" width="260" height="140" fill="#fff" stroke="#888" stroke-dasharray="3,3"/>
                      <text x="35" y="38" font-family="Georgia" font-size="11" fill="#666">Không gian mẫu toàn cục Ω</text>
                      <!-- Set B (known evidence) -->
                      <ellipse cx="170" cy="95" rx="90" ry="50" fill="#eee" stroke="#111" stroke-width="1.5"/>
                      <text x="235" y="80" font-family="Georgia" font-size="11" font-weight="bold">Tập B</text>
                      <!-- Set A -->
                      <ellipse cx="110" cy="95" rx="65" ry="45" fill="none" stroke="#666" stroke-width="1.5"/>
                      <text x="65" y="80" font-family="Georgia" font-size="11">Tập A</text>
                      <!-- Intersection A and B -->
                      <path d="M 125 55 A 65 45 0 0 1 155 95 A 65 45 0 0 1 125 135 A 90 50 0 0 1 105 95 A 90 50 0 0 1 125 55" fill="#111"/>
                      <text x="130" y="100" font-family="Georgia" font-size="10" fill="#fff" text-anchor="middle" font-weight="bold">A ∩ B</text>

                      <!-- Explanatory formula panel -->
                      <g transform="translate(310, 30)">
                        <text x="0" y="20" font-family="Georgia" font-size="13" font-weight="bold">Bản chất của P(A|B):</text>
                        <text x="0" y="45" font-family="Georgia" font-size="11">• Khi biết B đã xảy ra, không gian mẫu bị thu hẹp:</text>
                        <text x="15" y="65" font-family="Georgia" font-size="12" font-style="italic">Toàn bộ thế giới mới bây giờ chính là hình elip B!</text>
                        <text x="0" y="92" font-family="Georgia" font-size="11">• Xác suất của A trong thế giới mới B là tỉ lệ:</text>
                        <text x="15" y="115" font-family="Georgia" font-size="13" font-weight="bold">P(A|B) = Diện tích (A ∩ B) / Diện tích B</text>
                        <text x="0" y="138" font-family="Georgia" font-size="10" fill="#555">Nếu A và B độc lập: P(A|B) = P(A), diện tích tương đối không đổi.</text>
                      </g>
                    </svg>""",
                    "caption": "Trực quan hóa Xác suất có điều kiện: Khi B đã xảy ra, không gian mẫu thu hẹp từ toàn bộ không gian Ω về đúng tập B."
                },
                "commonPitfalls": "Cạm bẫy 'Ngụy biện công tố viên' (Prosecutor's Fallacy): Tuyệt đối không nhầm lẫn giữa $P(A|B)$ và $P(B|A)$! Ví dụ: Xác suất một người có râu khi người đó là Đàn ông $P(\\text{Có râu}|\\text{Nam})$ là khoảng $30\\%$. Nhưng xác suất một người là Nam khi biết người đó Có râu $P(\\text{Nam}|\\text{Có râu})$ là xấp xỉ $100\\%$! Hai giá trị này hoàn toàn khác nhau!",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Trong một lớp học sinh có 60% học sinh thích môn Toán, 40% học sinh thích môn Tin học, và 30% học sinh thích CẢ HAI môn Toán và Tin học. Chọn ngẫu nhiên một học sinh trong lớp, biết rằng bạn này thích môn Toán. Xác suất bạn này CŨNG thích môn Tin học là bao nhiêu?",
                    "options": [
                        "A. 0.30 (30%)",
                        "B. 0.50 (50%)",
                        "C. 0.75 (75%)",
                        "D. 0.20 (20%)"
                    ],
                    "correctIndex": 1,
                    "hint": "Xác định biến cố đã biết: 'Bạn này thích môn Toán' là điều kiện B. Biến cố cần tính: 'Thích môn Tin' là A. Dùng công thức P(Tin|Toán) = P(Toán ∩ Tin) / P(Toán).",
                    "solution": [
                        "Bước 1: Gọi các biến cố và tóm tắt đề bài:",
                        "  - Biến cố T: Học sinh thích Toán => P(T) = 0.60.",
                        "  - Biến cố C: Học sinh thích Tin => P(C) = 0.40.",
                        "  - Biến cố giao (thích cả hai môn): P(T ∩ C) = 0.30.",
                        "Bước 2: Đề bài yêu cầu: Biết học sinh thích Toán (T đã xảy ra), tính xác suất thích Tin (C):",
                        "  - Áp dụng công thức xác suất có điều kiện:",
                        "    P(C|T) = P(T ∩ C) / P(T) = 0.30 / 0.60 = 1/2 = 0.50 (50%).",
                        "Kết luận: Có 50% khả năng bạn học sinh đó thích môn Tin học. Đáp án đúng là B."
                    ]
                }
            },

            # =================================================================
            # MỤC 3.2: ĐỊNH LÝ BAYES - NGHỆ THUẬT CẬP NHẬT NIỀM TIN
            # =================================================================
            {
                "heading": "3.2. Định Lý Bayes (Bayes' Theorem): Nghệ Thuật Cập Nhật Niềm Tin Trong Trí Tuệ Nhân Tạo",
                "content": "Làm thế nào một cỗ máy có thể 'thay đổi quan điểm' khi tiếp nhận thêm chứng cứ mới? Định lý Bayes chính là công thức toán học vĩ đại nhất để mô tả quá trình tư duy suy luận logic của con người và máy móc.",
                "deepDive": r"""**1. Chứng minh toán học chỉ trong đúng 2 dòng:**
Từ quy tắc nhân xác suất ở Mục 3.1, ta có hai cách biểu diễn xác suất đồng thời của hai biến cố $X$ và $Y$:
$$P(X \cap Y) = P(Y) \cdot P(X|Y)$$
$$P(X \cap Y) = P(X) \cdot P(Y|X)$$

Vì vế trái bằng nhau, hai vế phải bắt buộc phải bằng nhau:
$$P(X) \cdot P(Y|X) = P(Y) \cdot P(X|Y)$$

Chia cả hai vế cho $P(X)$ (với điều kiện $P(X) > 0$), ta thu được **Định Lý Bayes**:
$$P(Y|X) = \frac{P(X|Y) \cdot P(Y)}{P(X)}$$

---

**2. Mổ xẻ 4 thành phần vàng của Định lý Bayes (Bắt buộc phải thuộc làu):**

| Thành phần | Tên gọi chuẩn mực | Ý nghĩa bản chất trong Học Máy |
| :--- | :--- | :--- |
| **$P(Y|X)$** | **Posterior** *(Xác suất hậu nghiệm)* | Xác suất nhãn $Y$ là đúng **SAU KHI** đã quan sát thấy dữ liệu/triệu chứng $X$. Đây là **mục tiêu cuối cùng mô hình cần dự đoán**. |
| **$P(Y)$** | **Prior** *(Xác suất tiên nghiệm)* | Niềm tin ban đầu về nhãn $Y$ **TRƯỚC KHI** nhìn thấy bất kỳ dữ liệu nào. Được tính bằng tỷ lệ phần trăm mẫu của nhãn $Y$ trong tập huấn luyện. |
| **$P(X|Y)$** | **Likelihood** *(Hàm hợp lý)* | Khả năng xuất hiện dữ liệu $X$ nếu giả thuyết $Y$ thực sự là đúng. Đong đếm xem nhãn $Y$ ủng hộ bằng chứng $X$ mạnh mẽ đến đâu. |
| **$P(X)$** | **Evidence** *(Bằng chứng biên)* | Tổng xác suất xuất hiện dữ liệu $X$ trên toàn bộ thế giới: $P(X) = \sum_y P(Y=y) P(X|Y=y)$. Đóng vai trò là hằng số chuẩn hóa để tổng các Posterior cộng lại bằng đúng 1. |

---

**3. Bài toán Y tế kinh điển: Nghịch lý tại sao xét nghiệm chính xác 99% mà xác suất có bệnh chỉ có 9%?**

*Bài toán:* Một căn bệnh hiếm gặp trong xã hội có tỷ lệ mắc bệnh là $1/1000$ người ($P(\text{Bệnh}) = 0.001$).
Có một que thử nghiệm cực kỳ hiện đại với độ chính xác:
- Nếu người thực sự có bệnh, que thử báo Dương tính 99% ($P(\text{Dương}|\text{Bệnh}) = 0.99$).
- Nếu người hoàn toàn khỏe mạnh, que thử báo nhầm Dương tính giả chỉ 1% ($P(\text{Dương}|\text{Khỏe}) = 0.01$).

Một người dân ngẫu nhiên đi xét nghiệm và nhận kết quả: **DƯƠNG TÍNH**. Hỏi xác suất người này thực sự mắc bệnh ($P(\text{Bệnh}|\text{Dương})$) là bao nhiêu?
*Phần lớn mọi người đoán là 99%. Nhưng hãy giải bằng Định lý Bayes:*

- **Bước 1: Tính tử số (Khả năng thực sự có bệnh):**
  $$\text{Tử số} = P(\text{Bệnh}) \cdot P(\text{Dương}|\text{Bệnh}) = 0.001 \times 0.99 = 0.00099$$
- **Bước 2: Tính mẫu số $P(\text{Dương})$ bằng công thức xác suất toàn phần:**
  Một người nhận kết quả dương tính có thể đến từ 2 trường hợp: Thực sự có bệnh HOẶC Bị dương tính giả do que thử nhầm!
  $$P(\text{Dương}) = P(\text{Bệnh}) P(\text{Dương}|\text{Bệnh}) + P(\text{Khỏe}) P(\text{Dương}|\text{Khỏe})$$
  $$P(\text{Dương}) = (0.001 \times 0.99) + (0.999 \times 0.01) = 0.00099 + 0.00999 = 0.01098$$
- **Bước 3: Tính xác suất hậu nghiệm Posterior:**
  $$P(\text{Bệnh}|\text{Dương}) = \frac{0.00099}{0.01098} \approx 0.09016 \implies \mathbf{9.02\%}!$$

*Bản chất trực giác sâu sắc:* Vì bệnh quá hiếm (chỉ 1/1000 người), số lượng người khỏe mạnh áp đảo hoàn toàn (999 người). Do đó, số lượng người khỏe bị dương tính giả (khoảng 10 người) vẫn nhiều gấp 10 lần số người thực sự mắc bệnh (1 người)!
Nhờ Bayes, bác sĩ sẽ không vội hoảng loạn kê thuốc độc hại mà sẽ yêu cầu bệnh nhân xét nghiệm lần thứ hai!

---

**4. Nguyên lý Quyết định MAP (Maximum A Posteriori):**
Trong bài toán phân loại, ta cần so sánh giữa các nhãn $y \in \{C_1, C_2, \dots, C_K\}$.
Do mẫu số $P(X)$ là **HOÀN TOÀN GIỐNG NHAU** đối với tất cả các nhãn, ta có thể bỏ qua mẫu số và đưa ra nhãn dự đoán $\hat{y}$ bằng cách chỉ cần tối đa hóa tử số:
$$\hat{y} = \arg\max_{y} \left[ P(y) \cdot P(X|y) \right]$$""",
                "formula": r"P(Y|X) = \frac{P(X|Y) \cdot P(Y)}{P(X)} = \frac{P(X|Y) \cdot P(Y)}{\sum_{y'} P(X|y') P(y')}",
                "mathExplainer": [
                    { "sym": r"P(Y|X) (Posterior)", "name": "Xác suất hậu nghiệm", "mean": "Mục tiêu dự đoán của AI: Xác suất đối tượng thuộc nhãn Y sau khi biết tập đặc trưng X." },
                    { "sym": r"P(Y) (Prior)", "name": "Xác suất tiên nghiệm", "mean": "Tỷ lệ xuất hiện tự nhiên của nhãn Y trong lịch sử (tần suất xuất hiện của nhãn)." },
                    { "sym": r"P(X|Y) (Likelihood)", "name": "Hàm hợp lý Likelihood", "mean": "Mức độ phù hợp của dữ liệu quan sát X dưới giả thuyết nhãn Y." },
                    { "sym": r"\\arg\\max_y", "name": "Giá trị cực đại hóa", "mean": "Chọn nhãn y mang lại giá trị tích xác suất lớn nhất trong số các nhãn có thể." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 190" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="190" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Step 1 Prior -->
                      <g transform="translate(30, 25)">
                        <rect x="0" y="20" width="110" height="70" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="55" y="45" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">PRIOR P(Y)</text>
                        <text x="55" y="65" font-family="Georgia" font-size="10" text-anchor="middle">Niềm tin ban đầu</text>
                        <text x="55" y="80" font-family="Georgia" font-size="9" fill="#666" text-anchor="middle">(Tỷ lệ mẫu cũ)</text>
                      </g>

                      <!-- Multiplier icon -->
                      <text x="160" y="65" font-family="Georgia" font-size="20" font-weight="bold" text-anchor="middle">×</text>

                      <!-- Step 2 Likelihood -->
                      <g transform="translate(185, 25)">
                        <rect x="0" y="20" width="130" height="70" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="65" y="45" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">LIKELIHOOD P(X|Y)</text>
                        <text x="65" y="65" font-family="Georgia" font-size="10" text-anchor="middle">Chứng cứ thực tế</text>
                        <text x="65" y="80" font-family="Georgia" font-size="9" fill="#666" text-anchor="middle">(Độ hợp lý triệu chứng)</text>
                      </g>

                      <!-- Equals icon -->
                      <text x="335" y="65" font-family="Georgia" font-size="20" font-weight="bold" text-anchor="middle">∝</text>

                      <!-- Step 3 Posterior -->
                      <g transform="translate(360, 20)">
                        <rect x="0" y="15" width="130" height="80" fill="#111"/>
                        <text x="65" y="42" font-family="Georgia" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">POSTERIOR</text>
                        <text x="65" y="60" font-family="Georgia" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">P(Y|X)</text>
                        <text x="65" y="80" font-family="Georgia" font-size="10" fill="#eee" text-anchor="middle">Niềm tin cập nhật</text>
                      </g>

                      <!-- Normalized note below -->
                      <g transform="translate(505, 30)">
                        <line x1="0" y1="50" x2="90" y2="50" stroke="#888"/>
                        <text x="45" y="40" font-family="Georgia" font-size="10" text-anchor="middle">Chia cho P(X)</text>
                        <text x="45" y="70" font-family="Georgia" font-size="10" fill="#555" text-anchor="middle">(Hằng số chuẩn hóa)</text>
                      </g>

                      <!-- Bottom description -->
                      <text x="310" y="145" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Quy tắc vàng: Posterior tỷ lệ thuận với [ Prior × Likelihood ]</text>
                      <text x="310" y="165" font-family="Georgia" font-size="10" fill="#555" text-anchor="middle">Trong phân loại: So sánh các nhãn Y chỉ cần so sánh tử số này, không cần chia cho P(X)!</text>
                    </svg>""",
                    "caption": "Luồng cập nhật niềm tin của Định lý Bayes: Niềm tin ban đầu nhân với Bằng chứng quan sát cho ra Niềm tin cập nhật."
                },
                "commonPitfalls": "Quên tính đầy đủ mẫu số $P(X)$ khi đề bài hỏi xác suất tuyệt đối: Nếu đề bài hỏi 'Tính xác suất phần trăm bệnh nhân mắc bệnh', bạn bắt buộc phải chia cho mẫu số $P(X) = P(Bệnh)P(Dương|Bệnh) + P(Khỏe)P(Dương|Khỏe)$. Nhưng nếu đề bài chỉ hỏi 'Dự đoán nhãn là Spam hay Ham', bạn chỉ cần so sánh tử số!",
                "practiceQuestion": {
                    "level": "Vận dụng",
                    "question": "Trong một nhà máy sản xuất chip AI, Máy A sản xuất 70% tổng số chip, Máy B sản xuất 30% còn lại. Tỷ lệ chip bị lỗi của Máy A là 2%, của Máy B là 5%. Một kỹ sư kiểm tra ngẫu nhiên thấy một con chip bị lỗi. Hỏi xác suất con chip bị lỗi này do Máy B sản xuất là bao nhiêu?",
                    "options": [
                        "A. 15 / 29 (khoảng 51.72%)",
                        "B. 14 / 29 (khoảng 48.28%)",
                        "C. 0.015 (khoảng 1.5%)",
                        "D. 0.050 (khoảng 5.0%)"
                    ],
                    "correctIndex": 0,
                    "hint": "Dùng định lý Bayes: P(B|Lỗi) = [P(B) × P(Lỗi|B)] / P(Lỗi). Trong đó P(Lỗi) = P(A)P(Lỗi|A) + P(B)P(Lỗi|B).",
                    "solution": [
                        "Bước 1: Liệt kê các đại lượng xác suất:",
                        "  - Prior: P(A) = 0.70; P(B) = 0.30.",
                        "  - Likelihood lỗi: P(Lỗi|A) = 0.02; P(Lỗi|B) = 0.05.",
                        "Bước 2: Tính mẫu số P(Lỗi) bằng công thức xác suất toàn phần:",
                        "  P(Lỗi) = P(A) × P(Lỗi|A) + P(B) × P(Lỗi|B)",
                        "  P(Lỗi) = (0.70 × 0.02) + (0.30 × 0.05) = 0.014 + 0.015 = 0.029.",
                        "Bước 3: Tính Posterior P(B|Lỗi):",
                        "  P(B|Lỗi) = [P(B) × P(Lỗi|B)] / P(Lỗi) = 0.015 / 0.029 = 15 / 29 ≈ 51.72%.",
                        "Kết luận: Dù Máy B chỉ sản xuất 30% chip, nhưng do tỷ lệ lỗi cao hơn nên khi phát hiện chip lỗi, khả năng nó đến từ Máy B lên tới hơn 51.72%! Đáp án đúng là A."
                    ]
                }
            },

            # =================================================================
            # MỤC 3.3: GIẢ ĐỊNH ĐỘC LẬP NGÂY THƠ
            # =================================================================
            {
                "heading": "3.3. Bộ Phân Loại Naive Bayes & Cú Đột Phá Của Giả Định Độc Lập 'Ngây Thơ'",
                "content": "Một câu văn hay một văn bản không chỉ có 1 từ mà có hàng trăm, hàng nghìn từ. Làm thế nào áp dụng định lý Bayes cho một chuỗi dữ liệu phức tạp mà không bị nổ tung bộ nhớ máy tính? Đó chính là lúc sự 'Ngây thơ' (Naive) phát huy sức mạnh kỳ diệu.",
                "deepDive": r"""**1. Bế tắc của định lý Bayes cổ điển trên dữ liệu nhiều chiều:**
Giả sử ta muốn phân loại một email $X$ gồm $d$ từ ngữ: $X = (x_1, x_2, \dots, x_d)$ vào nhãn $Y \in \{\text{Spam}, \text{Ham}\}$.
Theo định lý Bayes, tử số cần tính là:
$$P(Y) \cdot P(X|Y) = P(Y) \cdot P(x_1, x_2, \dots, x_d | Y)$$

Để tính xác suất đồng thời $P(x_1, x_2, \dots, x_d | Y)$ một cách chính xác tuyệt đối, ta phải áp dụng quy tắc chuỗi xác suất:
$$P(x_1, x_2, \dots, x_d | Y) = P(x_1|Y) \cdot P(x_2 | x_1, Y) \cdot P(x_3 | x_1, x_2, Y) \dots P(x_d | x_1, x_2, \dots, x_{d-1}, Y)$$

- **Sự bế tắc chí mạng:**
  - Để tính $P(x_d | x_1, \dots, x_{d-1}, Y)$, ta cần đếm tần suất một chuỗi $d$ từ xuất hiện cùng nhau trong dữ liệu huấn luyện.
  - Nếu từ vựng có kích thước $|V| = 10,000$ từ và văn bản chỉ dài $d = 20$ từ, số trường hợp tổ hợp có thể xảy ra là $|V|^d = 10000^{20} = 10^{80}$ (nhiều hơn toàn bộ số hạt nguyên tử trong vũ trụ!).
  - Hầu như không có chuỗi văn bản nào lặp lại y hệt trong thực tế $\implies$ Xác suất sẽ bị bằng 0 ở khắp mọi nơi!

---

**2. Giả định độc lập 'ngây thơ' (Conditional Independence Assumption):**
Các nhà khoa học máy tính đã đưa ra một giả định cực kỳ táo bạo:
**'Khi ĐÃ BIẾT đối tượng thuộc nhãn $Y$, ta giả định tất cả các đặc trưng $x_1, x_2, \dots, x_d$ hoàn toàn độc lập với nhau!'**

Nhờ giả định này, xác suất đồng thời phức tạp của cả một đoạn văn dài lập tức biến thành **TÍCH CỦA CÁC XÁC SUẤT ĐƠN TỪ ĐỘC LẬP**:
$$P(x_1, x_2, \dots, x_d | Y) = \prod_{i=1}^d P(x_i | Y) = P(x_1|Y) \cdot P(x_2|Y) \cdot P(x_3|Y) \dots P(x_d|Y)$$

---

**3. Tại sao gọi là 'Ngây thơ' (Naive)?**
- Giả định này được gọi là 'ngây thơ' (ngây ngô) vì trong thực tế, các từ ngữ trong ngôn ngữ con người **KHÔNG HỀ ĐỘC LẬP**!
  - Từ 'Hà' xuất hiện thì từ tiếp theo gần như chắc chắn là 'Nội'.
  - Từ 'trúng' xuất hiện thì rất có khả năng từ 'thưởng' đi kèm.
  - Naive Bayes hoàn toàn phớt lờ ngữ pháp, thứ tự từ, và ngữ cảnh cú pháp. Nó xem văn bản như một 'Túi đựng từ' (Bag of Words) bị xáo trộn lung tung!

**4. Nhưng tại sao 'Ngây thơ' mà Naive Bayes vẫn hoạt động cực kỳ xuất sắc?**
1. **Mục đích là Phân loại, không phải ước lượng xác suất:** Để phân loại đúng nhãn, mô hình chỉ cần tính xem nhãn nào có điểm số LỚN HƠN, chứ không cần biết con số xác suất tuyệt đối chính xác đến từng chữ số thập phân. Dù các xác suất bị phóng đại hay thu nhỏ do bỏ qua tương quan, thứ tự xếp hạng giữa các nhãn hầu như không bị đảo lộn!
2. **Không bị Quá khớp (Overfitting):** Vì không cố gắng ghi nhớ các mối liên hệ phức tạp giữa các cụm từ, Naive Bayes cực kỳ kiên cường khi tập dữ liệu huấn luyện có kích thước nhỏ.
3. **Tốc độ tính toán ánh sáng:** Huấn luyện Naive Bayes chỉ đơn giản là một phép đếm tần suất trên bảng dữ liệu, không cần chạy đạo hàm hay lan truyền ngược tốn kém như Deep Learning!""",
                "formula": r"P(x_1, x_2, \dots, x_d | Y) \stackrel{\text{Naive}}{=} \prod_{i=1}^d P(x_i | Y) \implies \hat{y} = \arg\max_{y} \left[ P(y) \prod_{i=1}^d P(x_i | y) \right]",
                "mathExplainer": [
                    { "sym": r"\\prod_{i=1}^d", "name": "Ký hiệu tích dồn", "mean": "Nhân liên tiếp các giá trị từ i = 1 đến d: P(x₁) · P(x₂) · ... · P(x_d)." },
                    { "sym": r"Conditional Independence", "name": "Độc lập có điều kiện", "mean": "P(x_i, x_j | Y) = P(x_i | Y) · P(x_j | Y). Các đặc trưng độc lập với nhau KHI ĐÃ BIẾT nhãn Y." },
                    { "sym": r"Bag of Words (BoW)", "name": "Mô hình túi từ", "mean": "Giả định coi văn bản như một tập hợp các từ độc lập, bỏ qua hoàn toàn thứ tự ngữ pháp." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Central Class Node -->
                      <g transform="translate(310, 35)">
                        <circle cx="0" cy="0" r="26" fill="#111"/>
                        <text x="0" y="5" font-family="Georgia" font-size="13" font-weight="bold" fill="#fff" text-anchor="middle">Nhãn Y</text>
                      </g>

                      <!-- Feature Nodes -->
                      <!-- Node x1 -->
                      <g transform="translate(80, 130)">
                        <circle cx="0" cy="0" r="22" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="0" y="4" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Từ x₁</text>
                      </g>
                      <!-- Node x2 -->
                      <g transform="translate(195, 130)">
                        <circle cx="0" cy="0" r="22" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="0" y="4" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Từ x₂</text>
                      </g>
                      <!-- Node x3 -->
                      <g transform="translate(310, 130)">
                        <circle cx="0" cy="0" r="22" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="0" y="4" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Từ x₃</text>
                      </g>
                      <!-- Node x4 -->
                      <g transform="translate(425, 130)">
                        <circle cx="0" cy="0" r="22" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="0" y="4" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Từ x₄</text>
                      </g>
                      <!-- Node xd -->
                      <g transform="translate(540, 130)">
                        <circle cx="0" cy="0" r="22" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="0" y="4" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Từ x_d</text>
                      </g>

                      <!-- Directed Edges -->
                      <line x1="290" y1="50" x2="100" y2="115" stroke="#111" stroke-width="1.5"/>
                      <polygon points="100,115 110,110 106,120" fill="#111"/>

                      <line x1="298" y1="58" x2="210" y2="112" stroke="#111" stroke-width="1.5"/>
                      <polygon points="210,112 220,108 217,118" fill="#111"/>

                      <line x1="310" y1="61" x2="310" y2="108" stroke="#111" stroke-width="1.5"/>
                      <polygon points="310,108 306,98 314,98" fill="#111"/>

                      <line x1="322" y1="58" x2="410" y2="112" stroke="#111" stroke-width="1.5"/>
                      <polygon points="410,112 403,118 400,108" fill="#111"/>

                      <line x1="330" y1="50" x2="520" y2="115" stroke="#111" stroke-width="1.5"/>
                      <polygon points="520,115 514,120 510,110" fill="#111"/>

                      <!-- Text label -->
                      <text x="310" y="170" font-family="Georgia" font-size="10" fill="#444" text-anchor="middle">Mô hình đồ thị có hướng: Khi biết Nhãn Y, không có bất kỳ mũi tên nào nối giữa các từ xᵢ với nhau!</text>
                    </svg>""",
                    "caption": "Mô hình đồ thị xác suất Naive Bayes: Nhãn Y là cha độc lập sinh ra từng đặc trưng x_i. Không có liên kết qua lại giữa các x_i."
                },
                "commonPitfalls": "Nhầm lẫn giữa Độc lập biên (Marginal Independence) và Độc lập có điều kiện (Conditional Independence): Trong Naive Bayes, các từ $x_1$ và $x_2$ KHÔNG độc lập với nhau trong đời sống bình thường. Chúng chỉ được giả định độc lập KHI VÀ CHỈ KHI nhãn $Y$ đã được cố định!",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Giả sử một văn bản chứa 3 từ đặc trưng x₁, x₂, x₃. Theo giả định độc lập có điều kiện của Naive Bayes, công thức tính xác suất xuất hiện của cả 3 từ này khi biết nhãn là Spam P(x₁, x₂, x₃ | Spam) bằng biểu thức nào sau đây?",
                    "options": [
                        "A. P(x₁|Spam) + P(x₂|Spam) + P(x₃|Spam)",
                        "B. P(x₁|Spam) × P(x₂|Spam) × P(x₃|Spam)",
                        "C. P(Spam) × P(x₁|Spam) × P(x₂|x₁)",
                        "D. [P(x₁|Spam) × P(x₂|Spam) × P(x₃|Spam)] / P(Spam)"
                    ],
                    "correctIndex": 1,
                    "hint": "Giả định Naive biến xác suất đồng thời thành TÍCH của các xác suất thành phần riêng lẻ có điều kiện theo Spam.",
                    "solution": [
                        "Bước 1: Áp dụng trực tiếp định nghĩa giả định độc lập có điều kiện của Naive Bayes:",
                        "  P(x₁, x₂, x₃ | Y) = P(x₁|Y) × P(x₂|Y) × P(x₃|Y).",
                        "Bước 2: Thay nhãn Y = Spam:",
                        "  P(x₁, x₂, x₃ | Spam) = P(x₁|Spam) × P(x₂|Spam) × P(x₃|Spam).",
                        "Kết luận: Đáp án chính xác là B."
                    ]
                }
            },

            # =================================================================
            # MỤC 3.4: 3 BIẾN THỂ NAIVE BAYES
            # =================================================================
            {
                "heading": "3.4. Ba Biến Thể Naive Bayes Cốt Lõi: Bernoulli, Multinomial & Gaussian",
                "content": "Dữ liệu trong thế giới thực vô cùng đa dạng: Có lúc là từ ngữ văn bản, có lúc là số đếm tần suất, có lúc là các con số thực đo lường liên tục (huyết áp, nhiệt độ). Để xử lý từng dạng dữ liệu, Naive Bayes phân nhánh thành 3 biến thể chuyên biệt.",
                "deepDive": r"""**1. Bernoulli Naive Bayes (Dành cho đặc trưng Nhị phân 0 / 1):**
- **Đặc điểm dữ liệu:** Mỗi đặc trưng $x_i \in \{0, 1\}$ chỉ cho biết thuộc tính đó **CÓ XUẤT HIỆN HAY KHÔNG**, hoàn toàn không quan tâm xuất hiện bao nhiêu lần.
  - Ví dụ: Trong email, $x_{\text{bitcoin}} = 1$ (có từ bitcoin), $x_{\text{khuyến mãi}} = 0$ (không có).
- **Mô hình xác suất:** Tuân theo phân phối Bernoulli:
  $$P(x_i | Y) = p_{yi}^{x_i} (1 - p_{yi})^{1 - x_i}$$
  - Nếu $x_i = 1$: $P(x_i=1|Y) = p_{yi}$ (xác suất xuất hiện).
  - Nếu $x_i = 0$: $P(x_i=0|Y) = 1 - p_{yi}$ (xác suất KHÔNG xuất hiện).
- **Điểm đặc biệt cần lưu ý:** Bernoulli Naive Bayes tính toán cả sự **VẮNG MẶT** của từ ngữ! Một từ không xuất hiện cũng là bằng chứng quan trọng để suy đoán.
- **Ứng dụng:** Phân loại văn bản rất ngắn (tin nhắn SMS, bình luận Twitter/X).

---

**2. Multinomial Naive Bayes (Tiêu chuẩn vàng cho Xử lý Ngôn ngữ Tự nhiên - NLP):**
- **Đặc điểm dữ liệu:** Mỗi đặc trưng $x_i \in \{0, 1, 2, 3, \dots\}$ là **TẦN SUẤT SỐ LẦN XUẤT HIỆN** của từ $w_i$ trong văn bản (Mô hình Bag-of-Words).
  - Một email chứa từ 'khuyến mãi' 5 lần sẽ có trọng lượng cảnh báo mạnh hơn nhiều so với email chỉ chứa từ đó 1 lần.
- **Mô hình xác suất:** Tuân theo phân phối Đa thức (Multinomial Distribution):
  $$P(X | Y) = \frac{(\sum_{i=1}^d x_i)!}{\prod_{i=1}^d x_i!} \prod_{i=1}^d P(w_i | Y)^{x_i}$$
- Khi phân loại, phần giai thừa là hằng số với mọi nhãn, nên ta chỉ cần tính tích có lũy thừa số mũ:
  $$\hat{y} = \arg\max_y \left[ P(y) \prod_{i=1}^d P(w_i | y)^{x_i} \right]$$
- **Ứng dụng:** Phân loại tài liệu, lọc thư rác, phân tích sắc thái cảm xúc (Sentiment Analysis: Khen vs Chê).

---

**3. Gaussian Naive Bayes (Dành cho dữ liệu Số thực liên tục $\mathbb{R}$):**
- **Đặc điểm dữ liệu:** Các đặc trưng là các số đo lường liên tục $x_i \in \mathbb{R}$ (Ví dụ: Chiều cao, Cân nặng, Huyết áp, Nồng độ đường trong máu, Nhiệt độ môi trường).
  - Ta không thể đếm số lần xuất hiện của số thực (ví dụ nhiệt độ $37.245^\circ\text{C}$ có thể chỉ xuất hiện đúng 1 lần duy nhất trong toàn bộ tập dữ liệu!).
- **Mô hình xác suất:** Giả định rằng trong mỗi lớp $Y$, đặc trưng $x_i$ tuân theo **Phân Phối Chuẩn (Phân phối hình chuông Gauss)** với giá trị trung bình $\mu_{yi}$ và phương sai $\sigma_{yi}^2$:
  $$P(x_i | Y) = \frac{1}{\sqrt{2\pi \sigma_{yi}^2}} \exp \left( - \frac{(x_i - \mu_{yi})^2}{2\sigma_{yi}^2} \right)$$
- **Cách huấn luyện:**
  1. Với mỗi lớp $y$, tính trung bình mẫu $\mu_{yi} = \frac{1}{N_y} \sum_{k=1}^{N_y} x_{ik}$.
  2. Tính phương sai mẫu $\sigma_{yi}^2 = \frac{1}{N_y} \sum_{k=1}^{N_y} (x_{ik} - \mu_{yi})^2$.
  3. Khi có mẫu mới $x_i^*$, thay trực tiếp vào hàm mật độ xác suất Gauss ở trên!
- **Ứng dụng:** Chẩn đoán y khoa, nhận dạng chữ số viết tay MNIST (độ xám pixel từ 0 đến 255), phân loại loài hoa Iris.

---

**Bảng so sánh đối đầu 3 biến thể:**

| Tiêu chí | Bernoulli Naive Bayes | Multinomial Naive Bayes | Gaussian Naive Bayes |
| :--- | :--- | :--- | :--- |
| **Kiểu dữ liệu đầu vào** | Nhị phân $x_i \in \{0, 1\}$ | Số đếm tần suất $x_i \in \mathbb{N}$ | Số thực liên tục $x_i \in \mathbb{R}$ |
| **Ý nghĩa đặc trưng** | Từ có mặt hay vắng mặt | Số lần từ xuất hiện trong bài | Giá trị đo lường liên tục |
| **Xử lý sự vắng mặt** | CÓ (nhân cả $1 - p$) | KHÔNG (chỉ tính từ có mặt) | Không áp dụng |
| **Bài toán tiêu biểu** | Phân loại tin nhắn SMS ngắn | Phân loại văn bản dài, email | Chẩn đoán y khoa, cảm biến IoT |""",
                "formula": r"\text{Gaussian: } P(x_i|Y) = \frac{1}{\sqrt{2\pi\sigma_{yi}^2}} e^{-\frac{(x_i-\mu_{yi})^2}{2\sigma_{yi}^2}} \quad \text{vs} \quad \text{Multinomial: } P(X|Y) \propto \prod_{i=1}^d P(w_i|Y)^{x_i}",
                "mathExplainer": [
                    { "sym": r"\\mu_{yi}", "name": "Giá trị trung bình lớp y", "mean": "Điểm tâm trung tâm của phân phối chuẩn Gaussian đối với đặc trưng i trong lớp y." },
                    { "sym": r"\\sigma_{yi}^2", "name": "Phương sai của lớp y", "mean": "Độ phân tán, đo độ dàn trải của dữ liệu đặc trưng i quanh giá trị trung bình." },
                    { "sym": r"x_i \\in \\{0, 1\\}", "name": "Đặc trưng nhị phân", "mean": "Dạng dữ liệu 0/1 của mô hình Bernoulli, chỉ ra sự xuất hiện hoặc không xuất hiện." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Bernoulli Panel -->
                      <g transform="translate(25, 20)">
                        <rect x="0" y="0" width="170" height="140" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="85" y="25" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Bernoulli NB</text>
                        <text x="85" y="42" font-family="Georgia" font-size="10" fill="#666" text-anchor="middle">Dữ liệu Nhị phân {0, 1}</text>
                        <!-- Binary bars -->
                        <rect x="35" y="60" width="30" height="55" fill="#111"/>
                        <text x="50" y="130" font-family="Georgia" font-size="10" text-anchor="middle">Có (1)</text>
                        <rect x="105" y="85" width="30" height="30" fill="#bbb"/>
                        <text x="120" y="130" font-family="Georgia" font-size="10" text-anchor="middle">Không (0)</text>
                      </g>

                      <!-- Multinomial Panel -->
                      <g transform="translate(225, 20)">
                        <rect x="0" y="0" width="170" height="140" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="85" y="25" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Multinomial NB</text>
                        <text x="85" y="42" font-family="Georgia" font-size="10" fill="#666" text-anchor="middle">Số đếm tần suất {0, 1, 2...}</text>
                        <!-- Histogram bars -->
                        <rect x="25" y="70" width="20" height="45" fill="#555"/>
                        <rect x="55" y="55" width="20" height="60" fill="#111"/>
                        <rect x="85" y="85" width="20" height="30" fill="#888"/>
                        <rect x="115" y="65" width="20" height="50" fill="#333"/>
                        <text x="85" y="130" font-family="Georgia" font-size="10" text-anchor="middle">Đếm từ (Bag-of-Words)</text>
                      </g>

                      <!-- Gaussian Panel -->
                      <g transform="translate(425, 20)">
                        <rect x="0" y="0" width="170" height="140" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="85" y="25" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Gaussian NB</text>
                        <text x="85" y="42" font-family="Georgia" font-size="10" fill="#666" text-anchor="middle">Số thực liên tục x ∈ ℝ</text>
                        <!-- Bell curve -->
                        <path d="M 20 115 Q 60 115 75 80 Q 85 45 95 80 Q 110 115 150 115" fill="none" stroke="#111" stroke-width="2"/>
                        <line x1="85" y1="45" x2="85" y2="115" stroke="#888" stroke-dasharray="2,2"/>
                        <text x="85" y="130" font-family="Georgia" font-size="10" text-anchor="middle">Phân phối chuẩn (μ, σ²)</text>
                      </g>
                    </svg>""",
                    "caption": "Ba biến thể Naive Bayes thích ứng với 3 kiểu dữ liệu: Nhị phân (Bernoulli), Tần suất đếm (Multinomial), và Số thực liên tục (Gaussian)."
                },
                "commonPitfalls": "Chọn sai biến thể Naive Bayes: Trong đề thi thực tế, nếu bài toán yêu cầu phân loại bệnh nhân theo các chỉ số xét nghiệm huyết áp (ví dụ 120.5 mmHg), đường huyết (5.4 mmol/L) mà học sinh lại chọn Multinomial Naive Bayes là sai hoàn toàn! Bắt buộc phải dùng Gaussian Naive Bayes cho dữ liệu liên tục.",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Một hệ thống AI được xây dựng để dự đoán bệnh Tiểu đường dựa trên 3 thông tin của bệnh nhân: (1) Chỉ số đường huyết đo lúc đói (mg/dL), (2) Chỉ số huyết áp tâm thu (mmHg), và (3) Độ tuổi (năm). Cả 3 đặc trưng này đều là các đại lượng số thực đo lường liên tục. Biến thể Naive Bayes nào là sự lựa chọn phù hợp nhất?",
                    "options": [
                        "A. Multinomial Naive Bayes",
                        "B. Bernoulli Naive Bayes",
                        "C. Gaussian Naive Bayes",
                        "D. Categorical Naive Bayes"
                    ],
                    "correctIndex": 2,
                    "hint": "Dữ liệu là các số thực đo lường liên tục (huyết áp, đường huyết), phù hợp với mô hình phân phối chuẩn đường cong chuông Gaussian.",
                    "solution": [
                        "Bước 1: Phân tích bản chất dữ liệu đầu vào:",
                        "  - Các đại lượng đường huyết (ví dụ: 105.2 mg/dL) và huyết áp (ví dụ: 125.8 mmHg) là các biến ngẫu nhiên liên tục (thuộc tập số thực R).",
                        "Bước 2: Đối chiếu với các biến thể Naive Bayes:",
                        "  - Bernoulli NB: Chỉ dành cho dữ liệu nhị phân {0, 1}.",
                        "  - Multinomial NB: Chỉ dành cho dữ liệu số nguyên đếm tần suất {0, 1, 2, ...}.",
                        "  - Gaussian NB: Giả định các đặc trưng liên tục tuân theo phân phối chuẩn Gaussian N(μ, σ²).",
                        "Kết luận: Gaussian Naive Bayes là biến thể phù hợp nhất. Đáp án đúng là C."
                    ]
                }
            },

            # =================================================================
            # MỤC 3.5: KỸ THUẬT SỐNG CÒN TRONG CÀI ĐẶT
            # =================================================================
            {
                "heading": "3.5. Hai Kỹ Thuật Sinh Tử Trong Cài Đặt: Tràn Số Dưới (Underflow) & Làm Mịn Laplace (Laplace Smoothing)",
                "content": "Khi chuyển giao công thức Naive Bayes từ sách giáo khoa vào code máy tính thực tế, mô hình của bạn sẽ lập tức bị sụp đổ nếu không trang bị hai kỹ thuật sống còn này.",
                "deepDive": r"""**1. Vấn đề thứ nhất: Hiện tượng Tràn số dưới (Numerical Underflow):**

- **Bản chất vấn đề:**
  - Trong phân loại văn bản, mỗi từ $w_i$ có xác suất xuất hiện rất nhỏ, ví dụ $P(w_i|Y) \approx 0.0001 = 10^{-4}$.
  - Một văn bản thông thường chứa khoảng $d = 200$ từ. Khi nhân dồn 200 xác suất này với nhau:
    $$P(X|Y) = \prod_{i=1}^{200} P(w_i|Y) \approx (10^{-4})^{200} = 10^{-800}!$$
  - Tuy nhiên, chuẩn biểu diễn số thực 64-bit IEEE 754 trên mọi máy tính hiện đại chỉ hỗ trợ số nhỏ nhất tới khoảng $10^{-324}$.
  - Hậu quả: Bất kỳ số nào nhỏ hơn $10^{-324}$ sẽ bị máy tính làm tròn thành đúng **SỐ 0 TUYỆT ĐỐI (Underflow)**!
  - Cả hai lớp Spam và Ham đều ra kết quả 0, máy tính không thể so sánh và toàn bộ hệ thống tê liệt!

- **Vũ khí cứu cánh: Chuyển sang không gian Log-Likelihood:**
  - Vì hàm logarit tự nhiên $\ln(x)$ (hoặc $\log_{10}$) là một **hàm đồng biến nghiêm ngặt** trên khoảng $(0, \infty)$:
    $$A > B \iff \log(A) > \log(B)$$
  - Thay vì nhân các xác suất, ta lấy logarit hai vế. Phép nhân lập tức biến thành **PHÉP CỘNG CÁC CON SỐ ÂM HIỀN HÒA**:
    $$\log \left( P(Y) \prod_{i=1}^d P(x_i|Y) \right) = \log P(Y) + \sum_{i=1}^d \log P(x_i|Y)$$
  - Ví dụ: Thay vì nhân $10^{-4} \times 10^{-4}$, ta tính $(-4) + (-4) = -8$. Máy tính xử lý phép cộng số âm siêu nhanh, cực kỳ chính xác và không bao giờ lo bị tràn số!

---

**2. Vấn đề thứ hai: Tần suất bằng 0 (Zero-Frequency Problem / Out-of-Vocabulary):**

- **Bản chất thảm họa:**
  - Giả sử trong tập huấn luyện, từ 'bitcoin' xuất hiện 50 lần trong lớp Spam, nhưng xuất hiện **0 lần** trong lớp Ham ($N_{\text{bitcoin, Ham}} = 0$).
  - Khi ước lượng theo tần suất cực đại (MLE):
    $$P(\text{bitcoin} | \text{Ham}) = \frac{0}{N_{\text{Ham}}} = 0$$
  - Bây giờ, một email từ người bạn thân gửi đến với nội dung: 'Hôm nay tớ đọc báo thấy có bài viết hay về bitcoin, cậu xem nhé'. Đây rõ ràng là thư thường (Ham) 100%!
  - Nhưng khi Naive Bayes tính xác suất lớp Ham:
    $$P(\text{Email}|\text{Ham}) = P(\text{hôm nay}|\text{Ham}) \dots \times \mathbf{P(\text{bitcoin}|\text{Ham})} \dots = (\dots) \times \mathbf{0} \times (\dots) = \mathbf{0}!$$
  - **Chỉ đúng 1 con số 0 duy nhất đã xóa sổ sạch sành sanh mọi bằng chứng khác!** Dù 99 từ còn lại đều chứng minh email này là thư thường, chỉ vì có đúng từ 'bitcoin', mô hình kết luận xác suất Ham = 0 và tống thẳng thư của bạn vào thùng rác!

- **Vũ khí cứu cánh: Làm mịn Laplace (Laplace / Add-1 Smoothing):**
  - **Ý tưởng:** Giả định rằng mỗi từ trong từ điển đã từng xuất hiện ít nhất một số lần ảo trước đó!
  - **Công thức Laplace Smoothing ($\alpha = 1$):**
    $$\hat{P}(w_i | Y) = \frac{N_{w_i, Y} + 1}{N_Y + |V|}$$
    - $N_{w_i, Y}$: Số lần từ $w_i$ thực tế xuất hiện trong lớp $Y$.
    - $N_Y$: Tổng số từ của toàn bộ lớp $Y$.
    - $|V|$: **Tổng số từ vựng duy nhất trong toàn hệ thống (Kích thước từ điển).**

- **Tại sao mẫu số bắt buộc phải cộng $|V|$ mà không phải cộng 1?**
  - Đây là câu hỏi kinh điển trong các kỳ thi học sinh giỏi!
  - Để đảm bảo tính chất thiêng liêng của xác suất: Tổng xác suất của tất cả các từ trong từ điển phải luôn luôn bằng đúng 1:
    $$\sum_{w \in V} \hat{P}(w|Y) = \sum_{w \in V} \frac{N_{w, Y} + 1}{N_Y + |V|} = \frac{\sum_{w \in V} N_{w, Y} + \sum_{w \in V} 1}{N_Y + |V|} = \frac{N_Y + |V|}{N_Y + |V|} = 1$$
  - Nếu ở mẫu số không cộng $|V|$, tổng xác suất sẽ vượt quá 1 và phá hỏng toàn bộ lý thuyết xác suất!
- **Làm mịn Lidstone (Add-$\alpha$ Smoothing):** Tổng quát hóa khi cộng thêm một tham số thực $\alpha \in (0, 1]$ thay vì cố định bằng 1: $\hat{P}(w_i|Y) = \frac{N_{w_i, Y} + \alpha}{N_Y + \alpha |V|}$.""",
                "formula": r"\hat{P}(w_i | Y) = \frac{N_{w_i, Y} + 1}{N_Y + |V|} \quad \Longleftrightarrow \quad \log P(Y|X) \propto \log P(Y) + \sum_{i=1}^d \log \hat{P}(x_i | Y)",
                "mathExplainer": [
                    { "sym": r"N_{w_i, Y} + 1", "name": "Tử số làm mịn", "mean": "Cộng thêm 1 lần xuất hiện ảo để đảm bảo xác suất không bao giờ bị rơi về số 0 tuyệt đối." },
                    { "sym": r"N_Y + |V|", "name": "Mẫu số làm mịn", "mean": "Cộng thêm kích thước từ điển |V| để bảo toàn tính chất tổng xác suất toàn từ điển luôn bằng 1." },
                    { "sym": r"\\sum \\log P(x_i|Y)", "name": "Tổng Log-Likelihood", "mean": "Chuyển phép nhân dãy số thực cực nhỏ thành phép cộng các số âm, triệt tiêu lỗi tràn số dưới." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Left side: Zero probability disaster -->
                      <g transform="translate(25, 20)">
                        <rect x="0" y="0" width="260" height="140" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="130" y="25" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Thảm Họa Xác Suất = 0</text>
                        <text x="20" y="55" font-family="Georgia" font-size="11">P(từ 1) = 0.05</text>
                        <text x="20" y="75" font-family="Georgia" font-size="11">P(từ 2) = 0.08</text>
                        <text x="20" y="95" font-family="Georgia" font-size="11" font-weight="bold">P(từ mới) = 0.00  (Chưa gặp)</text>
                        <line x1="20" y1="105" x2="240" y2="105" stroke="#111"/>
                        <text x="130" y="125" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Tích = 0.05 × 0.08 × 0 = 0 !</text>
                      </g>

                      <!-- Arrow transition -->
                      <g transform="translate(295, 75)">
                        <line x1="0" y1="15" x2="25" y2="15" stroke="#111" stroke-width="2"/>
                        <polygon points="25,15 15,10 15,20" fill="#111"/>
                      </g>

                      <!-- Right side: Laplace solution -->
                      <g transform="translate(330, 20)">
                        <rect x="0" y="0" width="265" height="140" fill="#111"/>
                        <text x="132" y="25" font-family="Georgia" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">Cứu Tinh: Làm Mịn Laplace</text>
                        <text x="20" y="55" font-family="Georgia" font-size="11" fill="#eee">Cộng 1 vào tử số: N_từ + 1</text>
                        <text x="20" y="75" font-family="Georgia" font-size="11" fill="#eee">Cộng |V| vào mẫu số: N_lớp + |V|</text>
                        <line x1="20" y1="90" x2="245" y2="90" stroke="#888"/>
                        <text x="132" y="112" font-family="Georgia" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">P(từ mới) = (0 + 1) / (N + |V|) > 0</text>
                        <text x="132" y="130" font-family="Georgia" font-size="9" fill="#ccc" text-anchor="middle">Xóa bỏ hoàn toàn số 0, mô hình sống sót!</text>
                      </g>
                    </svg>""",
                    "caption": "Sự kỳ diệu của Laplace Smoothing: Chuyển xác suất 0 thành một giá trị dương nhỏ hợp lý, cứu vãn toàn bộ tích xác suất của bài toán."
                },
                "commonPitfalls": "Cạm bẫy tính mẫu số Laplace: Đề thi thường gài bẫy bằng cách cho $N_{\\text{Spam}}$ là tổng số từ của lớp Spam, và cho thêm số văn bản $D$ của lớp đó. Rất nhiều bạn lấy mẫu số là $N_{\\text{Spam}} + D$ thay vì $N_{\\text{Spam}} + |V|$. Hãy khắc cốt ghi tâm: Mẫu số luôn luôn cộng với kích thước toàn bộ TẬP TỪ VỰNG DUY NHẤT $|V|$!",
                "practiceQuestion": {
                    "level": "Nâng cao",
                    "question": "Trong một tập dữ liệu phân loại tin tức, lớp 'Thể thao' có tổng cộng N = 800 từ. Toàn bộ tập dữ liệu có tổng cộng |V| = 200 từ vựng duy nhất. Từ 'VAR' xuất hiện đúng 2 lần trong lớp Thể thao. Áp dụng kỹ thuật làm mịn Laplace (Add-1), xác suất P('VAR' | Thể thao) bằng bao nhiêu?",
                    "options": [
                        "A. 3 / 801 (khoảng 0.0037)",
                        "B. 3 / 1000 (chính xác 0.0030)",
                        "C. 2 / 1000 (chính xác 0.0020)",
                        "D. 3 / 200 (chính xác 0.0150)"
                    ],
                    "correctIndex": 1,
                    "hint": "Công thức Laplace: P = (N_từ + 1) / (N_lớp + |V|). Thay số: (2 + 1) / (800 + 200).",
                    "solution": [
                        "Bước 1: Xác định các thành phần của công thức làm mịn Laplace:",
                        "  - Số lần từ 'VAR' xuất hiện trong lớp Thể thao: N_VAR = 2.",
                        "  - Tổng số từ của lớp Thể thao: N_lớp = 800.",
                        "  - Kích thước từ vựng toàn cục: |V| = 200.",
                        "Bước 2: Thay vào công thức Laplace Smoothing:",
                        "  P('VAR' | Thể thao) = (N_VAR + 1) / (N_lớp + |V|)",
                        "  P('VAR' | Thể thao) = (2 + 1) / (800 + 200) = 3 / 1000 = 0.0030.",
                        "Kết luận: Đáp án chính xác là B (3 / 1000)."
                    ]
                }
            },

            # =================================================================
            # MỤC 3.6: BÀI TOÁN THỰC HÀNH TÍNH TAY TỪ A ĐẾN Z
            # =================================================================
            {
                "heading": "3.6. Bài Toán Tính Tay Chuẩn Đề Thi VAIO: Huấn Luyện & Dự Đoán Bộ Lọc Spam Email Hoàn Chỉnh",
                "content": "Để thực sự làm chủ Naive Bayes và tự tin 100% trong phòng thi Olympic AI, hãy cùng thực hiện toàn bộ quy trình tính tay từ A đến Z trên một tập dữ liệu mẫu mini hoàn chỉnh.",
                "deepDive": r"""**ĐỀ BÀI THỰC HÀNH CHUẨN:**
Cho một tập dữ liệu huấn luyện gồm $5$ email ngắn đã được dán nhãn như sau:

| Email ID | Nhãn | Nội dung email |
| :---: | :---: | :--- |
| **D1** | **Spam** | 'tiền thưởng miễn phí' |
| **D2** | **Spam** | 'ưu đãi tiền mặt' |
| **D3** | **Spam** | 'miễn phí tiền thưởng ưu đãi' |
| **D4** | **Ham** | 'họp dự án tiền lương' |
| **D5** | **Ham** | 'báo cáo dự án' |

Hãy huấn luyện mô hình Multinomial Naive Bayes có làm mịn Laplace ($\alpha = 1$) và phân loại một email kiểm thử mới:
$$\mathbf{D_{\text{test}}} = \text{'ưu đãi dự án tiền thưởng'}$$

---

**BƯỚC 1: XÂY DỰNG TẬP TỪ VỰNG TOÀN CỤC (VOCABULARY $V$)**
Ta gom tất cả các từ duy nhất xuất hiện trong toàn bộ 5 văn bản:
$V = \{$tiền, thưởng, miễn, phí, ưu, đãi, mặt, họp, dự, án, lương, báo, cáo$\}$.
*(Để đơn giản, ta coi các từ ghép 'miễn phí', 'tiền thưởng', 'ưu đãi', 'dự án' là các token đơn lẻ):*
- $V = \{$tiền, thưởng, miễn phí, ưu đãi, mặt, họp, dự án, lương, báo cáo$\}$.
- Đếm tổng số từ vựng duy nhất: **$|V| = 9$ từ**.

---

**BƯỚC 2: TÍNH XÁC SUẤT TIÊN NGHIỆM (PRIOR PROBABILITIES)**
- Tổng số email: $N = 5$.
- Số email Spam: $3$ (D1, D2, D3) $\implies P(\text{Spam}) = \frac{3}{5} = \mathbf{0.6}$.
- Số email Ham: $2$ (D4, D5) $\implies P(\text{Ham}) = \frac{2}{5} = \mathbf{0.4}$.

---

**BƯỚC 3: ĐẾM TỔNG SỐ TỪ VÀ LẬP BẢNG TẦN SUẤT CHO TỪNG LỚP**
- **Lớp Spam:**
  - D1: tiền (1), thưởng (1), miễn phí (1) $\implies 3$ từ.
  - D2: ưu đãi (1), tiền (1), mặt (1) $\implies 3$ từ.
  - D3: miễn phí (1), tiền (1), thưởng (1), ưu đãi (1) $\implies 4$ từ.
  - $\implies$ Tổng số từ của lớp Spam: **$N_{\text{Spam}} = 3 + 3 + 4 = 10$ từ**.
- **Lớp Ham:**
  - D4: họp (1), dự án (1), tiền (1), lương (1) $\implies 4$ từ.
  - D5: báo cáo (1), dự án (1) $\implies 2$ từ.
  - $\implies$ Tổng số từ của lớp Ham: **$N_{\text{Ham}} = 4 + 2 = 6$ từ**.

---

**BƯỚC 4: TÍNH CÁC XÁC SUẤT LIKELIHOOD CÓ LÀM MỊN LAPLACE CHO CÁC TỪ TRONG EMAIL TEST**
Email kiểm thử gồm 4 từ: $D_{\text{test}} = \{$ưu đãi, dự án, tiền, thưởng$\}$.
Áp dụng công thức: $P(w|Y) = \frac{N_{w, Y} + 1}{N_Y + |V|}$ (với mẫu số Spam là $10 + 9 = \mathbf{19}$; mẫu số Ham là $6 + 9 = \mathbf{15}$):

1. **Từ 'ưu đãi':**
   - Trong Spam: xuất hiện 2 lần (D2, D3) $\implies P(\text{ưu đãi}|\text{Spam}) = \frac{2 + 1}{19} = \frac{3}{19}$.
   - Trong Ham: xuất hiện 0 lần $\implies P(\text{ưu đãi}|\text{Ham}) = \frac{0 + 1}{15} = \frac{1}{15}$.
2. **Từ 'dự án':**
   - Trong Spam: xuất hiện 0 lần $\implies P(\text{dự án}|\text{Spam}) = \frac{0 + 1}{19} = \frac{1}{19}$.
   - Trong Ham: xuất hiện 2 lần (D4, D5) $\implies P(\text{dự án}|\text{Ham}) = \frac{2 + 1}{15} = \frac{3}{15}$.
3. **Từ 'tiền':**
   - Trong Spam: xuất hiện 3 lần (D1, D2, D3) $\implies P(\text{tiền}|\text{Spam}) = \frac{3 + 1}{19} = \frac{4}{19}$.
   - Trong Ham: xuất hiện 1 lần (D4) $\implies P(\text{tiền}|\text{Ham}) = \frac{1 + 1}{15} = \frac{2}{15}$.
4. **Từ 'thưởng':**
   - Trong Spam: xuất hiện 2 lần (D1, D3) $\implies P(\text{thưởng}|\text{Spam}) = \frac{2 + 1}{19} = \frac{3}{19}$.
   - Trong Ham: xuất hiện 0 lần $\implies P(\text{thưởng}|\text{Ham}) = \frac{0 + 1}{15} = \frac{1}{15}$.

---

**BƯỚC 5: TÍNH TỬ SỐ BAYES CHO TỪNG LỚP VÀ KẾT LUẬN**

- **Điểm số cho lớp Spam:**
  $$\text{Score}(\text{Spam}) = P(\text{Spam}) \times P(\text{ưu đãi}|\text{Spam}) \times P(\text{dự án}|\text{Spam}) \times P(\text{tiền}|\text{Spam}) \times P(\text{thưởng}|\text{Spam})$$
  $$\text{Score}(\text{Spam}) = 0.6 \times \frac{3}{19} \times \frac{1}{19} \times \frac{4}{19} \times \frac{3}{19} = 0.6 \times \frac{36}{130,321} \approx \mathbf{1.657 \times 10^{-4}}$$

- **Điểm số cho lớp Ham:**
  $$\text{Score}(\text{Ham}) = P(\text{Ham}) \times P(\text{ưu đãi}|\text{Ham}) \times P(\text{dự án}|\text{Ham}) \times P(\text{tiền}|\text{Ham}) \times P(\text{thưởng}|\text{Ham})$$
  $$\text{Score}(\text{Ham}) = 0.4 \times \frac{1}{15} \times \frac{3}{15} \times \frac{2}{15} \times \frac{1}{15} = 0.4 \times \frac{6}{50,625} \approx \mathbf{4.741 \times 10^{-5}}$$

---

**BƯỚC 6: SO SÁNH VÀ KẾT LUẬN PHÂN LOẠI**
- Ta thấy: $\text{Score}(\text{Spam}) \approx 1.657 \times 10^{-4} > \text{Score}(\text{Ham}) \approx 4.741 \times 10^{-5}$.
- Tỷ lệ vượt trội: $\frac{\text{Score}(\text{Spam})}{\text{Score}(\text{Ham})} \approx \frac{16.57}{4.74} \approx \mathbf{3.5 \text{ lần}}$!
- **Xác suất phần trăm chuẩn hóa:**
  $$P(\text{Spam}|D_{\text{test}}) = \frac{1.657}{1.657 + 0.474} \approx \mathbf{77.75\%}$$
  $$P(\text{Ham}|D_{\text{test}}) = \frac{0.474}{1.657 + 0.474} \approx \mathbf{22.25\%}$$

**KẾT LUẬN CỦA MÔ HÌNH AI:** Email này được phân loại chính xác là **THƯ RÁC (SPAM)** với độ tin cậy $77.75\%$!""",
                "formula": r"\text{Score}(Y) = P(Y) \prod_{w \in D_{\text{test}}} \frac{N_{w, Y} + 1}{N_Y + |V|} \implies \hat{y} = \arg\max \{\text{Score}(\text{Spam}), \text{Score}(\text{Ham})\}",
                "mathExplainer": [
                    { "sym": r"D_{\\text{test}}", "name": "Văn bản thử nghiệm", "mean": "Mẫu dữ liệu mới cần đưa qua mô hình để dự đoán phân loại nhãn." },
                    { "sym": r"\\text{Score}(Y)", "name": "Tử số quyết định MAP", "mean": "Tích của xác suất tiên nghiệm và các xác suất thành phần của các từ có trong văn bản." },
                    { "sym": r"P(\\text{Spam}|D)", "name": "Độ tự tin chuẩn hóa", "mean": "Lấy Score(Spam) chia cho tổng [Score(Spam) + Score(Ham)] để đưa về thang đo phần trăm 0% - 100%." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 185" width="100%" height="185" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="185" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Training phase -->
                      <g transform="translate(20, 20)">
                        <rect x="0" y="0" width="140" height="145" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="70" y="25" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">1. Huấn Luyện</text>
                        <text x="15" y="50" font-family="Georgia" font-size="10">• 5 Email mẫu</text>
                        <text x="15" y="70" font-family="Georgia" font-size="10">• Đếm Prior: P(S)=0.6</text>
                        <text x="15" y="90" font-family="Georgia" font-size="10">• Đếm từ vựng: |V|=9</text>
                        <text x="15" y="110" font-family="Georgia" font-size="10">• Lập bảng Laplace</text>
                        <text x="15" y="130" font-family="Georgia" font-size="9" fill="#555">N_Spam=10, N_Ham=6</text>
                      </g>

                      <line x1="165" y1="92" x2="190" y2="92" stroke="#111" stroke-width="2"/>
                      <polygon points="190,92 182,88 182,96" fill="#111"/>

                      <!-- Testing phase -->
                      <g transform="translate(195, 20)">
                        <rect x="0" y="0" width="180" height="145" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="90" y="25" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">2. Tính Toán Email Mới</text>
                        <text x="15" y="48" font-family="Georgia" font-size="10" font-weight="bold">Email: 'ưu đãi dự án tiền thưởng'</text>
                        <text x="15" y="70" font-family="Georgia" font-size="10">Score(Spam) = 0.6 × 3/19</text>
                        <text x="25" y="85" font-family="Georgia" font-size="9" fill="#444">× 1/19 × 4/19 × 3/19 ≈ 1.66e-4</text>
                        <text x="15" y="108" font-family="Georgia" font-size="10">Score(Ham) = 0.4 × 1/15</text>
                        <text x="25" y="123" font-family="Georgia" font-size="9" fill="#444">× 3/15 × 2/15 × 1/15 ≈ 0.47e-4</text>
                      </g>

                      <line x1="380" y1="92" x2="405" y2="92" stroke="#111" stroke-width="2"/>
                      <polygon points="405,92 397,88 397,96" fill="#111"/>

                      <!-- Decision phase -->
                      <g transform="translate(410, 20)">
                        <rect x="0" y="0" width="190" height="145" fill="#111"/>
                        <text x="95" y="25" font-family="Georgia" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">3. Quyết Định MAP</text>
                        <text x="95" y="55" font-family="Georgia" font-size="11" fill="#eee" text-anchor="middle">Score(Spam) > Score(Ham)</text>
                        <rect x="25" y="70" width="140" height="30" fill="#fff"/>
                        <text x="95" y="90" font-family="Georgia" font-size="12" font-weight="bold" fill="#111" text-anchor="middle">KẾT QUẢ: SPAM</text>
                        <text x="95" y="125" font-family="Georgia" font-size="11" fill="#fff" text-anchor="middle">Độ tin cậy: 77.75%</text>
                      </g>
                    </svg>""",
                    "caption": "Sơ đồ dòng dữ liệu hoàn chỉnh của bộ phân loại Naive Bayes: Từ tập huấn luyện mini đến quyết định nhãn email thử nghiệm."
                },
                "commonPitfalls": "Bỏ quên các từ vắng mặt nhưng có trong câu test: Khi tính điểm số cho lớp Spam, từ 'dự án' không có trong các email Spam huấn luyện. Một số bạn quên tính từ này hoặc gán bằng 0. Nhớ rằng nhờ Laplace smoothing, từ 'dự án' vẫn có xác suất là (0 + 1)/19! Tương tự cho các từ 'ưu đãi' và 'thưởng' trong lớp Ham.",
                "practiceQuestion": {
                    "level": "Nâng cao",
                    "question": "Giả sử một email kiểm thử khác chỉ chứa đúng 1 từ duy nhất: 'họp'. Dựa vào bảng dữ liệu huấn luyện ở trên, tỷ số tử số Bayes giữa lớp Ham so với lớp Spam [Score(Ham) / Score(Spam)] xấp xỉ bằng bao nhiêu?",
                    "options": [
                        "A. Khoảng 1.05 lần",
                        "B. Khoảng 1.69 lần (Ham chiến thắng)",
                        "C. Khoảng 0.50 lần (Spam chiến thắng)",
                        "D. Khoảng 3.25 lần"
                    ],
                    "correctIndex": 1,
                    "hint": "Tính Score(Ham) = 0.4 × P('họp'|Ham) = 0.4 × (1+1)/(6+9) = 0.4 × 2/15. Score(Spam) = 0.6 × P('họp'|Spam) = 0.6 × (0+1)/(10+9) = 0.6 × 1/19.",
                    "solution": [
                        "Bước 1: Tính Score cho lớp Ham:",
                        "  Từ 'họp' xuất hiện 1 lần trong lớp Ham (D4).",
                        "  P('họp'|Ham) = (1 + 1) / (6 + 9) = 2 / 15.",
                        "  Score(Ham) = P(Ham) × P('họp'|Ham) = 0.4 × (2/15) = 0.8 / 15 ≈ 0.05333.",
                        "Bước 2: Tính Score cho lớp Spam:",
                        "  Từ 'họp' xuất hiện 0 lần trong lớp Spam.",
                        "  P('họp'|Spam) = (0 + 1) / (10 + 9) = 1 / 19.",
                        "  Score(Spam) = P(Spam) × P('họp'|Spam) = 0.6 × (1/19) = 0.6 / 19 ≈ 0.03158.",
                        "Bước 3: Lập tỉ số Score(Ham) / Score(Spam):",
                        "  Tỉ số = 0.05333 / 0.03158 ≈ 1.6888 ≈ 1.69 lần.",
                        "Kết luận: Score(Ham) lớn hơn Score(Spam) khoảng 1.69 lần, email được phân loại là Ham. Đáp án đúng là B."
                    ]
                }
            }
        ],
        "interactiveWidget": "widget-naive-bayes",
        "examConnection": {
            "questionTitle": "Điểm Trọng Tâm Về Xác Suất & NLP Trong Đề Thi VAIO 2025",
            "items": [
                {
                    "code": "Xác Suất Hậu Nghiệm (Posterior)",
                    "problem": "Tại sao Naive Bayes thường được dùng làm mô hình Baseline (đối chuẩn cơ sở) đầu tiên trong mọi cuộc thi AI xử lý văn bản?",
                    "solution": [
                        "1. Tốc độ cực nhanh: Thời gian huấn luyện O(N·d), chỉ là đếm tần suất trên một vòng lặp duyệt dữ liệu.",
                        "2. Khả năng chống quá khớp tốt với tập dữ liệu ít mẫu nhờ giả định độc lập làm giảm số lượng tham số cần ước lượng từ hàm mũ 2^d xuống tuyến tính O(d).",
                        "3. Dễ diễn giải (Explainability): Mỗi từ đóng góp trực tiếp một lượng log-odds vào quyết định phân loại, giúp kỹ sư dễ dàng kiểm tra từ khóa nào gây ra dự đoán sai."
                    ]
                },
                {
                    "code": "Laplace Smoothing & Underflow",
                    "problem": "Hai lỗi lập trình phổ biến nhất khiến mô hình Naive Bayes tự viết bị crash điểm trong phần thi thực hành là gì?",
                    "solution": [
                        "1. Không lấy Log-Likelihood: Nhân liên tiếp các xác suất thực dẫn đến Underflow làm tròn về 0.0, khiến mô hình gán nhãn ngẫu nhiên hoặc crash chia cho 0.",
                        "2. Quên cộng kích thước từ điển |V| ở mẫu số khi làm mịn Laplace, làm vi phạm điều kiện tiên quyết của phân phối xác suất (tổng xác suất không bằng 1)."
                    ]
                }
            ]
        },
        "takeaways": [
            "Định lý Bayes là cơ chế cập nhật niềm tin: Posterior ∝ Prior × Likelihood.",
            "Giả định Naive độc lập có điều kiện: P(x₁, ..., x_d | Y) = ∏ P(x_i | Y), biến bài toán nổ tung tổ hợp thành phép nhân đơn giản.",
            "3 Biến thể: Bernoulli (nhị phân 0/1), Multinomial (đếm tần suất văn bản Bag-of-Words), Gaussian (số thực liên tục hình chuông).",
            "Làm mịn Laplace (Add-1 Smoothing): P(w|Y) = (N_w + 1) / (N_Y + |V|), cứu mô hình khỏi thảm họa xác suất 0.",
            "Log-Likelihood: Chuyển phép nhân dãy số nhỏ thành phép cộng số âm log P(Y) + ∑ log P(x_i|Y) để dập tắt nguy cơ tràn số dưới (Underflow)."
        ]
    }
