// quiz.js - Interactive Exam Simulator with Authentic Questions from VAIO 2025 (Mã Đề 006)

const QUIZ_DATA = [
  {
    id: 1,
    category: "Deep Learning",
    question: "Câu 1. Trong mạng nơ-ron, chuẩn hóa lô (Batch Normalization) thường được đặt ở đâu?",
    options: [
      "A. Trước hàm kích hoạt ReLU và sau lớp tuyến tính (Linear)",
      "B. Sau ReLU",
      "C. Sau lớp bỏ ngẫu nhiên (dropout)",
      "D. Trước lớp đầu vào (input layer)"
    ],
    correctIndex: 0,
    explanation: "Chuẩn hóa lô (Batch Normalization) thường được đặt trước ReLU và sau lớp tuyến tính (Linear → BatchNorm → ReLU). Nếu đặt sau ReLU, các giá trị âm bị biến thành 0 sẽ tạo ra sự lệch phân phối đỉnh 0 và dẫn tới gradient thưa thớt (sparse gradient), làm chậm quá trình huấn luyện."
  },
  {
    id: 2,
    category: "Computer Vision",
    question: "Câu 2. Thành phần nào sau đây là một tham số có thể học (learnable parameter) trong một lớp tích chập (Conv2D)?",
    options: [
      "A. Kích thước của dữ liệu đầu vào",
      "B. Các giá trị trong bộ lọc (filter weights)",
      "C. Kích thước bước nhảy (stride)",
      "D. Kích thước padding"
    ],
    correctIndex: 1,
    explanation: "Các giá trị trong bộ lọc (kernel weights) là tham số học được qua quá trình lan truyền ngược (backpropagation). Kích thước đầu vào, bước nhảy (stride) và padding là các siêu tham số (hyperparameters) do người dùng thiết lập cố định."
  },
  {
    id: 3,
    category: "Training Flow",
    question: "Câu 3. Nếu mất mát (loss) không giảm sau 5 vòng lặp (epoch) đầu tiên dù tỷ lệ học là 0.001, bạn nên làm gì đầu tiên?",
    options: [
      "A. Dừng lại và chọn mô hình khác",
      "B. Kiểm tra lại quy trình dữ liệu (data pipeline), tăng cường dữ liệu (augmentation) và bộ tối ưu",
      "C. Tăng tỷ lệ học lên 0.1",
      "D. Tăng số lớp của mô hình"
    ],
    correctIndex: 1,
    explanation: "5 vòng lặp là khoảng thời gian rất sớm. Việc tăng vọt lr lên 0.1 có thể làm mô hình phân kỳ. Cách xử lý chuyên nghiệp đầu tiên là kiểm tra data pipeline (dữ liệu có bị lỗi, nhãn đúng không, batch size có phù hợp không) và bộ tối ưu."
  },
  {
    id: 10,
    category: "Computer Vision",
    question: "Câu 10. Áp dụng thuật toán Non-Maximum Suppression (NMS) với ngưỡng IoU_threshold = 0.40 cho 3 hộp bao: B1 (0,0,100,100, conf=0.95); B2 (10,10,90,90, conf=0.90); B3 (105,105,200,200, conf=0.85). Những hộp nào sẽ được giữ lại?",
    options: [
      "A. B1 và B2",
      "B. Chỉ B1",
      "C. B1 và B3",
      "D. B2 và B3"
    ],
    correctIndex: 2,
    explanation: "Bước 1: Chọn B1 vì điểm tin cậy cao nhất (0.95), đưa vào tập kết quả. Bước 2: B2 nằm hoàn toàn trong B1. Diện tích giao = 80 × 80 = 6400, diện tích hợp = 10000 ⇒ IoU(B1, B2) = 0.64 > 0.40 ⇒ Loại B2. Bước 3: B3 không giao nhau với B1 (IoU = 0) ⇒ Giữ lại B3. Kết quả cuối: Giữ B1 và B3."
  },
  {
    id: 12,
    category: "Machine Learning",
    question: "Câu 12. Thuật toán học máy nào sau đây là phổ biến và hiệu quả, dựa trên ý tưởng bagging (Bootstrap Aggregating)?",
    options: [
      "A. XGBoost",
      "B. Hồi quy tuyến tính (Linear Regression)",
      "C. Cây quyết định (Decision Tree)",
      "D. Rừng ngẫu nhiên (Random Forest)"
    ],
    correctIndex: 3,
    explanation: "Random Forest được xây dựng trên nền tảng Bagging: lấy mẫu tái lập có hoàn lại (Bootstrap) và huấn luyện nhiều cây quyết định song song độc lập, sau đó bầu cử đa số hoặc tính trung bình để giảm phương sai (variance)."
  },
  {
    id: 14,
    category: "NLP",
    question: "Câu 14. Trong xử lý ngôn ngữ tự nhiên, đâu là thứ tự đúng của các bước xử lý cơ bản?",
    options: [
      "A. 2 (Chuẩn hóa) → 1 (Tách từ) → 4 (Gán nhãn từ loại) → 3 (Rút gọn từ)",
      "B. 2 (Chuẩn hóa) → 1 (Tách từ) → 3 (Rút gọn từ) → 4 (Gán nhãn từ loại)",
      "C. 1 → 3 → 2 → 4",
      "D. 1 → 2 → 4 → 3"
    ],
    correctIndex: 1,
    explanation: "Quy trình chuẩn: 2. Chuẩn hóa văn bản (hạ thường, bỏ ký tự lạ) → 1. Tách từ (Tokenization) → 3. Rút gọn từ (Stemming) → 4. Gán nhãn từ loại (POS Tagging)."
  },
  {
    id: 16,
    category: "NLP & LLM",
    question: "Câu 16. Kỹ thuật Chain-of-Thought (CoT) trong các mô hình ngôn ngữ lớn (LLM) là gì?",
    options: [
      "A. Yêu cầu mô hình trả lời càng ngắn gọn càng tốt để tiết kiệm tài nguyên",
      "B. Huấn luyện mô hình dự đoán từ tiếp theo bằng dữ liệu song ngữ",
      "C. Yêu cầu mô hình sinh câu hỏi thay vì câu trả lời",
      "D. Thúc đẩy mô hình giải bài toán bằng cách liệt kê từng bước suy luận trung gian"
    ],
    correctIndex: 3,
    explanation: "Chain-of-Thought (chuỗi suy nghĩ) hướng dẫn mô hình phân tích bài toán thành các bước lập luận trung gian từng bước một trước khi đưa ra kết luận cuối cùng, giúp tăng vượt bậc độ chính xác trong giải toán và suy luận logic."
  },
  {
    id: 18,
    category: "Clustering",
    question: "Câu 18. Cho 7 điểm dữ liệu chia vào 3 cụm: C1={(0,6), (6,0)}; C2={(2,2), (4,4), (6,6)}; C3={(5,5), (7,7)}. Tâm của 3 cụm sẽ là?",
    options: [
      "A. C1:(0,0), C2:(48,48), C3:(35,35)",
      "B. C1:(3,3), C2:(4,4), C3:(6,6)",
      "C. C1:(6,6), C2:(12,12), C3:(12,12)",
      "D. C1:(3,3), C2:(6,6), C3:(12,12)"
    ],
    correctIndex: 1,
    explanation: "Tâm cụm là trung bình cộng tọa độ: C1 = ((0+6)/2, (6+0)/2) = (3,3); C2 = ((2+4+6)/3, (2+4+6)/3) = (4,4); C3 = ((5+7)/2, (5+7)/2) = (6,6)."
  },
  {
    id: 20,
    category: "NLP",
    question: "Câu 20. Mô hình BERT nhận đầu vào là gì?",
    options: [
      "A. Vector ID (Token ID), Mặt nạ chú ý (Attention mask), ID loại token (Token type ID)",
      "B. Chỉ văn bản thô (raw text)",
      "C. Cặp câu với nhúng (embedding)",
      "D. Từ rời rạc"
    ],
    correctIndex: 0,
    explanation: "Đầu vào hoàn chỉnh của mô hình BERT gồm 3 thành phần: Token IDs (chỉ số từ vựng), Attention Mask (đánh dấu từ thật vs padding), và Token Type IDs (phân biệt câu A và câu B trong cặp câu)."
  },
  {
    id: 25,
    category: "Machine Learning",
    question: "Câu 25. Cho tập dữ liệu 8 mẫu 3 đặc trưng (F1, F2, F3). Điểm truy vấn Q = (6, 2, 6). Sử dụng k-NN với khoảng cách Euclid và k = 3, lớp nào sẽ được dự đoán?",
    options: [
      "A. Xanh dương",
      "B. Đỏ",
      "C. Xanh lá",
      "D. Hòa (không thể quyết định)"
    ],
    correctIndex: 2,
    explanation: "Tính khoảng cách từ Q=(6,2,6) đến các điểm: d(S7) = √((6-5)² + (2-2)² + (6-5)²) = √2 ≈ 1.41 (Xanh lá); d(S8) = √((6-6)² + (2-1)² + (6-4)²) = √5 ≈ 2.24 (Xanh lá); d(S5) = √((6-9)² + (2-6)² + (6-6)²) = 5 (Xanh dương). 3 láng giềng gần nhất là S7, S8 (Xanh lá) và S5 (Xanh dương). Bình chọn đa số: Xanh lá thắng với 2/3 phiếu."
  },
  {
    id: 27,
    category: "Computer Vision",
    question: "Câu 27. Cho đầu vào shape (1, 32, 32, 3), qua lớp Conv2D(filters=32, kernel_size=(5,5), strides=(2,2), padding='same'). Kích thước của output_tensor là bao nhiêu?",
    options: [
      "A. (1, 16, 16, 32)",
      "B. (1, 16, 16, 3)",
      "C. (1, 14, 14, 32)",
      "D. (1, 32, 32, 32)"
    ],
    correctIndex: 0,
    explanation: "Với padding='same' và stride=2: H_out = ⌈32 / 2⌉ = 16, W_out = ⌈32 / 2⌉ = 16. Số kênh đầu ra bằng số bộ lọc filters = 32. Do đó shape là (1, 16, 16, 32)."
  },
  {
    id: 37,
    category: "Machine Learning",
    question: "Câu 37. Dựa trên tập dữ liệu 6 sinh viên (4 sinh viên Passed=T, 2 sinh viên Passed=F), hãy tính xấp xỉ Entropy H(Passed)?",
    options: [
      "A. 0.66",
      "B. 1.92",
      "C. 0.92",
      "D. 1.32"
    ],
    correctIndex: 2,
    explanation: "p(T) = 4/6 = 2/3, p(F) = 2/6 = 1/3. H(Passed) = - [ (2/3) log₂(2/3) + (1/3) log₂(1/3) ] = - [ (0.667 × -0.585) + (0.333 × -1.585) ] = 0.390 + 0.528 = 0.918 ≈ 0.92."
  },
  {
    id: 40,
    category: "Deep Learning",
    question: "Câu 40. Khi huấn luyện MLP bằng mini-batch SGD, bạn cần làm gì sau mỗi epoch để đảm bảo học hiệu quả và tránh thiên lệch?",
    options: [
      "A. Xáo trộn dữ liệu (shuffle) huấn luyện",
      "B. Sử dụng toàn bộ dữ liệu (full-batch) để cập nhật trọng số",
      "C. Đặt lại trọng số về giá trị ban đầu",
      "D. Chuyển sang sử dụng bộ tối ưu Adam"
    ],
    correctIndex: 0,
    explanation: "Xáo trộn dữ liệu (Shuffle) huấn luyện sau mỗi epoch giúp các mini-batch liên tục thay đổi hình thái bề mặt hàm mất mát, tạo điều kiện cho mô hình thoát khỏi các cực tiểu địa phương (local minima) xấu."
  },
  {
    id: 43,
    category: "Computer Vision",
    question: "Câu 43. Khối 'block 4-2' của ResNet-18 gồm 2 lớp Conv 3x3 với Cin=512, Cout=512. Xử lý tensor đầu vào (1, 512, 7, 7). Tổng số tham số có thể huấn luyện và FLOPs xấp xỉ là bao nhiêu?",
    options: [
      "A. 11.7 M; 1.8 GFLOPs",
      "B. 4.7 M; 0.46 GFLOPs",
      "C. 0.50 M; 0.05 GFLOPs",
      "D. 8.4 M; 0.82 GFLOPs"
    ],
    correctIndex: 1,
    explanation: "Params = 2 × (3 × 3 × 512 × 512) = 4,718,592 ≈ 4.7 Triệu (4.7M). MACs = 2 × (7 × 7 × 512 × (512 × 3 × 3)) = 231,211,008. FLOPs ≈ 2 × MACs = 462,422,016 ≈ 0.46 GFLOPs."
  },
  {
    id: 48,
    category: "Calculus",
    question: "Câu 48. Gradient của hàm số f(x, y) = 2x² - 3y² + 4y - 10 tại điểm (0, 0) là gì?",
    options: [
      "A. 1i + 10j",
      "B. 2i - 3j",
      "C. -3i + 4j",
      "D. 0i + 4j"
    ],
    correctIndex: 3,
    explanation: "∂f/∂x = 4x; tại x=0 ⇒ 4(0) = 0. ∂f/∂y = -6y + 4; tại y=0 ⇒ -6(0) + 4 = 4. Do đó ∇f = 0i + 4j."
  },
  {
    id: 56,
    category: "Deep Learning",
    question: "Câu 56. Trường hợp nào sau đây khi khởi tạo trọng số sẽ khiến mạng nơ-ron KHÓ đạt được độ chính xác cao trong tương lai?",
    options: [
      "A. Đảo ngẫu nhiên dữ liệu khi bắt đầu mỗi epoch",
      "B. Khởi tạo tất cả bộ tham số bằng 0",
      "C. Sử dụng momentum",
      "D. Sử dụng Dropout"
    ],
    correctIndex: 1,
    explanation: "Khởi tạo tất cả trọng số bằng 0 gây hiện tượng 'đối xứng hoán vị' (symmetry breaking failure). Tất cả nơ-ron nhận gradient giống nhau và cập nhật như nhau ở mọi epoch, khiến mạng bị suy biến thành 1 nơ-ron duy nhất."
  },
  {
    id: 70,
    category: "Deep Learning",
    question: "Câu 70. Khi sử dụng câu lệnh nn.CrossEntropyLoss trong PyTorch, bạn nên đưa gì vào đối số đầu tiên?",
    options: [
      "A. Logits do lớp cuối cùng của mạng tạo ra",
      "B. Vector one-hot biểu diễn các lớp mục tiêu",
      "C. Xác suất sau khi áp dụng softmax",
      "D. Log-xác suất sau khi áp dụng log_softmax"
    ],
    correctIndex: 0,
    explanation: "nn.CrossEntropyLoss trong PyTorch nhận trực tiếp giá trị Logits (chưa qua Softmax), vì bên trong hàm này đã tự động kết hợp LogSoftmax và NLLLoss để đảm bảo độ chính xác số học."
  },
  {
    id: 73,
    category: "Computer Vision",
    question: "Câu 73. Trong khối Identity Block của ResNet, phép toán kết nối tắt (Skip connection) được thực hiện như thế nào?",
    options: [
      "A. Kết nối tắt ở dòng khởi tạo đầu tiên",
      "B. Kết nối tắt nằm trong BatchNorm",
      "C. Không có cơ chế kết nối tắt",
      "D. Phép cộng Add()([X_shortcut, X]) trước hàm kích hoạt ReLU cuối"
    ],
    correctIndex: 3,
    explanation: "Identity connection của ResNet cộng trực tiếp tensor ban đầu X_shortcut với tensor sau tích chập: Add()([X_shortcut, X]) rồi mới qua hàm kích hoạt ReLU cuối cùng."
  },
  {
    id: 75,
    category: "Computer Vision",
    question: "Câu 75. Trong phần bộ giải mã (decoder) của mạng U-Net, thao tác kết nối tắt (skip connection) phù hợp nhất là gì?",
    options: [
      "A. Phép nối (Concatenation) dọc theo chiều batch",
      "B. Phép nối (Concatenation) dọc theo chiều kênh (channel dimension)",
      "C. Phép cộng element-wise",
      "D. Phép nhân element-wise"
    ],
    correctIndex: 1,
    explanation: "U-Net kết hợp đặc trưng từ encoder với decoder bằng phép nối tensor (Concatenation) dọc theo trục số kênh (channel axis), giúp giữ nguyên độ phân giải không gian và tích hợp thông tin ngữ cảnh đa mức."
  },
  {
    id: 80,
    category: "Machine Learning",
    question: "Câu 80. Cho Giá trị kỳ vọng: [15, 17, 10, 26, 14, 12, 11, 13] và Giá trị thực tế: [12, 19, 15, 24, 13, 14, 8, 11]. Hàm mất mát MSE là bao nhiêu?",
    options: [
      "A. 8.5",
      "B. 6.5",
      "C. 5.5",
      "D. 7.5"
    ],
    correctIndex: 3,
    explanation: "Bình phương sai lệch: (15-12)² + (17-19)² + (10-15)² + (26-24)² + (14-13)² + (12-14)² + (11-8)² + (13-11)² = 9 + 4 + 25 + 4 + 1 + 4 + 9 + 4 = 60. MSE = 60 / 8 = 7.5."
  },
  {
    id: 83,
    category: "Clustering",
    question: "Câu 83. Một điểm p thuộc cụm C1 có khoảng cách trung bình nội cụm a(p) = 0.35. Khoảng cách trung bình đến cụm C2 là 0.60, đến cụm C3 là 0.45. Silhouette Coefficient s(p) là bao nhiêu?",
    options: [
      "A. 0.0",
      "B. 0.222",
      "C. 0.125",
      "D. 0.308"
    ],
    correctIndex: 1,
    explanation: "Cụm lân cận gần nhất là C3 vì d(p, C3) = 0.45 < 0.60 ⇒ b(p) = 0.45. Silhouette: s(p) = (b(p) - a(p)) / max(a(p), b(p)) = (0.45 - 0.35) / max(0.35, 0.45) = 0.10 / 0.45 ≈ 0.222."
  },
  {
    id: 89,
    category: "Evaluation",
    question: "Câu 89. Hệ thống phát hiện các gói tin chứa mối đe dọa (lớp hiếm). Yêu cầu không được bỏ sót bất kỳ gói đe dọa nào. Độ đo quan trọng nhất là gì?",
    options: [
      "A. Accuracy",
      "B. F1",
      "C. Recall",
      "D. Precision"
    ],
    correctIndex: 2,
    explanation: "Không được bỏ sót bất kỳ mối đe dọa nào có nghĩa là False Negative (FN) phải tối thiểu hóa về 0. Độ đo trực tiếp phản ánh điều này là Recall = TP / (TP + FN)."
  },
  {
    id: 94,
    category: "Linear Algebra",
    question: "Câu 94. Cho vector w1 = [0.8, 0.6, 0.0, 0.2] và 3 vector w2=[0.9, 0.5, 0.1, 0.3], w3=[1.0, 0.1, 0.0, 0.0], w4=[0.0, 0.1, 0.9, 0.3]. Từ nào gần nhất với w1 theo Cosine Similarity?",
    options: [
      "A. Có nhiều hơn một từ",
      "B. w3",
      "C. w4",
      "D. w2"
    ],
    correctIndex: 3,
    explanation: "Tích vô hướng w1 · w2 = 0.8(0.9) + 0.6(0.5) + 0 + 0.2(0.3) = 1.08. Độ dài |w1| = √(0.64+0.36+0+0.04) = √1.04 ≈ 1.0198. |w2| = √(0.81+0.25+0.01+0.09) = √1.16 ≈ 1.077. Cosine(w1, w2) = 1.08 / (1.0198 × 1.077) ≈ 0.98. Đây là giá trị lớn nhất so với w3 (0.84) và w4 (0.12) ⇒ w2 gần nhất."
  },
  {
    id: 100,
    category: "Machine Learning",
    question: "Câu 100. Mô hình SVM có vector trọng số w = [2, -3] và độ lệch b = 1. Dự đoán nhãn cho điểm dữ liệu (x1, x2) = (1, 2) là gì?",
    options: [
      "A. Không xác định được",
      "B. Không phân loại",
      "C. +1",
      "D. -1"
    ],
    correctIndex: 3,
    explanation: "Tính hàm phân tách: o = w1·x1 + w2·x2 + b = 2(1) + (-3)(2) + 1 = 2 - 6 + 1 = -3. Vì o < 0, theo nguyên tắc phân lớp của SVM y = sign(w^T x + b), nhãn được dự đoán là -1."
  }
,
{
  "id": 101,
  "category": "Computer Vision",
  "question": "Câu 101 (VAIC 2026). Những độ đo nào sau đây được sử dụng phổ biến nhất để đánh giá chất lượng của mô hình phát hiện vật thể (Object Detection) như YOLO hay Faster R-CNN?",
  "options": [
    "A. Mean Average Precision (mAP)",
    "B. Peak Signal-to-Noise Ratio (PSNR)",
    "C. Structural Similarity Index (SSIM)",
    "D. Mean Squared Error (MSE)"
  ],
  "correctIndex": 0,
  "explanation": "Trong bài toán phát hiện vật thể (Object Detection), mô hình phải đồng thời định vị (Bounding Box qua IoU) và phân loại lớp vật thể. Độ đo chuẩn mực toàn cầu là mAP (Mean Average Precision), tính diện tích dưới đường cong Precision-Recall trung bình trên tất cả các lớp vật thể ở các ngưỡng IoU khác nhau (ví dụ mAP@0.5 hoặc mAP@[0.5:0.95]). Ngược lại, PSNR và SSIM dùng cho phục chế ảnh (Super-resolution, Denoising), còn MSE dùng cho bài toán hồi quy (Regression)."
},
{
  "id": 102,
  "category": "NLP & LLM",
  "question": "Câu 102 (VAIC 2026). Trong kiến trúc Transformer, nếu sử dụng $\\text{softmax}(QK^T)$ thay vì $\\text{softmax}\\left(\\frac{QK^T}{\\sqrt{d}}\\right)$, những hiện tượng bất lợi nào có thể xuất hiện khi số chiều $d$ lớn?",
  "options": [
    "A. Hàm softmax quá sắc nhọn, gradient bị triệt tiêu (vanishing) và sự chú ý bị bão hòa vào một số ít token",
    "B. Số lượng tham số học được của mô hình bị bùng nổ tăng gấp đôi",
    "C. Độ phức tạp tính toán bị tăng từ $\\mathcal{O}(N^2)$ lên $\\mathcal{O}(N^3)$",
    "D. Ma trận trọng số Attention mất hoàn toàn tính đối xứng"
  ],
  "correctIndex": 0,
  "explanation": "Khi hai vector $q, k$ có chiều $d$ với các phần tử có phương sai bằng 1, tích vô hướng $q \\cdot k = \\sum_{i=1}^d q_i k_i$ sẽ có phương sai bằng $d$. Khi $d$ rất lớn (ví dụ $d=64$ hoặc $512$), các giá trị tích vô hướng có biên độ rất lớn, khiến hàm softmax bị đẩy vào các vùng cực đoan (gần 0 hoặc gần 1) với phân phối cực nhọn. Tại vùng bão hòa này, đạo hàm của hàm softmax xấp xỉ bằng 0 (triệt tiêu gradient), khiến mô hình học rất chậm hoặc ngừng học. Việc chia cho $\\sqrt{d}$ giúp kéo phương sai trở về 1, ổn định gradient lan truyền ngược."
},
{
  "id": 103,
  "category": "Machine Learning",
  "question": "Câu 103 (VAIC 2026). Một hệ thống gợi ý phim dự đoán mức độ yêu thích của người dùng $U_1$ cho phim $M$ dựa trên lịch sử của 3 người dùng lân cận: $\\text{sim}(U_1, U_2) = 0.9$, $\\text{sim}(U_1, U_3) = 0.6$, $\\text{sim}(U_1, U_4) = 0.3$. Đánh giá thực tế cho phim $M$ lần lượt là $r(U_2, M) = 5$, $r(U_3, M) = 4$, $r(U_4, M) = 2$. Đánh giá dự đoán $\\hat{r}(U_1, M)$ theo trung bình có trọng số là bao nhiêu?",
  "options": [
    "A. 3.667",
    "B. 4.167",
    "C. 4.500",
    "D. 3.833"
  ],
  "correctIndex": 1,
  "explanation": "Áp dụng công thức trung bình có trọng số (Weighted Average):<br>$$\\hat{r} = \\frac{\\sum \\text{sim}(U_1, U_i) \\cdot r(U_i, M)}{\\sum \\text{sim}(U_1, U_i)} = \\frac{0.9 \\times 5 + 0.6 \\times 4 + 0.3 \\times 2}{0.9 + 0.6 + 0.3} = \\frac{4.5 + 2.4 + 0.6}{1.8} = \\frac{7.5}{1.8} = \\frac{25}{6} \\approx 4.167.$$"
},
{
  "id": 104,
  "category": "Machine Learning",
  "question": "Câu 104 (VAIC 2026). Những hạn chế nào liên quan trực tiếp nhất đến việc sử dụng Information Gain trong thuật toán Cây quyết định ID3?",
  "options": [
    "A. Không thể áp dụng cho các bài toán phân loại nhiều lớp",
    "B. Có xu hướng thiên vị (ưu tiên) các thuộc tính có nhiều giá trị khác nhau",
    "C. Luôn tạo ra cây quyết định cân bằng hoàn hảo",
    "D. Phải dùng thuật toán Gradient Descent để tối ưu hóa"
  ],
  "correctIndex": 1,
  "explanation": "Information Gain $IG(S, A) = H(S) - \\sum \\frac{|S_v|}{|S|} H(S_v)$ có nhược điểm chí mạng là thiên vị các thuộc tính có số lượng giá trị phân biệt lớn (ví dụ thuộc tính 'Số CMND' hay 'ID khách hàng'). Nếu chia theo ID, mỗi nhánh con chỉ có 1 mẫu, entropy rơi về 0 khiến $IG$ đạt cực đại, nhưng cây bị overfitting nặng và mất hoàn toàn khả năng khái quát. Thuật toán C4.5 đã khắc phục nhược điểm này bằng cách sử dụng Gain Ratio (chuẩn hóa bằng Split Information)."
},
{
  "id": 105,
  "category": "Deep Learning",
  "question": "Câu 105 (VAIC 2026). Một mô hình huấn luyện có kết quả:<br>• Epoch 10: Train Acc = 82.1%, Val Acc = 80.5%, Val Loss = 0.63<br>• Epoch 20: Train Acc = 90.4%, Val Acc = 87.8%, Val Loss = 0.42<br>• Epoch 30: Train Acc = 97.5%, Val Acc = 84.1%, Val Loss = 0.70<br>Nhận định nào sau đây là chính xác nhất?",
  "options": [
    "A. Mô hình bắt đầu bị quá khớp (overfitting) sau Epoch 20, nên áp dụng Early Stopping gần Epoch 20",
    "B. Epoch 30 là checkpoint tốt nhất để triển khai vì Train Acc đạt cao nhất (97.5%)",
    "C. Mô hình đang bị underfitting vì Train Acc chưa đạt 100%",
    "D. Nên tiếp tục huấn luyện thêm 50 epoch nữa vì Val Loss sẽ tự động giảm sâu"
  ],
  "correctIndex": 0,
  "explanation": "Từ Epoch 20 sang Epoch 30, Train Acc tiếp tục tăng mạnh từ 90.4% lên 97.5%, nhưng Val Acc giảm từ 87.8% xuống 84.1% và Val Loss tăng vọt từ 0.42 lên 0.70. Đây là dấu hiệu kinh điển của Overfitting (mô hình học thuộc dữ liệu huấn luyện nhưng mất khả năng tổng quát hóa trên tập kiểm thử). Do đó, checkpoint tại Epoch 20 (nơi Val Loss đạt cực tiểu 0.42) là tối ưu nhất và kỹ thuật Early Stopping gần Epoch 20 là chuẩn xác."
},
{
  "id": 106,
  "category": "Computer Vision",
  "question": "Câu 106 (VAIC 2026). Một bộ phát hiện vật thể (detector) đạt kết quả: $AP_{\\text{small}} = 0.30$, $AP_{\\text{medium}} = 0.69$, $AP_{\\text{large}} = 0.84$. Hướng cải thiện nào sau đây có khả năng tác động trực tiếp và hiệu quả nhất?",
  "options": [
    "A. Tăng độ phân giải ảnh, bổ sung đặc trưng đa tỉ lệ (FPN) và thu thập thêm dữ liệu chứa vật thể nhỏ",
    "B. Đổi bộ tối ưu hóa từ Adam sang SGD thuần túy sẽ lập tức giải quyết triệt để vấn đề",
    "C. Tăng mạnh hệ số Regularization $L_2$ để làm mờ các vật thể lớn",
    "D. Giảm số lượng lớp tích chập (Conv layers) xuống một nửa để giảm chi phí tính toán"
  ],
  "correctIndex": 0,
  "explanation": "$AP_{\\text{small}} = 0.30$ thấp hơn rất nhiều so với vật thể vừa (0.69) và lớn (0.84) do vật thể nhỏ chiếm rất ít pixel và thông tin bị mất mát sau các lớp Downsampling/Pooling. Ba giải pháp kinh điển và trực tiếp nhất bao gồm: 1. Tăng độ phân giải ảnh đầu vào (giúp vật thể nhỏ có nhiều pixel đặc trưng hơn); 2. Bổ sung Feature Pyramid Network (FPN) để trích xuất đặc trưng đa tỉ lệ từ các tầng nông có độ phân giải cao; 3. Bổ sung dữ liệu và kỹ thuật Data Augmentation chuyên biệt cho vật thể nhỏ (Mosaic, Copy-Paste)."
},
{
  "id": 107,
  "category": "NLP & LLM",
  "question": "Câu 107 (VAIC 2026). Nếu mô hình Word2Vec học tốt mối quan hệ ngữ nghĩa trong không gian vector (Word Embedding), phép toán vector nào sau đây cho kết quả hợp lý nhất?",
  "options": [
    "A. $\\vec{v}(\\text{King}) - \\vec{v}(\\text{Man}) + \\vec{v}(\\text{Woman}) \\approx \\vec{v}(\\text{Queen})$",
    "B. $\\vec{v}(\\text{King}) + \\vec{v}(\\text{Queen}) \\approx \\vec{v}(\\text{Woman})$",
    "C. $\\vec{v}(\\text{Man}) - \\vec{v}(\\text{Woman}) \\approx \\vec{v}(\\text{King})$",
    "D. $\\vec{v}(\\text{Queen}) - \\vec{v}(\\text{King}) \\approx \\vec{v}(\\text{Man})$"
  ],
  "correctIndex": 0,
  "explanation": "Đây là ví dụ nổi tiếng nhất về tính chất tương tự ngữ nghĩa tuyến tính (Semantic Analogy) của Word2Vec (Mikolov et al., 2013). Vector hiệu $\\vec{v}(\\text{King}) - \\vec{v}(\\text{Man})$ mã hóa khái niệm trừu tượng về 'hoàng gia/vương quyền không xét giới tính'. Khi cộng thêm $\\vec{v}(\\text{Woman})$, vector kết quả sẽ nằm gần nhất với vector $\\vec{v}(\\text{Queen})$ theo độ tương đồng Cosine."
},
{
  "id": 108,
  "category": "Computer Vision",
  "question": "Câu 108 (VAIC 2026). Bộ lọc Sobel $3 \\times 3$ có thể được phân tách thành tích ngoài của hai vector $1\\text{D}$:<br>$$\\begin{bmatrix} 1 & 2 & 1 \\\\ 0 & 0 & 0 \\\\ -1 & -2 & -1 \\end{bmatrix} = \\begin{bmatrix} 1 \\\\ 0 \\\\ -1 \\end{bmatrix} \\begin{bmatrix} 1 & 2 & 1 \\end{bmatrix}$$<br>Phát biểu nào sau đây là chính xác?",
  "options": [
    "A. Việc phân tách giúp giảm số phép tính từ 9 xuống 6 phép nhân mỗi pixel, và đây là phép xấp xỉ đạo hàm bậc 1 của Gaussian (Smoothing theo chiều ngang rồi lấy đạo hàm theo chiều dọc)",
    "B. Việc phân tách gây ra hiện tượng biên giả (spurious edge artifacts) do mất mát thông tin",
    "C. Bộ lọc Sobel không thể phân tách được trong không gian thực",
    "D. Phân tách bộ lọc chỉ có tác dụng nén dung lượng bộ nhớ chứ không tăng tốc độ tính toán"
  ],
  "correctIndex": 0,
  "explanation": "Bộ lọc Sobel là một bộ lọc khả tách (Separable Filter) hạng 1. Tách ma trận $3 \\times 3$ thành hai bộ lọc $1\\text{D}$ ($[1, 0, -1]^T$ và $[1, 2, 1]$) giúp giảm số phép nhân tích chập cho mỗi pixel từ $3 \\times 3 = 9$ xuống chỉ còn $3 + 3 = 6$ phép tính (tổng quát với kernel $K \\times K$ giảm từ $K^2$ xuống $2K$). Về bản chất toán học, vector $[1, 2, 1]$ thực hiện làm mịn Gauss nhị thức (Gaussian smoothing), còn $[1, 0, -1]^T$ lấy đạo hàm sai phân trung tâm bậc 1, không hề gây biên giả."
},
{
  "id": 109,
  "category": "Evaluation",
  "question": "Câu 109 (VAIC 2026). Cho ma trận nhầm lẫn (Confusion Matrix) của bài toán phân loại 3 lớp (hàng là nhãn thực tế, cột là nhãn dự đoán):<br>• Lớp A: Dự đoán A=90, B=8, C=2<br>• Lớp B: Dự đoán A=15, B=70, C=15<br>• Lớp C: Dự đoán A=3, B=12, C=85<br>Nếu chỉ được thu thập thêm dữ liệu cho MỘT lớp để cải thiện hiệu năng tổng thể, lựa chọn nào hợp lý nhất?",
  "options": [
    "A. Lớp A vì có số mẫu dự đoán đúng lớn nhất (90 mẫu)",
    "B. Lớp B vì có tỷ lệ nhầm lẫn cao nhất (Recall chỉ đạt 70%, sai 30 mẫu sang A và C)",
    "C. Lớp C vì có 12 mẫu bị nhầm sang lớp B",
    "D. Cả 3 lớp đều có hiệu năng ngang nhau nên chọn ngẫu nhiên"
  ],
  "correctIndex": 1,
  "explanation": "Xét Recall (Độ thu hồi) thực tế của từng lớp:<br>• Lớp A: $\\text{Recall}_A = 90 / (90+8+2) = 90 / 100 = 90\\%$ (chỉ sai 10 mẫu).<br>• Lớp C: $\\text{Recall}_C = 85 / (3+12+85) = 85 / 100 = 85\\%$ (chỉ sai 15 mẫu).<br>• Lớp B: $\\text{Recall}_B = 70 / (15+70+15) = 70 / 100 = 70\\%$ (bị sai tới 30 mẫu sang A và C).<br>Lớp B có tỷ lệ lỗi cao nhất và là nút thắt cổ chai làm giảm hiệu năng của toàn bộ hệ thống. Do đó, ưu tiên bổ sung dữ liệu cho lớp B sẽ đem lại cải thiện lớn nhất cho mô hình."
},
{
  "id": 110,
  "category": "Evaluation",
  "question": "Câu 110 (VAIC 2026). Cho ma trận nhầm lẫn nhị phân (hàng là Thực tế, cột là Dự đoán):<br>• Thực tế Dương (P): Dự đoán P = 90 (TP), Dự đoán N = 10 (FN)<br>• Thực tế Âm (N): Dự đoán P = 20 (FP), Dự đoán N = 80 (TN)<br>Precision của lớp dương tính bằng bao nhiêu (làm tròn 3 chữ số thập phân)?",
  "options": [
    "A. 0.818",
    "B. 0.900",
    "C. 0.850",
    "D. 0.750"
  ],
  "correctIndex": 0,
  "explanation": "Độ chuẩn xác (Precision) của lớp dương tính là tỉ lệ các mẫu thực sự dương tính trong tổng số các mẫu mà mô hình dự đoán là dương:<br>$$\\text{Precision} = \\frac{TP}{TP + FP} = \\frac{90}{90 + 20} = \\frac{90}{110} = \\frac{9}{11} \\approx 0.81818... \\approx 0.818.$$"
},
{
  "id": 111,
  "category": "Machine Learning",
  "question": "Câu 111 (VAIC 2026). Trong một bộ dữ liệu phân loại nhị phân, có đúng 8 mẫu dương và 8 mẫu âm. Entropy Shannon của bộ dữ liệu này bằng bao nhiêu?",
  "options": [
    "A. 0.0 bit",
    "B. 0.5 bit",
    "C. 1.0 bit",
    "D. 2.0 bit"
  ],
  "correctIndex": 2,
  "explanation": "Tổng số mẫu $N = 8 + 8 = 16$. Xác suất mỗi lớp là $p_+ = 8/16 = 0.5$ và $p_- = 8/16 = 0.5$.<br>Áp dụng công thức Entropy Shannon cơ số 2:<br>$$H(S) = -p_+ \\log_2(p_+) - p_- \\log_2(p_-) = -0.5 \\log_2(0.5) - 0.5 \\log_2(0.5) = -0.5(-1) - 0.5(-1) = 0.5 + 0.5 = 1.0\\text{ bit}.$$<br>Khi hai lớp cân bằng tuyệt đối, mức độ hỗn loạn (bất định) đạt cực đại và bằng đúng 1 bit."
},
{
  "id": 112,
  "category": "NLP & LLM",
  "question": "Câu 112 (VAIC 2026). Trong bài toán phân loại cảm xúc văn bản tiếng Việt (Sentiment Analysis: Tích cực / Tiêu cực), phương pháp nào sau đây thường đem lại hiệu năng vượt trội và độ chính xác cao nhất?",
  "options": [
    "A. TF-IDF kết hợp Logistic Regression",
    "B. Word2Vec kết hợp Support Vector Machine (SVM)",
    "C. Fine-tuning mô hình ngôn ngữ ngữ cảnh tiền huấn luyện PhoBERT",
    "D. Bag of Words (BoW) kết hợp Naive Bayes"
  ],
  "correctIndex": 2,
  "explanation": "PhoBERT là mô hình ngôn ngữ dựa trên kiến trúc RoBERTa được tiền huấn luyện chuyên sâu trên kho ngữ liệu tiếng Việt khổng lồ (20GB văn bản). Nhờ cơ chế Self-Attention đa tầng hai chiều và phân tách từ theo âm tiết/từ ghép tiếng Việt (RDRSegmenter), PhoBERT nắm bắt được ngữ cảnh phức tạp, từ đồng nghĩa, đảo ngữ và sắc thái cảm xúc tốt hơn rất nhiều so với các mô hình biểu diễn tĩnh (Word2Vec, TF-IDF, BoW)."
},
{
  "id": 113,
  "category": "Computer Vision",
  "question": "Câu 113 (VAIC 2026). Mô hình Vision Transformer (ViT) nhận ảnh kích thước $224 \\times 224$ với kích thước patch là $16 \\times 16$. Nếu kích thước patch tăng lên thành $32 \\times 32$, độ phức tạp tính toán của cơ chế Self-Attention thay đổi như thế nào?",
  "options": [
    "A. Giảm xấp xỉ 4 lần",
    "B. Giảm xấp xỉ 16 lần",
    "C. Tăng xấp xỉ 4 lần",
    "D. Tăng xấp xỉ 16 lần"
  ],
  "correctIndex": 1,
  "explanation": "Số lượng patches $N$ được tính bằng diện tích ảnh chia cho diện tích mỗi patch:<br>• Với patch $16 \\times 16$: $N_1 = \\frac{224}{16} \\times \\frac{224}{16} = 14 \\times 14 = 196$ tokens.<br>• Với patch $32 \\times 32$: $N_2 = \\frac{224}{32} \\times \\frac{224}{32} = 7 \\times 7 = 49$ tokens.<br>Số token giảm đi $\\frac{196}{49} = 4$ lần. Vì độ phức tạp tính toán của ma trận Attention $QK^T$ tỷ lệ bậc hai với số lượng token $\\mathcal{O}(N^2)$, nên độ phức tạp giảm đi:<br>$$\\left(\\frac{N_1}{N_2}\\right)^2 = 4^2 = 16\\text{ lần}.$$"
},
{
  "id": 114,
  "category": "Machine Learning",
  "question": "Câu 114 (VAIC 2026). Vì sao một Cây quyết định (Decision Tree) được phát triển quá sâu thường hoạt động rất kém trên tập kiểm thử (Test Set), dù đạt độ chính xác gần 100% trên tập huấn luyện?",
  "options": [
    "A. Cây học thuộc cả các điểm nhiễu (noise) và dao động ngẫu nhiên trong tập huấn luyện (Overfitting, phương sai cao)",
    "B. Cây càng sâu thì luôn có thiên lệch (bias) cao hơn cây nông",
    "C. Cây quyết định về bản chất không thể phân tách được các ranh giới phi tuyến",
    "D. Hàm Entropy không còn xác định được khi cây vượt quá 5 tầng"
  ],
  "correctIndex": 0,
  "explanation": "Khi cây quyết định phát triển không kiểm soát (không giới hạn độ sâu tối đa max_depth hay điều kiện dừng min_samples_split), các nhánh sẽ tiếp tục phân chia cho tới khi mỗi nút lá chỉ chứa 1-2 điểm dữ liệu. Khi đó mô hình học thuộc toàn bộ nhiễu và các ngoại lệ cục bộ (High Variance, Low Bias), dẫn đến ranh giới quyết định bị chia cắt manh mún và mất khả năng khái quát hóa. Để khắc phục, cần áp dụng tỉa cành (pruning) hoặc giới hạn độ sâu cây."
},
{
  "id": 115,
  "category": "Evaluation",
  "question": "Câu 115 (VAIC 2026). Một hệ thống gợi ý Top-5 sản phẩm cho người dùng đưa ra danh sách: $[A, B, C, D, E]$. Thực tế người dùng quan tâm đến danh sách các sản phẩm: $[B, C, F, G, Z]$. Giá trị của $\\text{Precision@5}$ và $\\text{Recall@5}$ lần lượt là bao nhiêu?",
  "options": [
    "A. 0.4 ; 0.4",
    "B. 0.4 ; 0.5",
    "C. 0.2 ; 0.4",
    "D. 0.5 ; 0.4"
  ],
  "correctIndex": 0,
  "explanation": "Tập gợi ý Top-5: $R_5 = \\{A, B, C, D, E\\}$ ($|R_5| = 5$).<br>Tập thực tế quan tâm (Relevant): $Rel = \\{B, C, F, G, Z\\}$ ($|Rel| = 5$).<br>Số sản phẩm liên quan xuất hiện trong Top-5 là phần giao: $R_5 \\cap Rel = \\{B, C\\} \\implies 2$ sản phẩm.<br>• $\\text{Precision@5} = \\frac{|R_5 \\cap Rel|}{5} = \\frac{2}{5} = 0.4$.<br>• $\\text{Recall@5} = \\frac{|R_5 \\cap Rel|}{|Rel|} = \\frac{2}{5} = 0.4$."
},
{
  "id": 116,
  "category": "Machine Learning",
  "question": "Câu 116 (VAIC 2026). Nếu một nút trong Cây quyết định (Decision Tree) có giá trị Entropy bằng 0, những kết luận nào sau đây là hoàn toàn chính xác?",
  "options": [
    "A. Tất cả các mẫu trong nút đó đều thuộc cùng một lớp (nút thuần khiết), và Information Gain của mọi phép chia tiếp theo tại nút này đều bằng 0",
    "B. Các mẫu trong nút được phân bố đồng đều 50-50 giữa các lớp",
    "C. Nút đó bắt buộc phải là nút gốc (Root node) của cây",
    "D. Cây quyết định đang bị lỗi tràn số học"
  ],
  "correctIndex": 0,
  "explanation": "Theo định nghĩa Entropy Shannon $H = -\\sum p_i \\log_2 p_i$, $H = 0$ khi và chỉ khi có một lớp có xác suất $p=1$ và các lớp còn lại có $p=0$. Điều này chứng minh nút đó là 'nút thuần khiết' (Pure node) - mọi mẫu dữ liệu bên trong đều mang cùng một nhãn phân loại. Vì trạng thái đã hoàn toàn thuần khiết (không còn sự bất định nào), không thể thực hiện thêm bất kỳ phép chia nào để giảm entropy thêm được nữa, tức Information Gain của mọi phép chia tại nút lá này đều bằng 0."
},
{
  "id": 117,
  "category": "Machine Learning",
  "question": "Câu 117 (VAIC 2026). Một nền tảng phim vừa tải lên một bộ phim mới toanh chưa có bất kỳ người dùng nào đánh giá hay xem (rating = null), nhưng có đầy đủ siêu dữ liệu: Thể loại, Đạo diễn, Diễn viên, Mô tả tóm tắt nội dung. Phương pháp gợi ý nào vẫn có thể hoạt động hiệu quả để giải quyết hiện tượng này?",
  "options": [
    "A. User-based Collaborative Filtering",
    "B. Item-based Collaborative Filtering",
    "C. Content-based Filtering (Lọc dựa trên nội dung)",
    "D. Matrix Factorization (Phân rã ma trận SVD)"
  ],
  "correctIndex": 2,
  "explanation": "Đây là bài toán Khởi đầu lạnh cho vật phẩm (Item Cold-Start Problem) kinh điển. Các phương pháp Lọc cộng tác (Collaborative Filtering và Matrix Factorization SVD) đều dựa hoàn toàn vào ma trận tương tác User-Item (ratings/views); khi vật phẩm mới chưa có lượt tương tác nào, các phương pháp này hoàn toàn tê liệt. Trái lại, Content-based Filtering biểu diễn vật phẩm bằng vector đặc trưng từ siêu dữ liệu (Thể loại, Diễn viên qua TF-IDF / Embedding) và so khớp với hồ sơ sở thích của người dùng qua Cosine Similarity, do đó hoạt động hoàn hảo ngay khi vật phẩm vừa ra mắt."
},
{
  "id": 118,
  "category": "Machine Learning",
  "question": "Câu 118 (VAIC 2026). Trong thuật toán $k$-Nearest Neighbors ($k$-NN), điều gì có khả năng cao nhất xảy ra khi ta thiết lập giá trị $k$ rất nhỏ, cụ thể là $k = 1$?",
  "options": [
    "A. Mô hình trở nên mượt mà hơn và miễn nhiễm hoàn toàn với nhiễu",
    "B. Mô hình có thiên lệch thấp (Low Bias) nhưng phương sai rất cao (High Variance, dễ Overfitting)",
    "C. Mô hình bị thiên lệch rất cao (High Bias) và Underfitting",
    "D. Thuật toán tự động chuyển đổi thành Hồi quy tuyến tính"
  ],
  "correctIndex": 1,
  "explanation": "Với $k=1$, mô hình chỉ gán nhãn dựa trên đúng 1 điểm dữ liệu gần nhất trong không gian huấn luyện. Do đó, trên tập huấn luyện độ chính xác đạt 100% (Bias = 0), nhưng biên phân lớp sẽ bị bẻ ngoằn ngoèo, cực kỳ nhạy cảm với từng điểm nhiễu hoặc điểm ngoại lai (Outlier). Khi áp dụng vào tập kiểm thử, chỉ một biến động nhỏ cũng làm thay đổi dự đoán, thể hiện tính chất Phương sai cực cao (High Variance - Overfitting). Tăng $k$ sẽ làm biên quyết định phẳng hơn, tăng Bias nhưng giảm Variance."
},
{
  "id": 119,
  "category": "Computer Vision",
  "question": "Câu 119 (VAIC 2026). Khi huấn luyện trên một tập dữ liệu có quy mô tương đối nhỏ, nhận định nào sau đây là đúng nhất khi so sánh Vision Transformer (ViT) với Convolutional Neural Network (CNN) có cùng lượng tham số?",
  "options": [
    "A. ViT có Inductive Bias (thiên kiến quy nạp) yếu hơn CNN nên phụ thuộc nặng nề vào Data Augmentation hoặc Pretraining; CNN tận dụng dữ liệu nhỏ hiệu quả hơn",
    "B. ViT luôn luôn vượt trội hơn CNN trong mọi kịch bản dữ liệu nhỏ mà không cần bất kỳ kỹ thuật bổ trợ nào",
    "C. CNN không có khả năng trích xuất đặc trưng cục bộ trên tập dữ liệu nhỏ",
    "D. ViT không thể huấn luyện được bằng thuật toán lan truyền ngược"
  ],
  "correctIndex": 0,
  "explanation": "Mạng CNN được tích hợp sẵn hai Inductive Bias (thiên kiến quy nạp) vật lý cực mạnh: Tính cục bộ (Locality) (các pixel gần nhau có quan hệ mật thiết) và Tính bất biến tịnh tiến (Translation Invariance) (bộ lọc quét đồng nhất khắp ảnh). Nhờ đó, CNN học rất nhanh và ổn định ngay cả với tập dữ liệu nhỏ. Trong khi đó, ViT coi ảnh như chuỗi các patches tự do liên kết qua Global Self-Attention và hoàn toàn thiếu hai thiên kiến này, đòi hỏi phải được huấn luyện trước (Pretraining) trên các bộ dữ liệu khổng lồ (JFT-300M, ImageNet-21k) hoặc dùng kỹ thuật tăng cường dữ liệu mạnh để tự học các cấu trúc không gian."
},
{
  "id": 120,
  "category": "Evaluation",
  "question": "Câu 120 (VAIC 2026). Trong bài toán phân loại đa lớp (Multi-class Classification) với giả thiết mỗi mẫu chỉ thuộc duy nhất một lớp (Single-label), khi áp dụng phương pháp tính trung bình vi mô (Micro-averaging), đẳng thức nào sau đây luôn luôn đúng?",
  "options": [
    "A. F1-score = Accuracy, nhưng Recall ≠ Precision",
    "B. Accuracy ≥ F1-score ≥ Recall ≥ Precision",
    "C. F1-score = Accuracy = Recall = Precision",
    "D. F1-score ≠ Accuracy, nhưng Recall = Precision"
  ],
  "correctIndex": 2,
  "explanation": "Trong bài toán phân loại đơn nhãn (mỗi mẫu thuộc đúng 1 lớp):<br>Tổng các mẫu phân loại đúng của tất cả các lớp là $\\sum TP_i$. Khi một mẫu thuộc lớp $A$ bị mô hình dự đoán nhầm thành lớp $B$, nó đồng thời tạo ra một False Negative cho lớp $A$ ($FN_A$) và một False Positive cho lớp $B$ ($FP_B$). Do đó, trên toàn bộ tập dữ liệu: $\\sum FP_i = \\sum FN_i = \\text{Tổng số mẫu bị phân loại sai}$.<br>Khi tính Micro-average:<br>• $\\text{Micro-Precision} = \\frac{\\sum TP_i}{\\sum TP_i + \\sum FP_i} = \\frac{\\text{Số mẫu đúng}}{\\text{Tổng số mẫu}} = \\text{Accuracy}$.<br>• $\\text{Micro-Recall} = \\frac{\\sum TP_i}{\\sum TP_i + \\sum FN_i} = \\text{Micro-Precision} = \\text{Accuracy}$.<br>• $\\text{Micro-F1} = 2 \\times \\frac{\\text{Precision} \\times \\text{Recall}}{\\text{Precision} + \\text{Recall}} = \\text{Accuracy}$.<br>Vậy F1-score = Accuracy = Recall = Precision."
}
];
