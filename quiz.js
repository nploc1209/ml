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
];
