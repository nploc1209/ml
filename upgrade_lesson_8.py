# -*- coding: utf-8 -*-
"""
upgrade_lesson_8.py - Masterpiece Lesson 8 for VAIO 2025 AI Olympiad
Chủ đề: Máy Vector Hỗ Trợ (SVM), Kernel Trick & Thuật Toán k-NN
Toàn diện từ con số 0 đến làm chủ sâu sắc.

Tuân thủ nghiêm ngặt chuẩn sư phạm:
Trực giác đời sống -> Bản chất toán học -> Cách thức hoạt động ->
Giải mã ký hiệu cho học sinh lớp 12 -> Ví dụ tính toán bằng số từng bước ->
Cạm bẫy phòng thi -> Câu hỏi trắc nghiệm kiểm tra độ hiểu có lời giải chi tiết.
"""

def get_masterpiece_lesson_8():
    return {
        "id": "lesson-8",
        "title": "8. Máy Vector Hỗ Trợ (SVM), Kernel Trick & Thuật Toán k-NN",
        "syllabusBadge": "BUỔI 4: MÁY VECTOR HỖ TRỢ (SVM) & THUẬT TOÁN k-NN",
        "summary": "Nghệ thuật phân chia ranh giới hình học tối ưu: Từ trực giác dải phân cách an toàn giữa hai ngôi làng đến Siêu phẳng lề cực đại (Maximum Margin Hyperplane = 2/||w||), giải mã vai trò độc tôn của các Support Vectors qua hệ điều kiện KKT, Soft-Margin SVM với biến lỏng xi và tham số phạt C, vũ khí tối thượng Kernel Trick (RBF chiếu lên không gian vô hạn chiều), và đối chiếu chuyên sâu với thuật toán 'học lười biếng' k-NN cùng lời nguyền số chiều (Curse of Dimensionality).",
        "intuition": {
            "title": "Trực giác thực tế: Con đường biên giới công bằng giữa hai ngôi làng và nguyên lý 'chọn bạn mà chơi'",
            "content": """Hãy tưởng tượng hai ngôi làng A và B nằm ở hai bên bờ một thung lũng. Họ muốn xây dựng một con đường ranh giới và một dải đất trống phi quân sự (Hành lang đệm) ở giữa để cư dân hai làng không bao giờ cãi cọ va chạm.

Có vô số con đường có thể vẽ ra để ngăn cách hai làng.
Nhưng nếu bạn kẻ một con đường sát sạt tường nhà của làng A, chỉ cần một đứa trẻ làng A bước chân ra khỏi cửa là đã giẫm sang ranh giới tranh chấp! Con đường đó quá mong manh và nguy hiểm (mô hình kém ổn định trước nhiễu).

Con đường biên giới công bằng, an toàn và bền vững nhất phải là: **Chạy chính giữa và cách xa nhất có thể các ngôi nhà gần nhất của cả hai làng**! Bề rộng của hành lang đệm (Lề - Margin) phải được mở rộng tối đa!
- Những ngôi nhà nằm sát mép hành lang đệm nhất được gọi là các **Support Vectors (Các điểm tựa)**. Vị trí của con đường chỉ phụ thuộc duy nhất vào những ngôi nhà tiền tuyến này; mọi ngôi nhà khác nằm sâu trong đất liền không hề ảnh hưởng đến vị trí con đường! Đây chính là triết lý của **Support Vector Machine (SVM)**!

Và khi có một vị khách lạ bước vào vùng đất đó, làm sao biết anh ta thuộc về phe nào?
Hãy nhìn vào **3 người hàng xóm gần nhất** xung quanh nhà anh ta: Nếu 2 trong 3 người là cư dân làng A, anh ta chắc chắn thuộc về làng A! Đây chính là triết lý 'chọn bạn mà chơi' của thuật toán **k-Láng Giềng Gần Nhất (k-NN)**!"""
        },
        "sections": [
            # =================================================================
            # MỤC 8.1: BẢN CHẤT HÌNH HỌC CỦA SVM & SIÊU PHẲNG LỀ CỰC ĐẠI
            # =================================================================
            {
                "heading": "8.1. Khởi Đầu Từ Con Số 0: Bản Chất Hình Học Của SVM & Siêu Phẳng Lề Cực Đại (Maximum Margin)",
                "content": "Trong không gian dữ liệu, có vô số siêu phẳng có thể phân tách hai lớp. SVM ra đời để tìm ra duy nhất MỘT siêu phẳng tối ưu tuyệt đối: Siêu phẳng có khoảng cách tới các điểm dữ liệu gần nhất là LỚN NHẤT.",
                "deepDive": r"""**1. Siêu phẳng (Hyperplane) là gì?**
- Trong không gian 2 chiều (2D): Siêu phẳng là một **Đường thẳng**: $w_1 x_1 + w_2 x_2 + b = 0$.
- Trong không gian 3 chiều (3D): Siêu phẳng là một **Mặt phẳng**: $w_1 x_1 + w_2 x_2 + w_3 x_3 + b = 0$.
- Trong không gian $d$ chiều tổng quát: Siêu phẳng là tập hợp các điểm $x$ thỏa mãn phương trình:
  $$w^T x + b = 0$$
  - $w = (w_1, w_2, \dots, w_d)^T$: **Vector pháp tuyến (Normal Vector)**, vuông góc với siêu phẳng và quyết định hướng nghiêng của siêu phẳng.
  - $b$: **Hệ số chệch (Bias)**, quyết định khoảng cách dịch chuyển của siêu phẳng so với gốc tọa độ.

**2. Quy ước nhãn đặc thù trong SVM: $y \in \{-1, +1\}$:**
Khác với Hồi quy Logistic quy ước nhãn là $\{0, 1\}$, SVM quy ước nhãn là **$\pm 1$**:
- Nếu mẫu $x_i$ thuộc lớp Dương: $y_i = +1 \implies w^T x_i + b \ge +1$.
- Nếu mẫu $x_i$ thuộc lớp Âm: $y_i = -1 \implies w^T x_i + b \le -1$.
- **Điều kỳ diệu của phép nhân:** Ta có thể gộp hai điều kiện trên thành duy nhất một bất đẳng thức toán học tao nhã:
  $$y_i (w^T x_i + b) \ge 1, \quad \forall i = 1, \dots, N$$
  *(Bởi vì nếu $y_i = -1$ và $(w^T x_i + b) \le -1$ thì tích của hai số âm luôn là một số dương $\ge +1$!).*

**3. Chứng minh toán học: Bề rộng hành lang lề (Margin Width) = $2 / \|w\|$:**
Hai bờ rào biên giới tiếp xúc với các điểm gần nhất lần lượt có phương trình:
- Bờ rào dương: $w^T x_+ + b = +1$
- Bờ rào âm: $w^T x_- + b = -1$

Trừ hai phương trình cho nhau:
$$w^T (x_+ - x_-) = 2$$
Vector $(x_+ - x_-)$ là đoạn thẳng nối từ một điểm trên bờ rào âm sang bờ rào dương.
Để tìm khoảng cách vuông góc hình học giữa hai bờ rào (Margin), ta chiếu vector này lên vector pháp tuyến đơn vị $\frac{w}{\|w\|}$:
$$\text{Margin Width} = \frac{w^T (x_+ - x_-)}{\|w\|} = \frac{2}{\|w\|}$$

**4. Bài toán tối ưu lề cực đại (Hard-Margin SVM):**
Mục tiêu là **tối đa hóa bề rộng lề** $\frac{2}{\|w\|}$.
Tối đa hóa $\frac{2}{\|w\|}$ tương đương với việc **cực tiểu hóa $\|w\|$, hay cực tiểu hóa $\frac{1}{2}\|w\|^2$** (để đạo hàm đẹp):
$$\min_{w, b} \frac{1}{2}\|w\|^2 \quad \text{thỏa mãn điều kiện} \quad y_i (w^T x_i + b) \ge 1, \, \forall i$$
Đây là một bài toán **Quy hoạch toàn phương lồi (Convex Quadratic Programming)**, đảm bảo luôn tìm được duy nhất một nghiệm cực tiểu toàn cục mà không sợ bị mắc kẹt ở cực tiểu địa phương!""",
                "formula": r"\min_{w, b} \frac{1}{2}\|w\|^2 \quad \text{s.t.} \quad y_i (w^T x_i + b) \ge 1, \quad \text{Margin} = \frac{2}{\|w\|}",
                "mathExplainer": [
                    { "sym": "w", "name": "Vector pháp tuyến", "mean": "Vector vuông góc với siêu phẳng, xác định hướng của đường ranh giới." },
                    { "sym": "b", "name": "Hệ số chệch (Bias)", "mean": "Xác định khoảng cách tịnh tiến của siêu phẳng so với gốc tọa độ." },
                    { "sym": "y_i \\in \\{-1, +1\\}", "name": "Nhãn lớp trong SVM", "mean": "Quy ước nhị phân chuẩn của SVM (+1 cho lớp dương, -1 cho lớp âm)." },
                    { "sym": "\\|w\\|", "name": "Độ dài chuẩn L2 của w", "mean": "Căn bậc hai của tổng bình phương các thành phần: sqrt(w₁² + w₂² + ... + w_d²)." },
                    { "sym": "\\text{Margin} = 2/\\|w\\|", "name": "Bề rộng hành lang lề", "mean": "Khoảng cách vuông góc giữa 2 bờ rào biên giới tiếp xúc với các điểm gần nhất." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="210" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(60, 20)">
                        <text x="260" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">SIÊU PHẲNG LỀ CỰC ĐẠI TRONG KHÔNG GIAN 2D</text>

                        <!-- Margin Zone shaded -->
                        <polygon points="120,170 320,10 380,10 180,170" fill="#eee"/>

                        <!-- Positive boundary line: w^T x + b = +1 -->
                        <line x1="120" y1="170" x2="320" y2="10" stroke="#888" stroke-width="1.5" stroke-dasharray="4,4"/>
                        <text x="325" y="15" font-family="Georgia" font-size="9" fill="#555">wᵀx + b = +1</text>

                        <!-- Decision Hyperplane: w^T x + b = 0 -->
                        <line x1="150" y1="170" x2="350" y2="10" stroke="#111" stroke-width="2.5"/>
                        <text x="355" y="28" font-family="Georgia" font-size="10" font-weight="bold">wᵀx + b = 0</text>

                        <!-- Negative boundary line: w^T x + b = -1 -->
                        <line x1="180" y1="170" x2="380" y2="10" stroke="#888" stroke-width="1.5" stroke-dasharray="4,4"/>
                        <text x="385" y="42" font-family="Georgia" font-size="9" fill="#555">wᵀx + b = -1</text>

                        <!-- Normal vector w arrow -->
                        <line x1="250" y1="90" x2="290" y2="40" stroke="#111" stroke-width="2"/>
                        <polygon points="290,40 280,45 285,52" fill="#111"/>
                        <text x="295" y="55" font-family="Georgia" font-size="10" font-weight="bold">w (Pháp tuyến)</text>

                        <!-- Support Vectors -->
                        <!-- Positive points -->
                        <circle cx="80" cy="140" r="5" fill="#111"/><circle cx="120" cy="90" r="5" fill="#111"/><circle cx="160" cy="50" r="5" fill="#111"/>
                        <!-- SV positive on the boundary -->
                        <circle cx="220" cy="90" r="8" fill="none" stroke="#111" stroke-width="2"/>
                        <circle cx="220" cy="90" r="4" fill="#111"/>
                        <text x="145" y="105" font-family="Georgia" font-size="9" font-weight="bold">Support Vector (+1)</text>

                        <!-- Negative points -->
                        <circle cx="340" cy="150" r="5" fill="#fff" stroke="#111" stroke-width="2"/>
                        <circle cx="380" cy="110" r="5" fill="#fff" stroke="#111" stroke-width="2"/>
                        <!-- SV negative on the boundary -->
                        <circle cx="280" cy="90" r="8" fill="none" stroke="#111" stroke-width="2"/>
                        <circle cx="280" cy="90" r="4" fill="#fff" stroke="#111" stroke-width="2"/>
                        <text x="295" y="105" font-family="Georgia" font-size="9" font-weight="bold">Support Vector (-1)</text>

                        <!-- Margin arrow -->
                        <line x1="185" y1="120" x2="245" y2="120" stroke="#111" stroke-width="1.5"/>
                        <text x="215" y="135" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Margin = 2/||w||</text>
                      </g>
                    </svg>""",
                    "caption": "Mô hình SVM lề cực đại: Siêu phẳng chính giữa cách đều hai bờ rào lề, khoảng cách giữa 2 bờ rào đạt giá trị lớn nhất 2/||w||."
                },
                "commonPitfalls": "Nhầm lẫn giữa công thức khoảng cách từ 1 điểm đến siêu phẳng và bề rộng lề: Khoảng cách từ 1 Support Vector đến siêu phẳng chính giữa là 1/||w|| (nửa bề rộng lề). Bề rộng toàn bộ hành lang lề giữa hai bờ rào đối diện là 2/||w||!",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Trong không gian 2D, một mô hình SVM tìm được vector trọng số w = (3, 4)ᵀ. Bề rộng toàn phần của hành lang lề (Margin Width) của siêu phẳng phân loại này bằng bao nhiêu?",
                    "options": [
                        "A. 0.40",
                        "B. 0.20",
                        "C. 0.50",
                        "D. 2.00"
                    ],
                    "correctIndex": 0,
                    "hint": "Tính độ dài chuẩn ||w|| = sqrt(3² + 4²) = sqrt(9 + 16) = sqrt(25) = 5. Bề rộng lề Margin = 2 / ||w|| = 2 / 5.",
                    "solution": [
                        "Bước 1: Tính độ dài vector pháp tuyến ||w||:",
                        "  ||w|| = sqrt(w₁² + w₂²) = sqrt(3² + 4²) = sqrt(9 + 16) = sqrt(25) = 5.",
                        "Bước 2: Áp dụng công thức bề rộng lề SVM:",
                        "  Margin = 2 / ||w|| = 2 / 5 = 0.40.",
                        "Đáp án chính xác: A (0.40)."
                    ]
                }
            },

            # =================================================================
            # MỤC 8.2: CÁC SUPPORT VECTORS & BÀI TOÁN ĐỐI NGẪU LAGRANGE
            # =================================================================
            {
                "heading": "8.2. Giải Mã Các Support Vectors: Tính Thưa (Sparsity) & Bài Toán Đối Ngẫu Lagrange (Dual Form)",
                "content": "Tại sao thuật toán lại có tên là 'Máy Vector Hỗ Trợ'? Khám phá vai trò độc tôn của các điểm Support Vectors, hệ điều kiện KKT và cách bài toán đối ngẫu đưa tích vô hướng vào trung tâm của mô hình.",
                "deepDive": r"""**1. Support Vectors (Các Vector Hỗ Trợ) là gì?**
- Trong toán học, mỗi điểm dữ liệu $x_i$ trong không gian $d$ chiều chính là một vector tọa độ.
- **Support Vectors** là những điểm dữ liệu nằm **CHÍNH XÁC TRÊN HAI BỜ RÀO LỀ**:
  $$y_i (w^T x_i + b) = 1$$
- Chúng là những điểm 'tiền tuyến' gần siêu phẳng nhất, đóng vai trò như những chiếc cột trụ chống đỡ toàn bộ bờ rào lề.

**2. Tính chất độc tôn chấn động: Nghiệm thưa (Sparsity) của SVM:**
Hãy tưởng tượng bạn có 1,000,000 điểm dữ liệu trong tập huấn luyện:
- Thuật toán SVM tìm ra nghiệm và chỉ có đúng 4 điểm dữ liệu là Support Vectors!
- **Điều gì xảy ra nếu bạn XÓA BỎ 999,996 ĐIỂM DỮ LIỆU CÒN LẠI?**
  $\implies$ Siêu phẳng SVM **GIỮ NGUYÊN 100% VỊ TRÍ CŨ**, không hề suy suyển 1 milimet nào!
- **Điều gì xảy ra nếu bạn THÊM VÀO 1,000,000 ĐIỂM MỚI nằm sâu trong vùng an toàn?**
  $\implies$ Siêu phẳng SVM **HOÀN TOÀN KHÔNG BỊ ẢNH HƯỞNG**!
- *Ý nghĩa:* Khác với Hồi quy Logistic hay Naive Bayes (nơi mọi điểm dữ liệu đều tham gia kéo đường biên), vị trí của siêu phẳng SVM **CHỈ ĐƯỢC QUYẾT ĐỊNH DUY NHẤT BỞI CÁC SUPPORT VECTORS**!

**3. Bài toán Đối Ngẫu Lagrange (Lagrange Dual Problem):**
Để giải bài toán tối ưu có ràng buộc, ta lập hàm Lagrange với các nhân tử $\alpha_i \ge 0$:
$$\mathcal{L}(w, b, \alpha) = \frac{1}{2}\|w\|^2 - \sum_{i=1}^N \alpha_i \left[ y_i (w^T x_i + b) - 1 \right]$$

Lấy đạo hàm riêng theo các biến gốc $w$ và $b$ rồi cho bằng 0:
$$\frac{\partial \mathcal{L}}{\partial w} = 0 \implies w = \sum_{i=1}^N \alpha_i y_i x_i$$
$$\frac{\partial \mathcal{L}}{\partial b} = 0 \implies \sum_{i=1}^N \alpha_i y_i = 0$$

**Hệ điều kiện bù trừ KKT (Karush-Kuhn-Tucker Complementary Slackness):**
$$\alpha_i \left[ y_i (w^T x_i + b) - 1 \right] = 0$$
- Nếu điểm $x_i$ nằm sâu trong vùng an toàn ($y_i(w^Tx_i+b) > 1$) $\implies$ Bắt buộc **$\alpha_i = 0$**! (Điểm này hoàn toàn không đóng góp gì vào vector trọng số $w$).
- Chỉ những điểm nằm đúng trên bờ rào lề ($y_i(w^Tx_i+b) = 1$) mới có **$\alpha_i > 0$**! Đây chính là các **Support Vectors**!

**4. Dạng đối ngẫu toàn phần (Dual Formulation):**
Thay $w = \sum \alpha_i y_i x_i$ ngược lại vào hàm Lagrange, ta thu được bài toán đối ngẫu chỉ còn ẩn số $\alpha$:
$$\max_\alpha \sum_{i=1}^N \alpha_i - \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N \alpha_i \alpha_j y_i y_j (\mathbf{x}_i^T \mathbf{x}_j) \quad \text{s.t.} \quad \alpha_i \ge 0, \, \sum_{i=1}^N \alpha_i y_i = 0$$
**Điểm mấu chốt vĩ đại:** Toàn bộ dữ liệu huấn luyện chỉ xuất hiện dưới dạng duy nhất là **TÍCH VÔ HƯỚNG $\mathbf{x}_i^T \mathbf{x}_j$**! Đây chính là cánh cửa thần kỳ mở ra vũ khí Kernel Trick!""",
                "formula": r"w = \sum_{i \in \text{SV}} \alpha_i y_i x_i, \quad \alpha_i [y_i (w^T x_i + b) - 1] = 0, \quad \max_\alpha \sum \alpha_i - \frac{1}{2}\sum \alpha_i \alpha_j y_i y_j (x_i^T x_j)",
                "mathExplainer": [
                    { "sym": "\\alpha_i (Alpha)", "name": "Nhân tử Lagrange", "mean": "Trọng số đóng góp của điểm i. alpha_i = 0 với điểm bình thường, alpha_i > 0 với Support Vectors." },
                    { "sym": "\\text{KKT Conditions}", "name": "Hệ điều kiện Karush-Kuhn-Tucker", "mean": "Điều kiện cần và đủ cho nghiệm tối ưu của bài toán quy hoạch phi tuyến có ràng buộc." },
                    { "sym": "x_i^T x_j", "name": "Tích vô hướng giữa 2 điểm", "mean": "Thước đo độ tương đồng hình học giữa 2 mẫu dữ liệu trong không gian gốc." },
                    { "sym": "\\text{Sparsity}", "name": "Tính thưa của nghiệm", "mean": "Đại đa số các mẫu đều có alpha_i = 0, mô hình chỉ lưu lại một tập nhỏ các Support Vectors." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 20)">
                        <text x="280" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">TÍNH THƯA CỦA NGHIỆM SVM: α = 0 VS α &gt; 0</text>

                        <!-- Non-SV points (alpha = 0) -->
                        <g transform="translate(30, 40)">
                          <rect x="0" y="0" width="230" height="100" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="115" y="22" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Điểm Trong Đất Liền (α_i = 0)</text>
                          <text x="15" y="48" font-family="Georgia" font-size="10">• Nằm sâu trong vùng an toàn</text>
                          <text x="15" y="68" font-family="Georgia" font-size="10">• y_i(wᵀx_i + b) &gt; 1</text>
                          <text x="15" y="90" font-family="Georgia" font-size="11" font-weight="bold" fill="#555">Xóa bỏ không ảnh hưởng gì!</text>
                        </g>

                        <!-- Arrow -->
                        <line x1="275" y1="90" x2="305" y2="90" stroke="#111" stroke-width="2"/>
                        <polygon points="305,90 297,86 297,94" fill="#111"/>

                        <!-- SV points (alpha > 0) -->
                        <g transform="translate(320, 40)">
                          <rect x="0" y="0" width="240" height="100" fill="#111"/>
                          <text x="120" y="22" font-family="Georgia" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">Support Vectors (α_i &gt; 0)</text>
                          <text x="15" y="48" font-family="Georgia" font-size="10" fill="#eee">• Nằm CHÍNH XÁC trên bờ rào lề</text>
                          <text x="15" y="68" font-family="Georgia" font-size="10" fill="#eee">• y_i(wᵀx_i + b) = 1</text>
                          <text x="15" y="90" font-family="Georgia" font-size="11" font-weight="bold" fill="#fff">Quyết định 100% vị trí siêu phẳng!</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "Chỉ các điểm Support Vectors với nhân tử Lagrange α > 0 mới quyết định vị trí siêu phẳng; các điểm khác trong đất liền có α = 0 hoàn toàn không ảnh hưởng."
                },
                "commonPitfalls": "Cạm bẫy phòng thi: Đề bài cho một tập dữ liệu đã huấn luyện SVM xong. Thêm 1,000 điểm dữ liệu mới nằm rất xa siêu phẳng. Hỏi siêu phẳng có thay đổi không? Đáp án là KHÔNG HỀ THAY ĐỔI vì các điểm mới đều có α = 0!",
                "practiceQuestion": {
                    "level": "Nâng cao (Câu 52 Đề Thi VAIO 2025)",
                    "question": "Trong thuật toán SVM phân loại nhị phân, điều gì sẽ xảy ra với siêu phẳng phân loại tối ưu nếu ta xóa bỏ một điểm dữ liệu huấn luyện x_k có nhân tử Lagrange α_k = 0?",
                    "options": [
                        "A. Siêu phẳng sẽ xoay đi một góc nhỏ",
                        "B. Bề rộng lề Margin sẽ bị thu hẹp lại",
                        "C. Siêu phẳng phân loại hoàn toàn không thay đổi vị trí và hướng",
                        "D. Bài toán tối ưu sẽ trở nên vô nghiệm"
                    ],
                    "correctIndex": 2,
                    "hint": "Theo công thức w = sum(α_i * y_i * x_i), nếu α_k = 0 thì điểm x_k có đóng góp gì vào vector trọng số w không?",
                    "solution": [
                        "Bước 1: Vector trọng số w được biểu diễn qua nghiệm đối ngẫu: w = sum_{i=1}^N α_i y_i x_i.",
                        "Bước 2: Với điểm x_k có α_k = 0, số hạng tương ứng trong tổng bằng 0 * y_k * x_k = 0.",
                        "Bước 3: Do đó, việc xóa bỏ điểm x_k không làm thay đổi giá trị của w và b. Siêu phẳng giữ nguyên 100% vị trí cũ.",
                        "Đáp án chính xác: C."
                    ]
                }
            },

            # =================================================================
            # MỤC 8.3: SOFT-MARGIN SVM, BIẾN LỎNG & SIÊU THAM SỐ C
            # =================================================================
            {
                "heading": "8.3. Dữ Liệu Có Nhiễu: Soft-Margin SVM, Biến Lỏng $\\xi_i$ & Siêu Tham Số Đánh Đổi $C$",
                "content": "Trong thực tế, dữ liệu hiếm khi phân tách hoàn hảo mà luôn có các điểm nhiễu lọt nhầm sang bên kia chiến tuyến. Khám phá cách Soft-Margin SVM sử dụng biến lỏng ξ để dung thứ cho sai sót và vai trò đánh đổi sống còn của tham số C.",
                "deepDive": r"""**1. Bế tắc của Hard-Margin SVM trên dữ liệu thực tế:**
- Nếu dữ liệu không phân tách tuyến tính hoàn hảo (Linearly Inseparable), hoặc chỉ cần có **đúng 1 điểm nhiễu Outlier** nằm lẫn sang vùng của lớp kia:
  - Hệ bất đẳng thức $y_i(w^Tx_i+b) \ge 1$ sẽ trở nên **VÔ NGHIỆM**!
  - Hoặc nếu cố tìm nghiệm, siêu phẳng sẽ bị ép uốn éo theo điểm dị biệt đó, khiến lề Margin bị co lại cực kỳ hẹp $\implies$ **Quá khớp (Overfitting)** thảm hại!

**2. Đột phá Soft-Margin SVM (Cortes & Vapnik, 1995):**
Cho phép một số điểm dữ liệu được quyền 'phạm quy' (nhảy vào trong hành lang lề hoặc thậm chí sang nhầm bên kia siêu phẳng).
Khoảng cách vi phạm của mỗi điểm được đo bằng **Biến lỏng (Slack Variable) $\xi_i \ge 0$** (đọc là Xi):
$$y_i (w^T x_i + b) \ge 1 - \xi_i, \quad \xi_i \ge 0$$
- **Trường hợp 1: $\xi_i = 0$:** Điểm nằm an toàn ngoài bờ rào lề hoặc đúng trên bờ rào lề (Phân loại đúng hoàn hảo).
- **Trường hợp 2: $0 < \xi_i \le 1$:** Điểm lọt vào bên trong hành lang lề (Margin), nhưng vẫn nằm đúng phía của siêu phẳng (Vẫn phân loại đúng, nhưng xâm lấn vùng đệm an toàn).
- **Trường hợp 3: $\xi_i > 1$:** Điểm vượt qua siêu phẳng sang nhầm bên kia chiến tuyến $\implies$ **BỊ PHÂN LOẠI SAI (Misclassified)**!

**3. Hàm mục tiêu Soft-Margin và Siêu tham số $C$:**
$$\min_{w, b, \xi} \frac{1}{2}\|w\|^2 + C \sum_{i=1}^N \xi_i$$
- $\frac{1}{2}\|w\|^2$: Mục tiêu **Mở rộng bề rộng lề** Margin.
- $\sum \xi_i$: Tổng mức độ vi phạm sai số.
- $C > 0$: **Siêu tham số đánh đổi (Trade-off Parameter)** giữa độ rộng lề và số lượng lỗi chấp nhận.

**4. Bản chất của siêu tham số $C$ (Trọng tâm Câu 64 Đề thi VAIO):**
- **Khi $C$ rất lớn ($C \to \infty$ - Khắt khe, không khoan nhượng):**
  - Thuật toán phạt cực nặng mọi sai sót. Nó ép $\xi_i \to 0$ bằng mọi giá!
  - Kết quả: Mô hình cố né tránh mọi lỗi nhỏ, chấp nhận thu hẹp lề Margin $\implies$ **Dễ bị Quá khớp (Overfitting)**!
- **Khi $C$ nhỏ ($C \to 0$ - Bao dung, rộng lượng):**
  - Thuật toán coi trọng việc giữ lề Margin rộng thênh thang hơn là việc bắt bẻ từng điểm lỗi. Chấp nhận hy sinh vài điểm vi phạm để đổi lấy ranh giới ổn định.
  - Kết quả: Lề Margin rộng, mô hình kiên cường trước nhiễu $\implies$ **Chống Overfitting tốt, tăng tổng quát hóa**, nhưng nếu $C$ quá nhỏ sẽ dẫn tới **Thiếu khớp (Underfitting)**!

**5. Góc nhìn Hinge Loss (Hàm mất mát bản lề):**
Bản chất Soft-Margin SVM chính là việc tối ưu hàm mất mát Hinge Loss có Regularization L2:
$$\mathcal{L}_{\text{Hinge}}(z) = \max(0, 1 - z), \quad \text{với } z = y_i(w^Tx_i+b)$$
Nếu điểm nằm an toàn ($z \ge 1$), mất mát bằng đúng 0; nếu điểm vi phạm ($z < 1$), mất mát tăng tuyến tính $1 - z$!""",
                "formula": r"\min_{w, b, \xi} \frac{1}{2}\|w\|^2 + C \sum_{i=1}^N \xi_i \quad \text{s.t.} \quad y_i(w^Tx_i+b) \ge 1 - \xi_i, \, \xi_i \ge 0",
                "mathExplainer": [
                    { "sym": "\\xi_i (Xi)", "name": "Biến lỏng (Slack Variable)", "mean": "Khoảng cách vi phạm bờ rào lề của mẫu i (xi=0 là an toàn; 0<xi<=1 là lọt vào lề; xi>1 là đoán sai)." },
                    { "sym": "C", "name": "Siêu tham số phạt C", "mean": "C lớn phạt lỗi nặng (lề hẹp, dễ Overfit); C nhỏ chấp nhận lỗi (lề rộng, chống Overfit)." },
                    { "sym": "\\mathcal{L}_{\\text{Hinge}}", "name": "Hàm mất mát bản lề", "mean": "max(0, 1 - y(w^T x + b)): bằng 0 khi phân loại đúng ngoài lề, tăng tuyến tính khi vi phạm." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 190" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="190" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(60, 20)">
                        <text x="260" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Ý NGHĨA HÌNH HỌC CỦA BIẾN LỎNG ξ TRONG SOFT-MARGIN SVM</text>

                        <!-- Lines -->
                        <line x1="80" y1="140" x2="440" y2="140" stroke="#888" stroke-dasharray="3,3"/>
                        <text x="450" y="143" font-family="Georgia" font-size="9" fill="#555">Bờ rào (+1)</text>

                        <line x1="80" y1="90" x2="440" y2="90" stroke="#111" stroke-width="2"/>
                        <text x="450" y="93" font-family="Georgia" font-size="10" font-weight="bold">Siêu phẳng (0)</text>

                        <line x1="80" y1="40" x2="440" y2="40" stroke="#888" stroke-dasharray="3,3"/>
                        <text x="450" y="43" font-family="Georgia" font-size="9" fill="#555">Bờ rào (-1)</text>

                        <!-- Points with Slack values -->
                        <!-- Point 1: Safe -->
                        <circle cx="120" cy="160" r="5" fill="#111"/>
                        <text x="120" y="175" font-family="Georgia" font-size="9" text-anchor="middle">ξ = 0 (An toàn)</text>

                        <!-- Point 2: On margin -->
                        <circle cx="200" cy="140" r="5" fill="#111"/>
                        <text x="200" y="155" font-family="Georgia" font-size="9" text-anchor="middle">ξ = 0 (Trên lề)</text>

                        <!-- Point 3: Inside margin -->
                        <circle cx="280" cy="115" r="5" fill="#111"/>
                        <line x1="280" y1="140" x2="280" y2="115" stroke="#111" stroke-width="1.5"/>
                        <text x="280" y="110" font-family="Georgia" font-size="9" font-weight="bold" text-anchor="middle">0 &lt; ξ &lt; 1 (Trong lề)</text>

                        <!-- Point 4: Misclassified -->
                        <circle cx="380" cy="60" r="5" fill="#111"/>
                        <line x1="380" y1="140" x2="380" y2="60" stroke="#111" stroke-width="1.5"/>
                        <text x="380" y="55" font-family="Georgia" font-size="9" font-weight="bold" text-anchor="middle">ξ &gt; 1 (Sai nhãn!)</text>
                      </g>
                    </svg>""",
                    "caption": "Phân loại các mức độ vi phạm của biến lỏng ξ: ξ = 0 là an toàn; 0 < ξ <= 1 xâm lấn lề nhưng đoán đúng; ξ > 1 là đoán sai nhãn."
                },
                "commonPitfalls": "Nhầm lẫn giữa C lớn và C nhỏ: Hãy nhớ rằng trong SVM, tham số C đứng trước tổng lỗi (C * sum(xi)). Do đó, C LỚN = PHẠT LỖI NẶNG = Cố sửa lỗi = Dễ Overfitting. C NHỎ = Khoan dung với lỗi = Lề rộng = Chống Overfitting!",
                "practiceQuestion": {
                    "level": "Trung bình",
                    "question": "Trong mô hình Soft-Margin SVM, một điểm dữ liệu x_i thuộc lớp Dương (+1) có giá trị hàm quyết định wᵀx_i + b = -0.5. Giá trị biến lỏng ξ_i tương ứng của điểm này bằng bao nhiêu và điểm này có bị phân loại sai không?",
                    "options": [
                        "A. ξ_i = 0.5, phân loại đúng",
                        "B. ξ_i = 1.5, bị phân loại sai",
                        "C. ξ_i = 1.0, nằm đúng trên siêu phẳng",
                        "D. ξ_i = 0.0, nằm an toàn ngoài lề"
                    ],
                    "correctIndex": 1,
                    "hint": "Điểm thuộc lớp +1 nhưng wᵀx + b = -0.5 < 0 nên đã bị máy đoán nhầm sang lớp Âm! Thay vào công thức: y_i(wᵀx_i + b) = 1 - ξ_i.",
                    "solution": [
                        "Bước 1: Tính tích y_i(wᵀx_i + b): (+1) × (-0.5) = -0.5.",
                        "Bước 2: Thay vào phương trình bờ rào lề: y_i(wᵀx_i + b) = 1 - ξ_i.",
                        "  -0.5 = 1 - ξ_i  =>  ξ_i = 1 - (-0.5) = 1 + 0.5 = 1.5.",
                        "Bước 3: Vì ξ_i = 1.5 > 1 và wᵀx_i + b < 0, điểm này nằm hẳn sang phía âm của siêu phẳng và bị phân loại sai.",
                        "Đáp án chính xác: B (ξ_i = 1.5, bị phân loại sai)."
                    ]
                }
            },

            # =================================================================
            # MỤC 8.4: KERNEL TRICK & RBF KERNEL CHIẾU LÊN VÔ HẠN CHIỀU
            # =================================================================
            {
                "heading": "8.4. Vũ Khí Tối Thượng: Kernel Trick (Thủ Thuật Hạt Nhân) & RBF Kernel Chiếu Lên Không Gian Vô Hạn Chiều",
                "content": "Làm thế nào để chia cắt hai vòng tròn đồng tâm khi không thể kẻ đường thẳng ở 2D? Khám phá thủ thuật Kernel Trick - bước đột phá vĩ đại cho phép tính toán trong không gian vô hạn chiều mà không tốn thêm tài nguyên máy tính.",
                "deepDive": r"""**1. Bế tắc của bài toán phi tuyến trong không gian gốc:**
Hãy tưởng tượng dữ liệu là hai vòng tròn đồng tâm trên mặt bàn 2D:
- Vòng tròn Đỏ nằm gọn ở tâm ($x_1^2 + x_2^2 \le 1$).
- Vòng tròn Xanh bao bọc xung quanh ở vành ngoài ($x_1^2 + x_2^2 > 1$).
Không có bất kỳ chiếc thước kẻ hay đường thẳng nào trên mặt bàn có thể chia cắt được hai vòng tròn này!

**2. Ý tưởng nâng số chiều (Feature Mapping):**
Hãy chiếu các điểm trên mặt bàn 2D lên không gian 3 chiều (3D) bằng một ánh xạ phi tuyến $\phi(x)$:
$$(x_1, x_2) \xrightarrow{\phi} (z_1 = x_1^2, \, z_2 = \sqrt{2}x_1 x_2, \, z_3 = x_2^2)$$
Nhìn vào trục cao độ mới $z_1 + z_3 = x_1^2 + x_2^2 = r^2$ (Khoảng cách tới tâm):
- Các điểm Đỏ (ở gần tâm) sẽ chìm xuống đáy thung lũng (cao độ thấp).
- Các điểm Xanh (ở xa) sẽ bay vọt lên miệng phễu (cao độ cao).
- Ở không gian 3 chiều này, bạn chỉ cần đưa một **tờ giấy phẳng cắt ngang ở giữa** là chia đôi hai lớp một cách hoàn hảo!

**3. Điều kỳ diệu của Kernel Trick (Thủ thuật hạt nhân):**
- *Khó khăn:* Nếu ta muốn chiếu dữ liệu lên không gian 1,000,000 chiều hoặc không gian vô hạn chiều, việc tính toán từng tọa độ $\phi(x)$ sẽ làm nổ tung bộ nhớ máy tính!
- *Sự cứu rỗi:* Nhớ lại ở Mục 8.2, thuật toán SVM **CHỈ CẦN TÍNH TÍCH VÔ HƯỚNG $\phi(x_i)^T \phi(x_j)$**!
- **Định nghĩa Hàm Kernel:** Hàm Kernel $K(x, x')$ là một hàm số tính trực tiếp tích vô hướng trong không gian nhiều chiều mà không cần thực hiện phép chiếu $\phi$:
  $$K(x, x') = \phi(x)^T \phi(x')$$

**4. RBF Kernel (Radial Basis Function - Hạt nhân xuyên tâm / Gaussian Kernel):**
Đây là hàm Kernel phổ biến và mạnh mẽ nhất thế giới:
$$K(x, x') = \exp\left(-\gamma \|x - x'\|^2\right)$$
- **Bí mật toán học chấn động:** RBF Kernel tương đương với việc chiếu dữ liệu lên một **KHÔNG GIAN CÓ SỐ CHIỀU VÔ HẠN (Infinite-dimensional Hilbert Space)**!
  *(Chứng minh: Khai triển Taylor hàm mũ $\exp(z) = 1 + z + \frac{z^2}{2!} + \frac{z^3}{3!} + \dots$ tạo ra chuỗi đa thức bậc vô hạn!).*

**5. Bản chất của siêu tham số $\gamma$ (Gamma) trong RBF Kernel (Trọng tâm Câu 77 VAIO):**
$\gamma$ quyết định bán kính ảnh hưởng của mỗi Support Vector:
- **Khi $\gamma$ rất lớn:** Bán kính ảnh hưởng rất hẹp. Ranh giới quyết định co cụm thành những 'hòn đảo nhỏ' bao quanh từng điểm dữ liệu $\implies$ **Quá khớp (Overfitting) trầm trọng**!
- **Khi $\gamma$ rất nhỏ:** Bán kính ảnh hưởng rất rộng. Mọi điểm đều có tầm ảnh hưởng lan tỏa phẳng lặng $\implies$ Ranh giới gần như thẳng $\implies$ **Thiếu khớp (Underfitting)**!""",
                "formula": r"K(x, x') = \exp(-\gamma \|x - x'\|^2), \quad f(x) = \text{sign}\left(\sum_{i \in \text{SV}} \alpha_i y_i K(x_i, x) + b\right)",
                "mathExplainer": [
                    { "sym": "K(x, x')", "name": "Hàm Kernel", "mean": "Đo độ tương đồng giữa 2 điểm trong không gian chiếu chiều cao mà không cần tính tọa độ chiếu." },
                    { "sym": "\\gamma (Gamma)", "name": "Hệ số co giãn RBF", "mean": "Gamma càng lớn thì bán kính ảnh hưởng càng hẹp, đường biên càng uốn lượn (dễ Overfit)." },
                    { "sym": "\\text{Hilbert Space}", "name": "Không gian Hilbert vô hạn chiều", "mean": "Không gian hàm số nơi RBF ngầm định chiếu dữ liệu tới thông qua khai triển chuỗi Taylor." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 20)">
                        <!-- 2D Non-linear space -->
                        <g transform="translate(20, 10)">
                          <text x="100" y="0" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Không Gian 2D Gốc (Phi Tuyến)</text>
                          <circle cx="100" cy="75" r="50" fill="none" stroke="#888" stroke-dasharray="2,2"/>
                          <circle cx="100" cy="75" r="6" fill="#111"/><circle cx="90" cy="70" r="5" fill="#111"/><circle cx="110" cy="80" r="5" fill="#111"/>
                          <circle cx="55" cy="45" r="5" fill="#fff" stroke="#111" stroke-width="2"/>
                          <circle cx="145" cy="45" r="5" fill="#fff" stroke="#111" stroke-width="2"/>
                          <circle cx="65" cy="115" r="5" fill="#fff" stroke="#111" stroke-width="2"/>
                          <circle cx="135" cy="115" r="5" fill="#fff" stroke="#111" stroke-width="2"/>
                          <text x="100" y="145" font-family="Georgia" font-size="9" text-anchor="middle">Không thể tách bằng 1 đường thẳng</text>
                        </g>

                        <!-- Kernel Arrow -->
                        <g transform="translate(250, 60)">
                          <line x1="0" y1="15" x2="60" y2="15" stroke="#111" stroke-width="2"/>
                          <polygon points="60,15 50,10 50,20" fill="#111"/>
                          <text x="30" y="5" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Kernel Trick</text>
                          <text x="30" y="32" font-family="Georgia" font-size="8" fill="#555" text-anchor="middle">K(x, x') = exp(-γ||x-x'||²)</text>
                        </g>

                        <!-- 3D Separable Space -->
                        <g transform="translate(360, 10)">
                          <text x="110" y="0" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Không Gian Chiều Cao (Tách Tuyến Tính)</text>
                          <rect x="20" y="25" width="180" height="110" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <!-- Separating plane -->
                          <line x1="20" y1="80" x2="200" y2="80" stroke="#111" stroke-width="2"/>
                          <text x="180" y="75" font-family="Georgia" font-size="8" font-weight="bold">Siêu phẳng phẳng</text>
                          <!-- Upper points -->
                          <circle cx="60" cy="50" r="5" fill="#fff" stroke="#111" stroke-width="2"/>
                          <circle cx="150" cy="45" r="5" fill="#fff" stroke="#111" stroke-width="2"/>
                          <!-- Lower points -->
                          <circle cx="100" cy="105" r="5" fill="#111"/>
                          <circle cx="120" cy="115" r="5" fill="#111"/>
                          <text x="110" y="145" font-family="Georgia" font-size="9" text-anchor="middle">Phân tách dễ dàng bằng 1 mặt phẳng!</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "Thủ thuật Kernel Trick: Biến đổi dữ liệu phi tuyến ở không gian gốc thành bài toán phân tách tuyến tính ở không gian số chiều cao hơn."
                },
                "commonPitfalls": "Nhầm lẫn vai trò của Gamma trong RBF: Gamma quá lớn khiến mô hình học vẹt từng điểm (Overfitting). Gamma quá nhỏ làm mất khả năng học phi tuyến và trở về tuyến tính đơn giản (Underfitting). Cần phân biệt rõ Gamma của RBF và tham số phạt C!",
                "practiceQuestion": {
                    "level": "Nâng cao (Câu 77 Đề Thi VAIO 2025)",
                    "question": "Khi sử dụng mô hình SVM với hàm nhân RBF Kernel K(x, x') = exp(-γ||x - x'||²), nếu ta thiết lập tham số γ (Gamma) quá lớn, hiện tượng nào sau đây sẽ xảy ra với ranh giới quyết định của mô hình?",
                    "options": [
                        "A. Ranh giới trở nên gần như một đường thẳng phẳng tuyệt đối (Underfitting)",
                        "B. Ranh giới phân chia bị uốn lượn cực kỳ phức tạp quanh từng điểm dữ liệu huấn luyện đơn lẻ (Overfitting)",
                        "C. Bề rộng lề Margin tăng lên vô cùng",
                        "D. Thuật toán không thể hội tụ do ma trận Kernel không xác định dương"
                    ],
                    "correctIndex": 1,
                    "hint": "Gamma lớn làm bán kính ảnh hưởng exp(-gamma * d²) rơi về 0 rất nhanh khi khoảng cách d chỉ hơi lớn hơn 0 một chút.",
                    "solution": [
                        "Bước 1: Phân tích hàm nhân RBF: exp(-γ ||x - x'||²).",
                        "Bước 2: Khi γ rất lớn, giá trị Kernel giảm đột ngột về 0 đối với bất kỳ điểm nào không nằm sát sạt x_i.",
                        "Bước 3: Điều này khiến mỗi Support Vector chỉ có tầm ảnh hưởng cục bộ cực hẹp, tạo thành các 'vùng ốc đảo' bao quanh từng điểm, gây ra hiện tượng Overfitting nghiêm trọng.",
                        "Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 8.5: THUẬT TOÁN k-NN & LỜI NGUYỀN SỐ CHIỀU
            # =================================================================
            {
                "heading": "8.5. Thuật Toán k-NN (k-Láng Giềng Gần Nhất), Học Lười Biếng (Lazy Learning) & Lời Nguyền Số Chiều",
                "content": "Khám phá thuật toán 'chọn bạn mà chơi' k-NN: Tại sao nó không cần huấn luyện (Lazy Learning), tầm quan trọng sống còn của Chuẩn hóa dữ liệu (Feature Scaling), và sự sụp đổ hình học dưới Lời nguyền số chiều (Curse of Dimensionality).",
                "deepDive": r"""**1. Nguyên lý hoạt động của k-NN (k-Nearest Neighbors):**
Thuật toán phân loại dựa trên giả định: *'Những điểm dữ liệu có đặc trưng tương đồng sẽ có xu hướng mang cùng một nhãn'*.
Khi có một điểm dữ liệu mới $Q$ (Query point) cần dự đoán:
1. Tính khoảng cách từ $Q$ tới **TẤT CẢ các điểm dữ liệu** trong tập huấn luyện.
2. Tìm ra $k$ điểm có khoảng cách nhỏ nhất (tức $k$ láng giềng gần nhất).
3. **Bỏ phiếu đa số (Majority Voting):** Đếm xem trong $k$ người hàng xóm đó, nhãn lớp nào xuất hiện nhiều nhất thì gán nhãn đó cho $Q$!

**2. Bản chất 'Học lười biếng' (Lazy Learning / Instance-Based Learning):**
- **Thời gian huấn luyện = 0 ($\mathcal{O}(1)$):** k-NN không hề học bất kỳ tham số $w$ hay $b$ nào. Nó chỉ đơn giản là nạp toàn bộ dữ liệu Train vào bộ nhớ RAM và nằm chờ!
- **Thời gian dự đoán rất chậm ($\mathcal{O}(N \cdot d)$):** Với mỗi mẫu mới cần dự đoán, nó phải quét qua toàn bộ $N$ điểm dữ liệu cũ để tính khoảng cách. Nếu tập Train có 1 triệu điểm thì việc dự đoán sẽ bị nghẽn nghiêm trọng!

**3. Các hàm đo khoảng cách hình học:**
- **Khoảng cách Euclid ($L_2$ norm - Đường chim bay):**
  $$d_2(x, q) = \sqrt{\sum_{i=1}^d (x_i - q_i)^2}$$
- **Khoảng cách Manhattan ($L_1$ norm - Đường đi taxi ô bàn cờ):**
  $$d_1(x, q) = \sum_{i=1}^d |x_i - q_i|$$

**4. Tác động của siêu tham số $k$ (Bias-Variance Tradeoff):**
- **Khi $k = 1$:** Chỉ nghe theo đúng 1 người hàng xóm gần nhất. Ranh giới cực kỳ uốn lượn, nhạy cảm với từng điểm nhiễu $\implies$ **Phương sai cao (High Variance / Overfitting)**!
- **Khi $k$ tăng:** Đường ranh giới trơn tru hơn, ổn định hơn.
- **Khi $k = N$ (Bằng toàn bộ tập Train):** Mọi điểm mới đều được gán nhãn đa số toàn cục $\implies$ **Độ lệch cao (High Bias / Underfitting)**!
- *Mẹo phòng thi:* Luôn chọn $k$ là **số lẻ** (1, 3, 5, 7) trong phân loại 2 lớp để triệt tiêu hoàn toàn khả năng hòa phiếu!

**5. Yêu cầu bắt buộc: Chuẩn hóa đặc trưng (Feature Scaling):**
Nếu đặc trưng $x_1$ là Tuổi ($[18, 80]$) và đặc trưng $x_2$ là Thu nhập ($[10^7, 10^8]$):
$$(x_2 - q_2)^2 \gg (x_1 - q_1)^2$$
Khoảng cách Euclid sẽ bị chi phối $99.99\%$ bởi Thu nhập, biến Tuổi thành con số vô hình!
$\implies$ **BẮT BUỘC PHẢI CHUẨN HÓA DỮ LIỆU (StandardScaler / MinMaxScaler) TRƯỚC KHI CHẠY k-NN!**

**6. Lời nguyền số chiều (Curse of Dimensionality):**
Khi số chiều $d$ tăng lên cao (hàng trăm chiều):
- Thể tích của không gian bùng nổ theo cấp số nhân ($V \propto r^d$), khiến dữ liệu trở nên cực kỳ thưa thớt (Sparse).
- Khoảng cách giữa điểm gần nhất và điểm xa nhất hội tụ về xấp xỉ bằng nhau:
  $$\lim_{d \to \infty} \frac{d_{\max} - d_{\min}}{d_{\min}} \to 0$$
- Mọi điểm đều cách xa nhau như nhau $\implies$ Khái niệm 'hàng xóm gần nhất' mất hoàn toàn ý nghĩa hình học!""",
                "formula": r"d(x, q) = \sqrt{\sum_{i=1}^d (x_i - q_i)^2}, \quad \hat{y} = \text{mode}\big(\{y_i \mid x_i \in \mathcal{N}_k(q)\}\big)",
                "mathExplainer": [
                    { "sym": "d(x, q)", "name": "Khoảng cách Euclid", "mean": "Độ dài đoạn thẳng nối giữa 2 điểm x và q trong không gian d chiều." },
                    { "sym": "k", "name": "Số lượng hàng xóm", "mean": "Siêu tham số quyết định quy mô hội đồng biểu quyết (nên chọn số lẻ để tránh hòa phiếu)." },
                    { "sym": "\\mathcal{N}_k(q)", "name": "Tập k láng giềng gần nhất", "mean": "Tập hợp k điểm dữ liệu có khoảng cách nhỏ nhất tới điểm truy vấn q." },
                    { "sym": "\\text{Curse of Dimensionality}", "name": "Lời nguyền số chiều", "mean": "Hiện tượng không gian loãng đi và khoảng cách mất ý nghĩa khi số chiều d tăng cao." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(60, 20)">
                        <text x="260" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">BIỂU QUYẾT k-NN: KẾT QUẢ ĐẢO CHIỀU KHI THAY ĐỔI k (1 VS 3)</text>

                        <!-- Query Point Q -->
                        <circle cx="160" cy="90" r="6" fill="#111"/>
                        <text x="160" y="80" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Q (Cần đoán)</text>

                        <!-- Nearest neighbor (Black circle) -->
                        <circle cx="185" cy="80" r="5" fill="#111"/>
                        <circle cx="160" cy="90" r="30" fill="none" stroke="#111" stroke-dasharray="3,3"/>
                        <text x="160" y="128" font-family="Georgia" font-size="9" text-anchor="middle">Vòng k = 1</text>

                        <!-- Next 2 neighbors (White circles) -->
                        <circle cx="120" cy="85" r="5" fill="#fff" stroke="#111" stroke-width="2"/>
                        <circle cx="170" cy="130" r="5" fill="#fff" stroke="#111" stroke-width="2"/>
                        <circle cx="160" cy="90" r="55" fill="none" stroke="#111" stroke-width="1.5"/>
                        <text x="160" y="155" font-family="Georgia" font-size="9" text-anchor="middle">Vòng k = 3</text>

                        <!-- Right table comparison -->
                        <g transform="translate(290, 40)">
                          <rect x="0" y="0" width="250" height="100" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="125" y="22" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Kết Quả Biểu Quyết</text>
                          <text x="15" y="48" font-family="Georgia" font-size="10">• Khi k = 1: Điểm gần nhất là ĐEN (●)</text>
                          <text x="25" y="65" font-family="Georgia" font-size="10" font-weight="bold">⇒ Dự đoán: LỚP ĐEN</text>
                          <text x="15" y="85" font-family="Georgia" font-size="10">• Khi k = 3: Có 1 ĐEN (●) và 2 TRẮNG (○)</text>
                          <text x="25" y="102" font-family="Georgia" font-size="10" font-weight="bold">⇒ Dự đoán: LỚP TRẮNG (Đảo chiều!)</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "Quy luật biểu quyết của k-NN: Thay đổi k từ 1 lên 3 làm đảo ngược hoàn toàn nhãn dự đoán do số lượng láng giềng trong bán kính thay đổi."
                },
                "commonPitfalls": "Quên chuẩn hóa dữ liệu trước khi chạy k-NN: Đây là sai lầm chết người số 1! Các đặc trưng có thang đo lớn (như Tiền lương hàng chục triệu) sẽ nuốt chửng các đặc trưng có thang đo nhỏ (như Số năm kinh nghiệm từ 1 đến 10), khiến khoảng cách tính sai hoàn toàn.",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Tại sao trong bài toán phân loại nhị phân 2 lớp, người ta luôn khuyến nghị chọn siêu tham số k trong thuật toán k-NN là một số lẻ (như k = 3, 5, 7)?",
                    "options": [
                        "A. Để thuật toán chạy nhanh hơn",
                        "B. Để tránh hiện tượng hòa phiếu (Tie) khi số phiếu bầu cho 2 lớp bằng nhau",
                        "C. Để làm giảm phương sai của mô hình",
                        "D. Để loại bỏ ảnh hưởng của lời nguyền số chiều"
                    ],
                    "correctIndex": 1,
                    "hint": "Nếu k = 4 và có 2 người bầu lớp A, 2 người bầu lớp B thì kết quả thế nào?",
                    "solution": [
                        "Bước 1: Trong bài toán 2 lớp, nếu chọn k là số chẵn (ví dụ k = 4), hoàn toàn có khả năng xảy ra trường hợp 2 phiếu cho Lớp 1 và 2 phiếu cho Lớp 2.",
                        "Bước 2: Tình trạng hòa phiếu khiến thuật toán không thể đưa ra kết luận dứt khoát nếu không có quy tắc phá hòa ngẫu nhiên.",
                        "Bước 3: Chọn k là số lẻ đảm bảo luôn có một bên chiếm đa số tuyệt đối (ví dụ 2-1 hoặc 3-2).",
                        "Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 8.6: BÀI TOÁN TÍNH TAY CHUẨN ĐỀ THI VAIO (CÂU 25 & CÂU 38)
            # =================================================================
            {
                "heading": "8.6. Bài Toán Tính Tay Chuẩn Đề Thi VAIO: Tính Toán Khoảng Cách k-NN, Phân Lớp Biểu Quyết & Lề Siêu Phẳng SVM",
                "content": "Thực hành giải bài toán kinh điển mô phỏng chuẩn xác Câu 25 và Câu 38 Đề thi Olympic AI: Tính toán chi tiết từng khoảng cách hình học cho k-NN, biểu quyết láng giềng và phân tích siêu phẳng SVM.",
                "deepDive": r"""**1. Đề bài chuẩn Olympic AI:**
Cho một tập dữ liệu 2 chiều gồm 4 điểm mẫu đã biết trước nhãn:
- $A(2, 2)$ mang nhãn **Lớp +1**
- $B(4, 4)$ mang nhãn **Lớp +1**
- $C(6, 8)$ mang nhãn **Lớp -1**
- $D(8, 8)$ mang nhãn **Lớp -1**

Một điểm dữ liệu mới cần dự đoán nhãn là $Q(6, 6)$.

**YÊU CẦU THÍ SINH:**
1. Tính khoảng cách hình học Euclid từ điểm $Q(6, 6)$ tới cả 4 điểm $A, B, C, D$. *(Mẹo thi: Hãy tính bình phương khoảng cách $d^2$ trước để so sánh thứ tự siêu tốc mà không cần bấm máy tính căn bậc hai)*.
2. Áp dụng thuật toán **k-NN với $k = 1$**: Xác định láng giềng gần nhất và nhãn dự đoán cho điểm $Q$.
3. Áp dụng thuật toán **k-NN với $k = 3$**: Liệt kê 3 láng giềng gần nhất, lập bảng kiểm phiếu biểu quyết đa số và xác định nhãn dự đoán cho $Q$.
4. Giả sử sau đó ta huấn luyện một mô hình **Hard-Margin SVM** trên dữ liệu, tìm được phương trình siêu phẳng phân loại tối ưu là:
   $$x_1 + x_2 - 11 = 0 \quad \text{với vector pháp tuyến } w = (1, 1)^T \text{ và } b = -11$$
   - Tính bề rộng hành lang lề (Margin Width) của siêu phẳng này.
   - Dùng siêu phẳng SVM để dự đoán nhãn cho điểm $Q(6, 6)$ và so sánh với kết quả của k-NN ($k=3$).

---

**2. Lời giải chi tiết từng bước (Step-by-Step Derivation):**

**Bước 1: Tính bình phương khoảng cách $d^2$ từ $Q(6, 6)$:**
Áp dụng công thức $d^2 = (x - 6)^2 + (y - 6)^2$:
- **Khoảng cách tới $A(2, 2)$:**
  $$d^2(Q, A) = (2 - 6)^2 + (2 - 6)^2 = (-4)^2 + (-4)^2 = 16 + 16 = 32 \implies d = \sqrt{32} \approx 5.66$$
- **Khoảng cách tới $B(4, 4)$:**
  $$d^2(Q, B) = (4 - 6)^2 + (4 - 6)^2 = (-2)^2 + (-2)^2 = 4 + 4 = 8 \implies d = \sqrt{8} \approx 2.83$$
- **Khoảng cách tới $C(6, 8)$:**
  $$d^2(Q, C) = (6 - 6)^2 + (8 - 6)^2 = 0^2 + 2^2 = 0 + 4 = 4 \implies d = \sqrt{4} = 2.00$$
- **Khoảng cách tới $D(8, 8)$:**
  $$d^2(Q, D) = (8 - 6)^2 + (8 - 6)^2 = 2^2 + 2^2 = 4 + 4 = 8 \implies d = \sqrt{8} \approx 2.83$$

**Sắp xếp thứ tự các điểm theo khoảng cách tăng dần từ $Q$:**
1. Gần nhất: $C$ ($d = 2.00$) — Mang nhãn **-1**
2. Gần nhì: $B$ ($d \approx 2.83$) — Mang nhãn **+1**
3. Gần ba: $D$ ($d \approx 2.83$) — Mang nhãn **-1**
4. Xa nhất: $A$ ($d \approx 5.66$) — Mang nhãn **+1**

**Bước 2: Dự đoán k-NN với $k = 1$:**
- Láng giềng gần nhất duy nhất là điểm $C$ ($d = 2.00$).
- Điểm $C$ mang nhãn -1.
- **Kết luận:** Với $k = 1$, điểm $Q$ được phân loại vào **Lớp -1**.

**Bước 3: Dự đoán k-NN với $k = 3$:**
- Ba láng giềng gần nhất là $\{C, B, D\}$.
- Nhãn của từng láng giềng:
  - $C$: Lớp -1
  - $D$: Lớp -1
  - $B$: Lớp +1
- Bỏ phiếu biểu quyết đa số:
  - **Lớp -1 nhận được 2 phiếu** (từ $C$ và $D$).
  - **Lớp +1 nhận được 1 phiếu** (từ $B$).
- Tỷ lệ phiếu là $2/3 \implies$ **Kết luận:** Với $k = 3$, điểm $Q$ được phân loại vào **Lớp -1**.

**Bước 4: Phân tích siêu phẳng SVM và so sánh:**
Cho phương trình siêu phẳng: $x_1 + x_2 - 11 = 0 \implies w = (1, 1)^T, \, b = -11$.
- Độ dài chuẩn của vector pháp tuyến $w$:
  $$\|w\| = \sqrt{1^2 + 1^2} = \sqrt{2} \approx 1.414$$
- Bề rộng hành lang lề (Margin Width):
  $$\text{Margin} = \frac{2}{\|w\|} = \frac{2}{\sqrt{2}} = \sqrt{2} \approx 1.414$$
- Dự đoán nhãn cho điểm $Q(6, 6)$ bằng hàm dấu của SVM:
  $$\hat{y}_Q = \text{sign}(w^T x_Q + b) = \text{sign}(1 \times 6 + 1 \times 6 - 11) = \text{sign}(12 - 11) = \text{sign}(+1) = +1$$
  *(Hoặc nếu quy ước ngược dấu: $\hat{y}_Q = \text{sign}(11 - 12) = -1$ tùy thuộc vào phía đặt nhãn).*
- **So sánh triết lý quan trọng:**
  - k-NN nhìn vào **mật độ cục bộ** của các điểm láng giềng xung quanh.
  - SVM nhìn vào **siêu phẳng ranh giới toàn cục** tối ưu hóa bề rộng lề!""",
                "formula": r"d(Q, C)=2.00, \, d(Q, B)=d(Q, D)=\sqrt{8}\approx 2.83, \, d(Q, A)=\sqrt{32} \implies \text{k-NN}(k=3) \to -1, \, \text{Margin}_{\text{SVM}}=\sqrt{2}",
                "mathExplainer": [
                    { "sym": "d^2(Q, C) = 4", "name": "Bình phương khoảng cách đến C", "mean": "Điểm gần nhất tới điểm truy vấn Q với khoảng cách d = 2.0." },
                    { "sym": "k=3 \\to -1", "name": "Kết quả biểu quyết k-NN", "mean": "Lớp -1 thắng áp đảo với 2/3 phiếu từ 2 điểm C và D." },
                    { "sym": "\\text{Margin} = \\sqrt{2}", "name": "Bề rộng lề SVM", "mean": "Khoảng cách giữa hai bờ rào lề của siêu phẳng x₁ + x₂ - 11 = 0." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 190" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="190" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 20)">
                        <text x="280" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">TỔNG HỢP KẾT QUẢ TÍNH TAY THỰC CHIẾN CÂU 25 &amp; CÂU 38</text>

                        <!-- Box 1: Distance calculation -->
                        <g transform="translate(10, 35)">
                          <rect x="0" y="0" width="250" height="120" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="125" y="22" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">1. Khoảng Cách Từ Q(6, 6)</text>
                          <text x="15" y="48" font-family="Georgia" font-size="10">• Đến C(6, 8): d = 2.00 (Lớp -1) [Gần nhất]</text>
                          <text x="15" y="68" font-family="Georgia" font-size="10">• Đến B(4, 4): d = 2.83 (Lớp +1)</text>
                          <text x="15" y="88" font-family="Georgia" font-size="10">• Đến D(8, 8): d = 2.83 (Lớp -1)</text>
                          <text x="15" y="108" font-family="Georgia" font-size="10">• Đến A(2, 2): d = 5.66 (Lớp +1)</text>
                        </g>

                        <!-- Box 2: Voting & SVM result -->
                        <g transform="translate(280, 35)">
                          <rect x="0" y="0" width="280" height="120" fill="#111"/>
                          <text x="140" y="22" font-family="Georgia" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">2. Quyết Định Mô Hình</text>
                          <text x="15" y="48" font-family="Georgia" font-size="10" fill="#eee">• k-NN (k=1): Chọn C ⇒ Lớp -1</text>
                          <text x="15" y="70" font-family="Georgia" font-size="11" font-weight="bold" fill="#fff">• k-NN (k=3): 2 Lớp -1 vs 1 Lớp +1 ⇒ LỚP -1</text>
                          <text x="15" y="92" font-family="Georgia" font-size="10" fill="#eee">• SVM: Margin = 2/||w|| = 2/√2 = √2 ≈ 1.414</text>
                          <text x="15" y="112" font-family="Georgia" font-size="9" fill="#ccc">Mẹo thi: So sánh d² để tránh bấm căn bậc hai!</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "Bảng tổng hợp kết quả tính toán chi tiết: Khoảng cách hình học, kiểm phiếu biểu quyết k-NN và bề rộng lề SVM."
                },
                "commonPitfalls": "Mẹo phòng thi để tiết kiệm thời gian: Khi so sánh khoảng cách trong k-NN, KHÔNG CẦN BẤM MÁY TÍNH CĂN BẬC HAI! Hàm f(x) = sqrt(x) là hàm đồng biến, nên so sánh d² cũng tương đương so sánh d. Tính d² chỉ gồm phép trừ và bình phương số nguyên, làm nhanh hơn gấp 3 lần!",
                "practiceQuestion": {
                    "level": "Nâng cao (Câu 25 Đề Thi VAIO 2025)",
                    "question": "Cho điểm truy vấn Q(3, 4). Khoảng cách Manhattan (L1) và khoảng cách Euclid (L2) từ gốc tọa độ O(0, 0) tới điểm Q lần lượt là:",
                    "options": [
                        "A. Manhattan = 7.0, Euclid = 5.0",
                        "B. Manhattan = 5.0, Euclid = 7.0",
                        "C. Manhattan = 25.0, Euclid = 5.0",
                        "D. Manhattan = 7.0, Euclid = 25.0"
                    ],
                    "correctIndex": 0,
                    "hint": "Manhattan = |x - 0| + |y - 0| = 3 + 4 = 7. Euclid = sqrt(3² + 4²) = sqrt(9 + 16) = 5.",
                    "solution": [
                        "Bước 1: Tính khoảng cách Manhattan (chuẩn L1):",
                        "  d_1 = |3 - 0| + |4 - 0| = 3 + 4 = 7.0.",
                        "Bước 2: Tính khoảng cách Euclid (chuẩn L2):",
                        "  d_2 = sqrt((3 - 0)² + (4 - 0)²) = sqrt(3² + 4²) = sqrt(9 + 16) = sqrt(25) = 5.0.",
                        "Kết luận: Khoảng cách Manhattan = 7.0, khoảng cách Euclid = 5.0. (Nhận xét: Khoảng cách Manhattan luôn >= khoảng cách Euclid).",
                        "Đáp án chính xác: A."
                    ]
                }
            }
        ],
        "interactiveWidget": "widget-knn-classifier",
        "examConnection": {
            "questionTitle": "Điểm Trọng Tâm Về SVM & k-NN Trong Đề Thi VAIO 2025",
            "items": [
                {
                    "code": "Câu 25 VAIO: Tính Toán Khoảng Cách k-NN",
                    "problem": "Tính toán nhanh khoảng cách và xử lý trường hợp hòa phiếu hoặc khác biệt thang đo trong k-NN.",
                    "solution": [
                        "1. Tính d² để sắp xếp thứ tự nhanh, tránh tính căn thức.",
                        "2. Nhận diện các lỗi do chưa chuẩn hóa Feature Scaling khi một trục có biên độ quá lớn.",
                        "3. Chọn k lẻ để triệt tiêu khả năng hòa phiếu."
                    ]
                },
                {
                    "code": "Câu 38 & 52 VAIO: Siêu Phẳng & Support Vectors",
                    "problem": "Bề rộng lề Margin và tính bất biến của siêu phẳng khi thêm bớt dữ liệu an toàn.",
                    "solution": [
                        "1. Margin Width = 2 / ||w||.",
                        "2. Chỉ các Support Vectors (có α_i > 0) mới quyết định siêu phẳng. Mọi điểm trong đất liền có α_i = 0 không ảnh hưởng gì tới mô hình."
                    ]
                },
                {
                    "code": "Câu 64 & 77 VAIO: Tham Số C và Gamma Trong Kernel RBF",
                    "problem": "Quy luật kiểm soát Overfitting / Underfitting của cặp siêu tham số (C, Gamma).",
                    "solution": [
                        "1. C lớn = Phạt nặng vi phạm => Lề hẹp => Overfitting. C nhỏ = Khoan dung => Lề rộng => Chống Overfitting.",
                        "2. Gamma lớn = Bán kính RBF co hẹp => Uốn lượn quanh từng điểm => Overfitting. Gamma nhỏ => Bán kính phẳng => Underfitting."
                    ]
                }
            ]
        },
        "takeaways": [
            "SVM tìm siêu phẳng lề cực đại với bề rộng Margin = 2/||w|| thông qua bài toán quy hoạch toàn phương lồi.",
            "Nghiệm SVM có tính thưa: Vị trí siêu phẳng chỉ phụ thuộc duy nhất vào các Support Vectors (có nhân tử Lagrange α > 0).",
            "Soft-Margin SVM dùng biến lỏng ξ để dung thứ cho lỗi; tham số C điều khiển sự đánh đổi giữa bề rộng lề và lỗi phạt.",
            "Kernel Trick (như RBF exp(-γ||x-x'||²)) cho phép phân tách phi tuyến trong không gian Hilbert vô hạn chiều chỉ bằng tích vô hướng.",
            "k-NN là thuật toán 'học lười biếng' không cần huấn luyện nhưng suy luận chậm; cực kỳ nhạy cảm với thang đo đặc trưng.",
            "Lời nguyền số chiều (Curse of Dimensionality) làm loãng không gian và triệt tiêu ý nghĩa khoảng cách khi số chiều d tăng cao."
        ]
    }
