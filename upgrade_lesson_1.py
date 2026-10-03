# -*- coding: utf-8 -*-
"""
upgrade_lesson_1.py - Generates an ultra-detailed, textbook-grade Masterpiece for Lesson 1:
'1. Đạo Hàm, Đạo Hàm Riêng & Vector Gradient'
Tailored specifically for 12th graders starting from absolute zero calculus knowledge.
"""

def get_masterpiece_lesson_1():
    return {
        "id": "lesson-1",
        "title": "1. Đạo Hàm, Đạo Hàm Riêng & Vector Gradient",
        "summary": "Khởi đầu từ con số 0: Nền tảng giải tích của toàn bộ ngành học máy. Dẫn dắt từng bước từ bản chất hàm số, giới hạn, vận tốc tức thời, đạo hàm, đạo hàm riêng nhiều biến, quy tắc chuỗi (Chain Rule) đến vector gradient chỉ hướng leo dốc và hạ dốc của hàm mất mát.",
        "syllabusBadge": "BUỔI 1: GIẢI TÍCH NỀN TẢNG & VECTOR GRADIENT",
        "intuition": {
            "title": "Trực giác thực tế: Dò đường xuống đáy thung lũng trong màn sương mù dày đặc",
            "content": "Hãy tưởng tượng bạn đang bị lạc trên một sườn núi gập ghềnh vào một buổi chiều muộn. Xung quanh sương mù dày đặc đến mức tầm nhìn của bạn chỉ đúng 1 mét quanh bàn chân. Bạn không thể nhìn thấy chân núi ở đâu, cũng không thấy đỉnh núi ở đâu. Nhiệm vụ sống còn của bạn là phải tìm đường xuống đáy thung lũng (nơi có làng mạc và nguồn nước). Bạn sẽ làm gì?\n\nCách duy nhất bạn có thể làm là dùng bàn chân cảm nhận độ dốc của mặt đất xung quanh mình 360 độ: hướng nào mặt đất dốc xuống mạnh nhất, bạn bước một bước ngắn về hướng đó. Sau khi bước xong, bạn lại dừng lại, cảm nhận độ dốc mới tại vị trí mới, và tiếp tục bước. Cứ lặp lại như vậy hàng trăm lần, từng bước một, bạn chắc chắn sẽ xuống tới đáy thung lũng!\n\nTrong Machine Learning, toàn bộ quá trình máy tính tự học diễn ra y hệt như vậy:\n- **Mặt đất sườn núi:** Chính là Hàm Mất Mát (Loss Function) đo mức độ sai lệch của mô hình.\n- **Độ dốc tại vị trí bạn đứng:** Chính là Đạo Hàm Riêng (Partial Derivatives) theo từng biến số.\n- **Hướng dốc xuống mạnh nhất:** Chính là Hướng Ngược Với Vector Gradient ($-\\nabla f$).\n- **Độ dài bước chân:** Chính là Tốc Độ Học (Learning Rate $\\eta$).\n- **Đáy thung lũng:** Chính là Điểm Cực Tiểu Toàn Cục (Global Minimum), nơi mô hình dự đoán chính xác nhất!"
        },
        "sections": [
            {
                "heading": "1.1. Bức Tranh Toàn Cảnh: Học Máy Là Gì? Phân Biệt Hồi Quy (Regression) vs Phân Loại (Classification)",
                "content": "Hãy tưởng tượng bạn đang dạy một đứa trẻ 3 tuổi nhận biết quả táo và quả cam. Bạn không dạy bằng cách đưa cho đứa trẻ một bảng công thức hình học: 'Nếu bán kính từ 3 đến 5 cm, bước sóng ánh sáng từ 620 đến 750 nm thì đó là quả táo'. Cách dạy đó là bất khả thi! Thay vào đó, bạn đưa cho đứa trẻ xem 10 quả táo thật và 10 quả cam thật, vừa chỉ vừa nói: 'Đây là táo', 'Đây là cam'. Sau vài lần quan sát, bộ não đứa trẻ tự động tổng quát hóa và nhận biết được quả nào là táo khi nhìn thấy một quả hoàn toàn mới. Đó chính xác là cách Học Máy (Machine Learning) ra đời.",
                "deepDive": """**1. So sánh Lập trình truyền thống vs Học máy:**
- **Lập trình truyền thống (Rule-based Programming):** Con người nắm rõ mọi quy tắc, ngồi gõ từng dòng mã lệnh: Dữ liệu (Data) + Quy tắc (Rules) $\\to$ Máy tính xuất ra Kết quả (Answers). Ví dụ: Tính lương công nhân: `Lương = Ngày công * 300.000 + Thưởng`.
- **Học máy (Machine Learning):** Con người KHÔNG biết hoặc không thể viết ra quy tắc toán học chính xác (ví dụ: làm sao viết hàng triệu lệnh if-else để nhận diện khuôn mặt bạn giữa 8 tỷ người?). Thay vào đó, con người nạp Dữ liệu (Data) + Kết quả mẫu (Answers) vào, máy tính sẽ dùng giải tích để TỰ ĐỘNG MÒ MẪM TÌM RA QUY TẮC $y = f(x)$!

**2. Hai nhánh bài toán cốt lõi trong Học Máy Có Giám Sát (Supervised Learning):**
Mọi bài toán học máy có giám sát đều được phân chia dựa trên bản chất của biến đầu ra $y$:

**Nhánh 1: Bài toán Hồi quy (Regression):**
- **Bản chất toán học:** Giá trị đầu ra $y$ là một con số thực liên tục ($y \\in \\mathbb{R}$). Con số này có thể nhận vô số giá trị thập phân lẻ trong một khoảng.
- **Ví dụ thực tiễn đời sống:**
  - Dự đoán giá bán một căn hộ chung cư (ví dụ: 3.45 tỷ, 3.46 tỷ VNĐ...).
  - Dự đoán thời gian tài xế Grab giao thức ăn đến nhà bạn (ví dụ: 18.5 phút, 19.2 phút).
  - Dự đoán điểm thi tốt nghiệp THPT môn Toán của học sinh (ví dụ: 8.75 điểm).
  - Dự đoán nồng độ bụi mịn PM2.5 trong không khí (ví dụ: 45.6 $\\mu\\text{g}/\\text{m}^3$).
- **Ý nghĩa hình học:** Tìm ra một đường cong hoặc mặt phẳng xấp xỉ liên tục đi xuyên qua đám mây dữ liệu sao cho khoảng cách sai số giữa các điểm thực tế tới đường dự đoán là nhỏ nhất.

**Nhánh 2: Bài toán Phân loại (Classification):**
- **Bản chất toán học:** Giá trị đầu ra $y$ là một nhãn danh mục rời rạc ($y \\in \\{0, 1\\}$ hoặc $y \\in \\{1, 2, \\dots, C\\}$). Máy tính phải phân chia đối tượng vào các nhóm cụ thể không thể chia nhỏ.
- **Ví dụ thực tiễn đời sống:**
  - Lọc Email: 'Thư rác (Spam = 1)' hay 'Hợp lệ (Ham = 0)'.
  - Chẩn đoán y khoa: Phim chụp X-quang phổi là 'Có u (1)' hay 'Bình thường (0)'.
  - Nhận diện chữ số viết tay từ ảnh: Nhãn thuộc tập hợp 10 chữ số rời rạc $\\{0, 1, 2, \\dots, 9\\}$.
  - Cảnh báo chất lượng không khí: Phân vào một trong 3 mức danh mục {Tốt, Trung bình, Nguy hại}.
- **Ý nghĩa hình học:** Tìm ra một ranh giới phân chia (Decision Boundary) cắt ngang không gian dữ liệu thành các vùng lãnh thổ độc lập cho từng nhãn.""",
                "formula": "\\text{Hồi quy: } y \\in \\mathbb{R} \\quad \\Longleftrightarrow \\quad \\text{Phân loại: } y \\in \\{0, 1, \\dots, C-1\\}",
                "mathExplainer": [
                    { "sym": "y \\in \\mathbb{R}", "name": "Số thực liên tục", "mean": "y thuộc tập số thực (Real numbers), có thể nhận vô số giá trị thập phân lẻ như 3.14, 0.005 hay -12.8." },
                    { "sym": "y \\in \\{0, 1\\}", "name": "Nhãn nhị phân", "mean": "y chỉ nhận một trong hai trạng thái đối lập rời rạc: 0 (Không/Âm tính) hoặc 1 (Có/Dương tính)." },
                    { "sym": "C \\ge 2", "name": "Số lớp phân loại", "mean": "Số lượng danh mục nhãn cần phân biệt trong bài toán phân loại đa lớp (Multiclass Classification)." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(30, 20)">
                        <text x="120" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Hồi Quy (Regression): Đầu ra liên tục y ∈ ℝ</text>
                        <line x1="20" y1="125" x2="220" y2="125" stroke="#111" stroke-width="1.5"/>
                        <line x1="20" y1="25" x2="20" y2="125" stroke="#111" stroke-width="1.5"/>
                        <line x1="30" y1="115" x2="210" y2="35" stroke="#111" stroke-width="2"/>
                        <circle cx="50" cy="100" r="3.5" fill="#111"/><circle cx="90" cy="90" r="3.5" fill="#111"/><circle cx="130" cy="60" r="3.5" fill="#111"/><circle cx="170" cy="50" r="3.5" fill="#111"/>
                        <text x="120" y="145" font-family="Georgia" font-size="10" text-anchor="middle">Đường xấp xỉ liên tục y = f(x)</text>
                      </g>
                      <g transform="translate(340, 20)">
                        <text x="120" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Phân Loại (Classification): Nhãn rời rạc y ∈ {0, 1}</text>
                        <line x1="20" y1="125" x2="220" y2="125" stroke="#111" stroke-width="1.5"/>
                        <line x1="20" y1="25" x2="20" y2="125" stroke="#111" stroke-width="1.5"/>
                        <line x1="30" y1="125" x2="200" y2="25" stroke="#111" stroke-dasharray="3,3" stroke-width="1.5"/>
                        <circle cx="60" cy="45" r="4" fill="#111"/><circle cx="90" cy="35" r="4" fill="#111"/><circle cx="70" cy="65" r="4" fill="#111"/>
                        <text x="75" y="25" font-family="Georgia" font-size="9">Lớp +1</text>
                        <circle cx="150" cy="95" r="4" fill="none" stroke="#111" stroke-width="2"/><circle cx="180" cy="110" r="4" fill="none" stroke="#111" stroke-width="2"/>
                        <text x="165" y="125" font-family="Georgia" font-size="9">Lớp 0</text>
                        <text x="120" y="145" font-family="Georgia" font-size="10" text-anchor="middle">Ranh giới phân chia (Decision Boundary)</text>
                      </g>
                    </svg>""",
                    "caption": "So sánh trực quan: Hồi quy dự đoán giá trị liên tục trên đường cong; Phân loại tìm đường ranh giới chia cắt các nhóm nhãn."
                },
                "commonPitfalls": "Cạm bẫy phòng thi kinh điển: Nhiều học sinh nhầm lẫn rằng bài toán dự đoán xác suất (ví dụ: dự đoán xác suất khách hàng click vào quảng cáo là 0.78) là bài toán Hồi quy vì 0.78 là số thực. SAI HOÀN TOÀN! Bản chất nhãn thực tế sau cùng chỉ có thể là 'Click (1)' hoặc 'Không click (0)' $\\implies$ Đây là bài toán PHÂN LOẠI NHỊ PHÂN. Con số 0.78 chỉ là mức độ tự tin của mô hình trước khi làm tròn thành nhãn.",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Một trạm quan trắc môi trường thông minh cần thực hiện 2 nhiệm vụ: (1) Dự đoán chính xác nồng độ bụi mịn PM2.5 vào lúc 12h trưa mai (tính bằng microgam/m³), và (2) Phát tín hiệu cảnh báo chất lượng không khí thuộc mức nào trong 3 mức {An toàn, Cảnh báo, Nguy hiểm}. Hai tác vụ này lần lượt thuộc nhóm học máy nào?",
                    "options": [
                        "A. Cả hai tác vụ đều là Hồi quy (Regression)",
                        "B. Tác vụ (1) là Phân loại (Classification); Tác vụ (2) là Hồi quy (Regression)",
                        "C. Tác vụ (1) là Hồi quy (Regression); Tác vụ (2) là Phân loại (Classification)",
                        "D. Cả hai tác vụ đều là Phân loại (Classification)"
                    ],
                    "correctIndex": 2,
                    "hint": "Hãy xem xét đầu ra: Đại lượng có thể nhận vô số giá trị thập phân liên tục (Hồi quy) hay là các danh mục được đặt tên tách rời (Phân loại)?",
                    "solution": [
                        "Bước 1: Phân tích tác vụ (1): Nồng độ bụi mịn PM2.5 là một số thực liên tục (ví dụ: 35.4, 35.5, 42.8 microgam/m³) $\\implies$ Đây là bài toán Hồi quy (Regression).",
                        "Bước 2: Phân tích tác vụ (2): Nhãn cảnh báo thuộc tập hợp 3 danh mục rời rạc {An toàn, Cảnh báo, Nguy hiểm} $\\implies$ Đây là bài toán Phân loại đa lớp (Multiclass Classification).",
                        "Kết luận: Đáp án chính xác là C."
                    ]
                }
            },
            {
                "heading": "1.2. Khởi Đầu Từ Con Số 0: Bản Chất Hàm Số, Giới Hạn (Limit) & Các Hàm Số Cốt Lõi Trong AI",
                "content": "Nhiều bạn học sinh khi nhìn vào công thức toán học thường cảm thấy sợ hãi vì những ký hiệu lạ lẫm. Đừng lo! Hãy cùng bóc tách từng khái niệm từ nguồn gốc trực giác nguyên bản nhất: Hàm số thực chất là gì? Giới hạn sinh ra để làm gì? Và tại sao các nhà nghiên cứu AI lại chọn những hàm số đặc biệt như Sigmoid, ReLU hay hàm bậc hai?",
                "deepDive": """**1. Hàm số (Function) thực chất là gì?**
Hàm số $y = f(x)$ không có gì thần bí: nó giống như một cỗ máy tự động hóa trong một xưởng sản xuất:
- Bạn ném vào cỗ máy một nguyên liệu đầu vào $x$ (gọi là Input hay biến số độc lập).
- Cỗ máy thực hiện một quy tắc biến đổi cố định bên trong.
- Cỗ máy đẩy ra một thành phẩm $y$ (gọi là Output hay giá trị hàm số).
*Ví dụ:* Máy tính tiền cước taxi: $f(x) = 15000 + 12000 \\cdot x$. Nếu bạn đi $x = 3$ km, máy nhả ra $y = 15000 + 12000(3) = 51000$ VNĐ.

**2. Phân biệt Biến số (Variables) và Tham số (Parameters):**
Trong Machine Learning, một hàm số thường được viết dưới dạng $y = f(x; w, b)$:
- $x$: Biến số đầu vào (Dữ liệu khách hàng, người dùng đưa vào, mô hình không thể tự sửa dữ liệu này).
- $w$ (Weight - trọng số) và $b$ (Bias - độ lệch): Là các 'núm vặn' nằm bên trong cỗ máy! Ban đầu máy vặn bừa khiến kết quả sai bét. Quá trình 'huấn luyện mô hình' (Training) thực chất là tự động xoay các núm vặn $w$ và $b$ cho đến khi máy tính ra kết quả chuẩn xác nhất!

**3. Giới hạn (Limit) là gì? Tại sao phải cần giới hạn?**
Hãy tưởng tượng bạn đang bước những bước chân ngày càng lại gần một bờ sông tại vị trí $x = a$. Giới hạn $\\lim_{x \\to a} f(x)$ trả lời câu hỏi: Khi bạn bước cực kỳ gần sát tới $a$, giá trị của $f(x)$ đang nhắm tới con số nào?
Tại sao phải cần khái niệm này? Hãy xét biểu thức:
$$g(x) = \\frac{x^2 - 4}{x - 2}$$
- Nếu bạn cắm trực tiếp $x = 2$ vào: Mẫu số bằng $2 - 2 = 0$, tử số bằng $2^2 - 4 = 0$. Máy tính sẽ báo lỗi sập chương trình ngay lập tức vì phép chia cho $0$ không xác định!
- Nhưng nếu bạn cho $x$ tiến sát 2 mà không bằng 2 (ví dụ $x = 2.001$ thì $g(x) = 4.001$; $x = 1.999$ thì $g(x) = 3.999$):
Ta phân tích: $\\frac{x^2 - 4}{x - 2} = \\frac{(x - 2)(x + 2)}{x - 2} = x + 2$.
Khi $x$ tiến sát tới 2, giá trị $x + 2$ tiến sát tới $4$! Ta viết: $\\lim_{x \\to 2} \\frac{x^2 - 4}{x - 2} = 4$.
*Bản chất:* Giới hạn cho phép các nhà toán học nhìn thấy xu hướng vận động của những đại lượng vô cùng bé mà không bị mắc kẹt bởi lỗi chia cho 0!

**4. Năm hàm số kinh điển mà mọi kỹ sư AI bắt buộc phải biết:**

**a) Hàm bậc hai (Parabol) $f(x) = x^2$:**
- Hình dáng: Một chiếc lòng chảo đối xứng có đáy sâu nhất tại $x = 0$.
- Ứng dụng trong AI: Đây là dạng của Hàm mất mát bình phương trung bình (MSE). Khi mô hình dự đoán sai, sai số bị bình phương lên: sai lệch 2 đơn vị bị phạt $2^2 = 4$, sai lệch 5 đơn vị bị phạt $5^2 = 25$! Bình phương vừa làm triệt tiêu dấu âm, vừa phạt cực nặng những dự đoán lệch nhiều.

**b) Hàm mũ $e^x$ và hằng số Euler $e \\approx 2.71828$:**
- Tính chất: Luôn dương ($e^x > 0$ với mọi $x$). Tăng trưởng bùng nổ theo cấp số nhân.
- Đạo hàm kỳ diệu: $(e^x)' = e^x$ (Tốc độ tăng trưởng bằng chính giá trị hiện tại của nó).

**c) Hàm Logarit tự nhiên $\\ln(x)$ (Logarit cơ số $e$):**
- Điều kiện: Chỉ xác định khi $x > 0$. Khi $x \\to 1$ thì $\\ln(1) = 0$. Khi $x \\to 0^+$ thì $\\ln(x) \\to -\\infty$.
- Ứng dụng trong AI: Dùng làm hàm mất mát Cross-Entropy Loss trong phân loại. Nếu xác suất dự đoán đúng $p = 1$, Loss $= -\\ln(1) = 0$ (không phạt). Nếu xác suất dự đoán đúng $p \\to 0$, Loss $= -\\ln(p) \\to +\\infty$ (phạt vô hạn)!

**d) Hàm Sigmoid $\\sigma(z) = \\frac{1}{1 + e^{-z}}$:**
- Đặc tính: Nhận bất kỳ số thực nào từ $-\\infty$ đến $+\\infty$ và 'nén' chặt lại vào khoảng an toàn $(0, 1)$.
- Ứng dụng trong AI: Biến giá trị thô thành 'xác suất' trong phân loại nhị phân (Logistic Regression) và mạng nơ-ron.

**e) Hàm ReLU (Rectified Linear Unit) $f(x) = \\max(0, x)$:**
- Đặc tính: Nếu $x < 0$, giá trị bằng 0. Nếu $x \\ge 0$, giá trị bằng chính $x$.
- Ứng dụng trong AI: Là hàm kích hoạt được sử dụng nhiều nhất trong thị giác máy tính và học sâu vì đạo hàm cực kỳ đơn giản (bằng 1 khi $x>0$), giúp máy tính huấn luyện nhanh gấp hàng chục lần so với Sigmoid.""",
                "formula": "\\sigma(z) = \\frac{1}{1 + e^{-z}}, \\quad \\text{ReLU}(z) = \\max(0, z), \\quad \\text{MSE}(w) = \\frac{1}{2}(w \\cdot x - y)^2",
                "mathExplainer": [
                    { "sym": "\\lim_{x \\to a}", "name": "Giới hạn (Limit)", "mean": "Mô tả giá trị mà hàm số tiến gần tới khi biến x tiến sát vô cùng gần điểm a." },
                    { "sym": "e \\approx 2.718", "name": "Hằng số Euler", "mean": "Hằng số toán học tự nhiên, cơ sở của hàm mũ e^x và logarit tự nhiên ln(x)." },
                    { "sym": "\\sigma(z)", "name": "Hàm Sigmoid", "mean": "Hàm nén giá trị số thực bất kỳ về khoảng xác suất (0, 1)." },
                    { "sym": "\\max(0, z)", "name": "Hàm ReLU", "mean": "Hàm kích hoạt trả về 0 nếu z âm, và giữ nguyên z nếu z dương." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(20, 20)">
                        <text x="80" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">1. Parabol y = x² (MSE)</text>
                        <line x1="20" y1="125" x2="140" y2="125" stroke="#111" stroke-width="1"/>
                        <line x1="80" y1="25" x2="80" y2="125" stroke="#111" stroke-width="1"/>
                        <path d="M 30 45 Q 80 135 130 45" fill="none" stroke="#111" stroke-width="2"/>
                        <text x="80" y="145" font-family="Georgia" font-size="9" text-anchor="middle">Đáy thung lũng x = 0</text>
                      </g>
                      <g transform="translate(210, 20)">
                        <text x="90" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">2. Sigmoid σ(z) = 1/(1+e⁻ᶻ)</text>
                        <line x1="20" y1="125" x2="160" y2="125" stroke="#111" stroke-width="1"/>
                        <line x1="90" y1="25" x2="90" y2="125" stroke="#111" stroke-width="1"/>
                        <line x1="20" y1="35" x2="160" y2="35" stroke="#bbb" stroke-dasharray="2,2"/>
                        <text x="170" y="38" font-family="Georgia" font-size="8">y=1</text>
                        <path d="M 25 120 C 70 120 70 40 155 40" fill="none" stroke="#111" stroke-width="2"/>
                        <circle cx="90" cy="80" r="3" fill="#111"/>
                        <text x="110" y="80" font-family="Georgia" font-size="8">σ(0)=0.5</text>
                        <text x="90" y="145" font-family="Georgia" font-size="9" text-anchor="middle">Nén vào (0, 1)</text>
                      </g>
                      <g transform="translate(420, 20)">
                        <text x="80" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">3. ReLU y = max(0, z)</text>
                        <line x1="20" y1="125" x2="140" y2="125" stroke="#111" stroke-width="1"/>
                        <line x1="80" y1="25" x2="80" y2="125" stroke="#111" stroke-width="1"/>
                        <line x1="20" y1="125" x2="80" y2="125" stroke="#111" stroke-width="3"/>
                        <line x1="80" y1="125" x2="140" y2="45" stroke="#111" stroke-width="2.5"/>
                        <text x="80" y="145" font-family="Georgia" font-size="9" text-anchor="middle">Gãy khúc tại 0</text>
                      </g>
                    </svg>""",
                    "caption": "Ba hàm số trụ cột trong Học máy: Parabol bình phương lỗi (MSE), Sigmoid nén xác suất, và ReLU kích hoạt nơ-ron."
                },
                "commonPitfalls": "Cạm bẫy toán học: Giá trị của hàm Sigmoid $\\sigma(z)$ KHÔNG BAO GIỜ chạm tới 0 hoặc 1, nó luôn nằm nghiêm ngặt trong khoảng $(0, 1)$. Tại $z = 0$: $\\sigma(0) = \\frac{1}{1 + e^0} = \\frac{1}{1 + 1} = 0.5$. Con số 0.5 mang ý nghĩa mô hình hoàn toàn phân vân 50-50 giữa hai nhãn!",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Trong một mô hình phân loại nhị phân dự đoán bệnh nhân có mắc bệnh hay không, nơ-ron đầu ra tính được giá trị tổng z = 0. Giá trị xác suất dự đoán sau khi qua hàm kích hoạt Sigmoid σ(z) bằng bao nhiêu và mang ý nghĩa gì?",
                    "options": [
                        "A. Bằng 0: Chắc chắn bệnh nhân không mắc bệnh",
                        "B. Bằng 0.5: Mô hình hoàn toàn phân vân giữa việc có bệnh và không bệnh (xác suất 50%)",
                        "C. Bằng 1: Chắc chắn bệnh nhân mắc bệnh",
                        "D. Bằng không xác định vì mẫu số bị chia cho 0"
                    ],
                    "correctIndex": 1,
                    "hint": "Thay z = 0 vào công thức Sigmoid: e⁰ = 1, mẫu số là 1 + 1 = 2.",
                    "solution": [
                        "Bước 1: Áp dụng công thức hàm Sigmoid: σ(z) = 1 / (1 + e^(-z)).",
                        "Bước 2: Thay z = 0: e^(-0) = e^0 = 1. Mẫu số = 1 + 1 = 2.",
                        "Bước 3: Ta được σ(0) = 1 / 2 = 0.5.",
                        "Ý nghĩa thực tế: Giá trị 0.5 nằm chính giữa ranh giới, thể hiện mô hình đánh giá cơ hội mắc bệnh và không mắc bệnh là ngang nhau (50% - 50%).",
                        "Đáp án chính xác: B."
                    ]
                }
            },
            {
                "heading": "1.3. Bản Chất Đạo Hàm (Derivative): Từ Vận Tốc Tức Thời Đến Hệ Số Góc Tiếp Tuyến & Điểm Cực Trị",
                "content": "Bạn đã bao giờ thắc mắc: Làm thế nào đồng hồ đo tốc độ của xe máy (công-tơ-mét) có thể chỉ ra đúng con số 45 km/h tại đúng một giây cụ thể, trong khi để tính vận tốc ta luôn cần 'quãng đường chia cho thời gian'? Nếu tại đúng 1 tích tắc, thời gian chưa trôi đi (Δt = 0), quãng đường chưa dịch chuyển (Δs = 0), làm sao chia được 0 cho 0? Câu trả lời mở ra toàn bộ nền văn minh giải tích: ĐẠO HÀM.",
                "deepDive": """**1. Trực giác vật lý: Vận tốc trung bình vs Vận tốc tức thời:**
- Vận tốc trung bình trong khoảng thời gian $\\Delta t$: $v_{tb} = \\frac{\\Delta s}{\\Delta t} = \\frac{s(t + \\Delta t) - s(t)}{\\Delta t}$. Con số này chỉ cho ta biết bức tranh tổng thể, không phản ánh xe đang phóng nhanh hay dừng lại trong từng khoảnh khắc.
- Vận tốc tức thời tại thời điểm $t$: Hãy cho khoảng thời gian $\\Delta t$ co lại thật bé: 0.1 giây, 0.001 giây, $0.000001$ giây... Khi $\\Delta t \\to 0$, tỉ số $\\frac{\\Delta s}{\\Delta t}$ không biến mất mà hội tụ về một con số xác định duy nhất! Con số đó chính là **Vận tốc tức thời**:
$$v(t) = s'(t) = \\lim_{\\Delta t \\to 0} \\frac{s(t + \\Delta t) - s(t)}{\\Delta t}$$

**2. Định nghĩa hình học của Đạo hàm: Cát tuyến biến thành Tiếp tuyến:**
Xét đồ thị hàm số $y = f(x)$:
- Lấy hai điểm $A(x, f(x))$ và $B(x + \\Delta x, f(x + \\Delta x))$. Đường thẳng nối $A$ và $B$ gọi là một **đường cát tuyến** (cắt đồ thị tại 2 điểm).
- Độ dốc (hệ số góc) của cát tuyến $AB$ là: $k_{\\text{cát tuyến}} = \\frac{f(x + \\Delta x) - f(x)}{\\Delta x}$.
- Bây giờ, hãy cho điểm $B$ trượt dọc theo đường cong tiến sát về điểm $A$ (tương ứng $\\Delta x \\to 0$). Đường thẳng cát tuyến sẽ xoay dần và khi $B$ chạm khít vào $A$, nó trở thành **ĐƯỜNG TIẾP TUYẾN (Tangent line)** của đồ thị tại điểm $A$!
- **Kết luận hình học tối cao:** Đạo hàm $f'(x)$ chính là HỆ SỐ GÓC (ĐỘ DỐC) của đường tiếp tuyến tại điểm $x$.

**3. Ý nghĩa sống còn của Dấu đạo hàm:**
Hệ số góc của tiếp tuyến cho ta biết chính xác xu hướng thay đổi của hàm số:
- **Nếu $f'(x) > 0$:** Tiếp tuyến nghiêng lên từ trái sang phải $\\implies$ Khi $x$ tăng thì $f(x)$ TĂNG (Đồ thị đang leo dốc, hàm đồng biến).
- **Nếu $f'(x) < 0$:** Tiếp tuyến dốc xuống từ trái sang phải $\\implies$ Khi $x$ tăng thì $f(x)$ GIẢM (Đồ thị đang xuống dốc, hàm nghịch biến).
- **Nếu $f'(x) = 0$:** Tiếp tuyến nằm ngang hoàn toàn (song song trục hoành, độ dốc bằng 0) $\\implies$ Đồ thị tạm thời bằng phẳng! Đây chính là vị trí của **ĐIỂM CỰC TRỊ**:
  - Nếu đồ thị từ dốc xuống ($f' < 0$) chuyển qua bằng phẳng ($f' = 0$) rồi dốc lên ($f' > 0$): Đó là **Đáy cực tiểu (Local Minimum)** - Nơi hàm mất mát đạt giá trị nhỏ nhất!
  - Nếu đồ thị từ dốc lên chuyển qua bằng phẳng rồi dốc xuống: Đó là **Đỉnh cực đại (Local Maximum)**.

**4. Bảng quy tắc đạo hàm cơ bản giải thích cặn kẽ:**
- $(c)' = 0$: Đạo hàm của hằng số bằng 0 (vì một con số cố định không thay đổi, tốc độ biến thiên phải bằng 0).
- $(x^n)' = n \\cdot x^{n-1}$: Quy tắc lũy thừa (Ví dụ: $(x^2)' = 2x$, $(x^3)' = 3x^2$, $(x)' = 1$).
- $(c \\cdot f(x))' = c \\cdot f'(x)$: Hằng số nhân giữ nguyên (Ví dụ: $(5x^2)' = 5 \\cdot (2x) = 10x$).
- $(u \\pm v)' = u' \\pm v'$: Đạo hàm của tổng bằng tổng các đạo hàm.
- $(e^x)' = e^x$: Đạo hàm hàm mũ tự nhiên giữ nguyên.
- $(\\ln x)' = \\frac{1}{x}$: Đạo hàm của logarit tự nhiên.

**5. Ví dụ số học hoàn chỉnh từng bước tính tay:**
Giả sử hàm mất mát của mô hình hồi quy một tham số $w$ là: $L(w) = 2w^2 - 8w + 11$.
Ta muốn tìm giá trị trọng số $w$ sao cho hàm lỗi $L$ đạt cực tiểu (sai số nhỏ nhất).
- **Bước 1: Tính đạo hàm $L'(w)$:**
  $L'(w) = \\frac{d}{dw}(2w^2 - 8w + 11) = 2(2w) - 8(1) + 0 = 4w - 8$.
- **Bước 2: Phân tích độ dốc tại điểm ban đầu $w = 0$:**
  $L'(0) = 4(0) - 8 = -8 < 0$.
  Độ dốc là số âm (tiếp tuyến đang dốc xuống) $\\implies$ Nếu ta TĂNG $w$ lên thì hàm Loss sẽ GIẢM xuống!
- **Bước 3: Tìm điểm đáy cực tiểu:**
  Đáy cực tiểu xảy ra khi tiếp tuyến nằm ngang: $L'(w) = 0$.
  $4w - 8 = 0 \\iff 4w = 8 \\iff w = 2$.
- **Bước 4: Tính giá trị cực tiểu của Loss:**
  $L(2) = 2(2^2) - 8(2) + 11 = 2(4) - 16 + 11 = 8 - 16 + 11 = 3$.
  Như vậy, trọng số tối ưu là $w = 2$ và sai số thấp nhất có thể đạt được là $3$.""",
                "formula": "f'(x) = \\lim_{\\Delta x \\to 0} \\frac{f(x + \\Delta x) - f(x)}{\\Delta x}, \\quad L'(w) = 0 \\iff \\text{Điểm dừng (Extremum)}",
                "mathExplainer": [
                    { "sym": "f'(x) = \\frac{df}{dx}", "name": "Đạo hàm bậc một", "mean": "Hệ số góc của tiếp tuyến tại điểm x, đo tốc độ thay đổi tức thời của hàm f." },
                    { "sym": "\\Delta x \\to 0", "name": "Gia số tiến về 0", "mean": "Khoảng dịch chuyển vô cùng nhỏ trên trục hoành." },
                    { "sym": "L'(w) = 0", "name": "Điều kiện cực trị", "mean": "Tiếp tuyến nằm ngang hoàn toàn, hàm số đạt cực đại hoặc cực tiểu." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 20)">
                        <text x="120" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Cát Tuyến → Tiếp Tuyến (Tangent)</text>
                        <line x1="20" y1="125" x2="220" y2="125" stroke="#111" stroke-width="1"/>
                        <line x1="20" y1="25" x2="20" y2="125" stroke="#111" stroke-width="1"/>
                        <path d="M 30 115 Q 120 110 200 35" fill="none" stroke="#111" stroke-width="2"/>
                        <circle cx="80" cy="100" r="3.5" fill="#111"/><text x="75" y="115" font-family="Georgia" font-size="9">A(x)</text>
                        <circle cx="150" cy="65" r="3" fill="#888"/><text x="155" y="75" font-family="Georgia" font-size="9">B</text>
                        <line x1="50" y1="115" x2="190" y2="45" stroke="#888" stroke-dasharray="2,2" stroke-width="1.2"/>
                        <line x1="40" y1="125" x2="160" y2="45" stroke="#111" stroke-width="2"/>
                        <text x="120" y="145" font-family="Georgia" font-size="9" text-anchor="middle">Tiếp tuyến tại A có hệ số góc f'(x)</text>
                      </g>
                      <g transform="translate(340, 20)">
                        <text x="120" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Dấu Đạo Hàm &amp; Đáy Cực Tiểu L'(w) = 0</text>
                        <path d="M 40 40 Q 120 140 200 40" fill="none" stroke="#111" stroke-width="2"/>
                        <line x1="60" y1="110" x2="180" y2="110" stroke="#111" stroke-dasharray="3,3" stroke-width="1.5"/>
                        <circle cx="120" cy="110" r="4.5" fill="#111"/>
                        <text x="120" y="130" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Đáy Cực Tiểu: L'(w) = 0</text>
                        <text x="60" y="70" font-family="Georgia" font-size="9">L'(w) &lt; 0 (Dốc xuống)</text>
                        <text x="180" y="70" font-family="Georgia" font-size="9">L'(w) &gt; 0 (Dốc lên)</text>
                      </g>
                    </svg>""",
                    "caption": "Trực quan hóa đạo hàm: Cát tuyến biến thành tiếp tuyến khi khoảng cách tiến về 0; Điểm đáy cực tiểu có tiếp tuyến nằm ngang."
                },
                "commonPitfalls": "Nhầm lẫn tai hại: Nhiều học sinh nghĩ rằng tại điểm cực tiểu thì giá trị hàm số phải bằng 0 ($L(w) = 0$). SAI! Tại điểm cực tiểu, ĐẠO HÀM bằng 0 ($L'(w) = 0$), còn bản thân hàm số $L(w)$ có thể nhận giá trị bằng 3, 10 hay bất kỳ con số nào!",
                "practiceQuestion": {
                    "level": "Vận dụng",
                    "question": "Cho hàm mất mát của một mô hình học máy: L(w) = 5w² - 30w + 50. Giá trị trọng số w tối ưu để hàm mất mát đạt giá trị nhỏ nhất (cực tiểu) bằng bao nhiêu?",
                    "options": [
                        "A. w = 0",
                        "B. w = 6",
                        "C. w = 3",
                        "D. w = 5"
                    ],
                    "correctIndex": 2,
                    "hint": "Tính đạo hàm L'(w), cho L'(w) = 0 và giải phương trình bậc nhất tìm w.",
                    "solution": [
                        "Bước 1: Tính đạo hàm của L(w): L'(w) = d/dw (5w² - 30w + 50) = 10w - 30.",
                        "Bước 2: Tìm điểm cực tiểu bằng cách giải phương trình L'(w) = 0: 10w - 30 = 0 <=> 10w = 30 <=> w = 3.",
                        "Bước 3: Kiểm tra đạo hàm bậc hai: L''(w) = 10 > 0 => w = 3 chắc chắn là điểm cực tiểu.",
                        "Đáp án chính xác: C (w = 3)."
                    ]
                }
            },
            {
                "heading": "1.4. Đạo Hàm Riêng (Partial Derivatives) Cho Hàm Nhiều Biến & Kỹ Thuật 'Đóng Băng'",
                "content": "Trong thế giới thực, một ngôi nhà không bao giờ chỉ có một thuộc tính. Giá nhà phụ thuộc cùng lúc vào Diện tích (x₁), Số phòng ngủ (x₂), Khoảng cách đến trường học (x₃),... Trong mạng nơ-ron học sâu (Deep Learning), một mô hình có thể có hàng triệu đến hàng tỷ trọng số w₁, w₂, ..., wₙ. Làm thế nào để biết trọng số w₅₀₀ đang làm tăng hay giảm sai số của mô hình khi tất cả các trọng số khác đều đang cùng biến động?",
                "deepDive": """**1. Vấn đề của hàm nhiều biến:**
Một hàm số nhiều biến có dạng $z = f(x, y)$ hoặc $L(w_1, w_2, \\dots, w_n)$.
Nếu cả $x$ và $y$ cùng thay đổi cùng lúc, ta sẽ rơi vào mớ bòng bong không thể đo đếm được nguyên nhân sai số đến từ biến nào.

**2. Ý tưởng thiên tài: Kỹ thuật 'Đóng băng' (Freezing):**
Các nhà toán học đưa ra giải pháp trực quan và thông minh bậc nhất:
Muốn đo độ dốc theo biến nào, hãy **ĐÓNG BĂNG TẤT CẢ CÁC BIẾN CÒN LẠI**, coi chúng như những con số hằng số cố định bất di bất dịch (như số 5, số 10), và chỉ cho duy nhất một biến đó cựa quậy!
Phép đạo hàm đặc biệt này được gọi là **ĐẠO HÀM RIÊNG (Partial Derivative)**.

**3. Ký hiệu chữ cong $\\partial$ (Del):**
- Đối với hàm một biến $y = f(x)$, ta dùng chữ $d$ thẳng: $\\frac{df}{dx}$.
- Đối với hàm nhiều biến, ta bắt buộc phải dùng ký hiệu chữ cong $\\partial$ (đọc là 'del' hoặc 'partial'):
  - $\\frac{\\partial f}{\\partial x}$: Đạo hàm riêng của $f$ theo biến $x$ (giữ $y, z...$ cố định).
  - $\\frac{\\partial f}{\\partial y}$: Đạo hàm riêng của $f$ theo biến $y$ (giữ $x, z...$ cố định).

**4. Ý nghĩa hình học trong không gian 3 chiều:**
Đồ thị của hàm số hai biến $z = f(x, y)$ là một mặt cong 3D (như một quả đồi hoặc chiếc võng):
- Khi bạn đứng tại một điểm trên quả đồi, có vô số hướng đi 360 độ xung quanh.
- $\\frac{\\partial f}{\\partial x}$: Chính là độ dốc của mặt đồi khi bạn CHỈ đi dọc theo trục Tây - Đông (giữ nguyên vĩ độ Bắc - Nam).
- $\\frac{\\partial f}{\\partial y}$: Chính là độ dốc của mặt đồi khi bạn CHỈ đi dọc theo trục Nam - Bắc (giữ nguyên kinh độ Tây - Đông).

**5. Bài toán thực hành tính tay chi tiết từng chữ số một:**
Cho hàm số: $f(x, y) = 3x^2 y^3 + 5x^3 - 4y^2 + 7xy - 12$.

**Bước 1: Tính $\\frac{\\partial f}{\\partial x}$ (Coi $y$ như hằng số):**
- Xét hạng tử $3x^2 y^3$: Vì $y$ là hằng số, nên $3y^3$ là một cụm số hằng đứng trước $x^2$. Ta giữ nguyên $3y^3$ và đạo hàm $x^2$ thành $2x$:
  $\\frac{\\partial}{\\partial x}(3x^2 y^3) = (3y^3) \\cdot (2x) = 6x y^3$.
- Xét hạng tử $5x^3$: Đạo hàm bình thường theo $x$ $\\implies 5(3x^2) = 15x^2$.
- Xét hạng tử $-4y^2$: Chú ý! Biểu thức này CHỈ CHỨA $y$, không chứa biến $x$. Đối với $x$, nó là một con số cố định $\\implies$ Đạo hàm của hằng số bằng $0$!
- Xét hạng tử $7xy$: Coi $7y$ là hằng số, đạo hàm $x$ bằng 1 $\\implies 7y(1) = 7y$.
- Xét hạng tử $-12$: Hằng số $\\implies 0$.
$\\implies \\mathbf{\\frac{\\partial f}{\\partial x} = 6xy^3 + 15x^2 + 7y}$.

**Bước 2: Tính $\\frac{\\partial f}{\\partial y}$ (Coi $x$ như hằng số):**
- Xét hạng tử $3x^2 y^3$: Vì $x$ là hằng số, cụm $3x^2$ là hằng số đứng trước $y^3$. Đạo hàm $y^3$ thành $3y^2$:
  $\\frac{\\partial}{\\partial y}(3x^2 y^3) = (3x^2) \\cdot (3y^2) = 9x^2 y^2$.
- Xét hạng tử $5x^3$: Không chứa $y$, hoàn toàn là hằng số đối với $y \\implies 0$!
- Xét hạng tử $-4y^2$: Đạo hàm theo $y$ $\\implies -4(2y) = -8y$.
- Xét hạng tử $7xy$: Coi $7x$ là hằng số, đạo hàm $y$ bằng 1 $\\implies 7x(1) = 7x$.
- Xét hạng tử $-12$: Hằng số $\\implies 0$.
$\\implies \\mathbf{\\frac{\\partial f}{\\partial y} = 9x^2 y^2 - 8y + 7x}$.

**Bước 3: Thay số tại điểm $(x = 1, y = 2)$:**
- $\\frac{\\partial f}{\\partial x}(1, 2) = 6(1)(2^3) + 15(1^2) + 7(2) = 6(8) + 15 + 14 = 48 + 29 = 77$.
- $\\frac{\\partial f}{\\partial y}(1, 2) = 9(1^2)(2^2) - 8(2) + 7(1) = 9(4) - 16 + 7 = 36 - 16 + 7 = 27$.

**6. Điều kiện cực trị của hàm nhiều biến:**
Một điểm $(x^*, y^*)$ là điểm cực tiểu/cực đại thì TẤT CẢ các tiếp tuyến theo mọi phương đều phải nằm ngang đồng thời, nghĩa là mọi đạo hàm riêng phải bằng 0:
$$\\begin{cases} \\frac{\\partial f}{\\partial x} = 0 \\\\ \\frac{\\partial f}{\\partial y} = 0 \\end{cases}$$""",
                "formula": "\\frac{\\partial f}{\\partial x_i} = \\lim_{\\Delta x_i \\to 0} \\frac{f(x_1, \\dots, x_i + \\Delta x_i, \\dots, x_n) - f(x_1, \\dots, x_i, \\dots, x_n)}{\\Delta x_i}",
                "mathExplainer": [
                    { "sym": "\\partial", "name": "Ký hiệu Del", "mean": "Biểu thị đạo hàm riêng cho hàm nhiều biến, chỉ phẩy theo một biến duy nhất." },
                    { "sym": "\\frac{\\partial f}{\\partial x}", "name": "Đạo hàm theo x", "mean": "Đo tốc độ biến thiên khi chỉ có biến x dịch chuyển, giữ nguyên tất cả biến còn lại." },
                    { "sym": "\\frac{\\partial f}{\\partial y}", "name": "Đạo hàm theo y", "mean": "Đo tốc độ biến thiên khi chỉ có biến y dịch chuyển, giữ nguyên tất cả biến còn lại." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(60, 20)">
                        <text x="140" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Thiết Diện Mặt Cắt 3D Của Đạo Hàm Riêng</text>
                        <path d="M 40 120 Q 140 20 240 120" fill="none" stroke="#111" stroke-width="2"/>
                        <line x1="80" y1="45" x2="200" y2="45" stroke="#111" stroke-dasharray="3,3" stroke-width="1.5"/>
                        <circle cx="140" cy="45" r="4" fill="#111"/>
                        <text x="140" y="35" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Điểm Cực Trị: ∂f/∂x = 0 và ∂f/∂y = 0</text>
                        <line x1="50" y1="125" x2="110" y2="65" stroke="#888" stroke-width="1.5"/>
                        <circle cx="80" cy="95" r="3.5" fill="#111"/>
                        <text x="50" y="80" font-family="Georgia" font-size="9">Độ dốc ∂f/∂x &gt; 0</text>
                      </g>
                      <g transform="translate(360, 30)">
                        <text x="0" y="20" font-family="Georgia" font-size="11" font-weight="bold">Quy tắc vàng đóng băng biến số:</text>
                        <text x="0" y="45" font-family="Georgia" font-size="10">• Phẩy theo x: coi y, z, w là con số hằng.</text>
                        <text x="0" y="65" font-family="Georgia" font-size="10">• Phẩy theo y: coi x, z, w là con số hằng.</text>
                        <text x="0" y="90" font-family="Georgia" font-size="11" font-weight="bold">Ví dụ: f(x, y) = 3x²y + 5y³</text>
                        <text x="10" y="110" font-family="Georgia" font-size="10">∂f/∂x = 3(2x)y + 0 = 6xy</text>
                        <text x="10" y="128" font-family="Georgia" font-size="10">∂f/∂y = 3x²(1) + 15y² = 3x² + 15y²</text>
                      </g>
                    </svg>""",
                    "caption": "Ý nghĩa hình học của đạo hàm riêng: Độ dốc của mặt cong khi cắt bởi mặt phẳng song song với trục Ox hoặc Oy."
                },
                "commonPitfalls": "Lỗi sai chết người: Khi đạo hàm theo $x$, gặp hạng tử chỉ chứa $y$ (như $7y^3$) thì vội vàng viết là $21y^2$. SAI NẶNG! Đối với $x$, toàn bộ $7y^3$ là một hằng số độc lập, đạo hàm của nó bắt buộc phải bằng 0!",
                "practiceQuestion": {
                    "level": "Vận dụng",
                    "question": "Cho hàm mất mát của mô hình hai tham số: L(w₁, w₂) = 4w₁² - 2w₁w₂ + 3w₂² - 8w₁ + 5. Đạo hàm riêng của hàm số này theo biến w₁ tại điểm (w₁ = 2, w₂ = 1) có giá trị bằng bao nhiêu?",
                    "options": [
                        "A. 14",
                        "B. 6",
                        "C. -2",
                        "D. 10"
                    ],
                    "correctIndex": 1,
                    "hint": "Coi w₂ là hằng số, tính đạo hàm theo w₁: d/dw₁(4w₁²) = 8w₁; d/dw₁(-2w₁w₂) = -2w₂; d/dw₁(3w₂² + 5) = 0.",
                    "solution": [
                        "Bước 1: Tính đạo hàm riêng ∂L/∂w₁ bằng cách coi w₂ là hằng số:",
                        "  - Đạo hàm của 4w₁² theo w₁ là: 8w₁.",
                        "  - Đạo hàm của -2w₁w₂ theo w₁ là: -2w₂ (vì w₂ là hằng số nhân phía sau).",
                        "  - Đạo hàm của 3w₂² và 5 theo w₁ bằng 0 (vì không chứa biến w₁).",
                        "  - Đạo hàm của -8w₁ theo w₁ là: -8.",
                        "  => Ta được: ∂L/∂w₁ = 8w₁ - 2w₂ - 8.",
                        "Bước 2: Thay tọa độ điểm (w₁=2, w₂=1) vào công thức vừa tìm được:",
                        "  ∂L/∂w₁(2, 1) = 8(2) - 2(1) - 8 = 16 - 2 - 8 = 6.",
                        "Đáp án chính xác: B (6)."
                    ]
                }
            },
            {
                "heading": "1.5. Hàm Hợp & Quy Tắc Chuỗi (Chain Rule) - Trái Tim Của Lan Truyền Ngược (Backpropagation)",
                "content": "Một chiếc ô tô hiện đại không bao giờ nối trực tiếp chân ga tới bánh xe bằng một thanh sắt đơn giản. Khi bạn nhấn chân ga (x), tín hiệu truyền tới bộ vi xử lý phun xăng (u), van mở cung cấp nhiên liệu cho buồng đốt tạo áp suất xi-lanh (v), áp suất làm quay trục khuỷu (w), và trục khuỷu làm quay bánh xe (y). Từng khâu nối tiếp nhau như một dây chuyền xích. Trong Deep Learning, mạng nơ-ron cũng kết nối hàng trăm tầng liên tiếp như vậy. Làm thế nào để biết nhích nhẹ chân ga 1 milimet sẽ làm tăng tốc độ bánh xe thêm bao nhiêu km/h? Câu trả lời là QUY TẮC CHUỖI.",
                "deepDive": """**1. Hàm hợp (Composite Function) là gì?**
Hàm hợp là một hàm lồng trong một hàm khác: $y = f(u)$ trong đó $u = g(x)$. Tóm tắt là $y = f(g(x))$.
Đầu vào $x$ đi qua cỗ máy thứ nhất $g$ tạo ra thành phẩm trung gian $u$. Thành phẩm trung gian $u$ ngay lập tức trở thành nguyên liệu đầu vào cho cỗ máy thứ hai $f$ để tạo ra thành phẩm cuối cùng $y$.

**2. Trực giác kinh điển: Bánh răng xe đạp:**
Giả sử bạn đạp xe đạp thể thao:
- Đĩa xích trước liên kết với bàn đạp: Khi bàn đạp ($x$) quay 1 vòng, đĩa xích ($u$) quay 2 vòng $\\implies \\frac{du}{dx} = 2$.
- Líp xe sau liên kết với đĩa trước: Khi đĩa ($u$) quay 1 vòng, bánh xe sau ($y$) quay 3 vòng $\\implies \\frac{dy}{du} = 3$.
- Hỏi: Nếu bạn đạp bàn đạp quay 1 vòng, bánh xe sau sẽ quay mấy vòng?
- Rõ ràng: 1 vòng đạp $\\to$ 2 vòng đĩa $\\to 2 \\times 3 = 6$ vòng bánh xe!
- Tốc độ thay đổi của bánh xe theo bàn đạp là tích của các tỷ lệ truyền động từng chặng:
$$\\frac{dy}{dx} = \\frac{dy}{du} \\cdot \\frac{du}{dx} = 3 \\cdot 2 = 6$$
Đó chính là nội dung của **QUY TẮC CHUỖI (Chain Rule)**!

**3. Quy tắc chuỗi trong Mạng Nơ-ron Nhân Tạo (Trọng tâm Đề thi VAIO):**
Hãy xét một nơ-ron nhân tạo cơ bản nhất trong quá trình tính toán:
- **Chặng 1: Tổng có trọng số (Linear sum):** Nhận đầu vào $x$, nhân với trọng số $w$ và cộng độ lệch $b$:
  $$z = w \\cdot x + b$$
- **Chặng 2: Hàm kích hoạt phi tuyến (Activation):** Ép qua hàm kích hoạt $\\sigma$ (ví dụ Sigmoid) để tạo dự đoán:
  $$\\hat{y} = \\sigma(z)$$
- **Chặng 3: Tính hàm mất mát (Loss):** So sánh dự đoán $\\hat{y}$ với đáp án thực tế $y$:
  $$\\mathcal{L} = \\frac{1}{2}(\\hat{y} - y)^2$$

Mục tiêu của thuật toán học máy là: Cần biết thay đổi trọng số $w$ một chút thì hàm mất mát $\\mathcal{L}$ tăng hay giảm bao nhiêu, tức tính $\\frac{\\partial \\mathcal{L}}{\\partial w}$!
Vì $w$ nằm sâu ở tầng đầu, muốn chạm tới $\\mathcal{L}$ ở tầng cuối, ta phải áp dụng Quy tắc chuỗi xâu chuỗi 3 mắt xích từ sau ra trước:
$$\\frac{\\partial \\mathcal{L}}{\\partial w} = \\frac{\\partial \\mathcal{L}}{\\partial \\hat{y}} \\cdot \\frac{\\partial \\hat{y}}{\\partial z} \\cdot \\frac{\\partial z}{\\partial w}$$

**4. Tính chi tiết từng mắt xích một bằng số cụ thể:**
Giả sử nơ-ron đang xét có:
- Đầu vào: $x = 2.0$.
- Trọng số hiện tại: $w = 3.0$, bias $b = 1.0$.
- Nhãn thực tế: $y = 0.0$.
- Hàm kích hoạt là Sigmoid có công thức đạo hàm đẹp đẽ: $\\sigma'(z) = \\sigma(z)(1 - \\sigma(z))$.

*Giai đoạn 1: Lan truyền tiến (Forward Pass) tính toán các giá trị:*
- $z = w \\cdot x + b = 3.0(2.0) + 1.0 = 7.0$.
- Giả sử $\\hat{y} = \\sigma(7.0) \\approx 0.9$.
- $\\mathcal{L} = \\frac{1}{2}(0.9 - 0.0)^2 = \\frac{1}{2}(0.81) = 0.405$.

*Giai đoạn 2: Lan truyền ngược (Backward Pass) tính từng đạo hàm:*
- Mắt xích 1: $\\frac{\\partial \\mathcal{L}}{\\partial \\hat{y}} = \\frac{d}{d\\hat{y}}[\\frac{1}{2}(\\hat{y} - y)^2] = \\hat{y} - y = 0.9 - 0.0 = 0.9$.
- Mắt xích 2: $\\frac{\\partial \\hat{y}}{\\partial z} = \\sigma'(z) = \\hat{y}(1 - \\hat{y}) = 0.9(1 - 0.9) = 0.9(0.1) = 0.09$.
- Mắt xích 3: $\\frac{\\partial z}{\\partial w} = \\frac{\\partial}{\\partial w}(w \\cdot x + b) = x = 2.0$.

*Giai đoạn 3: Ghép nối bằng Quy tắc chuỗi:*
$$\\frac{\\partial \\mathcal{L}}{\\partial w} = 0.9 \\times 0.09 \\times 2.0 = 0.162$$
Ý nghĩa: Vì đạo hàm dương ($0.162 > 0$), nếu ta tăng $w$ thì Loss sẽ tăng. Muốn giảm Loss, ta phải GIẢM trọng số $w$!""",
                "formula": "\\frac{dy}{dx} = \\frac{dy}{du} \\cdot \\frac{du}{dx}, \\quad \\frac{\\partial \\mathcal{L}}{\\partial w} = \\frac{\\partial \\mathcal{L}}{\\partial \\hat{y}} \\cdot \\frac{\\partial \\hat{y}}{\\partial z} \\cdot \\frac{\\partial z}{\\partial w}",
                "mathExplainer": [
                    { "sym": "\\frac{\\partial \\mathcal{L}}{\\partial \\hat{y}}", "name": "Đạo hàm theo đầu ra dự đoán", "mean": "Đo mức độ nhạy cảm của Loss khi dự đoán ŷ lệch đi một chút." },
                    { "sym": "\\frac{\\partial \\hat{y}}{\\partial z}", "name": "Đạo hàm của hàm kích hoạt", "mean": "Độ dốc của hàm phi tuyến tại điểm làm việc z." },
                    { "sym": "\\frac{\\partial z}{\\partial w}", "name": "Đạo hàm theo trọng số", "mean": "Bằng chính giá trị đầu vào x truyền vào nơ-ron." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 160" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="160" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 25)">
                        <circle cx="40" cy="50" r="22" fill="#fff" stroke="#111" stroke-width="2"/>
                        <text x="40" y="55" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">w</text>
                        <line x1="65" y1="50" x2="145" y2="50" stroke="#111" stroke-width="1.5"/>
                        <polygon points="145,46 155,50 145,54" fill="#111"/>
                        <text x="105" y="40" font-family="Georgia" font-size="10" text-anchor="middle">z = wx + b</text>
                        <circle cx="180" cy="50" r="22" fill="#fff" stroke="#111" stroke-width="2"/>
                        <text x="180" y="55" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">z</text>
                        <line x1="205" y1="50" x2="285" y2="50" stroke="#111" stroke-width="1.5"/>
                        <polygon points="285,46 295,50 285,54" fill="#111"/>
                        <text x="245" y="40" font-family="Georgia" font-size="10" text-anchor="middle">ŷ = σ(z)</text>
                        <circle cx="320" cy="50" r="22" fill="#fff" stroke="#111" stroke-width="2"/>
                        <text x="320" y="55" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">ŷ</text>
                        <line x1="345" y1="50" x2="425" y2="50" stroke="#111" stroke-width="1.5"/>
                        <polygon points="425,46 435,50 425,54" fill="#111"/>
                        <text x="385" y="40" font-family="Georgia" font-size="10" text-anchor="middle">Loss L(ŷ, y)</text>
                        <circle cx="460" cy="50" r="22" fill="#111"/>
                        <text x="460" y="55" font-family="Georgia" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">L</text>
                        <!-- Backward arrow below -->
                        <path d="M 450 85 C 320 120 180 120 50 85" fill="none" stroke="#111" stroke-width="2" stroke-dasharray="3,3"/>
                        <polygon points="48,82 43,90 52,91" fill="#111"/>
                        <text x="250" y="125" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Lan truyền ngược: ∂L/∂w = (∂L/∂ŷ) × (∂ŷ/∂z) × (∂z/∂w)</text>
                      </g>
                    </svg>""",
                    "caption": "Dây chuyền tính toán (Computational Graph): Lan truyền tiến tính giá trị Loss; Quy tắc chuỗi lan truyền ngược tính Gradient."
                },
                "commonPitfalls": "Lỗi bỏ quên mắt xích hàm kích hoạt: Rất nhiều học sinh bỏ quên mắt xích đạo hàm $\\frac{\\partial \\hat{y}}{\\partial z}$ và nhân tắt $\\frac{\\partial \\mathcal{L}}{\\partial \\hat{y}} \\times x$. Đây là lỗi sai tai hại phá hủy toàn bộ cơ chế hội tụ của mạng nơ-ron sâu!",
                "practiceQuestion": {
                    "level": "Vận dụng",
                    "question": "Cho một nơ-ron nhân tạo: Đầu vào x = 3, trọng số w = 2, bias b = 1. Giá trị tổng z = w·x + b. Đầu ra ŷ = z². Hàm mất mát Loss L = (ŷ - y_true) với y_true = 25. Hãy tính đạo hàm ∂L/∂w tại điểm dữ liệu này.",
                    "options": [
                        "A. 14",
                        "B. 42",
                        "C. 21",
                        "D. 7"
                    ],
                    "correctIndex": 1,
                    "hint": "Tính từng bước theo Chain Rule: ∂L/∂w = (∂L/∂ŷ) × (∂ŷ/∂z) × (∂z/∂w). Tính z trước: z = 2(3) + 1 = 7.",
                    "solution": [
                        "Bước 1: Tính giá trị trung gian: z = w·x + b = 2(3) + 1 = 7.",
                        "Bước 2: Tính ŷ = z² = 7² = 49. Hàm Loss L = ŷ - 25 = 49 - 25 = 24.",
                        "Bước 3: Tính từng đạo hàm thành phần:",
                        "  - ∂L/∂ŷ = d/dŷ(ŷ - 25) = 1.",
                        "  - ∂ŷ/∂z = d/dz(z²) = 2z = 2(7) = 14.",
                        "  - ∂z/∂w = d/dw(w·x + b) = x = 3.",
                        "Bước 4: Nhân theo quy tắc chuỗi: ∂L/∂w = (∂L/∂ŷ) × (∂ŷ/∂z) × (∂z/∂w) = 1 × 14 × 3 = 42.",
                        "Đáp án chính xác: B (42)."
                    ]
                }
            },
            {
                "heading": "1.6. Vector Gradient ∇f & La Bàn Tối Ưu Hóa (Bám Sát Câu 48 Đề Thi VAIO 2025)",
                "content": "Bây giờ bạn đã biết cách tính đạo hàm riêng cho từng biến số riêng rẽ. Nhưng trong mô hình AI, các trọng số không đứng một mình, chúng tạo thành một không gian đa chiều. Làm sao gom tất cả các độ dốc này lại thành một chiếc 'la bàn' chỉ đường duy nhất cho máy tính biết phải bước chân về hướng nào để giảm sai số? Khái niệm trung tâm của toàn bộ nền khoa học học máy chính là: VECTOR GRADIENT.",
                "deepDive": """**1. Định nghĩa Vector Gradient:**
Vector Gradient của một hàm số nhiều biến $f(x, y)$ (hoặc hàm $n$ biến) là một vector gồm các thành phần là toàn bộ các đạo hàm riêng của hàm số đó:
$$\\nabla f(x, y) = \\begin{bmatrix} \\frac{\\partial f}{\\partial x} \\\\ \\frac{\\partial f}{\\partial y} \\end{bmatrix} = \\frac{\\partial f}{\\partial x} \\mathbf{i} + \\frac{\\partial f}{\\partial y} \\mathbf{j}$$
- Ký hiệu $\\nabla$: Là một tam giác ngược, gọi là **Nabla** (hoặc đọc trực tiếp là Gradient của $f$).
- $\\mathbf{i} = \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}$ và $\\mathbf{j} = \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}$: Là hai vector đơn vị dọc theo trục hoành Ox và trục tung Oy.

**2. Ba định lý hình học cốt tử của Vector Gradient (Chắc chắn xuất hiện trong đề thi):**

**Định lý 1: Vector Gradient $\\nabla f$ LUÔN LUÔN chỉ về hướng mà hàm số TĂNG NHANH NHẤT!**
Nếu bạn đang đứng trên sườn núi, bạn quay la bàn theo vector $\\nabla f$, đó chính là hướng dốc đứng nhất dẫn thẳng lên đỉnh núi!

**Định lý 2: Độ dài của vector gradient $\\|\\nabla f\\|$ thể hiện độ dốc cực đại:**
$$\\|\\nabla f\\| = \\sqrt{\\left(\\frac{\\partial f}{\\partial x}\\right)^2 + \\left(\\frac{\\partial f}{\\partial y}\\right)^2}$$
Nếu $\\|\\nabla f\\|$ rất lớn, vách núi đang dựng đứng hiểm trở. Nếu $\\|\\nabla f\\| = 0$, bạn đang đứng trên một mặt phẳng bằng phẳng hoàn toàn (Đáy thung lũng hoặc Đỉnh núi).

**Định lý 3: Vector Gradient luôn VUÔNG GÓC với các Đường đồng mức (Contour Lines):**
- Đường đồng mức là đường nối tất cả các điểm có cùng độ cao (cùng giá trị hàm Loss).
- Khi bạn đi dọc theo đường đồng mức, độ cao không đổi (độ dốc bằng 0).
- Vì thế, hướng vuông góc với đường đồng mức chính là hướng có độ dốc lớn nhất $\\implies$ Gradient luôn trực giao (vuông góc) với tiếp tuyến đường đồng mức tại mọi điểm!

**3. Tại sao Học máy lại bước đi theo $-\\nabla f$ (Gradient Descent)?**
- Mục tiêu của học máy là **CỰC TIỂU HÓA HÀM MẤT MÁT (Minimize Loss)**, tìm nơi sai số nhỏ nhất.
- Vì $\\nabla L$ là hướng Loss tăng nhanh nhất (lên đỉnh núi sai số),
- Nên hướng ngược lại: **$-\\nabla L$ chính là HƯỚNG LOSS GIẢM NHANH NHẤT** (xuống đáy thung lũng an toàn)!
- Công thức cập nhật tham số huyền thoại của Machine Learning:
$$\\mathbf{w}_{\\text{mới}} = \\mathbf{w}_{\\text{cũ}} - \\eta \\nabla L(\\mathbf{w})$$
Dấu trừ ($-$) trong công thức trên chính là bản chất vì sao thuật toán có tên là **HẠ GRADIENT (Gradient Descent)**. Con số $\\eta > 0$ gọi là **Tốc độ học (Learning Rate)**, kiểm soát độ dài của mỗi bước chân.

**4. Phân tích bám sát Câu 48 Đề thi chính thức Olympic AI VAIO 2025 (Mã Đề 006):**
*Đề bài nguyên văn:* Tính gradient của hàm số $f(x, y) = 2x^2 - 3y^2 + 4y - 10$ tại điểm $(0, 0)$.
Các phương án lựa chọn:
A. $1\\mathbf{i} + 10\\mathbf{j}$ \t B. $2\\mathbf{i} - 3\\mathbf{j}$ \t C. $-3\\mathbf{i} + 4\\mathbf{j}$ \t D. $0\\mathbf{i} + 4\\mathbf{j}$

*Cách 1: Lời giải tự luận chi tiết từng bước:*
- **Bước 1: Tính đạo hàm riêng theo biến $x$:**
  Coi $y$ là hằng số:
  $\\frac{\\partial f}{\\partial x} = \\frac{\\partial}{\\partial x}(2x^2 - 3y^2 + 4y - 10) = 4x - 0 + 0 - 0 = 4x$.
- **Bước 2: Tính đạo hàm riêng theo biến $y$:**
  Coi $x$ là hằng số:
  $\\frac{\\partial f}{\\partial y} = \\frac{\\partial}{\\partial y}(2x^2 - 3y^2 + 4y - 10) = 0 - 6y + 4 - 0 = -6y + 4$.
- **Bước 3: Thay tọa độ điểm cần xét $(x=0, y=0)$ vào:**
  $\\frac{\\partial f}{\\partial x}(0, 0) = 4(0) = 0$.
  $\\frac{\\partial f}{\\partial y}(0, 0) = -6(0) + 4 = 4$.
- **Bước 4: Viết vector gradient dưới dạng tổ hợp vector đơn vị:**
  $\\nabla f(0, 0) = \\frac{\\partial f}{\\partial x}(0, 0) \\mathbf{i} + \\frac{\\partial f}{\\partial y}(0, 0) \\mathbf{j} = 0\\mathbf{i} + 4\\mathbf{j}$.
$\\implies$ Chọn đáp án **D**.

*Cách 2: Kỹ năng thi trắc nghiệm đỉnh cao giải trong 3 giây:*
- Liếc nhanh biến $x$: Hạng tử chứa $x$ duy nhất là $2x^2$, đạo hàm ra $4x$. Tại $x = 0$, chắc chắn thành phần theo $\\mathbf{i}$ phải bằng $0$!
- Nhìn 4 đáp án:
  - A: có $1\\mathbf{i} \\neq 0$ (Loại ngay).
  - B: có $2\\mathbf{i} \\neq 0$ (Loại ngay).
  - C: có $-3\\mathbf{i} \\neq 0$ (Loại ngay).
  - D: có $0\\mathbf{i} = 0$ (ĐÚNG DUY NHẤT!).
Chưa đầy 3 giây là có ngay điểm trọn vẹn của câu thi Olympic!""",
                "formula": "\\nabla f(x, y) = \\begin{bmatrix} \\frac{\\partial f}{\\partial x} \\\\ \\frac{\\partial f}{\\partial y} \\end{bmatrix} = \\frac{\\partial f}{\\partial x}\\mathbf{i} + \\frac{\\partial f}{\\partial y}\\mathbf{j}, \\quad \\mathbf{w}_{t+1} = \\mathbf{w}_t - \\eta \\nabla L(\\mathbf{w}_t)",
                "mathExplainer": [
                    { "sym": "\\nabla f (Nabla)", "name": "Vector Gradient", "mean": "Vector gồm tất cả các đạo hàm riêng, luôn chỉ về hướng hàm số tăng nhanh nhất." },
                    { "sym": "-\\nabla f", "name": "Gradient âm (Ngược hướng)", "mean": "Hướng hàm số giảm nhanh nhất, là hướng bước đi của thuật toán Gradient Descent." },
                    { "sym": "\\mathbf{i}, \\mathbf{j}", "name": "Vector đơn vị", "mean": "Vector có độ dài bằng 1 dọc theo trục hoành Ox và trục tung Oy." },
                    { "sym": "\\eta (Eta)", "name": "Tốc độ học (Learning Rate)", "mean": "Độ lớn của mỗi bước chân cập nhật trọng số trong thuật toán tối ưu." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(60, 20)">
                        <ellipse cx="120" cy="70" rx="90" ry="50" fill="none" stroke="#bbb" stroke-dasharray="2,2"/>
                        <ellipse cx="120" cy="70" rx="55" ry="30" fill="none" stroke="#777"/>
                        <ellipse cx="120" cy="70" rx="20" ry="10" fill="none" stroke="#111"/>
                        <circle cx="120" cy="70" r="3.5" fill="#111"/>
                        <text x="120" y="65" font-family="Georgia" font-size="9" text-anchor="middle">Đáy Cực Tiểu (Loss min)</text>
                        <!-- Current point -->
                        <circle cx="170" cy="45" r="4.5" fill="#111"/>
                        <!-- Gradient arrow UP -->
                        <line x1="170" y1="45" x2="210" y2="25" stroke="#888" stroke-width="2"/>
                        <polygon points="210,22 216,27 207,29" fill="#888"/>
                        <text x="215" y="20" font-family="Georgia" font-size="10" fill="#666">+∇L (Hướng tăng Loss)</text>
                        <!-- Negative Gradient arrow DOWN to center -->
                        <line x1="170" y1="45" x2="130" y2="65" stroke="#111" stroke-width="2.5"/>
                        <polygon points="130,68 124,63 133,60" fill="#111"/>
                        <text x="155" y="85" font-family="Georgia" font-size="11" font-weight="bold">-η∇L (Hướng bước của GD)</text>
                      </g>
                      <g transform="translate(360, 30)">
                        <text x="0" y="20" font-family="Georgia" font-size="11" font-weight="bold">Điểm cốt lõi cho kỳ thi VAIO:</text>
                        <text x="0" y="45" font-family="Georgia" font-size="10">• Gradient luôn VUÔNG GÓC với đường đồng mức (Contour line).</text>
                        <text x="0" y="65" font-family="Georgia" font-size="10">• Tại điểm cực tiểu hoặc cực đại: ∇f = 0 (mọi đạo hàm riêng = 0).</text>
                        <text x="0" y="85" font-family="Georgia" font-size="10">• Đề thi thường yêu cầu tính giá trị ∇f tại điểm cụ thể (x₀, y₀).</text>
                      </g>
                    </svg>""",
                    "caption": "Các đường đồng mức của hàm mất mát: Vector Gradient vuông góc với đường đồng mức và chỉ hướng dốc tăng nhanh nhất; Hướng ngược lại chỉ về tâm cực tiểu."
                },
                "commonPitfalls": "Bẫy đề thi kinh điển: Đề thi trắc nghiệm thường hỏi 'Vector Gradient chỉ hướng nào của hàm số?'. Rất nhiều học sinh chọn 'Hướng giảm nhanh nhất của hàm số'. ĐÂY LÀ ĐÁP ÁN SAI! Bản thân ∇f chỉ hướng TĂNG nhanh nhất. Phải có dấu trừ (-) tức -∇f mới là hướng GIẢM nhanh nhất!",
                "practiceQuestion": {
                    "level": "Nâng cao (Câu 48 Đề Thi VAIO 2025)",
                    "question": "Tính gradient của hàm số f(x, y) = 2x² - 3y² + 4y - 10 tại điểm (0, 0). (Câu 48 Đề thi chính thức VAIO 2025)",
                    "options": [
                        "A. 1i + 10j",
                        "B. 2i - 3j",
                        "C. -3i + 4j",
                        "D. 0i + 4j"
                    ],
                    "correctIndex": 3,
                    "hint": "Tính ∂f/∂x coi y là hằng số, tính ∂f/∂y coi x là hằng số; sau đó thay x=0, y=0 vào từng thành phần của vector [∂f/∂x, ∂f/∂y].",
                    "solution": [
                        "Bước 1: Tính đạo hàm riêng theo biến x (coi y là số hằng):",
                        "  ∂f/∂x = d/dx (2x² - 3y² + 4y - 10) = 4x - 0 + 0 - 0 = 4x.",
                        "Bước 2: Tính đạo hàm riêng theo biến y (coi x là số hằng):",
                        "  ∂f/∂y = d/dy (2x² - 3y² + 4y - 10) = 0 - 6y + 4 - 0 = -6y + 4.",
                        "Bước 3: Thay tọa độ điểm (x=0, y=0) vào hai đạo hàm riêng:",
                        "  - Thành phần theo trục i: ∂f/∂x (0, 0) = 4(0) = 0.",
                        "  - Thành phần theo trục j: ∂f/∂y (0, 0) = -6(0) + 4 = 4.",
                        "Bước 4: Biểu diễn gradient dưới dạng vector đơn vị:",
                        "  ∇f(0, 0) = (∂f/∂x)i + (∂f/∂y)j = 0i + 4j.",
                        "Đáp án chính xác: D (0i + 4j)."
                    ]
                }
            }
        ],
        "interactiveWidget": "widget-gradient-descent",
        "examConnection": {
            "questionTitle": "Phân Tích Dạng Bài Thi Olympic VAIO 2025 (Mã Đề 006)",
            "items": [
                {
                    "code": "Câu 48",
                    "problem": "Tính vector gradient của hàm đa thức hai biến $f(x, y) = 2x^2 - 3y^2 + 4y - 10$ tại gốc tọa độ $(0, 0)$.",
                    "solution": [
                        "Chiến lược giải nhanh trong 3 giây: Tách riêng biến x: $2x^2 \\to 4x$, tại $x=0$ bằng 0 $\\implies$ Loại ngay A, B, C.",
                        "Chỉ còn duy nhất đáp án D ($0i + 4j$). Không cần tính biến y vẫn chọn đúng 100%!"
                    ]
                },
                {
                    "code": "Câu 47",
                    "problem": "Tính đầu ra nơ-ron: Vector trọng số $\\mathbf{w} = [1, 4, 3]$, vector đầu vào $\\mathbf{x} = [4, 8, 5]$, hệ số kích hoạt tuyến tính $k = 3$.",
                    "solution": [
                        "Bước 1: Tính tích vô hướng tổng có trọng số: $z = 1(4) + 4(8) + 3(5) = 4 + 32 + 15 = 51$.",
                        "Bước 2: Nhân với hệ số kích hoạt: $Output = 3 \\times 51 = 153$."
                    ]
                }
            ]
        },
        "takeaways": [
            "Học máy phân chia thành Hồi quy (đầu ra số thực liên tục y ∈ ℝ) và Phân loại (đầu ra nhãn rời rạc y ∈ {0, 1}).",
            "Đạo hàm f'(x) là hệ số góc của tiếp tuyến; f'(x) = 0 là điều kiện cần của điểm cực trị (đáy thung lũng nơi Loss nhỏ nhất).",
            "Đạo hàm riêng theo biến nào thì 'đóng băng' toàn bộ các biến còn lại như một con số hằng.",
            "Quy tắc chuỗi (Chain Rule) ∂L/∂w = (∂L/∂ŷ) · (∂ŷ/∂z) · (∂z/∂w) là trái tim để lan truyền ngược sai số qua các tầng nơ-ron.",
            "Vector Gradient ∇f luôn chỉ hướng TĂNG nhanh nhất; do đó thuật toán Gradient Descent bắt buộc phải bước đi theo hướng NGƯỢC LẠI: -η∇f."
        ]
    }

if __name__ == "__main__":
    l1 = get_masterpiece_lesson_1()
    print("Masterpiece Lesson 1 generated successfully!")
    print(f"Title: {l1['title']}")
    print(f"Sections count: {len(l1['sections'])}")
    for i, s in enumerate(l1['sections']):
        print(f"  Sec {i+1}: {s['heading']} (deepDive: {len(s['deepDive'])} chars)")
