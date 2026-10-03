# -*- coding: utf-8 -*-
"""
upgrade_lesson_5.py - Masterpiece Lesson 5 for VAIO 2025 AI Olympiad
Chủ đề: Hồi Quy Tuyến Tính (Linear Regression) & Regularization (Lasso, Ridge, ElasticNet)
Toàn diện từ con số 0 đến làm chủ sâu sắc.

Tuân thủ nghiêm ngặt chuẩn sư phạm:
Trực giác đời sống -> Bản chất toán học -> Cách thức hoạt động ->
Giải mã ký hiệu cho học sinh lớp 12 -> Ví dụ tính toán bằng số từng bước ->
Cạm bẫy phòng thi -> Câu hỏi trắc nghiệm kiểm tra độ hiểu có lời giải chi tiết.
"""

def get_masterpiece_lesson_5():
    return {
        "id": "lesson-5",
        "title": "5. Hồi Quy Tuyến Tính (Linear Regression) & Regularization",
        "syllabusBadge": "BUỔI 3: HỒI QUY TUYẾN TÍNH & REGULARIZATION",
        "summary": "Mô hình nền tảng của mọi bài toán dự đoán số thực: Dẫn dắt từ phương trình đường thẳng lớp 9, 4 giả định sống còn (LINE) của mô hình thống kê, giải mã hiện tượng Heteroscedasticity, hai con đường tìm nghiệm (Normal Equation vs Gradient Descent), và nghệ thuật co rút trọng số L1 Lasso vs L2 Ridge chống quá khớp.",
        "intuition": {
            "title": "Trực giác thực tế: Sợi dây thun đàn hồi giữ các tham số không bị nổi loạn",
            "content": """Hãy tưởng tượng bạn đang cố gắng vẽ một đường thẳng đi qua một đám mây điểm dữ liệu phân tán trên giấy (ví dụ: mối quan hệ giữa Diện tích nhà và Giá bán).

Nếu bạn để mô hình hoàn toàn tự do điều chỉnh các trọng số $w$, nó sẽ tìm mọi cách uốn éo thành một đường cong zíc-zắc phức tạp bậc 15 để đi qua chính xác từng điểm nhiễu đơn lẻ (hiện tượng Quá khớp - Overfitting)! Khi có một căn nhà mới toanh xuất hiện, mô hình này sẽ dự đoán một con số hoàn toàn trên trời hoặc âm vô lý!

Làm sao để kiềm chế mô hình, buộc nó phải vẽ một đường thẳng trơn tru, đơn giản?
Hãy buộc một **sợi dây thun đàn hồi** nối từ mỗi trọng số $w$ về gốc tọa độ 0:
- Nếu mô hình muốn tăng vọt trọng số $w$ lên rất lớn để chiều chuộng các điểm nhiễu, sợi dây thun sẽ bị kéo căng cực độ và tạo ra một lực cản (Khoản phạt - Penalty) cộng thẳng vào hàm mất mát Loss!
- Mô hình bị ép phải cân nhắc: 'Việc tăng trọng số này có thực sự giúp giảm sai số nhiều đến mức bù lại được lực căng của sợi dây thun hay không?'.
- Nếu thuộc tính đó chỉ là nhiễu vu vơ, mô hình sẽ thả lỏng và kéo trọng số co rút về sát 0!

Sợi dây thun hình thoi kim cương gọi là **Lasso (L1)**: Có khả năng cắt phăng các trọng số của đặc trưng vô dụng về đúng bằng 0 tuyệt đối để tự động lọc biến!
Sợi dây thun hình tròn trơn gọi là **Ridge (L2)**: Co cụm đều tất cả các trọng số về rất nhỏ nhưng không triệt tiêu về 0, giải quyết dứt điểm thảm họa đa cộng tuyến!
Đây chính là nghệ thuật **Regularization (Chính quy hóa / Co rút trọng số)** trong Machine Learning!"""
        },
        "sections": [
            # =================================================================
            # MỤC 5.1: BẢN CHẤT HỒI QUY TUYẾN TÍNH TỪ SỐ 0
            # =================================================================
            {
                "heading": "5.1. Khởi Đầu Từ Con Số 0: Hồi Quy Tuyến Tính Là Gì? Từ Đường Thẳng Lớp 9 Đến Không Gian Đa Chiều",
                "content": "Hồi quy (Regression) là nhiệm vụ dự đoán một giá trị số thực liên tục (giá nhà, nhiệt độ, doanh thu, thời gian chạy). Mô hình đơn giản nhất, cổ xưa nhất nhưng mạnh mẽ nhất chính là Hồi quy tuyến tính.",
                "deepDive": r"""**1. Từ phương trình đường thẳng hình học lớp 9:**
Ở bậc trung học cơ sở, bạn đã quen thuộc với phương trình đường thẳng:
$$y = a x + b$$
- $a$: Hệ số góc (độ dốc của đường thẳng - dốc đứng hay thoai thoải).
- $b$: Tung độ gốc (giao điểm của đường thẳng với trục tung khi $x = 0$).

Trong Machine Learning, ta giữ nguyên bản chất đó nhưng đổi tên ký hiệu để chuẩn hóa theo quốc tế:
$$\hat{y} = w x + b$$
- $x$: Biến độc lập (Feature / Thuộc tính đầu vào - ví dụ: Diện tích nhà tính bằng $m^2$).
- $\hat{y}$ (đọc là *y-mũ*): Giá trị dự đoán đầu ra (Predicted Value - ví dụ: Giá nhà dự đoán tính bằng tỷ VNĐ).
- $w$ (Weight): Trọng số hay Hệ số góc (Slope) của mô hình.
- $b$ (Bias): Độ chệch hay Hệ số chặn (Intercept) của mô hình.

---

**2. Ý nghĩa kinh tế và vật lý của từng tham số (Bắt buộc phải hiểu bản chất):**
- **Ý nghĩa của trọng số $w$:**
  $$w = \frac{\Delta \hat{y}}{\Delta x}$$
  Trọng số $w$ cho biết: **Khi đặc trưng $x$ tăng thêm đúng 1 đơn vị, thì giá trị dự đoán $\hat{y}$ sẽ tăng thêm (hoặc giảm bớt nếu $w < 0$) bao nhiêu đơn vị!**
  *Ví dụ:* Nếu mô hình dự đoán giá nhà là $\hat{y} = 0.05 x + 0.5$ (với $x$ là $m^2$ và $y$ là tỷ VNĐ), thì $w = 0.05$ nghĩa là: Cứ mỗi mét vuông diện tích tăng thêm, giá nhà dự kiến sẽ tăng thêm $0.05$ tỷ (tức 50 triệu VNĐ)!
- **Ý nghĩa của hệ số chặn $b$:**
  Là giá trị cơ sở của $\hat{y}$ khi toàn bộ các đặc trưng đầu vào đều bằng 0 ($x = 0$). Trong ví dụ trên, $b = 0.5$ có thể hiểu là giá trị nền tảng tối thiểu của mảnh đất.

---

**3. Mở rộng lên không gian đa biến (Multiple Linear Regression):**
Trong thực tế, giá nhà không chỉ phụ thuộc vào diện tích ($x_1$), mà còn phụ thuộc vào Số phòng ngủ ($x_2$), Khoảng cách tới trung tâm ($x_3$), Mặt tiền ($x_4$)...
Mô hình mở rộng thành tổ hợp tuyến tính của $d$ đặc trưng:
$$\hat{y} = w_1 x_1 + w_2 x_2 + \dots + w_d x_d + b$$

Biểu diễn gọn gàng bằng **Tích vô hướng hai vector**:
$$\hat{y} = \mathbf{w}^T \mathbf{x} + b \quad \text{với } \mathbf{w} = \begin{bmatrix} w_1 \\ w_2 \\ \dots \\ w_d \end{bmatrix}, \; \mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ \dots \\ x_d \end{bmatrix}$$

---

**4. Dạng ma trận cho toàn bộ tập dữ liệu (Matrix Formulation):**
Để xử lý cùng lúc $N$ mẫu dữ liệu, các kỹ sư AI dùng một mẹo đại số tuyệt đẹp: Gộp hệ số chặn $b$ vào thành phần đầu tiên của vector trọng số ($w_0 = b$), và chèn thêm một cột toàn số 1 vào đầu ma trận dữ liệu $\mathbf{X}$:
$$\mathbf{X} = \begin{bmatrix} 1 & x_{11} & x_{12} & \dots & x_{1d} \\ 1 & x_{21} & x_{22} & \dots & x_{2d} \\ \vdots & \vdots & \vdots & \ddots & \vdots \\ 1 & x_{N1} & x_{N2} & \dots & x_{Nd} \end{bmatrix} \in \mathbb{R}^{N \times (d+1)}, \quad \mathbf{w} = \begin{bmatrix} b \\ w_1 \\ \vdots \\ w_d \end{bmatrix} \in \mathbb{R}^{(d+1) \times 1}$$

Khi đó, toàn bộ dự đoán cho $N$ mẫu được tính trong **ĐÚNG MỘT PHÉP NHÂN MA TRẬN DUY NHẤT**:
$$\hat{\mathbf{y}} = \mathbf{X} \mathbf{w} \in \mathbb{R}^{N \times 1}$$""",
                "formula": r"\hat{y} = \mathbf{w}^T \mathbf{x} + b \quad \Longleftrightarrow \quad \hat{\mathbf{y}} = \mathbf{X} \mathbf{w}",
                "mathExplainer": [
                    { "sym": r"\hat{y} \text{ (y-hat)}", "name": "Giá trị dự đoán", "mean": "Đầu ra ước lượng của mô hình, phân biệt với giá trị nhãn thực tế y (Ground Truth)." },
                    { "sym": r"w_j \text{ (Weight)}", "name": "Trọng số đặc trưng j", "mean": "Mức độ thay đổi của y khi đặc trưng x_j tăng 1 đơn vị và các đặc trưng khác cố định." },
                    { "sym": r"b \text{ (Bias)}", "name": "Độ chệch / Hệ số chặn", "mean": "Giá trị dự đoán cơ sở khi tất cả các đặc trưng đầu vào đều bằng 0." },
                    { "sym": r"\mathbf{X} \in \mathbb{R}^{N \times (d+1)}", "name": "Ma trận thiết kế (Design Matrix)", "mean": "Bảng dữ liệu gồm N hàng (mẫu) và d+1 cột (cột 1 chứa toàn số 1 để nhân với bias b)." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Axes -->
                      <g transform="translate(40, 20)">
                        <line x1="20" y1="130" x2="240" y2="130" stroke="#111" stroke-width="1.5"/>
                        <line x1="20" y1="10" x2="20" y2="130" stroke="#111" stroke-width="1.5"/>
                        <text x="235" y="145" font-family="Georgia" font-size="11">Diện tích x</text>
                        <text x="10" y="15" font-family="Georgia" font-size="11">Giá y</text>

                        <!-- Fitted line y = wx + b -->
                        <line x1="20" y1="105" x2="220" y2="25" stroke="#111" stroke-width="2"/>
                        <text x="215" y="20" font-family="Georgia" font-size="11" font-weight="bold">ŷ = wx + b</text>

                        <!-- Intercept b -->
                        <circle cx="20" cy="105" r="3.5" fill="#111"/>
                        <text x="5" y="108" font-family="Georgia" font-size="11" font-weight="bold">b</text>

                        <!-- Data points with residuals -->
                        <!-- pt 1 -->
                        <circle cx="60" cy="80" r="3.5" fill="#111"/>
                        <line x1="60" y1="80" x2="60" y2="89" stroke="#888" stroke-dasharray="2,2"/>
                        <!-- pt 2 -->
                        <circle cx="100" cy="85" r="3.5" fill="#111"/>
                        <line x1="100" y1="85" x2="100" y2="73" stroke="#888" stroke-dasharray="2,2"/>
                        <!-- pt 3 -->
                        <circle cx="140" cy="50" r="3.5" fill="#111"/>
                        <line x1="140" y1="50" x2="140" y2="57" stroke="#888" stroke-dasharray="2,2"/>
                        <!-- pt 4 -->
                        <circle cx="180" cy="35" r="3.5" fill="#111"/>
                        <line x1="180" y1="35" x2="180" y2="41" stroke="#888" stroke-dasharray="2,2"/>

                        <text x="105" y="65" font-family="Georgia" font-size="9" fill="#555">Residual eᵢ = yᵢ - ŷᵢ</text>
                      </g>

                      <!-- Explanatory Panel -->
                      <g transform="translate(320, 25)">
                        <text x="0" y="20" font-family="Georgia" font-size="12" font-weight="bold">Mục tiêu của Hồi Quy Tuyến Tính:</text>
                        <text x="0" y="45" font-family="Georgia" font-size="11">• Tìm cặp tham số (w, b) sao cho đường thẳng</text>
                        <text x="15" y="65" font-family="Georgia" font-size="11" font-style="italic">đi xuyên qua đám mây điểm dữ liệu tốt nhất.</text>
                        <text x="0" y="92" font-family="Georgia" font-size="11">• 'Tốt nhất' được định nghĩa là: Tổng bình phương</text>
                        <text x="15" y="112" font-family="Georgia" font-size="11">các đoạn thẳng đứt nét (Residuals) là nhỏ nhất!</text>
                        <text x="0" y="138" font-family="Georgia" font-size="10" font-weight="bold">Phương pháp Bình Phương Tối Thiểu (OLS: Ordinary Least Squares)</text>
                      </g>
                    </svg>""",
                    "caption": "Mô hình Hồi quy tuyến tính đơn biến: Tìm đường thẳng ŷ = wx + b sao cho tổng bình phương khoảng cách thẳng đứng (Residuals) từ các điểm tới đường thẳng là nhỏ nhất."
                },
                "commonPitfalls": "Nhầm lẫn giữa khoảng cách vuông góc và khoảng cách thẳng đứng: Nhiều học sinh nhầm rằng OLS đo khoảng cách vuông góc từ điểm tới đường thẳng. SAI! OLS chỉ đo khoảng cách theo TRỤC THẲNG ĐỨNG (trục Y): e_i = y_i - ŷ_i, vì mục tiêu là giảm thiểu sai số dự đoán trên biến mục tiêu Y!",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Một mô hình hồi quy tuyến tính dự đoán lượng tiêu thụ điện của gia đình có phương trình: ŷ = 15.0 × T + 120.0, trong đó T là nhiệt độ trung bình ngoài trời (°C) và ŷ là số số điện (kWh). Hệ số góc w = 15.0 mang ý nghĩa gì?",
                    "options": [
                        "A. Khi nhiệt độ bằng 0°C, lượng điện tiêu thụ là 15 kWh",
                        "B. Cứ khi nhiệt độ ngoài trời tăng thêm 1°C, lượng điện tiêu thụ dự kiến tăng thêm 15 kWh",
                        "C. Lượng điện tiêu thụ trung bình của gia đình luôn là 15 kWh mỗi ngày",
                        "D. Cứ mỗi 15 ngày, nhiệt độ sẽ tăng thêm 1°C"
                    ],
                    "correctIndex": 1,
                    "hint": "Hệ số góc w đo tỷ lệ thay đổi: Δŷ = w × ΔT. Khi ΔT = 1, Δŷ = 15.",
                    "solution": [
                        "Bước 1: Phân tích phương trình ŷ = 15.0 × T + 120.0:",
                        "  - Biến đầu vào: T (Nhiệt độ ngoài trời).",
                        "  - Biến dự đoán: ŷ (Lượng điện tiêu thụ).",
                        "  - Trọng số w = 15.0.",
                        "Bước 2: Theo định nghĩa toán học của hệ số góc: Đạo hàm dŷ / dT = 15.0.",
                        "  Nghĩa là khi nhiệt độ T tăng thêm 1 đơn vị (1°C), lượng điện dự đoán ŷ sẽ tăng thêm 15.0 đơn vị (15 kWh).",
                        "Kết luận: Đáp án đúng là B."
                    ]
                }
            },

            # =================================================================
            # MỤC 5.2: 4 GIẢ ĐỊNH CỐT LÕI & HETEROSCEDASTICITY
            # =================================================================
            {
                "heading": "5.2. Bốn Giả Định Cốt Lõi (L.I.N.E) & Hiện Tượng Phương Sai Không Đồng Nhất (Heteroscedasticity)",
                "content": "Hồi quy tuyến tính không chỉ là một công cụ máy tính để kẻ đường thẳng, mà là một mô hình suy diễn thống kê chuẩn mực. Để các kết luận, khoảng tin cậy 95% và giá trị p-value có giá trị khoa học, dữ liệu bắt buộc phải thỏa mãn 4 giả định sống còn.",
                "deepDive": r"""**1. Bốn giả định kinh điển theo quy tắc nhớ L.I.N.E:**

Mô hình thực tế có dạng: $y = \mathbf{w}^T \mathbf{x} + b + \epsilon$ (với $\epsilon$ là sai số ngẫu nhiên). 4 giả định bao gồm:

1. **L - Linearity (Tính tuyến tính của mối quan hệ):**
   - Mối quan hệ kỳ vọng giữa các biến độc lập $X$ và biến phụ thuộc $y$ phải là tuyến tính: $\mathbb{E}[y|X] = \mathbf{w}^T \mathbf{x} + b$.
   - Nếu dữ liệu thực tế uốn lượn hình sin hoặc hàm mũ mà cố tình ép đường thẳng $\implies$ Mô hình sẽ bị thiên lệch cực lớn (High Bias / Underfitting).

2. **I - Independence (Tính độc lập của các sai số):**
   - Các sai số thặng dư $e_i = y_i - \hat{y}_i$ của từng mẫu dữ liệu phải **hoàn toàn độc lập với nhau**: $\text{Cov}(e_i, e_j) = 0$ với mọi $i \ne j$.
   - *Vi phạm:* Thường gặp trong dữ liệu chuỗi thời gian (Time-series) hoặc chu kỳ kinh tế, nơi sai số của ngày hôm nay có liên quan chặt chẽ tới sai số của ngày hôm qua (hiện tượng Tự tương quan - Autocorrelation).

3. **N - Normality of Residuals (Phân phối chuẩn của sai số):**
   - Các sai số ngẫu nhiên $\epsilon$ phải tuân theo **Phân Phối Chuẩn hình chuông Gauss** với kỳ vọng bằng 0: $\epsilon \sim \mathcal{N}(0, \sigma^2)$.
   - *Cạm bẫy phòng thi:* Giả định phân phối chuẩn là dành cho **SAI SỐ DƯ $\epsilon$**, TUYỆT ĐỐI KHÔNG PHẢI dành cho biến đầu vào $X$! Biến $X$ có thể là nhị phân 0/1, phân phối đều hay bất kỳ hình dạng nào!

4. **E - Equal Variance / Homoscedasticity (Phương sai đồng nhất):**
   - Phương sai của các sai số thặng dư phải giữ nguyên không đổi dọc theo toàn bộ dải giá trị của $X$: $\text{Var}(\epsilon | X) = \sigma^2 = \text{const}$.
   - Dải phân tán của các điểm dữ liệu quanh đường hồi quy phải có độ dày đồng đều như một dải băng song song!

---

**2. Thảm họa Phương sai không đồng nhất (Heteroscedasticity):**
- **Hiện tượng:** Khi giá trị $X$ hoặc $\hat{y}$ càng lớn, độ phân tán của sai số càng **PHÌNH TO RA NHƯ CÁI LOA KÈN / CÁI PHỄU** (hoặc co hẹp lại)!
- *Ví dụ đời sống kinh điển:*
  - Khảo sát mối quan hệ giữa Thu nhập ($X$) và Chi tiêu ăn uống ($y$):
  - Người có thu nhập 5 triệu/tháng: Chi tiêu bắt buộc phải dao động hẹp trong khoảng 3 - 4.5 triệu (độ phân tán rất nhỏ).
  - Người có thu nhập 100 triệu/tháng: Có người chỉ tiêu 10 triệu, nhưng có người tiêu 80 triệu (độ phân tán cực kỳ khổng lồ!).
- **Hậu quả nguy hiểm trong AI & Thống kê:**
  - Đường thẳng hồi quy OLS tuy vẫn không bị lệch tâm, nhưng các ước lượng về **Sai số chuẩn (Standard Errors)** của trọng số sẽ bị SAI HOÀN TOÀN!
  - Khoảng tin cậy $95\%$ và các kiểm định giả thuyết thống kê (t-test, F-test, p-value) trở nên vô giá trị, khiến mô hình đưa ra những kết luận sai lệch nghiêm trọng!
- **Cách khắc phục:** Lấy hàm logarit $\ln(y)$, biến đổi căn bậc hai $\sqrt{y}$, hoặc biến đổi Box-Cox để nén độ phân tán lại.

---

**3. Vấn đề Đa cộng tuyến (Multicollinearity):**
- Xảy ra khi hai hoặc nhiều biến độc lập $X_i, X_j$ có mối tương quan tuyến tính rất mạnh với nhau (ví dụ: đưa cả $X_1$ là Diện tích $m^2$ và $X_2$ là Diện tích feet vuông vào cùng một mô hình!).
- **Hậu quả:** Ma trận $\mathbf{X}^T \mathbf{X}$ gần như bị suy biến (định thức xấp xỉ 0), việc tính nghịch đảo $(\mathbf{X}^T \mathbf{X})^{-1}$ làm các trọng số bị bùng nổ dao động cực lớn $\implies$ Đây là lý do sống còn cần đến **Ridge Regression (L2)**!""",
                "formula": r"y = \mathbf{w}^T \mathbf{x} + b + \epsilon, \quad \epsilon \stackrel{\text{iid}}{\sim} \mathcal{N}(0, \sigma^2) \quad \text{với } \text{Var}(\epsilon|X) = \sigma^2 \text{ (Homoscedasticity)}",
                "mathExplainer": [
                    { "sym": r"\text{Homoscedasticity}", "name": "Đồng nhất phương sai", "mean": "Sai số có độ phân tán cố định không đổi trên toàn bộ dải giá trị (dải băng đều)." },
                    { "sym": r"\text{Heteroscedasticity}", "name": "Không đồng nhất phương sai", "mean": "Phương sai sai số bị phình to hoặc thu nhỏ theo biến X (hình cái phễu/loa kèn)." },
                    { "sym": r"\text{Multicollinearity}", "name": "Đa cộng tuyến", "mean": "Hiện tượng các biến đầu vào X tương quan mạnh với nhau làm ma trận X^T X khó nghịch đảo." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Left Panel: Homoscedasticity -->
                      <g transform="translate(30, 20)">
                        <text x="110" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Homoscedasticity (Đạt Chuẩn)</text>
                        <line x1="20" y1="130" x2="210" y2="130" stroke="#111" stroke-width="1.5"/>
                        <line x1="20" y1="20" x2="20" y2="130" stroke="#111" stroke-width="1.5"/>
                        <!-- Center line -->
                        <line x1="30" y1="100" x2="200" y2="40" stroke="#111" stroke-width="2"/>
                        <!-- Parallel bounds -->
                        <line x1="30" y1="80" x2="200" y2="20" stroke="#888" stroke-dasharray="2,2"/>
                        <line x1="30" y1="120" x2="200" y2="60" stroke="#888" stroke-dasharray="2,2"/>
                        <!-- Points -->
                        <circle cx="50" cy="95" r="3" fill="#111"/><circle cx="70" cy="82" r="3" fill="#111"/><circle cx="100" cy="70" r="3" fill="#111"/>
                        <circle cx="130" cy="65" r="3" fill="#111"/><circle cx="160" cy="50" r="3" fill="#111"/><circle cx="185" cy="48" r="3" fill="#111"/>
                        <text x="110" y="152" font-family="Georgia" font-size="10" text-anchor="middle">Độ dày sai số đều đặn như dải băng</text>
                      </g>

                      <!-- Right Panel: Heteroscedasticity -->
                      <g transform="translate(340, 20)">
                        <text x="110" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Heteroscedasticity (Lỗi Vi Phạm)</text>
                        <line x1="20" y1="130" x2="210" y2="130" stroke="#111" stroke-width="1.5"/>
                        <line x1="20" y1="20" x2="20" y2="130" stroke="#111" stroke-width="1.5"/>
                        <!-- Center line -->
                        <line x1="30" y1="100" x2="200" y2="40" stroke="#111" stroke-width="2"/>
                        <!-- Funnel bounds -->
                        <line x1="30" y1="95" x2="200" y2="10" stroke="#888" stroke-dasharray="2,2"/>
                        <line x1="30" y1="105" x2="200" y2="70" stroke="#888" stroke-dasharray="2,2"/>
                        <!-- Points with widening spread -->
                        <circle cx="45" cy="98" r="3" fill="#111"/><circle cx="65" cy="92" r="3" fill="#111"/>
                        <circle cx="110" cy="82" r="3" fill="#111"/><circle cx="120" cy="60" r="3" fill="#111"/>
                        <circle cx="170" cy="22" r="3" fill="#111"/><circle cx="185" cy="65" r="3" fill="#111"/><circle cx="195" cy="30" r="3" fill="#111"/>
                        <text x="110" y="152" font-family="Georgia" font-size="10" text-anchor="middle">Sai số phình to thành hình cái phễu</text>
                      </g>
                    </svg>""",
                    "caption": "Đối chiếu trực quan giữa Phương sai đồng nhất (Homoscedasticity) chuẩn mực và Phương sai không đồng nhất (Heteroscedasticity) hình cái phễu làm sai lệch khoảng tin cậy."
                },
                "commonPitfalls": "Cạm bẫy 'Phân phối chuẩn của dữ liệu X': Trong các câu hỏi lý thuyết trắc nghiệm, đề thi thường bẫy câu hỏi: 'Hồi quy tuyến tính bắt buộc biến đầu vào X phải có phân phối chuẩn?'. Hãy khẳng định ngay: SAI! Biến X không cần phân phối chuẩn. Chỉ có SAI SỐ DƯ (Residuals e = y - ŷ) mới cần tuân theo phân phối chuẩn N(0, σ²)!",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Trong phân tích hồi quy tuyến tính, một nhà khoa học dữ liệu vẽ biểu đồ phần dư (Residual Plot) giữa giá trị dự đoán ŷ và sai số thặng dư e. Anh nhận thấy khi ŷ càng lớn, các điểm sai số càng tỏa rộng ra hai phía tạo thành hình cái phễu (funnel shape). Hiện tượng này được gọi là gì?",
                    "options": [
                        "A. Đa cộng tuyến hoàn hảo (Perfect Multicollinearity)",
                        "B. Phương sai không đồng nhất (Heteroscedasticity)",
                        "C. Sai số tự tương quan bậc một (First-order Autocorrelation)",
                        "D. Hiện tượng dưới khớp (Underfitting)"
                    ],
                    "correctIndex": 1,
                    "hint": "Hình cái phễu (funnel) là dấu hiệu nhận diện đặc trưng của phương sai sai số thay đổi dọc theo trục hoành.",
                    "solution": [
                        "Bước 1: Nhận diện hình dạng biểu đồ phần dư (Residual Plot):",
                        "  - Nếu phương sai đồng nhất (Homoscedasticity): Các điểm phần dư rải đều trong một dải băng nằm ngang có độ rộng không đổi.",
                        "  - Nếu các điểm tỏa rộng dần ra tạo thành hình cái phễu (funnel): Độ phân tán (phương sai) của sai số tăng dần theo giá trị dự đoán.",
                        "Bước 2: Đối chiếu định nghĩa: Đây chính là hiện tượng Heteroscedasticity (Phương sai không đồng nhất).",
                        "Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 5.3: HAI CON ĐƯỜNG TÌM LỜI GIẢI
            # =================================================================
            {
                "heading": "5.3. Hai Con Đường Tìm Nghiệm Tối Ưu: Phương Trình Pháp Tuyến (Normal Equation) vs Gradient Descent",
                "content": "Để tìm bộ trọng số w sao cho tổng bình phương sai số là nhỏ nhất, toán học cung cấp cho chúng ta hai con đường hoàn toàn khác biệt: Một bước giải tích ăn ngay (Normal Equation) hoặc từng bước hạ dốc lặp đi lặp lại (Gradient Descent).",
                "deepDive": r"""**1. Con đường 1: Phương trình giải tích đóng (The Normal Equation):**

Hàm mất mát bình phương tối thiểu (OLS Loss) dạng ma trận:
$$\mathcal{L}(\mathbf{w}) = \frac{1}{2} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 = \frac{1}{2} (\mathbf{X}\mathbf{w} - \mathbf{y})^T (\mathbf{X}\mathbf{w} - \mathbf{y})$$

Khai triển đại số ma trận:
$$\mathcal{L}(\mathbf{w}) = \frac{1}{2} \left( \mathbf{w}^T \mathbf{X}^T \mathbf{X} \mathbf{w} - 2 \mathbf{y}^T \mathbf{X} \mathbf{w} + \mathbf{y}^T \mathbf{y} \right)$$

Để tìm điểm cực tiểu toàn cục, ta lấy đạo hàm riêng theo vector $\mathbf{w}$ và cho bằng vector $\mathbf{0}$:
$$\nabla_{\mathbf{w}} \mathcal{L} = \mathbf{X}^T \mathbf{X} \mathbf{w} - \mathbf{X}^T \mathbf{y} = \mathbf{0}$$
$$\iff \mathbf{X}^T \mathbf{X} \mathbf{w} = \mathbf{X}^T \mathbf{y}$$

Nhân cả hai vế với ma trận nghịch đảo $(\mathbf{X}^T \mathbf{X})^{-1}$ (nếu ma trận này khả nghịch):
$$\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y}$$

- **Ưu điểm thần kỳ:**
  - **Chính xác tuyệt đối 100%:** Cho ngay nghiệm tối ưu toàn cục chỉ sau đúng 1 dòng code!
  - **Không cần siêu tham số:** Không cần chọn Learning rate $\eta$, không cần chọn Epochs, không cần kiểm tra hội tụ!
- **Nhược điểm chết người:**
  - Để tính $(\mathbf{X}^T \mathbf{X})^{-1}$, máy tính phải tính nghịch đảo một ma trận kích thước $d \times d$ (với $d$ là số đặc trưng).
  - Độ phức tạp tính toán là $\mathcal{O}(d^3)$. Nếu $d = 100,000$ (trong bài toán văn bản hay ảnh), phép tính này đòi hỏi $10^{15}$ phép tính và hàng Terabyte RAM $\implies$ Máy tính treo cứng ngay lập tức!
  - Nếu các đặc trưng bị đa cộng tuyến, ma trận $\mathbf{X}^T \mathbf{X}$ bị suy biến (không khả nghịch), công thức hoàn toàn vô nghiệm!

---

**2. Con đường 2: Thuật toán Gradient Descent (Lặp từng bước):**
Khởi tạo $\mathbf{w}$ ngẫu nhiên và bước từng bước theo hướng ngược gradient:
$$\mathbf{w}_{t+1} = \mathbf{w}_t - \eta \frac{1}{N} \mathbf{X}^T (\mathbf{X}\mathbf{w}_t - \mathbf{y})$$
- **Ưu điểm:** Độ phức tạp mỗi bước chỉ là $\mathcal{O}(N \cdot d)$, chạy cực kỳ mượt mà ngay cả khi $d$ lên tới hàng triệu đặc trưng hoặc dữ liệu có hàng tỷ mẫu!
- **Nhược điểm:** Cần dò tìm tốc độ học $\eta$, phải lặp qua nhiều Epochs.

---

**Bảng so sánh đối đầu chiến lược:**

| Tiêu chí | Normal Equation $(\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$ | Gradient Descent |
| :--- | :--- | :--- |
| **Cách tìm nghiệm** | Giải tích một lần (Closed-form) | Thuật toán lặp qua từng bước |
| **Cần chọn $\eta$ không?** | KHÔNG | CÓ (bắt buộc phải tinh chỉnh $\eta$) |
| **Độ phức tạp tính toán** | $\mathcal{O}(d^3)$ (Cực nặng theo số chiều $d$) | $\mathcal{O}(k \cdot N \cdot d)$ (Tuyến tính theo $d$) |
| **Khi $d$ nhỏ ($d < 2,000$)** | Lựa chọn số 1, nhanh và chính xác tuyệt đối | Chậm hơn, mất công tinh chỉnh |
| **Khi $d$ khổng lồ ($d > 50,000$)** | Tràn RAM, không thể tính nổi | Hoạt động xuất sắc, tiêu chuẩn công nghiệp |""",
                "formula": r"\mathbf{w}^* = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{y} \quad \text{vs} \quad \mathbf{w}_{t+1} = \mathbf{w}_t - \frac{\eta}{N} \mathbf{X}^T (\mathbf{X}\mathbf{w}_t - \mathbf{y})",
                "mathExplainer": [
                    { "sym": r"(\mathbf{X}^T \mathbf{X})^{-1}", "name": "Ma trận nghịch đảo", "mean": "Thành phần nghẽn cổ chai tính toán O(d³), đòi hỏi ma trận vuông X^T X phải khả nghịch." },
                    { "sym": r"\mathbf{X}^T \mathbf{y}", "name": "Vector tương quan", "mean": "Tích giữa ma trận dữ liệu chuyển vị và vector nhãn thực tế." },
                    { "sym": r"\mathcal{O}(d^3)", "name": "Độ phức tạp lập phương", "mean": "Khi số đặc trưng d tăng gấp đôi, thời gian tính nghịch đảo tăng gấp 8 lần (2³ = 8)!" }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Left: Normal Equation -->
                      <g transform="translate(30, 20)">
                        <rect x="0" y="0" width="250" height="140" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="125" y="25" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Normal Equation (Giải Tích)</text>
                        <text x="20" y="55" font-family="Georgia" font-size="11" font-weight="bold">w* = (XᵀX)⁻¹ Xᵀy</text>
                        <text x="20" y="80" font-family="Georgia" font-size="10">• Đúng 1 bước ăn ngay</text>
                        <text x="20" y="100" font-family="Georgia" font-size="10">• Không cần chọn learning rate η</text>
                        <text x="20" y="125" font-family="Georgia" font-size="9" fill="#c00">• Bế tắc khi d > 10,000 do tính O(d³)</text>
                      </g>

                      <!-- Right: Gradient Descent -->
                      <g transform="translate(340, 20)">
                        <rect x="0" y="0" width="250" height="140" fill="#111"/>
                        <text x="125" y="25" font-family="Georgia" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">Gradient Descent (Hạ Dốc)</text>
                        <text x="20" y="55" font-family="Georgia" font-size="11" fill="#fff" font-weight="bold">w ← w - η ∇L</text>
                        <text x="20" y="80" font-family="Georgia" font-size="10" fill="#eee">• Lặp từng bước tiến về đáy</text>
                        <text x="20" y="100" font-family="Georgia" font-size="10" fill="#eee">• Độ phức tạp tuyến tính O(N·d)</text>
                        <text x="20" y="125" font-family="Georgia" font-size="9" fill="#ccc">• Xử lý mượt mà hàng triệu đặc trưng!</text>
                      </g>
                    </svg>""",
                    "caption": "Hai triết lý tìm nghiệm: Normal Equation giải tích 1 bước nhưng nghẽn cổ chai O(d³); Gradient Descent lặp từng bước nhưng mở rộng không giới hạn cho Big Data."
                },
                "commonPitfalls": "Điều kiện để Normal Equation tồn tại nghiệm duy nhất: Ma trận vuông $\\mathbf{X}^T \\mathbf{X}$ phải KHẢ NGHỊCH (Invertible), tức là định thức $\\det(\\mathbf{X}^T \\mathbf{X}) \\ne 0$. Nếu số mẫu ít hơn số đặc trưng ($N < d$) hoặc có hai cột đặc trưng phụ thuộc tuyến tính, $\\mathbf{X}^T \\mathbf{X}$ sẽ bị suy biến và Normal Equation không thể tính được!",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Khi xây dựng mô hình Hồi quy tuyến tính cho tập dữ liệu có N = 50,000 mẫu và số đặc trưng d = 80,000 (dữ liệu túi từ BoW trong văn bản), phương pháp nào sau đây là sự lựa chọn tối ưu nhất để tìm bộ trọng số w?",
                    "options": [
                        "A. Áp dụng phương trình pháp tuyến Normal Equation w = (XᵀX)⁻¹ Xᵀy",
                        "B. Thuật toán Mini-Batch Gradient Descent",
                        "C. Tính định thức ma trận nghịch đảo cấp 80,000 bằng tay",
                        "D. Khởi tạo ngẫu nhiên và không cần tối ưu hóa"
                    ],
                    "correctIndex": 1,
                    "hint": "Số đặc trưng d = 80,000 là cực kỳ lớn. Độ phức tạp tính nghịch đảo ma trận O(d³) sẽ đòi hỏi hàng triệu tỷ phép tính.",
                    "solution": [
                        "Bước 1: Đánh giá kích thước đặc trưng d = 80,000:",
                        "  - Nếu dùng Normal Equation: Cần nghịch đảo ma trận cấp 80,000 × 80,000. Độ phức tạp O(d³) ≈ 80,000³ ≈ 5.12 × 10¹⁴ phép tính, gây tràn RAM và sập hệ thống.",
                        "Bước 2: Gradient Descent chỉ có độ phức tạp O(B · d) trên mỗi mẻ dữ liệu, xử lý nhẹ nhàng và hội tụ ổn định.",
                        "Kết luận: Phải dùng Mini-Batch Gradient Descent. Đáp án đúng là B."
                    ]
                }
            },

            # =================================================================
            # MỤC 5.4: CÁC HÀM MẤT MÁT & HỆ SỐ R-SQUARED
            # =================================================================
            {
                "heading": "5.4. Các Hàm Mất Mát Hồi Quy (MSE, MAE, Huber) & Thước Đo Hệ Số Xác Định R² (R-squared)",
                "content": "Làm thế nào để đánh giá một đường hồi quy khớp dữ liệu tốt đến đâu? Tại sao việc chỉ dùng MSE lại tiềm ẩn rủi ro chết người trước các điểm ngoại lai (Outliers)?",
                "deepDive": r"""**1. Phân tích đối đầu 3 hàm mất mát hồi quy:**

1. **MSE (Mean Squared Error - Sai số bình phương trung bình / $L_2$ Loss):**
   $$\text{MSE} = \frac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2$$
   - **Ưu điểm:** Hàm số lồi trơn nhẵn, có đạo hàm liên tục tại mọi điểm $\implies$ Cực kỳ thân thiện cho Gradient Descent.
   - **Nhược điểm chí mạng:** Do có số mũ bình phương ($^2$), sai số càng lớn thì bị phạt theo hàm số mũ! Nếu trong tập dữ liệu có đúng 1 điểm ngoại lai (Outlier) bị lỗi cảm biến hoặc nhập nhầm số (ví dụ: nhà 3 tỷ gõ nhầm thành 300 tỷ), sai số $297^2 \approx 88,209$ sẽ **kéo lệch toàn bộ đường thẳng hồi quy về phía điểm dị biệt đó**, làm hỏng kết quả dự đoán của 99% các mẫu bình thường còn lại!

2. **MAE (Mean Absolute Error - Sai số tuyệt đối trung bình / $L_1$ Loss):**
   $$\text{MAE} = \frac{1}{N} \sum_{i=1}^N |y_i - \hat{y}_i|$$
   - **Ưu điểm:** Rất kiên cường trước Outliers (Robust to Outliers). Sai số tăng tuyến tính, không bị phóng đại bình phương.
   - **Nhược điểm:** Đạo hàm tại điểm $e = 0$ không tồn tại (đồ thị có góc nhọn chữ V), gradient luôn là hằng số $\pm 1$ dù ở rất gần đáy, khiến thuật toán khó hội tụ êm ái.

3. **Huber Loss (Sự kết hợp tinh hoa):**
   - Được thiết kế để lấy trọn ưu điểm của cả MSE và MAE thông qua ngưỡng ngưỡng $\delta$:
     $$\mathcal{L}_{\delta}(e) = \begin{cases} \frac{1}{2} e^2 & \text{khi } |e| \le \delta \quad (\text{Vùng lỗi nhỏ: hoạt động như MSE}) \\ \delta (|e| - \frac{1}{2}\delta) & \text{khi } |e| > \delta \quad (\text{Vùng lỗi lớn: hoạt động như MAE}) \end{cases}$$
   - Giúp mô hình vừa có đạo hàm trơn tru ở gần cực tiểu, vừa không bị bẻ cong bởi các điểm dị biệt ngoại lai!

---

**2. Thước đo Hệ số xác định $R^2$ (R-squared / Coefficient of Determination):**
Để biết mô hình hồi quy giải thích được bao nhiêu phần trăm sự biến thiên của dữ liệu thực tế, ta dùng chỉ số $R^2$:
$$R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} = 1 - \frac{\sum_{i=1}^N (y_i - \hat{y}_i)^2}{\sum_{i=1}^N (y_i - \bar{y})^2}$$
- $\text{SS}_{\text{res}}$ (Residual Sum of Squares): Tổng bình phương sai số thặng dư của mô hình hồi quy.
- $\text{SS}_{\text{tot}}$ (Total Sum of Squares): Tổng bình phương sai số của một mô hình ngây thơ (Baseline Model) luôn luôn dự đoán bằng giá trị trung bình $\bar{y}$.

**Ý nghĩa các mức giá trị của $R^2$:**
- **$R^2 = 1.0$ (100%):** Đường hồi quy đi qua chính xác tuyệt đối từng điểm dữ liệu, không có chút sai số nào.
- **$R^2 = 0.85$ (85%):** Mô hình giải thích được 85% sự biến động của giá nhà dựa vào các đặc trưng đầu vào; 15% còn lại là do yếu tố ngẫu nhiên khác.
- **$R^2 = 0.0$ (0%):** Mô hình chỉ có khả năng dự đoán tương đương việc đoán bừa giá trị trung bình $\bar{y}$.
- **$R^2 < 0$ (Âm):** Mô hình dự đoán tồi tệ đến mức còn tệ hơn cả việc lấy trung bình $\bar{y}$! (Thường xảy ra khi đánh giá mô hình trên tập Test bị quá khớp nặng).""",
                "formula": r"R^2 = 1 - \frac{\sum_{i=1}^N (y_i - \hat{y}_i)^2}{\sum_{i=1}^N (y_i - \bar{y})^2} \in (-\infty, 1]",
                "mathExplainer": [
                    { "sym": r"\text{SS}_{\text{res}}", "name": "Tổng bình phương sai số mô hình", "mean": "Đo lường lượng thông tin mà mô hình KHÔNG giải thích được (phần dư thừa)." },
                    { "sym": r"\text{SS}_{\text{tot}}", "name": "Tổng bình phương sai số toàn phần", "mean": "Mức độ phân tán tự nhiên của dữ liệu y quanh giá trị trung bình y-ngang." },
                    { "sym": r"R^2", "name": "Hệ số xác định", "mean": "Tỷ lệ phần trăm sự biến thiên của biến mục tiêu y được giải thích bởi các đặc trưng đầu vào X." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Left: Outlier pulling MSE -->
                      <g transform="translate(30, 20)">
                        <text x="110" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Hiệu Ứng Outlier Trên MSE vs MAE</text>
                        <line x1="20" y1="130" x2="220" y2="130" stroke="#111" stroke-width="1.5"/>
                        <line x1="20" y1="20" x2="20" y2="130" stroke="#111" stroke-width="1.5"/>
                        <!-- Cluster points -->
                        <circle cx="40" cy="110" r="3" fill="#111"/><circle cx="60" cy="100" r="3" fill="#111"/>
                        <circle cx="80" cy="95" r="3" fill="#111"/><circle cx="100" cy="85" r="3" fill="#111"/>
                        <!-- Outlier point -->
                        <circle cx="190" cy="25" r="5" fill="#111"/>
                        <text x="180" y="15" font-family="Georgia" font-size="9" fill="#c00" font-weight="bold">Outlier Dị Biệt!</text>
                        <!-- MAE line (robust) -->
                        <line x1="20" y1="120" x2="210" y2="70" stroke="#111" stroke-width="2"/>
                        <text x="215" y="73" font-family="Georgia" font-size="10" font-weight="bold">MAE</text>
                        <!-- MSE line (pulled up) -->
                        <line x1="20" y1="110" x2="210" y2="35" stroke="#888" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <text x="215" y="38" font-family="Georgia" font-size="10" fill="#666">MSE (bị kéo)</text>
                      </g>

                      <!-- Right: R-squared breakdown -->
                      <g transform="translate(340, 20)">
                        <text x="110" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Ý Nghĩa Của Hệ Số R²</text>
                        <rect x="20" y="35" width="200" height="25" fill="#e5e5e5" stroke="#111"/>
                        <rect x="20" y="35" width="160" height="25" fill="#111"/>
                        <text x="100" y="52" font-family="Georgia" font-size="11" fill="#fff" text-anchor="middle">R² = 80% (Giải thích được)</text>
                        <text x="200" y="52" font-family="Georgia" font-size="9" fill="#111" text-anchor="middle">20%</text>

                        <text x="20" y="85" font-family="Georgia" font-size="10">• R² = 1.0: Khớp hoàn hảo 100%</text>
                        <text x="20" y="105" font-family="Georgia" font-size="10">• R² = 0.0: Bằng với việc đoán bừa trung bình</text>
                        <text x="20" y="125" font-family="Georgia" font-size="10">• R² &lt; 0: Tệ hơn cả đoán giá trị trung bình!</text>
                      </g>
                    </svg>""",
                    "caption": "So sánh hàm mất mát trước Outliers: MSE bị điểm dị biệt kéo lệch nghiêm trọng; MAE giữ vững đường hồi quy thực tế."
                },
                "commonPitfalls": "Nhầm lẫn giá trị R² luôn dương: R² trên tập Train của mô hình OLS tuyến tính luôn nằm trong [0, 1]. Tuy nhiên, khi áp dụng mô hình đó lên tập Test (hoặc với mô hình phi tuyến tính), R² HOÀN TOÀN CÓ THỂ BỊ ÂM (R² < 0) nếu tổng bình phương sai số dự đoán lớn hơn phương sai tự nhiên của tập dữ liệu!",
                "practiceQuestion": {
                    "level": "Vận dụng",
                    "question": "Cho một tập dữ liệu nhỏ có các giá trị nhãn thực tế y = [2, 4, 6]. Giá trị trung bình y-ngang = 4. Một mô hình dự đoán ra ŷ = [3, 4, 5]. Hệ số xác định R² của mô hình này bằng bao nhiêu?",
                    "options": [
                        "A. R² = 0.50 (50%)",
                        "B. R² = 0.75 (75%)",
                        "C. R² = 0.25 (25%)",
                        "D. R² = 1.00 (100%)"
                    ],
                    "correctIndex": 1,
                    "hint": "Tính SS_tot = ∑(y_i - 4)² = (2-4)² + (4-4)² + (6-4)². Tính SS_res = ∑(y_i - ŷ_i)² = (2-3)² + (4-4)² + (6-5)². R² = 1 - SS_res / SS_tot.",
                    "solution": [
                        "Bước 1: Tính tổng bình phương toàn phần SS_tot:",
                        "  y-ngang = 4.",
                        "  SS_tot = (2 - 4)² + (4 - 4)² + (6 - 4)² = (-2)² + 0² + 2² = 4 + 0 + 4 = 8.0.",
                        "Bước 2: Tính tổng bình phương phần dư SS_res:",
                        "  e₁ = 2 - 3 = -1 => e₁² = 1",
                        "  e₂ = 4 - 4 = 0  => e₂² = 0",
                        "  e₃ = 6 - 5 = 1  => e₃² = 1",
                        "  SS_res = 1 + 0 + 1 = 2.0.",
                        "Bước 3: Tính hệ số R²:",
                        "  R² = 1 - (SS_res / SS_tot) = 1 - (2.0 / 8.0) = 1 - 0.25 = 0.75 (75%).",
                        "Kết luận: Mô hình giải thích được 75% sự biến động của dữ liệu. Đáp án đúng là B."
                    ]
                }
            },

            # =================================================================
            # MỤC 5.5: BIAS-VARIANCE TRADEOFF & REGULARIZATION
            # =================================================================
            {
                "heading": "5.5. Đánh Đổi Bias - Variance & Kỹ Thuật Co Rút Trọng Số (L1 Lasso, L2 Ridge & ElasticNet)",
                "content": "Tại sao một mô hình học quá giỏi trên tập luyện tập lại thi trượt thảm hại trên tập thi cử thực tế? Làm thế nào các chuẩn độ dài vector L1 và L2 lại có thể biến thành những chiếc cùm khóa chân hiện tượng Quá khớp (Overfitting)?",
                "deepDive": r"""**1. Sự đánh đổi Độ lệch - Phương sai (The Bias - Variance Tradeoff):**
Mọi sai số kiểm tra của một mô hình học máy đều phân rã thành 3 thành phần không thể tách rời:
$$\text{Expected Error} = \text{Bias}^2 + \text{Variance} + \sigma_{\text{noise}}^2$$

- **Bias (Độ lệch / Thiên kiến):**
  - Sai số do các giả định sai lầm hoặc quá đơn giản hóa bài toán.
  - **High Bias $\implies$ Underfitting (Chưa khớp):** Mô hình quá ngô nghê, không học được cấu trúc của dữ liệu (ví dụ: dùng đường thẳng bậc 1 cho dữ liệu hình lượn sóng). Cả Train Loss và Test Loss đều cao chót vót.
- **Variance (Phương sai / Độ nhạy):**
  - Mức độ dao động của mô hình khi được huấn luyện trên các tập dữ liệu khác nhau.
  - **High Variance $\implies$ Overfitting (Quá khớp):** Mô hình quá phức tạp (ví dụ: đa thức bậc 20), học thuộc lòng từng hạt nhiễu của tập Train. Train Loss gần bằng 0 nhưng Test Loss vọt lên mây xanh!
- **Nhiễu không thể giảm thiểu ($\sigma_{\text{noise}}^2$):** Giới hạn tự nhiên của vũ trụ do sai số đo lường.

---

**2. Nghệ thuật Chính quy hóa (Regularization):**
Ý tưởng cốt lõi: Ta cộng thêm một **Khoản phạt độ lớn trọng số (Penalty)** vào hàm mất mát để ép mô hình phải giữ cho các trọng số $\mathbf{w}$ luôn nhỏ và đơn giản:
$$\mathcal{L}_{\text{Reg}}(\mathbf{w}) = \text{MSE}(\mathbf{w}) + \lambda \cdot \Omega(\mathbf{w})$$
- $\lambda \ge 0$ (Lambda): **Siêu tham số điều chỉnh độ căng của hình phạt.**
  - Nếu $\lambda = 0$: Trở về mô hình OLS thông thường (không có phạt, dễ Overfitting).
  - Nếu $\lambda \to \infty$: Hình phạt quá nặng, ép toàn bộ trọng số $\mathbf{w} \to \mathbf{0}$, mô hình biến thành đường thẳng nằm ngang (High Bias / Underfitting).

---

**3. Hồi quy Ridge (L2 Regularization - Chuẩn bình phương):**
Khoản phạt là bình phương chuẩn $L_2$ của vector trọng số:
$$\mathcal{L}_{\text{Ridge}} = \text{MSE} + \lambda \|\mathbf{w}\|_2^2 = \text{MSE} + \lambda \sum_{j=1}^d w_j^2$$
- **Nghiệm giải tích đóng của Ridge:**
  $$\mathbf{w}_{\text{Ridge}} = (\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^T \mathbf{y}$$
  *(Trong đó $\mathbf{I}$ là ma trận đơn vị).*
- **Phép màu của Ridge đối với Đa cộng tuyến:**
  Khi dữ liệu có đa cộng tuyến, $\mathbf{X}^T \mathbf{X}$ không khả nghịch. Nhưng khi cộng thêm $\lambda \mathbf{I}$, ma trận $(\mathbf{X}^T \mathbf{X} + \lambda \mathbf{I})$ **LUÔN LUÔN KHẢ NGHỊCH 100%**!
- **Đặc điểm:** Ridge co nhỏ đều đặn tất cả các trọng số về sát 0, nhưng **KHÔNG BAO GIỜ ép trọng số về đúng bằng 0 tuyệt đối**.

---

**4. Hồi quy Lasso (L1 Regularization - Chuẩn trị tuyệt đối):**
Khoản phạt là chuẩn $L_1$ của vector trọng số:
$$\mathcal{L}_{\text{Lasso}} = \text{MSE} + \lambda \|\mathbf{w}\|_1 = \text{MSE} + \lambda \sum_{j=1}^d |w_j|$$
- **Bản chất hình học tại sao Lasso triệt tiêu trọng số về 0 (Câu hỏi vàng Olympic):**
  - Vùng ràng buộc của Ridge ($w_1^2 + w_2^2 \le C$) là **Đường tròn trơn nhẵn**. Đường đồng mức của hàm Loss tiếp xúc với đường tròn tại một điểm ngẫu nhiên trên cung tròn, nơi cả $w_1$ và $w_2$ đều khác 0.
  - Vùng ràng buộc của Lasso ($|w_1| + |w_2| \le C$) là **Hình thoi kim cương có 4 ĐỈNH NHỌN nằm ngay trên các trục tọa độ**. Đường đồng mức Loss có xác suất cực cao tiếp xúc trúng ngay đỉnh nhọn trên trục tọa độ $\implies$ Tại đỉnh này, **trọng số $w_1 = 0$ tuyệt đối**!
- **Hệ quả cách mạng:** Lasso đóng vai trò như một **Bộ tự động chọn lọc đặc trưng (Feature Selection)**. Nó tự động gạt bỏ các thuộc tính vô dụng bằng cách gán trọng số đúng bằng 0, tạo ra ma trận trọng số thưa thớt (Sparse Model).

---

**5. Hồi quy ElasticNet (Kết hợp cả L1 và L2):**
$$\mathcal{L}_{\text{ElasticNet}} = \text{MSE} + \lambda \left( \alpha \|\mathbf{w}\|_1 + \frac{1-\alpha}{2} \|\mathbf{w}\|_2^2 \right)$$
Khi có một nhóm đặc trưng tương quan mạnh với nhau, Lasso thường chỉ chọn ngẫu nhiên 1 đặc trưng và vứt bỏ các đặc trưng còn lại. ElasticNet dung hòa cả hai: vừa chọn lọc đặc trưng như Lasso, vừa giữ lại tính ổn định nhóm của Ridge!""",
                "formula": r"\mathcal{L}_{\text{Ridge}} = \text{MSE} + \lambda \|\mathbf{w}\|_2^2 \quad \text{vs} \quad \mathcal{L}_{\text{Lasso}} = \text{MSE} + \lambda \|\mathbf{w}\|_1",
                "mathExplainer": [
                    { "sym": r"\lambda \text{ (Lambda)}", "name": "Siêu tham số chính quy hóa", "mean": "Hệ số phạt: λ càng lớn mô hình càng đơn giản (giảm variance, tăng bias)." },
                    { "sym": r"\|\mathbf{w}\|_2^2 = \sum w_j^2", "name": "Chuẩn L2 (Ridge Penalty)", "mean": "Co nhỏ đều các trọng số, giải quyết đa cộng tuyến, không triệt tiêu về 0." },
                    { "sym": r"\|\mathbf{w}\|_1 = \sum |w_j|", "name": "Chuẩn L1 (Lasso Penalty)", "mean": "Ép thẳng các trọng số không quan trọng về đúng bằng 0 (chọn lọc đặc trưng)." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Left Panel: Lasso L1 diamond -->
                      <g transform="translate(60, 20)">
                        <text x="100" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Lasso L1: Hình Thoi Kim Cương</text>
                        <line x1="10" y1="80" x2="190" y2="80" stroke="#888"/>
                        <line x1="100" y1="10" x2="100" y2="150" stroke="#888"/>
                        <polygon points="100,40 140,80 100,120 60,80" fill="none" stroke="#111" stroke-width="2"/>
                        <ellipse cx="145" cy="45" rx="35" ry="25" fill="none" stroke="#777" stroke-dasharray="2,2"/>
                        <circle cx="100" cy="40" r="4.5" fill="#111"/>
                        <text x="100" y="140" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Chạm tại ĐỈNH trục ⇒ w₁ = 0</text>
                        <text x="100" y="155" font-family="Georgia" font-size="9" fill="#555" text-anchor="middle">(Tự động loại bỏ đặc trưng thừa)</text>
                      </g>

                      <!-- Right Panel: Ridge L2 circle -->
                      <g transform="translate(360, 20)">
                        <text x="100" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Ridge L2: Hình Tròn Trơn</text>
                        <line x1="10" y1="80" x2="190" y2="80" stroke="#888"/>
                        <line x1="100" y1="10" x2="100" y2="150" stroke="#888"/>
                        <circle cx="100" cy="80" r="40" fill="none" stroke="#111" stroke-width="2"/>
                        <ellipse cx="145" cy="45" rx="35" ry="25" fill="none" stroke="#777" stroke-dasharray="2,2"/>
                        <circle cx="128" cy="52" r="4.5" fill="#111"/>
                        <text x="100" y="140" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Chạm trên CUNG TRÒN ⇒ w₁, w₂ ≠ 0</text>
                        <text x="100" y="155" font-family="Georgia" font-size="9" fill="#555" text-anchor="middle">(Co nhỏ đều, giải quyết đa cộng tuyến)</text>
                      </g>
                    </svg>""",
                    "caption": "Bản chất hình học giải mã sự khác biệt giữa L1 và L2: Hình thoi L1 có đỉnh nhọn nằm ngay trên trục tọa độ nên tiếp xúc tại điểm có w = 0; đường tròn L2 trơn nhẵn tiếp xúc ngoài trục nên không triệt tiêu về 0."
                },
                "commonPitfalls": "Nhầm lẫn giữa mục đích của L1 và L2: Hãy khắc cốt ghi tâm: Nếu đề bài hỏi 'Phương pháp nào có khả năng tạo ra mô hình thưa thớt (Sparse Model) và tự động lựa chọn đặc trưng (Feature Selection)?', câu trả lời LUÔN LUÔN LÀ L1 LASSO! Ridge (L2) chỉ co nhỏ trọng số chứ không triệt tiêu biến nào về 0.",
                "practiceQuestion": {
                    "level": "Nâng cao",
                    "question": "Trong một bài toán phân tích biểu hiện gen trong y sinh, bạn có 20,000 gen đầu vào nhưng chỉ có 100 bệnh nhân. Bạn biết rằng chỉ có một số ít gen thực sự gây bệnh, đa số còn lại là nhiễu. Thuật toán hồi quy nào sau đây là phù hợp nhất để vừa dự đoán bệnh vừa xác định chính xác danh sách các gen gây bệnh?",
                    "options": [
                        "A. Hồi quy tuyến tính thông thường OLS (Ordinary Least Squares)",
                        "B. Hồi quy Ridge (L2 Regularization)",
                        "C. Hồi quy Lasso (L1 Regularization)",
                        "D. Hồi quy đa thức bậc 5 không có regularization"
                    ],
                    "correctIndex": 2,
                    "hint": "Cần một thuật toán có khả năng ép các trọng số của hàng chục ngàn gen nhiễu về đúng bằng 0 và giữ lại các gen quan trọng.",
                    "solution": [
                        "Bước 1: Phân tích đặc thù dữ liệu: Số đặc trưng (d = 20,000) lớn hơn rất nhiều so với số mẫu (N = 100), dữ liệu có tính chất thưa thớt (sparse).",
                        "Bước 2: Hồi quy tuyến tính thông thường OLS sẽ bị quá khớp nghiêm trọng và ma trận X^T X bị suy biến không khả nghịch.",
                        "Bước 3: Hồi quy Ridge (L2) giữ lại toàn bộ 20,000 gen trong công thức, không thể chỉ ra gen nào gây bệnh.",
                        "Bước 4: Hồi quy Lasso (L1) ép các trọng số của gen không quan trọng về đúng bằng 0, chỉ giữ lại các gen có trọng số khác 0 (tự động lựa chọn đặc trưng).",
                        "Kết luận: Lasso Regression là lựa chọn tối ưu nhất. Đáp án đúng là C."
                    ]
                }
            },

            # =================================================================
            # MỤC 5.6: BÀI TOÁN THỰC HÀNH TÍNH TAY TỪ A ĐẾN Z
            # =================================================================
            {
                "heading": "5.6. Bài Toán Tính Tay Chuẩn Đề Thi VAIO: Tính Hệ Số OLS & Hiệu Ứng Co Rút Ridge",
                "content": "Để tự tin giành trọn điểm trong kỳ thi Olympic AI, hãy cùng thực hành tính toán từng bước phương trình hồi quy tuyến tính cổ điển OLS và phân tích cách trọng số bị co rút khi có Ridge Regularization.",
                "deepDive": r"""**ĐỀ BÀI THỰC HÀNH KINH ĐIỂN:**
Cho tập dữ liệu nhỏ gồm $N = 3$ căn nhà:

| Mẫu nhà | Diện tích $x$ ($100m^2$) | Giá bán thực tế $y$ (Tỷ VNĐ) |
| :---: | :---: | :---: |
| **Nhà 1** | $1.0$ | $2.0$ |
| **Nhà 2** | $2.0$ | $3.0$ |
| **Nhà 3** | $3.0$ | $5.0$ |

Hãy thực hiện tính toán:
1. **Phần 1:** Tìm phương trình hồi quy tuyến tính chuẩn mực $\hat{y} = w x + b$ bằng phương pháp OLS.
2. **Phần 2:** Tính hệ số xác định $R^2$ của mô hình trên tập dữ liệu này.
3. **Phần 3:** Dự đoán giá bán của một căn nhà mới có diện tích $x_{\text{new}} = 4.0$ ($400m^2$).
4. **Phần 4:** Giả sử mô hình hồi quy không có hệ số chặn $b$ ($\hat{y} = w x$). So sánh nghiệm $w$ của OLS và nghiệm $w_{\text{Ridge}}$ khi thêm chuẩn phạt Ridge với $\lambda = 1.0$.

---

**LỜI GIẢI CHI TIẾT TỪNG BƯỚC:**

**PHẦN 1: TÌM HỆ SỐ HỒI QUY OLS BẰNG TAY**
- **Bước 1.1: Tính giá trị trung bình $\bar{x}$ và $\bar{y}$:**
  $$\bar{x} = \frac{1.0 + 2.0 + 3.0}{3} = \frac{6.0}{3} = \mathbf{2.0}$$
  $$\bar{y} = \frac{2.0 + 3.0 + 5.0}{3} = \frac{10.0}{3} \approx \mathbf{3.333}$$

- **Bước 1.2: Lập bảng tính hiệp phương sai và phương sai mẫu:**

| $i$ | $x_i$ | $y_i$ | $x_i - \bar{x}$ | $y_i - \bar{y}$ | $(x_i - \bar{x})^2$ | $(x_i - \bar{x})(y_i - \bar{y})$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | 1.0 | 2.0 | -1.0 | -1.333 | 1.0 | +1.333 |
| 2 | 2.0 | 3.0 | 0.0 | -0.333 | 0.0 | 0.0 |
| 3 | 3.0 | 5.0 | +1.0 | +1.667 | 1.0 | +1.667 |
| **Tổng $\sum$** | | | | | **2.0** | **3.0** |

- **Bước 1.3: Tính hệ số góc $w$:**
  $$w = \frac{\sum_{i=1}^3 (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^3 (x_i - \bar{x})^2} = \frac{3.0}{2.0} = \mathbf{1.5}$$

- **Bước 1.4: Tính hệ số chặn $b$:**
  $$b = \bar{y} - w \bar{x} = \frac{10}{3} - 1.5(2.0) = 3.333 - 3.0 = \frac{1}{3} \approx \mathbf{0.333}$$

- **Kết luận phương trình hồi quy:**
  $$\mathbf{\hat{y} = 1.5 x + 0.333}$$

---

**PHẦN 2: TÍNH HỆ SỐ XÁC ĐỊNH $R^2$**
- **Tính các giá trị dự đoán $\hat{y}_i$ và phần dư $e_i = y_i - \hat{y}_i$:**
  - Nhà 1 ($x=1$): $\hat{y}_1 = 1.5(1) + 0.333 = 1.833 \implies e_1 = 2.0 - 1.833 = +0.167 \implies e_1^2 \approx 0.0278$.
  - Nhà 2 ($x=2$): $\hat{y}_2 = 1.5(2) + 0.333 = 3.333 \implies e_2 = 3.0 - 3.333 = -0.333 \implies e_2^2 \approx 0.1111$.
  - Nhà 3 ($x=3$): $\hat{y}_3 = 1.5(3) + 0.333 = 4.833 \implies e_3 = 5.0 - 4.833 = +0.167 \implies e_3^2 \approx 0.0278$.
- **Tổng bình phương phần dư:**
  $$\text{SS}_{\text{res}} = 0.0278 + 0.1111 + 0.0278 = \mathbf{0.1667}$$
- **Tổng bình phương toàn phần:**
  $$\text{SS}_{\text{tot}} = (2 - 3.333)^2 + (3 - 3.333)^2 + (5 - 3.333)^2 = 1.778 + 0.111 + 2.778 = \mathbf{4.667}$$
- **Hệ số xác định:**
  $$R^2 = 1 - \frac{\text{SS}_{\text{res}}}{\text{SS}_{\text{tot}}} = 1 - \frac{0.1667}{4.667} = 1 - 0.0357 = \mathbf{0.9643 \quad (96.43\%)}$$
  *(Nhận xét: $R^2 = 96.43\%$ cho thấy đường hồi quy khớp gần như hoàn hảo với dữ liệu thực tế!).*

---

**PHẦN 3: DỰ ĐOÁN NHÀ MỚI ($x_{\text{new}} = 4.0$)**
$$\hat{y}_{\text{new}} = 1.5(4.0) + 0.333 = 6.0 + 0.333 = \mathbf{6.333 \text{ tỷ VNĐ}}$$

---

**PHẦN 4: SO SÁNH HIỆU ỨNG CO RÚT CỦA RIDGE REGULARIZATION**
Xét mô hình hồi quy không có hệ số chặn: $\hat{y} = w x$.
- Vector dữ liệu: $\mathbf{x} = [1, 2, 3]^T$, $\mathbf{y} = [2, 3, 5]^T$.
- $\mathbf{x}^T \mathbf{x} = 1^2 + 2^2 + 3^2 = 1 + 4 + 9 = \mathbf{14}$.
- $\mathbf{x}^T \mathbf{y} = 1(2) + 2(3) + 3(5) = 2 + 6 + 15 = \mathbf{23}$.
- **Nghiệm OLS chuẩn:**
  $$w_{\text{OLS}} = \frac{\mathbf{x}^T \mathbf{y}}{\mathbf{x}^T \mathbf{x}} = \frac{23}{14} \approx \mathbf{1.643}$$
- **Nghiệm khi thêm Ridge Penalty với $\lambda = 1.0$:**
  Công thức giải tích: $w_{\text{Ridge}} = \frac{\mathbf{x}^T \mathbf{y}}{\mathbf{x}^T \mathbf{x} + \lambda}$.
  $$w_{\text{Ridge}} = \frac{23}{14 + 1.0} = \frac{23}{15} \approx \mathbf{1.533}$$

**KẾT LUẬN SÂU SẮC:**
Trọng số $w$ đã bị sợi dây thun Ridge co rút từ **$1.643$ xuống còn $1.533$**! Hệ số góc bị ép giảm đi, làm đường hồi quy bớt dốc và ít nhạy cảm hơn trước các biến động nhiễu!""",
                "formula": r"w_{\text{OLS}} = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}, \quad b = \bar{y} - w \bar{x}, \quad w_{\text{Ridge}} = \frac{\mathbf{x}^T \mathbf{y}}{\mathbf{x}^T \mathbf{x} + \lambda}",
                "mathExplainer": [
                    { "sym": r"\sum (x_i - \bar{x})(y_i - \bar{y})", "name": "Hiệp phương sai tử số", "mean": "Đo mức độ đồng biến thiên cùng chiều giữa diện tích và giá nhà." },
                    { "sym": r"\sum (x_i - \bar{x})^2", "name": "Phương sai mẫu mẫu số", "mean": "Độ dàn trải của biến độc lập diện tích x quanh giá trị trung bình." },
                    { "sym": r"\frac{23}{14 + \lambda}", "name": "Mẫu số co rút Ridge", "mean": "Cộng thêm λ vào mẫu số làm phân số nhỏ đi, trực tiếp ép trọng số w co nhỏ lại." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Step 1: OLS Line -->
                      <g transform="translate(30, 20)">
                        <rect x="0" y="0" width="165" height="140" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="82" y="25" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">1. Nghiệm OLS Chuẩn</text>
                        <text x="15" y="52" font-family="Georgia" font-size="11">• w = 3.0 / 2.0 = 1.5</text>
                        <text x="15" y="75" font-family="Georgia" font-size="11">• b = 3.333 - 3.0 = 0.33</text>
                        <text x="15" y="100" font-family="Georgia" font-size="12" font-weight="bold">ŷ = 1.5x + 0.33</text>
                        <text x="15" y="125" font-family="Georgia" font-size="10" fill="#555">R² = 96.43% (Khớp cao)</text>
                      </g>

                      <!-- Arrow 1-2 -->
                      <line x1="205" y1="90" x2="230" y2="90" stroke="#111" stroke-width="2"/>
                      <polygon points="230,90 222,86 222,94" fill="#111"/>

                      <!-- Step 2: Prediction -->
                      <g transform="translate(235, 20)">
                        <rect x="0" y="0" width="165" height="140" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="82" y="25" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">2. Dự Đoán Nhà Mới</text>
                        <text x="15" y="52" font-family="Georgia" font-size="11">• Diện tích x = 4.0</text>
                        <text x="15" y="75" font-family="Georgia" font-size="11">• ŷ = 1.5(4) + 0.333</text>
                        <text x="15" y="100" font-family="Georgia" font-size="13" font-weight="bold">ŷ = 6.33 Tỷ VNĐ</text>
                        <text x="15" y="125" font-family="Georgia" font-size="10" fill="#555">Nội suy &amp; ngoại suy tuyến tính</text>
                      </g>

                      <!-- Arrow 2-3 -->
                      <line x1="410" y1="90" x2="435" y2="90" stroke="#111" stroke-width="2"/>
                      <polygon points="435,90 427,86 427,94" fill="#111"/>

                      <!-- Step 3: Ridge shrinkage -->
                      <g transform="translate(440, 20)">
                        <rect x="0" y="0" width="155" height="140" fill="#111"/>
                        <text x="77" y="25" font-family="Georgia" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">3. Co Rút Ridge (L2)</text>
                        <text x="15" y="52" font-family="Georgia" font-size="11" fill="#eee">• OLS: w = 23/14 ≈ 1.64</text>
                        <text x="15" y="75" font-family="Georgia" font-size="11" fill="#eee">• λ = 1.0 (Phạt L2)</text>
                        <text x="15" y="100" font-family="Georgia" font-size="12" font-weight="bold" fill="#fff">w_Ridge = 23/15 ≈ 1.53</text>
                        <text x="15" y="125" font-family="Georgia" font-size="10" fill="#bbb">Trọng số co rút 6.7%!</text>
                      </g>
                    </svg>""",
                    "caption": "Luồng tính toán thực hành trọn vẹn: Từ tìm hệ số hồi quy chuẩn OLS, tính độ khớp R², ngoại suy mẫu mới đến hiệu ứng co rút trọng số của Ridge Regularization."
                },
                "commonPitfalls": "Quên căn bậc hai khi chuyển đổi giữa R và R²: R² là hệ số xác định (bình phương hệ số tương quan Pearson r trong hồi quy đơn biến). Nếu r = 0.9 thì R² = 0.81 (chứ không phải 0.9). Ngược lại, nếu R² = 0.64 thì hệ số tương quan r có thể là +0.8 hoặc -0.8 tùy thuộc vào dấu của hệ số góc w!",
                "practiceQuestion": {
                    "level": "Nâng cao",
                    "question": "Cho mô hình hồi quy đơn biến không có hệ số chặn ŷ = w x. Dữ liệu huấn luyện có xᵀx = 20 và xᵀy = 50. Nếu áp dụng Ridge Regression với hệ số phạt λ = 5, giá trị trọng số w_Ridge sẽ giảm đi bao nhiêu phần trăm so với trọng số OLS ban đầu?",
                    "options": [
                        "A. Giảm đúng 20%",
                        "B. Giảm đúng 25%",
                        "C. Giảm đúng 10%",
                        "D. Giảm đúng 50%"
                    ],
                    "correctIndex": 0,
                    "hint": "Tính w_OLS = 50 / 20 = 2.5. Tính w_Ridge = 50 / (20 + 5) = 50 / 25 = 2.0. Tỷ lệ giảm = (2.5 - 2.0) / 2.5.",
                    "solution": [
                        "Bước 1: Tính trọng số OLS ban đầu:",
                        "  w_OLS = xᵀy / xᵀx = 50 / 20 = 2.5.",
                        "Bước 2: Tính trọng số khi có Ridge Regularization với λ = 5:",
                        "  w_Ridge = xᵀy / (xᵀx + λ) = 50 / (20 + 5) = 50 / 25 = 2.0.",
                        "Bước 3: Tính tỷ lệ suy giảm của trọng số:",
                        "  Tỷ lệ giảm = (w_OLS - w_Ridge) / w_OLS = (2.5 - 2.0) / 2.5 = 0.5 / 2.5 = 1/5 = 0.20 = 20%.",
                        "Kết luận: Trọng số bị co rút giảm đúng 20%. Đáp án chính xác là A."
                    ]
                }
            }
        ],
        "interactiveWidget": "widget-linear-regression",
        "examConnection": {
            "questionTitle": "Điểm Trọng Tâm Về Hồi Quy & Co Rút Trong Đề Thi VAIO 2025",
            "items": [
                {
                    "code": "4 Giả Định LINE & Heteroscedasticity",
                    "problem": "Khi dữ liệu vi phạm giả định phương sai đồng nhất (xảy ra Heteroscedasticity), điều gì sẽ xảy ra và cách xử lý trong thực tế là gì?",
                    "solution": [
                        "1. Hậu quả: Dù đường hồi quy OLS vẫn không thiên lệch (unbiased), nhưng sai số chuẩn của các hệ số bị tính sai hoàn toàn, khiến các kiểm định thống kê và khoảng tin cậy 95% mất giá trị.",
                        "2. Cách xử lý: Sử dụng biến đổi Logarit (Log Transformation: ln(y)) hoặc biến đổi Box-Cox để nén phương sai, hoặc áp dụng Hồi quy bình phương tối thiểu có trọng số (Weighted Least Squares - WLS)."
                    ]
                },
                {
                    "code": "L1 Lasso vs L2 Ridge",
                    "problem": "Tại sao trong bài toán tuyển chọn đặc trưng gen hoặc từ vựng văn bản thưa thớt, Lasso lại được ưa chuộng tuyệt đối hơn Ridge?",
                    "solution": [
                        "Do hình học góc nhọn của hình thoi chuẩn L1, nghiệm của Lasso tiếp xúc ngay tại các đỉnh trên trục tọa độ, ép thẳng các hệ số của thuộc tính không quan trọng về đúng bằng 0. Ridge chỉ co nhỏ hệ số về gần 0 nhưng vẫn giữ lại tất cả đặc trưng, không có khả năng triệt tiêu biến thừa."
                    ]
                }
            ]
        },
        "takeaways": [
            "Mô hình Hồi quy tuyến tính: ŷ = w^T x + b (đơn biến là đường thẳng, đa biến là siêu phẳng).",
            "4 Giả định cốt lõi L.I.N.E: Tuyến tính, Độc lập sai số, Phân phối chuẩn sai số N(0, σ²), và Phương sai đồng nhất (Homoscedasticity).",
            "Normal Equation: w* = (X^T X)^{-1} X^T y giải tích một bước ăn ngay, nhưng bị nghẽn O(d³) khi số đặc trưng d lớn.",
            "MSE nhạy cảm với Outliers; MAE kiên cường; Huber Loss kết hợp êm ái cả hai.",
            "L1 Lasso ép trọng số về đúng 0 (Feature Selection); L2 Ridge co nhỏ đều các trọng số và giải quyết triệt để thảm họa đa cộng tuyến."
        ]
    }
