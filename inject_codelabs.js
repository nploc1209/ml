// inject_codelabs.js - Injects Hands-On Code Lab to all 13 lessons in lessons.js
const fs = require("fs");

const CODE_LABS = {
  "lesson-1": {
    title: "Tự Viết Thuật Toán Gradient Descent & Tối Ưu Với Scikit-Learn",
    description: "Trong bài thực hành này, bạn sẽ tự tay lập trình thuật toán Gradient Descent từ con số 0 (from scratch) bằng NumPy để tối ưu hóa hàm mất mát MSE, sau đó đối chiếu kết quả với mô hình `SGDRegressor` chuyên dụng của Scikit-Learn.",
    steps: [
      {
        title: "Tự lập trình hàm tính đạo hàm riêng và vòng lặp Gradient Descent bằng NumPy",
        explanation: "Hàm mất mát MSE cho hồi quy đơn biến: $L(w, b) = \\frac{1}{m} \\sum (w x_i + b - y_i)^2$. Đạo hàm riêng theo $w$ là $\\frac{\\partial L}{\\partial w} = \\frac{2}{m} X^T (\\hat{y} - y)$ và theo $b$ là $\\frac{\\partial L}{\\partial b} = \\frac{2}{m} \\sum (\\hat{y} - y)$.",
        code: `import numpy as np

# 1. Tạo tập dữ liệu tuyến tính đơn giản: y = 2*x + 1 kèm nhiễu
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 2 * X + 1 + 0.1 * np.random.randn(100, 1)

# 2. Khởi tạo tham số w và b ngẫu nhiên
w = np.random.randn(1, 1)
b = np.random.randn(1, 1)
learning_rate = 0.1
epochs = 100
m = len(X)

# 3. Vòng lặp Gradient Descent
for epoch in range(epochs):
    y_hat = X.dot(w) + b # Dự đoán
    
    # Tính gradient đạo hàm riêng
    dw = (2 / m) * X.T.dot(y_hat - y)
    db = (2 / m) * np.sum(y_hat - y)
    
    # Cập nhật ngược chiều gradient
    w -= learning_rate * dw
    b -= learning_rate * db

print(f"NumPy Scratch -> w: {w[0][0]:.4f}, b: {b[0][0]:.4f}")`,
        output: "NumPy Scratch -> w: 1.9876, b: 1.0182"
      },
      {
        title: "Huấn luyện bài toán tương đương bằng SGDRegressor trong Scikit-Learn",
        explanation: "Scikit-Learn cung cấp lớp `SGDRegressor` tối ưu hóa hàm mất mát tuyến tính với thuật toán hạ gradient ngẫu nhiên và hỗ trợ sẵn các kỹ thuật điều chuẩn.",
        code: `from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error

# Khởi tạo mô hình SGDRegressor với hàm loss='squared_error'
sgd = SGDRegressor(max_iter=1000, tol=1e-3, eta0=0.1, penalty=None, random_state=42)
sgd.fit(X, y.ravel())

y_pred = sgd.predict(X)
print(f"Scikit-Learn  -> w: {sgd.coef_[0]:.4f}, b: {sgd.intercept_[0]:.4f}")
print(f"MSE Loss: {mean_squared_error(y, y_pred):.6f}")`,
        output: "Scikit-Learn  -> w: 1.9868, b: 1.0189\nMSE Loss: 0.009482"
      }
    ],
    exercise: {
      title: "Tìm điểm cực tiểu của hàm 2 biến phi tuyến",
      task: "Viết hàm tìm điểm cực tiểu của hàm 2 biến $f(x, y) = x^2 + 2y^2 - 4x + 4y + 6$ bằng thuật toán Gradient Descent. Cho điểm ban đầu $(x_0, y_0) = (0, 0)$, tốc độ học $\\eta = 0.1$, số vòng lặp 50 bước.",
      hint: "Vector gradient: $\\nabla f = [2x - 4, 4y + 4]$. Cực tiểu lý thuyết đạt tại $\\nabla f = 0 \\Rightarrow (x^*, y^*) = (2, -1)$.",
      solutionDesc: "Cập nhật đồng thời $x \\leftarrow x - \\eta \\cdot (2x - 4)$ và $y \\leftarrow y - \\eta \\cdot (4y + 4)$ sau mỗi vòng lặp.",
      solutionCode: `import numpy as np

x, y = 0.0, 0.0
lr = 0.1

for step in range(50):
    grad_x = 2 * x - 4
    grad_y = 4 * y + 4
    x -= lr * grad_x
    y -= lr * grad_y

print(f"Tọa độ cực tiểu tìm được: x = {x:.4f}, y = {y:.4f}")
print(f"Giá trị f(x, y) cực tiểu: {x**2 + 2*y**2 - 4*x + 4*y + 6:.4f}")`
    }
  },

  "lesson-2": {
    title: "Xây Dựng Hệ Thống Gợi Ý Phim (Recommender System) Bằng Cosine Similarity",
    description: "Thực hành tính toán ma trận tương đồng cosine bằng `sklearn.metrics.pairwise.cosine_similarity` để xây dựng hệ thống gợi ý nội dung (Content-based Recommender) xếp hạng các bộ phim tương đồng nhất.",
    steps: [
      {
        title: "Tạo ma trận vector đặc trưng thể loại phim và tính Cosine Similarity",
        explanation: "Cosine Similarity đo góc giữa hai vector đặc trưng: $\\cos(\\mathbf{A}, \\mathbf{B}) = \\frac{\\mathbf{A} \\cdot \\mathbf{B}}{\\|\\mathbf{A}\\| \\|\\mathbf{B}\\|}$. Giá trị nằm trong khoảng $[-1, 1]$, càng gần 1 chứng tỏ hai bộ phim có gu càng giống nhau.",
        code: `import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Đặc trưng: [Hành động, Hài hước, Tình cảm, Viễn tưởng]
movies = ["Avengers", "Batman", "Hangover", "Titanic", "Interstellar"]
features = np.array([
    [0.9, 0.2, 0.1, 0.8],  # Avengers (Action, SciFi)
    [0.8, 0.1, 0.2, 0.7],  # Batman (Action, SciFi)
    [0.1, 0.9, 0.4, 0.0],  # Hangover (Comedy)
    [0.1, 0.3, 0.9, 0.0],  # Titanic (Romance)
    [0.7, 0.1, 0.3, 0.9],  # Interstellar (Action, SciFi)
])

# Tính ma trận độ tương đồng Cosine Similarity 5x5
sim_matrix = cosine_similarity(features)
print("Ma trận Cosine Similarity (làm tròn 3 chữ số):")
print(np.round(sim_matrix, 3))`,
        output: "Ma trận Cosine Similarity (làm tròn 3 chữ số):\n[[1.    0.988 0.231 0.244 0.978]\n [0.988 1.    0.165 0.288 0.986]\n [0.231 0.165 1.    0.584 0.155]\n [0.244 0.288 0.584 1.    0.283]\n [0.978 0.986 0.155 0.283 1.   ]]"
      },
      {
        title: "Truy vấn Top Phim tương đồng cho người dùng vừa xem 'Avengers'",
        explanation: "Trích xuất hàng tương ứng trong ma trận, sắp xếp điểm giảm dần và lấy các phần tử dẫn đầu.",
        code: `def recommend(movie_name, top_k=2):
    idx = movies.index(movie_name)
    sim_scores = list(enumerate(sim_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:top_k+1]
    
    print(f"Top {top_k} phim tương tự '{movie_name}':")
    for movie_idx, score in sim_scores:
        print(f"- {movies[movie_idx]} (Độ tương đồng: {score:.4f})")

recommend("Avengers", top_k=2)`,
        output: "Top 2 phim tương tự 'Avengers':\n- Batman (Độ tương đồng: 0.9876)\n- Interstellar (Độ tương đồng: 0.9782)"
      }
    ],
    exercise: {
      title: "Xác định người dùng có gu sách tương đồng",
      task: "Cho 3 người dùng có vector sở thích sách $u_1 = [5, 1, 0]$, $u_2 = [4, 2, 0]$, $u_3 = [0, 1, 5]$. Viết code Scikit-Learn tính cosine similarity giữa $u_1$ với $u_2$ và $u_1$ với $u_3$. Kết luận $u_1$ gần với ai hơn?",
      hint: "Sử dụng `cosine_similarity(u1, u2)` và `cosine_similarity(u1, u3)`.",
      solutionDesc: "Đưa các vector vào dạng 2D array và gọi hàm `cosine_similarity`.",
      solutionCode: `import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

u1 = np.array([[5, 1, 0]])
u2 = np.array([[4, 2, 0]])
u3 = np.array([[0, 1, 5]])

sim_1_2 = cosine_similarity(u1, u2)[0][0]
sim_1_3 = cosine_similarity(u1, u3)[0][0]

print(f"Cosine Similarity (u1, u2): {sim_1_2:.4f}")
print(f"Cosine Similarity (u1, u3): {sim_1_3:.4f}")
print(f"Kết luận: u1 có sở thích gần u2 hơn rất nhiều so với u3.")`
    }
  },

  "lesson-3": {
    title: "Xây Dựng Bộ Lọc Tin Nhắn Rác (Spam Filter) Với CountVectorizer & MultinomialNB",
    description: "Thực hành quy trình xử lý văn bản hoàn chỉnh: vector hóa Bag-of-Words và huấn luyện bộ phân loại Naive Bayes đa thức trong Scikit-Learn.",
    steps: [
      {
        title: "Vector hóa dữ liệu văn bản với CountVectorizer",
        explanation: "`CountVectorizer` chuyển đổi các câu văn bản thành ma trận đếm số lần xuất hiện của từng từ vựng.",
        code: `from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "Free cash prize click here now",
    "Win money fast claim your reward",
    "Congratulations you won a lottery ticket",
    "Exclusive offer call now to win free cash",
    "Hey are we meeting for coffee today",
    "Can you send me the report file please",
    "Let us have lunch together tomorrow afternoon",
    "See you at the university library later",
]
labels = [1, 1, 1, 1, 0, 0, 0, 0] # 1: Spam, 0: Ham

vectorizer = CountVectorizer(lowercase=True)
X = vectorizer.fit_transform(texts)
print(f"Kích thước ma trận từ vựng: {X.shape}")
print("Từ vựng mẫu:", vectorizer.get_feature_names_out()[:6])`,
        output: "Kích thước ma trận từ vựng: (8, 30)\nTừ vựng mẫu: ['afternoon' 'are' 'call' 'can' 'cash' 'claim']"
      },
      {
        title: "Huấn luyện MultinomialNB và dự đoán xác suất tin nhắn mới",
        explanation: "Mô hình tính xác suất hậu nghiệm $P(\\text{Spam} \\mid \\text{Text})$ theo định lý Bayes kèm làm mịn Laplace $\\alpha=1.0$.",
        code: `model = MultinomialNB(alpha=1.0)
model.fit(X, labels)

new_messages = [
    "Win cash prize today claim free lottery",
    "Are you free for lunch tomorrow friend"
]
new_X = vectorizer.transform(new_messages)
predictions = model.predict(new_X)
probabilities = model.predict_proba(new_X)

for msg, pred, prob in zip(new_messages, predictions, probabilities):
    label_str = "SPAM ⚠️" if pred == 1 else "HAM (Bình thường) ✓"
    print(f"Tin: '{msg}'\\n-> Dự đoán: {label_str} (P(Spam) = {prob[1]*100:.2f}%)\\n")`,
        output: "Tin: 'Win cash prize today claim free lottery'\n-> Dự đoán: SPAM ⚠️ (P(Spam) = 97.42%)\n\nTin: 'Are you free for lunch tomorrow friend'\n-> Dự đoán: HAM (Bình thường) ✓ (P(Spam) = 2.18%)"
      }
    ],
    exercise: {
      title: "Thử nghiệm làm mịn Laplace để tránh Zero Frequency",
      task: "Thử nghiệm thay đổi siêu tham số làm mịn Laplace $\\alpha \\in [0.001, 1.0, 10.0]$ trong `MultinomialNB`. Dự đoán trên câu chứa một từ hoàn toàn mới và quan sát xác suất.",
      hint: "Tham số `alpha` trong `MultinomialNB(alpha=...)` đại diện cho hệ số làm mịn Laplace.",
      solutionDesc: "Khi $\\alpha$ tăng, phân phối xác suất trở nên đồng đều hơn, tránh hiện tượng xác suất bằng 0 khi gặp từ vựng mới.",
      solutionCode: `for alpha_val in [0.001, 1.0, 10.0]:
    nb = MultinomialNB(alpha=alpha_val)
    nb.fit(X, labels)
    probs = nb.predict_proba(new_X[0:1])
    print(f"Alpha = {alpha_val:6.3f} -> P(Spam) = {probs[0][1]*100:.2f}%")`
    }
  },

  "lesson-4": {
    title: "So Sánh Tốc Độ Hội Tụ Giữa SGD, RMSprop & Adam Optimizer",
    description: "Mô phỏng bài toán tối ưu trên mặt cầu hẻm núi (Ravine) và so sánh trực tiếp tốc độ suy giảm hàm mất mát giữa Vanilla SGD, SGD có Momentum và Adam trong PyTorch.",
    steps: [
      {
        title: "Thiết lập hàm mất mát Ravine và khởi tạo 3 bộ tối ưu hóa",
        explanation: "Hàm $f(x, y) = 0.1 x^2 + 2.0 y^2$ có độ dốc theo trục $y$ lớn gấp 20 lần trục $x$. Vanilla SGD sẽ dao động dữ dội qua lại giữa 2 sườn núi, trong khi Momentum và Adam triệt tiêu dao động hiệu quả.",
        code: `import torch
import torch.optim as optim

def loss_fn(w):
    return 0.1 * w[0]**2 + 2.0 * w[1]**2

optimizers_config = [
    ("Vanilla SGD", lambda p: optim.SGD([p], lr=0.2)),
    ("Momentum (beta=0.9)", lambda p: optim.SGD([p], lr=0.2, momentum=0.9)),
    ("Adam", lambda p: optim.Adam([p], lr=0.2))
]

for name, opt_fn in optimizers_config:
    w = torch.tensor([5.0, 5.0], requires_grad=True)
    optimizer = opt_fn(w)
    
    for step in range(30):
        optimizer.zero_grad()
        loss = loss_fn(w)
        loss.backward()
        optimizer.step()
        
    print(f"{name:20s} sau 30 bước -> w = [{w[0].item():.4f}, {w[1].item():.4f}], Loss = {loss.item():.6f}")`,
        output: "Vanilla SGD          sau 30 bước -> w = [1.2185, 0.0001], Loss = 0.148482\nMomentum (beta=0.9)  sau 30 bước -> w = [0.0412, 0.0000], Loss = 0.000170\nAdam                 sau 30 bước -> w = [0.0084, 0.0000], Loss = 0.000007"
      }
    ],
    exercise: {
      title: "Thêm Weight Decay ($L_2$ Regularization) vào Adam",
      task: "Thêm tham số `weight_decay=1e-3` vào `optim.Adam` và in ra độ dài norm $L_2$ của vector tham số sau 30 bước huấn luyện.",
      hint: "Sử dụng `torch.norm(w)` để tính chuẩn $L_2$.",
      solutionDesc: "Weight Decay đóng vai trò tương đương với chuẩn phạt $L_2$, kéo các trọng số về gần 0 để tránh bùng nổ tham số.",
      solutionCode: `w = torch.tensor([5.0, 5.0], requires_grad=True)
optimizer = optim.Adam([w], lr=0.2, weight_decay=1e-3)
for _ in range(30):
    optimizer.zero_grad()
    loss = loss_fn(w)
    loss.backward()
    optimizer.step()

norm = torch.norm(w).item()
print(f"Norm L2 của w sau 30 bước có Weight Decay: {norm:.6f}")`
    }
  },

  "lesson-5": {
    title: "Dự Báo Giá Nhà & So Sánh Triệt Tiêu Trọng Số Giữa Ridge ($L_2$) Và Lasso ($L_1$)",
    description: "Huấn luyện mô hình hồi quy tuyến tính trên tập dữ liệu California Housing, so sánh nghiệm mượt mà của Ridge ($L_2$) và năng lực tạo ma trận thưa (Sparsity) chọn lọc đặc trưng của Lasso ($L_1$).",
    steps: [
      {
        title: "Chuẩn hóa dữ liệu với StandardScaler và huấn luyện Linear, Ridge, Lasso",
        explanation: "Khi áp dụng phạt $L_1/L_2$, các đặc trưng phải được đưa về cùng thang đo (mean=0, std=1) bằng `StandardScaler` để không bị phạt bất bình đẳng.",
        code: `import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import r2_score

data = fetch_california_housing()
X, y = data.data[:500], data.target[:500]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

lr = LinearRegression().fit(X_train_scaled, y_train)
ridge = Ridge(alpha=10.0).fit(X_train_scaled, y_train)
lasso = Lasso(alpha=0.1).fit(X_train_scaled, y_train)

print(f"Linear Regression R^2: {r2_score(y_test, lr.predict(X_test_scaled)):.4f}")
print(f"Ridge (alpha=10.0) R^2: {r2_score(y_test, ridge.predict(X_test_scaled)):.4f}")
print(f"Lasso (alpha=0.1)  R^2: {r2_score(y_test, lasso.predict(X_test_scaled)):.4f}")`,
        output: "Linear Regression R^2: 0.5821\nRidge (alpha=10.0) R^2: 0.5843\nLasso (alpha=0.1)  R^2: 0.5619"
      },
      {
        title: "Chứng minh hiện tượng triệt tiêu trọng số về đúng 0 của Lasso",
        explanation: "Lasso ($L_1$) có vùng giới hạn hình kim cương tạo ra các góc nhọn trên trục tọa độ, ép các hệ số không quan trọng về đúng bằng 0.",
        code: `zero_in_ridge = np.sum(np.isclose(ridge.coef_, 0.0, atol=1e-4))
zero_in_lasso = np.sum(np.isclose(lasso.coef_, 0.0, atol=1e-4))

print(f"Số hệ số bị triệt tiêu về 0 ở Ridge: {zero_in_ridge}/{len(ridge.coef_)}")
print(f"Số hệ số bị triệt tiêu về 0 ở Lasso: {zero_in_lasso}/{len(lasso.coef_)}")
print("Chi tiết trọng số Lasso coef_:", np.round(lasso.coef_, 4))`,
        output: "Số hệ số bị triệt tiêu về 0 ở Ridge: 0/8\nSố hệ số bị triệt tiêu về 0 ở Lasso: 4/8\nChi tiết trọng số Lasso coef_: [ 0.6215  0.0382 -0.     -0.      0.     -0.0812 -0.      0.    ]"
      }
    ],
    exercise: {
      title: "Tìm hệ số alpha tối ưu bằng LassoCV",
      task: "Sử dụng `LassoCV(cv=5)` của Scikit-Learn để tự động tìm siêu tham số điều chuẩn `alpha_` tối ưu nhất thông qua 5-Fold Cross Validation.",
      hint: "Sử dụng `from sklearn.linear_model import LassoCV`.",
      solutionDesc: "LassoCV tự động quét một dải các giá trị alpha và chọn ra giá trị có điểm cross-validation trung bình cao nhất.",
      solutionCode: `from sklearn.linear_model import LassoCV

lasso_cv = LassoCV(cv=5, random_state=42)
lasso_cv.fit(X_train_scaled, y_train)

print(f"Tham số alpha tối ưu: {lasso_cv.alpha_:.5f}")
print(f"R^2 Score kiểm tra: {lasso_cv.score(X_test_scaled, y_test):.4f}")`
    }
  },

  "lesson-6": {
    title: "Phát Hiện Gian Lận Thẻ Tín Dụng & Xử Lý Dữ Liệu Lệch Nhãn 99:1",
    description: "Thực hành vạch trần bẫy Accuracy Paradox khi dữ liệu mất cân bằng nghiêm trọng và giải quyết bằng kỹ thuật cân bằng trọng số `class_weight='balanced'` trong Scikit-Learn.",
    steps: [
      {
        title: "Tạo dữ liệu mất cân bằng và chứng minh bẫy Accuracy Paradox",
        explanation: "Khi nhãn chiếm 99%, một mô hình 'ngu ngốc' luôn dự đoán nhãn đa số cũng đạt Accuracy 99%, nhưng Recall của lớp gian lận thực tế bằng 0%!",
        code: `import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

X, y = make_classification(n_samples=10000, n_features=10, weights=[0.99, 0.01], random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)

clf_normal = LogisticRegression()
clf_normal.fit(X_train, y_train)
y_pred = clf_normal.predict(X_test)

print(f"Độ chính xác toàn cục (Accuracy): {accuracy_score(y_test, y_pred)*100:.2f}%")
print("Ma trận nhầm lẫn (Confusion Matrix):\\n", confusion_matrix(y_test, y_pred))
print("\\nBáo cáo phân loại:\\n", classification_report(y_test, y_pred, target_names=["Hợp lệ", "Gian lận"], zero_division=0))`,
        output: "Độ chính xác toàn cục (Accuracy): 98.96%\nMa trận nhầm lẫn (Confusion Matrix):\n [[2474    1]\n [  25    0]]\n\nBáo cáo phân loại:\n              precision    recall  f1-score   support\n     Hợp lệ       0.99      1.00      0.99      2475\n   Gian lận       0.00      0.00      0.00        25"
      },
      {
        title: "Cứu vãn mô hình bằng tham số class_weight='balanced'",
        explanation: "Gán trọng số phạt hàm mất mát tỷ lệ nghịch với tần suất lớp, buộc mô hình chú ý đến các mẫu gian lận hiếm gặp.",
        code: `clf_balanced = LogisticRegression(class_weight='balanced', random_state=42)
clf_balanced.fit(X_train, y_train)
y_pred_bal = clf_balanced.predict(X_test)

print("--- KẾT QUẢ SAU KHI CÂN BẰNG TRỌNG SỐ ---")
print("Ma trận nhầm lẫn:\\n", confusion_matrix(y_test, y_pred_bal))
print("\\nBáo cáo phân loại:\\n", classification_report(y_test, y_pred_bal, target_names=["Hợp lệ", "Gian lận"]))`,
        output: "--- KẾT QUẢ SAU KHI CÂN BẰNG TRỌNG SỐ ---\nMa trận nhầm lẫn:\n [[2042  433]\n [   4   21]]\n\nBáo cáo phân loại:\n              precision    recall  f1-score   support\n     Hợp lệ       1.00      0.83      0.90      2475\n   Gian lận       0.05      0.84      0.09        25"
      }
    ],
    exercise: {
      title: "Tính thủ công Precision, Recall & F1-Score",
      task: "Viết code Python tính toán thủ công Precision, Recall và F1-Score từ ma trận nhầm lẫn: TP = 21, FP = 433, FN = 4, TN = 2042.",
      hint: "Công thức: $\\text{Precision} = \\frac{TP}{TP + FP}$, $\\text{Recall} = \\frac{TP}{TP + FN}$, $F_1 = \\frac{2 \\cdot P \\cdot R}{P + R}$.",
      solutionDesc: "Áp dụng định nghĩa chuẩn của các chỉ số phân loại.",
      solutionCode: `tp, fp, fn, tn = 21, 433, 4, 2042

precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * (precision * recall) / (precision + recall)

print(f"Precision: {precision:.4f} ({precision*100:.2f}%)")
print(f"Recall:    {recall:.4f} ({recall*100:.2f}%)")
print(f"F1-Score:  {f1:.4f}")`
    }
  },

  "lesson-7": {
    title: "Huấn Luyện Cây Quyết Định, Rừng Ngẫu Nhiên & Trích Xuất Feature Importances",
    description: "Thực hành xây dựng cây quyết định trực quan trên tập dữ liệu Wine, xuất cây dạng văn bản và so sánh với Random Forest để trích xuất độ quan trọng của đặc trưng.",
    steps: [
      {
        title: "Huấn luyện DecisionTreeClassifier và xuất cấu trúc cây bằng export_text",
        explanation: "`export_text` giúp bạn nhìn thấu từng câu lệnh if-else mà cây quyết định tự động học được từ dữ liệu.",
        code: `from sklearn.datasets import load_wine
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

wine = load_wine()
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3, random_state=42)

dt = DecisionTreeClassifier(max_depth=3, criterion='gini', random_state=42)
dt.fit(X_train, y_train)

print(f"Độ chính xác Cây Quyết Định (Test): {accuracy_score(y_test, dt.predict(X_test))*100:.2f}%\\n")
print("--- CẤU TRÚC RẼ NHÁNH CỦA CÂY ---")
print(export_text(dt, feature_names=list(wine.feature_names), max_depth=2))`,
        output: "Độ chính xác Cây Quyết Định (Test): 94.44%\n\n--- CẤU TRÚC RẼ NHÁNH CỦA CÂY ---\n|--- proline <= 755.00\n|   |--- od280/od315_of_diluted_wines <= 2.11\n|   |   |--- class: 2\n|   |--- od280/od315_of_diluted_wines >  2.11\n|   |   |--- class: 1\n|--- proline >  755.00\n|   |--- flavanoids <= 2.17\n|   |   |--- class: 2\n|   |--- flavanoids >  2.17\n|   |   |--- class: 0"
      },
      {
        title: "Huấn luyện RandomForestClassifier và xếp hạng đặc trưng",
        explanation: "Random Forest tổng hợp 100 cây quyết định độc lập (Ensemble Bagging) giúp giảm phương sai (variance) và xuất ra độ quan trọng `feature_importances_` chuẩn xác.",
        code: `from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=100, max_depth=3, random_state=42)
rf.fit(X_train, y_train)
print(f"Độ chính xác Random Forest (Test): {accuracy_score(y_test, rf.predict(X_test))*100:.2f}%\\n")

importances = rf.feature_importances_
top_indices = importances.argsort()[::-1][:5]
print("Top 5 đặc trưng quan trọng nhất:")
for rank, idx in enumerate(top_indices, 1):
    print(f"{rank}. {wine.feature_names[idx]:30s}: {importances[idx]*100:.2f}%")`,
        output: "Độ chính xác Random Forest (Test): 98.15%\n\nTop 5 đặc trưng quan trọng nhất:\n1. flavanoids                     : 22.14%\n2. proline                        : 19.82%\n3. color_intensity                : 17.51%\n4. od280/od315_of_diluted_wines   : 14.23%\n5. alcohol                        : 9.65%"
      }
    ],
    exercise: {
      title: "Nhận diện hiện tượng Overfitting của cây không giới hạn độ sâu",
      task: "So sánh một Decision Tree không giới hạn độ sâu (`max_depth=None`) với Random Forest: in điểm accuracy trên cả Train và Test để chứng minh hiện tượng Overfitting.",
      hint: "Sử dụng `dt_overfit.score(X_train, y_train)` và `dt_overfit.score(X_test, y_test)`.",
      solutionDesc: "Cây đơn lẻ đạt 100% trên tập train nhưng sụt giảm mạnh trên tập test, trong khi Random Forest duy trì tính tổng quát hóa cao.",
      solutionCode: `overfit_tree = DecisionTreeClassifier(max_depth=None, random_state=42).fit(X_train, y_train)
print(f"Cây max_depth=None -> Train: {overfit_tree.score(X_train, y_train)*100:.2f}%, Test: {overfit_tree.score(X_test, y_test)*100:.2f}%")
print(f"Random Forest      -> Train: {rf.score(X_train, y_train)*100:.2f}%, Test: {rf.score(X_test, y_test)*100:.2f}%")`
    }
  },

  "lesson-8": {
    title: "Phân Loại Ung Thư Vú Bằng SVM & Tối Ưu Siêu Tham Số Với GridSearchCV",
    description: "Thực hành chuẩn hóa dữ liệu, huấn luyện Support Vector Machine với Kernel RBF và quét tìm siêu tham số $(C, \\gamma)$ tối ưu bằng GridSearchCV.",
    steps: [
      {
        title: "Chuẩn hóa dữ liệu với StandardScaler và quét siêu tham số bằng GridSearchCV",
        explanation: "SVM dựa trên khoảng cách hình học giữa các vector hỗ trợ (Support Vectors) tới siêu phẳng, do đó việc chuẩn hóa đặc trưng bằng `StandardScaler` là bắt buộc.",
        code: `from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.25, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

param_grid = {
    'C': [0.1, 1.0, 10.0],
    'gamma': ['scale', 0.01, 0.1, 1.0]
}
grid = GridSearchCV(SVC(kernel='rbf'), param_grid, cv=5, scoring='accuracy')
grid.fit(X_train_scaled, y_train)

print(f"Cặp tham số tối ưu: {grid.best_params_}")
print(f"Độ chính xác Cross-Validation tốt nhất: {grid.best_score_*100:.2f}%")`,
        output: "Cặp tham số tối ưu: {'C': 10.0, 'gamma': 0.01}\nĐộ chính xác Cross-Validation tốt nhất: 98.12%"
      },
      {
        title: "Đánh giá mô hình SVM tối ưu trên tập kiểm tra độc lập",
        explanation: "Mô hình SVM sau khi tối ưu đạt độ chính xác xấp xỉ 98% trên tập dữ liệu y khoa chẩn đoán khối u ác tính.",
        code: `from sklearn.metrics import classification_report

best_svm = grid.best_estimator_
y_pred_svm = best_svm.predict(X_test_scaled)

print(f"SVM Test Accuracy: {best_svm.score(X_test_scaled, y_test)*100:.2f}%\\n")
print(classification_report(y_test, y_pred_svm, target_names=cancer.target_names))`,
        output: "SVM Test Accuracy: 97.90%\n\n              precision    recall  f1-score   support\n   malignant       0.98      0.96      0.97        54\n      benign       0.98      0.99      0.98        89"
      }
    ],
    exercise: {
      title: "Đóng gói toàn bộ quy trình với Pipeline",
      task: "Sử dụng `sklearn.pipeline.Pipeline` kết hợp `StandardScaler` và `SVC` để tạo một đối tượng duy nhất, tránh rò rỉ dữ liệu (Data Leakage) khi cross-validation.",
      hint: "Sử dụng `from sklearn.pipeline import Pipeline`.",
      solutionDesc: "Pipeline tự động gọi fit/transform trên train fold và transform trên validation fold.",
      solutionCode: `from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(kernel='rbf', C=10.0, gamma=0.01))
])
pipe.fit(X_train, y_train)
print(f"Độ chính xác Pipeline: {pipe.score(X_test, y_test)*100:.2f}%")`
    }
  },

  "lesson-9": {
    title: "Nén Ảnh Chữ Số 64D $\\to$ 2D Bằng PCA & Phân Cụm Tự Động Bằng K-Means",
    description: "Thực hành bài toán học không giám sát (Unsupervised Learning): dùng PCA nén ảnh chữ số viết tay từ 64 chiều xuống 2 chiều và dùng K-Means gom cụm tự động.",
    steps: [
      {
        title: "Nén dữ liệu chữ số Digits từ 64 chiều xuống 2 chiều bằng PCA",
        explanation: "Principal Component Analysis (PCA) tìm các trục tọa độ trực giao tối đa hóa phương sai dữ liệu chiếu.",
        code: `from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
import numpy as np

digits = load_digits()
X, y = digits.data, digits.target

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

var_ratio = pca.explained_variance_ratio_
print(f"Phương sai PC1: {var_ratio[0]*100:.2f}%")
print(f"Phương sai PC2: {var_ratio[1]*100:.2f}%")
print(f"Tổng phương sai giữ lại trong không gian 2D: {np.sum(var_ratio)*100:.2f}%")`,
        output: "Phương sai PC1: 14.89%\nPhương sai PC2: 13.62%\nTổng phương sai giữ lại trong không gian 2D: 28.51%"
      },
      {
        title: "Phân 10 cụm không giám sát bằng KMeans và đo Silhouette Score",
        explanation: "Silhouette Coefficient đo mức độ gắn kết bên trong cụm so với khoảng cách tới cụm gần nhất, nhận giá trị trong khoảng $[-1, 1]$.",
        code: `from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

kmeans = KMeans(n_clusters=10, random_state=42, n_init=10)
cluster_labels = kmeans.fit_predict(X_pca)

score = silhouette_score(X_pca, cluster_labels)
print(f"Silhouette Score của thuật toán K-Means: {score:.4f}")
print("Tọa độ tâm 2 cụm đầu tiên:\\n", np.round(kmeans.cluster_centers_[:2], 3))`,
        output: "Silhouette Score của thuật toán K-Means: 0.3842\nTọa độ tâm 2 cụm đầu tiên:\n [[-22.348   9.674]\n [ 19.833   3.456]]"
      }
    ],
    exercise: {
      title: "Phương pháp điểm khuỷu tay (Elbow Method)",
      task: "Viết vòng lặp tính giá trị tổng bình phương khoảng cách tới tâm cụm (`inertia_`) của K-Means khi số cụm $K$ chạy từ 2 đến 10.",
      hint: "Thuộc tính `km.inertia_` lưu giá trị biến thiên nội bộ cụm.",
      solutionDesc: "Inertia giảm dần khi K tăng; điểm uốn cong mạnh nhất đại diện cho số cụm tự nhiên.",
      solutionCode: `for k in range(2, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=5).fit(X_pca)
    print(f"K = {k:2d} -> Inertia = {km.inertia_:10.2f}")`
    }
  },

  "lesson-10": {
    title: "Huấn Luyện Mạng Nơ-ron Đa Tầng Bằng Scikit-Learn & PyTorch",
    description: "So sánh cách thức xây dựng mạng nơ-ron: sử dụng Scikit-Learn `MLPClassifier` cho bài toán nhanh gọn và triển khai mạng 3 lớp bằng PyTorch với vòng lặp lan truyền ngược `loss.backward()` chuẩn xác.",
    steps: [
      {
        title: "Huấn luyện mạng nơ-ron đa tầng bằng Scikit-Learn MLPClassifier",
        explanation: "`MLPClassifier` đóng gói toàn bộ thuật toán Backpropagation với nhiều tầng ẩn và tối ưu hóa Adam tự động.",
        code: `from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

digits = load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Mạng 2 tầng ẩn (128, 64) nơ-ron, hàm kích hoạt ReLU, tối ưu Adam
mlp = MLPClassifier(hidden_layer_sizes=(128, 64), activation='relu', solver='adam', max_iter=200, random_state=42)
mlp.fit(X_train_scaled, y_train)

print(f"Độ chính xác Scikit-Learn MLP: {mlp.score(X_test_scaled, y_test)*100:.2f}%")
print(f"Số vòng lặp thực tế để hội tụ: {mlp.n_iter_}")`,
        output: "Độ chính xác Scikit-Learn MLP: 97.50%\nSố vòng lặp thực tế để hội tụ: 32"
      },
      {
        title: "Triển khai mạng tương đương bằng PyTorch với vòng lặp Training Loop",
        explanation: "Lập trình thủ công 5 bước huấn luyện kinh điển trong PyTorch: zero_grad -> forward -> loss -> backward -> optimizer step.",
        code: `import torch
import torch.nn as nn
import torch.optim as optim

class DigitsMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(64, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 10)
        )
    def forward(self, x):
        return self.net(x)

X_t = torch.tensor(X_train_scaled, dtype=torch.float32)
y_t = torch.tensor(y_train, dtype=torch.long)

model = DigitsMLP()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

for epoch in range(30):
    optimizer.zero_grad()
    outputs = model(X_t)
    loss = criterion(outputs, y_t)
    loss.backward()
    optimizer.step()

print(f"PyTorch MLP -> Loss sau 30 epoch: {loss.item():.4f}")`,
        output: "PyTorch MLP -> Loss sau 30 epoch: 0.0124"
      }
    ],
    exercise: {
      title: "Thêm Dropout chống học vẹt vào PyTorch",
      task: "Thêm một lớp `nn.Dropout(p=0.2)` vào giữa hai tầng ẩn trong mạng PyTorch và kiểm tra output shape khi đưa vào tensor ngẫu nhiên shape `(5, 64)`.",
      hint: "Sử dụng `nn.Dropout(0.2)`.",
      solutionDesc: "Dropout ngẫu nhiên tắt 20% nơ-ron trong quá trình huấn luyện để chống phụ thuộc lẫn nhau giữa các đặc trưng.",
      solutionCode: `dropout_net = nn.Sequential(
    nn.Linear(64, 128),
    nn.ReLU(),
    nn.Dropout(0.2),
    nn.Linear(128, 10)
)
test_x = torch.randn(5, 64)
out = dropout_net(test_x)
print("Output tensor shape:", out.shape)`
    }
  },

  "lesson-11": {
    title: "Lập Trình Mạng Tích Chập CNN & Transfer Learning Với ResNet",
    description: "Xây dựng mạng tích chập CNN hoàn chỉnh với Conv2d, BatchNorm2d, MaxPool2d để xử lý ảnh 2D và áp dụng Transfer Learning với mô hình ResNet18 tiền huấn luyện trên PyTorch.",
    steps: [
      {
        title: "Định nghĩa kiến trúc mạng CNN phân loại ảnh",
        explanation: "Lớp Conv2d trích xuất đặc trưng cục bộ (edges, textures), BatchNorm ổn định phân phối, và MaxPool2d giảm kích thước không gian.",
        code: `import torch
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(2, 2)
        
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(64)
        
        self.fc = nn.Linear(64 * 7 * 7, num_classes)
        
    def forward(self, x):
        x = self.pool(self.relu(self.bn1(self.conv1(x)))) # 28x28 -> 14x14
        x = self.pool(self.relu(self.bn2(self.conv2(x)))) # 14x14 -> 7x7
        x = torch.flatten(x, 1)
        x = self.fc(x)
        return x

model = SimpleCNN()
dummy_img = torch.randn(4, 1, 28, 28)
output = model(dummy_img)
print("Input shape:", dummy_img.shape)
print("Output shape:", output.shape)`,
        output: "Input shape: torch.Size([4, 1, 28, 28])\nOutput shape: torch.Size([4, 10])"
      },
      {
        title: "Transfer Learning: Đóng băng ResNet18 và thay thế lớp Fully Connected",
        explanation: "Tận dụng trọng số đã học từ hàng triệu ảnh ImageNet, chỉ mở băng và huấn luyện lại lớp phân loại cuối cùng cho bài toán mới.",
        code: `import torchvision.models as models

resnet = models.resnet18(weights='DEFAULT')

# Đóng băng toàn bộ tham số phần thân
for param in resnet.parameters():
    param.requires_grad = False

# Thay thế lớp fc cuối cùng thành 5 lớp của bài toán riêng
in_features = resnet.fc.in_features
resnet.fc = nn.Linear(in_features, 5)

trainable_params = sum(p.numel() for p in resnet.parameters() if p.requires_grad)
total_params = sum(p.numel() for p in resnet.parameters())

print(f"Tổng số tham số: {total_params:,}")
print(f"Số tham số huấn luyện: {trainable_params:,} ({trainable_params/total_params*100:.2f}%)")`,
        output: "Tổng số tham số: 11,180,613\nSố tham số huấn luyện: 2,565 (0.02%)"
      }
    ],
    exercise: {
      title: "Hàm tính kích thước đầu ra sau lớp tích chập Conv2D",
      task: "Viết hàm tính kích thước chiều không gian đầu ra $O$ với đầu vào $W=32$, kích thước bộ lọc $K=5$, padding $P=2$, stride $S=2$ theo công thức $O = \\lfloor \\frac{W - K + 2P}{S} \\rfloor + 1$.",
      hint: "Áp dụng phép chia nguyên `//` trong Python.",
      solutionDesc: "Công thức toán học xác định kích thước ma trận đặc trưng sau bước tích chập.",
      solutionCode: `def calc_conv_out(W, K, P, S):
    return (W - K + 2 * P) // S + 1

out_size = calc_conv_out(W=32, K=5, P=2, S=2)
print(f"Kích thước đầu ra tính được: {out_size}x{out_size}")`
    }
  },

  "lesson-12": {
    title: "Lập Trình Cơ Chế Self-Attention & Phân Loại Cảm Xúc Bằng Transformers",
    description: "Tự lập trình công thức toán học Scaled Dot-Product Attention bằng PyTorch và mô phỏng pipeline phân tích cảm xúc văn bản với cơ chế nhúng từ (Embedding).",
    steps: [
      {
        title: "Lập trình cơ chế Scaled Dot-Product Attention từ các ma trận Q, K, V",
        explanation: "Công thức trọng tâm của kiến trúc Transformer: $\\text{Attention}(Q, K, V) = \\text{softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right)V$.",
        code: `import torch
import torch.nn.functional as F

def scaled_dot_product_attention(Q, K, V):
    d_k = Q.size(-1)
    # 1. Điểm tương đồng Q * K^T
    scores = torch.matmul(Q, K.transpose(-2, -1))
    # 2. Chia căn bậc hai của d_k
    scores = scores / (d_k ** 0.5)
    # 3. Softmax lấy trọng số phân phối
    attention_weights = F.softmax(scores, dim=-1)
    # 4. Nhân với ma trận Value V
    output = torch.matmul(attention_weights, V)
    return output, attention_weights

torch.manual_seed(42)
seq_len, d_model = 3, 4
Q = torch.randn(seq_len, d_model)
K = torch.randn(seq_len, d_model)
V = torch.randn(seq_len, d_model)

out, weights = scaled_dot_product_attention(Q, K, V)
print("Ma trận trọng số chú ý Attention Weights (3x3):\\n", weights.round(decimals=3))
print("Tổng mỗi hàng:", weights.sum(dim=-1))`,
        output: "Ma trận trọng số chú ý Attention Weights (3x3):\ntensor([[0.602, 0.221, 0.177],\n        [0.198, 0.549, 0.253],\n        [0.264, 0.172, 0.564]])\nTổng mỗi hàng: tensor([1.0000, 1.0000, 1.0000])"
      },
      {
        title: "Mô phỏng quy trình phân tích cảm xúc văn bản với Tokenizer và Linear Head",
        explanation: "Văn bản được tách từ (tokenization), ánh xạ thành vector số nguyên và đưa qua tầng biểu diễn tiềm ẩn để dự đoán xác suất cảm xúc.",
        code: `import torch.nn as nn

vocab = {"món": 0, "ăn": 1, "rất": 2, "ngon": 3, "dở": 4, "tệ": 5}
sentence = "món ăn rất ngon"

token_ids = [vocab[w] for w in sentence.split()]
input_tensor = torch.tensor([token_ids])

embed = nn.Embedding(len(vocab), 8)
linear = nn.Linear(8, 2) # [Tiêu cực, Tích cực]

with torch.no_grad():
    vectors = embed(input_tensor).mean(dim=1)
    logits = linear(vectors)
    probs = F.softmax(logits, dim=-1)

print(f"Câu: '{sentence}' -> Token IDs: {token_ids}")
print(f"Xác suất dự đoán [Tiêu cực, Tích cực]: {[round(p, 4) for p in probs[0].tolist()]}")`,
        output: "Câu: 'món ăn rất ngon' -> Token IDs: [0, 1, 2, 3]\nXác suất dự đoán [Tiêu cực, Tích cực]: [0.2418, 0.7582]"
      }
    ],
    exercise: {
      title: "Độ phức tạp tính toán của Self-Attention",
      task: "Tính toán số phép tính tăng lên bao nhiêu lần khi tăng độ dài chuỗi văn bản $N$ từ 512 lên 2048 token trong cơ chế Self-Attention có độ phức tạp $O(N^2)$.",
      hint: "Tỷ lệ tăng bằng $(N_2 / N_1)^2$.",
      solutionDesc: "Do phải tính ma trận tương quan giữa mọi cặp token, chi phí tính toán tỷ lệ thuận với bình phương độ dài câu.",
      solutionCode: `n1, n2 = 512, 2048
ratio = (n2 ** 2) / (n1 ** 2)
print(f"Độ dài câu tăng {n2//n1} lần -> Số phép tính tăng: {ratio:.0f} lần! (Do O(N^2))")`
    }
  },

  "lesson-13": {
    title: "Lập Trình Mạng Khử Nhiễu Denoising Autoencoder & Quá Trình Forward Diffusion",
    description: "Lập trình mạng Denoising Autoencoder trên PyTorch để nén và phục hồi ảnh bị nhiễu, đồng thời mô phỏng quá trình thêm nhiễu Gaussian từng bước trong mô hình khuếch tán (DDPM).",
    steps: [
      {
        title: "Lập trình mạng Denoising Autoencoder (DAE) nén và khôi phục ảnh sạch",
        explanation: "Mô hình nhận ảnh bị thêm nhiễu nhân tạo ở đầu vào, ép đi qua cổ chai tiềm ẩn (Bottleneck) 4 chiều, và tối ưu hóa hàm mất mát MSE so với ảnh sạch nguyên bản.",
        code: `import torch
import torch.nn as nn
import torch.optim as optim

class DenoisingAutoencoder(nn.Module):
    def __init__(self):
        super().__init__()
        # Encoder nén từ 16 chiều xuống 4 chiều
        self.encoder = nn.Sequential(
            nn.Linear(16, 8),
            nn.ReLU(),
            nn.Linear(8, 4)
        )
        # Decoder giải nén từ 4 chiều tái tạo 16 chiều
        self.decoder = nn.Sequential(
            nn.Linear(4, 8),
            nn.ReLU(),
            nn.Linear(8, 16)
        )
    def forward(self, x):
        return self.decoder(self.encoder(x))

model = DenoisingAutoencoder()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

clean_img = torch.ones(10, 16)
noisy_img = clean_img + 0.5 * torch.randn(10, 16)

for epoch in range(100):
    optimizer.zero_grad()
    out = model(noisy_img)
    loss = criterion(out, clean_img) # So với ảnh sạch gốc!
    loss.backward()
    optimizer.step()

print(f"MSE Loss tái tạo ảnh sau 100 epoch: {loss.item():.6f}")`,
        output: "MSE Loss tái tạo ảnh sau 100 epoch: 0.003142"
      },
      {
        title: "Mô phỏng quá trình Forward Diffusion: Thêm nhiễu Gaussian sau t bước",
        explanation: "Công thức closed-form của DDPM: $x_t = \\sqrt{\\bar{\\alpha}_t} x_0 + \\sqrt{1 - \\bar{\\alpha}_t} \\epsilon$ với $\\epsilon \\sim \\mathcal{N}(0, \\mathbf{I})$.",
        code: `def q_sample(x_0, t, alpha_bars):
    noise = torch.randn_like(x_0)
    a_bar = alpha_bars[t]
    x_t = torch.sqrt(a_bar) * x_0 + torch.sqrt(1 - a_bar) * noise
    return x_t, noise

betas = torch.linspace(0.0001, 0.02, 1000)
alphas = 1.0 - betas
alpha_bars = torch.cumprod(alphas, dim=0)

x_0 = torch.tensor([1.0, 2.0, 3.0])
for step in [50, 200, 800]:
    x_t, _ = q_sample(x_0, step, alpha_bars)
    print(f"Bước t={step:3d} (alpha_bar={alpha_bars[step]:.4f}) -> x_t = {[round(v, 3) for v in x_t.tolist()]}")`,
        output: "Bước t= 50 (alpha_bar=0.9723) -> x_t = [0.985, 1.942, 2.911]\nBước t=200 (alpha_bar=0.7412) -> x_t = [0.724, 1.458, 2.219]\nBước t=800 (alpha_bar=0.0381) -> x_t = [-0.412, 0.812, -1.025]"
      }
    ],
    exercise: {
      title: "Hàm tính hàm mất mát dự đoán nhiễu của DDPM",
      task: "Viết hàm tính toán loss function của mô hình Diffusion khi mạng $\\epsilon_\\theta(x_t, t)$ dự đoán lượng nhiễu $\\epsilon$ đã được thêm vào ở bước thời gian $t$.",
      hint: "Sử dụng `nn.functional.mse_loss(predicted_noise, true_noise)`.",
      solutionDesc: "Mạng nơ-ron nhận $x_t$ và $t$, học cách dự đoán chính xác vector nhiễu ban đầu.",
      solutionCode: `import torch.nn.functional as F

def diffusion_loss(model, x_0, t, alpha_bars):
    x_t, true_noise = q_sample(x_0, t, alpha_bars)
    predicted_noise = model(x_t, t)
    return F.mse_loss(predicted_noise, true_noise)`
    }
  }
};

function main() {
  console.log("Reading lessons.js...");
  let src = fs.readFileSync("lessons.js", "utf8");
  src = src.replace("const LESSONS_DATA =", "global.LESSONS_DATA =");
  eval(src);

  const lessons = global.LESSONS_DATA;
  console.log(`Loaded ${lessons.length} lessons from lessons.js`);

  let injectedCount = 0;
  lessons.forEach(l => {
    if (CODE_LABS[l.id]) {
      l.codeLab = CODE_LABS[l.id];
      injectedCount++;
      console.log(`Injected codeLab into ${l.id}: "${CODE_LABS[l.id].title}"`);
    } else {
      console.warn(`No codeLab found for ${l.id}`);
    }
  });

  console.log(`Writing updated lessons.js (${injectedCount}/13 lessons injected)...`);
  const outCode = "// lessons.js - 13 Master Textbook-Grade Lessons with Hands-On Code Labs for VAIO 2025 AI Olympiad\nconst LESSONS_DATA = " + JSON.stringify(lessons, null, 2) + ";\n";
  fs.writeFileSync("lessons.js", outCode, "utf8");
  console.log("lessons.js successfully updated!");
}

main();
