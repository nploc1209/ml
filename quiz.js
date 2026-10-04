// quiz.js - Complete Exam Simulator with 120 Authentic Questions (100 VAIO 2025 & 20 VAIC 2026)

const QUIZ_DATA = [
  {
    "id": 1,
    "category": "Deep Learning",
    "question": "Câu 1. Trong mạng nơ-ron, chuẩn hóa lô (Batch Normalization) thường được đặt ở đâu?",
    "options": [
      "A. Trước hàm kích hoạt ReLU và sau lớp tuyến tính (Linear)",
      "B. Sau ReLU",
      "C. Sau lớp bỏ ngẫu nhiên (dropout)",
      "D. Trước lớp đầu vào (input layer)"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Chuẩn hóa lô (Batch Normalization) chuẩn hóa dữ liệu về mean=0, std=1 rồi áp dụng phép biến đổi tuyến tính với 2 tham số học được $(\\gamma, \\beta)$. Thứ tự chuẩn là **Linear → BatchNorm → ReLU**.\n• **Vì sao các đáp án khác sai:**\n- *Sau ReLU (B sai):* Các giá trị âm bị ép về 0 khiến phân phối bị lệch đỉnh 0 và dẫn tới gradient thưa thớt (sparse gradient), làm chậm quá trình học.\n- *Sau Dropout (C sai):* Dropout ngẫu nhiên triệt tiêu neuron làm nhiễu loạn thống kê mean/variance của batch.\n- *Trước Input layer (D sai):* Tiền xử lý dữ liệu đầu vào thường dùng mean/std cứng của toàn bộ tập dữ liệu (như ImageNet) thay vì tính động theo từng mini-batch."
  },
  {
    "id": 2,
    "category": "Computer Vision",
    "question": "Câu 2. Thành phần nào sau đây là một tham số có thể học trong một lớp tích chập?",
    "options": [
      "A. Kích thước của dữ liệu đầu vào",
      "B. Các giá trị trong bộ lọc",
      "C. Kích thước bước nhảy",
      "D. Kích thước padding"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Trong lớp tích chập (Conv2D), các giá trị trong bộ lọc (filter/kernel weights) là **tham số có thể học được (learnable parameters)** thông qua thuật toán lan truyền ngược (backpropagation) để tối ưu hóa hàm mất mát.\n• **Vì sao các đáp án khác sai:** Kích thước đầu vào, bước nhảy (stride), và kích thước padding (A, C, D) đều là các **siêu tham số (hyperparameters)** do người dùng thiết lập cố định trước khi huấn luyện."
  },
  {
    "id": 3,
    "category": "Deep Learning",
    "question": "Câu 3. Nếu mất mát (loss) không giảm sau 5 vòng lặp (epoch) đầu tiên dù tỷ lệ học là 0.001, bạn nên làm gì\nđầu tiên?",
    "options": [
      "A. Dừng lại và chọn mô hình khác",
      "B. Kiểm tra lại quy trình dữ liệu (data pipeline), tăng cường dữ liệu (augmentation) và bộ tối ưu",
      "C. Tăng tỷ lệ học lên 0.1",
      "D. Tăng số lớp của mô hình"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** 5 epoch đầu tiên là số lượng vòng lặp rất nhỏ. Khi loss không giảm dù $\\text{lr} = 0.001$, bước đầu tiên cần làm là **kiểm tra lại quy trình dữ liệu (data pipeline), tăng cường dữ liệu (augmentation) và bộ tối ưu** (xác minh shape tensor, kiểm tra dữ liệu đã shuffle chưa, nhãn có bị gán sai hay mất cân bằng không).\n• **Vì sao các đáp án khác sai:**\n- *Dừng lại chọn mô hình khác (A sai):* Quá sớm để kết luận mô hình không phù hợp.\n- *Tăng lr lên 0.1 (C sai):* Tăng gấp 100 lần dễ khiến mô hình phân kỳ hoặc dao động mất ổn định.\n- *Tăng số lớp (D sai):* Mô hình phức tạp hơn chỉ làm việc hội tụ ban đầu khó khăn hơn."
  },
  {
    "id": 4,
    "category": "NLP & LLM",
    "question": "Câu 4. Hạn chế lớn nhất khi tinh chỉnh (fine-tune) toàn bộ mô hình GPT là gì?",
    "options": [
      "A. Không dùng được tiếng Việt",
      "B. Cần tài nguyên tính toán rất lớn",
      "C. Không dùng được API",
      "D. Không sinh được ảnh"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Các mô hình GPT có từ hàng tỷ đến hàng trăm tỷ tham số. Việc tinh chỉnh toàn bộ (Full Fine-tuning) đòi hỏi **tài nguyên tính toán khổng lồ (bộ nhớ GPU/TPU, thời gian và chi phí huấn luyện rất lớn)**.\n• **Vì sao các đáp án khác sai:**\n- GPT hoàn toàn xử lý tốt tiếng Việt khi có dữ liệu/prompt phù hợp (A sai).\n- Mô hình fine-tune xong vẫn được triển khai và gọi qua API bình thường (C sai).\n- Khả năng sinh ảnh là tác vụ đa phương thức riêng (như DALL-E), không liên quan đến fine-tune văn bản (D sai)."
  },
  {
    "id": 5,
    "category": "Computer Vision",
    "question": "Câu 5. Khi muốn trích xuất đặc trưng (features) từ ResNet50, bạn nên làm gì?",
    "options": [
      "A. Sử dụng bộ tối ưu Adam",
      "B. Sử dụng đầu ra từ lớp gần cuối (ví dụ: avgpool, penultimate, …)",
      "C. Thêm nhiều lớp bỏ ngẫu nhiên (dropout)",
      "D. Thêm lớp kết nối đầy đủ siêu tốc (fully connected) mới"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Để trích xuất đặc trưng (feature extraction) từ ResNet50, ta lấy đầu ra từ **lớp áp cuối (penultimate layer) như `avgpool` (vector 2048 chiều)**. Đầu ra này đại diện cô đọng và trừu tượng nhất cho toàn bộ ảnh đầu vào, rất lý tưởng cho phân loại mới hoặc truy xuất ảnh tương đồng.\n• **Vì sao các đáp án khác sai:** Bộ tối ưu Adam (A), Dropout (C), hay thêm Fully Connected (D) là các bước huấn luyện, không phải thao tác trích xuất vector đặc trưng từ mô hình có sẵn."
  },
  {
    "id": 6,
    "category": "NLP & LLM",
    "question": "Câu 6. Giả sử bạn đang xây dựng một mô hình phân loại cảm xúc văn bản (positive/negative) bằng cách sử dụng biểu diễn Bag-of-Words (BoW) và PyTorch (phiên bản ≥ 1.6).\n\nĐoạn mã tiền xử lý:\n```python\nfrom sklearn.feature_extraction.text import CountVectorizer\nfrom sklearn.model_selection import train_test_split\nimport torch\nimport torch.nn as nn\nimport torch.optim as optim\n\ntexts = [\"I love this movie\", \"I hate this product\", \"Amazing quality\", \"Terrible service\"]\nlabels = [1, 0, 1, 0]\nvectorizer = CountVectorizer()\nX = vectorizer.fit_transform(texts).toarray()\ny = torch.tensor(labels)\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)\nX_train = torch.tensor(X_train, dtype=torch.float32)\n```\n\nPhương án nào sau đây là phần mã đúng để huấn luyện mô hình phân loại nhị phân đơn giản với biểu diễn BoW, một tầng tuyến tính và hàm loss phù hợp?",
    "options": [
      "A. model = nn.Linear(X_train.shape[1], 1); loss_fn = nn.BCEWithLogitsLoss(); outputs = model(X_train).squeeze(); loss = loss_fn(outputs, y_train.float())",
      "B. model = nn.Sequential(nn.Linear(X_train.shape[1], 10), nn.ReLU(), nn.Linear(10, 2)); loss_fn = nn.NLLLoss()",
      "C. model = nn.Linear(X_train.shape(1), 2); loss_fn = nn.CrossEntropyLoss() (sai cú pháp .shape(1))",
      "D. model = nn.Linear(X_train.shape[1], 1); loss_fn = nn.MSELoss() (dùng MSE cho phân loại nhị phân)"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Với phân loại nhị phân (nhãn 0/1) và một tầng tuyến tính đầu ra 1 chiều `nn.Linear(X_train.shape[1], 1)`, hàm mất mát chuẩn mực trong PyTorch là `nn.BCEWithLogitsLoss()` (tích hợp sẵn Sigmoid và Binary Cross-Entropy ổn định số học). Đầu ra cần `.squeeze()` để khớp chiều với `y_train.float()`.\n• **Vì sao các đáp án khác sai:**\n- (B sai): `nn.NLLLoss()` yêu cầu đầu vào là log-xác suất (LogSoftmax), không dùng trực tiếp cho logits.\n- (C sai): Sai cú pháp `X_train.shape(1)` (shape là tuple, không phải hàm gọi).\n- (D sai): `nn.MSELoss()` không phù hợp cho bài toán phân loại nhị phân vì dễ gây triệt tiêu gradient."
  },
  {
    "id": 7,
    "category": "Machine Learning",
    "question": "Câu 7. Điều nào sau đây là ĐÚNG khi so sánh SVM (support vector machine) với k-NN?",
    "options": [
      "A. Cả hai phương pháp chỉ được sử dụng cho các bài toán phân loại (không phải hồi quy).",
      "B. Huấn luyện SVM có thể tốn kém về mặt tính toán, đặc biệt đối với các bộ dữ liệu lớn, trong khi huấn\nluyện k-NN không liên quan đến quy trình huấn luyện rõ ràng.",
      "C. SVM luôn tốt hơn k-NN trên mọi tập dữ liệu.",
      "D. Dự đoán của cả hai phương pháp đều chậm vì cả hai đều cần xử lý tất cả các mẫu dữ liệu huấn luyện để\ndự đoán mẫu dữ liệu mới."
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Huấn luyện SVM phải giải bài toán tối ưu bậc hai lồi với ma trận kernel độ phức tạp $\\mathcal{O}(N^2)$ đến $\\mathcal{O}(N^3)$, rất tốn kém khi dữ liệu lớn. Ngược lại, $k$-NN là phương pháp 'học lười' (lazy learning/non-parametric), giai đoạn huấn luyện chỉ lưu trữ dữ liệu vào bộ nhớ mà không cần huấn luyện tường minh.\n• **Vì sao các đáp án khác sai:**\n- (A sai): Cả SVM và $k$-NN đều dùng được cho cả phân loại và hồi quy (SVR, $k$-NN regression).\n- (C sai): Theo định lý No Free Lunch, không mô hình nào luôn vượt trội trên mọi tập dữ liệu.\n- (D sai): SVM tuyến tính khi dự đoán chỉ cần một phép nhân vô hướng $w^T x + b$, cực kỳ nhanh và không phụ thuộc số mẫu."
  },
  {
    "id": 8,
    "category": "Machine Learning",
    "question": "Câu 8. Đối với SVM (support vector machine) phi tuyến, để dự đoán, đáp án nào đúng.",
    "options": [
      "A. Cần sử dụng cùng hàm chuyển đổi tương tự với giai đoạn huấn luyện",
      "B. Sử dụng một hàm chuyển đổi khác với giai đoạn huấn luyện",
      "C. SVM phi tuyến luôn tốt hơn SVM tuyến tính trong mọi tập dữ liệu",
      "D. Không cần hàm chuyển đổi"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** SVM phi tuyến sử dụng hàm kernel $K(x, z) = \\phi(x)^T \\phi(z)$ để ánh xạ dữ liệu sang không gian đặc trưng mới. Khi dự đoán, mô hình bắt buộc phải **sử dụng cùng hàm chuyển đổi (kernel) tương tự giai đoạn huấn luyện** để đảm bảo tính nhất quán của không gian biểu diễn.\n• **Vì sao các đáp án khác sai:** Dùng hàm khác hoặc không dùng hàm chuyển đổi (B, D) sẽ làm sai lệch hoàn toàn ranh giới quyết định. (C sai) vì SVM phi tuyến không phải lúc nào cũng tốt hơn SVM tuyến tính (dễ bị overfitting nếu dữ liệu phân tách tuyến tính)."
  },
  {
    "id": 9,
    "category": "Computer Vision",
    "question": "Câu 9. Khi sử dụng torchvision.models.resnet18(pretrained = True) trong PyTorch, mục đích chính\nlà gì?",
    "options": [
      "A. Huấn luyện mô hình từ đầu",
      "B. Tăng kích thước lô (batch size)",
      "C. Thử nghiệm mô hình mới",
      "D. Sử dụng trọng số huấn luyện trước (Pre – trained weights) trên ImageNet để trích xuất đặc trưng"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Tham số `pretrained = True` (hoặc `weights='DEFAULT'`) tải các **trọng số đã được huấn luyện trước trên tập dữ liệu ImageNet (1.2 triệu ảnh, 1000 lớp)**. Mục đích chính là tận dụng các đặc trưng thị giác cấp thấp và trung gian đã học để trích xuất đặc trưng hoặc fine-tuning cho bài toán mới.\n• **Vì sao các đáp án khác sai:** (A) Huấn luyện từ đầu tương ứng với `pretrained = False`. (B, C) không liên quan đến việc nạp trọng số."
  },
  {
    "id": 10,
    "category": "Computer Vision",
    "question": "Câu 10. Khi các mô hình phát hiện vật thể hoạt động, chúng thường đề xuất nhiều hộp bao (bounding box)\ncho cùng một đối tượng trong ảnh. Nhiều hộp bao này có thể chồng lấn lên nhau, dẫn đến thông tin dư thừa vì\nmục tiêu của chúng ta là chỉ xác định một hộp bao duy nhất và chính xác nhất cho mỗi đối tượng. Thuật toán\nNon – Maximum Suppression (NMS) được thiết kế để giải quyết vấn đề này. Nó giúp lọc và loại bỏ các hộp\nbao dư thừa, chỉ giữ lại những hộp bao đại diện tốt nhất cho mỗi đối tượng.\nThuật toán NMS gồm các bước như sau:\n- Sắp xếp: Sắp xếp tất cả các hộp bao trong tập 𝑃 theo thứ tự giảm dần của điểm tin cậy (confidence score).\n- Chọn hộp tốt nhất: Chọn hộp bao 𝐻 có điểm tin cậy cao nhất từ tập 𝑃. Hộp bao này được xem là đại diện\ntốt nhất hiện tại.\n- Giữ lại và loại bỏ: Chuyển hộp bao 𝐻 vào danh sách kết quả cuối cùng (gọi là 𝐾) và loại bỏ nó khỏi tập 𝑃.\n- So sánh và loại bỏ chồng lấn:\n+ Tính toán chỉ số Intersection over Union (IoU) giữa hộp 𝐻 (vừa chọn) và tất cả các hộp bao còn lại trong\ntập 𝑃. Chỉ số IoU được tính theo công thức sau:\nDiện tích vùng giao của 2 hộp\nIoU=\nDiện tích vùng hợp của hai hộp\n+ Đối với mỗi hộp bao còn lại trong 𝑃, nếu giá trị IoU của nó với hộp 𝐻 lớn hơn một ngưỡng xác định trước\n(IoU_threshold), thì loại bỏ hộp bao đó khỏi 𝑃. Lý do là vì nó chồng lấn quá nhiều với hộp 𝐻 (vốn có điểm\ntin cậy cao hơn) và được coi là dư thừa cho cùng một đối tượng.\n- Lặp lại: Quay lại Bước 2 và lặp lại quy trình (chọn hộp có điểm tin cậy cao nhất tiếp theo từ 𝑃, thêm vào 𝐾,\nloại bỏ các hộp chồng lấn khỏi 𝑃) cho đến khi tập 𝑃 không còn hộp bao nào.\n- Kết quả: Danh sách 𝐾 sẽ chứa các hộp bao cuối cùng được giữ lại, mỗi hộp đại diện cho một đối tượng\nriêng biệt đã được phát hiện.\nÁp dụng thuật toán NMS với ngưỡng IoU_threshold=0.40 và giả sử tất cả các hộp cùng một lớp và thông\ntin các hộp đã sắp thứ tự theo độ tin cậy (confidence score) như sau:\nTọa độ (𝒙𝟏,𝒚𝟏,𝒙𝟐,𝒚𝟐) (pixel) Độ tin cậy\n𝐵1 (0,0,100,100) 0.95\n(10,10,90,90) 0.90\n𝐵3 (105,105,200,200) 0.85\nNhững hộp nào sẽ được giữ lại?",
    "options": [
      "A. 𝐵1 và 𝐵2",
      "B. Chỉ 𝐵1",
      "C. 𝐵1 và 𝐵3",
      "D. 𝐵2 và 𝐵3"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất thuật toán NMS:**\n1. Sắp xếp theo độ tin cậy: $B_1 (0.95) > B_2 (0.90) > B_3 (0.85)$.\n2. Chọn $B_1$ có điểm cao nhất đưa vào danh sách giữ lại $K = \\{B_1\\}$.\n3. Tính IoU giữa $B_1$ và các hộp còn lại:\n   - $B_1 = (0, 0, 100, 100)$, diện tích $S_1 = 100 \\times 100 = 10000$.\n   - $B_2 = (10, 10, 90, 90)$, diện tích $S_2 = 80 \\times 80 = 6400$. $B_2$ nằm trọn trong $B_1 \\implies \\text{Giao} = 6400$, $\\text{Hợp} = 10000 \\implies \\text{IoU}(B_1, B_2) = 6400 / 10000 = 0.64 > 0.40 \\implies$ **Loại $B_2$**.\n   - $B_3 = (105, 105, 200, 200)$ không giao với $B_1 \\implies \\text{IoU}(B_1, B_3) = 0 \\le 0.40 \\implies$ **Giữ $B_3$**.\n4. Kết quả: Giữ lại $B_1$ và $B_3$."
  },
  {
    "id": 11,
    "category": "Machine Learning",
    "question": "Câu 11. Trong Pandas, phương thức nào dùng để lấy 5 dòng đầu tiên của DataFrame?",
    "options": [
      "A. df.head()",
      "B. df.take(5)",
      "C. df.top()",
      "D. df.first(5)"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Trong thư viện Pandas, phương thức `df.head(n=5)` trả về 5 dòng đầu tiên của DataFrame (mặc định tham số là 5).\n• **Vì sao các đáp án khác sai:** Các hàm `df.top()` và `df.first()` không tồn tại trong cú pháp Pandas; `df.take(5)` dùng để chọn dòng tại vị trí chỉ số cụ thể."
  },
  {
    "id": 12,
    "category": "Machine Learning",
    "question": "Câu 12. Thuật toán học máy nào sau đây là phổ biến và hiệu quả, dựa trên ý tưởng bagging?",
    "options": [
      "A. XGBoost",
      "B. Hồi quy tuyến tính (Linear Regression)",
      "C. Cây quyết định (Decision Tree)",
      "D. Rừng ngẫu nhiên (Random Forest)"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** **Rừng ngẫu nhiên (Random Forest)** là thuật toán tổ hợp điển hình dựa trên ý tưởng **Bagging (Bootstrap Aggregating)**: lấy mẫu tái lập từ tập dữ liệu gốc để huấn luyện song song nhiều cây quyết định độc lập, sau đó lấy biểu quyết đa số (phân loại) hoặc trung bình cộng (hồi quy) để giảm phương sai (variance).\n• **Vì sao các đáp án khác sai:**\n- XGBoost (A) dựa trên kỹ thuật **Boosting** (học tuần tự sửa sai cho mô hình trước).\n- Hồi quy tuyến tính (B) và Cây quyết định đơn lẻ (C) không phải là mô hình tổ hợp."
  },
  {
    "id": 13,
    "category": "Machine Learning",
    "question": "Câu 13. Kỹ thuật nào sau đây được sử dụng để giảm ảnh hưởng của nhiễu và ngoại lệ trong tập dữ liệu?",
    "options": [
      "A. Phân tích thành phần chính (Principal Component Analysis – PCA)",
      "B. Chính quy hóa (Regularization)",
      "C. Xác thực chéo (Cross – validation)",
      "D. Trích xuất đặc trưng (Feature extraction)"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất:** Trong các phương pháp được liệt kê, **Xác thực chéo (Cross-validation)** phân chia dữ liệu thành $k$ phần (folds), luân phiên huấn luyện và đánh giá trên từng phần. Quá trình này giúp phát hiện và giảm thiểu tác động ngẫu nhiên của các điểm nhiễu và ngoại lệ cục bộ, đem lại đánh giá khách quan về khả năng tổng quát hóa của mô hình.\n• **Lưu ý phòng thi:** Chính quy hóa (Regularization - B) cũng giúp kiểm soát độ phức tạp mô hình, tuy nhiên theo đáp án chính thức của kỳ thi, Cross-validation là kỹ thuật xác thực đánh giá chuẩn mực để kiểm soát ngoại lệ."
  },
  {
    "id": 14,
    "category": "NLP & LLM",
    "question": "Câu 14. Trong xử lý ngôn ngữ tự nhiên, đâu là thứ tự đúng của các bước xử lý cơ bản sau đây?\n- 1. Tách từ (Tokenization)\n- 2. Chuẩn hóa văn bản (Normalization)\n- 3. Rút gọn từ (Stemming)\n- 4. Gán nhãn từ loại (Part-of-speech tagging)",
    "options": [
      "A. 2⟶1⟶4⟶3",
      "B. 2⟶1⟶3⟶4",
      "C. 1⟶3⟶2⟶4",
      "D. 1⟶2⟶4⟶3\nID 𝐵2"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Thứ tự chuẩn của pipeline tiền xử lý ngôn ngữ tự nhiên (NLP) cơ bản:\n1. **Chuẩn hóa văn bản (Normalization - 2):** Chuyển chữ thường, xóa ký tự đặc biệt, loại bỏ khoảng trắng thừa.\n2. **Tách từ (Tokenization - 1):** Phân rã chuỗi văn bản thành danh sách các token (từ/tiếng).\n3. **Rút gọn từ (Stemming - 3):** Đưa từ về dạng gốc (bỏ hậu tố/tiền tố ngữ pháp).\n4. **Gán nhãn từ loại (Part-of-speech tagging - 4):** Xác định từ loại (danh từ, động từ, tính từ...) dựa trên ngữ cảnh.\n• **Thứ tự đúng:** $2 \\to 1 \\to 3 \\to 4$."
  },
  {
    "id": 15,
    "category": "Deep Learning",
    "question": "Câu 15. Tại sao learning rate thích ứng lại hữu ích trong thực tế?",
    "options": [
      "A. Làm mô hình huấn luyện ngẫu nhiên hơn",
      "B. Tự động điều chỉnh tốc độ học theo tham số cụ thể",
      "C. Tránh tràn số",
      "D. Hạn chế overfitting"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Tỷ lệ học thích ứng (Adaptive Learning Rate như AdaGrad, RMSProp, Adam) tự động theo dõi lịch sử gradient (bậc 1 và bậc 2) để **tự động điều chỉnh tốc độ học riêng cho từng tham số cụ thể** (tham số có gradient lớn nhận bước nhảy nhỏ, tham số có gradient nhỏ nhận bước nhảy lớn hơn).\n• **Vì sao các đáp án khác sai:** Tốc độ học thích ứng không làm tăng tính ngẫu nhiên (A), không nhằm tránh tràn số (C) hay trực tiếp hạn chế overfitting (D)."
  },
  {
    "id": 16,
    "category": "NLP & LLM",
    "question": "Câu 16. An là một học sinh giỏi toán. Khi biết rằng các mô hình ngôn ngữ lớn (LLM) có thể giải được những\nbài toán phức tạp, An đã thử nghiệm nhưng kết quả không như mong đợi. Tuy nhiên, sau khi tìm hiểu và áp\ndụng kỹ thuật Chain – of – Thought, An nhận thấy mô hình bắt đầu giải đúng nhiều bài toán hơn. Vậy, kỹ\nthuật Chain – of – Thought là gì?",
    "options": [
      "A. Yêu cầu mô hình trả lời càng ngắn gọn càng tốt để tiết kiệm tài nguyên",
      "B. Huấn luyện mô hình dự đoán từ tiếp theo bằng dữ liệu song ngữ",
      "C. Yêu cầu mô hình sinh câu hỏi thay vì câu trả lời",
      "D. Thúc đẩy mô hình giải bài toán bằng cách liệt kê từng bước suy luận trung gian"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Kỹ thuật **Chuỗi suy nghĩ (Chain-of-Thought - CoT)** là phương pháp prompt engineering thúc đẩy mô hình ngôn ngữ lớn (LLM) **giải bài toán bằng cách liệt kê từng bước suy luận trung gian (step-by-step reasoning)** trước khi đưa ra câu trả lời cuối cùng, giúp tăng vọt độ chính xác trong các bài toán đố và suy luận logic."
  },
  {
    "id": 17,
    "category": "Machine Learning",
    "question": "Câu 17. Trọng số các thuộc tính trong 𝑘-NN được được thực hiện bằng:",
    "options": [
      "A. Cập nhật giá trị thuộc tính của mẫu dữ liệu theo các trọng số khác nhau",
      "B. Thuộc tính quan trọng hơn được thêm vào bởi trọng số lớn hơn",
      "C. Điều chỉnh phép tính khoảng cách bằng cách nhân từng thuộc tính với trọng số",
      "D. Một ma trận trọng số được sử dụng để tính toán các hàng xóm"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất:** Trong thuật toán $k$-NN có trọng số thuộc tính (Feature Weighted $k$-NN), độ quan trọng của các thuộc tính được phản ánh bằng cách **nhân từng thuộc tính với một trọng số $w_j$ khi tính khoảng cách**: $d(x, z) = \\sqrt{\\sum w_j (x_j - z_j)^2}$. Thuộc tính quan trọng hơn có trọng số lớn hơn, làm tăng ảnh hưởng của nó lên khoảng cách tổng thể."
  },
  {
    "id": 18,
    "category": "Clustering",
    "question": "Câu 18. Chúng ta muốn phân 7 điểm dữ liệu vào trong 3 cụm sử dụng thuật toán K-means (với khoảng cách\nEuclid). Giả sử rằng sau vòng lặp đầu tiên, các cụm 𝐶1,𝐶2 và 𝐶3 chứa các điểm dữ liệu sau (trong không gian\n2 chiều): 𝐶1 chứa 2 điểm dữ liệu: (0,6),(6,0); 𝐶2 chứa 3 điểm dữ liệu: (2,2),(4,4),(6,6); 𝐶3 chứa 2 điểm dữ\nliệu: (5,5),(7,7). Tâm của 3 cụm sẽ là?",
    "options": [
      "A. 𝐶1: (0,0),𝐶2: (48,48),𝐶3: (35,35)",
      "B. 𝐶1: (3,3),𝐶2: (4,4),𝐶3: (6,6)",
      "C. 𝐶1: (6,6),𝐶2: (12,12),𝐶3: (12,12)",
      "D. 𝐶1: (3,3),𝐶2: (6,6),𝐶3: (12,12)"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Tọa độ tâm cụm trong $K$-means là trung bình cộng tọa độ của các điểm thuộc cụm đó:\n- $C_1$: 2 điểm $(0,6), (6,0) \\implies C_1 = \\left(\\frac{0+6}{2}, \\frac{6+0}{2}\\right) = (3, 3)$.\n- $C_2$: 3 điểm $(2,2), (4,4), (6,6) \\implies C_2 = \\left(\\frac{2+4+6}{3}, \\frac{2+4+6}{3}\\right) = (4, 4)$.\n- $C_3$: 2 điểm $(5,5), (7,7) \\implies C_3 = \\left(\\frac{5+7}{2}, \\frac{5+7}{2}\\right) = (6, 6)$."
  },
  {
    "id": 19,
    "category": "NLP & LLM",
    "question": "Câu 19. GloVe là một phương pháp nhúng từ (word embedding). Phát biểu nào sau đây mô tả đúng cách mà\nnhúng từ GloVe được tạo ra?",
    "options": [
      "A. Được tạo ra trong quá trình dịch máy",
      "B. Sử dụng cơ chế chú ý (attention) để tạo vector",
      "C. Được huấn luyện từ ma trận đồng xuất hiện (co-occurrence matrix) toàn cục",
      "D. Một dạng vector gồm các số 0 và một số 1 (one-hot vector)"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất:** **GloVe (Global Vectors for Word Representation)** là phương pháp nhúng từ không giám sát được huấn luyện bằng cách tối ưu hóa hồi quy bình phương tối thiểu trên **ma trận đếm đồng xuất hiện toàn cục (global co-occurrence matrix)** của các cặp từ trong toàn bộ kho ngữ liệu (corpus)."
  },
  {
    "id": 20,
    "category": "NLP & LLM",
    "question": "Câu 20. Mô hình BERT nhận đầu vào là gì?",
    "options": [
      "A. Vector ID, mặt nạ chú ý (attention mask), ID loại token",
      "B. Chỉ văn bản thô (raw text)",
      "C. Cặp câu với nhúng (embedding)",
      "D. Từ rời rạc"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Đầu vào chuẩn của mô hình BERT (Transformer Encoder) gồm bộ 3 biểu diễn được cộng lại với nhau:\n1. **Token IDs:** Mã số định danh của từ trong từ điển (bao gồm các token đặc biệt `[CLS]`, `[SEP]`, `[PAD]`).\n2. **Attention Mask:** Mặt nạ nhị phân (1 cho token thật, 0 cho padding `[PAD]`).\n3. **Token Type IDs (Segment IDs):** Nhận diện token thuộc câu A (0) hay câu B (1)."
  },
  {
    "id": 21,
    "category": "NLP & LLM",
    "question": "Câu 21. Nếu muốn sử dụng GPT để sinh câu trả lời dựa trên một đoạn văn, mô hình nào phù hợp nhất?",
    "options": [
      "A. BERT",
      "B. GPT-2",
      "C. GPT-Neo",
      "D. GPT-3.5 hoặc GPT-4 với gợi ý phù hợp"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Để sinh câu trả lời chất lượng cao dựa trên đoạn văn bản (Question Answering/Reading Comprehension), các mô hình **GPT-3.5 hoặc GPT-4 với lời nhắc (prompt) phù hợp** là lựa chọn vượt trội nhất nhờ khả năng hiểu ngữ cảnh sâu và tuân thủ chỉ dẫn (Instruction-following via RLHF).\n• **Vì sao các đáp án khác sai:** BERT (A) là Encoder dùng để hiểu/phân loại, không sinh văn bản hồi quy; GPT-2 (B) và GPT-Neo (C) có năng lực suy luận và sinh văn bản hạn chế hơn rất nhiều."
  },
  {
    "id": 22,
    "category": "Deep Learning",
    "question": "Câu 22. Nếu thêm bỏ ngẫu nhiên (dropout) vào mô hình nhưng độ chính xác kiểm tra (validation accuracy)\ngiảm mạnh, bạn nên thử gì đầu tiên?",
    "options": [
      "A. Dùng bộ tối ưu khác",
      "B. Giảm xác suất bỏ ngẫu nhiên xuống nhỏ hơn",
      "C. Tắt bỏ ngẫu nhiên",
      "D. Tăng xác suất bỏ ngẫu nhiên lên 0.8"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Khi thêm Dropout mà độ chính xác trên tập kiểm tra (validation accuracy) giảm mạnh, điều này chứng tỏ tỷ lệ bỏ rơi quá cao đang làm mô hình bị **học dưới mức (Underfitting)** do mất mát quá nhiều thông tin liên kết giữa các neuron. Giải pháp đầu tiên cần thử là **giảm xác suất bỏ ngẫu nhiên xuống mức nhỏ hơn** (ví dụ từ 0.5 xuống 0.2 hoặc 0.1)."
  },
  {
    "id": 23,
    "category": "NLP & LLM",
    "question": "Câu 23. Trong bài toán phân loại văn bản, nếu mô hình học tốt các từ khóa rõ ràng nhưng không hiểu ngữ\ncảnh, phương pháp nào giúp cải thiện khả năng hiểu ngữ cảnh?",
    "options": [
      "A. Giảm số chiều nhúng (embedding)",
      "B. Dùng mô hình dựa trên chú ý (attention-based) như BERT",
      "C. Chuyển sang dùng TF-IDF",
      "D. Bỏ nhúng (embedding), dùng vector gồm các số 0 và một số 1 (one-hot vector)"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Các phương pháp nhúng tĩnh (Word2Vec, GloVe, TF-IDF) gán mỗi từ một vector cố định bất kể ngữ cảnh. Để mô hình nắm bắt được ngữ cảnh phức tạp và từ đa nghĩa, giải pháp tối ưu là sử dụng **mô hình dựa trên cơ chế chú ý (Attention-based) như BERT**, trong đó biểu diễn của mỗi từ thay đổi linh hoạt phụ thuộc vào toàn bộ câu văn xung quanh."
  },
  {
    "id": 24,
    "category": "Machine Learning",
    "question": "Câu 24. Giả sử rằng bạn sử dụng phương pháp 1-láng giềng gần nhất (1-NN) để dự đoán nhãn lớp cho dữ liệu\n𝑥, dựa trên tập huấn luyện 𝐷 và thước đo khoảng cách 𝑑. 1-NN sẽ đưa ra dự đoán nào cho 𝑥?",
    "options": [
      "A. 𝑦∗ trong đó (𝑎∗\n,𝑦∗)=argmin\n𝑑(𝑥,𝑦)",
      "B. 𝑦∗ trong đó (𝑎∗\n,𝑦∗)=argmin\n𝑑(𝑥,𝑎)\n(𝑎,𝑦)∈𝐷\n(𝑎,𝑦)∈𝐷",
      "C. 𝑦∗ trong đó (𝑎∗\n,𝑦∗)=argmin\n𝑑(𝑥,𝑎)",
      "D. 𝑦∗ trong đó (𝑎∗\n,𝑦∗)= min\n𝑑(𝑥,𝑎)\n(𝑎,𝑦)∈𝐷\n(𝑎,𝑦)∈𝐷"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Thuật toán 1-NN (1-láng giềng gần nhất) dự đoán nhãn cho điểm truy vấn $x$ bằng nhãn $y^*$ của điểm dữ liệu huấn luyện $a^* \\in D$ có khoảng cách $d(x, a)$ nhỏ nhất: $(a^*, y^*) = \\arg\\min_{(a, y) \\in D} d(x, a)$."
  },
  {
    "id": 25,
    "category": "Machine Learning",
    "question": "Câu 25. Xét tập huấn luyện gồm 8 mẫu dưới đây. Mỗi mẫu được mô tả bằng 3 đặc trưng số (𝐹1,𝐹2,𝐹3) và\nthuộc về một trong ba lớp.\nID 𝑭𝟏 𝑭𝟐 𝑭𝟑 Lớp\n𝑆1 2 2 0 Đỏ\n𝑆2 1 3 1 Đỏ\n𝑆3 0 2 2 Đỏ\n𝑆4 8 7 7 Xanh dương\n𝑆5 9 6 6 Xanh dương\n𝑆6 7 7 8 Xanh dương\n𝑆7 5 2 5 Xanh lá\n𝑆8 6 1 4 Xanh lá\nSử dụng thuật toán 𝑘-láng giềng gần nhất (𝑘-NN) với khoảng cách Euclid và 𝑘 =3, lớp nào sẽ được dự đoán\ncho điểm truy vấn 𝑄 =(6,2,6)?",
    "options": [
      "A. Xanh dương",
      "B. Đỏ",
      "C. Xanh lá",
      "D. Hòa thuật toán không thể quyết định"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Tính khoảng cách Euclid từ $Q=(6, 2, 6)$ đến các mẫu:**\n- $S_1 (2,2,0): d = \\sqrt{4^2+0^2+6^2} = \\sqrt{52}$\n- $S_2 (1,3,1): d = \\sqrt{5^2+(-1)^2+5^2} = \\sqrt{51}$\n- $S_3 (0,2,2): d = \\sqrt{6^2+0^2+4^2} = \\sqrt{52}$\n- $S_4 (8,7,7): d = \\sqrt{(-2)^2+(-5)^2+(-1)^2} = \\sqrt{30}$\n- $S_5 (9,6,6): d = \\sqrt{(-3)^2+(-4)^2+0^2} = 5 = \\sqrt{25}$\n- $S_6 (7,7,8): d = \\sqrt{(-1)^2+(-5)^2+(-2)^2} = \\sqrt{30}$\n- $S_7 (5,2,5): d = \\sqrt{1^2+0^2+1^2} = \\sqrt{2} \\approx 1.41$\n- $S_8 (6,1,4): d = \\sqrt{0^2+1^2+2^2} = \\sqrt{5} \\approx 2.24$\n• **3 láng giềng gần nhất ($k=3$):** $S_7 (\\sqrt{2}$ - Xanh lá), $S_8 (\\sqrt{5}$ - Xanh lá), $S_5 (5$ - Xanh dương).\n• **Bỏ phiếu đa số:** 2 phiếu Xanh lá vs 1 phiếu Xanh dương $\\implies$ Dự đoán nhãn **Xanh lá**."
  },
  {
    "id": 26,
    "category": "Computer Vision",
    "question": "Câu 26. Hình dưới đây biểu thị bản đồ đặc trưng (feature map) thu được sau khi áp dụng một bộ lọc Conv2D lên ảnh đầu vào kích thước 128 × 128 (bản đồ hiển thị các đường sáng kéo dài theo cả chiều ngang và chiều dọc giao nhau thành dạng lưới grid/cross pattern).\n\nHãy cho biết bộ lọc này đang phát hiện đặc trưng gì nhất?",
    "options": [
      "A. Các mẫu bề mặt (texture patterns)",
      "B. Các đốm màu (color blobs)",
      "C. Các cạnh theo hướng kết hợp ngang và dọc (cross directional edges)",
      "D. cạnh theo hướng ngang (horizontal edges)"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất:** Bản đồ đặc trưng (feature map) hiển thị các đường sáng chạy dọc và chạy ngang giao nhau tạo thành cấu trúc lưới ô vuông rõ ràng. Điều này chứng minh bộ lọc Conv2D đang phát hiện **các cạnh theo cả hai hướng kết hợp ngang và dọc (cross directional edges)**."
  },
  {
    "id": 27,
    "category": "Computer Vision",
    "question": "Câu 27. Cho đoạn mã dưới đây, kích thước của output_tensor là bao nhiêu?\n1 import tensorflow as tf\n2\n3 input_tensor = tf.constant(tf.random.normal(shape = (1, 32, 32, 3)), dtype =\n4\ntf.float32)\n5 conv_layer = tf.keras.layers.Conv2D(filters = 32, kernel_size = (5, 5),\n\nstrides = (2, 2), padding = 'same')\n6\n7 output_tensor = conv_layer(input_tensor)\n8\n9 print(output_tensor.shape)",
    "options": [
      "A. (1,16,16,32)",
      "B. (1,16,16,3)",
      "C. (1,14,14,32)",
      "D. (1,32,32,32)"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Công thức kích thước đầu ra Conv2D với `padding='same'` và `strides=(2, 2)`:**\n- Chiều cao: $H_{\\text{out}} = \\lceil H_{\\text{in}} / \\text{stride} \\rceil = \\lceil 32 / 2 \\rceil = 16$.\n- Chiều rộng: $W_{\\text{out}} = \\lceil W_{\\text{in}} / \\text{stride} \\rceil = \\lceil 32 / 2 \\rceil = 16$.\n- Số kênh: $C_{\\text{out}} = \\text{filters} = 32$.\n- Kích thước batch: Giữ nguyên $B = 1$.\n• **Kích thước tensor đầu ra:** $(1, 16, 16, 32)$."
  },
  {
    "id": 28,
    "category": "NLP & LLM",
    "question": "Câu 28. Mục đích chính của lấy mẫu phủ định (Negative Sampling) trong huấn luyện mô hình vectơ từ là gì?",
    "options": [
      "A. Tăng số lượng tham số của mô hình.",
      "B. Giúp mô hình sinh ra văn bản dài hơn và tự nhiên hơn.",
      "C. Giúp cải thiện độ chính xác mô hình.",
      "D. Giảm chi phí tính toán khi huấn luyện trên tập từ vựng lớn."
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Trong huấn luyện Word2Vec, mẫu số của Softmax đòi hỏi phải tính tổng lũy thừa trên toàn bộ từ điển $V$ (thường có hàng trăm nghìn từ), gây chi phí tính toán cực kỳ tốn kém. **Lấy mẫu phủ định (Negative Sampling)** xấp xỉ bài toán bằng cách chỉ lấy một vài từ âm ngẫu nhiên (thường từ 5-20 từ) để biến thành bài toán phân loại nhị phân Logistic, giúp **giảm mạnh chi phí tính toán khi tập từ vựng lớn**."
  },
  {
    "id": 29,
    "category": "Deep Learning",
    "question": "Câu 29. Khi sử dụng bộ tối ưu Adam, nếu mất mát huấn luyện (training loss) ngừng giảm sớm (plateau), bạn\nnên thử gì tiếp theo?",
    "options": [
      "A. Đặt lại toàn bộ mô hình",
      "B. Tăng kích thước lô (batch size)",
      "C. Bỏ chuẩn hóa lô (BatchNorm)",
      "D. Giảm tỷ lệ học (learning rate) hoặc thử lại với SGD"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Khi dùng Adam mà training loss ngừng giảm sớm (bị chững lại/plateau), nguyên nhân phổ biến là do trung bình động hàm mũ (EMA) của gradient làm tốc độ học bị lệch hoặc learning rate ban đầu quá cao khiến mô hình nhảy qua cực tiểu. Biện pháp hiệu quả nhất là **giảm tỷ lệ học (learning rate) hoặc thử chuyển sang SGD với momentum** để hội tụ mịn hơn."
  },
  {
    "id": 30,
    "category": "Deep Learning",
    "question": "Câu 30. Học tự giám sát (self-supervised learning) thường sử dụng phương pháp nào?",
    "options": [
      "A. Đầu phân loại (classification head)",
      "B. Phân cụm (clustering)",
      "C. Tăng cường dữ liệu (augmentation) và mất mát đối lập (contrastive loss)",
      "D. Gắn nhãn thủ công"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất:** Học tự giám sát (Self-Supervised Learning) trên hình ảnh (như SimCLR, MoCo) tạo ra tín hiệu tự giám sát bằng cách áp dụng **tăng cường dữ liệu (data augmentation)** để tạo ra các góc nhìn khác nhau của cùng một ảnh, sau đó dùng **hàm mất mát đối lập (contrastive loss)** để kéo các biểu diễn của cùng ảnh lại gần nhau và đẩy biểu diễn của các ảnh khác ra xa nhau."
  },
  {
    "id": 31,
    "category": "Machine Learning",
    "question": "Câu 31. Chuẩn hóa rất quan trọng đối với 𝑘-NN vì",
    "options": [
      "A. Giúp tránh được vấn đề một thuộc tính có thể đóng vai trò quyết định, lấn át các thuộc tính khác.",
      "B. Nó biến đổi các giá trị thuộc tính thành phạm vi [0,1] để dễ dàng tính toán.",
      "C. Nó cho phép so sánh và phân tích có ý nghĩa giữa các biến.",
      "D. Nó cần thiết để tính toán khoảng cách giữa các mẫu dữ liệu."
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Thuật toán $k$-NN dựa trên khoảng cách hình học giữa các điểm dữ liệu. Nếu một thuộc tính có thang đo quá lớn (ví dụ: Thu nhập hàng chục triệu) so với thuộc tính khác (ví dụ: Tuổi từ 1-100), khoảng cách sẽ bị thuộc tính lớn chi phối hoàn toàn. **Chuẩn hóa dữ liệu (Scaling)** đưa các biến về cùng phạm vi (như $[0, 1]$ hoặc chuẩn hóa Z-score) để mọi thuộc tính đóng góp công bằng."
  },
  {
    "id": 32,
    "category": "Computer Vision",
    "question": "Câu 32. Cho bản đồ đặc trưng sau. Giá trị ở vị trí (0,0) của bản đồ đặc trưng đầu ra sau khi áp dụng lớp gộp\ntrung bình (Average Pooling) với kích thước cửa sổ 3×3 và bước nhảy 2 là:\n[[10, 20, 30, 40],\n[50, 60, 70, 80],\n[90, 100, 110, 120],\n[130, 140, 150, 160]]",
    "options": [
      "A. 55",
      "B. 70",
      "C. 60",
      "D. 50"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Tính Average Pooling cửa sổ $3 \\times 3$ tại vị trí $(0, 0)$:**\nCửa sổ $3 \\times 3$ góc trên bên trái gồm 9 phần tử:\n$$\\begin{bmatrix} 10 & 20 & 30 \\\\ 50 & 60 & 70 \\\\ 90 & 100 & 110 \\end{bmatrix}$$\nGiá trị trung bình cộng:\n$$\\text{Avg} = \\frac{10 + 20 + 30 + 50 + 60 + 70 + 90 + 100 + 110}{9} = \\frac{540}{9} = 60.$$"
  },
  {
    "id": 33,
    "category": "Computer Vision",
    "question": "Câu 33. Chương trình sau thực hiện:\n- Tải ResNet-50 pre-trained trên ImageNet.\n- Đóng băng toàn bộ các layer convolution.\n- Lấy output của lớp avgpool(shape(2048,1,1)) và flatten thành vector 2048.\nBạn thiếu dòng nào dưới đây để trả về vec tơ đặc trưng (feature vector)?\n1 import torch, torchvision.models as models\n2\n3 model = models.resnet50(weights = 'DEFAULT')\n4\n5 for p in model.parameters():\n6 p.requires_grad_(False)\n7\n8\n10 11 12\n13 9 model.fc = torch.nn.Identity()\nx = torch.randn(1, 3, 224, 224)\n... #  fil here\nprint(feature.shape)",
    "options": [
      "A. features = model(x)",
      "B. features = model.layer4(x)",
      "C. features = model.avgpool(x)",
      "D. features = x"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Khi ta đã thay thế lớp phân loại cuối cùng bằng `model.fc = torch.nn.Identity()`, mô hình ResNet50 sẽ trả về trực tiếp vector đặc trưng 2048 chiều tại đầu ra của lớp `avgpool`. Do đó, chỉ cần gọi hàm truyền xuôi `features = model(x)` để thu được vector đặc trưng."
  },
  {
    "id": 34,
    "category": "Computer Vision",
    "question": "Câu 34. Bạn muốn sử dụng một mô hình Mạng Nơ-ron Tích chập (CNN) cho nhiệm vụ phân tích ảnh viễn\nthám (ảnh chụp từ vệ tinh, máy bay). Bạn có hai lựa chọn:\n- Huấn luyện từ đầu: Xây dựng và huấn luyện một mô hình CNN hoàn toàn mới chỉ sử dụng bộ dữ liệu ảnh\nviễn thám (giả sử có kích thước trung bình).\n- Tinh chỉnh (Fine-tuning): Lấy một mô hình CNN đã được huấn luyện trước trên một tập dữ liệu lớn gồm ảnh\ntự nhiên (ví dụ: ImageNet - ảnh chó, mèo, ô tô, v.v.) và điều chỉnh (tinh chỉnh) nó cho phù hợp với bộ dữ liệu\nảnh viễn thám của bạn.\nSo với việc huấn luyện mô hình từ đầu, phương pháp tinh chỉnh mang lại nhiều lợi ích. Tuy nhiên, điều nào\ndưới đây KHÔNG phải là một ưu điểm điển hình của việc tinh chỉnh trong tình huống này?",
    "options": [
      "A. Giảm nguy cơ quá khớp (overfitting) vì có ít tham số cần cập nhật",
      "B. Khắc phục được hoàn toàn được vấn đề về sự khác biệt giữa đặc điểm ảnh tự nhiên và ảnh viễn thám.",
      "C. Mô hình hội tụ nhanh hơn do kế thừa trọng số đặc trưng cơ bản",
      "D. Tận dụng đặc trưng cấp thấp tổng quát"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Tinh chỉnh (Fine-tuning) kế thừa các bộ lọc cấp thấp tổng quát (cạnh, góc, texture) và hội tụ nhanh hơn. Tuy nhiên, **ảnh viễn thám có góc chụp từ trên xuống, đa phổ và đặc trưng quang học rất khác biệt so với ảnh tự nhiên (ImageNet)**. Do đó, fine-tuning **KHÔNG THỂ khắc phục hoàn toàn** được sự khác biệt miền (domain shift) này."
  },
  {
    "id": 35,
    "category": "Computer Vision",
    "question": "Câu 35. Một bộ lọc hình vuông, mỗi cạnh của nó dài 𝑘 ô vuông. Bộ lọc này được dùng để quét qua một bức\nảnh ban đầu có chiều ngang 𝑚 ô vuông và chiều dọc 𝑛 ô vuông (𝑚,𝑛 >𝑘). Mỗi lần quét, bộ lọc sẽ dịch\nchuyển đi 2 ô vuông theo cả chiều ngang lẫn chiều dọc. Quá trình quét này không thêm bất kỳ lớp đệm nào\nvào xung quanh ảnh gốc. Hỏi sau khi quét xong, bức ảnh kết quả (bản đồ đặc trưng đầu ra) sẽ có kích thước\nbao nhiêu ô vuông chiều ngang và bao nhiêu ô vuông chiều dọc?",
    "options": [
      "A. (𝑚\n𝑛\n2 ,\n2)",
      "B. (⌊𝑚−𝑘\n2 ⌋+1,⌊𝑛−𝑘\n2 ⌋+1)",
      "C. (𝑚−𝑘\n𝑛−𝑘\n2 +𝑘,\n2 +𝑘)",
      "D. (𝑚−𝑘+1\n2 ,\n𝑛−𝑘+1\n2 )"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Công thức kích thước đầu ra tích chập (không padding, stride = 2):**\n$$\\text{Chiều ngang} = \\left\\lfloor \\frac{m - k}{2} \\right\\rfloor + 1, \\quad \\text{Chiều dọc} = \\left\\lfloor \\frac{n - k}{2} \\right\\rfloor + 1.$$"
  },
  {
    "id": 36,
    "category": "Computer Vision",
    "question": "Câu 36. Khi dùng ViT để phân loại ảnh, lớp cuối cùng thường là gì?",
    "options": [
      "A. Khối chú ý (attention block)",
      "B. Bỏ ngẫu nhiên (dropout)",
      "C. Lớp kết nối đầy đủ (fully connected) và hàm Softmax",
      "D. LSTM"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất:** Trong mô hình Vision Transformer (ViT) cho bài toán phân loại ảnh, token đại diện `[CLS]` sau khi đi qua ngăn xếp Transformer Encoder sẽ được đưa vào khối **MLP Head (gồm một lớp kết nối đầy đủ Fully Connected và hàm Softmax)** để tính toán phân phối xác suất trên các lớp."
  },
  {
    "id": 37,
    "category": "Machine Learning",
    "question": "Câu 37. Dựa trên tập dữ liệu trong Bảng 1 dưới đây để xây dựng cây quyết định, hãy tính xấp xỉ entropy\n𝐻(Passed). Cây quyết định này dự đoán liệu sinh viên có qua môn hay không (𝑇 là có, 𝐹 là không), dựa trên\nđiểm CGPA (𝐻: cao, 𝑀: trung bình, 𝐿: thấp) và việc có ôn tập hay không (𝑇 hoặc 𝐹).\nCGPA Ôn tập Qua môn\n𝐻 𝐹 𝑇\n𝐻 𝑇 𝑇\n𝑀 𝐹 𝐹\n𝑀 𝑇 𝑇\n𝐿 𝐹 𝐹\n𝐿 𝑇 𝑇",
    "options": [
      "A. 0.66",
      "B. 1.92",
      "C. 0.92",
      "D. 1.32"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Tính Entropy của biến mục tiêu `Qua môn` (Passed):**\nCó 6 mẫu sinh viên: 4 mẫu $T$ (Qua môn) và 2 mẫu $F$ (Trượt môn).\n$$p_T = \\frac{4}{6} = \\frac{2}{3}, \\quad p_F = \\frac{2}{6} = \\frac{1}{3}$$\n$$H(\\text{Passed}) = - p_T \\log_2(p_T) - p_F \\log_2(p_F) = - \\frac{2}{3} \\log_2\\left(\\frac{2}{3}\\right) - \\frac{1}{3} \\log_2\\left(\\frac{1}{3}\\right) \\approx 0.918 \\approx 0.92\\text{ bit}.$$"
  },
  {
    "id": 38,
    "category": "Deep Learning",
    "question": "Câu 38. Một bức ảnh thuộc vào một trong hai lớp: 'chó' hoặc 'mèo'. Nhãn thực tế (ground truth label) của ảnh\nnày được biểu diễn dưới dạng one-hot encoding là [0,1], trong đó vị trí thứ nhất tương ứng với lớp 'chó' và vị\ntrí thứ hai tương ứng với lớp 'mèo'. Mô hình của chúng ta đã dự đoán xác suất cho ảnh này là [0.3,0.7], nghĩa\nlà xác suất dự đoán là 0.3 cho lớp 'chó' và 0.7 cho lớp 'mèo'. Hãy tính giá trị của hàm mất mát cross-entropy\ncho dự đoán này, sử dụng logarit tự nhiên (ln).",
    "options": [
      "A. 0.105",
      "B. 0.247",
      "C. 0.357",
      "D. 0.713"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Tính Cross-Entropy Loss cho bài toán nhị phân:**\nNhãn thực tế dạng one-hot: $y = [0, 1]$ (lớp 'mèo'). Xác suất dự đoán: $\\hat{y} = [0.3, 0.7]$.\n$$\\mathcal{L} = - \\sum y_i \\ln(\\hat{y}_i) = - 0 \\times \\ln(0.3) - 1 \\times \\ln(0.7) = - \\ln(0.7) \\approx 0.3567 \\approx 0.357.$$"
  },
  {
    "id": 39,
    "category": "Computer Vision",
    "question": "Câu 39. Khi tinh chỉnh (fine-tune) ResNet34, nếu suy luận (inference) chậm, bạn nên thử gì để tăng tốc độ?",
    "options": [
      "A. Chuyển sang dùng mô hình nhỏ hơn như MobileNet",
      "B. Thêm lớp bỏ ngẫu nhiên (dropout) vào suy luận",
      "C. Tăng số vòng lặp (epoch)",
      "D. Giảm số lớp (class)"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Để tăng tốc độ suy luận (inference speed) và giảm độ trễ, giải pháp kiến trúc trực tiếp và hiệu quả nhất là **chuyển sang mô hình nhẹ chuyên dụng như MobileNet** (sử dụng Depthwise Separable Convolution giúp giảm 8-9 lần khối lượng tính toán FLOPs so với mạng ResNet tiêu chuẩn)."
  },
  {
    "id": 40,
    "category": "Deep Learning",
    "question": "Câu 40. Khi huấn luyện mạng nơ-ron đa tầng (MLP) bằng phương pháp tối ưu hóa theo lô nhỏ (mini-batch\n\nSGD), bạn cần làm gì sau mỗi vòng lặp (epoch) để đảm bảo mô hình học hiệu quả và tránh thiên lệch?",
    "options": [
      "A. Xáo trộn dữ liệu (shuffle) huấn luyện",
      "B. Sử dụng toàn bộ dữ liệu (full-batch) để cập nhật trọng số",
      "C. Đặt lại trọng số về giá trị ban đầu",
      "D. Chuyển sang sử dụng bộ tối ưu Adam"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Trong mini-batch SGD, việc **xáo trộn dữ liệu (shuffle) sau mỗi epoch** đảm bảo các mini-batch ở mỗi vòng lặp mang tính ngẫu nhiên và đa dạng, giúp gradient ước lượng không bị thiên lệch theo thứ tự mẫu và giúp mô hình dễ dàng thoát khỏi các điểm cực tiểu cục bộ (local minima)."
  },
  {
    "id": 41,
    "category": "NLP & LLM",
    "question": "Câu 41. Với Lấy mẫu phủ định (Negative Sampling), các mẫu sẽ được chọn như thế nào?",
    "options": [
      "A. Là các từ có độ tương đồng ngữ nghĩa cao với từ mục tiêu.",
      "B. Là các từ gần nhất với từ ngữ cảnh trong văn bản.",
      "C. Là các từ có nhãn đúng trong tập huấn luyện.",
      "D. Được chọn ngẫu nhiên từ toàn bộ từ vựng, thường theo một phân phối cố định."
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Trong Negative Sampling của Word2Vec, các từ âm được **chọn ngẫu nhiên từ toàn bộ kho từ vựng theo phân phối Unigram lũy thừa $3/4$**: $P(w) \\propto U(w)^{0.75}$. Số mũ $0.75$ giúp làm mịn phân phối, giảm tần suất chọn các từ quá phổ biến và tăng cơ hội xuất hiện của các từ hiếm."
  },
  {
    "id": 42,
    "category": "Clustering",
    "question": "Câu 42. Cho trước tập dữ liệu không có nhãn gồm 𝑁 điểm dữ liệu: {𝑥1,𝑥2,…,𝑥𝑁}. Chúng ta chạy 𝐾-means\nvới 50 lần khởi tạo ngẫu nhiên tâm cụm khác nhau (luôn với cùng số lượng tâm cụm 𝐾) và thu được 50 bộ\ntâm cụm khác nhau. Đâu là cách được gợi ý cho việc chọn 1 kết quả từ 50 kết quả trên để sử dụng?\n𝑁\n1",
    "options": [
      "A. Chọn kết quả mà\n𝑁∑‖𝑥𝑖−𝑚𝑧𝑖‖2\nđạt giá trị nhỏ nhất trong 50 lần, với 𝑚𝑧𝑖 là tâm cụm mà 𝑥𝑖\n𝑖=1\nđược gán vào.",
      "B. Chọn lần chạy thứ mấy cũng có thể tốt.",
      "C. Luôn chọn lần cuối cùng (thứ 50), vì lần này có khả năng đã hội tụ thành một giải pháp tốt.",
      "D. Chỉ có cách duy nhất để chọn là yêu cầu dữ liệu phải có nhãn 𝑦𝑖."
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Thuật toán $K$-means hội tụ về cực tiểu cục bộ phụ thuộc vào việc khởi tạo tâm ban đầu. Khi chạy 50 lần với các khởi tạo ngẫu nhiên khác nhau, giải pháp tối ưu nhất là **chọn kết quả có tổng bình phương khoảng cách nội cụm ($D_{\\text{intra}}$ hay hàm quán tính SSE/Inertia) nhỏ nhất**: $\\frac{1}{N} \\sum \\|x_i - m_{z_i}\\|^2 \\to \\min$."
  },
  {
    "id": 43,
    "category": "Computer Vision",
    "question": "Câu 43. Sử dụng mô hình ResNet–18, với khoảng 11.7 triệu tham số, đã được tiền huấn luyện trên tập dữ\nliệu ImageNet làm điểm khởi đầu. Trong quá trình tinh chỉnh cho nhiệm vụ cụ thể, bạn áp dụng chiến lược\nđóng băng trọng số cho toàn bộ phần thân (backbone) của mô hình. Tuy nhiên, có một ngoại lệ đáng chú ý:\nbạn chỉ mở băng và cho phép cập nhật trọng số cho một khối duy nhất là BasicBlock thứ hai nằm trong lớp\nthứ tư (layer4), được gọi tắt là \"block 4–2\". Khối \"block 4–2\" này, bao gồm hai lớp tích chập 3×3:\n3×3,512,𝑠 = 1\n3×3,512,𝑠 = 1\nConv1:512\n← 512, Conv2:512\n← 512\n- Bỏ qua tham số và tính toán không cần thiết: Chúng ta sẽ không tính số lượng tham số bias và bỏ qua chi\nphí tính toán (FLOPs) của các lớp Batch Normalization (BN), hàm kích hoạt ReLU, và các kết nối tắt (skip\nconnection / identity mapping).\n- Định nghĩa FLOPs: Một phép toán dấu phẩy động (FLOP) được tính là một phép nhân và một phép cộng.\nĐối với lớp tích chập, tổng FLOPs xấp xỉ bằng 2 lần số phép tính nhân – cộng (MACs). (FLOPs ≈\n2×MACs).\n- Kích thước đầu vào cho khối: Khi mô hình xử lý một ảnh đầu vào gốc có kích thước 224×224, tensor đặc\ntrưng đi vào khối \"block 4–2\" có kích thước là (Batch=1, Channels=512, Height=7, Width=7).\nDựa trên giả sử trên, câu trả lời nào sau đây là đúng khi tính tính tổng số tham số có thể huấn luyện (trainable\nparameters) chỉ chứa trong khối \"block 4–2\" và tổng số FLOPs cần thiết để thực thi chỉ riêng khối \"block\n4–2\" khi xử lý tensor đầu vào có kích thước (1,512,7,7).",
    "options": [
      "A. 11.7 M; 1.8 GFLOPs",
      "B. 4.7 M; 0.46 GFLOPs",
      "C. 0.50 M; 0.05 GFLOPs",
      "D. 8.4 M; 0.82 GFLOPs"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Tính toán số tham số và FLOPs của Block 4-2 trong ResNet-18:**\nKhối gồm 2 lớp Conv2D ($3 \\times 3, 512 \\to 512$):\n- **Số tham số:** $2 \\times (3 \\times 3 \\times 512 \\times 512) = 2 \\times 2,359,296 \\approx 4.718.592 \\approx 4.7\\text{ M}$.\n- **FLOPs (với đầu vào $1 \\times 512 \\times 7 \\times 7$):**\n  $\\text{MACs} = 2 \\times [7 \\times 7 \\times 512 \\times (512 \\times 3 \\times 3)] \\approx 231.2\\text{ M}$.\n  $\\text{FLOPs} \\approx 2 \\times \\text{MACs} \\approx 462.4\\text{ MFLOPs} \\approx 0.46\\text{ GFLOPs}$."
  },
  {
    "id": 44,
    "category": "Deep Learning",
    "question": "Câu 44. Tỷ lệ học thích ứng (adaptive learning rate) như AdaGrad, RMSProp, Adam giúp gì cho mô hình?",
    "options": [
      "A. Giảm kích thước mô hình",
      "B. Tăng kích thước lô (batch size)",
      "C. Giảm số vòng lặp (epoch) cần thiết",
      "D. Tự động điều chỉnh tốc độ học cho từng tham số"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Các bộ tối ưu hóa thích ứng (AdaGrad, RMSProp, Adam) theo dõi độ lớn gradient lịch sử của từng trọng số để **tự động điều chỉnh tốc độ học (learning rate) riêng biệt cho từng tham số**, giải quyết triệt để bài toán chọn một learning rate chung cho toàn mạng."
  },
  {
    "id": 45,
    "category": "Deep Learning",
    "question": "Câu 45. Trong tối ưu hóa theo lô nhỏ (mini-batch SGD), nếu kích thước lô (batch size) quá nhỏ, hệ quả thường\ngặp là gì?",
    "options": [
      "A. Giảm thời gian huấn luyện",
      "B. Gradient quá nhiễu, gây dao động",
      "C. Độ chính xác tăng nhanh",
      "D. Không ảnh hưởng"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Khi kích thước lô (batch size) quá nhỏ (ví dụ 1 hoặc 2 mẫu), gradient ước lượng tại mỗi bước chỉ đại diện cho một vài mẫu ngẫu nhiên nên **bị nhiễu động rất lớn (high noise/variance)**, khiến đường cong hàm mất mát dao động mạnh và khó hội tụ ổn định."
  },
  {
    "id": 46,
    "category": "Machine Learning",
    "question": "Câu 46. Những chiến lược nào có thể giúp giảm vấn đề quá khớp (overfitting) trong cây quyết định?\n- i. Giới hạn độ sâu tối đa của cây\n\n- ii. Áp đặt số lượng mẫu tối thiểu tại các nút lá\n- iii. Cắt tỉa cây (pruning)\n- iv. Đảm bảo mỗi nút lá chứa duy nhất một lớp",
    "options": [
      "A. Không có lựa chọn nào đúng",
      "B. Tất cả",
      "C. (i), (ii) và (iii)",
      "D. (i), (iii), (iv)"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất:** Để giảm thiểu quá khớp (overfitting) trong Cây quyết định, các chiến lược chuẩn mực gồm: (i) Giới hạn độ sâu tối đa của cây (`max_depth`), (ii) Áp đặt số lượng mẫu tối thiểu tại nút lá (`min_samples_leaf`), và (iii) Cắt tỉa cây (pruning). Ràng buộc mỗi nút lá chỉ chứa duy nhất một lớp (iv) ngược lại sẽ làm cây bị overfitting cực nặng."
  },
  {
    "id": 47,
    "category": "Deep Learning",
    "question": "Câu 47. Một nơ-ron có 3 đầu vào với trọng số lần lượt là 1,4 và 3, không có bias. Hàm truyền là hàm tuyến\ntính với hằng số tỷ lệ bằng 3. Các đầu vào lần lượt là 4,8 và 5. Đầu ra sẽ là bao nhiêu?",
    "options": [
      "A. 162",
      "B. 153",
      "C. 139",
      "D. 160"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Tính đầu ra nơ-ron:**\n- Tổng có trọng số: $z = w_1 x_1 + w_2 x_2 + w_3 x_3 = 1 \\times 4 + 4 \\times 8 + 3 \\times 5 = 4 + 32 + 15 = 51$.\n- Hàm truyền tuyến tính với hệ số tỷ lệ $k = 3$:\n  $$y = k \\times z = 3 \\times 51 = 153.$$"
  },
  {
    "id": 48,
    "category": "Calculus",
    "question": "Câu 48. Gradient của hàm số 2𝑥2\n−3𝑦2 +4𝑦−10 tại điểm (0,0) là gì?",
    "options": [
      "A. 1𝑖+10𝑗",
      "B. 2𝑖−3𝑗",
      "C. −3𝑖+4𝑗",
      "D. 0𝑖+4𝑗"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Tính Vector Gradient:**\nHàm số $f(x, y) = 2x^2 - 3y^2 + 4y - 10$.\n- Đạo hàm riêng theo $x$: $\\frac{\\partial f}{\\partial x} = 4x$.\n- Đạo hàm riêng theo $y$: $\\frac{\\partial f}{\\partial y} = -6y + 4$.\n• Tại gốc tọa độ $(0, 0)$:\n$$\\nabla f(0, 0) = \\left(4(0), -6(0) + 4\\right) = 0\\vec{i} + 4\\vec{j}.$$"
  },
  {
    "id": 49,
    "category": "Evaluation",
    "question": "Câu 49. Khi huấn luyện mô hình phân loại nhiều lớp với tập dữ liệu mất cân bằng về nhãn lớp, nếu lớp hiếm\n(ít dữ liệu huấn luyện) gần như không được dự đoán, cách xử lý phù hợp là gì?",
    "options": [
      "A. Giảm số vòng lặp (epoch)",
      "B. Xóa lớp hiếm khỏi dữ liệu",
      "C. Tăng bỏ ngẫu nhiên (dropout)",
      "D. Sử dụng hàm mất mát có trọng số"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Khi dữ liệu mất cân bằng nghiêm trọng và lớp hiếm bị bỏ qua, giải pháp cấp thuật toán hiệu quả nhất là **sử dụng hàm mất mát có trọng số (Weighted Loss)**, trong đó các lỗi dự đoán sai trên lớp hiếm bị phạt với trọng số lớn hơn tỷ lệ nghịch với tần suất xuất hiện của lớp đó."
  },
  {
    "id": 50,
    "category": "Computer Vision",
    "question": "Câu 50. Khi tinh chỉnh (fine-tune) MobileNetV2 trên tập dữ liệu nhỏ, bước đầu tiên bạn nên làm là gì để tối\nưu hóa hiệu suất?",
    "options": [
      "A. Tăng số lớp",
      "B. Thay toàn bộ mô hình",
      "C. Đóng băng (freeze) các lớp đầu tiên",
      "D. Tăng tỷ lệ học (learning rate)"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất:** Khi tinh chỉnh (fine-tune) một mô hình tiền huấn luyện lớn trên tập dữ liệu nhỏ, bước đầu tiên quan trọng nhất là **đóng băng (freeze) các lớp trích xuất đặc trưng đầu tiên** và chỉ huấn luyện lớp phân loại cuối cùng. Điều này ngăn trọng số cơ bản bị phá vỡ và tránh hiện tượng overfitting."
  },
  {
    "id": 51,
    "category": "Deep Learning",
    "question": "Câu 51. Khi huấn luyện bằng PyTorch, nếu GPU bị đầy bộ nhớ (Out – of – Memory – OOM), bạn nên thử gì\nđầu tiên?",
    "options": [
      "A. Chuyển sang dùng CPU",
      "B. Thêm bỏ ngẫu nhiên (dropout)",
      "C. Dùng mô hình lớn hơn",
      "D. Giảm kích thước lô (batch size) hoặc dùng tích lũy gradient (gradient accumulation)"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Lỗi tràn bộ nhớ GPU (Out-Of-Memory - OOM) xuất phát từ việc kích thước batch quá lớn khiến GPU không đủ VRAM chứa activations trung gian. Biện pháp đầu tiên và chuẩn nhất là **giảm batch size kết hợp kỹ thuật tích lũy gradient (Gradient Accumulation)** để mô phỏng kích thước batch lớn mà vẫn vừa vặn bộ nhớ GPU."
  },
  {
    "id": 52,
    "category": "Clustering",
    "question": "Câu 52. Phương pháp nào sau đây KHÔNG thuộc nhóm học có giám sát?",
    "options": [
      "A. Cây quyết định",
      "B. Hồi quy tuyến tính với Ridge",
      "C. Naive Bayes",
      "D. K-means"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** **$K$-means** là thuật toán phân cụm không giám sát (Unsupervised Learning), gom cụm dữ liệu hoàn toàn dựa trên khoảng cách hình học mà không cần bất kỳ nhãn mục tiêu nào. Cây quyết định, Naive Bayes và Ridge Regression đều là các phương pháp học có giám sát."
  },
  {
    "id": 53,
    "category": "Machine Learning",
    "question": "Câu 53. Phát biểu nào sau đây là đúng về giải thuật học láng giềng gần nhất?",
    "options": [
      "A. Chỉ được sử dụng cho bài toán hồi quy",
      "B. Thuộc lớp bài toán học tham số",
      "C. Chỉ được sử dụng cho bài toán phân loại",
      "D. Được sử dụng cho cả bài toán phân loại và bài toán hồi quy"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Thuật toán $k$-láng giềng gần nhất ($k$-NN) là một thuật toán phi tham số có thể áp dụng cho **cả bài toán phân loại (dùng bầu chọn đa số) và bài toán hồi quy (dùng trung bình cộng giá trị của $k$ láng giềng)**."
  },
  {
    "id": 54,
    "category": "Deep Learning",
    "question": "Câu 54. Mục đích chính của việc tăng cường dữ liệu trong huấn luyện mô hình học máy/học sâu là gì?",
    "options": [
      "A. Tăng tốc độ huấn luyện mô hình",
      "B. Giảm số lượng tham số của mô hình",
      "C. Giảm kích thước vật lý của tập dữ liệu gốc",
      "D. Cải thiện khả năng tổng quát hóa của mô hình"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Mục đích cốt lõi của việc tăng cường dữ liệu (Data Augmentation) là tạo ra các biến thể nhân tạo hợp lý của dữ liệu huấn luyện, giúp mô hình học được các đặc trưng bất biến và **cải thiện đáng kể khả năng tổng quát hóa (generalization)** trên tập dữ liệu kiểm thử."
  },
  {
    "id": 55,
    "category": "NLP & LLM",
    "question": "Câu 55. Khi sử dụng BertTokenizer từ Hugging Face, điều nào sau đây đúng?",
    "options": [
      "A. Bộ mã hóa không hỗ trợ lô (batch)",
      "B. tokenizer.encode_plus() trả về input_ids, attention_mask",
      "C. BERT chỉ dùng cho tiếng Anh",
      "D. Bộ mã hóa (tokenizer) không cần đệm (padding)"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Trong thư viện Transformers của Hugging Face, bộ mã hóa `BertTokenizer` không bắt buộc phải đệm (padding) mà tham số `padding` có giá trị mặc định là `False` (chỉ thêm padding khi người dùng kích hoạt rõ ràng). Ngoài ra `bert-base-multilingual-uncased` hỗ trợ đa ngôn ngữ bao gồm tiếng Việt."
  },
  {
    "id": 56,
    "category": "Deep Learning",
    "question": "Câu 56. Dưới đây là một số lựa chọn để có thể thực hiện khi huấn luyện mạng nơ-ron. Đâu là trường hợp sẽ\nkhiến mạng của bạn KHÓ đạt được độ chính xác cao trong tương lai?",
    "options": [
      "A. Đảo ngẫu nhiên lại dữ liệu khi bắt đầu mỗi epoch",
      "B. Khởi tạo tất cả bộ tham số bằng 0",
      "C. Sử dụng momentum",
      "D. Sử dụng Dropout"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Khởi tạo tất cả trọng số mạng nơ-ron bằng 0 dẫn đến **hiện tượng đối xứng hoán vị (symmetry problem)**: tất cả các neuron trong cùng một lớp nhận tín hiệu đầu vào và gradient y hệt nhau, khiến chúng cập nhật giống hệt nhau ở mọi bước và mạng suy biến không thể học được các đặc trưng khác biệt."
  },
  {
    "id": 57,
    "category": "Computer Vision",
    "question": "Câu 57. Trong mô hình SSD, hộp neo (anchor boxes) có vai trò gì?",
    "options": [
      "A. Định nghĩa trước các tỷ lệ và kích thước hộp",
      "B. Làm nhẹ mô hình",
      "C. Làm tăng số lớp",
      "D. Tăng độ phân giải ảnh"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Trong mô hình phát hiện vật thể SSD (Single Shot MultiBox Detector), các hộp neo (Anchor / Default boxes) được thiết kế để **định nghĩa trước các tỷ lệ (aspect ratios) và kích thước (scales) hộp bao** trên các feature maps đa tỉ lệ, giúp mô hình phát hiện vật thể ở nhiều kích thước khác nhau."
  },
  {
    "id": 58,
    "category": "Evaluation",
    "question": "Câu 58. Quan sát hai ma trận nhầm lẫn (Confusion Matrix) dưới đây:\n• Tập Huấn luyện (Train): Lớp A (450/460), B (430/450), C (460/474), D (470/480) - Tỉ lệ xấp xỉ 1.02 : 1 : 1.05 : 1.07\n• Tập Kiểm tra (Test): Mỗi lớp có đúng 100 mẫu (80 đúng lớp A, 70 đúng lớp B, 65 đúng lớp C, 70 đúng lớp D) - Tỉ lệ 1 : 1 : 1 : 1\n\nNhận định nào sau đây là chính xác nhất trong số các lựa chọn được đưa ra?",
    "options": [
      "A. Mô hình có dấu hiệu quá khớp (Overfiting)",
      "B. Mô hình có dấu hiệu kém khớp (Underfitting).",
      "C. Độ chính xác trên tập kiểm thử và huấn luyện là gần như tương đương nhau.",
      "D. Sai số chỉ do phân bố lớp khác nhau giữa hai tập."
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Phân bố lớp trên tập Train (tỉ lệ $1.02 : 1 : 1.05 : 1.07$) và tập Test (mỗi lớp đúng 100 mẫu, tỉ lệ $1 : 1 : 1 : 1$) có sự khác biệt rõ rệt về phân bố. Do đó, ma trận nhầm lẫn này phản ánh sự sai khác phân bố giữa hai tập dữ liệu."
  },
  {
    "id": 59,
    "category": "Machine Learning",
    "question": "Câu 59. Entropy cao có nghĩa là các phần phân chia trong thuật toán cây quyết định ID3 thì",
    "options": [
      "A. Thuần khiết (Pure): Các điểm dữ liệu ở mỗi nhánh của cây quyết định tập trung đa số vào một lớp",
      "B. Không có ý nghĩa gì",
      "C. Không thuần khiết (Not pure): Các điểm dữ liệu ở mỗi nhánh của cây quyết định phân bố tương đối đều\nvào các lớp",
      "D. Có thể suy ra độ đo F1-score cao"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất:** Trong lý thuyết thông tin và thuật toán ID3, **Entropy cao biểu thị mức độ hỗn loạn cao**, tức là tập dữ liệu tại nhánh đó **không thuần khiết (Not pure)**, các điểm dữ liệu phân bố đều vào nhiều lớp khác nhau (bất định cực đại khi phân bố đều)."
  },
  {
    "id": 60,
    "category": "Deep Learning",
    "question": "Câu 60. Mục đích của việc thêm nhiễu Gaussian vào dữ liệu đầu vào khi huấn luyện là gì?",
    "options": [
      "A. Giảm số lớp cần thiết",
      "B. Tăng tính ổn định và khả năng chống nhiễu",
      "C. Giảm thời gian huấn luyện",
      "D. Tăng độ chính xác"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Kỹ thuật thêm nhiễu Gaussian (Noise Injection) vào dữ liệu đầu vào hoặc trọng số đóng vai trò như một cơ chế chính quy hóa (regularization), giúp mô hình không bị quá phụ thuộc vào các giá trị pixel chính xác, từ đó **tăng tính ổn định và khả năng chống chịu nhiễu** trong môi trường thực tế."
  },
  {
    "id": 61,
    "category": "Deep Learning",
    "question": "Câu 61. Khi huấn luyện mạng GAN, nếu bộ tạo (generator) tạo ra ảnh toàn màu xám, nguyên nhân có thể là\ngì?",
    "options": [
      "A. Mất mát (loss) quá nhỏ",
      "B. Tỷ lệ học (learning rate) quá nhỏ",
      "C. Kích thước lô (batch size) quá lớn",
      "D. Mất cân bằng giữa bộ phân biệt (discriminator) và bộ tạo (generator)"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Trong mạng GAN, hiện tượng ảnh sinh ra bị toàn màu xám hoặc lặp lại một mẫu duy nhất (Mode Collapse) xảy ra do **sự mất cân bằng giữa bộ tạo (Generator) và bộ phân biệt (Discriminator)**: khi Discriminator học quá nhanh và áp đảo, gradient trả về cho Generator bị triệt tiêu, khiến Generator bị mắc kẹt tại một cực tiểu cục bộ."
  },
  {
    "id": 62,
    "category": "NLP & LLM",
    "question": "Câu 62. Trong bài toán phân loại văn bản, nếu mô hình học tốt các từ khóa rõ ràng nhưng không hiểu ngữ\ncảnh, phương pháp nào giúp cải thiện khả năng hiểu ngữ cảnh?",
    "options": [
      "A. Dùng mô hình dựa trên chú ý (attention-based) như BERT",
      "B. Bỏ nhúng (embedding), dùng vector gồm các số 0 và một số 1 (one-hot vector)",
      "C. Chuyển sang dùng TF-IDF",
      "D. Giảm số chiều nhúng (embedding)"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Để khắc phục hạn chế của các phương pháp thống kê từ khóa (TF-IDF, BoW) vốn không hiểu ngữ cảnh câu, giải pháp tối ưu là sử dụng **mô hình dựa trên cơ chế chú ý (Attention-based) như BERT**, cho phép biểu diễn từ thay đổi linh hoạt phụ thuộc vào toàn bộ câu văn xung quanh."
  },
  {
    "id": 63,
    "category": "Deep Learning",
    "question": "Câu 63. Nếu mô hình bị học quá mức (overfitting), phương pháp nào nên thử đầu tiên để giảm hiện tượng\nnày?",
    "options": [
      "A. Tăng số vòng lặp (epoch)",
      "B. Thêm bỏ ngẫu nhiên (dropout) hoặc tăng suy giảm trọng số (weight decay)",
      "C. Tăng tỷ lệ học (learning rate)",
      "D. Giảm kích thước lô (batch size)"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Khi mô hình bị quá khớp (Overfitting), hai kỹ thuật chính quy hóa kinh điển và nên thử đầu tiên là **thêm bỏ ngẫu nhiên (Dropout)** trong mạng nơ-ron hoặc **tăng suy giảm trọng số (Weight Decay / Regularization $L_2$)** để phạt các trọng số có độ lớn bất thường."
  },
  {
    "id": 64,
    "category": "Deep Learning",
    "question": "Câu 64. Khi huấn luyện, nếu độ chính xác huấn luyện (training accuracy) tăng đều nhưng độ chính xác kiểm\ntra (validation accuracy) dao động mạnh và không cải thiện, nguyên nhân có thể là gì?",
    "options": [
      "A. Học quá mức (overfitting) hoặc dữ liệu kiểm tra chưa được xáo trộn kỹ",
      "B. Không sử dụng bỏ ngẫu nhiên (dropout)",
      "C. Mô hình quá nhỏ",
      "D. Số vòng lặp (epoch) quá ít"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Hiện tượng Training accuracy tăng đều đặn (mô hình học thuộc lòng tập train) trong khi Validation accuracy dao động mạnh và không cải thiện là dấu hiệu kinh điển của **Quá khớp (Overfitting)**, hoặc do tập dữ liệu kiểm tra chưa được xáo trộn ngẫu nhiên đại diện cho phân bố."
  },
  {
    "id": 65,
    "category": "NLP & LLM",
    "question": "Câu 65. Mục tiêu chính khi tinh chỉnh (fine-tune) mô hình BERT cho bài toán phân loại văn bản là gì?",
    "options": [
      "A. Tạo nhúng (embedding)",
      "B. Thay lớp cuối bằng một lớp phân loại",
      "C. Dùng mô hình sinh",
      "D. Tạo một bộ mã hóa (tokenizer) mới"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Khi fine-tune mô hình BERT cho bài toán phân loại văn bản, biểu diễn của token đặc biệt `[CLS]` ở lớp cuối cùng đóng vai trò là vector tóm tắt ngữ cảnh toàn câu. Mục tiêu chính là **thay lớp cuối cùng bằng một lớp phân loại (Classification Head: Linear + Softmax)** để dự đoán nhãn mục tiêu."
  },
  {
    "id": 66,
    "category": "Deep Learning",
    "question": "Câu 66. Nếu tỷ lệ học (learning rate) quá cao, điều gì có thể xảy ra trong quá trình huấn luyện?",
    "options": [
      "A. Mô hình dao động và không hội tụ",
      "B. Tăng khả năng regularization",
      "C. Hàm mất mát giảm đều đặn",
      "D. Mô hình hội tụ nhanh hơn"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Nếu tốc độ học (learning rate) quá cao, bước nhảy cập nhật tham số $-\\eta \\nabla L$ sẽ quá lớn, khiến hàm mất mát nhảy vọt qua điểm cực tiểu và liên tục **dao động dữ dội hoặc phân kỳ không thể hội tụ**."
  },
  {
    "id": 67,
    "category": "Evaluation",
    "question": "Câu 67. Sự khác biệt giữa tập kiểm tra (test set) và tập xác thực (validation set) là gì?",
    "options": [
      "A. Tập xác thực là không cần thiết trong học máy.",
      "B. Tập xác thực dùng để điều chỉnh siêu tham số, còn tập kiểm tra dùng để đánh giá hiệu suất của mô hình.",
      "C. Tập xác thực và tập kiểm tra là một.",
      "D. Tập xác thực dùng để đánh giá hiệu suất mô hình trong quá trình huấn luyện, trong khi tập kiểm tra dùng\nđể đánh giá sau khi huấn luyện."
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Trong quy trình Machine Learning chuẩn mực:\n- **Tập xác thực (Validation set):** Dùng để đánh giá trong quá trình huấn luyện và điều chỉnh các siêu tham số (hyperparameters), chọn checkpoint tốt nhất (Early stopping).\n- **Tập kiểm tra (Test set):** Hoàn toàn độc lập, chỉ dùng một lần duy nhất ở bước cuối cùng để đánh giá khách quan hiệu năng thực tế của mô hình."
  },
  {
    "id": 68,
    "category": "Machine Learning",
    "question": "Câu 68. Xét một Random Forest gồm 𝐾 cây với nhiệm vụ hồi quy. Mỗi cây quyết định 𝑖 có thể biểu diễn một\nhàm 𝑇𝑖(𝑥) của đầu vào 𝑥. Random Forest này biểu diễn hàm nào sau đây?\n𝐾",
    "options": [
      "A. 𝑦(𝑥)=∑𝑇𝑖(𝑥)\n𝑖=1\n𝐾",
      "B. 𝑦(𝑥)= max\n𝑖∈{1,…,𝐾}\n𝑇𝑖(𝑥)",
      "C. 𝑦(𝑥)=∑𝑇𝑖 (𝑥\n𝐾)\n𝑖=1\n𝐾\n1",
      "D. 𝑦(𝑥)=\n𝐾∑𝑇𝑖(𝑥)\n𝑖=1"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Đối với bài toán hồi quy, mô hình Rừng ngẫu nhiên (Random Forest) gồm $K$ cây quyết định độc lập sẽ đưa ra dự đoán bằng **trung bình cộng kết quả của tất cả $K$ cây**: $y(x) = \\frac{1}{K} \\sum_{i=1}^K T_i(x)$."
  },
  {
    "id": 69,
    "category": "NLP & LLM",
    "question": "Câu 69. Để tải nhúng từ (embedding) Word2Vec đã được huấn luyện trước trong thư viện gensim, bạn sử dụng\nlệnh nào?",
    "options": [
      "A. gensim.models.load(\"word2vec\")",
      "B. import word2vec.load_model(path)",
      "C. KeyedVectors.load_word2vec_format(path)",
      "D. spacy.load_word2vec(path)"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất:** Trong thư viện `gensim`, để tải mô hình nhúng từ Word2Vec đã được huấn luyện trước (định dạng nhị phân hoặc text), lệnh chuẩn là: `from gensim.models import KeyedVectors; model = KeyedVectors.load_word2vec_format(path)`."
  },
  {
    "id": 70,
    "category": "Deep Learning",
    "question": "Câu 70. Khi sử dụng câu lệnh nn.CrossEntropyLoss trong PyTorch, bạn nên đưa gì vào đối số đầu tiên?",
    "options": [
      "A. Logits do lớp cuối cùng của mạng tạo ra",
      "B. Vector gồm các số 0 và một số 1 (one-hot vector) biểu diễn các lớp mục tiêu",
      "C. Xác suất thu được sau khi áp dụng softmax lên đầu ra của mạng",
      "D. Log-xác suất sau khi áp dụng log_softmax lên đầu ra của mạng"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Trong PyTorch, hàm `nn.CrossEntropyLoss()` đã tích hợp sẵn hàm `LogSoftmax` và `NLLLoss` bên trong để tối ưu ổn định số học. Do đó, đối số đầu tiên truyền vào phải là **Logits thô do lớp tuyến tính cuối cùng của mạng tạo ra** (chưa qua hàm Softmax)."
  },
  {
    "id": 71,
    "category": "Deep Learning",
    "question": "Câu 71. Trong huấn luyện, nếu mất mát huấn luyện (training loss) giảm nhưng mất mát kiểm tra (validation\nloss) tăng, điều này cho thấy gì?",
    "options": [
      "A. Mô hình đang học quá mức (overfitting)",
      "B. Mô hình đang hội tụ",
      "C. Cần tăng tỷ lệ học (learning rate)",
      "D. Mô hình học chưa đủ (underfitting)"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Khi Training loss tiếp tục giảm (mô hình khớp ngày càng sát tập train) nhưng Validation loss bắt đầu tăng lên (mô hình đoán sai nhiều hơn trên tập kiểm thử), đây là dấu hiệu định nghĩa của hiện tượng **Quá khớp (Overfitting)**."
  },
  {
    "id": 72,
    "category": "Computer Vision",
    "question": "Câu 72. Trong các bài toán phân đoạn ảnh (image segmentation), một thách thức phổ biến là sự mất cân bằng\nnghiêm trọng giữa các lớp. Ví dụ, diện tích của đối tượng cần phân đoạn (lớp tiền cảnh – foreground) có thể\nrất nhỏ so với phần còn lại của ảnh (lớp hậu cảnh – background). Khi gặp tình huống mất cân bằng lớp như\nvậy, hàm mất mát (loss function) nào trong số các lựa chọn dưới đây thường được xem là hiệu quả hơn và\nđược ưu tiên sử dụng thay cho hàm Cross-Entropy (CE) tiêu chuẩn?",
    "options": [
      "A. Mean Squared Error (MSE)",
      "B. Hinge Loss",
      "C. 𝐿1 Loss",
      "D. Dice Loss hoặc Focal Loss"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Trong phân đoạn ảnh (Semantic Segmentation) khi lớp tiền cảnh (vật thể) chiếm diện tích rất nhỏ so với hậu cảnh (mất cân bằng lớp nặng), Cross-Entropy tiêu chuẩn bị hậu cảnh lấn át. Các hàm mất mát chuyên biệt như **Dice Loss (tối ưu hóa hệ số tương đồng IoU/F1)** hoặc **Focal Loss (giảm trọng số các pixel dễ)** đem lại hiệu năng vượt trội."
  },
  {
    "id": 73,
    "category": "Computer Vision",
    "question": "Câu 73. Mạng nơ-ron ResNet sử dụng một kỹ thuật quan trọng gọi là kết nối tắt (skip connection) để giải\nquyết hiện tượng biến mất đạo hàm (Vanishing Gradient) trong quá trình huấn luyện. Dựa trên đoạn mã của\n\nkhối identity_block dưới đây, hãy liệt kê các thành phần chính của khối theo đúng thứ tự xuất hiện và chỉ\nra dòng mã thực hiện phép kết nối tắt.\n1 def identity_block(X, f, filters, stage, block):\n2\n3 conv_name_base = 'res' + str(stage) + block + '_branch'\n4 bn_name_base = 'bn' + str(stage) + block + '_branch'\n5\n6 F1, F2, F3 = filters\n7\n8 X_shortcut = X\n9\n10 X = BatchNormalization(axis = 3, name = bn_name_base + '2b')(X)\nX = Conv2D(filters = F1, kernel_size = (1, 1), strides = (1, 1), padding =\n'valid', name = conv_name_base + '2a', kernel_initializer = glorot_uniform(seed =\n0))(X)\n11 12 13\n14 X = BatchNormalization(axis = 3, name = bn_name_base + '2a')(X)\nX = Activation('relu')(X)\nX = Conv2D(filters = F2, kernel_size = (1, 1), strides = (1, 1), padding =\n'same', name = conv_name_base + '2b', kernel_initializer = glorot_uniform(seed =\n0))(X)\n15 16 17\n18 X = Activation('relu')(X)\nX = Conv2D(filters = F3, kernel_size = (1, 1), strides = (1, 1), padding =\n'valid', name = conv_name_base + '2c', kernel_initializer = glorot_uniform(seed =\n0))(X)\nX = BatchNormalization(axis = 3, name = bn_name_base + '2c')(X)\nX = Add()([X_shortcut, X])\nX = Activation('relu')(X)\nreturn X\n19 20\n21 22 23\n24",
    "options": [
      "A. Ba cặp Conv2D − BatchNorm − ReLU; kết nối tắt ở dòng ở dòng 8.",
      "B. Hai cặp Conv2D − BatchNorm − ReLU; kết nối tắt nằm trong BatchNorm ở dòng 11,15,19.",
      "C. Ba cặp Conv2D − BatchNorm − ReLU; Không có cơ chế kết nối tắt ở dòng.",
      "D. Ba cặp Conv2D − BatchNorm − ReLU; kết nối tắt ở dòng 21."
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Trong khối `identity_block` của ResNet, luồng chính đi qua ba cặp Conv2D - BatchNorm - ReLU. Phép kết nối tắt (skip connection) lấy tensor đầu vào ban đầu $X_{\\text{shortcut}}$ cộng với tensor đặc trưng sau 3 lớp tích chập được thực hiện tại **dòng 21: `X = Add()([X_shortcut, X])`**."
  },
  {
    "id": 74,
    "category": "NLP & LLM",
    "question": "Câu 74. Trong mô hình Transformer, cơ chế chú ý (attention) giúp mô hình làm gì?",
    "options": [
      "A. Tự động sinh từ tiếp theo",
      "B. Tập trung vào phần quan trọng của câu khi tính toán",
      "C. Xác định vị trí từ trong câu",
      "D. Chuẩn hóa đầu vào"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Cơ chế chú ý (Attention Mechanism) trong Transformer cho phép mỗi vị trí token trong chuỗi tính toán trọng số tương quan với tất cả các token khác, giúp mô hình **tập trung vào các phần quan trọng và có liên quan ngữ nghĩa nhất của câu** khi sinh biểu diễn."
  },
  {
    "id": 75,
    "category": "Computer Vision",
    "question": "Câu 75. Trong các kiến trúc mạng phân đoạn ảnh dạng bộ mã hóa – bộ giải mã (encoder – decoder), ví dụ\nnhư U-Net, các \"kết nối tắt\" (skip connections) đóng vai trò quan trọng. Chúng kết hợp thông tin đặc trưng từ\ncác lớp ở bộ mã hóa (encoder path) với thông tin tương ứng ở bộ giải mã (decoder path) sau khi được phóng\nđại (upsampling). Điều này giúp mô hình giữ lại các chi tiết không gian có độ phân giải cao bị mất trong quá\ntrình mã hóa.\nGiả sử bạn đang xây dựng một lớp trong phần bộ giải mã của mạng U-Net bằng Python, sử dụng một\nframework học sâu như TensorFlow/Keras hoặc PyTorch. Bạn có hai tensor:\n- encoder_output: Tensor chứa các đặc trưng từ một lớp tương ứng ở bộ mã hóa.\n- decoder_input: Tensor đầu vào cho lớp hiện tại ở bộ giải mã, đã được upsample để có cùng kích thước\nchiều cao (𝐻) và chiều rộng (𝑊) với encoder_output.\n1\n4\n2 # encoder_output.shape = (batch, H, W, C1) in TF/Keras or (batch, C1, H, W) in\nPytorch\n3 # decoder_input.shape = (batch, H, W, C2) in TF/Keras or (batch, C2, H, W) in\nPytorch\n5 merged_features = some_concatenation_operation([decoder_input,\nencoder_output], axis = …)\n\nThao tác some_concatenation_operation và tham số axis phù hợp nhất để thực hiện kết nối tắt (skip\nconnection) kiểu U-Net là gì?",
    "options": [
      "A. Phép nối (Concatenation) và axis dọc theo chiều batch",
      "B. Phép nối (Concatenation) và axis dọc theo chiều kênh (channel dimension)",
      "C. Phép cộng element-wise và axis không quan trọng",
      "D. Phép nhân element-wise và axis không quan trọng"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Trong kiến trúc U-Net, kết nối tắt giữa đường dẫn mã hóa (Encoder) và giải mã (Decoder) kết hợp các đặc trưng bằng **phép nối (Concatenation) dọc theo chiều kênh (channel dimension: axis=3 trong Keras, dim=1 trong PyTorch)** để truyền toàn vẹn chi tiết không gian độ phân giải cao sang tầng giải mã."
  },
  {
    "id": 76,
    "category": "NLP & LLM",
    "question": "Câu 76. Mô hình ngôn ngữ lớn (Large Language Model – LLM) là gì?",
    "options": [
      "A. Một công cụ tìm kiếm dựa trên quy tắc",
      "B. Một mô hình học sâu được huấn luyện trên lượng lớn dữ liệu văn bản để dự đoán từ tiếp theo trong một\nchuỗi",
      "C. Một hệ thống học tăng cường chuyên cho bài toán xử lý ngôn ngữ",
      "D. Một cơ sở dữ liệu ngữ nghĩa với các quan hệ giữa từ"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Mô hình ngôn ngữ lớn (LLM như GPT) về bản chất là một mạng nơ-ron học sâu được huấn luyện theo phương pháp tự giám sát trên kho ngữ liệu khổng lồ với mục tiêu **dự đoán từ tiếp theo trong chuỗi (Next-token prediction / Causal Language Modeling)**."
  },
  {
    "id": 77,
    "category": "Deep Learning",
    "question": "Câu 77. Stable Diffusion thuộc loại mô hình nào trong các lựa chọn sau?",
    "options": [
      "A. Bộ chuyển đổi (Transformer)",
      "B. Mô hình khuếch tán (Diffusion Model)",
      "C. GAN",
      "D. Bộ mã hóa tự động (autoencoder)"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Stable Diffusion hoạt động trên không gian tiềm ẩn (Latent Diffusion) nhờ vào một **bộ mã hóa tự động biến phân (Variational Autoencoder - VAE)** để nén ảnh gốc từ không gian pixel xuống không gian tiềm ẩn nhỏ hơn, nơi quá trình khuếch tán và khử nhiễu diễn ra hiệu quả."
  },
  {
    "id": 78,
    "category": "Deep Learning",
    "question": "Câu 78. Để áp dụng kỹ thuật dừng sớm (Early Stopping) trong huấn luyện, bạn cần theo dõi chỉ số nào để\nquyết định dừng huấn luyện?",
    "options": [
      "A. Mất mát kiểm tra (validation loss) hoặc độ chính xác kiểm tra (validation accuracy)",
      "B. Tỷ lệ học (learning rate)",
      "C. Số vòng lặp (epoch count)",
      "D. Mất mát huấn luyện (training loss)"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Kỹ thuật dừng sớm (Early Stopping) giám sát hiệu năng trên tập kiểm thử để tránh overfitting. Chỉ số chuẩn cần theo dõi là **mất mát kiểm tra (Validation Loss)** hoặc **độ chính xác kiểm tra (Validation Accuracy)**. Khi validation loss không giảm sau một số epoch quy định (`patience`), quá trình huấn luyện sẽ dừng lại."
  },
  {
    "id": 79,
    "category": "Deep Learning",
    "question": "Câu 79. Lệnh nào dùng để chuyển mô hình sang GPU?",
    "options": [
      "A. model.gpu()",
      "B. model.to('cuda')",
      "C. model.cuda.enable()",
      "D. model.device('GPU')"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Trong PyTorch, lệnh chuẩn mực và an toàn nhất để chuyển toàn bộ tham số và bộ đệm của mô hình sang GPU là: `model.to('cuda')` (hoặc `model.cuda()`)."
  },
  {
    "id": 80,
    "category": "Evaluation",
    "question": "Câu 80. Hàm chi phí sử dụng MSE (mean squared error) từ dữ liệu sau là bao nhiêu?\nGiá trị kỳ vọng Giá trị thực tế",
    "options": [
      "A. 8.5",
      "B. 6.5",
      "C. 5.5",
      "D. 7.5"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Tính sai số bình phương trung bình (MSE):**\n- Giá trị kỳ vọng: $[15, 17, 10, 26, 14, 12, 11, 13]$\n- Giá trị thực tế: $[12, 19, 15, 24, 13, 14, 8, 11]$\n- Sai số $(x - \\hat{x})$: $[-3, 2, 5, -2, -1, 2, -3, -2]$\n- Bình phương $(x - \\hat{x})^2$: $[9, 4, 25, 4, 1, 4, 9, 4]$\n$$\\text{MSE} = \\frac{9 + 4 + 25 + 4 + 1 + 4 + 9 + 4}{8} = \\frac{60}{8} = 7.5.$$"
  },
  {
    "id": 81,
    "category": "NLP & LLM",
    "question": "Câu 81. Thư viện LangChain được sử dụng để làm gì?",
    "options": [
      "A. Phân tích âm thanh",
      "B. Dịch máy",
      "C. Sinh văn bản ngẫu nhiên",
      "D. Kết nối và xây dựng quy trình cho tác nhân ngôn ngữ lớn (LLM agent pipeline)"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** **LangChain** là một framework mã nguồn mở được thiết kế chuyên biệt để **kết nối, tích hợp và xây dựng các quy trình tự động hóa cho các mô hình ngôn ngữ lớn (LLM Agent Pipelines)**, cung cấp các thành phần như Chains, Prompt Templates, Memory, Retrievers và Tools."
  },
  {
    "id": 82,
    "category": "Machine Learning",
    "question": "Câu 82. Trong mô hình hồi quy logistic sử dụng scikit-learn, thuộc tính nào chứa trọng số đã học của mô\nhình?",
    "options": [
      "A. model.weights",
      "B. model.intercept",
      "C. model.coefficients",
      "D. model.coef"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Trong thư viện Scikit-learn, sau khi khớp mô hình Logistic Regression (`LogisticRegression().fit(X, y)`), vector trọng số đã học của các đặc trưng được lưu trữ trong thuộc tính **`model.coef_`** (và hệ số chặn lưu trong `model.intercept_`)."
  },
  {
    "id": 83,
    "category": "Clustering",
    "question": "Câu 83. Bạn đang phát triển một hệ thống phân tích ảnh vệ tinh để xác định các loại cây trồng khác nhau trong\nmột khu vực nông nghiệp rộng lớn. Sau khi tiền xử lý và trích xuất đặc trưng từ ảnh đa phổ, bạn áp dụng một\nmô hình phân cụm (clustering) dựa trên thuật toán 𝐾-means để phân đoạn các vùng có khả năng chứa cùng một\nloại cây trồng.\nGiả sử sau khi chạy thuật toán 𝐾-means với 𝐾 =3, bạn thu được ba cụm 𝐶1,𝐶2,𝐶3 đại diện cho ba loại cây\ntrồng tiềm năng. Để đánh giá chất lượng phân cụm, bạn quyết định sử dụng một biến thể của Silhouette\nCoefficient.\n𝑏(𝑖)−𝑎(𝑖)\nSilhouette Coefficient cho một điểm dữ liệu 𝑖 được định nghĩa là: 𝑠(𝑖)=\nmax(𝑎(𝑖),𝑏(𝑖)), trong đó 𝑎(𝑖) là\nkhoảng cách trung bình từ điểm 𝑖 đến tất cả các điểm khác trong cùng cụm. 𝑏(𝑖) là khoảng cách trung bình từ\nđiểm 𝑖 đến tất cả các điểm trong cụm lân cận gần nhất (khác với cụm của 𝑖).\nTrong trường hợp đang xét, mỗi pixel trong ảnh sau khi trích xuất đặc trưng có thể được coi là một điểm dữ\n15 17 10 26 14 12 11 13\n12 19 15 24 13 14 8 11\n\nliệu trong không gian đặc trưng nhiều chiều. Giả sử bạn chọn ngẫu nhiên một pixel 𝑝 thuộc cụm 𝐶1. Sau khi\ntính toán, bạn có các giá trị sau:\n- Khoảng cách trung bình từ pixel 𝑝 đến tất cả các pixel khác trong cụm 𝐶1 là 𝑎(𝑝)=0.35.\n- Khoảng cách trung bình từ pixel 𝑝 đến tất cả các pixel trong cụm 𝐶2 là 𝑑(𝑝,𝐶2)=0.60.\n- Khoảng cách trung bình từ pixel 𝑝 đến tất cả các pixel trong cụm 𝐶3 là 𝑑(𝑝,𝐶3)=0.45.\nBiết rằng 𝑏(𝑝) là khoảng cách trung bình nhỏ nhất từ pixel 𝑝 đến các điểm trong một cụm khác với cụm chứa 𝑝.\nHãy tính Silhouette Coefficient 𝑠(𝑝) cho pixel 𝑝.",
    "options": [
      "A. 0.0",
      "B. 0.222",
      "C. 0.125",
      "D. 0.308"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Tính hệ số Silhouette Coefficient $s(p)$:**\n- Khoảng cách trung bình nội cụm $C_1$: $a(p) = 0.35$.\n- Khoảng cách trung bình đến các cụm khác: $d(p, C_2) = 0.60$, $d(p, C_3) = 0.45$.\n- Khoảng cách đến cụm lân cận gần nhất: $b(p) = \\min(0.60, 0.45) = 0.45$.\n$$s(p) = \\frac{b(p) - a(p)}{\\max(a(p), b(p))} = \\frac{0.45 - 0.35}{\\max(0.35, 0.45)} = \\frac{0.10}{0.45} = \\frac{2}{9} \\approx 0.222.$$"
  },
  {
    "id": 84,
    "category": "Deep Learning",
    "question": "Câu 84. Nếu khởi tạo trọng số (weight initialization) không phù hợp, hiện tượng nào có thể xảy ra trong quá\ntrình huấn luyện?",
    "options": [
      "A. Mô hình học nhanh hơn.",
      "B. Không ảnh hưởng vì bộ tối ưu sẽ điều chỉnh.",
      "C. Học quá mức nhẹ (overfitting).",
      "D. Gradient biến mất (vanishing) hoặc nổ (exploding)."
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Khởi tạo trọng số không phù hợp là nguyên nhân trực tiếp dẫn tới hiện tượng **Gradient biến mất (Vanishing Gradient)** nếu trọng số quá nhỏ (các tầng sâu nhận gradient xấp xỉ 0) hoặc **Gradient bùng nổ (Exploding Gradient)** nếu trọng số quá lớn, khiến mạng mất ổn định và không thể huấn luyện."
  },
  {
    "id": 85,
    "category": "Evaluation",
    "question": "Câu 85. Để đánh giá mô hình phân loại ảnh với các lớp không cân bằng, chỉ số nào nên dùng thay vì chỉ độ\nchính xác (accuracy)?",
    "options": [
      "A. AUC (Area Under the Curve)",
      "B. Điểm F1 trung bình (Macro F1-score)",
      "C. RMSE (Root mean square error)",
      "D. Độ chính xác cao nhất (Top-1 accuracy)"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A và B**\n\n• **Bản chất:** Khi các lớp mất cân bằng nặng (ví dụ 99% lớp âm, 1% lớp dương), độ chính xác (Accuracy) dễ bị đánh lừa (mô hình đoán toàn bộ là âm vẫn đạt 99% Acc). Hai chỉ số chuẩn mực thay thế là **AUC (Area Under ROC Curve - A)** và **Điểm F1 trung bình (Macro F1-score - B)** vì chúng đánh giá công bằng hiệu năng trên từng lớp."
  },
  {
    "id": 86,
    "category": "Deep Learning",
    "question": "Câu 86. Sau khi huấn luyện mô hình phân loại với độ chính xác 90 %, khách hàng muốn triển khai thực tế.\nViệc cần làm tiếp theo là gì?",
    "options": [
      "A. Nén ảnh đầu vào.",
      "B. Chuyển mô hình sang TensorRT/ONNX để triển khai (deploy).",
      "C. Tăng thêm số vòng lặp (epoch) để đạt 95 %.",
      "D. Thay mô hình sang BERT"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Khi mô hình đã huấn luyện xong đạt độ chính xác yêu cầu và sẵn sàng đưa vào môi trường sản xuất thực tế, bước kỹ thuật tiếp theo là tối ưu hóa suy luận bằng cách **chuyển đổi mô hình sang định dạng chuẩn trung gian ONNX hoặc tối ưu hóa phần cứng bằng NVIDIA TensorRT** để đạt thông lượng cao và độ trễ thấp."
  },
  {
    "id": 87,
    "category": "Computer Vision",
    "question": "Câu 87. Khi xử lý dữ liệu ảnh, nếu một số ảnh bị hỏng (không mở được), cách tốt nhất để xử lý khi huấn luyện\nlà gì?",
    "options": [
      "A. Tăng kích thước lô (batch size) để bù lại",
      "B. Bỏ qua toàn bộ thư mục chứa ảnh đó",
      "C. Bắt lỗi khi tải ảnh và bỏ qua ảnh bị hỏng",
      "D. Dừng toàn bộ huấn luyện"
    ],
    "correctIndex": 0,
    "explanation": "**Đáp án đúng: A**\n\n• **Bản chất:** Khi huấn luyện trên tập dữ liệu ảnh quy mô cực lớn (hàng triệu ảnh), việc xuất hiện một vài file ảnh bị hỏng là điều khó tránh. Cách xử lý chuẩn là **bắt lỗi ngoại lệ (try-catch) khi tải ảnh và bỏ qua ảnh hỏng**, tiếp tục huấn luyện mà không làm gián đoạn toàn bộ hệ thống."
  },
  {
    "id": 88,
    "category": "Deep Learning",
    "question": "Câu 88. Trong PyTorch, để thêm lớp bỏ ngẫu nhiên (dropout) với xác suất 0.5 vào mạng nơ-ron, bạn sử dụng\nlệnh nào?",
    "options": [
      "A. F.dropout(0.5)",
      "B. nn.dropout(0.5)",
      "C. nn.Dropout(p=0.5)",
      "D. nn.Dropout2d(0.5)"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất:** Trong PyTorch, lớp Dropout ngẫu nhiên triệt tiêu các kết nối neuron với xác suất $p=0.5$ được định nghĩa chuẩn xác bằng cú pháp module: **`nn.Dropout(p=0.5)`** (hoặc `nn.Dropout(0.5)`)."
  },
  {
    "id": 89,
    "category": "Evaluation",
    "question": "Câu 89. Hãy xem xét một công cụ phát hiện các gói tin chứa mối đe dọa trong trường hợp chỉ có một số lượng\nnhỏ gói là mối đe dọa. Yêu cầu là công cụ cần phát hiện các gói đe dọa mà không bỏ sót gói nào. Đâu là độ\nđo quan trọng nhất để đánh giá công cụ?",
    "options": [
      "A. Accuracy",
      "B. 𝐹1",
      "C. Recall",
      "D. Precision"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất:** Yêu cầu bài toán là 'phát hiện các gói đe dọa mà không bỏ sót gói nào', nghĩa là số lượng trường hợp đe dọa bị bỏ qua (False Negatives - FN) phải xấp xỉ bằng 0. Độ đo phản ánh trực tiếp khả năng không bỏ sót này là **Độ thu hồi (Recall = TP / (TP + FN))**."
  },
  {
    "id": 90,
    "category": "Machine Learning",
    "question": "Câu 90. Phương pháp nào dưới đây mà việc chuẩn hóa các thuộc tính dữ liệu đầu vào không ảnh hưởng đến\nkết quả dự đoán?",
    "options": [
      "A. Mạng nơ-ron (Neural Networks)",
      "B. Cây quyết định",
      "C. Soft-margin SVM",
      "D. 𝑘-NN"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** **Cây quyết định (Decision Tree)** phân tách dữ liệu bằng cách so sánh từng thuộc tính đơn lẻ với ngưỡng phân chia ($x_j \\le \\theta$). Khi chuẩn hóa (Scaling/Normalization), thứ tự tương đối giữa các giá trị không đổi nên các điểm phân chia tối ưu vẫn giữ nguyên tính chất, **hoàn toàn không ảnh hưởng đến cấu trúc cây hay kết quả dự đoán**."
  },
  {
    "id": 91,
    "category": "NLP & LLM",
    "question": "Câu 91. Mục tiêu huấn luyện của mô hình CBOW (Continuous Bag-of-Words) là gì?",
    "options": [
      "A. Sử dụng toàn bộ văn bản để dự đoán một từ bất kỳ",
      "B. Sử dụng vị trí của từ trong câu để dự đoán nghĩa của câu",
      "C. Sử dụng các từ xung quanh để dự đoán từ trung tâm",
      "D. Sử dụng từ trung tâm để dự đoán các từ xung quanh"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất:** Trong kiến trúc Word2Vec, mô hình **CBOW (Continuous Bag-of-Words)** có mục tiêu là **sử dụng các từ ngữ cảnh xung quanh (Context words) để dự đoán từ trung tâm (Target word)**. Ngược lại, mô hình Skip-gram dùng từ trung tâm để dự đoán các từ ngữ cảnh xung quanh."
  },
  {
    "id": 92,
    "category": "Deep Learning",
    "question": "Câu 92. Mục tiêu chính của phương pháp học tương phản (contrastive learning) trong lĩnh vực học tự giám\nsát (self-supervised learning) là gì?",
    "options": [
      "A. Tối thiểu hoá khoảng cách Euclidean giữa mọi cặp ảnh trong batch\n\n𝐴⋅𝐵",
      "B. Khôi phục ảnh gốc từ ảnh đã bị thêm nhiễu Gaussian",
      "C. Đưa các ảnh được biến đổi từ cùng một ảnh gốc thông qua các phép biến đổi cơ bản tới gần nhau, đẩy\ncác mẫu lấy từ các ảnh khác nhau xa nhau trên không gian biểu diễn (embedding space)",
      "D. Tối ưu hoá hàm cross-entropy có nhãn đầy đủ"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất:** Mục tiêu cốt lõi của Học tương phản (Contrastive Learning) trong học tự giám sát là **kéo các biểu diễn của các ảnh được biến đổi từ cùng một ảnh gốc lại gần nhau trong không gian nhúng**, đồng thời **đẩy các biểu diễn của các ảnh khác nhau ra xa nhau**."
  },
  {
    "id": 93,
    "category": "Deep Learning",
    "question": "Câu 93. Điểm khác biệt chính giữa Stochastic Gradient Descent (SGD) và Mini-Batch Gradient Descent là\ngì?",
    "options": [
      "A. SGD luôn hội tụ nhanh hơn",
      "B. Mini-Batch Gradient Descent là một thuật toán hoàn toàn khác",
      "C. SGD không dùng được trong mạng nơ-ron",
      "D. SGD cập nhật tham số sau mỗi mẫu dữ liệu, Mini-Batch thì sau một nhóm mẫu"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Điểm khác biệt mấu chốt giữa hai thuật toán: **SGD thuần túy (Stochastic Gradient Descent) cập nhật tham số sau mỗi mẫu dữ liệu đơn lẻ**, trong khi **Mini-Batch Gradient Descent cập nhật tham số sau một nhóm mẫu (lô nhỏ)**."
  },
  {
    "id": 94,
    "category": "Calculus",
    "question": "Câu 94. Giả sử các từ được biểu diễn bởi các vector 4 chiều như sau:\n𝑤1 =[0.8,0.6,0.0,0.2]\n𝑤2 =[0.9,0.5,0.1,0.3]\n𝑤3 =[1.0,0.1,0.0,0.0]\n𝑤4 =[0.0,0.1,0.9,0.3]\nHãy tính độ tương đồng cosine giữa 𝑤1 và các từ còn lại (𝑤2,𝑤3,𝑤4), sau đó chọn từ gần nhất với 𝑤1. Công\nthức tính cosine similarity giữa hai vector 𝐴 và 𝐵 là:\ncosine−similarity(𝐴,𝐵)=\n|𝐴|×|𝐵|\nVới: 𝐴⋅𝐵 là tích vô hướng giữa hai vector, |𝐴| là độ dài của vector 𝐴, tính bằng căn bậc hai tổng bình phương\ncác thành phần.",
    "options": [
      "A. Có nhiều hơn một từ gần nhất với 𝑤1",
      "B. 𝑤3",
      "C. 𝑤4",
      "D. 𝑤2"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Tính Cosine Similarity giữa $w_1=[0.8, 0.6, 0.0, 0.2]$ và các vector:**\n- Độ dài $|w_1| = \\sqrt{0.64+0.36+0+0.04} = \\sqrt{1.04} \\approx 1.0198$.\n- Với $w_2=[0.9, 0.5, 0.1, 0.3]$: $|w_2| = \\sqrt{0.81+0.25+0.01+0.09} = \\sqrt{1.16} \\approx 1.0770$.\n  Tích vô hướng $w_1 \\cdot w_2 = 0.8(0.9) + 0.6(0.5) + 0 + 0.2(0.3) = 1.08$.\n  $\\cos(w_1, w_2) = \\frac{1.08}{1.0198 \\times 1.0770} \\approx 0.983$ (cao nhất).\n• **Kết luận:** Từ $w_2$ gần nhất với $w_1$."
  },
  {
    "id": 95,
    "category": "Deep Learning",
    "question": "Câu 95. Mạng GAN bao gồm hai mạng chính nào?",
    "options": [
      "A. Bộ phát hiện (Detector) và Bộ phân đoạn (Segmentor)",
      "B. Bộ chuyển đổi (Transformer) và Cơ chế chú ý (Attention)",
      "C. Bộ mã hóa (Encoder) và Bộ giải mã (Decoder)",
      "D. Bộ tạo (Generator) và Bộ phân biệt (Discriminator)"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Mạng đối kháng tạo sinh (GAN) bao gồm hai mạng nơ-ron đối nghịch nhau trong trò chơi minimax: **Bộ tạo (Generator)** chuyên sinh ra các mẫu dữ liệu giả và **Bộ phân biệt (Discriminator)** chuyên phân biệt giữa mẫu thật từ dữ liệu và mẫu giả từ bộ tạo."
  },
  {
    "id": 96,
    "category": "Machine Learning",
    "question": "Câu 96. Quá khớp (Overfitting) có thể do",
    "options": [
      "A. Lựa chọn mô hình không phù hợp",
      "B. Độ phức tạp của bài toán học",
      "C. Một lỗi nào đó trong quá trình huấn luyện",
      "D. Nhiễu trong dữ liệu"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Quá khớp (Overfitting) xảy ra khi mô hình có độ phức tạp cao ghi nhớ quá mức cả **các thành phần nhiễu (noise) và dao động ngẫu nhiên** trong tập huấn luyện thay vì học quy luật tổng quát tiềm ẩn của dữ liệu, dẫn đến khả năng tổng quát kém trên dữ liệu mới."
  },
  {
    "id": 97,
    "category": "Deep Learning",
    "question": "Câu 97. Khi huấn luyện bộ mã hóa tự động (autoencoder), nếu ảnh đầu ra bị mờ, nguyên nhân có thể là gì?",
    "options": [
      "A. Bỏ ngẫu nhiên (dropout) quá thấp",
      "B. Bộ tối ưu sai",
      "C. Lớp ẩn quá nhỏ hoặc chính quy hóa (regularization) quá mạnh",
      "D. Kích thước lô (batch size) lớn"
    ],
    "correctIndex": 2,
    "explanation": "**Đáp án đúng: C**\n\n• **Bản chất:** Trong mạng Autoencoder, ảnh đầu ra bị mờ xảy ra khi **không gian tiềm ẩn (latent space) quá nhỏ hoặc chính quy hóa quá mạnh**, làm mất mát các thành phần tần số cao (chi tiết cạnh, góc sắc nét), khiến bộ giải mã chỉ tái tạo được dạng mờ trung bình của ảnh."
  },
  {
    "id": 98,
    "category": "NLP & LLM",
    "question": "Câu 98. Mô hình DALL ⋅ E có khả năng đặc biệt nào?",
    "options": [
      "A. Phân đoạn vật thể",
      "B. Sinh ảnh từ mô tả văn bản",
      "C. Nén ảnh thành vector",
      "D. Sinh mô tả từ ảnh"
    ],
    "correctIndex": 1,
    "explanation": "**Đáp án đúng: B**\n\n• **Bản chất:** Mô hình **DALL-E** (phát triển bởi OpenAI) là một mô hình tạo sinh đa phương thức kết hợp Transformer có khả năng đặc biệt là **sinh ra hình ảnh chất lượng cao và sáng tạo từ mô tả văn bản (Text-to-Image)**."
  },
  {
    "id": 99,
    "category": "NLP & LLM",
    "question": "Câu 99. Trong xử lý ngôn ngữ tự nhiên (NLP), mục đích chính của việc loại bỏ từ dừng (stopword) khỏi văn\nbản là gì?",
    "options": [
      "A. Để giảm số lượng từ trong tập huấn luyện",
      "B. Để tạo ra các câu hoàn chỉnh và rõ nghĩa hơn",
      "C. Để làm giảm độ phức tạp và tập trung vào các từ mang nội dung quan trọng",
      "D. Để giữ lại tất cả các từ giúp cải thiện độ chính xác"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Bản chất:** Trong xử lý ngôn ngữ tự nhiên (NLP), việc loại bỏ từ dừng (Stopwords: như 'the', 'is', 'và', 'của'...) giúp **giảm độ phức tạp tính toán và tập trung vào các từ mang nội dung và ý nghĩa phân biệt quan trọng** của văn bản."
  },
  {
    "id": 100,
    "category": "Machine Learning",
    "question": "Câu 100. Cho các tham số của mô hình SVM (Support Vector Machine) đã huấn luyện:\nVector trọng số: $w = [2, -3]$, độ lệch: $b = 1$.\nDữ liệu mẫu tại chỉ số 0: $(x_1, x_2) = (1, 2)$.\n\nDự đoán nhãn cho mẫu chỉ số 0 là gì?",
    "options": [
      "A. Không xác định được",
      "B. Không phân loại",
      "C. +1",
      "D. -1"
    ],
    "correctIndex": 3,
    "explanation": "**Đáp án đúng: D**\n\n• **Tính hàm quyết định SVM cho mẫu $(x_1, x_2) = (1, 2)$:**\nVới $w = [2, -3]$ và bias $b = 1$:\n$$o = w_1 x_1 + w_2 x_2 + b = 2(1) + (-3)(2) + 1 = 2 - 6 + 1 = -3$$\nVì $o < 0$, theo quy tắc phân loại của SVM $\\hat{y} = \\text{sign}(w^T x + b)$, nhãn dự đoán là **-1**."
  },
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
