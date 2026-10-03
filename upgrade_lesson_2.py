# -*- coding: utf-8 -*-
"""
upgrade_lesson_2.py - Generates an ultra-detailed, textbook-grade Masterpiece for Lesson 2:
'2. Đại Số Tuyến Tính, Vector, Ma Trận & Cosine Similarity'
Tailored specifically for 12th graders starting from absolute zero linear algebra knowledge.
"""

def get_masterpiece_lesson_2():
    return {
        "id": "lesson-2",
        "title": "2. Đại Số Tuyến Tính, Vector, Ma Trận & Cosine Similarity",
        "summary": "Khởi đầu từ con số 0: Ngôn ngữ biểu diễn dữ liệu của toàn bộ thế giới AI. Dẫn dắt tường minh từ bản chất Scalar, Vector, Matrix, Tensor đến các phép toán cốt tử: Tích vô hướng (Dot Product), Tích Hadamard (⊙), Phép nhân ma trận, Chuẩn độ dài L1/L2, và Độ đo góc Cosine Similarity trong các hệ thống gợi ý & mô hình ngôn ngữ lớn (LLMs).",
        "syllabusBadge": "BUỔI 4: ĐẠI SỐ TUYẾN TÍNH & HỆ THỐNG GỢI Ý",
        "intuition": {
            "title": "Trực giác thực tế: Gu âm nhạc trên Spotify và Không gian đa chiều",
            "content": "Làm thế nào Spotify có thể biết bạn và một người lạ ở nửa bên kia bán cầu có sở thích âm nhạc giống hệt nhau để gợi ý bài hát cho bạn? Spotify không thể đọc suy nghĩ của bạn bằng phép thuật. Thay vào đó, Spotify biến toàn bộ hành vi nghe nhạc của mỗi người thành một danh sách các con số (Vector biểu diễn):\n- **Người A:** [Thích Rock: 0.90, Thích Pop: 0.20, Thích Jazz: 0.10, Thích EDM: 0.85]\n- **Người B:** [Thích Rock: 0.85, Thích Pop: 0.15, Thích Jazz: 0.05, Thích EDM: 0.90]\n- **Người C:** [Thích Rock: 0.05, Thích Pop: 0.95, Thích Jazz: 0.80, Thích EDM: 0.10]\n\nMỗi danh sách số này là một 'mũi tên' (Vector) chỉ về một hướng trong không gian sở thích 4 chiều. Người A và Người B có mũi tên cùng chỉ về một góc nhọn rất hẹp trong không gian $\\implies$ Góc lệch $\\theta \\approx 0^\\circ \\implies \\cos(\\theta) \\approx 0.99$. Hệ thống lập tức kết luận: 'Hai người này có gu âm nhạc tương đồng tuyệt đối!'\n\nĐây chính là sức mạnh tối thượng của Đại Số Tuyến Tính trong AI: Biến mọi khái niệm trừu tượng của thế giới thực (bài hát, phim ảnh, bài báo, khuôn mặt, giọng nói) thành các con số và dùng hình học không gian để đo độ tương đồng!"
        },
        "sections": [
            {
                "heading": "2.1. Khởi Đầu Từ Con Số 0: Đại Số Tuyến Tính Là Gì? 4 Cấp Bậc Dữ Liệu (Scalar, Vector, Matrix, Tensor)",
                "content": "Bộ vi xử lý của máy tính thực chất chỉ là những mạch bán dẫn đóng ngắt dòng điện. Máy tính không thể nhìn thấy 'bức ảnh con mèo', không thể nghe thấy 'bản nhạc của Taylor Swift', cũng không thể hiểu 'đoạn văn tiếng Việt'. Muốn máy tính học được, con người bắt buộc phải chuyển đổi mọi thông tin ngoài đời thực thành các con số. Đại số tuyến tính chính là ngôn ngữ toán học giúp ta tổ chức các con số đó một cách ngăn nắp và khoa học.",
                "deepDive": """**1. Bản chất của Đại số tuyến tính:**
Đại số tuyến tính nghiên cứu các không gian vector và các phép biến đổi tuyến tính (co giãn, xoay, chiếu) giữa các không gian đó. Trong Machine Learning, nó đóng vai trò là 'hệ xương sống' để chứa đựng và truyền dẫn dữ liệu.

**2. Bốn cấp bậc cấu trúc dữ liệu theo chiều không gian:**

**a) Cấp bậc 0D: Scalar (Đại lượng vô hướng - Con số đơn lẻ):**
- **Định nghĩa:** Là một con số thực duy nhất ($x \\in \\mathbb{R}$). Nó không có hướng, chỉ có độ lớn.
- **Ví dụ thực tế:**
  - Nhiệt độ phòng: $28^\\circ\\text{C}$.
  - Tuổi của học sinh: $18$.
  - Tốc độ học (Learning Rate) của mô hình AI: $\\eta = 0.01$.
- **Ký hiệu:** Viết bằng chữ cái thường nghiêng: $x, y, z, c$.

**b) Cấp bậc 1D: Vector (Mảng một chiều - Danh sách thuộc tính):**
- **Định nghĩa:** Là một danh sách gồm nhiều con số được sắp xếp theo thứ tự, đại diện cho MỘT ĐỐI TƯỢNG có nhiều đặc trưng (features).
- **Ý nghĩa hình học:** Một vector $\\mathbf{x} \\in \\mathbb{R}^d$ là một **mũi tên** trong không gian $d$ chiều, có gốc xuất phát từ gốc tọa độ $(0, 0, \\dots, 0)$ và đỉnh mũi tên trỏ tới tọa độ của các con số đó.
- **Ví dụ thực tế:** Hồ sơ đặc trưng của một căn nhà:
  $$\\mathbf{x} = \\begin{bmatrix} 85.5 \\\\ 3 \\\\ 4.2 \\\\ 12 \\end{bmatrix} \\begin{matrix} \\leftarrow \\text{Diện tích (m²)} \\\\ \\leftarrow \\text{Số phòng ngủ} \\\\ \\leftarrow \\text{Khoảng cách đến trung tâm (km)} \\\\ \\leftarrow \\text{Tầng cao} \\end{matrix}$$
- **Phân biệt Vector cột vs Vector hàng:**
  - Theo quy ước chuẩn quốc tế của Machine Learning, một vector mặc định luôn là **Vector Cột** (kích thước $d \\times 1$).
  - Muốn biểu diễn vector hàng, ta dùng dấu chuyển vị: $\\mathbf{x}^T = [85.5, 3, 4.2, 12]$ (kích thước $1 \\times d$).

**c) Cấp bậc 2D: Matrix (Ma trận - Bảng dữ liệu hai chiều):**
- **Định nghĩa:** Là một bảng chữ nhật gồm $m$ hàng và $n$ cột ($A \\in \\mathbb{R}^{m \\times n}$).
- **Ký hiệu phần tử:** $A_{ij}$ là con số nằm ở hàng thứ $i$ và cột thứ $j$.
- **Ví dụ thực tế:**
  - Một tập dữ liệu khách hàng (Dataset): Gồm 1000 khách hàng (1000 hàng) và mỗi khách hàng có 10 đặc trưng (10 cột) $\\implies$ Ma trận kích thước $1000 \\times 10$.
  - Một bức ảnh xám (Grayscale Image) kích thước $28 \\times 28$ pixel (như bộ dữ liệu chữ số MNIST): Mỗi điểm ảnh là một ô chứa độ sáng từ 0 (đen) đến 255 (trắng) $\\implies$ Ma trận $28 \\times 28$.

**d) Cấp bậc 3D, 4D+: Tensor (Mảng đa chiều):**
- **Định nghĩa:** Là khái niệm mở rộng tổng quát hóa của ma trận lên không gian 3, 4, 5 chiều trở lên.
- **Ví dụ kinh điển trong Computer Vision:**
  - Một bức ảnh màu kỹ thuật số (RGB Image): Gồm 3 kênh màu riêng biệt (Kênh Đỏ - Red, Kênh Xanh lá - Green, Kênh Xanh dương - Blue). Mỗi kênh màu là một ma trận kích thước Chiều cao $H \\times$ Chiều rộng $W$. Do đó, 1 bức ảnh màu là một **Tensor 3 chiều** kích thước $(3, H, W)$.
  - Một lô huấn luyện (Mini-batch) gồm 64 ảnh màu đưa vào mạng nơ-ron cùng lúc: Là một **Tensor 4 chiều** kích thước $(64, 3, 224, 224)$ tương ứng $(\\text{Batch\\_size}, \\text{Channels}, \\text{Height}, \\text{Width})$.
  - Một video clip: Thêm một trục thời gian (số khung hình/giây) $\\implies$ **Tensor 5 chiều**!""",
                "formula": "x \\in \\mathbb{R} \\text{ (0D)} \\quad \\to \\quad \\mathbf{x} \\in \\mathbb{R}^d \\text{ (1D)} \\quad \\to \\quad A \\in \\mathbb{R}^{m \\times n} \\text{ (2D)} \\quad \\to \\quad \\mathcal{T} \\in \\mathbb{R}^{B \\times C \\times H \\times W} \\text{ (4D)}",
                "mathExplainer": [
                    { "sym": "x \\in \\mathbb{R}", "name": "Scalar (Vô hướng)", "mean": "Con số thực đơn lẻ duy nhất, không có hướng." },
                    { "sym": "\\mathbf{x} \\in \\mathbb{R}^d", "name": "Vector d chiều", "mean": "Mảng số 1 chiều biểu diễn một mũi tên có d tọa độ thuộc tính." },
                    { "sym": "A \\in \\mathbb{R}^{m \\times n}", "name": "Ma trận m × n", "mean": "Bảng số 2 chiều gồm m hàng ngang và n cột dọc." },
                    { "sym": "\\mathcal{T} \\in \\mathbb{R}^{B \\times C \\times H \\times W}", "name": "Tensor 4 chiều", "mean": "Mảng đa chiều trong học sâu: B lô ảnh, C kênh màu, H chiều cao, W chiều rộng." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(20, 20)">
                        <text x="50" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">1. Scalar (0D)</text>
                        <rect x="25" y="45" width="50" height="50" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="50" y="75" font-family="Georgia" font-size="16" font-weight="bold" text-anchor="middle">42</text>
                        <text x="50" y="125" font-family="Georgia" font-size="9" text-anchor="middle">Một số đơn lẻ</text>
                      </g>
                      <g transform="translate(140, 20)">
                        <text x="60" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">2. Vector (1D)</text>
                        <rect x="35" y="30" width="50" height="80" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="60" y="50" font-family="Georgia" font-size="11" text-anchor="middle">x₁ = 3</text>
                        <text x="60" y="75" font-family="Georgia" font-size="11" text-anchor="middle">x₂ = 7</text>
                        <text x="60" y="100" font-family="Georgia" font-size="11" text-anchor="middle">x₃ = -1</text>
                        <text x="60" y="125" font-family="Georgia" font-size="9" text-anchor="middle">Mảng 1 chiều</text>
                      </g>
                      <g transform="translate(280, 20)">
                        <text x="75" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">3. Matrix (2D)</text>
                        <rect x="25" y="30" width="100" height="80" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="50" y="55" font-family="Georgia" font-size="10" text-anchor="middle">1.2</text>
                        <text x="100" y="55" font-family="Georgia" font-size="10" text-anchor="middle">4.5</text>
                        <text x="50" y="80" font-family="Georgia" font-size="10" text-anchor="middle">0.8</text>
                        <text x="100" y="80" font-family="Georgia" font-size="10" text-anchor="middle">9.1</text>
                        <text x="50" y="105" font-family="Georgia" font-size="10" text-anchor="middle">3.4</text>
                        <text x="100" y="105" font-family="Georgia" font-size="10" text-anchor="middle">2.7</text>
                        <text x="75" y="125" font-family="Georgia" font-size="9" text-anchor="middle">Bảng 3 hàng × 2 cột</text>
                      </g>
                      <g transform="translate(440, 20)">
                        <text x="75" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">4. Tensor (3D/4D)</text>
                        <!-- 3D layered boxes -->
                        <rect x="45" y="30" width="70" height="60" fill="#e5e5e5" stroke="#777" stroke-width="1"/>
                        <rect x="35" y="40" width="70" height="60" fill="#f0f0f0" stroke="#555" stroke-width="1"/>
                        <rect x="25" y="50" width="70" height="60" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="60" y="85" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Ảnh RGB (3,H,W)</text>
                        <text x="75" y="125" font-family="Georgia" font-size="9" text-anchor="middle">Khối lập phương đa chiều</text>
                      </g>
                    </svg>""",
                    "caption": "Trực quan hóa 4 cấp bậc dữ liệu trong Machine Learning: Từ con số đơn lẻ (Scalar) đến Vector thuộc tính, Bảng ma trận, và Khối Tensor đa kênh."
                },
                "commonPitfalls": "Cạm bẫy quy ước kích thước: Nhiều bạn nhầm lẫn thứ tự (Hàng, Cột). Hãy nhớ câu thần chú: 'HÀNG TRƯỚC, CỘT SAU' (Row-first, Column-second). Ma trận kích thước $3 \\times 2$ có 3 hàng ngang và 2 cột dọc. Nếu viết nhầm thành $2 \\times 3$, toàn bộ phép nhân ma trận phía sau sẽ bị lỗi kích thước!",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Trong một hệ thống thị giác máy tính nhận diện biển số xe, mỗi lô dữ liệu huấn luyện nạp vào mô hình chứa 32 bức ảnh màu chất lượng cao, mỗi bức ảnh có chiều cao 128 pixel, chiều rộng 256 pixel và có 3 kênh màu (Đỏ, Xanh lá, Xanh dương). Cấu trúc dữ liệu chứa lô ảnh này là Tensor mấy chiều và có kích thước (Shape) bằng bao nhiêu?",
                    "options": [
                        "A. Tensor 3 chiều với kích thước (32, 128, 256)",
                        "B. Tensor 4 chiều với kích thước (32, 3, 128, 256)",
                        "C. Ma trận 2 chiều với kích thước (32, 32768)",
                        "D. Tensor 5 chiều với kích thước (32, 3, 128, 256, 1)"
                    ],
                    "correctIndex": 1,
                    "hint": "Đếm 4 thành phần: Số ảnh trong lô (Batch), Số kênh màu (Channels), Chiều cao (Height), Chiều rộng (Width).",
                    "solution": [
                        "Bước 1: Xác định từng trục dữ liệu:",
                        "  - Trục 1: Số lượng ảnh trong lô huấn luyện (Batch size) = 32.",
                        "  - Trục 2: Số kênh màu (Channels) = 3 (Đỏ, Xanh lá, Xanh dương).",
                        "  - Trục 3: Chiều cao ảnh (Height) = 128.",
                        "  - Trục 4: Chiều rộng ảnh (Width) = 256.",
                        "Bước 2: Ghép lại theo quy chuẩn NCHW (hoặc NHWC) của học sâu: (32, 3, 128, 256) gồm 4 trục chiều không gian => Tensor 4 chiều.",
                        "Đáp án chính xác: B."
                    ]
                }
            },
            {
                "heading": "2.2. Các Phép Toán Vector Cốt Lõi: Cộng, Trừ, Nhân Vô Hướng & Chuẩn Độ Dài L1/L2",
                "content": "Để làm chủ các thuật toán học máy, ta không thể chỉ nhìn ngắm các vector mà phải bắt chúng vận động. Hai vector cộng với nhau ra cái gì? Làm thế nào để đo độ dài của một mũi tên trong không gian 1000 chiều? Và tại sao các nhà toán học lại phân biệt giữa 'Khoảng cách chim bay' (Chuẩn L2) và 'Khoảng cách đi bộ trên phố' (Chuẩn L1)?",
                "deepDive": """**1. Các phép toán đại số cơ bản trên Vector:**

**a) Phép cộng và trừ hai Vector (Element-wise Addition & Subtraction):**
- **Điều kiện bắt buộc:** Hai vector PHẢI CÙNG KÍCH THƯỚC (cùng số chiều $d$).
- **Quy tắc:** Cộng hoặc trừ từng phần tử ở vị trí tương ứng:
  $$\\mathbf{u} + \\mathbf{v} = \\begin{bmatrix} u_1 \\\\ u_2 \\end{bmatrix} + \\begin{bmatrix} v_1 \\\\ v_2 \\end{bmatrix} = \\begin{bmatrix} u_1 + v_1 \\\\ u_2 + v_2 \\end{bmatrix}$$
- **Ý nghĩa hình học:** Tuân theo **Quy tắc hình bình hành** trong vật lý (tổng hợp hai lực kéo).

**b) Nhân Vector với một số vô hướng (Scalar Multiplication):**
- **Quy tắc:** Lấy con số đó nhân vào TỪNG phần tử của vector:
  $$c \\cdot \\mathbf{v} = c \\cdot \\begin{bmatrix} v_1 \\\\ v_2 \\end{bmatrix} = \\begin{bmatrix} c \\cdot v_1 \\\\ c \\cdot v_2 \\end{bmatrix}$$
- **Ý nghĩa hình học:**
  - Nếu $c > 1$: Phóng đại kéo dài mũi tên theo cùng hướng (ví dụ: $2\\mathbf{v}$ dài gấp đôi $\\mathbf{v}$).
  - Nếu $0 < c < 1$: Thu ngắn mũi tên (ví dụ: $0.5\\mathbf{v}$ ngắn bằng một nửa).
  - Nếu $c < 0$: Đảo ngược chiều mũi tên $180^\\circ$ (ví dụ: $-\\mathbf{v}$ quay ngược hướng). Đây chính là lý do $-\\eta \\nabla L$ đảo ngược hướng tăng thành hướng giảm trong Gradient Descent!

**2. Chuẩn Vector (Vector Norms) - Cách đo độ dài trong không gian đa chiều:**
Trong đời thực, khoảng cách giữa 2 điểm trên mặt phẳng được tính bằng định lý Pytago. Trong không gian nhiều chiều, khái niệm này được tổng quát hóa thành **Chuẩn (Norm)**, ký hiệu bằng hai dấu gạch đứng $\\|\\mathbf{v}\\|$:

**a) Chuẩn L2 (Euclidean Norm - Khoảng cách chim bay):**
- **Công thức:** Căn bậc hai của tổng các bình phương:
  $$\\|\\mathbf{v}\\|_2 = \\sqrt{v_1^2 + v_2^2 + \\dots + v_d^2} = \\sqrt{\\sum_{i=1}^d v_i^2}$$
- **Ý nghĩa:** Là độ dài vật lý thẳng tắp ngắn nhất nối từ gốc tọa độ $(0, 0)$ tới điểm ngọn của vector (khoảng cách chim bay).
- **Ứng dụng trong AI:** Dùng làm kỹ thuật phạt độ lớn trọng số **L2 Regularization (Ridge)** để ngăn mô hình bị quá khớp (Overfitting), và làm mẫu số trong công thức Cosine Similarity.

**b) Chuẩn L1 (Manhattan Norm / Taxi-cab Norm - Khoảng cách đi bộ trên phố):**
- **Công thức:** Tổng các giá trị tuyệt đối:
  $$\\|\\mathbf{v}\\|_1 = |v_1| + |v_2| + \\dots + |v_d| = \\sum_{i=1}^d |v_i|$$
- **Ý nghĩa:** Tưởng tượng bạn đang ở quận Manhattan (New York) với các con phố ô bàn cờ vuông góc. Bạn không thể bay xuyên qua các tòa nhà cao tầng mà phải đi dọc theo các đại lộ rồi rẽ ngang. Chuẩn L1 đo tổng quãng đường đi dọc theo các trục tọa độ.
- **Ứng dụng trong AI:** Dùng trong kỹ thuật **L1 Regularization (Lasso)** có khả năng triệt tiêu các trọng số thừa về đúng bằng 0, giúp chọn lọc đặc trưng tự động.

**c) Chuẩn hóa Vector (Unit Vector / Vector đơn vị):**
- Muốn biến một vector bất kỳ $\\mathbf{v}$ thành một vector có độ dài đúng bằng $1$ nhưng vẫn giữ nguyên hướng ban đầu, ta chỉ cần lấy vector đó chia cho độ dài L2 của chính nó:
  $$\\mathbf{u} = \\frac{\\mathbf{v}}{\\|\\mathbf{v}\\|_2}$$
- Phép biến đổi này gọi là **Chuẩn hóa (Normalization)**, cực kỳ quan trọng trong xử lý ngôn ngữ tự nhiên và tìm kiếm vector.""",
                "formula": "\\|\\mathbf{v}\\|_2 = \\sqrt{\\sum_{i=1}^d v_i^2}, \\quad \\|\\mathbf{v}\\|_1 = \\sum_{i=1}^d |v_i|, \\quad \\mathbf{u} = \\frac{\\mathbf{v}}{\\|\\mathbf{v}\\|_2}",
                "mathExplainer": [
                    { "sym": "\\|\\mathbf{v}\\|_2", "name": "Chuẩn L2 (Euclid)", "mean": "Độ dài đường thẳng hình học của vector theo định lý Pytago." },
                    { "sym": "\\|\\mathbf{v}\\|_1", "name": "Chuẩn L1 (Manhattan)", "mean": "Tổng giá trị tuyệt đối các tọa độ, đo quãng đường đi vuông góc theo trục." },
                    { "sym": "\\mathbf{u} = \\frac{\\mathbf{v}}{\\|\\mathbf{v}\\|}", "name": "Vector đơn vị", "mean": "Vector đã được chuẩn hóa về độ dài bằng 1, chỉ giữ lại thông tin phương hướng." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(60, 20)">
                        <text x="120" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Chuẩn L2 (Khoảng cách Euclid)</text>
                        <line x1="20" y1="125" x2="220" y2="125" stroke="#111" stroke-width="1.5"/>
                        <line x1="40" y1="25" x2="40" y2="125" stroke="#111" stroke-width="1.5"/>
                        <!-- Vector v = (3, 4) -->
                        <line x1="40" y1="125" x2="160" y2="45" stroke="#111" stroke-width="2.5"/>
                        <polygon points="160,45 150,47 154,55" fill="#111"/>
                        <circle cx="160" cy="45" r="3.5" fill="#111"/>
                        <text x="175" y="45" font-family="Georgia" font-size="10" font-weight="bold">v = (3, 4)</text>
                        <text x="115" y="75" font-family="Georgia" font-size="10" font-weight="bold" fill="#111">||v||₂ = √(3²+4²) = 5</text>
                        <line x1="40" y1="125" x2="160" y2="125" stroke="#888" stroke-dasharray="2,2"/>
                        <line x1="160" y1="125" x2="160" y2="45" stroke="#888" stroke-dasharray="2,2"/>
                        <text x="100" y="140" font-family="Georgia" font-size="9">Cạnh đáy = 3</text>
                        <text x="170" y="90" font-family="Georgia" font-size="9">Cạnh cao = 4</text>
                      </g>
                      <g transform="translate(360, 20)">
                        <text x="100" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Chuẩn L1 (Khoảng cách Manhattan)</text>
                        <line x1="20" y1="125" x2="200" y2="125" stroke="#111" stroke-width="1.5"/>
                        <line x1="40" y1="25" x2="40" y2="125" stroke="#111" stroke-width="1.5"/>
                        <!-- Manhattan path -->
                        <line x1="40" y1="125" x2="160" y2="125" stroke="#111" stroke-width="3"/>
                        <line x1="160" y1="125" x2="160" y2="45" stroke="#111" stroke-width="3"/>
                        <circle cx="160" cy="45" r="3.5" fill="#111"/>
                        <text x="100" y="105" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">||v||₁ = |3| + |4| = 7</text>
                        <text x="100" y="145" font-family="Georgia" font-size="9" text-anchor="middle">Đi dọc theo bàn cờ đường phố</text>
                      </g>
                    </svg>""",
                    "caption": "So sánh hình học giữa Chuẩn L2 (đường chéo ngắn nhất bằng 5) và Chuẩn L1 (tổng quãng đường ngang dọc bằng 7)."
                },
                "commonPitfalls": "Nhầm lẫn giữa Chuẩn L2 và Bình phương chuẩn L2: Nhiều bài toán hỏi chuẩn L2 $\\|\\mathbf{v}\\|_2$ nhưng học sinh quên rút căn bậc hai! Với vector $\\mathbf{v} = [3, 4]$, tổng bình phương là $3^2 + 4^2 = 25$, nhưng chuẩn L2 phải lấy căn: $\\sqrt{25} = 5$.",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Cho vector lỗi chênh lệch giữa dự đoán và thực tế của mô hình: e = [3, -2, 6]. Hãy tính chuẩn độ dài Euclid L2 (||e||₂) và chuẩn Manhattan L1 (||e||₁) của vector này.",
                    "options": [
                        "A. ||e||₂ = 49 và ||e||₁ = 7",
                        "B. ||e||₂ = 7 và ||e||₁ = 11",
                        "C. ||e||₂ = 7 và ||e||₁ = 7",
                        "D. ||e||₂ = 11 và ||e||₁ = 7"
                    ],
                    "correctIndex": 1,
                    "hint": "Chuẩn L2 = căn bậc hai của tổng bình phương. Chuẩn L1 = tổng các trị tuyệt đối (chú ý |-2| = +2).",
                    "solution": [
                        "Bước 1: Tính chuẩn L2: ||e||₂ = √(3² + (-2)² + 6²) = √(9 + 4 + 36) = √49 = 7.",
                        "Bước 2: Tính chuẩn L1: ||e||₁ = |3| + |-2| + |6| = 3 + 2 + 6 = 11.",
                        "Kết luận: ||e||₂ = 7 và ||e||₁ = 11. Đáp án đúng là B."
                    ]
                }
            },
            {
                "heading": "2.3. Tích Vô Hướng (Dot Product) vs Tích Hadamard (⊙) & Phép Chiếu Hình Học",
                "content": "Trong các bài giảng AI, bạn sẽ liên tục bắt gặp hai phép nhân vector khác hẳn nhau: lúc thì viết u · v, lúc thì viết u ⊙ v. Nếu không phân biệt được hai phép toán này, bạn sẽ không thể hiểu được cách một nơ-ron tính toán hay cách mạng LSTM kiểm soát thông tin. Hãy cùng làm sáng tỏ bản chất của chúng!",
                "deepDive": r"""**1. Tích vô hướng (Dot Product / Inner Product $\mathbf{u} \cdot \mathbf{v}$):**

**a) Cách tính đại số:**
Lấy từng cặp phần tử ở cùng vị trí nhân với nhau, rồi **CỘNG DỒN TẤT CẢ LẠI THÀNH MỘT CON SỐ DUY NHẤT (Scalar)**:
$$\\mathbf{u} \\cdot \\mathbf{v} = \\mathbf{u}^T \\mathbf{v} = u_1 v_1 + u_2 v_2 + \\dots + u_d v_d = \\sum_{i=1}^d u_i v_i$$
*Ví dụ:* Cho $\\mathbf{u} = [2, 3, -1]$ và $\\mathbf{v} = [4, 0, 5]$:
$$\\mathbf{u} \\cdot \\mathbf{v} = 2(4) + 3(0) + (-1)(5) = 8 + 0 - 5 = 3$$

**b) Ý nghĩa hình học thần thánh:**
Theo lượng giác, tích vô hướng liên hệ mật thiết với góc lệch $\\theta$ giữa hai vector:
$$\\mathbf{u} \\cdot \\mathbf{v} = \\|\\mathbf{u}\\| \\|\\mathbf{v}\\| \\cos(\\theta)$$
- Tích vô hướng đo xem hai mũi tên **'đồng lòng' (cùng hướng) với nhau đến mức độ nào**:
  - **Nếu $\\theta = 0^\\circ$ (cùng hướng):** $\\cos(0^\\circ) = 1 \\implies \\mathbf{u} \\cdot \\mathbf{v}$ đạt giá trị dương cực đại.
  - **Nếu $\\theta = 90^\\circ$ (vuông góc / trực giao):** $\\cos(90^\\circ) = 0 \\implies \\mathbf{u} \\cdot \\mathbf{v} = 0$. Hai vector hoàn toàn độc lập, không có chút liên quan nào!
  - **Nếu $\\theta = 180^\\circ$ (ngược hướng):** $\\cos(180^\\circ) = -1 \\implies \\mathbf{u} \\cdot \\mathbf{v}$ đạt giá trị âm cực đại.

**c) Ứng dụng trong AI (Nền tảng của Nơ-ron nhân tạo):**
Mọi nơ-ron trong mạng nơ-ron đều tính toán tổng có trọng số bằng chính Tích vô hướng giữa vector trọng số $\\mathbf{w}$ và vector đầu vào $\\mathbf{x}$:
$$z = \\mathbf{w} \\cdot \\mathbf{x} + b = w_1 x_1 + w_2 x_2 + \\dots + w_d x_d + b$$
(Đây chính là nội dung cốt lõi của **Câu 47 Đề thi VAIO 2025**!).

**2. Tích từng phần tử (Hadamard Product / Element-wise Product $\\mathbf{u} \\odot \\mathbf{v}$):**

**a) Cách tính đại số:**
Lấy từng cặp phần tử nhân với nhau và **GIỮ NGUYÊN VỊ TRÍ, KHÔNG CỘNG DỒN**:
$$\\mathbf{u} \\odot \\mathbf{v} = \\begin{bmatrix} u_1 \\\\ u_2 \\\\ u_3 \\end{bmatrix} \\odot \\begin{bmatrix} v_1 \\\\ v_2 \\\\ v_3 \\end{bmatrix} = \\begin{bmatrix} u_1 v_1 \\\\ u_2 v_2 \\\\ u_3 v_3 \\end{bmatrix}$$
*Ví dụ:* Với $\\mathbf{u} = [2, 3, -1]$ và $\\mathbf{v} = [4, 0, 5]$:
$$\\mathbf{u} \\odot \\mathbf{v} = [2(4), 3(0), (-1)(5)] = [8, 0, -5]$$
Kết quả trả về vẫn là **MỘT VECTOR CÙNG KÍCH THƯỚC**, hoàn toàn không phải một số vô hướng!

**b) Ứng dụng trong AI:**
- Dùng làm **Cơ chế cổng lọc (Gate)** trong mạng hồi quy LSTM và GRU: Cổng quên (Forget gate) sinh ra một vector gồm các số từ 0 đến 1, rồi nhân Hadamard với trạng thái bộ nhớ để quyết định xóa hay giữ thông tin nào.
- Dùng trong kỹ thuật **Dropout**: Nhân dữ liệu với một vector ngẫu nhiên gồm các số $\{0, 1\}$ để tắt bớt các nơ-ron nhằm chống học vẹt.

**3. Bảng so sánh đối đầu:**
- **Dot Product ($\mathbf{u} \cdot \mathbf{v}$):** Nhân rồi CỘNG $\implies$ Kết quả là 1 CON SỐ (Scalar). Đo độ tương đồng, chiếu không gian.
- **Hadamard ($\mathbf{u} \odot \mathbf{v}$):** Nhân GIỮ NGUYÊN $\implies$ Kết quả là 1 VECTOR/MA TRẬN. Dùng làm mặt nạ lọc, đóng mở cổng.""",
                "formula": "\\mathbf{u} \\cdot \\mathbf{v} = \\sum_{i=1}^d u_i v_i \\in \\mathbb{R} \\quad \\Longleftrightarrow \\quad [\\mathbf{u} \\odot \\mathbf{v}]_i = u_i v_i \\in \\mathbb{R}^d",
                "mathExplainer": [
                    { "sym": "\\mathbf{u} \\cdot \\mathbf{v}", "name": "Tích vô hướng (Dot product)", "mean": "Nhân các cặp phần tử rồi cộng dồn lại, kết quả xuất ra một số thực duy nhất." },
                    { "sym": "\\mathbf{u} \\odot \\mathbf{v}", "name": "Tích Hadamard", "mean": "Nhân các phần tử tương ứng độc lập với nhau, kết quả xuất ra mảng cùng kích thước." },
                    { "sym": "\\cos(\\theta)", "name": "Cosin góc lệch", "mean": "Tỉ số đo mức độ cùng hướng giữa hai vector trong không gian." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 20)">
                        <text x="110" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Tích Vô Hướng u · v (Ra 1 số)</text>
                        <!-- Vector u and v with angle -->
                        <line x1="40" y1="120" x2="180" y2="120" stroke="#111" stroke-width="2.5"/>
                        <polygon points="180,120 170,116 170,124" fill="#111"/>
                        <text x="185" y="125" font-family="Georgia" font-size="11" font-weight="bold">u</text>

                        <line x1="40" y1="120" x2="140" y2="40" stroke="#111" stroke-width="2.5"/>
                        <polygon points="140,40 130,46 137,52" fill="#111"/>
                        <text x="145" y="35" font-family="Georgia" font-size="11" font-weight="bold">v</text>

                        <!-- Projection -->
                        <line x1="140" y1="40" x2="140" y2="120" stroke="#888" stroke-dasharray="2,2"/>
                        <rect x="132" y="112" width="8" height="8" fill="none" stroke="#888"/>
                        <path d="M 70 120 A 30 30 0 0 0 62 102" fill="none" stroke="#111" stroke-width="1.5"/>
                        <text x="75" y="105" font-family="Georgia" font-size="10">θ</text>
                        <text x="110" y="145" font-family="Georgia" font-size="9" text-anchor="middle">u · v = ||u|| ||v|| cos(θ)</text>
                      </g>
                      <g transform="translate(340, 20)">
                        <text x="120" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Tích Hadamard u ⊙ v (Ra 1 vector)</text>
                        <rect x="20" y="45" width="45" height="60" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="42" y="68" font-family="Georgia" font-size="11" text-anchor="middle">2</text>
                        <text x="42" y="93" font-family="Georgia" font-size="11" text-anchor="middle">5</text>

                        <text x="80" y="82" font-family="Georgia" font-size="16" text-anchor="middle">⊙</text>

                        <rect x="95" y="45" width="45" height="60" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="117" y="68" font-family="Georgia" font-size="11" text-anchor="middle">3</text>
                        <text x="117" y="93" font-family="Georgia" font-size="11" text-anchor="middle">-1</text>

                        <text x="155" y="82" font-family="Georgia" font-size="16" text-anchor="middle">=</text>

                        <rect x="170" y="45" width="45" height="60" fill="#e5e5e5" stroke="#111" stroke-width="2"/>
                        <text x="192" y="68" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">6</text>
                        <text x="192" y="93" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">-5</text>
                        <text x="120" y="145" font-family="Georgia" font-size="9" text-anchor="middle">Nhân từng vị trí độc lập</text>
                      </g>
                    </svg>""",
                    "caption": "Phân biệt bản chất: Tích vô hướng chiếu hình học tạo ra 1 con số; Tích Hadamard nhân từng ô giữ nguyên cấu trúc mảng."
                },
                "commonPitfalls": "Lỗi nhầm lẫn tai hại trong phòng thi: Đề bài yêu cầu tính Tích Hadamard mà học sinh lại đi cộng dồn ra một con số (hoặc ngược lại). Hãy nhớ: Phép nhân có chữ 'VÔ HƯỚNG' (Dot product) thì kết quả bắt buộc phải là một đại lượng vô hướng (Scalar, 1 con số)! Còn Hadamard thì trả về vector/ma trận.",
                "practiceQuestion": {
                    "level": "Cơ bản (Bám sát Câu 47 Đề Thi VAIO 2025)",
                    "question": "Cho vector trọng số của một nơ-ron nhân tạo w = [1, 4, 3] và vector tín hiệu đầu vào x = [4, 8, 5]. Tính tích vô hướng w · x giữa hai vector này.",
                    "options": [
                        "A. [4, 32, 15]",
                        "B. 51",
                        "C. 48",
                        "D. 153"
                    ],
                    "correctIndex": 1,
                    "hint": "Nhân từng cặp tọa độ tương ứng rồi cộng dồn lại: 1(4) + 4(8) + 3(5).",
                    "solution": [
                        "Bước 1: Nhân từng cặp phần tử: 1 * 4 = 4; 4 * 8 = 32; 3 * 5 = 15.",
                        "Bước 2: Cộng dồn tất cả các tích thành phần: w · x = 4 + 32 + 15 = 51.",
                        "(Lưu ý: Nếu hỏi tích Hadamard w ⊙ x thì kết quả mới là vector [4, 32, 15] ở đáp án A).",
                        "Đáp án chính xác: B (51)."
                    ]
                }
            },
            {
                "heading": "2.4. Phép Nhân Ma Trận (Matrix Multiplication) & Các Dạng Ma Trận Đặc Biệt",
                "content": "Nếu coi vector là các mũi tên đơn lẻ, thì ma trận chính là những chiếc máy biến đổi không gian. Phép nhân ma trận là phép toán xuất hiện nhiều nhất trong toàn bộ mã nguồn của mạng nơ-ron. Tại sao nhân ma trận không phải là lấy từng ô nhân với nhau? Điều kiện sống còn để hai ma trận nhân được là gì? Và ma trận chuyển vị giúp ích gì cho mô hình học máy?",
                "deepDive": """**1. Điều kiện sống còn để hai Ma trận nhân được:**
Cho hai ma trận $A$ và $B$. Ta CHỈ CÓ THỂ thực hiện phép nhân $A \\times B$ khi và chỉ khi:
$$\\mathbf{\\text{Số CỘT của ma trận đứng trước } A = \\text{Số HÀNG của ma trận đứng sau } B}$$
- Kích thước: $(m \\times k) \\times (k \\times n) = (m \\times n)$.
- Hai chỉ số ở giữa ($k$) phải giống hệt nhau thì mới 'khớp bánh răng', và kích thước của ma trận kết quả sẽ lấy hàng của ma trận đầu ($m$) ghép với cột của ma trận sau ($n$)!
- *Ví dụ:* Ma trận $(3 \\times 4)$ nhân với $(4 \\times 2)$ sẽ cho ra ma trận kết quả $(3 \\times 2)$. Nhưng lấy $(4 \\times 2)$ nhân với $(3 \\times 4)$ thì KHÔNG THỂ NHÂN ĐƯỢC vì $2 \\neq 3$!

**2. Thuật toán nhân ma trận: Quy tắc 'HÀNG NHÂN CỘT' (Row-by-Column):**
Phần tử $C_{ij}$ nằm ở hàng $i$, cột $j$ của ma trận kết quả $C$ được tính bằng **Tích vô hướng giữa HÀNG $i$ của ma trận trước với CỘT $j$ của ma trận sau**:
$$C_{ij} = \\sum_{r=1}^k A_{ir} B_{rj}$$

*Ví dụ tính tay chi tiết từng bước:*
Cho hai ma trận:
$$A = \\begin{bmatrix} 1 & 2 \\\\ 3 & 4 \\end{bmatrix} (2 \\times 2), \\quad B = \\begin{bmatrix} 5 & 6 \\\\ 7 & 8 \\end{bmatrix} (2 \\times 2)$$
Ma trận kết quả $C = A \\times B$ có kích thước $2 \\times 2$:
- **Hàng 1, Cột 1 ($C_{11}$):** Lấy Hàng 1 của $A$ nhân Cột 1 của $B$:
  $$C_{11} = 1(5) + 2(7) = 5 + 14 = 19$$
- **Hàng 1, Cột 2 ($C_{12}$):** Lấy Hàng 1 của $A$ nhân Cột 2 của $B$:
  $$C_{12} = 1(6) + 2(8) = 6 + 16 = 22$$
- **Hàng 2, Cột 1 ($C_{21}$):** Lấy Hàng 2 của $A$ nhân Cột 1 của $B$:
  $$C_{21} = 3(5) + 4(7) = 15 + 28 = 43$$
- **Hàng 2, Cột 2 ($C_{22}$):** Lấy Hàng 2 của $A$ nhân Cột 2 của $B$:
  $$C_{22} = 3(6) + 4(8) = 18 + 32 = 50$$
Kết quả hoàn chỉnh:
$$C = \\begin{bmatrix} 19 & 22 \\\\ 43 & 50 \\end{bmatrix}$$

**3. Tính chất cốt tử: Phép nhân ma trận KHÔNG CÓ TÍNH GIAO HOÁN ($AB \\neq BA$):**
Trong đại số thông thường, $3 \\times 5 = 5 \\times 3$. Nhưng trong ma trận:
$$A \\times B \\neq B \\times A$$
Thậm chí, $AB$ tính được nhưng $BA$ có thể hoàn toàn vô nghĩa do lệch kích thước!

**4. Ma trận chuyển vị (Transpose $A^T$):**
- **Quy tắc:** Lật ngược ma trận qua đường chéo chính: Hàng biến thành Cột, Cột biến thành Hàng. Nếu $A$ có kích thước $m \\times n$ thì $A^T$ có kích thước $n \\times m$.
- **Tính chất vàng cần nhớ khi làm bài thi:**
  - $(A^T)^T = A$ (lật hai lần về lại ban đầu).
  - $(A + B)^T = A^T + B^T$.
  - **$(AB)^T = B^T A^T$ (ĐẢO NGƯỢC THỨ TỰ NHÂN - Cực kỳ hay bẫy trong đề thi!).**

**5. Các dạng ma trận đặc biệt trong Machine Learning:**
- **Ma trận đơn vị (Identity Matrix $I$):** Là ma trận vuông có các số trên đường chéo chính bằng 1, tất cả các ô còn lại bằng 0. Đóng vai trò như số 1 trong đại số: $A \\cdot I = I \\cdot A = A$.
- **Ma trận đối xứng (Symmetric Matrix):** Thỏa mãn $A = A^T$ (Ví dụ: Ma trận hiệp phương sai Covariance Matrix dùng trong thuật toán PCA).
- **Ma trận nghịch đảo (Inverse Matrix $A^{-1}$):** Thỏa mãn $A \\cdot A^{-1} = I$. Dùng để giải phương trình nghiệm chuẩn trong Hồi quy tuyến tính: $\\mathbf{w} = (X^T X)^{-1} X^T \\mathbf{y}$.""",
                "formula": "C_{ij} = \\sum_{r=1}^k A_{ir} B_{rj}, \\quad (AB)^T = B^T A^T, \\quad A \\cdot I = A, \\quad A \\cdot A^{-1} = I",
                "mathExplainer": [
                    { "sym": "A \\in \\mathbb{R}^{m \\times k}", "name": "Ma trận trước", "mean": "Ma trận có m hàng và k cột." },
                    { "sym": "B \\in \\mathbb{R}^{k \\times n}", "name": "Ma trận sau", "mean": "Ma trận có k hàng và n cột, số hàng k phải khớp với số cột của ma trận trước." },
                    { "sym": "A^T", "name": "Ma trận chuyển vị", "mean": "Ma trận lật các hàng thành cột và cột thành hàng qua đường chéo chính." },
                    { "sym": "I", "name": "Ma trận đơn vị", "mean": "Ma trận vuông có đường chéo chính bằng 1, nhân với ma trận nào cũng giữ nguyên ma trận đó." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 20)">
                        <text x="120" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Khớp Kích Thước: (m × k) × (k × n) = (m × n)</text>
                        <!-- Matrix A -->
                        <rect x="20" y="35" width="60" height="70" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <rect x="20" y="45" width="60" height="20" fill="#111"/>
                        <text x="50" y="59" font-family="Georgia" font-size="10" fill="#fff" text-anchor="middle">Hàng i</text>
                        <text x="50" y="125" font-family="Georgia" font-size="10" text-anchor="middle">A (m × k)</text>

                        <text x="95" y="75" font-family="Georgia" font-size="16" text-anchor="middle">×</text>

                        <!-- Matrix B -->
                        <rect x="110" y="35" width="70" height="60" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <rect x="135" y="35" width="20" height="60" fill="#111"/>
                        <text x="145" y="70" font-family="Georgia" font-size="9" fill="#fff" text-anchor="middle">Cột j</text>
                        <text x="145" y="125" font-family="Georgia" font-size="10" text-anchor="middle">B (k × n)</text>

                        <text x="195" y="75" font-family="Georgia" font-size="16" text-anchor="middle">=</text>

                        <!-- Matrix C -->
                        <rect x="210" y="35" width="70" height="70" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <circle cx="245" cy="55" r="5" fill="#111"/>
                        <text x="245" y="125" font-family="Georgia" font-size="10" text-anchor="middle">C (m × n)</text>
                        <text x="245" y="75" font-family="Georgia" font-size="9" font-weight="bold" text-anchor="middle">C_ij</text>
                      </g>
                      <g transform="translate(360, 30)">
                        <text x="0" y="15" font-family="Georgia" font-size="11" font-weight="bold">Quy tắc vàng chuyển vị tích:</text>
                        <text x="0" y="40" font-family="Georgia" font-size="12" font-weight="bold" fill="#111">(A · B)ᵀ = Bᵀ · Aᵀ</text>
                        <text x="0" y="65" font-family="Georgia" font-size="10">• Bắt buộc đảo ngược thứ tự hai ma trận!</text>
                        <text x="0" y="85" font-family="Georgia" font-size="10">• Nếu viết (A · B)ᵀ = Aᵀ · Bᵀ là SAI HOÀN TOÀN.</text>
                        <text x="0" y="110" font-family="Georgia" font-size="10">• Kích thước: Aᵀ(k×m), Bᵀ(n×k) ⇒ BᵀAᵀ ra (n×m).</text>
                      </g>
                    </svg>""",
                    "caption": "Quy tắc nhân ma trận: Hàng i của ma trận trước nhân tích vô hướng với Cột j của ma trận sau tạo thành phần tử C_ij."
                },
                "commonPitfalls": "Cạm bẫy phòng thi kinh điển: Biểu thức chuyển vị của tích hai ma trận $(AB)^T$. Rất nhiều học sinh chọn phương án $A^T B^T$. SAI HOÀN TOÀN! Quy tắc đúng bắt buộc phải ĐẢO NGƯỢC THỨ TỰ: $(AB)^T = B^T A^T$. Nếu giữ nguyên thứ tự, phép nhân $A^T B^T$ thậm chí còn không thể thực hiện được do lệch kích thước!",
                "practiceQuestion": {
                    "level": "Vận dụng",
                    "question": "Cho ma trận X có kích thước 100 × 5 (100 mẫu dữ liệu, 5 đặc trưng) và vector trọng số w có kích thước 5 × 1. Ma trận tích chuyển vị (X · w)ᵀ có kích thước bằng bao nhiêu?",
                    "options": [
                        "A. 100 × 1",
                        "B. 1 × 100",
                        "C. 5 × 100",
                        "D. 1 × 5"
                    ],
                    "correctIndex": 1,
                    "hint": "Tính kích thước của tích X · w trước (hàng của X ghép cột của w), sau đó lật kích thước qua phép chuyển vị Transpose.",
                    "solution": [
                        "Bước 1: Tính kích thước tích X · w: (100 × 5) nhân (5 × 1) cho ra vector kết quả có kích thước 100 × 1 (vector cột).",
                        "Bước 2: Áp dụng phép chuyển vị Transpose (·)ᵀ: Lật hàng thành cột => Kích thước 100 × 1 bị lật thành 1 × 100 (vector hàng).",
                        "Đáp án chính xác: B (1 × 100)."
                    ]
                }
            },
            {
                "heading": "2.5. Cosine Similarity: Thước Đo Góc Trong Không Gian Ngữ Nghĩa & Hệ Thống Gợi Ý (Câu 43 Đề Thi VAIO 2025)",
                "content": "Giả sử bạn đang xây dựng một công cụ tìm kiếm bài báo khoa học. Có một bài báo ngắn 50 từ và một bài báo dài 2000 từ cùng viết về chủ đề 'Khám phá Sao Hỏa'. Nếu dùng khoảng cách thông thường (Euclid), máy tính sẽ thấy hai bài báo này cách xa nhau cả cây số vì bài báo dài có số lượng từ lớn gấp 40 lần bài ngắn. Làm thế nào để máy tính nhận ra hai bài viết này có nội dung hoàn toàn giống nhau? Bí quyết nằm ở ĐỘ ĐO GÓC COSINE SIMILARITY.",
                "deepDive": """**1. Tại sao khoảng cách Euclidean thất bại khi so sánh văn bản & dữ liệu lớn?**
- Khoảng cách Euclid (Chuẩn L2) đo độ dài đoạn thẳng trực tiếp nối hai đỉnh mũi tên:
  $$d_{\\text{Euclid}}(\\mathbf{u}, \\mathbf{v}) = \\|\\mathbf{u} - \\mathbf{v}\\|_2 = \\sqrt{\\sum (u_i - v_i)^2}$$
- Nếu bài báo A ngắn 50 từ và bài báo B dài 2000 từ cùng nội dung: Vector từ của bài B sẽ dài gấp hàng chục lần vector bài A $\\implies$ Khoảng cách Euclid rất lớn $\\implies$ Máy tính kết luận nhầm: 'Hai bài này không liên quan!'
- Nhưng hãy quan sát hình học: Vì cùng nội dung về Sao Hỏa, hai mũi tên này **CÙNG CHỈ VỀ MỘT HƯỚNG TRONG KHÔNG GIAN**! Góc lệch giữa chúng xấp xỉ bằng $0^\\circ$!

**2. Định nghĩa toán học của Cosine Similarity:**
Cosine Similarity đo cosin của góc lệch $\\theta$ giữa hai vector trong không gian đa chiều:
$$\\text{Cosine Similarity}(\\mathbf{u}, \\mathbf{v}) = \\cos(\\theta) = \\frac{\\mathbf{u} \\cdot \\mathbf{v}}{\\|\\mathbf{u}\\|_2 \\|\\mathbf{v}\\|_2} = \\frac{\\sum_{i=1}^d u_i v_i}{\\sqrt{\\sum_{i=1}^d u_i^2} \\cdot \\sqrt{\\sum_{i=1}^d v_i^2}}$$

**3. Mổ xẻ cặn kẽ từng thành phần trong công thức:**
- **Tử số (Tích vô hướng $\\mathbf{u} \\cdot \\mathbf{v}$):** Nhân từng cặp tọa độ rồi cộng dồn lại. Đại lượng này mang thông tin về sự tương quan giữa các chiều.
- **Mẫu số (Tích độ dài Euclid $\\|\\mathbf{u}\\| \\|\\mathbf{v}\\|$):** Đóng vai trò là 'Bộ triệt tiêu kích thước'! Nó chia đều cho độ dài của từng vector, đưa cả hai vector về độ dài bằng 1 $\\implies$ Triệt tiêu hoàn toàn sự chênh lệch về độ dài ngắn của văn bản, chỉ giữ lại duy nhất thông tin về **PHƯƠNG HƯỚNG**!

**4. Ý nghĩa của các giá trị Cosine Similarity:**
Vì giá trị của hàm $\\cos(\\theta)$ luôn nằm trong đoạn $[-1, 1]$:
- **Bằng $+1.0$ (Góc $\\theta = 0^\\circ$):** Hai vector cùng hướng tuyệt đối $\\implies$ Hoàn toàn tương đồng (Hai bài viết y hệt nhau về chủ đề).
- **Bằng $0.0$ (Góc $\\theta = 90^\\circ$):** Hai vector vuông góc trực giao $\\implies$ Hoàn toàn độc lập, không có chút liên quan nào (Ví dụ: Một bài viết về nấu ăn và một bài viết về cơ học lượng tử).
- **Bằng $-1.0$ (Góc $\\theta = 180^\\circ$):** Hai vector ngược hướng hoàn toàn $\\implies$ Đối nghịch tuyệt đối.

**5. Bài toán tính tay mẫu mực từng bước (Bám sát Câu 43 Đề thi Olympic VAIO 2025):**
Cho hai vector đặc trưng của hai khách hàng:
$$\\mathbf{u} = [1, 2, 3], \\quad \\mathbf{v} = [2, 4, 6]$$
Hãy tính Cosine Similarity giữa hai khách hàng này:
- **Bước 1: Tính tích vô hướng ở tử số:**
  $$\\mathbf{u} \\cdot \\mathbf{v} = 1(2) + 2(4) + 3(6) = 2 + 8 + 18 = 28$$
- **Bước 2: Tính độ dài chuẩn L2 của vector $\\mathbf{u}$:**
  $$\\|\\mathbf{u}\\| = \\sqrt{1^2 + 2^2 + 3^2} = \\sqrt{1 + 4 + 9} = \\sqrt{14}$$
- **Bước 3: Tính độ dài chuẩn L2 của vector $\\mathbf{v}$:**
  $$\\|\\mathbf{v}\\| = \\sqrt{2^2 + 4^2 + 6^2} = \\sqrt{4 + 16 + 36} = \\sqrt{56} = \\sqrt{4 \\times 14} = 2\\sqrt{14}$$
- **Bước 4: Thay vào công thức Cosine Similarity:**
  $$\\cos(\\theta) = \\frac{28}{\\sqrt{14} \\times 2\\sqrt{14}} = \\frac{28}{2 \\times 14} = \\frac{28}{28} = 1.0$$
*Nhận xét sâu sắc:* Vì $\\mathbf{v} = 2\\mathbf{u}$ (vector $\\mathbf{v}$ chỉ là vector $\\mathbf{u}$ bị kéo dài gấp đôi), góc giữa chúng bằng đúng $0^\\circ$, nên $\\cos(\\theta) = 1.0$ tuyệt đối!

**6. Ứng dụng thực tế trong AI:**
- **Hệ thống gợi ý (Recommender Systems):** Spotify hay YouTube biểu diễn người dùng và bài hát/video thành các vector nhúng (Embeddings). Video nào có Cosine Similarity gần 1 nhất với sở thích của bạn sẽ được tự động xếp lên đầu trang chủ!
- **Mô hình ngôn ngữ lớn (LLMs & RAG):** Khi bạn hỏi ChatGPT, câu hỏi được mã hóa thành vector và so khớp Cosine Similarity với hàng triệu đoạn tài liệu để trích xuất câu trả lời chính xác nhất!""",
                "formula": "\\text{Cosine Similarity}(\\mathbf{u}, \\mathbf{v}) = \\frac{\\mathbf{u} \\cdot \\mathbf{v}}{\\|\\mathbf{u}\\|_2 \\|\\mathbf{v}\\|_2} = \\cos(\\theta) \\in [-1, 1]",
                "mathExplainer": [
                    { "sym": "\\cos(\\theta)", "name": "Cosine góc lệch", "mean": "Độ đo độ tương đồng phương hướng giữa 2 vector, nằm trong khoảng [-1, 1]." },
                    { "sym": "\\mathbf{u} \\cdot \\mathbf{v}", "name": "Tích vô hướng tử số", "mean": "Tổng các tích tọa độ đo mức độ liên kết giữa hai vector." },
                    { "sym": "\\|\\mathbf{u}\\| \\|\\mathbf{v}\\|", "name": "Mẫu số chuẩn hóa", "mean": "Tích độ dài hai vector, triệt tiêu ảnh hưởng của độ dài/kích thước dữ liệu." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 20)">
                        <text x="120" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Ba Trạng Thái Cosine Similarity</text>
                        <!-- Center Origin -->
                        <circle cx="120" cy="90" r="3.5" fill="#111"/>
                        <text x="120" y="105" font-family="Georgia" font-size="9" text-anchor="middle">Gốc O</text>
                        <!-- Angle = 0: cos = 1 -->
                        <line x1="120" y1="90" x2="200" y2="40" stroke="#111" stroke-width="2.5"/>
                        <line x1="120" y1="90" x2="230" y2="20" stroke="#888" stroke-dasharray="2,2" stroke-width="2"/>
                        <text x="210" y="30" font-family="Georgia" font-size="10" font-weight="bold">cos(0°) = 1.0</text>
                        <!-- Angle = 90: cos = 0 -->
                        <line x1="120" y1="90" x2="60" y2="40" stroke="#111" stroke-width="2"/>
                        <text x="50" y="35" font-family="Georgia" font-size="10" font-weight="bold">cos(90°) = 0</text>
                        <!-- Angle = 180: cos = -1 -->
                        <line x1="120" y1="90" x2="40" y2="140" stroke="#777" stroke-width="2"/>
                        <text x="30" y="155" font-family="Georgia" font-size="10" font-weight="bold">cos(180°) = -1.0</text>
                      </g>
                      <g transform="translate(340, 25)">
                        <text x="0" y="15" font-family="Georgia" font-size="11" font-weight="bold">Ứng dụng trong AI:</text>
                        <text x="0" y="40" font-family="Georgia" font-size="10">• Đo độ tương đồng bài hát trên Spotify.</text>
                        <text x="0" y="60" font-family="Georgia" font-size="10">• Tìm kiếm tài liệu ngữ nghĩa trong RAG &amp; LLMs.</text>
                        <text x="0" y="80" font-family="Georgia" font-size="10">• So sánh mức độ giống nhau của 2 bức ảnh.</text>
                        <text x="0" y="105" font-family="Georgia" font-size="11" font-weight="bold" fill="#111">Khoảng cách Cosine (Cosine Distance):</text>
                        <text x="0" y="125" font-family="Georgia" font-size="10">Distance = 1 - Cosine_Similarity (Càng nhỏ càng gần)</text>
                      </g>
                    </svg>""",
                    "caption": "Ý nghĩa của Cosine Similarity: Bằng 1 khi cùng hướng hoàn toàn; Bằng 0 khi vuông góc không liên quan; Bằng -1 khi ngược hướng đối nghịch."
                },
                "commonPitfalls": "Phân biệt Cosine Similarity và Cosine Distance: Đề thi có thể hỏi 'Khoảng cách Cosine' (Cosine Distance). Hãy nhớ công thức: $\\text{Cosine Distance} = 1 - \\text{Cosine Similarity}$. Hai vector giống hệt nhau thì Cosine Similarity bằng 1, nhưng Khoảng cách Cosine bằng $1 - 1 = 0$ (khoảng cách bằng 0 nghĩa là sát nhau tuyệt đối)!",
                "practiceQuestion": {
                    "level": "Vận dụng (Câu 43 Đề Thi Olympic VAIO 2025)",
                    "question": "Tính Cosine Similarity giữa hai vector thuộc tính u = [3, 4] và v = [6, 8].",
                    "options": [
                        "A. 0.5",
                        "B. 0.0",
                        "C. 1.0",
                        "D. 0.8"
                    ],
                    "correctIndex": 2,
                    "hint": "Để ý mối liên hệ: vector v = 2 * u. Hai vector tỉ lệ dương với nhau thì cùng chỉ về một hướng trong không gian.",
                    "solution": [
                        "Bước 1: Tính tích vô hướng tử số: u · v = 3(6) + 4(8) = 18 + 32 = 50.",
                        "Bước 2: Tính độ dài chuẩn L2 của từng vector:",
                        "  ||u|| = √(3² + 4²) = √25 = 5.",
                        "  ||v|| = √(6² + 8²) = √(36 + 64) = √100 = 10.",
                        "Bước 3: Thay vào công thức: Cosine Similarity = 50 / (5 * 10) = 50 / 50 = 1.0.",
                        "Nhận xét nhanh: Vì v = 2u, hai vector cùng phương cùng chiều (góc θ = 0°) nên cos(0°) = 1.0 ngay lập tức mà không cần bấm máy!",
                        "Đáp án chính xác: C (1.0)."
                    ]
                }
            },
            {
                "heading": "2.6. Vector Hóa (Vectorization) & Gradient Descent Dạng Ma Trận",
                "content": "Tại sao các mô hình học máy hiện đại như ChatGPT, Stable Diffusion hay xe tự hành Tesla lại ngốn hàng trăm triệu đô-la cho các chip đồ họa GPU của NVIDIA? Tại sao không dùng CPU của máy tính thông thường? Bí mật nằm ở kỹ thuật VECTOR HÓA (Vectorization) - chuyển đổi toàn bộ thuật toán về dạng ma trận để tính toán song song.",
                "deepDive": """**1. Nỗi ác mộng của Vòng lặp For trên CPU:**
Giả sử bạn có tập dữ liệu gồm $N = 1.000.000$ mẫu (1 triệu dòng) và mỗi mẫu có $d = 100$ thuộc tính:
- Nếu viết mã bằng vòng lặp `for` thông thường:
  ```python
  # Cách tính thủ công chậm chạp
  for i in range(1000000):
      y_pred[i] = 0
      for j in range(100):
          y_pred[i] += X[i][j] * w[j]
      y_pred[i] += b
  ```
  CPU phải thực hiện tuần tự $1.000.000 \\times 100 = 100.000.000$ phép tính nối tiếp nhau, mất hàng chục giây đến hàng phút cho MỘT LẦN lặp!

**2. Sức mạnh kỳ diệu của Vector hóa (Vectorization):**
Thay vì lặp từng phần tử, ta gom toàn bộ dữ liệu thành ma trận $X$ kích thước $N \\times d$, vector trọng số $\\mathbf{w}$ kích thước $d \\times 1$:
$$\\hat{\\mathbf{y}} = X \\mathbf{w} + \\mathbf{b}$$
- Chip GPU chứa hàng chục ngàn nhân tính toán nhỏ (CUDA cores). Toàn bộ phép nhân ma trận khổng lồ này được ném vào GPU và xử lý **đồng thời song song trong 1 tích tắc (vài mili-giây)**!
- Tốc độ tăng tốc nhanh gấp từ $100$ đến $10.000$ lần so với chạy vòng lặp tuần tự trên CPU!

**3. Thuật toán Gradient Descent dạng ma trận hoàn chỉnh:**
Hãy cùng viết lại thuật toán tối ưu hóa mô hình Hồi quy tuyến tính bằng ngôn ngữ ma trận:
- **Đầu vào:**
  - Ma trận dữ liệu: $X \\in \\mathbb{R}^{N \\times d}$ ($N$ mẫu, $d$ đặc trưng).
  - Vector nhãn thực tế: $\\mathbf{y} \\in \\mathbb{R}^{N \\times 1}$.
  - Vector trọng số cần học: $\\mathbf{w} \\in \\mathbb{R}^{d \\times 1}$.
- **Bước 1: Tính dự đoán cho toàn bộ 1 triệu mẫu cùng lúc:**
  $$\\hat{\\mathbf{y}} = X \\mathbf{w}$$
- **Bước 2: Tính vector sai số của toàn bộ tập dữ liệu:**
  $$\\mathbf{e} = \\hat{\\mathbf{y}} - \\mathbf{y} = X \\mathbf{w} - \\mathbf{y} \\in \\mathbb{R}^{N \\times 1}$$
- **Bước 3: Tính Vector Gradient của hàm Loss theo $\\mathbf{w}$:**
  $$\\nabla_{\\mathbf{w}} L = \\frac{1}{N} X^T (X \\mathbf{w} - \\mathbf{y}) = \\frac{1}{N} X^T \\mathbf{e} \\in \\mathbb{R}^{d \\times 1}$$
  *Kiểm tra kích thước:* $X^T$ có kích thước $(d \\times N)$, nhân với vector sai số $\\mathbf{e}$ kích thước $(N \\times 1)$ cho ra vector gradient có kích thước $(d \\times 1)$ khớp hoàn hảo với số chiều của $\\mathbf{w}$!
- **Bước 4: Cập nhật trọng số theo hướng ngược gradient:**
  $$\\mathbf{w} \\leftarrow \\mathbf{w} - \\eta \\nabla_{\\mathbf{w}} L$$
Chỉ với 4 dòng toán ma trận ngắn gọn, toàn bộ cỗ máy AI triệu tham số đã tự động học tập và hạ dốc sai số cực kỳ mạnh mẽ!""",
                "formula": "\\hat{\\mathbf{y}} = X \\mathbf{w} + \\mathbf{b}, \\quad \\nabla_{\\mathbf{w}} L = \\frac{1}{N} X^T (X \\mathbf{w} - \\mathbf{y}), \\quad \\mathbf{w} \\leftarrow \\mathbf{w} - \\eta \\nabla_{\\mathbf{w}} L",
                "mathExplainer": [
                    { "sym": "X \\in \\mathbb{R}^{N \\times d}", "name": "Ma trận thiết kế (Design Matrix)", "mean": "Bảng chứa toàn bộ dữ liệu huấn luyện gồm N hàng mẫu và d cột thuộc tính." },
                    { "sym": "\\mathbf{e} = X\\mathbf{w} - \\mathbf{y}", "name": "Vector sai số (Residual)", "mean": "Chênh lệch giữa giá trị dự đoán và nhãn thực tế trên toàn bộ N mẫu." },
                    { "sym": "X^T \\mathbf{e}", "name": "Tích ma trận chuyển vị", "mean": "Chiếu sai số ngược lại không gian d chiều của các trọng số để tính đạo hàm riêng." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 620 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="620" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(30, 20)">
                        <text x="120" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Vector Hóa: ŷ = X · w</text>
                        <!-- Matrix X -->
                        <rect x="20" y="35" width="80" height="70" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="60" y="75" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">X (N × d)</text>
                        <text x="115" y="75" font-family="Georgia" font-size="16" text-anchor="middle">×</text>
                        <!-- Vector w -->
                        <rect x="130" y="35" width="30" height="70" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="145" y="75" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">w (d×1)</text>
                        <text x="175" y="75" font-family="Georgia" font-size="16" text-anchor="middle">=</text>
                        <!-- Vector y_hat -->
                        <rect x="190" y="35" width="30" height="70" fill="#e5e5e5" stroke="#111" stroke-width="2"/>
                        <text x="205" y="75" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">ŷ (N×1)</text>
                        <text x="120" y="130" font-family="Georgia" font-size="9" text-anchor="middle">Dự đoán N mẫu chỉ trong 1 phép nhân GPU</text>
                      </g>
                      <g transform="translate(310, 20)">
                        <text x="140" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Gradient Dạng Ma Trận: ∇_w L = (1/N) Xᵀ e</text>
                        <!-- Matrix X^T -->
                        <rect x="20" y="45" width="80" height="40" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="60" y="70" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Xᵀ (d × N)</text>
                        <text x="115" y="70" font-family="Georgia" font-size="16" text-anchor="middle">×</text>
                        <!-- Vector e -->
                        <rect x="130" y="30" width="30" height="80" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <text x="145" y="75" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">e (N×1)</text>
                        <text x="175" y="70" font-family="Georgia" font-size="16" text-anchor="middle">=</text>
                        <!-- Vector grad -->
                        <rect x="190" y="45" width="30" height="40" fill="#111" stroke="#111" stroke-width="2"/>
                        <text x="205" y="70" font-family="Georgia" font-size="10" fill="#fff" font-weight="bold" text-anchor="middle">∇w (d×1)</text>
                        <text x="140" y="130" font-family="Georgia" font-size="9" text-anchor="middle">Khớp hoàn hảo với kích thước vector w!</text>
                      </g>
                    </svg>""",
                    "caption": "Sức mạnh của Vector hóa: Tính toán toàn bộ dự đoán và gradient trên toàn bộ tập dữ liệu chỉ bằng hai phép nhân ma trận."
                },
                "commonPitfalls": "Lỗi kích thước khi nhân Gradient: Nhiều học sinh viết công thức gradient là $X (X\\mathbf{w} - \\mathbf{y})$. SAI KÍCH THƯỚC! Ma trận $X$ có kích thước $(N \\times d)$, vector sai số có kích thước $(N \\times 1)$, hai số ở giữa là $d$ và $N$ không bằng nhau nên không thể nhân được! Bắt buộc phải chuyển vị $X^T$ có kích thước $(d \\times N)$ thì mới nhân được với $(N \\times 1)$ để ra kết quả $(d \\times 1)$!",
                "practiceQuestion": {
                    "level": "Nâng cao",
                    "question": "Trong thuật toán Hồi quy tuyến tính đa biến, tập dữ liệu có N = 500 mẫu và d = 8 đặc trưng. Ma trận tích Xᵀ · X có kích thước bằng bao nhiêu và mang ý nghĩa gì?",
                    "options": [
                        "A. 500 × 500: Ma trận khoảng cách giữa các mẫu dữ liệu",
                        "B. 8 × 8: Ma trận tương quan giữa các đặc trưng (Gram matrix)",
                        "C. 500 × 8: Ma trận dữ liệu gốc",
                        "D. 8 × 1: Vector trọng số tối ưu"
                    ],
                    "correctIndex": 1,
                    "hint": "X có kích thước 500 × 8, vậy Xᵀ có kích thước 8 × 500. Nhân (8 × 500) với (500 × 8) sẽ ra kích thước nào?",
                    "solution": [
                        "Bước 1: Ma trận dữ liệu X có kích thước N × d = 500 × 8.",
                        "Bước 2: Ma trận chuyển vị Xᵀ có kích thước d × N = 8 × 500.",
                        "Bước 3: Thực hiện phép nhân Xᵀ · X: (8 × 500) nhân (500 × 8) => Kích thước kết quả là 8 × 8.",
                        "Ý nghĩa: Ma trận 8 × 8 này đo mức độ tương quan và tích vô hướng giữa 8 đặc trưng của bài toán, xuất hiện trực tiếp trong nghiệm giải tích w = (XᵀX)⁻¹ Xᵀy.",
                        "Đáp án chính xác: B."
                    ]
                }
            }
        ],
        "interactiveWidget": "widget-cosine-similarity",
        "examConnection": {
            "questionTitle": "Phân Tích Dạng Bài Thi Olympic VAIO 2025 (Mã Đề 006)",
            "items": [
                {
                    "code": "Câu 43",
                    "problem": "Tính Cosine Similarity giữa hai vector thuộc tính: $\\mathbf{u} = [3, 4]$ và $\\mathbf{v} = [6, 8]$.",
                    "solution": [
                        "Mẹo giải thần tốc trong 2 giây: Nhận thấy vector $\\mathbf{v} = 2\\mathbf{u}$ (tỉ lệ dương gấp 2 lần).",
                        "Hai vector tỉ lệ dương thì hoàn toàn cùng hướng (góc lệch $\\theta = 0^\\circ$).",
                        "Do đó $\\cos(0^\\circ) = 1.0$ ngay lập tức, không cần tốn thời gian bấm máy tính!"
                    ]
                },
                {
                    "code": "Câu 47",
                    "problem": "Tính đầu ra nơ-ron: Vector trọng số $\\mathbf{w} = [1, 4, 3]$, vector đầu vào $\\mathbf{x} = [4, 8, 5]$, hệ số kích hoạt tuyến tính $k = 3$.",
                    "solution": [
                        "Bước 1: Tính tích vô hướng tổng có trọng số: $z = \\mathbf{w} \\cdot \\mathbf{x} = 1(4) + 4(8) + 3(5) = 4 + 32 + 15 = 51$.",
                        "Bước 2: Nhân với hệ số kích hoạt: $Output = k \\times z = 3 \\times 51 = 153$."
                    ]
                }
            ]
        },
        "takeaways": [
            "Đại số tuyến tính phân cấp dữ liệu thành 4 cấp: Scalar (0D, 1 số), Vector (1D, 1 đối tượng), Matrix (2D, bảng dữ liệu/ảnh xám), Tensor (3D/4D+, ảnh màu RGB/video).",
            "Tích vô hướng (Dot product) $\\mathbf{u} \\cdot \\mathbf{v}$ nhân rồi cộng ra 1 con số (Scalar); Tích Hadamard $\\mathbf{u} \\odot \\mathbf{v}$ nhân từng vị trí độc lập ra 1 vector/ma trận cùng kích thước.",
            "Phép nhân ma trận yêu cầu số cột ma trận trước bằng số hàng ma trận sau: $(m \\times k) \\times (k \\times n) = (m \\times n)$, và KHÔNG có tính chất giao hoán ($AB \\neq BA$).",
            "Chuyển vị của tích bắt buộc đảo ngược thứ tự: $(AB)^T = B^T A^T$.",
            "Cosine Similarity đo góc lệch $\\cos(\\theta) = \\frac{\\mathbf{u} \\cdot \\mathbf{v}}{\\|\\mathbf{u}\\| \\|\\mathbf{v}\\|} \\in [-1, 1]$, triệt tiêu ảnh hưởng của độ dài để so sánh ngữ nghĩa trong hệ thống gợi ý và LLMs."
        ]
    }

if __name__ == "__main__":
    l2 = get_masterpiece_lesson_2()
    print("Masterpiece Lesson 2 generated successfully!")
    print(f"Title: {l2['title']}")
    print(f"Sections count: {len(l2['sections'])}")
    for i, s in enumerate(l2['sections']):
        print(f"  Sec {i+1}: {s['heading']} (deepDive: {len(s['deepDive'])} chars)")
