# -*- coding: utf-8 -*-
"""
upgrade_lesson_9.py - Masterpiece Lesson 9 for VAIO 2025 AI Olympiad
Chủ đề: Phân Cụm K-Means & Giảm Chiều Dữ Liệu PCA
Toàn diện từ con số 0 đến làm chủ sâu sắc.

Tuân thủ nghiêm ngặt chuẩn sư phạm:
Trực giác đời sống -> Bản chất toán học -> Cách thức hoạt động ->
Giải mã ký hiệu cho học sinh lớp 12 -> Ví dụ tính toán bằng số từng bước ->
Cạm bẫy phòng thi -> Câu hỏi trắc nghiệm kiểm tra độ hiểu có lời giải chi tiết.
"""

def get_masterpiece_lesson_9():
    return {
        "id": "lesson-9",
        "title": "9. Phân Cụm K-Means & Giảm Chiều Dữ Liệu PCA",
        "syllabusBadge": "BUỔI 7: HỌC KHÔNG GIÁM SÁT: K-MEANS & PCA",
        "summary": "Khám phá thế giới Học Không Giám Sát (Unsupervised Learning): Tự động khai phá cấu trúc tiềm ẩn khi không có nhãn đúng. Nắm vững thuật toán phân cụm K-Means, hàm mục tiêu WCSS, khởi tạo thông minh K-Means++, hai thước đo chọn K tối ưu (Phương pháp khuỷu tay Elbow và Hệ số Silhouette [-1, 1]); làm chủ kỹ thuật giảm chiều kinh điển PCA: Khử tâm, ma trận hiệp phương sai, vector riêng (trục thành phần chính) và trị riêng (phương sai bảo toàn), đọc biểu đồ Scree Plot và nhận diện giới hạn phi tuyến.",
        "intuition": {
            "title": "Trực giác thực tế: Chiếu bóng chiếc ấm trà 3D lên bức tường 2D và Phân loại rổ đậu 1,000 hạt",
            "content": """Hãy tưởng tượng bạn đang cầm trên tay một chiếc ấm pha trà bằng gốm tinh xảo trong không gian 3 chiều và trong phòng có một ngọn đèn chiếu bóng lên bức tường phẳng 2 chiều:
- Nếu bạn chiếu bóng từ trên thẳng xuống: Chiếc ấm chỉ in lên tường một hình tròn xoe đặc xịt. Bạn đã làm mất sạch hình dáng cái vòi ấm và cái quai ấm! Bất kỳ ai nhìn vào bóng cũng không thể nhận ra đó là một chiếc ấm trà (bạn vừa làm mất gần như toàn bộ thông tin quan trọng)!
- Nhưng nếu bạn khéo léo xoay chiếc ấm sao cho góc nghiêng của nó in lên tường rõ nhất cả thân ấm, vòi ấm nhô sang bên trái và quai ấm uốn cong sang bên phải: Bất kỳ ai nhìn vào bóng 2D cũng thốt lên ngay: 'Đó là một chiếc ấm trà!'.

Đó chính là nguyên lý tối thượng của **PCA (Principal Component Analysis - Phân tích Thành phần Chính)**:
Tìm ra những góc 'chiếu bóng' tối ưu nhất trong không gian đa chiều sao cho **ĐỘ PHÂN TÁN (PHƯƠNG SAI) CỦA DỮ LIỆU ĐƯỢC GIỮ LẠI LỚN NHẤT**, giúp nén dữ liệu từ 100 chiều xuống 2 hoặc 3 chiều để vẽ đồ thị mà hầu như không làm mất mát thông tin cốt lõi!

Còn với **K-Means Clustering (Phân cụm K-Means)**:
Giống như bạn được giao một rổ gồm 1,000 hạt đậu đủ kích cỡ mà không hề có nhãn dán tên. Bạn muốn tự động chia rổ đậu thành 3 bát (Đậu nhỏ, Đậu vừa, Đậu to) dựa hoàn toàn vào khoảng cách kích thước tự nhiên giữa các hạt đậu. K-Means sẽ tự động tìm ra 3 hạt đậu 'đại diện' làm tâm, và từng hạt đậu sẽ tự giác lăn về chiếc bát có tâm gần nó nhất!"""
        },
        "sections": [
            # =================================================================
            # MỤC 9.1: BẢN CHẤT HỌC KHÔNG GIÁM SÁT & VŨ ĐIỆU K-MEANS
            # =================================================================
            {
                "heading": "9.1. Khởi Đầu Từ Con Số 0: Học Không Giám Sát Là Gì? Vũ Điệu Của Các Trọng Tâm K-Means & Hàm Mục Tiêu WCSS",
                "content": "Trong Học Không Giám Sát (Unsupervised Learning), ta chỉ có ma trận đặc trưng X mà hoàn toàn không có nhãn đúng y. Thuật toán phải tự thân vận động tìm ra các nhóm điểm có tính chất tương đồng.",
                "deepDive": r"""**1. Phân biệt Học Có Giám Sát vs Học Không Giám Sát:**
- **Học Có Giám Sát (Supervised Learning):** Dữ liệu có dạng $(x_i, y_i)$. Giống như học sinh học bài có sách giải mẫu bên cạnh. Mô hình so sánh dự đoán $\hat{y}$ với đáp án đúng $y$ để sửa sai.
- **Học Không Giám Sát (Unsupervised Learning):** Dữ liệu chỉ có $x_i$, **hoàn toàn không có nhãn $y$**! Máy tính giống như một nhà thám hiểm bước vào hòn đảo lạ, phải tự quan sát, đo đạc và nhóm các sinh vật có đặc điểm tương đồng vào các loài khác nhau.

**2. Vũ điệu 2 bước luân phiên của thuật toán K-Means (Lloyd's Algorithm):**
Mục tiêu là chia $N$ điểm dữ liệu thành $K$ cụm (Clusters) riêng biệt $C_1, C_2, \dots, C_K$.
Mỗi cụm được đại diện bởi một tọa độ trung tâm gọi là **Trọng tâm cụm (Centroid)** $\mu_k$.

Thuật toán hoạt động theo vòng lặp 2 bước nhịp nhàng:
- **Bước 1: Gán cụm (Assignment Step):**
  Mỗi điểm dữ liệu $x_i$ đo khoảng cách Euclid tới tất cả $K$ tâm cụm, và gia nhập vào cụm có tâm **GẦN NÓ NHẤT**:
  $$c_i = \arg\min_{k \in \{1, \dots, K\}} \|x_i - \mu_k\|^2$$
- **Bước 2: Cập nhật tâm cụm (Update Step):**
  Sau khi các điểm đã ổn định vị trí trong cụm, tâm cụm $\mu_k$ di chuyển về **TỌA ĐỘ TRUNG BÌNH CỘNG (MEAN)** của tất cả các thành viên trong cụm đó:
  $$\mu_k = \frac{1}{|C_k|} \sum_{x \in C_k} x$$
  *(Chính vì lấy giá trị trung bình Mean của K cụm nên thuật toán mới có tên là K-Means!).*
- **Điểm dừng (Convergence):**
  Lặp lại liên tục Bước 1 và Bước 2 cho đến khi các tâm cụm không còn di chuyển nữa (hoặc sự thay đổi nhỏ hơn ngưỡng sai số $\epsilon$).

**3. Hàm mục tiêu WCSS (Within-Cluster Sum of Squares) / Quán tính (Inertia):**
K-Means không chạy hú họa mà thực chất đang tối ưu hóa một hàm mục tiêu toán học rõ ràng:
$$\mathcal{J}_{\text{WCSS}} = \sum_{k=1}^K \sum_{x \in C_k} \|x - \mu_k\|^2$$
- **Ý nghĩa:** WCSS đo lường **Tổng bình phương khoảng cách** từ mỗi điểm dữ liệu đến tâm cụm của nó.
- WCSS đại diện cho **Độ chặt chẽ nội cụm (Cohesion)**: WCSS càng nhỏ chứng tỏ các cụm càng co cụm đặc quánh, các thành viên càng gần gũi với tâm cụm.
- **Định lý hội tụ:** Thuật toán Lloyd đảm bảo rằng sau mỗi bước gán và cập nhật, giá trị WCSS luôn **giảm đơn điệu hoặc giữ nguyên**, không bao giờ tăng!""",
                "formula": r"\mathcal{J}_{\text{WCSS}} = \sum_{k=1}^K \sum_{x \in C_k} \|x - \mu_k\|^2, \quad \mu_k = \frac{1}{|C_k|} \sum_{x \in C_k} x",
                "mathExplainer": [
                    { "sym": "K", "name": "Số lượng cụm", "mean": "Siêu tham số do con người cài đặt trước, xác định số nhóm cần phân chia." },
                    { "sym": "\\mu_k (Mu)", "name": "Tâm cụm (Centroid)", "mean": "Tọa độ trung bình cộng của tất cả các điểm dữ liệu thuộc cụm k." },
                    { "sym": "C_k", "name": "Cụm thứ k", "mean": "Tập hợp các điểm dữ liệu được gán về tâm cụm mu_k." },
                    { "sym": "\\mathcal{J}_{\\text{WCSS}}", "name": "Tổng bình phương nội cụm", "mean": "Thước đo độ nén chặt của các cụm (càng nhỏ cụm càng đặc quánh)." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 190" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="190" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(20, 20)">
                        <!-- Step 1: Init -->
                        <g transform="translate(10, 10)">
                          <rect x="0" y="0" width="180" height="140" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="90" y="20" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">1. Chọn K tâm ngẫu nhiên</text>
                          <circle cx="40" cy="50" r="4" fill="#888"/><circle cx="55" cy="70" r="4" fill="#888"/><circle cx="35" cy="85" r="4" fill="#888"/>
                          <circle cx="130" cy="65" r="4" fill="#888"/><circle cx="145" cy="85" r="4" fill="#888"/><circle cx="120" cy="100" r="4" fill="#888"/>
                          <!-- Centroids as crosses -->
                          <polygon points="50,45 54,53 46,53" fill="#111"/>
                          <text x="60" y="52" font-family="Georgia" font-size="9" font-weight="bold">μ₁</text>
                          <polygon points="120,80 124,88 116,88" fill="#111"/>
                          <text x="130" y="87" font-family="Georgia" font-size="9" font-weight="bold">μ₂</text>
                        </g>

                        <!-- Step 2: Assign -->
                        <g transform="translate(210, 10)">
                          <rect x="0" y="0" width="180" height="140" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="90" y="20" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">2. Gán điểm về tâm gần nhất</text>
                          <!-- Cluster 1 points (black) -->
                          <circle cx="40" cy="50" r="4" fill="#111"/><circle cx="55" cy="70" r="4" fill="#111"/><circle cx="35" cy="85" r="4" fill="#111"/>
                          <!-- Cluster 2 points (white stroke) -->
                          <circle cx="130" cy="65" r="4" fill="#fff" stroke="#111" stroke-width="2"/>
                          <circle cx="145" cy="85" r="4" fill="#fff" stroke="#111" stroke-width="2"/>
                          <circle cx="120" cy="100" r="4" fill="#fff" stroke="#111" stroke-width="2"/>
                          <!-- Boundary line -->
                          <line x1="90" y1="35" x2="90" y2="125" stroke="#888" stroke-dasharray="3,3"/>
                          <text x="90" y="135" font-family="Georgia" font-size="8" fill="#555" text-anchor="middle">Ranh giới Voronoi</text>
                        </g>

                        <!-- Step 3: Update -->
                        <g transform="translate(410, 10)">
                          <rect x="0" y="0" width="190" height="140" fill="#111"/>
                          <text x="95" y="20" font-family="Georgia" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">3. Dịch tâm về trọng tâm Mean</text>
                          <circle cx="40" cy="50" r="4" fill="#fff"/><circle cx="55" cy="70" r="4" fill="#fff"/><circle cx="35" cy="85" r="4" fill="#fff"/>
                          <circle cx="130" cy="65" r="4" fill="#888"/><circle cx="145" cy="85" r="4" fill="#888"/><circle cx="120" cy="100" r="4" fill="#888"/>
                          <!-- Updated Centroids -->
                          <circle cx="43" cy="68" r="6" fill="none" stroke="#fff" stroke-width="2"/>
                          <text x="55" y="72" font-family="Georgia" font-size="9" fill="#fff" font-weight="bold">μ₁ mới</text>
                          <circle cx="132" cy="83" r="6" fill="none" stroke="#fff" stroke-width="2"/>
                          <text x="144" y="87" font-family="Georgia" font-size="9" fill="#fff" font-weight="bold">μ₂ mới</text>
                          <text x="95" y="130" font-family="Georgia" font-size="9" fill="#ccc" text-anchor="middle">Lặp lại đến khi hội tụ!</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "Chu trình 3 bước lặp K-Means: Khởi tạo tâm -> Gán điểm theo khoảng cách Euclid nhỏ nhất -> Cập nhật tâm bằng trung bình cộng tọa độ (Mean)."
                },
                "commonPitfalls": "Nhầm lẫn giữa K-Means và k-NN: Rất nhiều thí sinh nhầm lẫn hai thuật toán này vì đều có chữ 'k'! Nhớ kỹ: K-Means là HỌC KHÔNG GIÁM SÁT (K là số cụm cần gom, không có nhãn đúng); k-NN là HỌC CÓ GIÁM SÁT (k là số láng giềng biểu quyết, có nhãn lớp cụ thể)!",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Trong thuật toán K-Means, tại bước Cập nhật tâm (Update Step), vị trí mới của tâm cụm μ_k được xác định bằng công thức toán học nào sau đây?",
                    "options": [
                        "A. Trung vị (Median) tọa độ của các điểm trong cụm k",
                        "B. Trung bình cộng (Mean) tọa độ của tất cả các điểm dữ liệu thuộc cụm k",
                        "C. Điểm dữ liệu có khoảng cách xa nhất tới các cụm khác",
                        "D. Điểm ngẫu nhiên được rút thăm lại từ tập dữ liệu ban đầu"
                    ],
                    "correctIndex": 1,
                    "hint": "Cái tên 'K-Means' xuất phát từ chính phép tính thống kê trung bình cộng (Mean) này.",
                    "solution": [
                        "Bước 1: Phân tích tên gọi K-Means: K đại diện cho số cụm, Means đại diện cho giá trị trung bình cộng.",
                        "Bước 2: Trong bước cập nhật tâm, tâm cụm mới μ_k được tính bằng tổng vector tọa độ của tất cả các điểm thuộc cụm k chia cho số lượng phần tử của cụm đó: μ_k = (1 / |C_k|) * sum(x_i).",
                        "Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 9.2: THUẬT TOÁN K-MEANS++ & BÍ QUYẾT KHỞI TẠO TÂM
            # =================================================================
            {
                "heading": "9.2. Gót Chân Achilles Của K-Means & Vũ Khí Khởi Tạo Thông Minh K-Means++",
                "content": "K-Means truyền thống rất dễ rơi vào bẫy cực tiểu địa phương nghèo nàn nếu chọn nhầm các tâm cụm ban đầu quá gần nhau. Thuật toán K-Means++ ra đời như một giải pháp cứu rỗi bằng cơ chế xác suất tỷ lệ thuận với bình phương khoảng cách.",
                "deepDive": r"""**1. Gót chân Achilles của K-Means truyền thống: Sự phụ thuộc vào khởi tạo:**
Hàm mục tiêu WCSS là một hàm **Phi lồi (Non-convex)** có vô số điểm cực tiểu địa phương (Local Minima):
- Nếu bạn chọn $K$ tâm ban đầu một cách hú họa:
  - Rất có thể 2 hoặc 3 tâm cụm ban đầu cùng rơi vào một đám mây điểm duy nhất!
  - Kết quả: Cụm tự nhiên đó bị chia cắt thành 2 nửa nhân tạo, trong khi một cụm dữ liệu tách biệt khác ở xa lại bị gộp chung hoặc bị bỏ sót!
  - Thuật toán K-Means truyền thống sẽ bị mắc kẹt tại nghiệm tồi tệ này mà không thể tự thoát ra được.

**2. Thuật toán K-Means++ (David Arthur & Sergei Vassilvitskii, 2007 - Câu 18 VAIO):**
Ý tưởng cốt lõi cực kỳ trực quan: **Các tâm cụm ban đầu phải nằm CÀNG XA NHAU CÀNG TỐT**!

**Quy trình 4 bước của K-Means++:**
1. **Bước 1:** Chọn ngẫu nhiên tâm cụm đầu tiên $\mu_1$ từ tập dữ liệu theo phân phối đều.
2. **Bước 2:** Với mỗi điểm dữ liệu $x$, tính khoảng cách ngắn nhất từ nó tới các tâm cụm đã chọn trước đó:
   $$D(x) = \min_{j \in \{1, \dots, m\}} \|x - \mu_j\|$$
3. **Bước 3:** Chọn tâm cụm tiếp theo $\mu_{m+1}$ theo phân phối xác suất tỷ lệ thuận với **BÌNH PHƯƠNG KHOẢNG CÁCH $D(x)^2$**:
   $$P(x) = \frac{D(x)^2}{\sum_{x' \in X} D(x')^2}$$
4. **Bước 4:** Lặp lại Bước 2 và Bước 3 cho đến khi chọn đủ $K$ tâm cụm ban đầu!

**3. Tại sao lại dùng xác suất $P(x) \propto D(x)^2$ mà không chọn luôn điểm xa nhất?**
- Nếu chọn điểm có $D(x)$ xa nhất tuyệt đối (Deterministic): Thuật toán sẽ ngay lập tức bốc phải các điểm nhiễu dị biệt (Outliers) nằm lạc lõng ở góc không gian!
- Bằng cách dùng phân phối xác suất:
  - Những điểm nằm càng xa các tâm cũ sẽ có xác suất được chọn rất cao.
  - Những điểm nằm sát sạt các tâm cũ sẽ có xác suất chọn gần bằng 0!
  - Vẫn giữ được tính ngẫu nhiên an toàn trước các điểm Outliers đơn lẻ.

**4. Hiệu quả vượt bậc:**
K-Means++ đã được chứng minh bằng toán học giúp thuật toán đạt chất lượng nghiệm xấp xỉ $\mathcal{O}(\log K)$-competitive so với nghiệm tối ưu toàn cục, tăng tốc độ hội tụ gấp đôi và trở thành **tiêu chuẩn mặc định trong Scikit-Learn** (`init='k-means++'`).""",
                "formula": r"P(x) = \frac{D(x)^2}{\sum_{x' \in X} D(x')^2}, \quad D(x) = \min_{j=1}^m \|x - \mu_j\|",
                "mathExplainer": [
                    { "sym": "D(x)", "name": "Khoảng cách tới tâm gần nhất", "mean": "Khoảng cách từ mẫu x tới tâm cụm gần nó nhất trong số các tâm đã được chọn." },
                    { "sym": "P(x)", "name": "Xác suất được chọn làm tâm mới", "mean": "Tỷ lệ xác suất để điểm x trở thành tâm tiếp theo, tỷ lệ thuận với D(x)²." },
                    { "sym": "\\mathcal{O}(\\log K)", "name": "Giới hạn xấp xỉ lý thuyết", "mean": "Độ đảm bảo toán học của Arthur & Vassilvitskii chứng minh K-Means++ vượt trội hoàn toàn so với khởi tạo ngẫu nhiên." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 20)">
                        <text x="280" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">CƠ CHẾ CHỌN TÂM XÁC SUẤT TRONG K-MEANS++</text>

                        <!-- First centroid mu_1 -->
                        <circle cx="100" cy="90" r="12" fill="#111"/>
                        <text x="100" y="94" font-family="Georgia" font-size="10" fill="#fff" font-weight="bold" text-anchor="middle">μ₁</text>
                        <text x="100" y="125" font-family="Georgia" font-size="9" text-anchor="middle">Tâm 1 (Chọn ngẫu nhiên)</text>

                        <!-- Near points (small D -> low prob) -->
                        <circle cx="130" cy="80" r="5" fill="#888"/>
                        <circle cx="110" cy="120" r="5" fill="#888"/>
                        <circle cx="80" cy="60" r="5" fill="#888"/>
                        <text x="145" y="70" font-family="Georgia" font-size="8" fill="#555">D(x) nhỏ ⇒ P(x) ≈ 0%</text>

                        <!-- Far points (large D -> high prob) -->
                        <line x1="100" y1="90" x2="380" y2="80" stroke="#111" stroke-width="1.5" stroke-dasharray="4,4"/>
                        <text x="240" y="75" font-family="Georgia" font-size="9" text-anchor="middle">Khoảng cách D(x) rất lớn!</text>

                        <circle cx="380" cy="80" r="14" fill="#fff" stroke="#111" stroke-width="2.5"/>
                        <text x="380" y="84" font-family="Georgia" font-size="9" font-weight="bold" text-anchor="middle">μ₂ ?</text>
                        <text x="380" y="115" font-family="Georgia" font-size="9" font-weight="bold" text-anchor="middle">P(x) ∝ D(x)² CỰC CAO!</text>
                        <text x="380" y="130" font-family="Georgia" font-size="8" fill="#555" text-anchor="middle">Được ưu tiên chọn làm tâm 2</text>
                      </g>
                    </svg>""",
                    "caption": "K-Means++ ưu tiên chọn các điểm ở xa tâm đã có làm tâm mới với xác suất tỷ lệ với D(x)², tránh hiện tượng các tâm chụm lại một chỗ."
                },
                "commonPitfalls": "Nhầm lẫn rằng K-Means++ chọn điểm xa nhất một cách tuyệt đối: Nếu luôn chọn điểm xa nhất tuyệt đối, mô hình sẽ bị bắt chết vào các điểm Outlier (nhiễu). K-Means++ chọn THEO XÁC SUẤT tỷ lệ thuận với D(x)², vẫn đảm bảo tính ngẫu nhiên khoa học!",
                "practiceQuestion": {
                    "level": "Nâng cao (Câu 18 Đề Thi VAIO 2025)",
                    "question": "Trong thuật toán K-Means++, xác suất P(x) để một điểm dữ liệu x được lựa chọn làm tâm cụm tiếp theo tỷ lệ thuận với đại lượng nào sau đây?",
                    "options": [
                        "A. Khoảng cách Euclid D(x) tới tâm cụm gần nhất",
                        "B. Bình phương khoảng cách D(x)² tới tâm cụm gần nhất đã chọn",
                        "C. Nghịch đảo khoảng cách 1 / D(x) để ưu tiên các điểm ở gần",
                        "D. Mật độ các điểm láng giềng xung quanh điểm x"
                    ],
                    "correctIndex": 1,
                    "hint": "Nhớ lại công thức xác suất của K-Means++: P(x) = D(x)² / sum(D(x')²).",
                    "solution": [
                        "Bước 1: Phân tích thuật toán Arthur & Vassilvitskii (2007) cho K-Means++.",
                        "Bước 2: Để kéo dãn khoảng cách giữa các tâm và tăng cường độ phân tách, thuật toán nâng khoảng cách lên lũy thừa bậc 2 (D(x)²).",
                        "Bước 3: Xác suất được chuẩn hóa theo phân phối P(x) = D(x)² / sum(D(x')²).",
                        "Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 9.3: CHỌN SỐ CỤM K: PHƯƠNG PHÁP KHUỶU TAY & HỆ SỐ SILHOUETTE
            # =================================================================
            {
                "heading": "9.3. Lựa Chọn Số Cụm K Tối Ưu: Phương Pháp Khuỷu Tay (Elbow Method) & Hệ Số Silhouette [-1, +1]",
                "content": "Làm thế nào để biết nên chia dữ liệu thành 2, 3 hay 5 cụm? Khám phá hai công cụ định lượng chuẩn mực: Phương pháp khuỷu tay Elbow dựa trên điểm uốn WCSS và Hệ số Silhouette đo độ nén nội cụm và cách ly ngoại cụm.",
                "deepDive": r"""**1. Bài toán hóc búa: Chọn K bằng bao nhiêu?**
Trong phân cụm không giám sát, con người không biết trước có bao nhiêu nhóm thực tế.
- Nếu bạn tăng $K$ từ 1 lên $N$ (bằng đúng số lượng mẫu):
  - Khi $K = N$: Mỗi điểm là một cụm riêng, $\text{WCSS} = 0$ tuyệt đối!
  - Nhưng điều đó hoàn toàn vô dụng vì mất đi ý nghĩa gom nhóm!
Ta cần một điểm cân bằng: Đủ số cụm để nén dữ liệu chặt chẽ, nhưng không quá nhiều cụm gây manh mún.

**2. Phương Pháp Khuỷu Tay (Elbow Method):**
- **Cách tiến hành:** Chạy K-Means với các giá trị $K = 1, 2, 3, 4, 5, \dots$ và ghi lại giá trị $\mathcal{J}_{\text{WCSS}}$ tương ứng.
- **Vẽ đồ thị:** Trục hoành là $K$, trục tung là $\text{WCSS}$.
- **Hiện tượng hình học:**
  - Khi $K$ tăng từ 1 lên 2, 3: WCSS giảm dốc đứng cực mạnh vì dữ liệu được phân chia đúng cấu trúc tự nhiên.
  - Sau một giá trị $K^*$ nào đó: Tốc độ giảm của WCSS đột ngột chậm hẳn lại, đồ thị thoai thoải dần.
  - Điểm uốn gập khúc này trông giống như **Khuỷu tay (Elbow)** của cánh tay người $\implies$ $K^*$ chính là **Số cụm tối ưu**!

**3. Hệ Số Silhouette (Silhouette Score - Peter Rousseeuw, 1987 - Câu 31 VAIO):**
Phương pháp Elbow đôi khi cho đường cong trơn tru không có khuỷu tay rõ ràng. Khi đó, **Hệ số Silhouette** là tiêu chuẩn định lượng số 1!

Với mỗi điểm dữ liệu $i$, ta tính hai đại lượng:
- **$a(i)$ - Độ gắn kết nội cụm (Cohesion):**
  Khoảng cách trung bình từ điểm $i$ tới tất cả các điểm khác TRONG CÙNG CỤM của nó:
  $$a(i) = \frac{1}{|C_A| - 1} \sum_{j \in C_A, j \ne i} \|x_i - x_j\|$$
  *(Càng nhỏ càng tốt $\implies$ Cụm đặc quánh, các điểm gần nhau).*
- **$b(i)$ - Độ phân tách ngoại cụm (Separation):**
  Khoảng cách trung bình từ điểm $i$ tới tất cả các điểm trong **CỤM LÁNG GIỀNG GẦN NHẤT**:
  $$b(i) = \min_{C_B \ne C_A} \frac{1}{|C_B|} \sum_{j \in C_B} \|x_i - x_j\|$$
  *(Càng lớn càng tốt $\implies$ Cụm của mình cách rất xa cụm đối thủ).*

**Công thức Hệ Số Silhouette của điểm $i$:**
$$s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}, \quad -1 \le s(i) \le +1$$

**Ý nghĩa các khoảng giá trị:**
- **$s(i) \approx +1$ (Lý tưởng):** $b(i) \gg a(i)$. Điểm nằm rất gần đồng đội và cách rất xa đối thủ $\implies$ Phân cụm xuất sắc!
- **$s(i) \approx 0$ (Lấp lửng ranh giới):** $b(i) \approx a(i)$. Điểm nằm ngay trên ranh giới tranh chấp giữa 2 cụm.
- **$s(i) < 0$ (Thảm họa):** $b(i) < a(i)$. Điểm bị gán nhầm cụm! Khoảng cách tới cụm khác còn gần hơn cụm hiện tại!

**Quy tắc chọn K:** Tính Silhouette Score trung bình trên toàn bộ dữ liệu $\bar{S} = \frac{1}{N}\sum s(i)$ cho từng $K$. **Chọn giá trị $K$ có $\bar{S}$ cao nhất!**""",
                "formula": r"s(i) = \frac{b(i) - a(i)}{\max(a(i), b(i))}, \quad -1 \le s(i) \le 1, \quad \bar{S} = \frac{1}{N}\sum_{i=1}^N s(i)",
                "mathExplainer": [
                    { "sym": "a(i)", "name": "Độ gắn kết nội cụm", "mean": "Khoảng cách trung bình từ điểm i tới các điểm trong cùng cụm (càng nhỏ càng tốt)." },
                    { "sym": "b(i)", "name": "Độ phân tách ngoại cụm", "mean": "Khoảng cách trung bình từ điểm i tới các điểm trong cụm láng giềng gần nhất (càng lớn càng tốt)." },
                    { "sym": "s(i)", "name": "Hệ số Silhouette của điểm i", "mean": "Thước đo chất lượng phân cụm [-1, 1]. Càng gần +1 càng hoàn hảo, âm là bị gán nhầm cụm." },
                    { "sym": "\\bar{S}", "name": "Silhouette Score trung bình", "mean": "Chỉ số đánh giá toàn cục để so sánh và lựa chọn số cụm K tối ưu." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 190" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="190" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 20)">
                        <!-- Elbow Chart (Left) -->
                        <g transform="translate(20, 10)">
                          <text x="100" y="0" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Phương Pháp Khuỷu Tay (Elbow)</text>
                          <line x1="20" y1="130" x2="180" y2="130" stroke="#111" stroke-width="1.5"/>
                          <line x1="20" y1="20" x2="20" y2="130" stroke="#111" stroke-width="1.5"/>
                          <text x="100" y="145" font-family="Georgia" font-size="9" text-anchor="middle">Số Cụm K (1, 2, 3, 4, 5)</text>
                          <text x="10" y="75" font-family="Georgia" font-size="9" transform="rotate(-90 10 75)" text-anchor="middle">WCSS</text>
                          <!-- Elbow curve: K=1(120), K=2(60), K=3(30), K=4(24), K=5(20) -->
                          <path d="M 30 25 L 60 70 L 95 105 L 135 115 L 175 120" fill="none" stroke="#111" stroke-width="2.5"/>
                          <!-- Elbow point circle -->
                          <circle cx="95" cy="105" r="6" fill="none" stroke="#111" stroke-width="2"/>
                          <text x="110" y="100" font-family="Georgia" font-size="10" font-weight="bold">Điểm Khuỷu K* = 3</text>
                        </g>

                        <!-- Divider -->
                        <line x1="270" y1="15" x2="270" y2="155" stroke="#ccc" stroke-dasharray="2,2"/>

                        <!-- Silhouette Diagram (Right) -->
                        <g transform="translate(320, 10)">
                          <text x="120" y="0" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Ý Nghĩa Hệ Số Silhouette s(i)</text>
                          <!-- Cluster A -->
                          <circle cx="50" cy="75" r="35" fill="#f0f0f0" stroke="#111" stroke-width="1.5"/>
                          <circle cx="45" cy="70" r="4" fill="#111"/>
                          <circle cx="60" cy="85" r="4" fill="#111"/>
                          <circle cx="35" cy="85" r="4" fill="#111"/>
                          <!-- Target point i -->
                          <circle cx="65" cy="65" r="5" fill="#111"/>
                          <text x="75" y="60" font-family="Georgia" font-size="9" font-weight="bold">Điểm i</text>
                          <text x="45" y="55" font-family="Georgia" font-size="8">a(i): Nội cụm</text>

                          <!-- Cluster B (Neighbor) -->
                          <circle cx="170" cy="75" r="35" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <circle cx="160" cy="70" r="4" fill="#888"/>
                          <circle cx="180" cy="85" r="4" fill="#888"/>
                          <circle cx="165" cy="90" r="4" fill="#888"/>

                          <!-- Line b(i) -->
                          <line x1="65" y1="65" x2="160" y2="70" stroke="#111" stroke-width="1.5" stroke-dasharray="3,3"/>
                          <text x="110" y="60" font-family="Georgia" font-size="9" font-weight="bold" text-anchor="middle">b(i): Ngoại cụm</text>

                          <text x="120" y="135" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">s(i) = [b(i) - a(i)] / max(a, b)</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "Hai phương pháp chọn K tối ưu: Điểm uốn gập khúc trên đường cong WCSS (Elbow) và thước đo tỷ lệ khoảng cách nội/ngoại cụm Silhouette."
                },
                "commonPitfalls": "Hiểu nhầm giá trị âm của Silhouette: Nếu một điểm có Silhouette âm (s < 0), điều đó KHÔNG PHẢI là lỗi thuật toán, mà là bằng chứng kết luận điểm đó đã bị gán nhầm cụm (khoảng cách tới cụm láng giềng b(i) nhỏ hơn khoảng cách nội cụm a(i))!",
                "practiceQuestion": {
                    "level": "Trung bình",
                    "question": "Một điểm dữ liệu x_i trong kết quả phân cụm có khoảng cách trung bình tới các điểm cùng cụm là a(i) = 3.0, và khoảng cách trung bình tới các điểm thuộc cụm láng giềng gần nhất là b(i) = 9.0. Hệ số Silhouette s(i) của điểm này bằng bao nhiêu?",
                    "options": [
                        "A. 0.67",
                        "B. 0.50",
                        "C. -0.67",
                        "D. 1.00"
                    ],
                    "correctIndex": 0,
                    "hint": "Áp dụng công thức s(i) = (b(i) - a(i)) / max(a(i), b(i)) = (9 - 3) / max(3, 9) = 6 / 9.",
                    "solution": [
                        "Bước 1: Tính tử số: b(i) - a(i) = 9.0 - 3.0 = 6.0.",
                        "Bước 2: Tính mẫu số: max(a(i), b(i)) = max(3.0, 9.0) = 9.0.",
                        "Bước 3: Tính hệ số Silhouette: s(i) = 6.0 / 9.0 = 2/3 ≈ 0.667 = 0.67.",
                        "Ý nghĩa: s(i) = 0.67 khá gần +1, chứng tỏ điểm này được phân cụm rất tốt.",
                        "Đáp án chính xác: A (0.67)."
                    ]
                }
            },

            # =================================================================
            # MỤC 9.4: BẢN CHẤT TOÁN HỌC CỦA PCA (EIGENDECOMPOSITION & SVD)
            # =================================================================
            {
                "heading": "9.4. Giảm Chiều Dữ Liệu PCA: Chiếu Bóng Tối Đa Hóa Phương Sai (Eigendecomposition & SVD)",
                "content": "Làm thế nào để nén dữ liệu từ hàng trăm chiều xuống 2 hoặc 3 chiều mà vẫn giữ lại linh hồn của thông tin? Khám phá thuật toán PCA của Karl Pearson: Từ khử tâm dữ liệu, ma trận hiệp phương sai, đến phân rã vector riêng.",
                "deepDive": r"""**1. Vấn đề của dữ liệu nhiều chiều (High-Dimensional Data):**
Trong thị giác máy tính, một bức ảnh $28 \times 28$ có tới $784$ chiều pixel. Trong y sinh, biểu hiện gen có tới $20,000$ chiều.
- Dữ liệu quá nhiều chiều khiến con người **không thể vẽ đồ thị trực quan hóa** (chỉ vẽ được 2D hoặc 3D).
- Gây ra **Lời nguyền số chiều (Curse of Dimensionality)**, làm chậm thuật toán và chứa rất nhiều đặc trưng thừa thãi, tương quan mạnh với nhau (Đa cộng tuyến).

**2. Mục tiêu toán học của PCA (Principal Component Analysis):**
PCA tìm kiếm các trục tọa độ mới $u_1, u_2, \dots, u_k$ (với $k < d$) sao cho:
1. **Phương sai (Độ phân tán) của dữ liệu sau khi chiếu lên các trục mới là LỚN NHẤT CÓ THỂ**.
2. **Sai số tái tạo (Reconstruction Error) bình phương là NHỎ NHẤT CÓ THỂ**.
*(Hai mục tiêu này đã được chứng minh toán học là hoàn toàn tương đương nhau!).*

**3. Quy trình 4 bước giải tích mẫu mực của PCA:**

- **Bước 1: Khử tâm (Mean Centering - BẮT BUỘC):**
  Trừ mỗi đặc trưng cho giá trị trung bình của nó:
  $$\tilde{X} = X - \bar{X}$$
  Đưa trọng tâm của toàn bộ đám mây dữ liệu về đúng gốc tọa độ $(0, 0, \dots, 0)$.

- **Bước 2: Tính Ma Trận Hiệp Phương Sai (Covariance Matrix $\Sigma$):**
  $$\Sigma = \frac{1}{N-1} \tilde{X}^T \tilde{X} \in \mathbb{R}^{d \times d}$$
  - Đường chéo chính $\Sigma_{ii}$: Phương sai của từng đặc trưng $x_i$ (Đo độ phân tán độc lập).
  - Các ô ngoài đường chéo $\Sigma_{ij}$: Hiệp phương sai giữa $x_i$ và $x_j$ (Đo mức độ tương quan tuyến tính giữa 2 biến).

- **Bước 3: Phân rã Trị riêng và Vector riêng (Eigendecomposition):**
  Giải phương trình đặc trưng:
  $$\Sigma v = \lambda v$$
  - **Vector riêng $v_k$ (Eigenvector):** Chính là **HƯỚNG CỦA TRỤC THÀNH PHẦN CHÍNH THỨ $k$ (Principal Component $k$)**! Các trục này luôn vuông góc (trực giao) từng đôi một: $v_i^T v_j = 0$ $\implies$ Triệt tiêu hoàn toàn sự dư thừa tương quan!
  - **Trị riêng $\lambda_k$ (Eigenvalue):** Chính là **ĐỘ LỚN CỦA PHƯƠNG SAI** mà dữ liệu giữ lại được khi chiếu lên trục $v_k$!
  Sắp xếp các trị riêng theo thứ tự giảm dần: $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_d \ge 0$.

- **Bước 4: Chiếu dữ liệu xuống không gian $k$ chiều ($k < d$):**
  Chọn $k$ vector riêng ứng với $k$ trị riêng lớn nhất làm ma trận chiếu $W = [v_1, v_2, \dots, v_k] \in \mathbb{R}^{d \times k}$.
  Tọa độ nén mới của dữ liệu là:
  $$Z = \tilde{X} W \in \mathbb{R}^{N \times k}$$

**4. Mối liên hệ kỳ diệu với SVD (Singular Value Decomposition):**
Trong thực tế (như hàm `PCA` của Scikit-Learn), máy tính không tính ma trận $\Sigma$ (vì tốn $\mathcal{O}(d^2)$ bộ nhớ), mà áp dụng SVD trực tiếp lên ma trận dữ liệu đã khử tâm:
$$\tilde{X} = U S V^T$$
Khi đó, các cột của ma trận $V$ chính là các vector riêng của $\Sigma$, và trị riêng liên hệ qua giá trị suy biến: $\lambda_i = \frac{s_i^2}{N-1}$!""",
                "formula": r"\Sigma = \frac{1}{N-1} \tilde{X}^T \tilde{X}, \quad \Sigma v_i = \lambda_i v_i, \quad Z = \tilde{X} W_k, \quad \tilde{X} = U S V^T",
                "mathExplainer": [
                    { "sym": "\\Sigma (Sigma)", "name": "Ma trận hiệp phương sai", "mean": "Ma trận vuông đối xứng d x d đo lường phương sai và tương quan giữa tất cả các cặp biến." },
                    { "sym": "v_i", "name": "Vector riêng (Eigenvector)", "mean": "Hướng của trục thành phần chính PC_i (các trục này luôn vuông góc trực giao với nhau)." },
                    { "sym": "\\lambda_i (Lambda)", "name": "Trị riêng (Eigenvalue)", "mean": "Độ lớn phương sai của dữ liệu được bảo toàn dọc theo trục thành phần chính v_i." },
                    { "sym": "Z = \\tilde{X} W_k", "name": "Dữ liệu sau khi giảm chiều", "mean": "Ma trận tọa độ mới trong không gian k chiều (k < d) sau phép chiếu tuyến tính." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 190" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="190" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(60, 20)">
                        <text x="260" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">HÌNH HỌC CỦA PCA: TRỤC CHÍNH PC1 (MAX PHƯƠNG SAI) &amp; PC2</text>

                        <!-- Old Axis -->
                        <line x1="40" y1="140" x2="380" y2="140" stroke="#888" stroke-width="1"/>
                        <line x1="210" y1="20" x2="210" y2="160" stroke="#888" stroke-width="1"/>
                        <text x="375" y="155" font-family="Georgia" font-size="9" fill="#666">Trục x₁ gốc</text>
                        <text x="215" y="30" font-family="Georgia" font-size="9" fill="#666">Trục x₂ gốc</text>

                        <!-- Elliptical Data points centered at (210, 90) -->
                        <circle cx="110" cy="130" r="3.5" fill="#111"/><circle cx="140" cy="115" r="3.5" fill="#111"/><circle cx="170" cy="105" r="3.5" fill="#111"/>
                        <circle cx="190" cy="100" r="3.5" fill="#111"/><circle cx="210" cy="90" r="4" fill="#111"/><circle cx="230" cy="80" r="3.5" fill="#111"/>
                        <circle cx="250" cy="75" r="3.5" fill="#111"/><circle cx="280" cy="65" r="3.5" fill="#111"/><circle cx="310" cy="50" r="3.5" fill="#111"/>

                        <!-- PC1 Vector (along elongation) -->
                        <line x1="80" y1="145" x2="340" y2="35" stroke="#111" stroke-width="2.5"/>
                        <polygon points="340,35 328,40 334,48" fill="#111"/>
                        <text x="345" y="35" font-family="Georgia" font-size="11" font-weight="bold">PC1 (v₁, λ₁ lớn nhất)</text>
                        <text x="310" y="20" font-family="Georgia" font-size="9" fill="#444">Phương sai cực đại</text>

                        <!-- PC2 Vector (orthogonal) -->
                        <line x1="175" y1="40" x2="245" y2="140" stroke="#111" stroke-width="1.5" stroke-dasharray="3,3"/>
                        <polygon points="175,40 185,46 178,52" fill="#111"/>
                        <text x="110" y="38" font-family="Georgia" font-size="10" font-weight="bold">PC2 (v₂, λ₂ nhỏ)</text>
                        <text x="145" y="145" font-family="Georgia" font-size="8" fill="#666">Vuông góc v₁ᵀv₂ = 0</text>
                      </g>
                    </svg>""",
                    "caption": "Trục PC1 bắt trọn hướng phân tán dài nhất của dữ liệu (ứng với trị riêng λ₁ lớn nhất); Trục PC2 trực giao vuông góc bắt phần phương sai còn lại."
                },
                "commonPitfalls": "Quên bước Mean Centering trước khi chạy PCA: Nếu không trừ trung bình (khử tâm), trục thành phần chính đầu tiên sẽ bị kéo lệch về phía gốc tọa độ thay vì đi qua tâm đám mây điểm, làm sai lệch hoàn toàn hướng phân tán!",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Trong thuật toán PCA, hai vector riêng (eigenvectors) ứng với hai thành phần chính khác nhau luôn thỏa mãn tính chất hình học nào sau đây?",
                    "options": [
                        "A. Luôn song song với nhau",
                        "B. Luôn trực giao (vuông góc) tuyệt đối với nhau (v_1ᵀ v_2 = 0)",
                        "C. Luôn có cùng độ dài trị riêng",
                        "D. Luôn đi qua điểm dị biệt (outlier) xa nhất"
                    ],
                    "correctIndex": 1,
                    "hint": "Ma trận hiệp phương sai là ma trận đối xứng thực. Các vector riêng ứng với các trị riêng phân biệt của ma trận đối xứng luôn trực giao nhau.",
                    "solution": [
                        "Bước 1: Ma trận hiệp phương sai Sigma là ma trận đối xứng thực (Sigma = Sigma^T).",
                        "Bước 2: Theo định lý phổ (Spectral Theorem) trong đại số tuyến tính, các vector riêng của ma trận đối xứng thực luôn trực giao từng đôi một: v_i^T v_j = 0 với mọi i khác j.",
                        "Bước 3: Ý nghĩa thực tiễn: Các trục thành phần chính vuông góc với nhau giúp triệt tiêu hoàn toàn tương quan tuyến tính giữa các biến mới.",
                        "Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 9.5: TỶ LỆ PHƯƠNG SAI GIẢI THÍCH & BIỂU ĐỒ SCREE PLOT
            # =================================================================
            {
                "heading": "9.5. Đọc Biểu Đồ Scree Plot, Tỷ Lệ Phương Sai Giải Thích (EVR) & Giới Hạn Tuyến Tính Của PCA",
                "content": "Làm thế nào để quyết định giữ lại bao nhiêu chiều? Học cách đọc biểu đồ Scree Plot, tính tỷ lệ phương sai giải thích tích lũy, và phân tích sự thất bại của PCA trước các bề mặt phi tuyến (Swiss Roll).",
                "deepDive": r"""**1. Tỷ Lệ Phương Sai Giải Thích (Explained Variance Ratio - EVR - Câu 47 VAIO):**
Tổng phương sai của toàn bộ dữ liệu bằng tổng các trị riêng:
$$\text{Total Variance} = \sum_{j=1}^d \lambda_j$$
Tỷ lệ phần trăm thông tin (phương sai) mà thành phần chính thứ $k$ giữ lại được là:
$$\text{EVR}_k = \frac{\lambda_k}{\sum_{j=1}^d \lambda_j}$$
- **Phương sai giải thích tích lũy (Cumulative Explained Variance):**
  $$\text{Cumulative EVR}(k) = \frac{\sum_{i=1}^k \lambda_i}{\sum_{j=1}^d \lambda_j}$$
- **Quy tắc công nghiệp:** Người ta thường chọn số chiều $k$ nhỏ nhất sao cho $\text{Cumulative EVR}(k) \ge 85\%$ hoặc $\ge 90\%$.

**2. Biểu Đồ Scree Plot (Biểu đồ sỏi đá chân núi):**
- **Nguồn gốc tên gọi:** Raymond Cattell (1966) đặt tên theo từ 'scree' (đá vụn rơi ở chân vách núi).
- **Cấu trúc biểu đồ:**
  - Trục hoành: Thứ tự các thành phần chính ($PC_1, PC_2, PC_3, \dots$).
  - Trục tung: Giá trị trị riêng $\lambda_i$ hoặc tỷ lệ $\text{EVR}_i$.
- **Quy tắc tìm điểm dừng:**
  - Vài thành phần đầu tiên có cột rất cao (Vách núi dựng đứng - Chứa thông tin cốt lõi).
  - Sau một điểm uốn gập khúc, các cột thấp tịt và thoai thoải dần (Đá vụn dưới chân núi - Chứa nhiễu).
  - Ta dừng lại ngay tại **điểm uốn của Scree Plot**, chỉ giữ lại các thành phần chính trước điểm uốn!

**3. Yêu cầu sống còn: Chuẩn hóa đặc trưng (Feature Scaling) trước PCA:**
- PCA là thuật toán **nhạy cảm cực độ với độ lớn thang đo**:
  - Nếu một biến đo bằng milimet ($[0, 5000]$) và một biến đo bằng mét ($[0, 5]$).
  - Phương sai của biến milimet sẽ lớn gấp hàng triệu lần biến mét!
  - PCA ngây thơ sẽ chọn luôn trục milimet làm PC1 mà không thèm nhìn biến mét!
  $\implies$ **BẮT BUỘC PHẢI CHUẨN HÓA DỮ LIỆU BẰNG `StandardScaler` (Z-score) TRƯỚC KHI CHẠY PCA!**

**4. Giới hạn chết người của PCA: Bề mặt phi tuyến (Swiss Roll):**
- PCA là thuật toán **Tuyến tính (Linear)**: Nó chỉ có thể chiếu dữ liệu lên các siêu phẳng phẳng tắp!
- Nếu dữ liệu có cấu trúc phi tuyến uốn khúc phức tạp (như chiếc bánh bông lan cuộn Swiss Roll):
  - Chiếu phẳng của PCA sẽ đè bẹp các vòng cuộn lên nhau, làm dính các điểm ở xa thành gần!
- **Giải pháp thay thế:**
  - **Kernel PCA:** Kết hợp Kernel Trick để giảm chiều phi tuyến.
  - **t-SNE (t-Distributed Stochastic Neighbor Embedding):** Chuyên dùng để trực quan hóa 2D/3D các cụm phức tạp (bảo toàn cấu trúc lân cận cục bộ).
  - **UMAP (Uniform Manifold Approximation and Projection):** Nhanh hơn t-SNE và bảo toàn tốt cả cấu trúc toàn cục.""",
                "formula": r"\text{EVR}_k = \frac{\lambda_k}{\sum_{j=1}^d \lambda_j}, \quad \text{Cumulative}(k) = \sum_{i=1}^k \text{EVR}_i \ge 0.90",
                "mathExplainer": [
                    { "sym": "\\text{EVR}_k", "name": "Tỷ lệ phương sai giải thích", "mean": "Phần trăm thông tin dữ liệu được bảo toàn bởi trục thành phần chính k." },
                    { "sym": "\\text{Cumulative EVR}", "name": "Phương sai tích lũy", "mean": "Tổng phần trăm thông tin giữ lại được khi chọn k thành phần chính đầu tiên." },
                    { "sym": "\\text{Scree Plot}", "name": "Biểu đồ sỏi đá", "mean": "Đồ thị cột trị riêng giảm dần giúp nhận diện điểm uốn để chọn số chiều dừng lại." },
                    { "sym": "\\text{Swiss Roll}", "name": "Cấu trúc bánh cuộn phi tuyến", "mean": "Dạng dữ liệu uốn khúc nơi PCA tuyến tính thất bại và bắt buộc phải dùng t-SNE / UMAP." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(60, 20)">
                        <text x="260" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">BIỂU ĐỒ SCREE PLOT: LỰA CHỌN SỐ CHIỀU NÉN TỐI ƯU</text>

                        <!-- Bars -->
                        <!-- PC1: 65% -->
                        <rect x="50" y="45" width="40" height="90" fill="#111"/>
                        <text x="70" y="40" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">65%</text>
                        <text x="70" y="150" font-family="Georgia" font-size="10" text-anchor="middle">PC1</text>

                        <!-- PC2: 25% -->
                        <rect x="110" y="100" width="40" height="35" fill="#444"/>
                        <text x="130" y="95" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">25%</text>
                        <text x="130" y="150" font-family="Georgia" font-size="10" text-anchor="middle">PC2</text>

                        <!-- PC3: 7% -->
                        <rect x="170" y="125" width="40" height="10" fill="#888"/>
                        <text x="190" y="120" font-family="Georgia" font-size="9" text-anchor="middle">7%</text>
                        <text x="190" y="150" font-family="Georgia" font-size="10" text-anchor="middle">PC3</text>

                        <!-- PC4: 3% -->
                        <rect x="230" y="131" width="40" height="4" fill="#aaa"/>
                        <text x="250" y="126" font-family="Georgia" font-size="9" text-anchor="middle">3%</text>
                        <text x="250" y="150" font-family="Georgia" font-size="10" text-anchor="middle">PC4</text>

                        <!-- Cumulative Curve -->
                        <line x1="70" y1="45" x2="130" y2="25" stroke="#111" stroke-width="2"/>
                        <circle cx="130" cy="25" r="4" fill="#111"/>
                        <text x="135" y="20" font-family="Georgia" font-size="10" font-weight="bold">PC1 + PC2 = 90%!</text>

                        <!-- Description box right -->
                        <g transform="translate(300, 35)">
                          <rect x="0" y="0" width="220" height="105" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="110" y="20" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Quyết Định Giảm Chiều</text>
                          <text x="15" y="42" font-family="Georgia" font-size="10">• PC1 giải thích 65% thông tin</text>
                          <text x="15" y="60" font-family="Georgia" font-size="10">• PC2 giải thích 25% thông tin</text>
                          <text x="15" y="80" font-family="Georgia" font-size="10" font-weight="bold">• Giữ 2 chiều: Nén được 90%!</text>
                          <text x="15" y="98" font-family="Georgia" font-size="9" fill="#555">Loại bỏ PC3, PC4 (chỉ là nhiễu)</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "Biểu đồ Scree Plot: Điểm gập khuỷu tay xuất hiện sau PC2; giữ lại PC1 và PC2 đã bảo toàn được 90% tổng phương sai của toàn bộ dữ liệu."
                },
                "commonPitfalls": "Quên rằng PCA là phép biến đổi tuyến tính: Rất nhiều người nghĩ PCA có thể bóc tách mọi hình thù phức tạp. Nếu dữ liệu phân bố dạng xoắn ốc hoặc hình cầu lồng nhau, PCA chiếu thẳng sẽ làm dính bết dữ liệu lại với nhau! Khi đó bắt buộc phải dùng t-SNE hoặc UMAP.",
                "practiceQuestion": {
                    "level": "Nâng cao (Câu 47 Đề Thi VAIO 2025)",
                    "question": "Khi thực hiện PCA trên một tập dữ liệu 5 chiều, ta thu được 5 trị riêng lần lượt là: λ₁ = 12.0, λ₂ = 5.0, λ₃ = 2.0, λ₄ = 0.8, λ₅ = 0.2. Nếu chỉ giữ lại 2 thành phần chính đầu tiên (PC1 và PC2), tỷ lệ phương sai giải thích tích lũy (Cumulative EVR) bằng bao nhiêu?",
                    "options": [
                        "A. 60.0%",
                        "B. 85.0%",
                        "C. 75.0%",
                        "D. 90.0%"
                    ],
                    "correctIndex": 1,
                    "hint": "Tính tổng phương sai = 12.0 + 5.0 + 2.0 + 0.8 + 0.2 = 20.0. Tính tổng λ₁ + λ₂ = 12.0 + 5.0 = 17.0. Tỷ lệ = 17.0 / 20.0.",
                    "solution": [
                        "Bước 1: Tính tổng phương sai toàn cục của cả 5 chiều:",
                        "  Total = 12.0 + 5.0 + 2.0 + 0.8 + 0.2 = 20.0.",
                        "Bước 2: Tính lượng phương sai được bảo tồn bởi PC1 và PC2:",
                        "  Sum(PC1, PC2) = λ₁ + λ₂ = 12.0 + 5.0 = 17.0.",
                        "Bước 3: Tính tỷ lệ tích lũy:",
                        "  Cumulative EVR = 17.0 / 20.0 = 0.85 = 85.0%.",
                        "Kết luận: Giữ lại 2 chiều đã bảo tồn được 85% tổng thông tin của dữ liệu gốc.",
                        "Đáp án chính xác: B (85.0%)."
                    ]
                }
            },

            # =================================================================
            # MỤC 9.6: BÀI TOÁN TÍNH TAY CHUẨN ĐỀ THI VAIO (CÂU 3 & CÂU 47)
            # =================================================================
            {
                "heading": "9.6. Bài Toán Tính Tay Chuẩn Đề Thi VAIO: Phân Cụm K-Means 1 Chiều, Cập Nhật Tâm & Tính Ma Trận Hiệp Phương Sai PCA",
                "content": "Thực hành giải bài toán tính tay kinh điển mô phỏng chuẩn xác Câu 3 và Câu 47 Đề thi Olympic AI: Tính toán chi tiết từng bước gán cụm, cập nhật tọa độ tâm mới, tính WCSS và tìm trục thành phần chính PCA giữ lại 100% phương sai.",
                "deepDive": r"""**1. Đề bài chuẩn Olympic AI:**

**PHẦN A (Phân Cụm K-Means - Bám sát Câu 3 Đề thi VAIO):**
Cho 6 điểm dữ liệu 1 chiều trên trục số thực:
$$X = \{2, \, 4, \, 10, \, 12, \, 14, \, 20\}$$
Ta muốn phân thành $K = 2$ cụm. Khởi tạo 2 tâm cụm ban đầu:
$$\mu_1 = 4.0, \quad \mu_2 = 12.0$$
*Yêu cầu thí sinh:*
1. Thực hiện bước Gán cụm (Assignment Step) cho cả 6 điểm về 2 tâm $\mu_1$ và $\mu_2$.
2. Thực hiện bước Cập nhật tâm (Update Step): Tính tọa độ tâm cụm mới $\mu_1'$ và $\mu_2'$.
3. Tính hàm chi phí $\text{WCSS}$ sau bước lặp đầu tiên này.

**PHẦN B (Giảm Chiều PCA - Bám sát Câu 47 Đề thi VAIO):**
Cho tập dữ liệu 2 chiều gồm $N = 4$ mẫu đã được chuẩn hóa:
$$x_1 = (1, 1)^T, \quad x_2 = (3, 3)^T, \quad x_3 = (-1, -1)^T, \quad x_4 = (-3, -3)^T$$
*Yêu cầu thí sinh:*
1. Kiểm tra xem dữ liệu đã được khử tâm (Mean Centered) hay chưa.
2. Tính ma trận hiệp phương sai mẫu $\Sigma$.
3. Tìm các trị riêng $\lambda_1, \lambda_2$ và vector riêng đơn vị $v_1$ của thành phần chính thứ nhất PC1.
4. Trục thành phần chính thứ nhất PC1 giải thích được bao nhiêu phần trăm tổng phương sai của dữ liệu?

---

**2. Lời giải chi tiết từng bước (Step-by-Step Derivation):**

**LỜI GIẢI PHẦN A (K-MEANS):**

**Bước 1: Bước Gán cụm (Assignment Step):**
Đo khoảng cách từ từng điểm tới $\mu_1 = 4.0$ và $\mu_2 = 12.0$:
- Điểm $x = 2$: $|2 - 4| = 2 \le |2 - 12| = 10 \implies$ **Thuộc Cụm 1**.
- Điểm $x = 4$: $|4 - 4| = 0 \le |4 - 12| = 8 \implies$ **Thuộc Cụm 1**.
- Điểm $x = 10$: $|10 - 4| = 6 > |10 - 12| = 2 \implies$ **Thuộc Cụm 2**.
- Điểm $x = 12$: $|12 - 4| = 8 > |12 - 12| = 0 \implies$ **Thuộc Cụm 2**.
- Điểm $x = 14$: $|14 - 4| = 10 > |14 - 12| = 2 \implies$ **Thuộc Cụm 2**.
- Điểm $x = 20$: $|20 - 4| = 16 > |20 - 12| = 8 \implies$ **Thuộc Cụm 2**.

Kết quả phân chia cụm:
- **Cụm 1 ($C_1$):** Gồm 2 điểm $\{2, 4\}$.
- **Cụm 2 ($C_2$):** Gồm 4 điểm $\{10, 12, 14, 20\}$.

**Bước 2: Bước Cập nhật tâm (Update Step):**
Tính trung bình cộng tọa độ (Mean) của từng cụm:
$$\mu_1' = \frac{2 + 4}{2} = \frac{6}{2} = 3.0$$
$$\mu_2' = \frac{10 + 12 + 14 + 20}{4} = \frac{56}{4} = 14.0$$
Tâm cụm mới đã dịch chuyển: $\mu_1$ từ $4.0 \to 3.0$; $\mu_2$ từ $12.0 \to 14.0$!

**Bước 3: Tính hàm chi phí WCSS:**
$$\text{WCSS}_1 = (2 - 3)^2 + (4 - 3)^2 = (-1)^2 + 1^2 = 1 + 1 = 2.0$$
$$\text{WCSS}_2 = (10 - 14)^2 + (12 - 14)^2 + (14 - 14)^2 + (20 - 14)^2$$
$$= (-4)^2 + (-2)^2 + 0^2 + 6^2 = 16 + 4 + 0 + 36 = 56.0$$
$$\text{Total WCSS} = \text{WCSS}_1 + \text{WCSS}_2 = 2.0 + 56.0 = 58.0$$

---

**LỜI GIẢI PHẦN B (PCA):**

**Bước 1: Kiểm tra khử tâm (Mean Centering):**
$$\bar{x} = \frac{1 + 3 + (-1) + (-3)}{4} = \frac{0}{4} = 0$$
$$\bar{y} = \frac{1 + 3 + (-1) + (-3)}{4} = \frac{0}{4} = 0$$
Cả hai trục đều có trung bình bằng 0 $\implies$ **Dữ liệu đã được khử tâm hoàn hảo!**

**Bước 2: Tính Ma trận Hiệp Phương Sai mẫu $\Sigma$ ($N = 4 \implies N - 1 = 3$):**
$$\Sigma = \frac{1}{3} \tilde{X}^T \tilde{X} = \frac{1}{3} \begin{bmatrix} x_1^2 + x_2^2 + x_3^2 + x_4^2 & x_1 y_1 + x_2 y_2 + x_3 y_3 + x_4 y_4 \\ x_1 y_1 + x_2 y_2 + x_3 y_3 + x_4 y_4 & y_1^2 + y_2^2 + y_3^2 + y_4^2 \end{bmatrix}$$
Ta có:
- $1^2 + 3^2 + (-1)^2 + (-3)^2 = 1 + 9 + 1 + 9 = 20$.
- $1(1) + 3(3) + (-1)(-1) + (-3)(-3) = 1 + 9 + 1 + 9 = 20$.
Do đó:
$$\Sigma = \frac{1}{3} \begin{bmatrix} 20 & 20 \\ 20 & 20 \end{bmatrix} = \begin{bmatrix} 20/3 & 20/3 \\ 20/3 & 20/3 \end{bmatrix}$$

**Bước 3: Tìm Trị riêng $\lambda$ và Vector riêng $v$:**
Phương trình đặc trưng: $\det(\Sigma - \lambda I) = 0$:
$$\det \begin{bmatrix} 20/3 - \lambda & 20/3 \\ 20/3 & 20/3 - \lambda \end{bmatrix} = \left(\frac{20}{3} - \lambda\right)^2 - \left(\frac{20}{3}\right)^2 = 0$$
$$\lambda \left(\lambda - \frac{40}{3}\right) = 0 \implies \lambda_1 = \frac{40}{3} \approx 13.33, \quad \lambda_2 = 0$$

Tìm vector riêng đơn vị $v_1$ ứng với $\lambda_1 = 40/3$:
$$(\Sigma - \lambda_1 I) v_1 = 0 \implies \begin{bmatrix} -20/3 & 20/3 \\ 20/3 & -20/3 \end{bmatrix} \begin{bmatrix} v_{11} \\ v_{12} \end{bmatrix} = 0 \implies v_{11} = v_{12}$$
Chuẩn hóa độ dài $\|v_1\| = 1$:
$$v_1 = \begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix} \approx \begin{bmatrix} 0.707 \\ 0.707 \end{bmatrix}$$
*Ý nghĩa hình học:* Trục PC1 chính là **đường phân giác góc phần tư I-III ($y = x$)**!

**Bước 4: Tỷ lệ phương sai giải thích của PC1:**
$$\text{EVR}_1 = \frac{\lambda_1}{\lambda_1 + \lambda_2} = \frac{40/3}{40/3 + 0} = \frac{40/3}{40/3} = 1.0 = 100\%!$$
**Kết luận kỳ vĩ:**
Vì 4 điểm dữ liệu ban đầu nằm thẳng hàng tuyệt đối trên đường thẳng $y = x$, trục PC1 đã bắt trọn **$100\%$ PHƯƠNG SAI CỦA DỮ LIỆU**! Khi nén từ 2D xuống 1D dọc theo trục PC1, ta bảo toàn trọn vẹn $100\%$ thông tin mà không làm mất mát bất kỳ một chút sai số nào!""",
                "formula": r"\mu_1'=3.0, \, \mu_2'=14.0 \implies \text{WCSS}=58.0; \quad \Sigma = \begin{bmatrix} 20/3 & 20/3 \\ 20/3 & 20/3 \end{bmatrix} \implies \lambda_1=\frac{40}{3}, \, \text{EVR}_1=100\%",
                "mathExplainer": [
                    { "sym": "\\mu_1'=3.0, \\mu_2'=14.0", "name": "Tâm cụm K-Means cập nhật", "mean": "Tọa độ mới sau 1 lượt lặp bằng trung bình cộng các điểm trong cụm." },
                    { "sym": "\\text{WCSS} = 58.0", "name": "Tổng bình phương nội cụm", "mean": "Đo lường độ nén chặt của 2 cụm sau bước phân chia." },
                    { "sym": "\\lambda_1 = 40/3, \\lambda_2 = 0", "name": "Các trị riêng của ma trận hiệp phương sai", "mean": "Trị riêng thứ nhất giữ lại toàn bộ độ phân tán; trị riêng thứ hai bằng 0 do dữ liệu thẳng hàng." },
                    { "sym": "\\text{EVR}_1 = 100\\%", "name": "Phương sai giải thích của PC1", "mean": "Trục PC1 bảo toàn 100% thông tin dữ liệu gốc khi giảm chiều từ 2D xuống 1D." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 190" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="190" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(30, 20)">
                        <text x="290" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">TỔNG HỢP KẾT QUẢ TÍNH TAY THỰC CHIẾN CÂU 3 &amp; CÂU 47</text>

                        <!-- Box 1: K-Means 1D -->
                        <g transform="translate(10, 35)">
                          <rect x="0" y="0" width="260" height="120" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="130" y="22" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">1. K-Means 1D (Câu 3)</text>
                          <text x="15" y="48" font-family="Georgia" font-size="10">• Cụm 1: {2, 4} ⇒ μ₁' = (2+4)/2 = 3.0</text>
                          <text x="15" y="68" font-family="Georgia" font-size="10">• Cụm 2: {10,12,14,20} ⇒ μ₂' = 56/4 = 14.0</text>
                          <text x="15" y="88" font-family="Georgia" font-size="10">• WCSS₁ = 2.0, WCSS₂ = 56.0</text>
                          <text x="15" y="110" font-family="Georgia" font-size="11" font-weight="bold">⇒ Tổng WCSS = 58.0</text>
                        </g>

                        <!-- Box 2: PCA 2D -> 1D -->
                        <g transform="translate(290, 35)">
                          <rect x="0" y="0" width="280" height="120" fill="#111"/>
                          <text x="140" y="22" font-family="Georgia" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">2. PCA Nén 2D → 1D (Câu 47)</text>
                          <text x="15" y="48" font-family="Georgia" font-size="10" fill="#eee">• Dữ liệu thẳng hàng y = x</text>
                          <text x="15" y="70" font-family="Georgia" font-size="11" font-weight="bold" fill="#fff">• Trị riêng: λ₁ = 40/3, λ₂ = 0</text>
                          <text x="15" y="92" font-family="Georgia" font-size="11" font-weight="bold" fill="#fff">• Trục PC1: v₁ = (1/√2, 1/√2)ᵀ</text>
                          <text x="15" y="112" font-family="Georgia" font-size="10" fill="#ccc">⇒ PC1 giữ lại 100% PHƯƠNG SAI!</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "Bảng tổng hợp tính tay thực chiến: Cập nhật tâm K-Means thu được WCSS = 58.0 và phân rã PCA bảo toàn trọn vẹn 100% phương sai khi nén xuống 1D."
                },
                "commonPitfalls": "Mẫu số của ma trận hiệp phương sai mẫu: Trong thống kê mẫu, mẫu số bắt buộc là N - 1 (với N = 4 mẫu thì chia cho 3) theo hiệu chỉnh Bessel để ước lượng không thiên lệch. Rất nhiều học sinh chia cho N = 4 dẫn tới sai số kết quả ma trận!",
                "practiceQuestion": {
                    "level": "Nâng cao (Câu 3 Đề Thi VAIO 2025)",
                    "question": "Cho một cụm gồm 3 điểm dữ liệu 2D: P₁(1, 2), P₂(3, 4), P₃(5, 6). Tọa độ trọng tâm (Centroid) của cụm này và tổng bình phương khoảng cách WCSS nội cụm lần lượt bằng:",
                    "options": [
                        "A. Tâm (3, 4), WCSS = 16.0",
                        "B. Tâm (3, 4), WCSS = 8.0",
                        "C. Tâm (3, 4), WCSS = 4.0",
                        "D. Tâm (2, 3), WCSS = 12.0"
                    ],
                    "correctIndex": 0,
                    "hint": "Tính tâm trung bình: x = (1+3+5)/3 = 3, y = (2+4+6)/3 = 4 => Tâm (3, 4). Tính d² từ từng điểm tới (3, 4).",
                    "solution": [
                        "Bước 1: Tính tọa độ tâm cụm bằng trung bình cộng:",
                        "  x_mean = (1 + 3 + 5) / 3 = 9 / 3 = 3.0.",
                        "  y_mean = (2 + 4 + 6) / 3 = 12 / 3 = 4.0.",
                        "  => Tâm cụm là (3, 4).",
                        "Bước 2: Tính tổng bình phương khoảng cách WCSS:",
                        "  - Đến P₁(1, 2): (1 - 3)² + (2 - 4)² = (-2)² + (-2)² = 4 + 4 = 8.",
                        "  - Đến P₂(3, 4): (3 - 3)² + (4 - 4)² = 0 + 0 = 0.",
                        "  - Đến P₃(5, 6): (5 - 3)² + (6 - 4)² = 2² + 2² = 4 + 4 = 8.",
                        "  => WCSS = 8 + 0 + 8 = 16.0.",
                        "Đáp án chính xác: A (Tâm (3, 4), WCSS = 16.0)."
                    ]
                }
            }
        ],
        "interactiveWidget": "widget-knn-classifier",
        "examConnection": {
            "questionTitle": "Điểm Trọng Tâm Về K-Means & PCA Trong Đề Thi VAIO 2025",
            "items": [
                {
                    "code": "Câu 3 VAIO: Chu Trình K-Means & WCSS",
                    "problem": "Tính toán tọa độ cập nhật tâm và chứng minh hàm WCSS luôn giảm đơn điệu sau mỗi bước lặp.",
                    "solution": [
                        "1. Gán điểm về tâm gần nhất theo khoảng cách Euclid.",
                        "2. Cập nhật tâm bằng Mean tọa độ của cụm.",
                        "3. Tính WCSS = sum ||x - mu||² để định lượng độ nén chặt."
                    ]
                },
                {
                    "code": "Câu 18 & 31 VAIO: K-Means++ & Hệ Số Silhouette",
                    "problem": "Khởi tạo thông minh với xác suất P(x) tỷ lệ thuận với D(x)² và tiêu chuẩn chọn K tối ưu.",
                    "solution": [
                        "1. K-Means++ chọn tâm xa nhau với P(x) ∝ D(x)².",
                        "2. Phương pháp Elbow tìm điểm uốn WCSS.",
                        "3. Hệ số Silhouette s(i) = [b(i) - a(i)] / max(a, b) trong khoảng [-1, 1]."
                    ]
                },
                {
                    "code": "Câu 47 VAIO: PCA & Ma Trận Hiệp Phương Sai",
                    "problem": "Bản chất của Vector riêng, Trị riêng và tỷ lệ phương sai giải thích tích lũy.",
                    "solution": [
                        "1. Vector riêng v_i xác định hướng trực giao của các trục chính.",
                        "2. Trị riêng λ_i đo lường phương sai được giữ lại.",
                        "3. Tỷ lệ phương sai giải thích EVR_k = λ_k / sum(λ). Bắt buộc khử tâm trước khi chạy PCA."
                    ]
                }
            ]
        },
        "takeaways": [
            "Học không giám sát tự động khám phá quy luật ẩn mà hoàn toàn không có nhãn đúng y.",
            "K-Means lặp 2 bước luân phiên: Gán điểm về tâm gần nhất và Cập nhật tâm bằng giá trị trung bình cộng (Mean).",
            "K-Means++ khởi tạo các tâm cụm nằm xa nhau với xác suất tỷ lệ thuận với bình phương khoảng cách D(x)².",
            "Chọn K tối ưu bằng điểm khuỷu tay Elbow của WCSS hoặc điểm cực đại của Hệ số Silhouette [-1, 1].",
            "PCA tìm các trục trực giao tối đa hóa phương sai: Vector riêng là hướng trục chiếu, Trị riêng là độ lớn phương sai bảo tồn.",
            "Cả K-Means và PCA đều BẮT BUỘC phải chuẩn hóa đặc trưng (Feature Scaling) trước khi chạy."
        ]
    }
