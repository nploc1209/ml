# -*- coding: utf-8 -*-
"""
upgrade_lesson_7.py - Masterpiece Lesson 7 for VAIO 2025 AI Olympiad
Chủ đề: Cây Quyết Định (Decision Tree) & Kỹ Thuật Ensemble (Random Forest, XGBoost)
Toàn diện từ con số 0 đến làm chủ sâu sắc.

Tuân thủ nghiêm ngặt chuẩn sư phạm:
Trực giác đời sống -> Bản chất toán học -> Cách thức hoạt động ->
Giải mã ký hiệu cho học sinh lớp 12 -> Ví dụ tính toán bằng số từng bước ->
Cạm bẫy phòng thi -> Câu hỏi trắc nghiệm kiểm tra độ hiểu có lời giải chi tiết.
"""

def get_masterpiece_lesson_7():
    return {
        "id": "lesson-7",
        "title": "7. Cây Quyết Định (Decision Tree) & Kỹ Thuật Ensemble",
        "syllabusBadge": "BUỔI 4 & 6: CÂY QUYẾT ĐỊNH & KỸ THUẬT ENSEMBLE",
        "summary": "Từ trò chơi 20 câu hỏi đến lý thuyết thông tin của Claude Shannon: Hiểu sâu sắc Độ hỗn loạn Entropy, Chỉ số vẩn đục Gini Impurity, Độ lợi thông tin Information Gain trong thuật toán ID3/C4.5/CART, các cơ chế kiểm soát Quá khớp (Pre-pruning và Cost-Complexity Post-pruning), và sức mạnh tối thượng của học kết hợp Ensemble: So sánh toàn diện Bagging (Random Forest, lấy mẫu Out-Of-Bag 36.8%) và Boosting (AdaBoost, Gradient Boosting, XGBoost giảm Bias).",
        "intuition": {
            "title": "Trực giác thực tế: Trò chơi '20 câu hỏi' và Hội đồng 100 vị bác sĩ độc lập",
            "content": """Hãy tưởng tượng bạn đang chơi trò chơi kinh điển '20 câu hỏi' với bạn của mình. Bạn nghĩ trong đầu một loài động vật bí mật, và bạn của bạn chỉ được phép đặt những câu hỏi Đúng/Sai (Yes/No).

Một người chơi thiếu kinh nghiệm sẽ đặt những câu hỏi hú họa: 'Nó có phải con hươu cao cổ không?' - Nếu câu trả lời là 'Không', anh ta vẫn còn hàng triệu loài vật khác phải đoán mò!
Nhưng một người chơi thông minh sẽ đặt những câu hỏi phân loại có tính chiến lược:
1. 'Nó sống trên cạn hay dưới nước?' -> Ngay lập tức loại bỏ 50% số loài vật trên Trái Đất!
2. 'Nó có phải loài đẻ trứng không?' -> Tiếp tục cắt đôi số loài còn lại!
Mỗi câu hỏi thông minh giúp chia đôi không gian tìm kiếm. Chỉ sau đúng 20 câu hỏi nhị phân, anh ta có thể thu hẹp $2^{20} = 1,048,576$ loài vật về đúng 1 loài duy nhất! Đây chính là cách hoạt động của một **Cây Quyết Định (Decision Tree)**!

Nhưng một cái cây đơn lẻ có thể bị 'học vẹt' (Overfitting) và đưa ra những phán đoán phiến diện.
Làm sao để đưa ra quyết định chuẩn xác tuyệt đối?
Hãy thành lập một **Hội đồng gồm 100 chuyên gia độc lập** (mỗi người được học từ các tài liệu khác nhau và có góc nhìn riêng). Sau đó, hãy cho cả 100 người cùng bỏ phiếu biểu quyết đa số! Những sai sót cá nhân ngẫu nhiên sẽ triệt tiêu lẫn nhau, và phán quyết của toàn hội đồng sẽ chuẩn xác đến kinh ngạc!
Đây chính là triết lý vĩ đại của kỹ thuật **Ensemble (Học kết hợp)** và thuật toán **Random Forest (Rừng ngẫu nhiên)**!"""
        },
        "sections": [
            # =================================================================
            # MỤC 7.1: BẢN CHẤT CÂY QUYẾT ĐỊNH & CẤU TRÚC PHÂN CẤP
            # =================================================================
            {
                "heading": "7.1. Khởi Đầu Từ Con Số 0: Cây Quyết Định Là Gì? Trò Chơi 20 Câu Hỏi & Phân Vùng Trực Giao Không Gian",
                "content": "Cây quyết định là mô hình học máy gần gũi nhất với tư duy logic của con người. Thay vì sử dụng các phương trình toán học phức tạp, nó mô hình hóa bài toán dưới dạng một sơ đồ cây các câu hỏi điều kiện If-Else phân cấp.",
                "deepDive": r"""**1. Giải phẫu cấu trúc của một Cây Quyết Định (Decision Tree):**
Khác với cây cối ngoài tự nhiên, Cây quyết định trong khoa học máy tính mọc ngược: Gốc ở trên đỉnh và Lá ở dưới đáy!
- **Nút Gốc (Root Node):** Nút khởi đầu cao nhất, chứa toàn bộ tập dữ liệu huấn luyện $S$ ban đầu. Nơi đặt câu hỏi quan trọng nhất.
- **Nút Quyết Định / Nút Phân Nhánh (Internal / Decision Nodes):** Các nút trung gian kiểm tra một điều kiện trên một đặc trưng cụ thể (ví dụ: $\text{Tuổi} \ge 30?$, $\text{Thu nhập} > 20\text{ triệu}?$).
- **Cành (Branches / Edges):** Các nhánh rẽ tương ứng với câu trả lời (Đúng rẽ trái, Sai rẽ phải).
- **Nút Lá (Leaf Nodes / Terminal Nodes):** Điểm dừng chân cuối cùng, không phân chia thêm nữa.
  - Trong bài toán **Phân loại (Classification):** Nút lá chứa nhãn lớp chiếm đa số trong nút đó.
  - Trong bài toán **Hồi quy (Regression):** Nút lá chứa giá trị trung bình $\bar{y}$ của các mẫu rơi vào nút đó.

**2. Bản chất hình học: Phân vùng trực giao không gian (Axis-Aligned Splits):**
Trong không gian các đặc trưng ($x_1, x_2$), mỗi câu hỏi If-Else tương ứng với việc kẻ một lát cắt thẳng đứng hoặc nằm ngang song song tuyệt đối với các trục tọa độ:
- Lát cắt 1: $x_1 \\le 3.5$ (chia không gian 2D làm 2 nửa trái - phải).
- Lát cắt 2: Tại nửa bên phải, kiểm tra tiếp $x_2 \\le 5.0$ (kẻ đường nằm ngang chia tiếp thành các ô chữ nhật con).
- **Kết quả hình học:** Cây quyết định chia toàn bộ không gian đặc trưng thành tập hợp các siêu khối hộp chữ nhật (Hyper-rectangles) rời nhau.
- **So sánh với SVM và Hồi quy Tuyến tính:**
  - Tuyến tính / SVM: Kẻ một siêu phẳng chéo xiên $w_1 x_1 + w_2 x_2 + b = 0$.
  - Cây quyết định: Kẻ các đường giật cục zíc-zắc dạng bậc thang bám theo các trục tọa độ!

**3. Ưu điểm nổi bật:**
- **Tính giải thích cao (White-box model):** Con người có thể nhìn vào cây và hiểu chính xác 100% tại sao máy lại đưa ra quyết định đó (rất quan trọng trong Y tế và Ngân hàng cấp tín dụng).
- **Không yêu cầu chuẩn hóa dữ liệu:** Không cần Scaling hay Chuẩn hóa Z-score vì phép so sánh $x \\le \\theta$ là bất biến với các phép biến đổi đơn điệu!
- Xử lý mượt mà cả dữ liệu dạng số (Numerical) và dữ liệu dạng phân loại (Categorical).""",
                "formula": r"\hat{y}(x) = \sum_{m=1}^{|T|} c_m \cdot \mathbb{I}(x \in R_m), \quad c_m = \text{mode}(y \in R_m) \text{ hoặc } \text{mean}(y \in R_m)",
                "mathExplainer": [
                    { "sym": "R_m", "name": "Vùng không gian thứ m", "mean": "Một khối hộp chữ nhật con trong không gian đặc trưng tương ứng với một nút lá của cây." },
                    { "sym": "c_m", "name": "Giá trị dự đoán tại lá m", "mean": "Nhãn đa số (phân loại) hoặc giá trị trung bình mẫu (hồi quy) của vùng R_m." },
                    { "sym": "\\mathbb{I}(\\cdot)", "name": "Hàm chỉ thị (Indicator Function)", "mean": "Bằng 1 nếu mẫu x rơi vào vùng R_m, bằng 0 nếu ngược lại." },
                    { "sym": "|T|", "name": "Số lượng nút lá", "mean": "Tổng số lượng vùng phân hoạch không gian được tạo ra bởi cây." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="210" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(30, 20)">
                        <!-- Decision Tree Graph (Left) -->
                        <g transform="translate(20, 10)">
                          <text x="120" y="0" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Cấu Trúc Cây Phân Cấp</text>
                          <!-- Root -->
                          <rect x="70" y="20" width="100" height="28" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="120" y="38" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Tuổi &lt; 30?</text>
                          <!-- Branch left -->
                          <line x1="90" y1="48" x2="40" y2="80" stroke="#111" stroke-width="1.5"/>
                          <text x="50" y="60" font-family="Georgia" font-size="9">Đúng</text>
                          <!-- Leaf 1 -->
                          <rect x="10" y="80" width="65" height="26" fill="#111"/>
                          <text x="42" y="97" font-family="Georgia" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">Lớp A</text>

                          <!-- Branch right -->
                          <line x1="150" y1="48" x2="190" y2="80" stroke="#111" stroke-width="1.5"/>
                          <text x="180" y="60" font-family="Georgia" font-size="9">Sai</text>
                          <!-- Node 2 -->
                          <rect x="150" y="80" width="90" height="28" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="195" y="98" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Lương &gt; 20M?</text>

                          <!-- Leaf 2 & 3 -->
                          <line x1="175" y1="108" x2="140" y2="135" stroke="#111" stroke-width="1.5"/>
                          <rect x="110" y="135" width="60" height="26" fill="#111"/>
                          <text x="140" y="152" font-family="Georgia" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">Lớp B</text>

                          <line x1="215" y1="108" x2="245" y2="135" stroke="#111" stroke-width="1.5"/>
                          <rect x="220" y="135" width="60" height="26" fill="#eee" stroke="#111"/>
                          <text x="250" y="152" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Lớp A</text>
                        </g>

                        <!-- Partition Space (Right) -->
                        <g transform="translate(340, 10)">
                          <text x="120" y="0" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Phân Vùng Trực Giao Trong Không Gian 2D</text>
                          <rect x="20" y="20" width="200" height="140" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <!-- Split 1: x1 < 30 -->
                          <line x1="80" y1="20" x2="80" y2="160" stroke="#111" stroke-width="2"/>
                          <text x="50" y="90" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Lớp A</text>
                          <text x="80" y="175" font-family="Georgia" font-size="9" text-anchor="middle">Tuổi = 30</text>

                          <!-- Split 2: x2 > 20 -->
                          <line x1="80" y1="80" x2="220" y2="80" stroke="#111" stroke-width="2"/>
                          <text x="150" y="55" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Lớp B</text>
                          <text x="150" y="125" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Lớp A</text>
                          <text x="235" y="85" font-family="Georgia" font-size="9">Lương=20M</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "Sự tương đương toán học: Mỗi câu hỏi If-Else trong cây nhị phân tương ứng với một lát cắt phẳng trực giao chia đôi không gian dữ liệu."
                },
                "commonPitfalls": "Nhầm lẫn rằng cây quyết định có thể vẽ đường biên nghiêng chéo: Cây quyết định tiêu chuẩn chỉ chia các điều kiện đơn biến (Univariate Splits: $x_i \\le \\theta$), do đó đường ranh giới của nó luôn vuông góc với các trục tọa độ. Để xấp xỉ một đường chéo $x_1 + x_2 = 1$, cây phải tạo ra rất nhiều lát cắt zíc-zắc hình bậc thang!",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Trong không gian 2 chiều với 2 đặc trưng (x₁, x₂), một cây quyết định có độ sâu bằng 2 (thực hiện đúng 2 phép chia đơn biến liên tiếp) có thể chia không gian dữ liệu thành tối đa bao nhiêu vùng chữ nhật riêng biệt?",
                    "options": [
                        "A. Tối đa 2 vùng",
                        "B. Tối đa 3 vùng",
                        "C. Tối đa 4 vùng",
                        "D. Tối đa 8 vùng"
                    ],
                    "correctIndex": 2,
                    "hint": "Nút gốc chia thành 2 nhánh. Mỗi nhánh con ở tầng 1 lại có thể chia tiếp thành 2 nhánh ở tầng 2. Số lá tối đa của cây nhị phân đầy đủ ở độ sâu d là 2^d.",
                    "solution": [
                        "Bước 1: Nút gốc (độ sâu 0) chia không gian làm 2 nửa.",
                        "Bước 2: Mỗi nút con ở độ sâu 1 tiếp tục chia nửa của nó thành 2 phần nhỏ hơn.",
                        "Bước 3: Tổng số vùng lá tối đa tạo thành là 2^2 = 4 vùng chữ nhật.",
                        "Đáp án chính xác: C (Tối đa 4 vùng)."
                    ]
                }
            },

            # =================================================================
            # MỤC 7.2: ĐỘ HỖN LOẠN ENTROPY & CHỈ SỐ GINI IMPURITY
            # =================================================================
            {
                "heading": "7.2. Thước Đo Độ Thuần Khiết: Độ Hỗn Loạn Entropy (Shannon) & Chỉ Số Vẩn Đục Gini Impurity",
                "content": "Để biết câu hỏi nào là 'tốt nhất' để đặt ở mỗi nút, thuật toán cần một thước đo định lượng mức độ thuần khiết (Purity) của dữ liệu. Hai thước đo kinh điển nhất là Entropy và Gini Impurity.",
                "deepDive": r"""**1. Entropy (Độ Hỗn Loạn Thông Tin - Claude Shannon, 1948):**
- **Trực giác vật lý & đời sống:**
  - Hãy tưởng tượng một chiếc hộp chứa 100 viên bi:
    - Nếu 100 viên đều là màu Đỏ: Bạn thò tay vào bốc, bạn chắc chắn 100% bốc được bi Đỏ. Không có gì bất ngờ $\implies$ **Độ hỗn loạn bằng 0!**
    - Nếu 50 viên Đỏ và 50 viên Xanh: Tỷ lệ 50-50 như tung đồng xu, hoàn toàn không thể đoán trước $\implies$ **Độ hỗn loạn cực đại!**
- **Công thức toán học của Entropy:**
  $$H(S) = - \sum_{i=1}^C p_i \log_2(p_i)$$
  - $C$: Số lượng lớp (với bài toán nhị phân thì $C = 2$).
  - $p_i$: Tỷ lệ mẫu thuộc lớp $i$ trong tập dữ liệu $S$ ($0 \le p_i \le 1$).
  - Đơn vị tính: Khi dùng cơ số $\log_2$, Entropy được đo bằng đơn vị **bit** thông tin.
  - **Quy ước toán học sống còn:** Nếu $p_i = 0$, ta quy ước:
    $$0 \times \log_2(0) = 0$$
    *(Cơ sở giải tích: $\lim_{p \to 0^+} p \log_2 p = 0$ theo quy tắc L'Hôpital).*

- **Khảo sát hàm Entropy nhị phân $H(p) = -p \log_2 p - (1-p) \log_2(1-p)$:**
  - Khi $p = 0$ hoặc $p = 1$ (Thuần khiết tuyệt đối): $H(S) = 0.0$ bit.
  - Khi $p = 0.5$ (Hỗn loạn cực đại):
    $$H(S) = - [ 0.5 \log_2(0.5) + 0.5 \log_2(0.5) ] = - [ 0.5(-1) + 0.5(-1) ] = -(-1.0) = 1.0\text{ bit}$$
  - Đồ thị Entropy là một đường cong hình vòm úp ngược hoàn hảo đối xứng qua điểm $p = 0.5$.

**2. Gini Impurity (Độ Vẩn Đục Gini - Breiman et al., 1984):**
- **Trực giác xác suất:**
  - Giả sử bạn bốc ngẫu nhiên một phần tử trong hộp, và sau đó gán nhãn cho nó một cách ngẫu nhiên theo đúng phân phối xác suất của tập dữ liệu. Xác suất bạn gán SAI nhãn là bao nhiêu? Đó chính là Gini Impurity!
- **Công thức toán học:**
  $$\text{Gini}(S) = 1 - \sum_{i=1}^C p_i^2$$
- **Với bài toán nhị phân gồm hai lớp có xác suất $p$ và $1-p$:**
  $$\text{Gini}(S) = 1 - [p^2 + (1-p)^2] = 1 - [p^2 + 1 - 2p + p^2] = 2p(1-p)$$
  - Khi $p = 0$ hoặc $p = 1$ (Thuần khiết): $\text{Gini}(S) = 0.0$.
  - Khi $p = 0.5$ (Hỗn loạn cực đại): $\text{Gini}(S) = 2 \times 0.5 \times 0.5 = 0.5$.

**3. So sánh đối chiếu toàn diện giữa Entropy và Gini (Điểm cốt tử phòng thi):**
- **Hình dáng đồ thị:** Cả hai đều đạt cực tiểu bằng 0 tại biên ($p=0, p=1$) và đạt cực đại tại tâm ($p=0.5$).
- **Giá trị cực đại:** Entropy cực đại là **1.0 bit**, Gini cực đại là **0.5**.
- **Hiệu năng tính toán (Computational Speed):**
  - Gini chỉ yêu cầu phép nhân và phép cộng: $1 - \sum p_i^2 \implies$ **Tính cực nhanh!**
  - Entropy bắt buộc phải tính logarit tự nhiên/cơ số 2: $\sum p_i \log_2 p_i \implies$ **Tốn kém chi phí CPU!**
  - Vì lý do này, thuật toán CART và thư viện Scikit-Learn chọn **Gini Impurity làm tiêu chuẩn mặc định**.""",
                "formula": r"H(S) = - \sum_{i=1}^C p_i \log_2(p_i), \quad \text{Gini}(S) = 1 - \sum_{i=1}^C p_i^2 = 2p(1-p)",
                "mathExplainer": [
                    { "sym": "H(S)", "name": "Độ hỗn loạn Entropy", "mean": "Thước đo mức độ không chắc chắn thông tin của tập S (cực đại bằng 1.0 khi phân bố 50-50)." },
                    { "sym": "\\text{Gini}(S)", "name": "Độ vẩn đục Gini", "mean": "Xác suất phân loại sai một mẫu nếu gán nhãn ngẫu nhiên theo phân phối (cực đại bằng 0.5)." },
                    { "sym": "p_i", "name": "Tỷ lệ xác suất lớp i", "mean": "Số lượng mẫu thuộc lớp i chia cho tổng số mẫu của nút: N_i / N." },
                    { "sym": "\\log_2", "name": "Hàm Logarit cơ số 2", "mean": "Đơn vị đo lường thông tin dạng nhị phân (bit). log₂(1)=0, log₂(0.5)=-1, log₂(0.25)=-2." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(60, 20)">
                        <text x="260" y="12" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">SO SÁNH ĐỒ THỊ ENTROPY VS GINI IMPURITY</text>
                        <!-- Axis -->
                        <line x1="30" y1="130" x2="430" y2="130" stroke="#111" stroke-width="1.5"/>
                        <line x1="30" y1="20" x2="30" y2="130" stroke="#111" stroke-width="1.5"/>
                        <text x="230" y="148" font-family="Georgia" font-size="10" text-anchor="middle">Xác suất p của Lớp Dương tính (0 → 1)</text>

                        <!-- Curves -->
                        <!-- Entropy (peaks at 1.0 -> y=30) -->
                        <path d="M 30 130 Q 230 10 430 130" fill="none" stroke="#111" stroke-width="2.5"/>
                        <circle cx="230" cy="30" r="4" fill="#111"/>
                        <text x="240" y="32" font-family="Georgia" font-size="10" font-weight="bold">Entropy cực đại = 1.0</text>

                        <!-- Gini (peaks at 0.5 -> y=80) -->
                        <path d="M 30 130 Q 230 65 430 130" fill="none" stroke="#666" stroke-width="2" stroke-dasharray="4,4"/>
                        <circle cx="230" cy="80" r="4" fill="#666"/>
                        <text x="240" y="82" font-family="Georgia" font-size="10" fill="#444">Gini cực đại = 0.5</text>

                        <!-- Legend on right -->
                        <g transform="translate(460, 40)">
                          <line x1="0" y1="10" x2="30" y2="10" stroke="#111" stroke-width="2.5"/>
                          <text x="35" y="14" font-family="Georgia" font-size="10" font-weight="bold">Entropy H(p)</text>
                          <line x1="0" y1="35" x2="30" y2="35" stroke="#666" stroke-width="2" stroke-dasharray="4,4"/>
                          <text x="35" y="39" font-family="Georgia" font-size="10" fill="#444">Gini 2p(1-p)</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "Đồ thị Entropy (đạt đỉnh 1.0) và Gini Impurity (đạt đỉnh 0.5): Cả hai đều đạt cực tiểu 0 khi thuần khiết và cực đại tại p = 0.5."
                },
                "commonPitfalls": "Quên dấu trừ đằng trước công thức Entropy: Vì các xác suất p_i đều nhỏ hơn hoặc bằng 1, nên log₂(p_i) luôn là số ÂM hoặc bằng 0. Nếu không có dấu trừ phía trước tổng, Entropy sẽ bị tính ra số âm, vi phạm bản chất độ hỗn loạn!",
                "practiceQuestion": {
                    "level": "Trung bình",
                    "question": "Một nút trong cây quyết định chứa 10 mẫu dữ liệu, trong đó có 8 mẫu thuộc Lớp 1 và 2 mẫu thuộc Lớp 2. Chỉ số Gini Impurity của nút này bằng bao nhiêu?",
                    "options": [
                        "A. 0.16",
                        "B. 0.32",
                        "C. 0.50",
                        "D. 0.68"
                    ],
                    "correctIndex": 1,
                    "hint": "Tính p₁ = 8/10 = 0.8, p₂ = 2/10 = 0.2. Áp dụng công thức Gini = 1 - (p₁² + p₂²) hoặc Gini = 2 * p₁ * p₂.",
                    "solution": [
                        "Bước 1: Tính tỷ lệ xác suất từng lớp:",
                        "  p₁ = 8 / 10 = 0.8",
                        "  p₂ = 2 / 10 = 0.2",
                        "Bước 2: Thay vào công thức Gini nhị phân:",
                        "  Gini = 1 - (p₁² + p₂²) = 1 - (0.8² + 0.2²) = 1 - (0.64 + 0.04) = 1 - 0.68 = 0.32.",
                        "Cách 2 nhanh hơn: Gini = 2 × p₁ × p₂ = 2 × 0.8 × 0.2 = 0.32.",
                        "Đáp án chính xác: B (0.32)."
                    ]
                }
            },

            # =================================================================
            # MỤC 7.3: THUẬT TOÁN ID3, C4.5, CART & INFORMATION GAIN
            # =================================================================
            {
                "heading": "7.3. Thuật Toán ID3, C4.5 & CART: Độ Lợi Thông Tin (Information Gain) & Cạm Bẫy Của Thuộc Tính ID",
                "content": "Làm thế nào để xây dựng cây quyết định tự động từ dữ liệu? Khám phá thuật toán kinh điển ID3 của Ross Quinlan, công thức Độ Lợi Thông Tin Information Gain, và cách C4.5 giải quyết cạm bẫy thuộc tính ID.",
                "deepDive": r"""**1. Độ Lợi Thông Tin (Information Gain - Thuật toán ID3):**
Mục tiêu của việc phân nhánh là làm cho các nút con có độ hỗn loạn thấp hơn nút cha.
Độ sụt giảm của độ hỗn loạn sau khi chia dữ liệu theo thuộc tính $A$ được gọi là **Information Gain (IG)**:
$$IG(S, A) = H(S) - H(S \mid A)$$
Trong đó:
- $H(S)$: Entropy ban đầu của nút cha trước khi chia.
- $H(S \mid A)$: Entropy có điều kiện (Trung bình có trọng số của Entropy các nhánh con):
  $$H(S \mid A) = \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v)$$
  - $v$: Một giá trị khả dĩ của thuộc tính $A$.
  - $S_v$: Tập các mẫu có thuộc tính $A = v$.
  - $\frac{|S_v|}{|S|}$: Trọng số tỷ lệ số phần tử rơi vào nhánh con $v$.

**Quy tắc tham lam (Greedy Choice) của ID3:**
Tại mỗi nút, thuật toán tính $IG(S, A)$ cho TOÀN BỘ các thuộc tính còn lại, và **CHỌN THUỘC TÍNH CÓ INFORMATION GAIN LỚN NHẤT** để làm câu hỏi phân nhánh!

**2. Cạm bẫy chí mạng của Information Gain: Thuộc tính Số CMND / ID:**
Hãy tưởng tượng tập dữ liệu có một thuộc tính là `Số Căn Cước Công Dân (CCCD)` hoặc `Mã Khách Hàng`:
- Mỗi người có đúng một mã duy nhất!
- Nếu cây quyết định chọn chia theo `Mã Khách Hàng`: Cây sẽ rẽ thành $N$ nhánh con, mỗi nhánh con chứa đúng 1 người duy nhất!
- Mỗi nhánh con chứa đúng 1 người nên thuần khiết $100\% \implies H(S_v) = 0$!
- Dẫn đến: $H(S \mid \text{Mã CCCD}) = 0 \implies IG(S, \text{Mã CCCD}) = H(S) - 0 = H(S)$ (Cực đại tuyệt đối)!
- Thuật toán ID3 ngây thơ sẽ reo lên: *'Đây là thuộc tính hoàn hảo nhất!'* và chọn ngay nó để làm gốc!
- **Hậu quả:** Cây bị Quá khớp (Overfitting) thảm hại! Nó hoàn toàn không có khả năng tổng quát hóa cho bất kỳ khách hàng mới nào!

**3. Đột phá của Thuật toán C4.5: Gain Ratio (Tỷ Số Độ Lợi):**
Ross Quinlan đã sửa lỗi này trong thuật toán nâng cấp C4.5 bằng cách chia $IG$ cho một đại lượng phạt gọi là **Split Information (Thông tin phân tách)**:
$$\text{Gain Ratio}(S, A) = \frac{IG(S, A)}{\text{Split Information}(S, A)}$$
với:
$$\text{Split Information}(S, A) = - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} \log_2\left(\frac{|S_v|}{|S|}\right)$$
- Thuộc tính nào chia ra càng nhiều nhánh con li ti thì $\text{Split Information}$ càng khổng lồ $\implies$ $\text{Gain Ratio}$ bị dìm xuống sát 0!
- C4.5 loại bỏ hoàn toàn thiên vị đối với các thuộc tính có quá nhiều giá trị riêng biệt!

**4. Bảng phân loại 3 thuật toán Cây Quyết Định kinh điển:**
| Thuật toán | Tác giả | Tiêu chuẩn phân chia | Kiểu phân nhánh | Loại bài toán |
|---|---|---|---|---|
| **ID3** | Ross Quinlan (1986) | Information Gain | Đa nhánh (Multi-way) | Phân loại (Thuộc tính rời rạc) |
| **C4.5** | Ross Quinlan (1993) | Gain Ratio | Đa nhánh & Nhị phân | Phân loại (Hỗ trợ liên tục) |
| **CART** | Leo Breiman (1984) | Gini Impurity / MSE | **Chỉ nhị phân (Binary split)** | **Cả Phân loại & Hồi quy** |""",
                "formula": r"IG(S, A) = H(S) - \sum_{v} \frac{|S_v|}{|S|} H(S_v), \quad \text{GainRatio} = \frac{IG(S, A)}{\text{SplitInfo}(S, A)}",
                "mathExplainer": [
                    { "sym": "IG(S, A)", "name": "Độ lợi thông tin (Information Gain)", "mean": "Lượng hỗn loạn giảm đi sau khi chia tập S theo thuộc tính A." },
                    { "sym": "H(S \\mid A)", "name": "Entropy có điều kiện", "mean": "Tổng Entropy các nhánh con có tính trọng số theo kích thước từng nhánh." },
                    { "sym": "\\text{SplitInfo}", "name": "Thông tin phân tách", "mean": "Thước đo đo lường mức độ phân mảnh của phép chia, dùng để phạt các thuộc tính có quá nhiều nhánh con." },
                    { "sym": "\\text{GainRatio}", "name": "Tỷ số độ lợi", "mean": "Chỉ số chuẩn hóa của C4.5 giúp chống lại cạm bẫy thiên vị thuộc tính ID." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 190" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="190" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 20)">
                        <text x="280" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">CƠ CHẾ TÍNH INFORMATION GAIN TẠI NÚT CHA</text>

                        <!-- Parent Node -->
                        <rect x="200" y="30" width="160" height="40" fill="#fff" stroke="#111" stroke-width="2"/>
                        <text x="280" y="48" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Nút Cha: S (N = 14)</text>
                        <text x="280" y="62" font-family="Georgia" font-size="10" text-anchor="middle">9 Yes, 5 No ⇒ H(S) = 0.940</text>

                        <!-- Split arrows -->
                        <line x1="240" y1="70" x2="130" y2="105" stroke="#111" stroke-width="1.5"/>
                        <text x="160" y="85" font-family="Georgia" font-size="9">Nhánh 1: |S₁| = 8</text>

                        <line x1="320" y1="70" x2="430" y2="105" stroke="#111" stroke-width="1.5"/>
                        <text x="400" y="85" font-family="Georgia" font-size="9">Nhánh 2: |S₂| = 6</text>

                        <!-- Child Node 1 -->
                        <rect x="50" y="105" width="160" height="40" fill="#eee" stroke="#111" stroke-width="1.5"/>
                        <text x="130" y="123" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">S₁ (6 Yes, 2 No)</text>
                        <text x="130" y="137" font-family="Georgia" font-size="9" text-anchor="middle">H(S₁) = 0.811 bit</text>

                        <!-- Child Node 2 -->
                        <rect x="350" y="105" width="160" height="40" fill="#eee" stroke="#111" stroke-width="1.5"/>
                        <text x="430" y="123" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">S₂ (3 Yes, 3 No)</text>
                        <text x="430" y="137" font-family="Georgia" font-size="9" text-anchor="middle">H(S₂) = 1.000 bit</text>

                        <!-- Bottom formula -->
                        <text x="280" y="170" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">IG = H(S) - [(8/14) × 0.811 + (6/14) × 1.000] = 0.940 - 0.892 = 0.048 bit</text>
                      </g>
                    </svg>""",
                    "caption": "Luồng tính toán Information Gain: Trừ Entropy nút cha cho trung bình có trọng số của Entropy các nút con."
                },
                "commonPitfalls": "Quên nhân tỷ lệ mẫu |S_v| / |S|: Rất nhiều học sinh cộng trung bình trực tiếp H(S₁) + H(S₂) rồi chia 2. Đây là sai lầm nghiêm trọng! Phải lấy trung bình có trọng số theo số lượng phần tử của mỗi nhánh con.",
                "practiceQuestion": {
                    "level": "Nâng cao",
                    "question": "Tại sao thuật toán ID3 có xu hướng thiên vị nghiêm trọng việc lựa chọn các thuộc tính có số lượng giá trị phân biệt rất lớn (như Số điện thoại hoặc Mã ID khách hàng)?",
                    "options": [
                        "A. Vì các thuộc tính đó có Entropy nút cha rất nhỏ",
                        "B. Vì khi chia theo thuộc tính đó, mỗi nhánh con chỉ chứa rất ít mẫu, làm Entropy từng nhánh con rơi về 0 và Information Gain đạt cực đại giả tạo",
                        "C. Vì thuật toán ID3 không thể xử lý dữ liệu dạng số liên tục",
                        "D. Vì các thuộc tính đó làm giảm tốc độ tính toán của máy tính"
                    ],
                    "correctIndex": 1,
                    "hint": "Nếu mỗi nhánh con chỉ có 1 người thì nhánh đó có thuần khiết tuyệt đối không? Khi H(S_v) = 0 thì IG = H(S) - 0 = H(S).",
                    "solution": [
                        "Bước 1: Phân tích thuộc tính có nhiều giá trị như Mã ID: số lượng nhánh con sinh ra bằng đúng số mẫu dữ liệu N.",
                        "Bước 2: Mỗi nhánh con chỉ chứa đúng 1 mẫu duy nhất, do đó tỷ lệ p = 1.0 và Entropy của mọi nhánh con đều bằng 0.",
                        "Bước 3: Khi đó Entropy có điều kiện H(S|ID) = 0, dẫn tới IG(S, ID) = H(S) đạt giá trị lớn nhất có thể.",
                        "Bước 4: ID3 sẽ chọn thuộc tính này dù nó hoàn toàn vô dụng trên thực tế (Quá khớp tuyệt đối).",
                        "Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 7.4: KIỂM SOÁT QUÁ KHỚP & KỸ THUẬT TỈA CÀNH (PRUNING)
            # =================================================================
            {
                "heading": "7.4. Kiểm Soát Quá Khớp (Overfitting): Kỹ Thuật Tỉa Cành (Pre-pruning & Cost-Complexity Post-pruning)",
                "content": "Cây quyết định có bản năng tự nhiên mọc sâu vô tận cho đến khi nhớ từng điểm dữ liệu nhiễu. Khám phá hai chiến lược thuần hóa cây: Tiền tỉa cành (Pre-pruning) và Hậu tỉa cành (Cost-Complexity Pruning).",
                "deepDive": r"""**1. Bản chất sự sụp đổ của Cây Quyết Định (Overfitting):**
Cây quyết định là thuật toán **Phi tham số (Non-parametric)**, nghĩa là nó không bị gò bó bởi bất kỳ giả định hình học nào như đường thẳng hay siêu phẳng.
- Nếu bạn không can thiệp, cây sẽ liên tục phân nhánh cho đến khi mỗi chiếc lá chỉ chứa đúng **1 điểm dữ liệu duy nhất**!
- Lúc này:
  - Sai số trên tập huấn luyện (Train Error) = **0%**!
  - Nhưng sai số trên tập kiểm tra (Test Error) vọt lên rất cao vì cây đã ghi nhớ cả các điểm nhiễu (Noise) và Outliers!

**2. Chiến lược 1: Tiền tỉa cành (Pre-pruning / Early Stopping):**
Chặn đứng sự phát triển của cây ngay trong quá trình xây dựng bằng các 'hàng rào an toàn':
- `max_depth`: Giới hạn độ sâu tối đa của cây (ví dụ: `max_depth=4` chỉ cho phép cây mọc tối đa 4 tầng).
- `min_samples_split`: Số lượng mẫu tối thiểu bắt buộc phải có ở một nút để được phép chia tiếp (ví dụ: nếu nút có ít hơn 20 mẫu thì dừng lại, không chia nữa).
- `min_samples_leaf`: Số lượng mẫu tối thiểu bắt buộc phải có ở một nút lá (ví dụ: mỗi lá phải có ít nhất 5 mẫu).
- `min_impurity_decrease`: Mức độ giảm Gini/Entropy tối thiểu để chấp nhận một phép chia.
- *Nhược điểm của Tiền tỉa cành:* Dễ mắc lỗi **Tầm nhìn ngắn (Myopic Stopping)**. Có những phép chia ở tầng hiện tại chỉ giảm rất ít Entropy, nhưng nó lại mở đường cho một phép chia cực kỳ xuất sắc ở tầng ngay sau đó! Nếu dừng quá sớm, ta sẽ bỏ lỡ cơ hội này.

**3. Chiến lược 2: Hậu tỉa cành (Post-pruning / Cost-Complexity Pruning - CCP):**
Cho phép cây phát triển thoải mái đến mức cực đại ($T_0$), sau đó dùng dao tỉa gọt bớt các cành lá thừa thãi từ dưới đáy lên trên!
- **Hàm mục tiêu phạt độ phức tạp (Cost-Complexity Criterion):**
  $$\mathcal{R}_\alpha(T) = \mathcal{R}(T) + \alpha |T|$$
  - $\mathcal{R}(T)$: Tổng sai số phân loại của toàn bộ cây $T$ trên tập dữ liệu.
  - $|T|$: Số lượng nút lá của cây $T$ (Đại diện cho kích thước và độ cồng kềnh của mô hình).
  - $\alpha \ge 0$: Siêu tham số điều chỉnh độ phạt tỉa cành (Complexity Parameter).
- **Cơ chế hoạt động của $\alpha$:**
  - Khi $\alpha = 0$: Không phạt gì cả $\implies$ Cây giữ nguyên kích thước khổng lồ ban đầu $T_0$.
  - Khi $\alpha$ tăng dần: Giá phạt cho mỗi chiếc lá tăng lên. Thuật toán sẽ so sánh: Việc giữ lại một nhánh con có giúp giảm sai số $\mathcal{R}(T)$ đủ nhiều để bù lại chi phí phạt $\alpha |T|$ hay không?
  - Nếu nhánh con đó chỉ giúp sửa sai cho một vài điểm nhiễu vu vơ, thuật toán sẽ **cắt phăng nhánh đó đi** và gộp lại thành một nút lá duy nhất!
  - Khi $\alpha \to \infty$: Toàn bộ các nhánh bị cắt sạch, chỉ còn lại đúng 1 nút gốc duy nhất!""",
                "formula": r"\mathcal{R}_\alpha(T) = \mathcal{R}(T) + \alpha |T|, \quad \alpha_{\text{eff}} = \frac{\mathcal{R}(t) - \mathcal{R}(T_t)}{|T_t| - 1}",
                "mathExplainer": [
                    { "sym": "\\mathcal{R}(T)", "name": "Sai số của cây T", "mean": "Tỷ lệ hoặc số lượng mẫu bị phân loại sai bởi cây trên tập dữ liệu." },
                    { "sym": "|T|", "name": "Số lượng nút lá", "mean": "Độ phức tạp kích cỡ của cây (càng nhiều lá cây càng dễ overfit)." },
                    { "sym": "\\alpha (Alpha)", "name": "Hệ số phạt độ phức tạp", "mean": "Siêu tham số điều khiển mức độ tỉa: alpha càng lớn cây càng bị gọt ngắn." },
                    { "sym": "\\alpha_{\\text{eff}}", "name": "Ngưỡng alpha hiệu dụng", "mean": "Mức alpha tối thiểu mà tại đó việc tỉa bỏ nhánh T_t đem lại lợi ích tốt hơn giữ lại." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 20)">
                        <!-- Overfitted Tree (Left) -->
                        <g transform="translate(30, 10)">
                          <text x="100" y="0" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Cây Mọc Tự Do (Overfit: 7 Lá)</text>
                          <circle cx="100" cy="25" r="5" fill="#111"/>
                          <line x1="95" y1="28" x2="60" y2="55" stroke="#111"/><line x1="105" y1="28" x2="140" y2="55" stroke="#111"/>
                          <circle cx="60" cy="58" r="4" fill="#111"/><circle cx="140" cy="58" r="4" fill="#111"/>
                          <line x1="55" y1="62" x2="30" y2="90" stroke="#111"/><line x1="65" y1="62" x2="80" y2="90" stroke="#111"/>
                          <circle cx="30" cy="92" r="3" fill="#111"/><circle cx="80" cy="92" r="3" fill="#111"/>
                          <!-- Noise branches -->
                          <line x1="28" y1="95" x2="15" y2="125" stroke="#888" stroke-dasharray="2,2"/>
                          <line x1="32" y1="95" x2="45" y2="125" stroke="#888" stroke-dasharray="2,2"/>
                          <circle cx="15" cy="127" r="3" fill="#888"/><circle cx="45" cy="127" r="3" fill="#888"/>
                          <text x="30" y="145" font-family="Georgia" font-size="8" fill="#888">Cành thừa do nhiễu</text>
                        </g>

                        <!-- Scissors Arrow -->
                        <g transform="translate(245, 65)">
                          <line x1="0" y1="15" x2="60" y2="15" stroke="#111" stroke-width="2"/>
                          <polygon points="60,15 50,10 50,20" fill="#111"/>
                          <text x="30" y="5" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Hậu tỉa cành</text>
                          <text x="30" y="32" font-family="Georgia" font-size="9" fill="#555" text-anchor="middle">Phạt R_α(T)</text>
                        </g>

                        <!-- Pruned Tree (Right) -->
                        <g transform="translate(360, 10)">
                          <text x="100" y="0" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Cây Sau Khi Tỉa (Tổng Quát: 3 Lá)</text>
                          <circle cx="100" cy="25" r="6" fill="#111"/>
                          <line x1="95" y1="30" x2="60" y2="65" stroke="#111" stroke-width="2"/>
                          <line x1="105" y1="30" x2="140" y2="65" stroke="#111" stroke-width="2"/>
                          <rect x="40" y="65" width="40" height="25" fill="#111"/>
                          <text x="60" y="81" font-family="Georgia" font-size="9" fill="#fff" text-anchor="middle">Lá 1</text>
                          <!-- Right split -->
                          <circle cx="140" cy="65" r="5" fill="#111"/>
                          <line x1="135" y1="70" x2="115" y2="105" stroke="#111" stroke-width="1.5"/>
                          <line x1="145" y1="70" x2="165" y2="105" stroke="#111" stroke-width="1.5"/>
                          <rect x="95" y="105" width="40" height="25" fill="#eee" stroke="#111"/>
                          <text x="115" y="121" font-family="Georgia" font-size="9" text-anchor="middle">Lá 2</text>
                          <rect x="145" y="105" width="40" height="25" fill="#111"/>
                          <text x="165" y="121" font-family="Georgia" font-size="9" fill="#fff" text-anchor="middle">Lá 3</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "Kỹ thuật Cost-Complexity Pruning cắt bỏ các cành lá sâu li ti ghi nhớ nhiễu để đưa mô hình về trạng thái tổng quát hóa cao."
                },
                "commonPitfalls": "Nhầm lẫn chiều tác động của siêu tham số alpha: Khi alpha = 0, mô hình phức tạp nhất (dễ Overfitting). Khi alpha TĂNG LÊN, mô hình bị tỉa ngắn lại (giảm Overfitting). Nếu alpha quá lớn, cây bị tỉa trụi lủi chỉ còn 1 lá, dẫn tới hiện tượng Underfitting!",
                "practiceQuestion": {
                    "level": "Trung bình",
                    "question": "Khi áp dụng kỹ thuật Cost-Complexity Pruning với hàm mục tiêu R_α(T) = R(T) + α|T|, nếu ta liên tục tăng giá trị siêu tham số α từ 0 lên vô cùng, điều gì sẽ xảy ra với số lượng nút lá |T| của cây quyết định?",
                    "options": [
                        "A. Số lượng nút lá |T| sẽ tăng dần để giảm sai số R(T)",
                        "B. Số lượng nút lá |T| sẽ giảm dần đơn điệu và cuối cùng chỉ còn lại 1 nút gốc duy nhất",
                        "C. Số lượng nút lá |T| không thay đổi vì cấu trúc cây đã được cố định trước đó",
                        "D. Cây sẽ bị xóa hoàn toàn và không còn nút nào"
                    ],
                    "correctIndex": 1,
                    "hint": "alpha là tiền phạt cho mỗi chiếc lá. Tiền phạt càng đắt đỏ thì thuật toán càng thẳng tay cắt bỏ các lá rườm rà.",
                    "solution": [
                        "Bước 1: Phân tích hàm mục tiêu: R_α(T) = R(T) + α|T|.",
                        "Bước 2: Khi α tăng lên, chi phí phạt cho mỗi nút lá tăng vọt, buộc thuật toán phải cắt bớt các nhánh con để cực tiểu hóa hàm mục tiêu.",
                        "Bước 3: Do đó số lượng lá |T| là một hàm giảm đơn điệu theo α, cho đến khi chỉ còn đúng 1 nút lá gốc.",
                        "Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 7.5: KỸ THUẬT ENSEMBLE: BAGGING (RANDOM FOREST) VS BOOSTING (XGBOOST)
            # =================================================================
            {
                "heading": "7.5. Kỹ Thuật Ensemble: Sức Mạnh Hội Đồng, Bagging (Random Forest, OOB 36.8%) vs Boosting (XGBoost)",
                "content": "Một cây đơn lẻ luôn có phương sai cao và dễ lung lay trước nhiễu. Kỹ thuật Học Kết Hợp (Ensemble Learning) kết nối hàng trăm cây lại với nhau, tạo ra những mô hình thống trị mọi cuộc thi Machine Learning trên thế giới.",
                "deepDive": r"""**1. Triết lý Ensemble và Định lý Ban Giám Khảo Condorcet (1785):**
Giả sử có một hội đồng gồm 100 vị bác sĩ độc lập. Mỗi vị bác sĩ có xác suất chẩn đoán đúng là $p = 70\%$ ($0.7$).
- Nếu bạn chỉ hỏi 1 bác sĩ: Xác suất đúng là $70\%$.
- Nhưng nếu bạn cho **cả 100 bác sĩ bỏ phiếu biểu quyết đa số**:
  Theo luật số lớn, xác suất để hơn một nửa hội đồng (từ 51 bác sĩ trở lên) cùng đoán đúng vọt lên tới:
  $$P(\text{Hội đồng đúng}) = \sum_{k=51}^{100} \binom{100}{k} (0.7)^k (0.3)^{100-k} \approx 99.997\%!$$
- Một tập hợp gồm các mô hình yếu (Weak Learners) độc lập khi kết hợp lại sẽ tạo ra một mô hình mạnh mẽ phi thường (Strong Learner)!

**2. Hai trường phái Ensemble vĩ đại: BAGGING vs BOOSTING (Trọng tâm Câu 12 Đề thi VAIO):**

| Tiêu Chí Phân Biệt | BAGGING (Bootstrap Aggregating) | BOOSTING (Tăng Cường Tuần Tự) |
|---|---|---|
| **Thuật toán đại diện** | **Random Forest (Rừng ngẫu nhiên)** | **AdaBoost, Gradient Boosting, XGBoost, LightGBM** |
| **Cách huấn luyện** | **Song song, độc lập hoàn toàn** (Parallel) | **Nối tiếp, tuần tự từng cây** (Sequential) |
| **Mục tiêu toán học** | **GIẢM PHƯƠNG SAI (Variance Reduction)** | **GIẢM ĐỘ LỆCH (Bias Reduction)** |
| **Loại cây cơ sở** | Cây mọc sâu hết mức (Low Bias, High Variance) | Cây nông, gốc cụt 1-3 tầng (High Bias, Low Variance) |
| **Cơ chế tổng hợp** | Bỏ phiếu đa số (Phân loại) hoặc Lấy trung bình cộng (Hồi quy) | Tổng có trọng số của các cây: $\hat{y} = \sum \eta f_b(x)$ |
| **Xử lý mẫu sai** | Các cây xem mọi mẫu dữ liệu bình đẳng như nhau | Cây sau **tập trung toàn lực vào các mẫu cây trước đoán sai** |
| **Độ nhạy với Nhiễu** | Rất kiên cường với nhiễu và Outliers | Dễ bị ảnh hưởng bởi nhiễu (vì cố ép học các mẫu khó) |

**3. Bí mật bên trong Random Forest: Hai tầng ngẫu nhiên hóa:**
Random Forest nâng cấp từ Bagging nhờ hai kỹ thuật ngẫu nhiên đột phá:
- **Tầng 1: Lấy mẫu Bootstrap có hoàn lại (Sample Bootstrapping):**
  - Từ tập dữ liệu $N$ mẫu, mỗi cây rút thăm ngẫu nhiên $N$ mẫu CÓ HOÀN LẠI (một mẫu có thể được rút nhiều lần).
  - **Định lý kỳ diệu Out-Of-Bag (OOB) trong đề thi Olympic:**
    - Xác suất một mẫu dữ liệu cụ thể KHÔNG ĐƯỢC CHỌN trong 1 lần bốc là $1 - \frac{1}{N}$.
    - Xác suất mẫu đó hoàn toàn vắng mặt sau cả $N$ lần bốc độc lập là:
      $$P(\text{Vắng mặt}) = \left(1 - \frac{1}{N}\right)^N$$
    - Khi kích thước dữ liệu lớn ($N \to \infty$):
      $$\lim_{N \to \infty} \left(1 - \frac{1}{N}\right)^N = \frac{1}{e} \approx 0.3679 \approx 36.8\%$$
    - **Ý nghĩa thực tiễn:** Trong mỗi cây, luôn có khoảng **$36.8\%$ dữ liệu gốc không hề được dùng để huấn luyện**! Tập này gọi là **Out-Of-Bag (OOB)**, được tận dụng làm tập kiểm thử Validation miễn phí mà không cần phải tốn công chia tập Validation riêng!

- **Tầng 2: Ngẫu nhiên hóa không gian đặc trưng (Feature Subsampling):**
  - Tại MỖI LẦN PHÂN NHÁNH, cây không được phép nhìn tất cả $d$ đặc trưng!
  - Cây chỉ được bốc ngẫu nhiên một tập con gồm $m$ đặc trưng:
    $$m = \sqrt{d} \text{ (với bài toán Phân loại)}, \quad m = \frac{d}{3} \text{ (với bài toán Hồi quy)}$$
  - *Tại sao phải làm vậy?* Nếu có 1 đặc trưng cực kỳ mạnh (ví dụ: Thu nhập), tất cả 100 cây đều sẽ chọn nó làm gốc, khiến 100 cây giống hệt nhau và tương quan chặt chẽ với nhau! Việc ép chọn ngẫu nhiên buộc các cây phải khám phá các đặc trưng khác nhau, làm **Mất tương quan (Decorrelate) giữa các cây**, giúp phương sai toàn cục giảm tối đa!

**4. Cơ chế hoạt động của Boosting (XGBoost / Gradient Boosting):**
- Cây thứ 1 huấn luyện xong, dự đoán còn sai lệch một lượng dư sai số (Residual):
  $$r_i^{(1)} = y_i - \hat{y}_i^{(1)}$$
- Cây thứ 2 sinh ra **không phải để dự đoán $y$**, mà để **dự đoán chính xác phần sai số dư $r_i^{(1)}$**!
- Cập nhật dự đoán tổng hợp với tốc độ học $\eta$ (Shrinkage factor, ví dụ $\eta = 0.05$):
  $$\hat{y}^{(2)} = \hat{y}^{(1)} + \eta f_2(x)$$
- Từng bước một, các cây nối tiếp nhau bào mòn sai số về gần bằng 0!""",
                "formula": r"\hat{y}_{\text{RF}} = \text{mode}(T_1, \dots, T_B), \quad \lim_{N \to \infty}\left(1-\frac{1}{N}\right)^N = \frac{1}{e} \approx 36.8\%, \quad \hat{y}_{\text{Boost}} = \sum_{b=1}^B \eta f_b(x)",
                "mathExplainer": [
                    { "sym": "B", "name": "Số lượng cây trong rừng", "mean": "Thường chọn từ 100 đến 500 cây (tăng B không làm overfit Random Forest, chỉ tốn thời gian)." },
                    { "sym": "m = \\sqrt{d}", "name": "Số đặc trưng ngẫu nhiên", "mean": "Quy tắc vàng của Leo Breiman: mỗi bước phân nhánh chỉ xét căn bậc hai tổng số đặc trưng." },
                    { "sym": "1/e \\approx 36.8\\%", "name": "Tỷ lệ mẫu Out-Of-Bag (OOB)", "mean": "Tỷ lệ phần trăm các mẫu dữ liệu không được rút trúng trong quá trình lấy mẫu Bootstrap." },
                    { "sym": "\\eta (Eta)", "name": "Hệ số co rút (Learning Rate)", "mean": "Tốc độ học trong Boosting (thường 0.01 đến 0.1) giúp ngăn chặn cây học quá nhanh dẫn tới overfit." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 210" width="100%" height="210" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="210" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(30, 20)">
                        <!-- Bagging Diagram (Left) -->
                        <g transform="translate(10, 10)">
                          <text x="130" y="0" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">BAGGING (Random Forest: Song Song)</text>
                          <!-- Data -->
                          <rect x="70" y="15" width="120" height="25" fill="#eee" stroke="#111"/>
                          <text x="130" y="32" font-family="Georgia" font-size="9" text-anchor="middle">Tập dữ liệu gốc D</text>
                          <!-- Parallel branches -->
                          <line x1="85" y1="40" x2="35" y2="65" stroke="#111"/>
                          <line x1="130" y1="40" x2="130" y2="65" stroke="#111"/>
                          <line x1="175" y1="40" x2="225" y2="65" stroke="#111"/>
                          <!-- Trees -->
                          <rect x="10" y="65" width="50" height="35" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="35" y="86" font-family="Georgia" font-size="9" text-anchor="middle">Cây 1</text>
                          <rect x="105" y="65" width="50" height="35" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="130" y="86" font-family="Georgia" font-size="9" text-anchor="middle">Cây 2</text>
                          <rect x="200" y="65" width="50" height="35" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="225" y="86" font-family="Georgia" font-size="9" text-anchor="middle">Cây B</text>
                          <!-- Voting box -->
                          <line x1="35" y1="100" x2="130" y2="130" stroke="#111"/>
                          <line x1="130" y1="100" x2="130" y2="130" stroke="#111"/>
                          <line x1="225" y1="100" x2="130" y2="130" stroke="#111"/>
                          <rect x="65" y="130" width="130" height="30" fill="#111"/>
                          <text x="130" y="149" font-family="Georgia" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">Biểu Quyết Đa Số</text>
                          <text x="130" y="178" font-family="Georgia" font-size="9" font-style="italic" text-anchor="middle">Mục tiêu: GIẢM PHƯƠNG SAI</text>
                        </g>

                        <!-- Divider -->
                        <line x1="290" y1="15" x2="290" y2="185" stroke="#ccc" stroke-dasharray="2,2"/>

                        <!-- Boosting Diagram (Right) -->
                        <g transform="translate(310, 10)">
                          <text x="140" y="0" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">BOOSTING (XGBoost: Tuần Tự)</text>
                          <!-- Sequential flow -->
                          <rect x="10" y="45" width="55" height="40" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="37" y="68" font-family="Georgia" font-size="9" text-anchor="middle">Cây 1</text>

                          <line x1="65" y1="65" x2="105" y2="65" stroke="#111" stroke-width="1.5"/>
                          <polygon points="105,65 97,61 97,69" fill="#111"/>
                          <text x="85" y="58" font-family="Georgia" font-size="8" text-anchor="middle">Sai số r₁</text>

                          <rect x="105" y="45" width="55" height="40" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="132" y="68" font-family="Georgia" font-size="9" text-anchor="middle">Cây 2</text>

                          <line x1="160" y1="65" x2="200" y2="65" stroke="#111" stroke-width="1.5"/>
                          <polygon points="200,65 192,61 192,69" fill="#111"/>
                          <text x="180" y="58" font-family="Georgia" font-size="8" text-anchor="middle">Sai số r₂</text>

                          <rect x="200" y="45" width="55" height="40" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="227" y="68" font-family="Georgia" font-size="9" text-anchor="middle">Cây 3</text>

                          <!-- Summation -->
                          <rect x="55" y="130" width="160" height="30" fill="#111"/>
                          <text x="135" y="149" font-family="Georgia" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">Tổng Có Trọng Số Σ η·f_b(x)</text>
                          <text x="135" y="178" font-family="Georgia" font-size="9" font-style="italic" text-anchor="middle">Mục tiêu: GIẢM ĐỘ LỆCH (BIAS)</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "So sánh kiến trúc song song Bagging (Random Forest - Giảm Variance) vs kiến trúc nối tiếp Boosting (XGBoost - Giảm Bias)."
                },
                "commonPitfalls": "Nhầm lẫn giữa cơ chế giảm lỗi của Bagging và Boosting: Đề thi VAIO thường xuyên gài bẫy: 'Random Forest giúp giảm thành phần nào trong sai số?'. Câu trả lời ĐÚNG là GIẢM PHƯƠNG SAI (Variance). Boosting mới là kỹ thuật tập trung GIẢM ĐỘ LỆCH (Bias)!",
                "practiceQuestion": {
                    "level": "Nâng cao (Câu 12 Đề Thi VAIO 2025)",
                    "question": "Trong thuật toán Rừng Ngẫu Nhiên (Random Forest), khi kích thước tập dữ liệu huấn luyện N rất lớn, tỷ lệ xấp xỉ của các mẫu dữ liệu không được rút trúng vào tập Bootstrap của mỗi cây (Tập Out-Of-Bag - OOB) là bao nhiêu?",
                    "options": [
                        "A. Khoảng 50.0%",
                        "B. Khoảng 36.8% (Tương đương 1/e)",
                        "C. Khoảng 63.2% (Tương đương 1 - 1/e)",
                        "D. Đúng bằng 0% vì tất cả mẫu đều được dùng"
                    ],
                    "correctIndex": 1,
                    "hint": "Tính giới hạn của (1 - 1/N)^N khi N tiến tới vô cùng. lim(1 - 1/N)^N = 1/e ≈ 0.368.",
                    "solution": [
                        "Bước 1: Xác suất một mẫu không được rút trong một lượt bốc là (1 - 1/N).",
                        "Bước 2: Sau N lượt bốc có hoàn lại độc lập, xác suất mẫu đó hoàn toàn vắng mặt là (1 - 1/N)^N.",
                        "Bước 3: Lấy giới hạn khi N -> vô cùng: lim (1 - 1/N)^N = e^(-1) = 1/e ≈ 0.367879 ≈ 36.8%.",
                        "Bước 4: Đây chính là tỷ lệ mẫu Out-Of-Bag (OOB). Mẫu được dùng trong cây chiếm 1 - 36.8% = 63.2%.",
                        "Đáp án chính xác: B (Khoảng 36.8%)."
                    ]
                }
            },

            # =================================================================
            # MỤC 7.6: BÀI TOÁN TÍNH TAY CHUẨN ĐỀ THI VAIO (CÂU 34 & CÂU 12)
            # =================================================================
            {
                "heading": "7.6. Bài Toán Tính Tay Chuẩn Đề Thi VAIO: Tính Entropy, Information Gain & Dự Đoán Biểu Quyết Random Forest",
                "content": "Thực hành giải bài toán kinh điển mô phỏng chuẩn xác Câu 34 và Câu 12 Đề thi Olympic AI: Tính toán chi tiết từng bit Entropy, độ lợi thông tin Information Gain, và phân biệt Hard Voting vs Soft Voting trong Random Forest.",
                "deepDive": r"""**1. Đề bài chuẩn Olympic AI:**
Xét bài toán phân loại kinh điển gồm $N = 14$ ngày quan sát để dự đoán quyết định có nên `Chơi Quần Vợt (Play Tennis)` hay không.
Tập dữ liệu ban đầu $S$ có:
- **9 ngày Chơi (Yes)**
- **5 ngày Nghỉ (No)**

Ta muốn đánh giá xem có nên chọn thuộc tính `Gió (Wind)` để phân nhánh tại nút gốc hay không. Thuộc tính `Gió` nhận 2 giá trị:
- `Gió Yếu (Weak)`: Gồm **8 ngày**, trong đó có **6 ngày Chơi (Yes)** và **2 ngày Nghỉ (No)**.
- `Gió Mạnh (Strong)`: Gồm **6 ngày**, trong đó có **3 ngày Chơi (Yes)** và **3 ngày Nghỉ (No)**.

*(Bảng số liệu hỗ trợ tính toán: $\log_2(9/14) \approx -0.6374$, $\log_2(5/14) \approx -1.4854$, $\log_2(6/8) \approx -0.4150$, $\log_2(2/8) \approx -2.0000$, $\log_2(0.5) = -1.0000$)*.

**YÊU CẦU THÍ SINH:**
1. Tính độ hỗn loạn Entropy ban đầu của tập dữ liệu: $H(S)$.
2. Tính Entropy của nhánh `Gió Yếu`: $H(S_{\text{Weak}})$ và nhánh `Gió Mạnh`: $H(S_{\text{Strong}})$.
3. Tính Entropy có điều kiện $H(S \mid \text{Wind})$ và Độ Lợi Thông Tin $\text{IG}(S, \text{Wind})$.
4. Tính chỉ số vẩn đục ban đầu $\text{Gini}(S)$.
5. Giả sử ta huấn luyện một mô hình Random Forest gồm $B = 5$ cây độc lập. Với một ngày mới có các điều kiện thời tiết $x$, 5 cây đưa ra các xác suất dự đoán $P(\text{Yes} \mid x)$ lần lượt là: $[0.8, 0.7, 0.4, 0.9, 0.3]$.
   - Theo cơ chế **Biểu quyết cứng (Hard Voting)** với ngưỡng 0.5: Kết quả phân loại là gì?
   - Theo cơ chế **Biểu quyết mềm (Soft Voting)**: Xác suất trung bình là bao nhiêu và kết quả phân loại là gì?

---

**2. Lời giải chi tiết từng bước (Step-by-Step Derivation):**

**Bước 1: Tính Entropy ban đầu $H(S)$:**
Tập $S$ có 9 Yes, 5 No trên tổng số 14 mẫu:
$$p_{\text{Yes}} = \frac{9}{14} \approx 0.6429, \quad p_{\text{No}} = \frac{5}{14} \approx 0.3571$$
$$H(S) = - \left[ \frac{9}{14} \log_2\left(\frac{9}{14}\right) + \frac{5}{14} \log_2\left(\frac{5}{14}\right) \right]$$
$$= - [ 0.6429 \times (-0.6374) + 0.3571 \times (-1.4854) ]$$
$$= - [ -0.4098 - 0.5305 ] = - (-0.9403) = 0.9403\text{ bit}$$

**Bước 2: Tính Entropy các nhánh con:**
- **Nhánh Gió Yếu ($S_{\text{Weak}}$ gồm 6 Yes, 2 No, tổng 8 mẫu):**
  $$p_1 = \frac{6}{8} = 0.75, \quad p_2 = \frac{2}{8} = 0.25$$
  $$H(S_{\text{Weak}}) = - [ 0.75 \log_2(0.75) + 0.25 \log_2(0.25) ]$$
  $$= - [ 0.75 \times (-0.4150) + 0.25 \times (-2.0000) ]$$
  $$= - [ -0.3113 - 0.5000 ] = 0.8113\text{ bit}$$

- **Nhánh Gió Mạnh ($S_{\text{Strong}}$ gồm 3 Yes, 3 No, tổng 6 mẫu):**
  Vì tỷ lệ chia đôi cân bằng 50-50 ($p_1 = 0.5, p_2 = 0.5$):
  $$H(S_{\text{Strong}}) = - [ 0.5 \log_2(0.5) + 0.5 \log_2(0.5) ] = - [ 0.5(-1) + 0.5(-1) ] = 1.0000\text{ bit}$$

**Bước 3: Tính Entropy có điều kiện và Information Gain:**
- Entropy có điều kiện $H(S \mid \text{Wind})$:
  $$H(S \mid \text{Wind}) = \frac{|S_{\text{Weak}}|}{|S|} H(S_{\text{Weak}}) + \frac{|S_{\text{Strong}}|}{|S|} H(S_{\text{Strong}})$$
  $$= \frac{8}{14} \times 0.8113 + \frac{6}{14} \times 1.0000$$
  $$= 0.5714 \times 0.8113 + 0.4286 \times 1.0000 = 0.4636 + 0.4286 = 0.8922\text{ bit}$$
- Độ Lợi Thông Tin $\text{IG}(S, \text{Wind})$:
  $$\text{IG}(S, \text{Wind}) = H(S) - H(S \mid \text{Wind}) = 0.9403 - 0.8922 = 0.0481\text{ bit}$$
  *Nhận xét:* Việc phân nhánh theo thuộc tính Gió giúp làm giảm độ hỗn loạn đi $0.0481$ bit thông tin.

**Bước 4: Tính Gini ban đầu $\text{Gini}(S)$:**
$$\text{Gini}(S) = 1 - \left[ \left(\frac{9}{14}\right)^2 + \left(\frac{5}{14}\right)^2 \right] = 1 - \left[ \frac{81}{196} + \frac{25}{196} \right] = 1 - \frac{106}{196} = \frac{90}{196} \approx 0.4592$$

**Bước 5: Dự đoán Random Forest (Hard Voting vs Soft Voting):**
Tập xác suất của 5 cây: $[0.8, 0.7, 0.4, 0.9, 0.3]$.
- **Biểu quyết cứng (Hard Voting):**
  Quy đổi từng xác suất thành nhãn nhị phân với ngưỡng $\theta = 0.5$:
  - Cây 1: $0.8 \ge 0.5 \implies$ **YES**
  - Cây 2: $0.7 \ge 0.5 \implies$ **YES**
  - Cây 3: $0.4 < 0.5 \implies$ **NO**
  - Cây 4: $0.9 \ge 0.5 \implies$ **YES**
  - Cây 5: $0.3 < 0.5 \implies$ **NO**
  - Kiểm phiếu: Có **3 phiếu YES** và **2 phiếu NO**.
  - **Kết luận:** Mô hình biểu quyết chọn **YES** (Thắng áp đảo 3-2).

- **Biểu quyết mềm (Soft Voting):**
  Tính xác suất trung bình cộng của cả 5 cây:
  $$\bar{P}(\text{Yes} \mid x) = \frac{0.8 + 0.7 + 0.4 + 0.9 + 0.3}{5} = \frac{3.1}{5} = 0.62 = 62.0\%$$
  Vì $\bar{P} = 62.0\% \ge 50\%$, mô hình kết luận nhãn **YES** với độ tin cậy $62\%$.
  *(Lưu ý: Soft Voting thường cho kết quả ổn định và chính xác hơn Hard Voting vì nó cân nhắc cả mức độ tự tin của từng cây!)*""",
                "formula": r"H(S) = 0.9403, \, H(S|\text{Wind}) = 0.8922 \implies \text{IG} = 0.0481\text{ bit}, \, \text{Gini} = 0.4592, \, \bar{P}_{\text{Soft}} = 62\%",
                "mathExplainer": [
                    { "sym": "H(S) = 0.9403", "name": "Entropy gốc", "mean": "Độ hỗn loạn ban đầu của 14 mẫu thời tiết." },
                    { "sym": "H(S|\\text{Wind}) = 0.8922", "name": "Entropy có điều kiện", "mean": "Độ hỗn loạn trung bình còn lại sau khi biết thông tin về Gió." },
                    { "sym": "\\text{IG} = 0.0481", "name": "Độ lợi thông tin", "mean": "Lượng thông tin hữu ích thu được từ thuộc tính Gió (0.0481 bit)." },
                    { "sym": "\\bar{P} = 62\\%", "name": "Xác suất Soft Voting", "mean": "Độ tin cậy tổng hợp của hội đồng 5 cây quyết định trong Random Forest." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 190" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="190" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(30, 20)">
                        <text x="290" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">TỔNG HỢP KẾT QUẢ TÍNH TOÁN THỰC CHIẾN CÂU 34 &amp; CÂU 12</text>

                        <!-- Box 1: Information Gain -->
                        <g transform="translate(10, 35)">
                          <rect x="0" y="0" width="260" height="120" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="130" y="22" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">1. Tính Toán Cây Đơn (ID3)</text>
                          <text x="15" y="48" font-family="Georgia" font-size="10">• H(S ban đầu) = 0.9403 bit</text>
                          <text x="15" y="68" font-family="Georgia" font-size="10">• H(S_Weak) = 0.8113, H(S_Strong) = 1.000</text>
                          <text x="15" y="88" font-family="Georgia" font-size="10">• H(S|Wind) = (8/14)(0.811) + (6/14)(1.0) = 0.892</text>
                          <text x="15" y="110" font-family="Georgia" font-size="11" font-weight="bold">⇒ IG(S, Wind) = 0.0481 bit</text>
                        </g>

                        <!-- Box 2: Random Forest Voting -->
                        <g transform="translate(300, 35)">
                          <rect x="0" y="0" width="270" height="120" fill="#111"/>
                          <text x="135" y="22" font-family="Georgia" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">2. Hội Đồng Rừng Ngẫu Nhiên</text>
                          <text x="15" y="48" font-family="Georgia" font-size="10" fill="#eee">• Xác suất 5 cây: [0.8, 0.7, 0.4, 0.9, 0.3]</text>
                          <text x="15" y="70" font-family="Georgia" font-size="11" font-weight="bold" fill="#fff">• Hard Voting: 3 YES vs 2 NO ⇒ YES</text>
                          <text x="15" y="92" font-family="Georgia" font-size="11" font-weight="bold" fill="#fff">• Soft Voting: Trung bình p = 62.0% ⇒ YES</text>
                          <text x="15" y="112" font-family="Georgia" font-size="9" fill="#ccc">Hội đồng triệt tiêu sai số ngẫu nhiên!</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "Bảng tổng kết toàn diện: Phép tính toán Entropy / Information Gain của thuật toán ID3 và cơ chế biểu quyết Hard/Soft Voting của Random Forest."
                },
                "commonPitfalls": "Nhầm lẫn giữa logarit tự nhiên ln và logarit cơ số 2 trong đề thi: Nếu đề bài yêu cầu tính Entropy theo đơn vị bit (Shannon Entropy), bạn BẮT BUỘC phải dùng logarit cơ số 2 (log₂). Nếu dùng logarit tự nhiên ln, đơn vị tính sẽ là nat (thường dùng trong vật lý thống kê).",
                "practiceQuestion": {
                    "level": "Nâng cao (Câu 34 Đề Thi VAIO 2025)",
                    "question": "Cho một tập dữ liệu nhị phân S gồm 16 mẫu với 12 mẫu Dương tính và 4 mẫu Âm tính. Nếu một thuộc tính A chia tập S thành hai tập con S₁ (gồm 8 mẫu Dương tính, 0 mẫu Âm tính) và S₂ (gồm 4 mẫu Dương tính, 4 mẫu Âm tính). Biết H(S) ≈ 0.811 bit. Độ Lợi Thông Tin IG(S, A) bằng bao nhiêu?",
                    "options": [
                        "A. 0.311 bit",
                        "B. 0.500 bit",
                        "C. 0.811 bit",
                        "D. 0.000 bit"
                    ],
                    "correctIndex": 0,
                    "hint": "Tính H(S₁) = 0 (thuần khiết). Tính H(S₂) = 1.0 (50-50). Tính H(S|A) = (8/16) * 0 + (8/16) * 1.0 = 0.5. IG = H(S) - H(S|A).",
                    "solution": [
                        "Bước 1: Tính Entropy từng nhánh con:",
                        "  Nhánh S₁: 8 mẫu (+) và 0 mẫu (-) ⇒ Thuần khiết tuyệt đối ⇒ H(S₁) = 0.0 bit.",
                        "  Nhánh S₂: 4 mẫu (+) và 4 mẫu (-) ⇒ Chia đôi 50-50 ⇒ H(S₂) = 1.0 bit.",
                        "Bước 2: Tính trọng số và Entropy có điều kiện:",
                        "  |S₁| = 8, |S₂| = 8, tổng |S| = 16.",
                        "  H(S|A) = (8/16) × H(S₁) + (8/16) × H(S₂) = 0.5 × 0 + 0.5 × 1.0 = 0.500 bit.",
                        "Bước 3: Tính Độ Lợi Thông Tin:",
                        "  IG(S, A) = H(S) - H(S|A) = 0.811 - 0.500 = 0.311 bit.",
                        "Đáp án chính xác: A (0.311 bit)."
                    ]
                }
            }
        ],
        "interactiveWidget": "widget-entropy-calculator",
        "examConnection": {
            "questionTitle": "Điểm Trọng Tâm Về Decision Tree & Ensemble Trong Đề Thi VAIO 2025",
            "items": [
                {
                    "code": "Câu 12 VAIO: Bagging vs Random Forest",
                    "problem": "Thuật toán nào sau đây là thuật toán phổ biến và hiệu quả nhất dựa trên ý tưởng Bagging (Bootstrap Aggregating)?",
                    "solution": [
                        "1. Random Forest (Rừng ngẫu nhiên) là hiện thân hoàn hảo nhất của Bagging.",
                        "2. Bản chất: Kết hợp lấy mẫu Bootstrap (rút thăm có hoàn lại) và ngẫu nhiên hóa đặc trưng (m = sqrt(d)) để làm mất tương quan giữa các cây, giúp GIẢM PHƯƠNG SAI (Variance) tối đa."
                    ]
                },
                {
                    "code": "Câu 34 VAIO: Tính Toán Entropy & Information Gain",
                    "problem": "Cách tính nhanh Entropy nhị phân và Information Gain trong phòng thi không dùng máy tính bỏ túi.",
                    "solution": [
                        "1. Ghi nhớ các mốc chuẩn: p = 0 hoặc 1 => H = 0; p = 0.5 => H = 1.0; p = 0.25 hoặc 0.75 => H ≈ 0.811 bit.",
                        "2. Luôn nhân trọng số số mẫu của từng nhánh: H(S|A) = (|S₁|/|S|) * H(S₁) + (|S₂|/|S|) * H(S₂).",
                        "3. Lấy Entropy nút cha trừ Entropy có điều kiện để ra IG."
                    ]
                },
                {
                    "code": "Câu 68 VAIO: Bias-Variance Trong Bagging vs Boosting",
                    "problem": "Tại sao Bagging dùng cây sâu trong khi Boosting lại dùng cây nông?",
                    "solution": [
                        "1. Bagging mục tiêu là GIẢM PHƯƠNG SAI (Variance): Cây sâu có Bias thấp nhưng Variance cao. Gom trung bình nhiều cây sâu độc lập sẽ triệt tiêu Variance mà vẫn giữ được Bias thấp.",
                        "2. Boosting mục tiêu là GIẢM ĐỘ LỆCH (Bias): Cây nông có Variance thấp nhưng Bias cao. Nối tiếp các cây nông sửa sai liên tiếp sẽ bào mòn Bias xuống thấp."
                    ]
                }
            ]
        },
        "takeaways": [
            "Cây quyết định phân hoạch không gian bằng các siêu phẳng trực giao song song với các trục tọa độ.",
            "Entropy đo độ hỗn loạn (cực đại 1.0 bit tại p = 0.5); Gini đo độ vẩn đục (cực đại 0.5 tại p = 0.5 và tính nhanh hơn).",
            "Thuật toán ID3 chọn thuộc tính có Information Gain lớn nhất; C4.5 dùng Gain Ratio để trị cạm bẫy thuộc tính ID.",
            "Pre-pruning (max_depth, min_samples_split) và Post-pruning (R_α(T) = R(T) + α|T|) giúp ngăn chặn Overfitting.",
            "Bagging (Random Forest) huấn luyện song song các cây sâu để GIẢM PHƯƠNG SAI; tỷ lệ mẫu OOB là (1-1/N)^N ≈ 36.8%.",
            "Boosting (XGBoost, AdaBoost) huấn luyện tuần tự các cây nông để dự đoán phần sai số dư nhằm GIẢM ĐỘ LỆCH."
        ]
    }
