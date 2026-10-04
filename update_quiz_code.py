# -*- coding: utf-8 -*-
"""
update_quiz_code.py - Formats code questions in quiz.js with syntax-highlighted markdown code blocks.
"""

import json
import re

def main():
    with open('quiz.js', 'r', encoding='utf-8') as f:
        text = f.read()

    m = re.search(r'const QUIZ_DATA\s*=\s*(\[[\s\S]*?\]);', text)
    if not m:
        print('Failed to find QUIZ_DATA')
        return

    data = json.loads(m.group(1))

    for q in data:
        qid = q['id']
        if qid == 6:
            q['question'] = """Câu 6. Giả sử bạn đang xây dựng một mô hình phân loại cảm xúc văn bản (positive/negative) bằng cách sử dụng biểu diễn Bag-of-Words (BoW) và PyTorch (phiên bản ≥ 1.6).

Đoạn mã tiền xử lý:
```python
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import torch
import torch.nn as nn
import torch.optim as optim

texts = ["I love this movie", "I hate this product", "Amazing quality", "Terrible service"]
labels = [1, 0, 1, 0]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts).toarray()
y = torch.tensor(labels)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
X_train = torch.tensor(X_train, dtype=torch.float32)
```

Phương án nào sau đây là phần mã đúng để huấn luyện mô hình phân loại nhị phân đơn giản với biểu diễn BoW, một tầng tuyến tính và hàm loss phù hợp?"""
            q['options'] = [
                "A. `model = nn.Linear(X_train.shape[1], 1); loss_fn = nn.BCEWithLogitsLoss(); outputs = model(X_train).squeeze(); loss = loss_fn(outputs, y_train.float())`",
                "B. `model = nn.Sequential(nn.Linear(X_train.shape[1], 10), nn.ReLU(), nn.Linear(10, 2)); loss_fn = nn.NLLLoss()`",
                "C. `model = nn.Linear(X_train.shape(1), 2); loss_fn = nn.CrossEntropyLoss()` (sai cú pháp .shape(1))",
                "D. `model = nn.Linear(X_train.shape[1], 1); loss_fn = nn.MSELoss()` (dùng MSE cho phân loại nhị phân)"
            ]

        elif qid == 27:
            q['question'] = """Câu 27. Cho đoạn mã dưới đây, kích thước của `output_tensor` là bao nhiêu?

```python
import tensorflow as tf

input_tensor = tf.constant(tf.random.normal(shape=(1, 32, 32, 3)), dtype=tf.float32)
conv_layer = tf.keras.layers.Conv2D(filters=32, kernel_size=(5, 5), strides=(2, 2), padding='same')

output_tensor = conv_layer(input_tensor)
print(output_tensor.shape)
```"""
            q['options'] = [
                "A. `(1, 16, 16, 32)`",
                "B. `(1, 16, 16, 3)`",
                "C. `(1, 14, 14, 32)`",
                "D. `(1, 32, 32, 32)`"
            ]

        elif qid == 33:
            q['question'] = """Câu 33. Chương trình sau thực hiện:
- Tải mô hình ResNet-50 pre-trained trên ImageNet.
- Đóng băng toàn bộ các layer convolution.
- Lấy output của lớp `avgpool` (shape `(2048, 1, 1)`) và flatten thành vector 2048 chiều.

Bạn thiếu dòng nào dưới đây để trả về vector đặc trưng (`features`)?

```python
import torch
import torchvision.models as models

model = models.resnet50(weights='DEFAULT')

for p in model.parameters():
    p.requires_grad_(False)

model.fc = torch.nn.Identity()
x = torch.randn(1, 3, 224, 224)

... # <-- Điền dòng mã vào đây

print(features.shape)
```"""
            q['options'] = [
                "A. `features = model(x)`",
                "B. `features = model.layer4(x)`",
                "C. `features = model.avgpool(x)`",
                "D. `features = x`"
            ]

        elif qid == 69:
            q['options'] = [
                'A. `gensim.models.load("word2vec")`',
                'B. `import word2vec.load_model(path)`',
                'C. `KeyedVectors.load_word2vec_format(path)`',
                'D. `spacy.load_word2vec(path)`'
            ]

        elif qid == 70:
            q['question'] = "Câu 70. Khi sử dụng câu lệnh `nn.CrossEntropyLoss` trong PyTorch, bạn nên đưa gì vào đối số đầu tiên?"
            q['options'] = [
                "A. Logits (chưa qua Softmax) do lớp cuối cùng của mạng tạo ra",
                "B. Vector gồm các số 0 và một số 1 (one-hot vector) biểu diễn các lớp mục tiêu",
                "C. Xác suất thu được sau khi áp dụng softmax lên đầu ra của mạng",
                "D. Log-xác suất sau khi áp dụng log_softmax lên đầu ra của mạng"
            ]

        elif qid == 73:
            q['question'] = """Câu 73. Mạng nơ-ron ResNet sử dụng kỹ thuật quan trọng gọi là kết nối tắt (skip connection / residual connection) để giải quyết hiện tượng biến mất đạo hàm (Vanishing Gradient). 

Dựa trên đoạn mã của khối `identity_block` dưới đây, hãy liệt kê các thành phần chính của khối theo đúng thứ tự xuất hiện và chỉ ra dòng mã thực hiện phép kết nối tắt:

```python
def identity_block(X, f, filters, stage, block):
    conv_name_base = 'res' + str(stage) + block + '_branch'
    bn_name_base   = 'bn'  + str(stage) + block + '_branch'
    F1, F2, F3 = filters
    
    # Dòng 8: Lưu trữ tensor đầu vào cho đường tắt (shortcut)
    X_shortcut = X
    
    # Dòng 10-12: Nhánh Conv 1x1
    X = Conv2D(filters=F1, kernel_size=(1, 1), strides=(1, 1), padding='valid', name=conv_name_base + '2a')(X)
    X = BatchNormalization(axis=3, name=bn_name_base + '2a')(X)
    X = Activation('relu')(X)
    
    # Dòng 14-16: Nhánh Conv fxf
    X = Conv2D(filters=F2, kernel_size=(f, f), strides=(1, 1), padding='same', name=conv_name_base + '2b')(X)
    X = BatchNormalization(axis=3, name=bn_name_base + '2b')(X)
    X = Activation('relu')(X)
    
    # Dòng 18-20: Nhánh Conv 1x1
    X = Conv2D(filters=F3, kernel_size=(1, 1), strides=(1, 1), padding='valid', name=conv_name_base + '2c')(X)
    X = BatchNormalization(axis=3, name=bn_name_base + '2c')(X)
    
    # Dòng 21: Phép kết nối tắt cộng tensor shortcut vào đầu ra
    X = Add()([X_shortcut, X])
    X = Activation('relu')(X)
    return X
```"""
            q['options'] = [
                "A. Ba cặp Conv2D − BatchNorm − ReLU; kết nối tắt ở dòng 8.",
                "B. Hai cặp Conv2D − BatchNorm − ReLU; kết nối tắt nằm trong BatchNorm ở dòng 11, 15, 19.",
                "C. Ba cặp Conv2D − BatchNorm − ReLU; Không có cơ chế kết nối tắt.",
                "D. Ba cặp Conv2D − BatchNorm − ReLU; kết nối tắt ở dòng 21 (`X = Add()([X_shortcut, X])`)."
            ]

        elif qid == 75:
            q['question'] = """Câu 75. Trong các kiến trúc mạng phân đoạn ảnh dạng bộ mã hóa – bộ giải mã (encoder – decoder), ví dụ như U-Net, các "kết nối tắt" (skip connections) đóng vai trò quan trọng. Chúng kết hợp thông tin đặc trưng từ các lớp ở bộ mã hóa (encoder path) với thông tin tương ứng ở bộ giải mã (decoder path) sau khi được phóng đại (upsampling).

Giả sử bạn đang xây dựng một lớp trong phần bộ giải mã của mạng U-Net bằng Python:
- `encoder_output`: Tensor đặc trưng từ lớp tương ứng ở bộ mã hóa.
- `decoder_input`: Tensor đầu vào ở bộ giải mã, đã được upsample để có cùng chiều cao (H) và chiều rộng (W) với `encoder_output`.

```python
# encoder_output.shape = (batch, H, W, C1) trong Keras  hoặc  (batch, C1, H, W) trong PyTorch
# decoder_input.shape  = (batch, H, W, C2) trong Keras  hoặc  (batch, C2, H, W) trong PyTorch

merged_features = some_concatenation_operation([decoder_input, encoder_output], axis=...)
```

Thao tác `some_concatenation_operation` và tham số `axis` phù hợp nhất để thực hiện kết nối tắt kiểu U-Net là gì?"""
            q['options'] = [
                "A. Phép cộng (`Add()`); không cần chỉ định `axis`",
                "B. Phép nối (`Concatenate()`) dọc theo chiều kênh: `axis=3` trong Keras hoặc `dim=1` trong PyTorch",
                "C. Phép nhân (`Multiply()`) từng phần tử",
                "D. Phép nối (`Concatenate()`) dọc theo chiều không gian: `axis=1` (chiều Height)"
            ]

        elif qid == 79:
            q['options'] = [
                "A. `model.gpu()`",
                "B. `model.to('cuda')` (hoặc `model.cuda()`)",
                "C. `model.cuda.enable()`",
                "D. `model.device('GPU')`"
            ]

        elif qid == 82:
            q['options'] = [
                "A. `model.weights`",
                "B. `model.intercept_`",
                "C. `model.coefficients`",
                "D. `model.coef_`"
            ]

        elif qid == 88:
            q['options'] = [
                "A. `F.dropout(0.5)`",
                "B. `nn.dropout(0.5)`",
                "C. `nn.Dropout(p=0.5)`",
                "D. `nn.Dropout2d(0.5)`"
            ]

    new_json = json.dumps(data, ensure_ascii=False, indent=2)
    new_content = '// quiz.js - Complete Exam Simulator with 120 Authentic Questions (100 VAIO 2025 & 20 VAIC 2026)\n\nconst QUIZ_DATA = ' + new_json + ';\n'

    with open('quiz.js', 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f'Updated quiz.js successfully ({len(data)} questions).')

if __name__ == '__main__':
    main()
