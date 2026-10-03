# -*- coding: utf-8 -*-
"""
upgrade_lesson_11.py - Masterpiece Lesson 11 for VAIO 2025 AI Olympiad
Chủ đề: Thị Giác Máy Tính: CNN, ResNet & Nhận Diện Vật Thể
Toàn diện từ con số 0 đến làm chủ sâu sắc.

Tuân thủ nghiêm ngặt chuẩn sư phạm:
Trực giác đời sống -> Bản chất toán học -> Cách thức hoạt động ->
Giải mã ký hiệu cho học sinh lớp 12 -> Ví dụ tính toán bằng số từng bước ->
Cạm bẫy phòng thi -> Câu hỏi trắc nghiệm kiểm tra độ hiểu có lời giải chi tiết.
"""

def get_masterpiece_lesson_11():
    return {
        "id": "lesson-11",
        "title": "11. Thị Giác Máy Tính: CNN, ResNet & Nhận Diện Vật Thể",
        "syllabusBadge": "BUỔI 9: THỊ GIÁC MÁY TÍNH (CV): CNN, RESNET & OBJECT DETECTION",
        "summary": "Khám phá thế giới Thị Giác Máy Tính từ con số 0: Bản chất ma trận điểm ảnh, phép tích chập (Convolution 2D), bộ lọc (Kernel), bước nhảy (Stride), viền đệm (Padding) và công thức kích thước đầu ra; tính toán số lượng tham số học được (Câu 2 VAIO) và độ phức tạp FLOPs (Câu 43 VAIO); lớp gom cụm Pooling và trường tiếp nhận (Receptive Field); giải mã hiện tượng suy thoái mạng sâu và giải pháp đột phá Cầu vượt cao tốc ResNet (Câu 31 VAIO); cùng tác vụ nhận diện vật thể (Object Detection) với chỉ số IoU và thuật toán Triệt tiêu không cực đại NMS (Câu 10 VAIO).",
        "intuition": {
            "title": "Trực giác thực tế: Chiếc kính lúp rà soát hoa văn & Ban giám khảo lọc khung hình trùng lặp",
            "content": r"""Để hiểu trọn vẹn Thị Giác Máy Tính và Mạng Tích Chập (CNN) mà không bị bỡ ngỡ, hãy quan sát hai hình ảnh đời sống sau:

**1. Chiếc kính lúp rà soát hoa văn & Cầu vượt cao tốc ResNet:**
- Hãy tưởng tượng bạn được giao một bức tranh tường khổng lồ kích thước $1,000 \times 1,000$ pixel màu (chứa tới 3 triệu con số!). Nếu bạn dùng mạng nơ-ron kết nối đầy đủ (MLP), mỗi nơ-ron ở tầng sau sẽ cần nối 3 triệu sợi dây tới từng điểm ảnh. Một tầng ẩn 1,000 nơ-ron sẽ đòi hỏi tới **3 TỶ TRỌNG SỐ KẾT NỐI**! Máy tính sẽ ngay lập tức bốc khói vì quá tải bộ nhớ. Nguy hiểm hơn, nếu bạn duỗi thẳng bức tranh thành 1 hàng ngang, mối liên hệ trên-dưới-trái-phải của các nét vẽ bị đứt gãy hoàn toàn!
- Thay vào đó, **CNN (Convolutional Neural Network)** hoạt động như một nhà thám tử cầm một chiếc kính lúp nhỏ $3 \times 3$ pixel:
  - Thám tử trượt chiếc kính lúp khắp bức tranh: từ trái sang phải, từ trên xuống dưới.
  - Chiếc kính lúp này dùng **CHUNG DUY NHẤT MỘT BỘ QUY TẮC SOI NÉT** trên toàn bộ bức ảnh (**Chia sẻ trọng số - Weight Sharing**)!
  - Dù chiếc tai mèo nằm ở góc trên bên trái hay chạy xuống góc dưới bên phải, chiếc kính lúp đều phát hiện ra đặc trưng đó một cách chính xác (**Bất biến dịch chuyển**)! Số lượng tham số giảm ngoạn mục từ 3 tỷ xuống chỉ còn vỏn vẹn vài chục con số!
- Và khi ta xếp chồng 100 lớp kính lúp để phân tích các chi tiết siêu tinh xảo, tín hiệu gradient bị tiêu biến và nghẽn tắc giữa đường (Hiện tượng suy thoái mạng sâu). Kaiming He đã xây một chiếc **CẦU VƯỢT CAO TỐC (Skip Connection trong ResNet)** nhảy cóc qua hai tầng, cho phép tín hiệu gradient phóng thẳng từ đích về vạch xuất phát mà không bị suy hao!

---

**2. Ban giám khảo chọn hoa hậu & Thuật toán NMS trong Nhận diện vật thể:**
- Trong tác vụ Nhận diện vật thể (Object Detection), khi phát hiện một chú chó trong bức ảnh, mô hình máy tính có thể vẽ ra 20 chiếc khung hộp chữ nhật chồng chéo lên nhau quanh cùng chú chó đó với các điểm tin cậy khác nhau ($0.95, 0.90, 0.85, \dots$).
- Ta không thể để 20 chiếc khung đè lên nhau như vậy được. Thuật toán **NMS (Non-Maximum Suppression - Triệt tiêu không cực đại)** đóng vai trò như ban giám khảo:
  1. Chọn ra chiếc khung có điểm số cao nhất (Hạng nhất $0.95$).
  2. Đo độ chồng lấn (**Chỉ số IoU**) giữa chiếc khung này với tất cả các khung còn lại.
  3. Những chiếc khung nào trùng lặp quá nhiều ($\text{IoU} > 0.40$) sẽ bị "triệt tiêu" và loại bỏ ngay lập tức!
  4. Lặp lại cho đến khi chỉ còn lại đúng 1 chiếc khung duy nhất ôm khít lấy chú chó!"""
        },
        "sections": [
            # =================================================================
            # MỤC 11.1: MÁY TÍNH NHÌN ẢNH & PHÉP TÍCH CHẬP CONVOLUTION
            # =================================================================
            {
                "heading": "11.1. Khởi Đầu Từ Con Số 0: Máy Tính 'Nhìn' Ảnh Như Thế Nào? Tại Sao Mạng Nơ-ron Cổ Điển (MLP) Thất Bại & Phép Tích Chập Ra Đời",
                "content": "Khám phá cách biểu diễn hình ảnh số dưới dạng ma trận và tensor đa chiều; phân tích 3 lý do chí mạng khiến mạng MLP thất bại trên dữ liệu ảnh; cơ chế toán học của phép tích chập (Convolution 2D) và hai siêu năng lực của CNN.",
                "deepDive": r"""**1. Máy tính 'nhìn' một bức ảnh như thế nào?**
Con người nhìn một bức ảnh và cảm nhận được màu sắc, ánh sáng, hình dáng chú mèo hay nụ cười của bạn bè. Nhưng máy tính không có mắt sinh học, nó hoàn toàn mù màu và chỉ nhìn thấy **CÁC MA TRẬN CON SỐ NGUYÊN (Pixel Grid)**:
- **Ảnh đa mức xám (Grayscale Image):**
  - Được biểu diễn bằng một ma trận 2 chiều kích thước $H \times W$ (Chiều cao $\times$ Chiều rộng).
  - Mỗi phần tử (Pixel) là một số nguyên từ $0$ đến $255$:
    - Giá trị $0$: Điểm ảnh đen tuyền hoàn toàn.
    - Giá trị $255$: Điểm ảnh trắng tinh khiết.
    - Giá trị nằm giữa $(1 \dots 254)$: Các mức độ xám chuyển tiếp.
- **Ảnh màu RGB (Red, Green, Blue):**
  - Được biểu diễn bằng một **Tensor 3 chiều** kích thước $H \times W \times C$, trong đó $C = 3$ là số kênh màu:
    - Kênh 0: Ma trận cường độ màu Đỏ (Red).
    - Kênh 1: Ma trận cường độ màu Lục (Green).
    - Kênh 2: Ma trận cường độ màu Lam (Blue).
  - Một điểm ảnh màu là sự pha trộn của bộ 3 số $(R, G, B)$ tại cùng tọa độ $(y, x)$.

---

**2. Ba lý do chí mạng khiến Mạng nơ-ron cổ điển (MLP) thất bại hoàn toàn trên dữ liệu ảnh:**
Trước khi CNN ra đời, các kỹ sư cố gắng dùng mạng MLP (kết nối đầy đủ - Fully Connected) để xử lý ảnh, nhưng đã vấp phải 3 bức tường thép không thể vượt qua:
1. **Bùng nổ tham số (Parameter Explosion):**
   - Xét một bức ảnh màu cỡ vừa $256 \times 256 \times 3 = 196,608$ điểm ảnh.
   - Để đưa vào mạng MLP, ta phải duỗi thẳng thành một vector đầu vào có $196,608$ chiều.
   - Nếu tầng ẩn đầu tiên chỉ có khiêm tốn $1,000$ nơ-ron, số trọng số kết nối sẽ là:
     $$196,608 \times 1,000 \approx 196.6 \text{ triệu trọng số!}$$
   - Số lượng tham số quá khổng lồ làm tràn ngập bộ nhớ RAM/GPU và chắc chắn dẫn tới hiện tượng **Quá khớp (Overfitting)** trầm trọng (mạng chỉ học vẹt mà không hiểu tổng quát).
2. **Phá hủy hoàn toàn cấu trúc không gian 2 chiều (Spatial Topology Destruction):**
   - Thao tác "duỗi thẳng" (Flatten) biến lưới 2D thành một đường thẳng 1D.
   - Hai điểm ảnh vốn nằm kề sát nhau theo phương dọc (như hàng 10 cột 5 và hàng 11 cột 5) sẽ bị đẩy xa nhau hàng trăm phần tử trong vector 1D! Mối tương quan không gian lân cận cực kỳ quý giá giữa các điểm ảnh bị xóa sổ hoàn toàn.
3. **Mất tính bất biến dịch chuyển (Lack of Translation Invariance):**
   - Trong MLP, mỗi nơ-ron gắn chặt với một vị trí tọa độ cố định. Nếu mô hình được học nhận diện mắt mèo ở góc trên bên trái, khi chú mèo dịch chuyển sang góc dưới bên phải, toàn bộ các pixel kích hoạt các nơ-ron hoàn toàn khác, và MLP sẽ thất bại thảm hại!

---

**3. Phép Tích Chập (Convolution) & Cảm hứng sinh học vỏ não thị giác:**
Vào năm 1959, hai nhà sinh lý học **David Hubel** và **Torsten Wiesel** đã tiến hành thí nghiệm lịch sử trên vỏ não thị giác của loài mèo (đoạt giải Nobel Y học năm 1981): Họ phát hiện các nơ-ron thị giác không nhìn toàn bộ tầm mắt cùng lúc, mà mỗi nơ-ron chỉ phản hồi với một vùng cục bộ nhỏ gọi là **Trường tiếp nhận (Receptive Field)**, và các tầng nơ-ron sơ cấp chỉ chuyên phát hiện các cạnh thẳng đơn giản (ngang, dọc, chéo).

Mô hình **CNN (Convolutional Neural Network)** ra đời dựa trên nguyên lý này:
- Thay vì kết nối toàn bộ, ta dùng một ma trận nhỏ gọi là **Bộ lọc (Kernel / Filter)** (thường kích thước $3 \times 3$ hoặc $5 \times 5$).
- **Quy trình tính toán Tích chập 2D:**
  1. Đặt bộ lọc $K$ đè lên một góc của ảnh đầu vào $I$.
  2. Nhân từng phần tử tương ứng của bộ lọc với pixel của ảnh (Element-wise Multiplication).
  3. Cộng dồn toàn bộ các tích lại và cộng thêm 1 hệ số bias $b$:
     $$S(i, j) = \sum_{m} \sum_{n} I(i + m, j + n) K(m, n) + b$$
  4. Trượt bộ lọc sang vị trí tiếp theo và lặp lại phép tính.
  5. Toàn bộ các giá trị thu được tạo thành một ma trận đầu ra mới gọi là **Bản đồ đặc trưng (Feature Map)**!

---

**4. Hai siêu năng lực đưa CNN thống trị thị giác máy tính:**
1. **Vùng tiếp nhận cục bộ (Local Receptive Fields):** Mỗi nơ-ron chỉ quan sát một cụm pixel $3 \times 3$ lân cận, bảo tồn nguyên vẹn tính chất hình học 2D của bức ảnh.
2. **Chia sẻ trọng số (Weight Sharing):** Cùng một bộ lọc $3 \times 3$ (chỉ gồm 9 con số) được quét đồng nhất trên toàn bộ bức ảnh!
   - Giúp giảm số tham số từ 200 triệu xuống còn **9 tham số**!
   - Đem lại tính **Bất biến dịch chuyển (Translation Equivariance)**: Dù bông hoa hay con chim xuất hiện ở bất kỳ góc nào trong khung hình, bộ lọc đều phát hiện ra đặc trưng đó!""",
                "formula": r"S(i, j) = (I * K)(i, j) + b = \sum_{m=0}^{K_h-1} \sum_{n=0}^{K_w-1} I(i + m, j + n) K(m, n) + b",
                "mathExplainer": [
                    { "sym": "I(i, j)", "name": "Điểm ảnh đầu vào", "mean": "Giá trị pixel của bức ảnh tại tọa độ hàng i, cột j (thang đo 0 đến 255)." },
                    { "sym": "K(m, n)", "name": "Trọng số bộ lọc (Kernel)", "mean": "Ma trận nhỏ chứa các trọng số có thể học được (thường cỡ 3x3 hoặc 5x5)." },
                    { "sym": "S(i, j)", "name": "Bản đồ đặc trưng (Feature Map)", "mean": "Đầu ra sau phép tích chập, thể hiện mức độ xuất hiện của đặc trưng tại từng vị trí." },
                    { "sym": "*", "name": "Toán tử Tích chập", "mean": "Phép nhân từng phần tử rồi cộng dồn giữa cửa sổ trượt và bộ lọc." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 660 190" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">
                      <rect width="660" height="190" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Left: Image 5x5 -->
                      <g transform="translate(25, 20)">
                        <text x="60" y="15" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Ảnh Đầu Vào 5×5</text>
                        <rect x="0" y="25" width="120" height="120" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <!-- Grid lines -->
                        <line x1="24" y1="25" x2="24" y2="145" stroke="#ccc"/><line x1="48" y1="25" x2="48" y2="145" stroke="#ccc"/><line x1="72" y1="25" x2="72" y2="145" stroke="#ccc"/><line x1="96" y1="25" x2="96" y2="145" stroke="#ccc"/>
                        <line x1="0" y1="49" x2="120" y2="49" stroke="#ccc"/><line x1="0" y1="73" x2="120" y2="73" stroke="#ccc"/><line x1="0" y1="97" x2="120" y2="97" stroke="#ccc"/><line x1="0" y1="121" x2="120" y2="121" stroke="#ccc"/>
                        <!-- Highlighted 3x3 receptive window -->
                        <rect x="0" y="25" width="72" height="72" fill="#e0e0e0" stroke="#111" stroke-width="2"/>
                        <text x="36" y="65" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Vùng 3×3</text>
                      </g>
                      <!-- Operator * -->
                      <text x="175" y="95" font-family="Georgia" font-size="20" font-weight="bold" text-anchor="middle">∗</text>
                      <!-- Center: Kernel 3x3 -->
                      <g transform="translate(205, 45)">
                        <text x="45" y="-10" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Bộ Lọc 3×3</text>
                        <rect x="0" y="0" width="90" height="90" fill="#111" rx="3"/>
                        <line x1="30" y1="0" x2="30" y2="90" stroke="#fff" stroke-width="0.8"/>
                        <line x1="60" y1="0" x2="60" y2="90" stroke="#fff" stroke-width="0.8"/>
                        <line x1="0" y1="30" x2="90" y2="30" stroke="#fff" stroke-width="0.8"/>
                        <line x1="0" y1="60" x2="90" y2="60" stroke="#fff" stroke-width="0.8"/>
                        <text x="15" y="20" font-family="Georgia" font-size="9" fill="#fff" text-anchor="middle">w₁</text>
                        <text x="45" y="20" font-family="Georgia" font-size="9" fill="#fff" text-anchor="middle">w₂</text>
                        <text x="75" y="20" font-family="Georgia" font-size="9" fill="#fff" text-anchor="middle">w₃</text>
                        <text x="45" y="50" font-family="Georgia" font-size="9" fill="#fff" text-anchor="middle">w₅</text>
                        <text x="45" y="80" font-family="Georgia" font-size="9" fill="#fff" text-anchor="middle">w₈</text>
                      </g>
                      <!-- Operator = -->
                      <text x="325" y="95" font-family="Georgia" font-size="20" font-weight="bold" text-anchor="middle">⇒</text>
                      <!-- Right: Feature Map 3x3 -->
                      <g transform="translate(355, 45)">
                        <text x="45" y="-10" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Bản Đồ Đặc Trưng 3×3</text>
                        <rect x="0" y="0" width="90" height="90" fill="#fff" stroke="#111" stroke-width="1.5"/>
                        <line x1="30" y1="0" x2="30" y2="90" stroke="#ccc"/>
                        <line x1="60" y1="0" x2="60" y2="90" stroke="#ccc"/>
                        <line x1="0" y1="30" x2="90" y2="30" stroke="#ccc"/>
                        <line x1="0" y1="60" x2="90" y2="60" stroke="#ccc"/>
                        <!-- Highlighted single pixel output -->
                        <rect x="0" y="0" width="30" height="30" fill="#111"/>
                        <text x="15" y="20" font-family="Georgia" font-size="10" fill="#fff" font-weight="bold" text-anchor="middle">S₁₁</text>
                      </g>
                      <!-- Summary panel -->
                      <g transform="translate(470, 35)">
                        <rect x="0" y="0" width="170" height="110" fill="#fff" stroke="#111" stroke-width="1"/>
                        <text x="85" y="20" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Ưu Thế Vượt Trội CNN</text>
                        <text x="10" y="42" font-family="Georgia" font-size="9">• Bảo toàn hình học 2D</text>
                        <text x="10" y="62" font-family="Georgia" font-size="9">• Giảm 99.9% tham số</text>
                        <text x="10" y="82" font-family="Georgia" font-size="9">• Bất biến dịch chuyển</text>
                        <text x="10" y="100" font-family="Georgia" font-size="8" fill="#555">(Weight Sharing)</text>
                      </g>
                    </svg>""",
                    "caption": "Cơ chế toán học của phép Tích chập 2D: Bộ lọc 3x3 trượt trên vùng tiếp nhận cục bộ của ảnh 5x5, tính tích vô hướng và sinh ra từng điểm ảnh trên Bản đồ đặc trưng."
                },
                "commonPitfalls": "Nhầm lẫn giữa Tích chập (Convolution) và Tương quan chéo (Cross-correlation): Trong toán học thuần túy, tích chập yêu cầu lật ngược bộ lọc 180 độ trước khi nhân. Tuy nhiên trong Deep Learning, vì các trọng số trong bộ lọc được học ngẫu nhiên từ đầu, việc lật ngược hay không hoàn toàn không làm thay đổi kết quả học tập! Mọi thư viện như PyTorch, TensorFlow thực chất đều cài đặt phép Tương quan chéo nhưng vẫn gọi tên là Convolution.",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Tại sao mạng nơ-ron tích chập (CNN) lại vượt trội hơn hoàn toàn so với mạng nơ-ron kết nối đầy đủ (MLP) khi xử lý dữ liệu hình ảnh 2 chiều?",
                    "options": [
                        "A. Vì CNN chuyển đổi mọi điểm ảnh thành chuỗi văn bản trước khi xử lý",
                        "B. Vì CNN áp dụng cơ chế chia sẻ trọng số (weight sharing) và vùng tiếp nhận cục bộ, giúp bảo tồn cấu trúc không gian 2D và giảm mạnh số lượng tham số",
                        "C. Vì CNN không cần sử dụng bất kỳ hàm kích hoạt phi tuyến nào",
                        "D. Vì CNN loại bỏ hoàn toàn quá trình tính toán lan truyền ngược"
                    ],
                    "correctIndex": 1,
                    "hint": "Cùng một bộ lọc trượt trên toàn bộ bức ảnh giúp tiết kiệm hàng triệu trọng số.",
                    "solution": [
                        "Bước 1: Mạng MLP duỗi thẳng ma trận ảnh 2D thành vector 1D làm phá vỡ hoàn toàn mối liên hệ không gian giữa các pixel lân cận.",
                        "Bước 2: MLP có quá nhiều trọng số (hàng trăm triệu) gây bùng nổ tham số và overfitting.",
                        "Bước 3: CNN giải quyết hoàn hảo 2 nhược điểm này bằng cách giữ nguyên ảnh 2D/3D, sử dụng vùng tiếp nhận cục bộ và chia sẻ trọng số (weight sharing) của bộ lọc.",
                        "Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 11.2: BỘ TỨ SIÊU THAM SỐ & CÔNG THỨC KÍCH THƯỚC ĐẦU RA
            # =================================================================
            {
                "heading": "11.2. Bộ 4 Siêu Tham Số Cốt Lõi (Kernel, Stride, Padding, Channel) & Công Thức Kích Thước Đầu Ra (Câu 27, 35 VAIO)",
                "content": "Làm chủ 4 thông số điều khiển lớp Conv2D: Kích thước bộ lọc, bước nhảy, các chế độ đệm viền (Valid vs Same Padding), và công thức vàng tính kích thước không gian đầu ra chuẩn đề thi Olympic AI.",
                "deepDive": r"""**1. Chi tiết 4 Siêu tham số điều khiển lớp Conv2D:**
Mỗi lớp tích chập Conv2D được định hình bởi 4 siêu tham số do kỹ sư con người thiết lập:
1. **Kích thước Kernel ($K$ - Kernel Size):**
   - Chiều cao và chiều rộng của cửa sổ trượt (thường là hình vuông $K \times K$).
   - Quy chuẩn vàng: **Luôn chọn $K$ là số lẻ** ($1 \times 1, 3 \times 3, 5 \times 5, 7 \times 7$).
   - *Lý do:* Số lẻ luôn có đúng **MỘT ĐIỂM TÂM ĐỐI XỨNG DUY NHẤT** tại tọa độ $(\frac{K-1}{2}, \frac{K-1}{2})$, giúp định vị pixel đầu ra trùng khớp chính xác với tâm của vùng tiếp nhận!
2. **Bước nhảy ($S$ - Stride):**
   - Số lượng pixel mà bộ lọc dịch chuyển sau mỗi lần tính toán:
     - $S = 1$: Bộ lọc trượt từng pixel một, trích xuất đặc trưng dày đặc và chi tiết.
     - $S = 2$: Bộ lọc nhảy cóc 2 pixel mỗi lần. Kết quả: Chiều rộng và chiều cao của bản đồ đặc trưng đầu ra **bị giảm đi một nửa**! (Thường dùng Stride $S=2$ để giảm kích thước không gian thay cho lớp Pooling).
3. **Viền đệm ($P$ - Padding):**
   - Thêm các hàng và cột chứa số $0$ (Zero-padding) bao quanh mép ngoài của bức ảnh.
   - *Tại sao phải dùng Padding?*
     - Nếu không dùng padding, sau mỗi lần trượt tích chập, ảnh sẽ bị co nhỏ lại liên tục. Qua 10 tầng, ảnh $32 \times 32$ sẽ bị teo tóp về $0 \times 0$!
     - Các pixel nằm ở góc mép ảnh chỉ được bộ lọc quét qua 1 lần duy nhất, trong khi pixel ở giữa được quét tới 9 lần. Padding giúp các pixel ở mép ảnh được bảo toàn thông tin công bằng như pixel ở tâm.
   - **Hai chế độ Padding kinh điển:**
     - **Chế độ `valid` ($P = 0$):** Không thêm bất kỳ viền nào. Ảnh đầu ra bị co nhỏ kích thước.
     - **Chế độ `same`:** Tự động đệm thêm số pixel $P$ sao cho **KÍCH THƯỚC ĐẦU RA BẰNG ĐÚNG KÍCH THƯỚC ĐẦU VÀO** (khi $S = 1$)!
       Công thức tính số pixel đệm $P$ mỗi phía:
       $$P = \frac{K - 1}{2}$$
       *(Ví dụ: Với Kernel $3 \times 3$, cần đệm $P = \frac{3-1}{2} = 1$ viền 0 quanh ảnh. Với Kernel $5 \times 5$, cần đệm $P = \frac{5-1}{2} = 2$).*
4. **Số kênh vào và ra ($C_{\text{in}}, C_{\text{out}}$):**
   - $C_{\text{in}}$: Số kênh của ảnh đầu vào (ảnh xám $= 1$, ảnh màu $= 3$, hoặc số feature map của tầng trước).
   - $C_{\text{out}}$: Số lượng bộ lọc độc lập được sử dụng. Mỗi bộ lọc học một mẫu hình riêng, do đó đầu ra sẽ có đúng $C_{\text{out}}$ bản đồ đặc trưng xếp chồng lên nhau.

---

**2. CÔNG THỨC VÀNG TÍNH KÍCH THƯỚC ĐẦU RA (Trọng tâm Câu 27, 35 Đề thi VAIO 2025):**
Cho ảnh đầu vào có kích thước chiều rộng $W_{\text{in}}$ (hoặc chiều cao $H_{\text{in}}$), kích thước bộ lọc $K$, viền đệm $P$ và bước nhảy $S$:
$$W_{\text{out}} = \left\lfloor \frac{W_{\text{in}} - K + 2P}{S} \right\rfloor + 1$$
*(Trong đó ký hiệu $\lfloor x \rfloor$ là phép lấy phần nguyên / làm tròn xuống).*

---

**3. Mẹo tính nhẩm cực nhanh trong phòng thi Olympic AI:**
- **Mẹo 1: Khi đề bài cho `padding='same'` và bước nhảy $S$ (Câu 27 VAIO):**
  Bạn không cần tính $P$ phức tạp, kích thước đầu ra chỉ đơn giản là:
  $$W_{\text{out}} = \left\lceil \frac{W_{\text{in}}}{S} \right\rceil$$
  *(Ví dụ: Ảnh $W = 224$, `padding='same'`, $S = 2 \implies W_{\text{out}} = \lceil 224 / 2 \rceil = 112$).*
- **Mẹo 2: Khi đề bài cho `padding='valid'` ($P = 0$) và $S = 1$:**
  $$W_{\text{out}} = W_{\text{in}} - K + 1$$
  *(Ví dụ: Ảnh $W = 32$, Kernel $K = 5 \implies W_{\text{out}} = 32 - 5 + 1 = 28$).*

---

**4. Bài tập tính tay mẫu từng bước:**
*Đề bài:* Cho một bức ảnh đầu vào kích thước $64 \times 64$, đưa qua lớp Conv2D có bộ lọc kích thước $K = 7 \times 7$, viền đệm $P = 2$, bước nhảy $S = 2$. Hỏi kích thước bản đồ đặc trưng đầu ra là bao nhiêu?
- **Bước 1:** Xác định các thông số: $W_{\text{in}} = 64, K = 7, P = 2, S = 2$.
- **Bước 2:** Áp dụng công thức vàng:
  $$W_{\text{out}} = \left\lfloor \frac{64 - 7 + 2(2)}{2} \right\rfloor + 1 = \left\lfloor \frac{64 - 7 + 4}{2} \right\rfloor + 1 = \left\lfloor \frac{61}{2} \right\rfloor + 1$$
- **Bước 3:** Tính phần nguyên: $\lfloor 30.5 \rfloor = 30$.
- **Bước 4:** Cộng thêm 1: $W_{\text{out}} = 30 + 1 = 31$.
- **Kết luận:** Bản đồ đặc trưng đầu ra có kích thước không gian là $31 \times 31$!""",
                "formula": r"W_{\text{out}} = \left\lfloor \frac{W_{\text{in}} - K + 2P}{S} \right\rfloor + 1, \quad P_{\text{same}} = \frac{K - 1}{2}, \quad W_{\text{out}}^{\text{same}} = \left\lceil \frac{W_{\text{in}}}{S} \right\rceil",
                "mathExplainer": [
                    { "sym": "W_{\\text{in}}, W_{\\text{out}}", "name": "Kích thước vào và ra", "mean": "Chiều rộng (hoặc chiều cao) của ma trận đặc trưng trước và sau lớp tích chập." },
                    { "sym": "K", "name": "Kích thước Kernel", "mean": "Cạnh của cửa sổ bộ lọc trượt (luôn chọn số lẻ như 3, 5, 7 để có tâm đối xứng)." },
                    { "sym": "2P", "name": "Tổng viền đệm", "mean": "Nhân đôi vì đệm thêm P pixel ở cả 2 phía đối diện (trái + phải, trên + dưới)." },
                    { "sym": "S", "name": "Bước nhảy (Stride)", "mean": "Khoảng cách dịch chuyển của bộ lọc sau mỗi bước; S=2 làm giảm kích thước một nửa." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 660 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="660" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Left: Valid Padding -->
                      <g transform="translate(25, 20)">
                        <rect x="0" y="0" width="280" height="140" fill="#fff" stroke="#111" stroke-width="1.2"/>
                        <text x="140" y="20" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Valid Padding (P = 0): Co Nhỏ</text>
                        <!-- 4x4 input to 2x2 output with 3x3 kernel -->
                        <rect x="25" y="35" width="80" height="80" fill="#fafafa" stroke="#111" stroke-width="1.5"/>
                        <rect x="25" y="35" width="60" height="60" fill="#e0e0e0" stroke="#111" stroke-width="1.5"/>
                        <text x="55" y="70" font-family="Georgia" font-size="9" text-anchor="middle">K=3×3</text>
                        <text x="65" y="130" font-family="Georgia" font-size="9">Ảnh 4×4</text>
                        <text x="135" y="80" font-family="Georgia" font-size="14" font-weight="bold">⇒</text>
                        <rect x="175" y="55" width="40" height="40" fill="#111"/>
                        <text x="195" y="80" font-family="Georgia" font-size="10" fill="#fff" font-weight="bold" text-anchor="middle">2×2</text>
                        <text x="195" y="115" font-family="Georgia" font-size="8" fill="#555" text-anchor="middle">W_out = 4 - 3 + 1 = 2</text>
                      </g>
                      <!-- Right: Same Padding -->
                      <g transform="translate(335, 20)">
                        <rect x="0" y="0" width="300" height="140" fill="#fff" stroke="#111" stroke-width="1.2"/>
                        <text x="150" y="20" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Same Padding (P = 1): Giữ Nguyên Kích Thước</text>
                        <!-- Padded 4x4 to 6x6 with dashed border -->
                        <rect x="25" y="35" width="80" height="80" fill="none" stroke="#888" stroke-dasharray="3,3" stroke-width="1.5"/>
                        <rect x="35" y="45" width="60" height="60" fill="#fafafa" stroke="#111" stroke-width="1.5"/>
                        <text x="65" y="80" font-family="Georgia" font-size="9" text-anchor="middle">Ảnh 4×4</text>
                        <text x="65" y="130" font-family="Georgia" font-size="8" fill="#555" text-anchor="middle">+ Viền 0 xung quanh (P=1)</text>
                        <text x="140" y="80" font-family="Georgia" font-size="14" font-weight="bold">⇒</text>
                        <rect x="180" y="45" width="60" height="60" fill="#111"/>
                        <text x="210" y="80" font-family="Georgia" font-size="11" fill="#fff" font-weight="bold" text-anchor="middle">4×4</text>
                        <text x="210" y="125" font-family="Georgia" font-size="8" fill="#555" text-anchor="middle">W_out = W_in = 4 (khi S=1)</text>
                      </g>
                    </svg>""",
                    "caption": "So sánh hai cơ chế Padding: Valid Padding (không đệm, kích thước co nhỏ) vs Same Padding (đệm viền 0 xung quanh, bảo toàn kích thước ảnh đầu ra)."
                },
                "commonPitfalls": "Quên nhân đôi 2P trong công thức: Rất nhiều học sinh viết công thức là (W - K + P) / S + 1. SAI! Vì viền đệm được thêm vào CẢ HAI PHÍA (bên trái và bên phải, hoặc phía trên và phía dưới), nên số pixel tăng thêm vào chiều rộng luôn là 2P!",
                "practiceQuestion": {
                    "level": "Vận dụng (Câu 27 & 35 Đề Thi VAIO 2025)",
                    "question": "Cho một bản đồ đặc trưng đầu vào có kích thước 28×28 đưa qua một lớp Conv2D có bộ lọc kích thước 5×5, bước nhảy S = 2 và viền đệm P = 1. Kích thước không gian của bản đồ đặc trưng đầu ra là bao nhiêu?",
                    "options": [
                        "A. 14×14",
                        "B. 13×13",
                        "C. 12×12",
                        "D. 15×15"
                    ],
                    "correctIndex": 1,
                    "hint": "Áp dụng công thức: floor((28 - 5 + 2*1) / 2) + 1.",
                    "solution": [
                        "Bước 1: Xác định các đại lượng: W_in = 28, K = 5, P = 1, S = 2.",
                        "Bước 2: Thay vào công thức: W_out = floor((28 - 5 + 2*1) / 2) + 1 = floor(25 / 2) + 1.",
                        "Bước 3: floor(12.5) = 12.",
                        "Bước 4: W_out = 12 + 1 = 13.",
                        "Kết quả: Bản đồ đặc trưng đầu ra có kích thước 13×13. Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 11.3: ĐẾM THAM SỐ HỌC ĐƯỢC & TÍNH TOÁN FLOPS
            # =================================================================
            {
                "heading": "11.3. Đếm Tham Số Học Được (Learnable Parameters - Câu 2 VAIO) & Độ Phức Tạp Tính Toán FLOPs (Câu 43 VAIO)",
                "content": "Phân biệt tuyệt đối giữa tham số học được và siêu tham số; thiết lập công thức tổng quát đếm tham số 1 lớp tích chập Conv2D; tính toán số phép tính dấu phẩy động FLOPs và MACs trong bài thi Olympic AI.",
                "deepDive": r"""**1. Phân biệt cốt tử: Tham số học được vs Siêu tham số (Câu 2 Đề thi VAIO 2025):**
Một trong những câu hỏi lý thuyết bẫy kinh điển nhất của đề thi VAIO:
> *'Thành phần nào là tham số có thể học (Learnable Parameter) trong lớp Conv2D?'*

- **Tham số có thể học (Learnable Parameters):**
  - Là những con số nằm BÊN TRONG BỘ LỌC: **Các trọng số của Filter (Weights)** và **Hệ số lệch (Bias)**!
  - Ban đầu được khởi tạo ngẫu nhiên, sau đó mô hình TỰ ĐỘNG CẬP NHẬT giá trị tối ưu thông qua quá trình lan truyền ngược Backpropagation.
- **Siêu tham số (Hyperparameters):**
  - Kích thước ảnh, Kích thước bộ lọc $K$, Bước nhảy $S$, Viền đệm $P$, Số lượng bộ lọc $C_{\text{out}}$ do KỸ SƯ CON NGƯỜI THIẾT LẬP CỐ ĐỊNH từ trước, mô hình không thể tự học được các số này!

---

**2. CÔNG THỨC ĐẾM THAM SỐ 1 LỚP CONV2D:**
Xét một lớp tích chập nhận đầu vào có $C_{\text{in}}$ kênh, sử dụng $C_{\text{out}}$ bộ lọc kích thước $K \times K$:
$$\text{Params} = (K \times K \times C_{\text{in}} + 1) \times C_{\text{out}} = K^2 \cdot C_{\text{in}} \cdot C_{\text{out}} + C_{\text{out}}$$

**Giải mã tường minh cấu trúc công thức:**
1. **Một bộ lọc đơn lẻ thực chất là một khối hộp 3D:**
   - Để trượt trên dữ liệu có $C_{\text{in}}$ kênh, bộ lọc bắt buộc phải có độ sâu bằng đúng $C_{\text{in}}$!
   - Kích thước của 1 bộ lọc là: $K \times K \times C_{\text{in}}$ trọng số.
2. **Mỗi bộ lọc có đúng 1 hệ số lệch Bias:**
   - Sau khi nhân tích chập trên toàn bộ $C_{\text{in}}$ kênh và cộng dồn lại, ta cộng thêm đúng $1$ hằng số bias. Do đó trong ngoặc có số $+1$!
3. **Có $C_{\text{out}}$ bộ lọc độc lập:**
   - Nhân toàn bộ với $C_{\text{out}}$ để ra tổng số lượng tham số cần học.

**LƯU Ý VÀNG PHÒNG THI:**
Số lượng tham số của lớp Conv2D **HOÀN TOÀN KHÔNG PHỤ THUỘC VÀO KÍCH THƯỚC ẢNH ĐẦU VÀO ($W_{\text{in}}, H_{\text{in}}$)**! Dù ảnh to $1024 \times 1024$ hay ảnh nhỏ $28 \times 28$, số tham số của lớp Conv vẫn bằng nhau chằn chặn nhờ cơ chế chia sẻ trọng số (Weight Sharing)!

---

**3. Độ phức tạp tính toán FLOPs & MACs (Câu 43 Đề thi VAIO 2025):**
Khi triển khai mô hình AI trên các thiết bị nhúng (điện thoại, drone, xe tự hành), ta phải đo lường năng lực tính toán thông qua:
- **MACs (Multiply-Accumulate Operations - Số phép Nhân và Cộng):**
  - Để tính ra 1 pixel trên 1 bản đồ đặc trưng đầu ra, ta cần thực hiện: $K \times K \times C_{\text{in}}$ phép nhân-cộng.
  - Tổng số pixel trên toàn bộ $C_{\text{out}}$ bản đồ đặc trưng đầu ra là: $H_{\text{out}} \times W_{\text{out}} \times C_{\text{out}}$.
  - Công thức tính MACs:
    $$\text{MACs} = H_{\text{out}} \times W_{\text{out}} \times C_{\text{out}} \times (K \times K \times C_{\text{in}})$$
- **FLOPs (Floating-Point Operations - Số phép tính dấu phẩy động):**
  - Vì 1 phép MAC gồm 1 phép nhân và 1 phép cộng dồn (2 phép toán số học), nên:
    $$\text{FLOPs} \approx 2 \times \text{MACs}$$

---

**4. Bài toán thực tế tính toán chuẩn đề thi:**
*Đề bài:* Cho lớp Conv2D nhận đầu vào $224 \times 224 \times 3$ (ảnh RGB), sử dụng 64 bộ lọc kích thước $3 \times 3$, `padding='same'`, Stride $S = 1$. Hãy tính:
1. Số tham số có thể học (Params)?
2. Kích thước đầu ra và số phép tính MACs?

*Lời giải:*
1. **Số tham số:**
   $$\text{Params} = (3 \times 3 \times 3 + 1) \times 64 = (27 + 1) \times 64 = 28 \times 64 = 1,792 \text{ tham số}.$$
2. **Kích thước đầu ra:**
   Vì `same` và $S = 1$ nên $H_{\text{out}} = W_{\text{out}} = 224$. Đầu ra là tensor $(224, 224, 64)$.
3. **Số phép tính MACs:**
   $$\text{MACs} = 224 \times 224 \times 64 \times (3 \times 3 \times 3) = 3,211,264 \times 27 \approx 86,704,128 \text{ MACs} \approx 86.7 \text{ MMACs}.$$
   $$\text{FLOPs} \approx 2 \times 86.7 \approx 173.4 \text{ MFLOPs}.$$""",
                "formula": r"\text{Params} = (K^2 \cdot C_{\text{in}} + 1) \cdot C_{\text{out}}, \quad \text{MACs} = H_{\text{out}} W_{\text{out}} C_{\text{out}} (K^2 C_{\text{in}}), \quad \text{FLOPs} \approx 2 \times \text{MACs}",
                "mathExplainer": [
                    { "sym": "K^2 \\cdot C_{\\text{in}}", "name": "Kích thước 1 bộ lọc 3D", "mean": "Số lượng trọng số trong 1 bộ lọc tích chập trải trên toàn bộ các kênh đầu vào." },
                    { "sym": "+ 1", "name": "Hệ số Bias", "mean": "Mỗi bộ lọc đầu ra có đúng 1 tham số độ lệch bias độc lập." },
                    { "sym": "C_{\\text{out}}", "name": "Số lượng bộ lọc", "mean": "Mỗi bộ lọc sinh ra 1 bản đồ đặc trưng (Feature Map) ở đầu ra." },
                    { "sym": "\\text{FLOPs}", "name": "Số phép tính dấu phẩy động", "mean": "Thước đo độ nặng tính toán của mô hình, xấp xỉ bằng 2 lần số phép tính MACs." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 660 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="660" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- 3D Filter decomposition -->
                      <g transform="translate(30, 20)">
                        <rect x="0" y="0" width="300" height="140" fill="#fff" stroke="#111" stroke-width="1.2"/>
                        <text x="150" y="20" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Cấu Trúc 1 Bộ Lọc 3D: K × K × C_in</text>
                        <!-- 3 slices representing channels -->
                        <g transform="translate(40, 35)">
                          <rect x="0" y="0" width="50" height="50" fill="#eee" stroke="#111" stroke-width="1"/>
                          <text x="25" y="28" font-family="Georgia" font-size="8" text-anchor="middle">Kênh R</text>
                          <rect x="15" y="15" width="50" height="50" fill="#ddd" stroke="#111" stroke-width="1"/>
                          <text x="40" y="43" font-family="Georgia" font-size="8" text-anchor="middle">Kênh G</text>
                          <rect x="30" y="30" width="50" height="50" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="55" y="58" font-family="Georgia" font-size="8" font-weight="bold" text-anchor="middle">Kênh B</text>
                        </g>
                        <text x="175" y="65" font-family="Georgia" font-size="10" font-weight="bold">Trọng số 1 Filter:</text>
                        <text x="175" y="85" font-family="Georgia" font-size="9">= K × K × C_in</text>
                        <text x="175" y="105" font-family="Georgia" font-size="9">+ 1 Bias</text>
                      </g>
                      <!-- Total params formula -->
                      <g transform="translate(350, 20)">
                        <rect x="0" y="0" width="280" height="140" fill="#111" rx="4"/>
                        <text x="140" y="25" font-family="Georgia" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">Tổng Số Tham Số (Câu 2 VAIO)</text>
                        <text x="140" y="60" font-family="Georgia" font-size="12" fill="#fff" font-weight="bold" text-anchor="middle">Params = (K² · C_in + 1) × C_out</text>
                        <line x1="20" y1="78" x2="260" y2="78" stroke="#555"/>
                        <text x="25" y="98" font-family="Georgia" font-size="9" fill="#ccc">• Trọng số Filter &amp; Bias là tham số học được!</text>
                        <text x="25" y="118" font-family="Georgia" font-size="9" fill="#ccc">• Không phụ thuộc vào kích thước ảnh đầu vào!</text>
                      </g>
                    </svg>""",
                    "caption": "Bóc tách cấu trúc tham số: Mỗi bộ lọc thực chất là một khối hộp 3D có độ sâu bằng đúng C_in. Tổng số tham số gồm toàn bộ trọng số 3D của C_out bộ lọc cộng thêm C_out hệ số bias."
                },
                "commonPitfalls": "Quên số kênh đầu vào C_in khi đếm tham số: Rất nhiều thí sinh chỉ tính K × K + 1 rồi nhân C_out. SAI! Nếu ảnh có 3 kênh (RGB), mỗi bộ lọc phải có 3 lát cắt 2D, do đó bắt buộc phải nhân với C_in (K × K × C_in + 1) × C_out!",
                "practiceQuestion": {
                    "level": "Thông hiểu (Câu 2 Đề Thi VAIO 2025)",
                    "question": "Thành phần nào sau đây là một tham số có thể học (learnable parameter) được tối ưu hóa trong quá trình huấn luyện của một lớp tích chập Conv2D? (Câu 2 Đề thi chính thức VAIO 2025)",
                    "options": [
                        "A. Kích thước chiều cao và chiều rộng của bức ảnh đầu vào",
                        "B. Các giá trị trọng số trong bộ lọc (Filter weights) và hệ số chệch (Bias)",
                        "C. Kích thước bước nhảy (Stride)",
                        "D. Kích thước viền đệm (Padding)"
                    ],
                    "correctIndex": 1,
                    "hint": "Cái gì được khởi tạo ngẫu nhiên và liên tục cập nhật đạo hàm bằng Gradient Descent?",
                    "solution": [
                        "Bước 1: Phân biệt siêu tham số (Hyperparameters): Input size, Kernel size K, Stride S, Padding P do con người thiết lập cố định.",
                        "Bước 2: Tham số học được (Learnable parameters): Trọng số của các bộ lọc (Filter weights) và Biases được cập nhật tự động bằng thuật toán lan truyền ngược Backpropagation.",
                        "Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 11.4: LỚP POOLING, RECEPTIVE FIELD & TIẾN HÓA CNN
            # =================================================================
            {
                "heading": "11.4. Lớp Gom Cụm Pooling, Trường Tiếp Nhận Receptive Field & Sự Tiến Hóa Kiến Trúc CNN",
                "content": "Tìm hiểu cơ chế hoạt động của Max Pooling và Average Pooling; giải mã bản chất 0 tham số học được; khám phá khái niệm Trường tiếp nhận (Receptive Field) và triết lý sử dụng bộ lọc 3x3 của VGG-16.",
                "deepDive": r"""**1. Lớp Gom Cụm (Pooling Layer) & Ý nghĩa thực tiễn:**
Sau khi trích xuất đặc trưng bằng lớp tích chập Conv2D, ta thường đưa qua một lớp **Gom cụm (Pooling)**:
- **Max Pooling (Gom cụm cực đại):**
  - Trượt một cửa sổ nhỏ (thường $2 \times 2$, Stride $S = 2$) qua bản đồ đặc trưng.
  - Tại mỗi vị trí, **CHỈ GIỮ LẠI GIÁ TRỊ LỚN NHẤT** trong 4 ô và vứt bỏ 3 ô còn lại!
  - *Ý nghĩa:* Giá trị lớn nhất đại diện cho sự hiện diện mạnh nhất của đặc trưng trong vùng đó. Bằng cách giữ lại giá trị cực đại, mô hình loại bỏ được các nhiễu nền xung quanh.
- **Average Pooling / Global Average Pooling (GAP):**
  - Lấy giá trị trung bình cộng của các ô trong cửa sổ.
  - **Global Average Pooling (GAP):** Lấy trung bình cộng của toàn bộ bản đồ đặc trưng $H \times W$ thành đúng **1 CON SỐ DUY NHẤT**! Kỹ thuật này thường được dùng ở cuối các mạng hiện đại (như ResNet) để thay thế hoàn toàn các tầng kết nối đầy đủ (Dense) cồng kềnh, giúp giảm hàng chục triệu tham số.

**ĐIỂM SỐNG CÒN TRONG KỲ THI OLYMPIC AI:**
- **Lớp Pooling HOÀN TOÀN KHÔNG CÓ BẤT KỲ THAM SỐ HỌC ĐƯỢC NÀO ($\text{Params} = 0$)!**
  Nó chỉ là một phép toán thống kê cố định (lấy Max hoặc lấy Mean).
- Lớp Max Pooling với cỡ $2 \times 2, S=2$ làm giảm chiều cao và chiều rộng đi một nửa ($H/2, W/2$), làm giảm diện tích và khối lượng tính toán của tầng sau tới **75%**!
- Cung cấp tính **Bất biến dịch chuyển cục bộ (Local Translation Invariance)**: Một nét vẽ hơi xê dịch 1 pixel thì giá trị Max trong ô $2 \times 2$ vẫn không hề thay đổi.

---

**2. Khái niệm Trường Tiếp Nhận (Receptive Field):**
- **Trường tiếp nhận (Receptive Field - RF)** là diện tích vùng pixel trên ảnh gốc ban đầu mà một nơ-ron ở tầng thứ $l$ có thể "nhìn thấy" và chịu ảnh hưởng.
- Tầng đầu tiên với Kernel $3 \times 3$ có $RF = 3 \times 3$.
- Tầng thứ hai với Kernel $3 \times 3$ trượt trên tầng thứ nhất: Mỗi nơ-ron tầng 2 nhìn thấy một vùng $3 \times 3$ của tầng 1, mà mỗi nơ-ron tầng 1 lại nhìn thấy $3 \times 3$ của ảnh gốc $\implies$ Nơ-ron tầng 2 nhìn thấy một vùng **$5 \times 5$ TRÊN ẢNH GỐC**!

---

**3. Bí mật thiết kế thiên tài của VGG-16 (Simonyan & Zisserman, 2014):**
Tại sao từ năm 2014 đến nay, các kiến trúc Deep Learning hầu như chỉ dùng các bộ lọc $3 \times 3$ mà không dùng $5 \times 5$ hay $7 \times 7$?
- VGG nhận ra rằng: **XẾP CHỒNG 2 LỚP CONV $3 \times 3$ HOÀN TOÀN TƯƠNG ĐƯƠNG VỀ TRƯỜNG TIẾP NHẬN VỚI 1 LỚP CONV $5 \times 5$**!
- **Nhưng hãy so sánh chi phí tham số giữa hai cách:**
  - Giả sử số kênh đầu vào và ra đều là $C$:
  - Dùng 1 lớp Conv $5 \times 5$:
    $$\text{Params} = 5 \times 5 \times C \times C = 25 C^2$$
  - Dùng 2 lớp Conv $3 \times 3$ liên tiếp:
    $$\text{Params} = 2 \times (3 \times 3 \times C \times C) = 18 C^2$$
  - **Tiết kiệm tới $28\%$ số lượng tham số!** (Nếu so 3 lớp $3 \times 3$ với 1 lớp $7 \times 7$, ta tiết kiệm tới $45\%$ tham số: $27 C^2$ so với $49 C^2$).
  - Hơn nữa, việc xếp chồng 2 lớp $3 \times 3$ mang lại **2 hàm kích hoạt phi tuyến ReLU** thay vì chỉ 1, giúp mạng học được các hàm toán học phức tạp và biểu diễn trừu tượng hơn rất nhiều!

---

**4. Dòng thời gian tiến hóa của các kiến trúc CNN:**
1. **LeNet-5 (1998 - Yann LeCun):** Kiến trúc CNN đầu tiên, gồm các lớp Conv xen kẽ Subsampling (Average Pooling) để nhận dạng chữ số viết tay trên séc ngân hàng.
2. **AlexNet (2012 - Alex Krizhevsky & Geoffrey Hinton):** Giành chiến thắng áp đảo tại ImageNet 2012, châm ngòi cho cuộc cách mạng Deep Learning. Sử dụng GPU, hàm kích hoạt ReLU và kỹ thuật Dropout.
3. **VGG-16 (2014):** Chuẩn hóa việc sử dụng đồng nhất các bộ lọc nhỏ $3 \times 3$ và Max Pooling $2 \times 2$.
4. **ResNet (2015):** Đột phá kết nối tắt Skip Connection, giải quyết triệt để bài toán suy thoái mạng sâu.""",
                "formula": r"\text{Max Pooling: } y = \max_{i,j \in \text{window}} x_{i,j}, \quad \text{Pooling Params} = 0, \quad 2 \times \text{Conv}(3\times3) \equiv \text{Conv}(5\times5)",
                "mathExplainer": [
                    { "sym": "\\text{Max Pooling}", "name": "Gom cụm cực đại", "mean": "Lấy giá trị lớn nhất trong cửa sổ 2x2, giữ lại tín hiệu nổi bật nhất." },
                    { "sym": "\\text{Params} = 0", "name": "Không có tham số", "mean": "Lớp Pooling hoàn toàn không có trọng số hay bias cần học, chỉ là phép toán cố định." },
                    { "sym": "\\text{Receptive Field}", "name": "Trường tiếp nhận", "mean": "Vùng diện tích trên ảnh gốc mà một nơ-ron tầng sâu có thể bao quát." },
                    { "sym": "18C^2 \\text{ vs } 25C^2", "name": "Tiết kiệm tham số VGG", "mean": "Dùng hai lớp 3x3 tiết kiệm 28% tham số so với một lớp 5x5 mà cùng trường tiếp nhận." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 660 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
                      <rect width="660" height="170" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Left: Max Pooling 2x2 Operation -->
                      <g transform="translate(30, 20)">
                        <rect x="0" y="0" width="280" height="130" fill="#fff" stroke="#111" stroke-width="1.2"/>
                        <text x="140" y="20" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Max Pooling 2×2 (Stride = 2)</text>
                        <!-- 4x4 matrix with 4 colored zones -->
                        <g transform="translate(25, 35)">
                          <rect x="0" y="0" width="40" height="40" fill="#eee" stroke="#111"/>
                          <text x="20" y="25" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">8</text>
                          <rect x="40" y="0" width="40" height="40" fill="#fafafa" stroke="#111"/>
                          <text x="60" y="25" font-family="Georgia" font-size="11" text-anchor="middle">3</text>
                          <rect x="0" y="40" width="40" height="40" fill="#fafafa" stroke="#111"/>
                          <text x="20" y="65" font-family="Georgia" font-size="11" text-anchor="middle">1</text>
                          <rect x="40" y="40" width="40" height="40" fill="#eee" stroke="#111"/>
                          <text x="60" y="65" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">9</text>
                        </g>
                        <text x="140" y="75" font-family="Georgia" font-size="14" font-weight="bold">⇒</text>
                        <g transform="translate(180, 50)">
                          <rect x="0" y="0" width="25" height="25" fill="#111"/>
                          <text x="12" y="17" font-family="Georgia" font-size="11" fill="#fff" font-weight="bold" text-anchor="middle">8</text>
                          <rect x="25" y="0" width="25" height="25" fill="#111"/>
                          <text x="37" y="17" font-family="Georgia" font-size="11" fill="#fff" font-weight="bold" text-anchor="middle">9</text>
                          <text x="25" y="45" font-family="Georgia" font-size="8" fill="#555" text-anchor="middle">Params = 0</text>
                        </g>
                      </g>
                      <!-- Right: 2 Conv 3x3 equals 1 Conv 5x5 -->
                      <g transform="translate(340, 20)">
                        <rect x="0" y="0" width="290" height="130" fill="#fff" stroke="#111" stroke-width="1.2"/>
                        <text x="145" y="20" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Triết Lý 2 Lớp 3×3 Trong VGG-16</text>
                        <text x="20" y="45" font-family="Georgia" font-size="9">• 1 lớp Conv 5×5: Tốn 25·C² tham số</text>
                        <text x="20" y="68" font-family="Georgia" font-size="9">• 2 lớp Conv 3×3: Tốn 18·C² tham số</text>
                        <text x="20" y="90" font-family="Georgia" font-size="9" font-weight="bold">⇒ TIẾT KIỆM 28% SỐ LƯỢNG THAM SỐ!</text>
                        <text x="20" y="112" font-family="Georgia" font-size="9" fill="#555">• Có 2 tầng ReLU tăng cường tính phi tuyến</text>
                      </g>
                    </svg>""",
                    "caption": "Trái: Cơ chế Max Pooling 2x2 (giữ lại giá trị lớn nhất, Params = 0). Phải: Triết lý VGG-16 thay thế 1 lớp 5x5 bằng 2 lớp 3x3 để tiết kiệm 28% tham số và tăng tính phi tuyến."
                },
                "commonPitfalls": "Nhầm lẫn rằng lớp Pooling có tham số học được: Đề thi thường gài bẫy tính tổng số tham số của một khối Conv + MaxPool. Hãy luôn nhớ: Lớp Pooling KHÔNG CÓ BẤT KỲ THAM SỐ NÀO (Params = 0)!",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Trong mạng nơ-ron tích chập, một lớp Max Pooling kích thước 2×2 với bước nhảy Stride S = 2 có bao nhiêu tham số học được (learnable parameters)?",
                    "options": [
                        "A. 4 tham số",
                        "B. 0 tham số",
                        "C. 1 tham số bias",
                        "D. Phụ thuộc vào số kênh của bản đồ đặc trưng"
                    ],
                    "correctIndex": 1,
                    "hint": "Phép toán lấy giá trị lớn nhất max() có cần trọng số kết nối không?",
                    "solution": [
                        "Lớp Max Pooling thực hiện phép toán thống kê cố định: chọn giá trị lớn nhất trong mỗi cửa sổ 2×2.",
                        "Nó hoàn toàn không chứa bất kỳ trọng số (weight) hay hệ số lệch (bias) nào.",
                        "Do đó số lượng tham số học được luôn bằng đúng 0.",
                        "Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 11.5: CẦU VƯỢT RESNET & ĐỐI ĐẦU RESNET VS U-NET
            # =================================================================
            {
                "heading": "11.5. Cầu Vượt Cao Tốc ResNet (He et al., 2015 - Câu 31 VAIO) & Đối Đầu ResNet vs U-Net",
                "content": "Giải mã hiện tượng suy thoái mạng sâu (Degradation Problem); cơ chế toán học của Khối phần dư Residual Block và đường tắt Skip Connection; chứng minh toán học sự bảo toàn gradient và phân biệt đối đầu ResNet vs U-Net.",
                "deepDive": r"""**1. Nghịch lý 'Suy thoái mạng sâu' (The Degradation Problem):**
Vào khoảng năm 2014, các nhà nghiên cứu tin rằng: *'Cứ xếp chồng mạng nơ-ron càng sâu thì độ chính xác sẽ càng cao'*.
Tuy nhiên, khi thử nghiệm thực tế, họ đã vấp phải một nghịch lý chấn động:
- Khi tăng độ sâu của mạng thuần túy (Plain Network) từ 20 tầng lên 56 tầng: **ĐỘ CHÍNH XÁC BỊ TỤT GIẢM NGHIÊM TRỌNG!**
- **Đây KHÔNG PHẢI là hiện tượng Quá khớp (Overfitting)!**
  Bởi vì sai số trên chính tập huấn luyện (Training Error) của mạng 56 tầng cũng cao hơn hẳn mạng 20 tầng!
- **Nguyên nhân cốt lõi:**
  Khi mạng quá sâu, gradient khi lan truyền ngược qua hàng chục tầng phi tuyến bị nhân dồn liên tục, dẫn tới **Tiêu biến Gradient (Vanishing Gradient)** hoặc làm biến dạng bề mặt hàm mất mát, khiến các thuật toán tối ưu hóa (SGD, Adam) hoàn toàn bị tắc nghẽn và không thể tìm được đường dốc xuống!

---

**2. Đột phá ResNet & Khối phần dư (Residual Block - Kaiming He et al., 2015 - Câu 31 VAIO):**
Vào năm 2015, nhóm nghiên cứu của Kaiming He (Microsoft Research) đã đề xuất kiến trúc **ResNet (Residual Network)** đoạt giải Best Paper tại CVPR 2016.
Ý tưởng cốt lõi cực kỳ thanh lịch:
- Thay vì bắt các tầng tích chập phải học trực tiếp một hàm ánh xạ phức tạp $H(x)$, ta hãy để nó học **PHẦN DƯ SAI LỆCH (Residual Mapping)**:
  $$F(x) = H(x) - x$$
- Khi đó, hàm mục tiêu ban đầu trở thành:
  $$H(x) = F(x) + x$$
- **Cơ chế Cầu vượt cao tốc (Skip Connection / Identity Shortcut):**
  Ta tạo một "đường tắt" mang thẳng tín hiệu đầu vào gốc $x$ nhảy cóc qua 2 hoặc 3 tầng Conv, rồi dùng **PHÉP CỘNG TỪNG PHẦN TỬ (Element-wise Addition)** cộng trực tiếp vào đầu ra $F(x)$ của khối:
  $$y = F(x) + x$$

---

**3. Chứng minh toán học: Số 1 kỳ diệu bảo toàn Gradient vĩnh viễn:**
Tại sao phép cộng $F(x) + x$ lại giúp huấn luyện được mạng sâu tới 152 tầng và thậm chí 1,000 tầng mà không bị tiêu biến gradient?
Hãy lấy đạo hàm của hàm mất mát $\mathcal{E}$ theo đầu vào $x$ bằng Quy tắc chuỗi (Chain Rule):
$$\frac{\partial \mathcal{E}}{\partial x} = \frac{\partial \mathcal{E}}{\partial y} \cdot \frac{\partial y}{\partial x} = \frac{\partial \mathcal{E}}{\partial y} \cdot \frac{\partial (F(x) + x)}{\partial x} = \frac{\partial \mathcal{E}}{\partial y} \cdot \left( \frac{\partial F(x)}{\partial x} + 1 \right)$$
Nhân phá ngoặc ra:
$$\frac{\partial \mathcal{E}}{\partial x} = \frac{\partial \mathcal{E}}{\partial y} \cdot \frac{\partial F(x)}{\partial x} + \frac{\partial \mathcal{E}}{\partial y}$$

**HÃY NHÌN VÀO SỐ HẠNG THỨ HAI $\frac{\partial \mathcal{E}}{\partial y}$:**
- Dù cho các tầng tích chập sâu có bị tiêu biến gradient khiến $\frac{\partial F(x)}{\partial x} \approx 0$, thì nhờ có số $+1$, tín hiệu gradient $\frac{\partial \mathcal{E}}{\partial y}$ vẫn được **PHÓNG TRỰC TIẾP $100\%$ VỀ CÁC TẦNG ĐẦU TIÊN** qua chiếc cầu vượt mà không hề bị cản trở hay suy giảm!
- Cầu vượt Skip Connection đóng vai trò như một **Đại lộ cao tốc Gradient (Gradient Superhighway)**, phá vỡ hoàn toàn bức tường tiêu biến gradient trong mạng nơ-ron siêu sâu!

---

**4. TRỌNG TÂM PHÒNG THI: ĐỐI ĐẦU KINH ĐIỂN RESNET VS U-NET:**
Trong các đề thi AI, giám khảo rất thích so sánh cơ chế kết nối tắt giữa **ResNet** và **U-Net**:

| Đặc điểm so sánh | ResNet (Residual Network) | U-Net (Segmentation Network) |
| :--- | :--- | :--- |
| **Bản chất phép toán** | **PHÉP CỘNG TỪNG PHẦN TỬ** (Element-wise Addition: $F(x) + x$) | **PHÉP NỐI THEO CHIỀU KÊNH** (Channel Concatenation: $[F(x), x]$) |
| **Kích thước kênh đầu ra** | **GIỮ NGUYÊN** số lượng kênh ($C$) | **TĂNG GẤP ĐÔI** số lượng kênh ($2C$) |
| **Yêu cầu không gian** | $x$ và $F(x)$ bắt buộc cùng kích thước $(H, W)$ | Nhánh Encoder và Decoder ghép nối cùng $(H, W)$ |
| **Mục đích chính** | Chống tiêu biến gradient để mạng sâu hơn | Truyền chi tiết biên sắc nét từ Encoder sang Decoder |""" ,
                "formula": r"\text{ResNet: } y = F(x) + x, \quad \frac{\partial \mathcal{E}}{\partial x} = \frac{\partial \mathcal{E}}{\partial y} \left( \frac{\partial F(x)}{\partial x} + 1 \right), \quad \text{U-Net: } y = [F(x), x]",
                "mathExplainer": [
                    { "sym": "F(x) + x", "name": "Khối phần dư ResNet", "mean": "Phép cộng từng phần tử giữa đầu vào gốc x và đầu ra của các lớp tích chập F(x)." },
                    { "sym": "+ 1", "name": "Số 1 kỳ diệu trong đạo hàm", "mean": "Bảo đảm gradient luôn có đường truyền trực tiếp về các tầng đầu mà không bị triệt tiêu về 0." },
                    { "sym": "\\text{Addition}", "name": "Phép cộng trong ResNet", "mean": "Cộng từng ô giá trị, số kênh đầu ra giữ nguyên không thay đổi." },
                    { "sym": "\\text{Concatenation}", "name": "Phép nối kênh trong U-Net", "mean": "Ghép các kênh lại với nhau, làm tăng gấp đôi số lượng kênh đặc trưng." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 660 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="660" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Left: ResNet Residual Block -->
                      <g transform="translate(30, 20)">
                        <rect x="0" y="0" width="280" height="140" fill="#fff" stroke="#111" stroke-width="1.2"/>
                        <text x="140" y="20" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">ResNet: Phép Cộng F(x) + x (Câu 31 VAIO)</text>
                        <circle cx="90" cy="40" r="10" fill="#111"/><text x="70" y="44" font-family="Georgia" font-size="10" font-weight="bold">x</text>
                        <!-- Main branch -->
                        <line x1="90" y1="50" x2="90" y2="65" stroke="#111" stroke-width="1.5"/>
                        <rect x="55" y="65" width="70" height="22" fill="#fff" stroke="#111" stroke-width="1.2"/>
                        <text x="90" y="79" font-family="Georgia" font-size="8" text-anchor="middle">Weight + ReLU</text>
                        <line x1="90" y1="87" x2="90" y2="105" stroke="#111" stroke-width="1.5"/>
                        <!-- Addition node -->
                        <circle cx="90" cy="115" r="10" fill="#fff" stroke="#111" stroke-width="2"/>
                        <text x="90" y="120" font-family="Georgia" font-size="14" font-weight="bold" text-anchor="middle">+</text>
                        <!-- Skip shortcut -->
                        <path d="M 100 40 C 160 40 160 115 102 115" fill="none" stroke="#111" stroke-width="2"/>
                        <polygon points="102,112 98,115 102,118" fill="#111"/>
                        <text x="175" y="78" font-family="Georgia" font-size="9" font-weight="bold">Cầu vượt (Skip)</text>
                        <text x="140" y="132" font-family="Georgia" font-size="8" fill="#555" text-anchor="middle">Số kênh giữ nguyên: C</text>
                      </g>
                      <!-- Right: U-Net Skip Connection -->
                      <g transform="translate(340, 20)">
                        <rect x="0" y="0" width="290" height="140" fill="#fff" stroke="#111" stroke-width="1.2"/>
                        <text x="145" y="20" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">U-Net: Phép Nối Kênh [F(x), x]</text>
                        <rect x="30" y="40" width="50" height="30" fill="#eee" stroke="#111"/>
                        <text x="55" y="58" font-family="Georgia" font-size="8" text-anchor="middle">Encoder: C</text>
                        <text x="105" y="58" font-family="Georgia" font-size="12" font-weight="bold">⊕</text>
                        <rect x="130" y="40" width="50" height="30" fill="#ddd" stroke="#111"/>
                        <text x="155" y="58" font-family="Georgia" font-size="8" text-anchor="middle">Decoder: C</text>
                        <text x="195" y="58" font-family="Georgia" font-size="12" font-weight="bold">⇒</text>
                        <rect x="220" y="35" width="50" height="40" fill="#111"/>
                        <text x="245" y="58" font-family="Georgia" font-size="9" fill="#fff" font-weight="bold" text-anchor="middle">2C Kênh</text>
                        <line x1="20" y1="90" x2="270" y2="90" stroke="#ccc"/>
                        <text x="145" y="112" font-family="Georgia" font-size="9" font-weight="bold" text-anchor="middle">Phép ghép nối (Concatenation)</text>
                        <text x="145" y="128" font-family="Georgia" font-size="8" fill="#555" text-anchor="middle">Số kênh đầu ra tăng gấp đôi!</text>
                      </g>
                    </svg>""",
                    "caption": "Đối đầu kiến trúc kinh điển: Khối phần dư ResNet sử dụng Phép cộng từng phần tử (Addition, giữ nguyên kênh) vs Khối U-Net sử dụng Phép ghép nối theo chiều kênh (Concatenation, tăng gấp đôi số kênh)."
                },
                "commonPitfalls": "Nhầm lẫn giữa phép toán của ResNet và U-Net: Rất nhiều học sinh nhầm lẫn rằng ResNet ghép kênh (concat). SAI HOÀN TOÀN! ResNet dùng PHÉP CỘNG ĐẠI SỐ TỪNG PHẦN TỬ F(x) + x. U-Net mới là mô hình dùng phép ghép nối kênh (Concatenation)!",
                "practiceQuestion": {
                    "level": "Thông hiểu (Câu 31 Đề Thi VAIO 2025)",
                    "question": "Trong kiến trúc mạng ResNet, cơ chế kết nối tắt (Skip connection / Residual connection) thực hiện phép toán nào sau đây giữa tín hiệu đầu vào x và đầu ra của các tầng tích chập F(x)? (Câu 31 Đề thi chính thức VAIO 2025)",
                    "options": [
                        "A. Phép nhân ma trận (Matrix Multiplication: F(x) * x)",
                        "B. Phép nối theo chiều kênh (Channel Concatenation: [F(x), x])",
                        "C. Phép cộng từng phần tử (Element-wise Addition: F(x) + x)",
                        "D. Phép tích chập giữa F(x) và x"
                    ],
                    "correctIndex": 2,
                    "hint": "Chính phép toán cộng này đã tạo ra số +1 trong đạo hàm để bảo toàn gradient.",
                    "solution": [
                        "Bước 1: Khối phần dư ResNet học hàm phần dư F(x) = H(x) - x.",
                        "Bước 2: Để khôi phục lại hàm H(x), đầu ra được tính bằng: y = F(x) + x.",
                        "Bước 3: Đây là phép cộng từng phần tử (Element-wise Addition), yêu cầu F(x) và x phải có cùng kích thước không gian và số kênh.",
                        "Đáp án chính xác: C."
                    ]
                }
            },

            # =================================================================
            # MỤC 11.6: NHẬN DIỆN VẬT THỂ, IOU & THUẬT TOÁN NMS
            # =================================================================
            {
                "heading": "11.6. Nhận Diện Vật Thể (Object Detection): Chỉ Số IoU, Thuật Toán NMS (Câu 10 VAIO) & Bài Toán Tính Tay Chuẩn Đề Thi",
                "content": "Phân biệt 4 tác vụ thị giác máy tính cốt lõi; thiết lập công thức tính diện tích giao và hợp IoU; thực hành giải chi tiết từng bước bài toán tính tay thuật toán Triệt tiêu không cực đại NMS mô phỏng chuẩn xác Câu 10 Đề thi Olympic AI.",
                "deepDive": r"""**1. Bốn cấp độ của Thị giác máy tính:**
Trước khi nhận diện vật thể, học sinh cần phân biệt rạch ròi 4 bài toán:
1. **Phân loại ảnh (Image Classification):** Trả lời câu hỏi: *'Bức ảnh này chứa cái gì?'* $\implies$ Đầu ra: 1 nhãn lớp duy nhất (ví dụ: Chó).
2. **Định vị vật thể (Classification + Localization):** Trả lời: *'Vật thể đó nằm ở đâu?'* $\implies$ Đầu ra: Nhãn lớp + 1 hộp bao chữ nhật (Bounding Box) duy nhất.
3. **Nhận diện vật thể (Object Detection):** Trả lời: *'Có những vật thể nào và chúng nằm ở đâu?'* $\implies$ Đầu ra: Tìm và vẽ hộp bao quanh **TẤT CẢ** các vật thể thuộc nhiều lớp khác nhau (ví dụ: 2 con mèo, 1 người, 3 xe hơi).
4. **Phân đoạn ảnh (Semantic / Instance Segmentation):** Gán nhãn lớp cho **TỪNG PIXEL RIÊNG BIỆT** của bức ảnh.

---

**2. Tọa độ Hộp bao & Chỉ số IoU (Intersection over Union):**
Mỗi hộp bao chữ nhật $B$ được xác định bởi tọa độ 2 đỉnh đối diện:
$$B = (x_1, y_1, x_2, y_2)$$
*(Trong đó $(x_1, y_1)$ là góc trên-trái, $(x_2, y_2)$ là góc dưới-phải).*
- Diện tích của hộp bao:
  $$\text{Area}(B) = (x_2 - x_1) \times (y_2 - y_1)$$

**Chỉ số IoU (Intersection over Union - Tỷ lệ Giao trên Hợp):**
$$\text{IoU}(A, B) = \frac{\text{Area}(A \cap B)}{\text{Area}(A \cup B)} = \frac{\text{Area}(A \cap B)}{\text{Area}(A) + \text{Area}(B) - \text{Area}(A \cap B)}$$
- **Cách tính diện tích vùng giao $A \cap B$:**
  - Tọa độ góc trên-trái vùng giao: $x_{\text{inter1}} = \max(x_{1A}, x_{1B}), \quad y_{\text{inter1}} = \max(y_{1A}, y_{1B})$.
  - Tọa độ góc dưới-phải vùng giao: $x_{\text{inter2}} = \min(x_{2A}, x_{2B}), \quad y_{\text{inter2}} = \min(y_{2A}, y_{2B})$.
  - Chiều rộng và chiều cao vùng giao:
    $$w_{\text{inter}} = \max(0, x_{\text{inter2}} - x_{\text{inter1}}), \quad h_{\text{inter}} = \max(0, y_{\text{inter2}} - y_{\text{inter1}})$$
  - $\text{Area}(A \cap B) = w_{\text{inter}} \times h_{\text{inter}}$.
- **Miền giá trị của IoU:** $\text{IoU} \in [0, 1]$.
  - $\text{IoU} = 0$: Hai hộp hoàn toàn không chạm nhau.
  - $\text{IoU} = 1$: Hai hộp trùng khít hoàn hảo từng pixel.
  - Ngưỡng đánh giá chuẩn: Thường coi dự đoán là đúng nếu $\text{IoU} \ge 0.50$.

---

**3. THUẬT TOÁN TRIỆT TIÊU KHÔNG CỰC ĐẠI (NMS - NON-MAXIMUM SUPPRESSION - CÂU 10 VAIO 2025):**
Khi chạy các bộ nhận diện hiện đại như YOLO hay SSD, mạng thường sinh ra hàng trăm hộp bao ứng viên quanh cùng một vật thể. Thuật toán NMS là bước hậu xử lý bắt buộc để dọn sạch các hộp thừa:

**Quy trình 5 bước kinh điển của NMS:**
1. **Bước 1:** Loại bỏ toàn bộ các hộp có điểm tin cậy (Confidence Score) nhỏ hơn ngưỡng phát hiện (ví dụ $< 0.50$).
2. **Bước 2:** Sắp xếp tất cả các hộp còn lại theo điểm tin cậy giảm dần.
3. **Bước 3:** Chọn hộp có điểm tin cậy cao nhất $M$ trong danh sách, đưa vào tập **KẾT QUẢ ĐƯỢC GIỮ LẠI (Kept List)**, và xóa $M$ khỏi danh sách ứng viên.
4. **Bước 4:** Lần lượt tính $\text{IoU}(M, B_i)$ giữa hộp $M$ với tất cả các hộp còn lại $B_i$.
   - Nếu $\text{IoU}(M, B_i) > \text{IoU\_threshold}$ (hai hộp trùng lặp quá nhiều vào cùng 1 vật thể): **LẬP TỨC LOẠI BỎ (Triệt tiêu)** hộp $B_i$!
5. **Bước 5:** Lặp lại Bước 3 và 4 cho các hộp chưa bị loại cho đến khi danh sách ứng viên rỗng.

---

**4. BÀI TOÁN TÍNH TAY MÔ PHỎNG CHUẨN XÁC CÂU 10 ĐỀ THI VAIO 2025:**
*Đề bài:* Áp dụng thuật toán Non-Maximum Suppression (NMS) với ngưỡng $\text{IoU\_threshold} = 0.40$ cho 3 hộp bao ứng viên sau:
- Hộp $B_1$: Tọa độ $(0, 0, 100, 100)$, điểm tin cậy $c_1 = 0.95$.
- Hộp $B_2$: Tọa độ $(10, 10, 90, 90)$, điểm tin cậy $c_2 = 0.90$.
- Hộp $B_3$: Tọa độ $(105, 105, 200, 200)$, điểm tin cậy $c_3 = 0.85$.
Hỏi: Những hộp bao nào sẽ được giữ lại cuối cùng?

*Lời giải chi tiết từng bước:*
- **Bước 1: Sắp xếp theo điểm tin cậy giảm dần:**
  Thứ tự ưu tiên: $B_1 (0.95) \longrightarrow B_2 (0.90) \longrightarrow B_3 (0.85)$.
- **Bước 2: Xét vòng lặp 1:**
  - Hộp $B_1$ có điểm cao nhất ($0.95$) $\implies$ **GIỮ $B_1$** vào danh sách kết quả!
  - Tính diện tích $B_1$: $\text{Area}(B_1) = (100 - 0) \times (100 - 0) = 100 \times 100 = 10,000$.
- **Bước 3: So sánh $B_2$ với $B_1$:**
  - Diện tích $B_2$: $\text{Area}(B_2) = (90 - 10) \times (90 - 10) = 80 \times 80 = 6,400$.
  - Tọa độ vùng giao:
    $x \in [\max(0, 10), \min(100, 90)] = [10, 90] \implies \text{chiều rộng} = 80$.
    $y \in [\max(0, 10), \min(100, 90)] = [10, 90] \implies \text{chiều cao} = 80$.
  - Diện tích giao: $\text{Area}(B_1 \cap B_2) = 80 \times 80 = 6,400$. (Toàn bộ hộp $B_2$ nằm trọn vẹn bên trong $B_1$!).
  - Diện tích hợp: $\text{Area}(B_1 \cup B_2) = 10,000 + 6,400 - 6,400 = 10,000$.
  - Tính IoU:
    $$\text{IoU}(B_1, B_2) = \frac{6,400}{10,000} = 0.64$$
  - So sánh với ngưỡng: Vì $0.64 > 0.40$ (ngưỡng đề bài), hộp $B_2$ bị trùng lặp quá mức với $B_1$ $\implies$ **LOẠI BỎ $B_2$**!
- **Bước 4: So sánh $B_3$ với $B_1$:**
  - Tọa độ $B_1$: $x \in [0, 100], y \in [0, 100]$.
  - Tọa độ $B_3$: $x \in [105, 200], y \in [105, 200]$.
  - Vì $100 < 105$, hai hộp hoàn toàn cách biệt và không chạm nhau! Vùng giao $= 0$.
  - $\text{IoU}(B_1, B_3) = 0$.
  - So sánh với ngưỡng: Vì $0 \le 0.40$, hộp $B_3$ không bị trùng lặp với $B_1$ $\implies$ **GIỮ $B_3$**!
- **Kết quả cuối cùng:** Tập hợp các hộp được giữ lại là **$B_1$ và $B_3$** (Đáp án C - Câu 10 Đề thi chính thức VAIO 2025)!""" ,
                "formula": r"\text{IoU}(A, B) = \frac{\text{Area}(A \cap B)}{\text{Area}(A) + \text{Area}(B) - \text{Area}(A \cap B)}, \quad \text{NMS: Loại } B_i \text{ nếu } \text{IoU}(M, B_i) > \tau",
                "mathExplainer": [
                    { "sym": "\\text{Area}(A \\cap B)", "name": "Diện tích vùng giao", "mean": "Phần diện tích chung mà cả hai hộp bao cùng bao phủ." },
                    { "sym": "\\text{Area}(A \\cup B)", "name": "Diện tích vùng hợp", "mean": "Tổng diện tích của cả hai hộp trừ đi phần giao trùng nhau để tránh tính 2 lần." },
                    { "sym": "\\text{IoU} \\in [0, 1]", "name": "Chỉ số trùng khít", "mean": "Thước đo mức độ đè lên nhau giữa hai khung hình chữ nhật." },
                    { "sym": "\\tau = 0.40", "name": "Ngưỡng NMS", "mean": "Ngưỡng quyết định: Nếu độ trùng lặp lớn hơn 0.40 thì hộp điểm thấp hơn sẽ bị xóa." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 660 190" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">
                      <rect width="660" height="190" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <!-- Left: Before NMS -->
                      <g transform="translate(30, 20)">
                        <rect x="0" y="0" width="280" height="150" fill="#fff" stroke="#111" stroke-width="1.2"/>
                        <text x="140" y="20" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Trước NMS: 3 Hộp Ban Đầu</text>
                        <!-- B1 -->
                        <rect x="25" y="35" width="80" height="80" fill="none" stroke="#111" stroke-width="2"/>
                        <text x="30" y="50" font-family="Georgia" font-size="9" font-weight="bold">B₁ (0.95)</text>
                        <!-- B2 inside B1 -->
                        <rect x="33" y="43" width="64" height="64" fill="none" stroke="#888" stroke-dasharray="3,3" stroke-width="1.5"/>
                        <text x="38" y="65" font-family="Georgia" font-size="8" fill="#555">B₂ (0.90)</text>
                        <!-- B3 separated -->
                        <rect x="145" y="45" width="76" height="76" fill="none" stroke="#111" stroke-width="2"/>
                        <text x="150" y="60" font-family="Georgia" font-size="9" font-weight="bold">B₃ (0.85)</text>
                        <text x="140" y="135" font-family="Georgia" font-size="8" fill="#555" text-anchor="middle">B₂ nằm trong B₁ ⇒ IoU = 0.64 &gt; 0.40</text>
                      </g>
                      <!-- Arrow -->
                      <text x="325" y="95" font-family="Georgia" font-size="20" font-weight="bold" text-anchor="middle">⇒</text>
                      <!-- Right: After NMS -->
                      <g transform="translate(350, 20)">
                        <rect x="0" y="0" width="280" height="150" fill="#fff" stroke="#111" stroke-width="1.2"/>
                        <text x="140" y="20" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Sau NMS: Kết Quả (Câu 10 VAIO)</text>
                        <!-- B1 kept -->
                        <rect x="25" y="35" width="80" height="80" fill="#eee" stroke="#111" stroke-width="2.5"/>
                        <text x="30" y="50" font-family="Georgia" font-size="10" font-weight="bold">GIỮ B₁ (0.95)</text>
                        <text x="30" y="70" font-family="Georgia" font-size="8" fill="#555">Hộp tối ưu vật thể 1</text>
                        <!-- B2 crossed out -->
                        <text x="30" y="100" font-family="Georgia" font-size="8" fill="#888">✗ Loại B₂ (IoU=0.64)</text>
                        <!-- B3 kept -->
                        <rect x="145" y="45" width="76" height="76" fill="#eee" stroke="#111" stroke-width="2.5"/>
                        <text x="150" y="60" font-family="Georgia" font-size="10" font-weight="bold">GIỮ B₃ (0.85)</text>
                        <text x="150" y="80" font-family="Georgia" font-size="8" fill="#555">Vật thể 2 riêng biệt</text>
                        <text x="140" y="138" font-family="Georgia" font-size="9" font-weight="bold" text-anchor="middle">KẾT QUẢ: GIỮ B₁ VÀ B₃!</text>
                      </g>
                    </svg>""",
                    "caption": "Mô phỏng trực quan bài toán Câu 10 Đề thi VAIO 2025: B2 nằm lọt trong B1 có IoU = 0.64 > 0.40 nên bị loại; B3 tách rời độc lập (IoU = 0) nên được giữ lại cùng B1."
                },
                "commonPitfalls": "Bẫy tính diện tích hợp trong IoU: Khi tính mẫu số Area(A ∪ B), rất nhiều học sinh chỉ lấy Area(A) + Area(B). SAI! Bắt buộc phải TRỪ ĐI diện tích phần giao Area(A ∩ B) để tránh việc phần diện tích chung bị cộng lặp 2 lần!",
                "practiceQuestion": {
                    "level": "Nâng cao (Câu 10 Đề Thi Chính Thức VAIO 2025)",
                    "question": "Áp dụng thuật toán Non-Maximum Suppression (NMS) với ngưỡng IoU_threshold = 0.40 cho 3 hộp bao: B1 (0, 0, 100, 100, conf=0.95); B2 (10, 10, 90, 90, conf=0.90); B3 (105, 105, 200, 200, conf=0.85). Những hộp nào sẽ được giữ lại? (Câu 10 Đề thi chính thức VAIO 2025)",
                    "options": [
                        "A. B1 và B2",
                        "B. Chỉ duy nhất B1",
                        "C. B1 và B3",
                        "D. B2 và B3"
                    ],
                    "correctIndex": 2,
                    "hint": "B1 có conf cao nhất được giữ. B2 nằm trong B1 có IoU = 0.64 > 0.40 nên bị triệt tiêu. B3 không chạm B1 nên được giữ.",
                    "solution": [
                        "Bước 1: B1 có confidence = 0.95 cao nhất trong danh sách => Giữ lại B1.",
                        "Bước 2: Tính IoU giữa B2 và B1: Diện tích B1 = 10000, Diện tích B2 = 6400. Toàn bộ B2 nằm trong B1 nên Giao = 6400, Hợp = 10000. IoU = 6400 / 10000 = 0.64.",
                        "Bước 3: Vì IoU = 0.64 > 0.40 (ngưỡng NMS) => Loại bỏ B2.",
                        "Bước 4: So sánh B3 và B1: B3 bắt đầu từ tọa độ x=105, hoàn toàn không giao với B1 (kết thúc tại x=100). IoU = 0 <= 0.40 => Giữ lại B3.",
                        "Kết quả cuối cùng: Giữ lại B1 và B3. Đáp án chính xác: C."
                    ]
                }
            }
        ],
        "interactiveWidget": "widget-cnn-calculator",
        "examConnection": {
            "questionTitle": "Tổng Hợp Ma Trận Câu Hỏi Thị Giác Máy Tính Đề Thi Olympic AI (VAIO 2025)",
            "items": [
                {
                    "code": "Câu 2 VAIO",
                    "problem": "Thành phần nào là tham số có thể học (learnable parameter) trong Conv2D? (Đáp án B: Trọng số bộ lọc Filter weights và Biases).",
                    "solution": [
                        "Kích thước ảnh, Kernel, Stride, Padding là siêu tham số do con người đặt trước."
                    ]
                },
                {
                    "code": "Câu 10 VAIO",
                    "problem": "Thuật toán NMS với ngưỡng IoU = 0.40 loại bỏ hộp bao B2 và giữ lại B1, B3 (Đáp án C).",
                    "solution": [
                        "B2 có IoU = 0.64 > 0.40 so với B1 nên bị loại; B3 tách rời hoàn toàn nên được giữ lại."
                    ]
                },
                {
                    "code": "Câu 27 & 35 VAIO",
                    "problem": "Công thức kích thước đầu ra Conv2D: W_out = floor((W_in - K + 2P)/S) + 1. Khi padding='same', W_out = ceil(W_in / S).",
                    "solution": [
                        "Áp dụng tính nhẩm nhanh chính xác trong phòng thi."
                    ]
                },
                {
                    "code": "Câu 31 VAIO",
                    "problem": "Cơ chế Skip Connection trong ResNet sử dụng phép cộng từng phần tử F(x) + x (Đáp án C).",
                    "solution": [
                        "Khác với U-Net dùng phép nối theo chiều kênh (Concatenation)."
                    ]
                },
                {
                    "code": "Câu 43 VAIO",
                    "problem": "Tính toán số tham số Params = (K^2 * C_in + 1) * C_out và số phép tính MACs = H_out * W_out * C_out * (K^2 * C_in).",
                    "solution": [
                        "Mỗi bộ lọc 3D có độ sâu C_in và 1 bias riêng."
                    ]
                }
            ]
        },
        "takeaways": [
            "CNN khắc phục triệt để bùng nổ tham số và mất cấu trúc không gian của MLP nhờ cơ chế Chia sẻ trọng số (Weight Sharing) và Vùng tiếp nhận cục bộ.",
            "Công thức kích thước đầu ra Conv2D: W_out = floor((W_in - K + 2P) / S) + 1. Với padding='same': W_out = ceil(W_in / S).",
            "Tổng số tham số học được của 1 lớp Conv2D: Params = (K^2 * C_in + 1) * C_out. Lớp Pooling HOÀN TOÀN KHÔNG CÓ THAM SỐ (Params = 0).",
            "ResNet giải quyết hiện tượng suy thoái mạng sâu bằng Cầu vượt Skip Connection với PHÉP CỘNG TỪNG PHẦN TỬ F(x) + x, tạo ra số +1 trong đạo hàm bảo toàn gradient.",
            "Trong Nhận diện vật thể, thuật toán NMS sắp xếp theo Confidence Score, giữ hộp cao nhất và loại bỏ các hộp có IoU > threshold."
        ]
    }
