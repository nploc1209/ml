# 📚 Sổ Tay Học Máy & Deep Learning (ML Handbook)

> **Giáo trình tương tác toàn diện từ con số 0 đến Deep Learning hiện đại.**  
> Chạy hoàn toàn tự do (100% Offline), tích hợp 78 chuyên đề sâu, 78 sơ đồ vector SVG, 11 bộ mô phỏng trực quan Canvas, bộ đề thi trắc nghiệm 24 câu có lời giải chi tiết, và lưu tiến trình học tự động vào LocalStorage.

---

## 🌟 Tính Năng Nổi Bật

1. **Sư Phạm Chuẩn Mực & Dẫn Dắt Từ Con Số 0**:
   - **13 bài học lớn**, chia thành **78 chuyên đề chi tiết** (mỗi bài đúng 6 phần chuẩn hóa).
   - **78 Trực giác thực tế** (Intuition): Dùng ví dụ đời sống để người mới bắt đầu không bỡ ngỡ.
   - **78 Hộp giải mã ký hiệu toán học**: Phân tách từng ký hiệu ($\sum, \mathbb{E}, \nabla, \partial, \in, \odot, \dots$) giúp bất kỳ ai cũng có thể đọc hiểu công thức.
   - **78 Sơ đồ kiến trúc vector SVG**: Trực quan hóa hình học, luồng dữ liệu tensor và mạng nơ-ron sắc nét trên mọi độ phân giải.
   - **78 Cạm bẫy phòng thi & thực tế (Pitfalls)**: Chỉ rõ lỗi sai học sinh / kỹ sư hay mắc phải.
   - **78 Câu hỏi kiểm tra hiểu bài (Checkpoints)**: Trắc nghiệm ngay sau mỗi phần kèm gợi ý và lời giải từng bước.

2. **11 Bộ Mô Phỏng Tương Tác Canvas (Interactive Simulators)**:
   - **Gradient Descent Simulator**: Tùy chỉnh tốc độ học $\eta$, điểm xuất phát $x_0$, quan sát hội tụ và hiện tượng phân kỳ.
   - **Cosine Similarity & Semantic Space**: Kéo góc 2 vector để trực quan hóa độ tương đồng góc trong NLP & Hệ thống gợi ý.
   - **Naive Bayes & Laplace Smoothing**: Phân tích xác suất từ ngữ trong lọc email Spam vs Ham.
   - **Linear, Ridge & Lasso Regression**: Quan sát hiệu ứng co rút trọng số $L_1, L_2$ và độ nhạy với ngoại lai (Outliers).
   - **Confusion Matrix & Metrics**: Tính Precision, Recall, F1-Score trên dữ liệu mất cân bằng nghiêm trọng.
   - **Entropy & Information Gain**: Đồ thị hàm Entropy nhị phán và cách Cây Quyết Định chọn ngưỡng cắt tốt nhất.
   - **k-NN Classifier**: Tương tác trực tiếp trên mặt phẳng 2D, chọn $k$ lẻ để giải quyết hòa phiếu.
   - **CNN Feature Map Calculator**: Tính kích thước ma trận đầu ra sau tích chập và max pooling.
   - **Multi-Head Self-Attention Matrix**: Mô phỏng ma trận trọng số chú ý trong kiến trúc Transformer.
   - **Forward & Backpropagation Step-by-Step**: Lan truyền tiến và lan truyền ngược trên mạng MLP nhiều tầng.
   - **Generative Diffusion Denoising**: Khử nhiễu từng bước từ Gauss trắng thành mẫu dữ liệu có cấu trúc.

3. **Toán Học Chuẩn Xác & Độc Lập 100% (Offline-First)**:
   - Bộ giải mã công thức toán tự xây dựng hỗ trợ đầy đủ hơn 90 lệnh LaTeX ($\frac{a}{b}$, $\sqrt{x}$, $\begin{bmatrix}\dots\end{bmatrix}$, $\begin{cases}\dots\end{cases}$, các chữ cái Hy Lạp, ký hiệu tập hợp, đạo hàm riêng, ma trận).
   - Tự động tích hợp thư viện KaTeX khi có kết nối mạng để đạt chất lượng ấn phẩm Springer/MIT Press, đồng thời hoạt động hoàn hảo khi mất mạng với 0 lỗi hiển thị.

4. **Tối Ưu Trải Nghiệm Di Động (Đặc Biệt Cho iPhone 13 & Màn Hình Nhỏ)**:
   - Tương thích hoàn hảo với màn hình chiều rộng từ **390px** (iPhone 13 / 14 / 15) đến màn hình Retina 4K.
   - Menu drawer trượt mượt mà có backdrop làm mờ và nút đóng riêng biệt.
   - Canvas và đồ thị tự động co giãn theo tỉ lệ khung hình (Aspect Ratio), hỗ trợ cả cảm ứng chạm (Touch) và chuột.
   - Nút bấm và lựa chọn đạt chuẩn chiều cao tối thiểu 44px của Apple Human Interface Guidelines.
   - Đảm bảo an toàn vùng khuyết tai thỏ / đảo động (Safe Area Insets).

5. **Lưu Tiến Trình Tự Động (LocalStorage)**:
   - Lưu bài học đang đọc dở dang — khi tải lại trang sẽ mở lại đúng vị trí.
   - Lưu các bài học đã hoàn thành cùng thanh tiến độ phần trăm trực quan.
   - Lưu trạng thái các câu hỏi kiểm tra và bộ đề thi trắc nghiệm 24 câu.
   - Có nút **Đặt lại tiến trình** khi muốn ôn tập lại từ đầu.

---

## 📖 Mục Lục Giáo Trình (13 Bài Học)

| Bài | Tên Bài Học | Bộ Mô Phỏng Tương Tác |
|:---:|:---|:---:|
| **01** | Đạo Hàm, Đạo Hàm Riêng & Vector Gradient | Gradient Descent 2D |
| **02** | Đại Số Tuyến Tính, Vector, Ma Trận & Tích Vô Hướng | Cosine Similarity |
| **03** | Xác Suất Thống Kê, Định Lý Bayes & Naive Bayes | Naive Bayes & Laplace |
| **04** | Tối Ưu Hóa Nâng Cao: SGD, Momentum & Adam | Optimizer Dynamics |
| **05** | Hồi Quy Tuyến Tính (Linear Regression) & Regularization | Ridge vs Lasso Shrinkage |
| **06** | Các Chỉ Số Đánh Giá (Metrics) & Dữ Liệu Mất Cân Bằng | Confusion Matrix & F1 |
| **07** | Cây Quyết Định (Decision Tree) & Kỹ Thuật Ensemble | Entropy & Information Gain |
| **08** | Máy Vector Hỗ Trợ (SVM), Kernel Trick & k-NN | k-NN Decision Boundary |
| **09** | Phân Cụm K-Means & Giảm Chiều Dữ Liệu PCA | Dimensionality Reduction |
| **10** | Mạng Nơ-ron (MLP) & Thuật Toán Lan Truyền Ngược | MLP Backprop Step-by-Step |
| **11** | Thị Giác Máy Tính: CNN, ResNet & Nhận Diện Vật Thể | CNN Feature Map & Stride |
| **12** | Xử Lý Ngôn Ngữ Tự Nhiên (NLP), Attention & LLMs | Self-Attention Heatmap |
| **13** | Học Tự Giám Sát, GANs & Mô Hình Khuếch Tán (Diffusion) | Denoising Diffusion Steps |

---

## 🚀 Hướng Dẫn Sử Dụng

### Cách 1: Sử Dụng Ngay (Không Cần Cài Đặt)
Chỉ cần nhấp đúp để mở tệp `index.html` trong bất kỳ trình duyệt web nào (Chrome, Safari, Firefox, Edge, Cốc Cốc) trên máy tính hoặc điện thoại của bạn. Không cần cài đặt máy chủ (web server) hay cài đặt Python/Node.js!

### Cách 2: Chạy Qua Local Server (Tùy Chọn)
Nếu muốn chạy qua HTTP server cục bộ:
```bash
# Sử dụng Python có sẵn:
python3 -m http.server 8000

# Sau đó mở trình duyệt tại:
# http://localhost:8000
```

---

## 🛠️ Biên Tập & Tái Tạo Mã Nguồn (Build Pipeline)

Mã nguồn được thiết kế theo kiến trúc module hóa:
- `lessons.js`: Chứa toàn bộ dữ liệu 13 bài học với 78 chuyên đề chi tiết.
- `styles.css`: Hệ thống giao diện phong cách báo in học thuật, tối ưu responsive.
- `app.js`: Xử lý logic ứng dụng, render toán học, điều hướng, và các simulator.
- `quiz.js`: Ngân hàng câu hỏi trắc nghiệm 24 câu chuẩn đề thi.

Khi bạn sửa đổi nội dung bài học hoặc giao diện, chạy các lệnh sau để tự động đóng gói:
```bash
# 1. Lắp ráp dữ liệu 13 bài học vào lessons.js:
python3 assemble_deep_lessons.py

# 2. Đóng gói toàn bộ CSS, JS và HTML thành 1 file index.html duy nhất (100% offline):
python3 bundle_index_html.py
```

---

## 📤 Hướng Dẫn Đẩy Lên GitHub & Kích Hoạt GitHub Pages

### Bước 1: Khởi tạo Git và Commit
Mở Terminal tại thư mục này và chạy các lệnh sau:

```bash
# 1. Khởi tạo kho chứa Git cục bộ (nếu chưa có)
git init

# 2. Thêm toàn bộ các file vào staging (đã tự động bỏ qua cache nhờ .gitignore)
git add .

# 3. Tạo commit đầu tiên
git commit -m "feat: complete master Machine Learning handbook with 13 deep lessons, responsive mobile UI, and offline math rendering"
```

### Bước 2: Liên kết với GitHub và Đẩy lên
Tạo một kho chứa mới (New Repository) trên [GitHub](https://github.com/new) (ví dụ đặt tên `ml-handbook` hoặc `ml`), sau đó chạy:

```bash
# 1. Đặt tên nhánh chính là main
git branch -M main

# 2. Thêm địa chỉ kho chứa từ xa của bạn (thay thế URL bằng link repo GitHub của bạn)
git remote add origin https://github.com/<USERNAME>/<REPO_NAME>.git

# 3. Đẩy mã nguồn lên GitHub
git push -u origin main
```

### Bước 3: Kích Hoạt Miễn Phí Trên GitHub Pages
Sau khi đẩy mã nguồn lên GitHub:
1. Vào trang Repository trên GitHub của bạn $\to$ Chọn thẻ **Settings**.
2. Chọn mục **Pages** ở thanh menu bên trái.
3. Dưới mục **Build and deployment**:
   - **Source**: Chọn `Deploy from a branch`.
   - **Branch**: Chọn `main`, thư mục là `/(root)`.
   - Bấm **Save**.
4. Chờ 1–2 phút, trang web của bạn sẽ được xuất bản công khai tại địa chỉ:  
   `https://<USERNAME>.github.io/<REPO_NAME>/`  
   Mọi người đều có thể truy cập và học tập trên điện thoại, máy tính bảng hay máy tính xách tay!

---

## 📄 Bản Quyền
Dự án được xây dựng phục vụ mục đích giáo dục phi thương mại và cộng đồng yêu thích Trí tuệ Nhân tạo & Học máy.
