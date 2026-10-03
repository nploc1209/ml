# -*- coding: utf-8 -*-
"""
upgrade_lesson_6.py - Masterpiece Lesson 6 for VAIO 2025 AI Olympiad
Chủ đề: Các Chỉ Số Đánh Giá (Metrics) & Dữ Liệu Mất Cân Bằng (Class Imbalance)
Toàn diện từ con số 0 đến làm chủ sâu sắc.

Tuân thủ nghiêm ngặt chuẩn sư phạm:
Trực giác đời sống -> Bản chất toán học -> Cách thức hoạt động ->
Giải mã ký hiệu cho học sinh lớp 12 -> Ví dụ tính toán bằng số từng bước ->
Cạm bẫy phòng thi -> Câu hỏi trắc nghiệm kiểm tra độ hiểu có lời giải chi tiết.
"""

def get_masterpiece_lesson_6():
    return {
        "id": "lesson-6",
        "title": "6. Các Chỉ Số Đánh Giá (Metrics) & Dữ Liệu Mất Cân Bằng",
        "syllabusBadge": "BUỔI 5: METRICS ĐÁNH GIÁ & IMBALANCED DATA",
        "summary": "Thước đo thành bại của mọi bài toán Machine Learning: Phá vỡ ảo tưởng Accuracy Paradox, làm chủ Ma trận nhầm lẫn (Confusion Matrix 2×2), cân não giữa Lỗi Loại 1 (Báo động giả) và Lỗi Loại 2 (Bỏ sót hiểm họa), giải mã bản chất toán học của Precision, Recall, Trung bình điều hòa F1-Score (và F_beta), so sánh sâu sắc ROC-AUC vs PR-Curve trên dữ liệu mất cân bằng nặng, cùng 3 cấp độ chiến thuật công nghiệp: SMOTE, Class Weighting và Threshold Tuning.",
        "intuition": {
            "title": "Trực giác thực tế: Vị 'bác sĩ lười biếng' và bài học xương máu về độ chính xác 99.5%",
            "content": """Hãy tưởng tượng một thị trấn nhỏ có 1,000 người dân cùng đi xét nghiệm tầm soát một căn bệnh ung thư hiếm gặp. Trong thực tế, chỉ có đúng 5 người thực sự mang mầm bệnh nguy hiểm, còn 995 người hoàn toàn khỏe mạnh.

Một 'bác sĩ lười biếng' (hoặc một mô hình AI sơ sài) nghĩ ra một mánh khóe gian lận: Ông ta không thèm xem xét bất kỳ kết quả chụp X-quang hay xét nghiệm máu nào, mà chỉ viết sẵn một kết luận duy nhất cho tất cả 1,000 người:
'BẠN HOÀN TOÀN KHỎE MẠNH, CHÚC MỪNG BẠN!'

Khi hội đồng y khoa kiểm tra lại kết quả:
- Ông ta đã đoán đúng cho 995 người khỏe mạnh!
- Độ chính xác toàn thể (Accuracy) đạt: 995 / 1000 = 99.5%!
Các tờ báo giật tít: 'Bác sĩ thiên tài chẩn đoán chính xác tới 99.5%!'.

Nhưng sự thật đằng sau là gì?
Cả 5 người bệnh thực sự đều bị ông ta phán là 'khỏe mạnh', yên tâm ra về, không được điều trị và bỏ lỡ thời gian vàng cứu sống! Trong số 5 người bệnh cần cứu nhất, ông ta đã bỏ lọt cả 5 (tỷ lệ bắt trúng Recall = 0%). Bác sĩ này không phải thiên tài, mà là một thảm họa y tế!

Đây chính là **Nghịch lý độ chính xác (Accuracy Paradox)** kinh điển trong Trí tuệ Nhân tạo: Khi tập dữ liệu bị mất cân bằng trầm trọng (lớp đa số áp đảo lớp thiểu số), chỉ số Accuracy trở thành một tấm bình phong giả tạo, ru ngủ các kỹ sư và che giấu sự sụp đổ hoàn toàn của hệ thống! Để giải quyết bài toán này, ta bắt buộc phải có một hệ thống thước đo đa chiều và các kỹ thuật cân bằng dữ liệu khoa học."""
        },
        "sections": [
            # =================================================================
            # MỤC 6.1: NGHỊCH LÝ ĐỘ CHÍNH XÁC (ACCURACY PARADOX)
            # =================================================================
            {
                "heading": "6.1. Khởi Đầu Từ Con Số 0: Tại Sao Accuracy Là Một Cái Bẫy Chết Người? Nghịch Lý Độ Chính Xác (Accuracy Paradox)",
                "content": "Trong các bài học phổ thông, học sinh thường mặc định 'tỷ lệ đoán đúng càng cao thì càng giỏi'. Nhưng trong thế giới dữ liệu thực tế, khi các lớp phân bố không đều nhau, việc tin tưởng mù quáng vào Accuracy sẽ dẫn đến những sai lầm chết người.",
                "deepDive": r"""**1. Khái niệm Dữ liệu Mất Cân Bằng (Class Imbalance):**
Trong bài toán phân loại nhị phân (Binary Classification), ta thường chia dữ liệu thành 2 nhãn:
- **Lớp Âm tính (Negative Class / Nhãn 0):** Đại diện cho trạng thái bình thường, phổ biến.
- **Lớp Dương tính (Positive Class / Nhãn 1):** Đại diện cho trạng thái đặc biệt, hiếm hoi, hiểm họa hoặc mục tiêu cần phát hiện.

Hiện tượng **Mất cân bằng lớp (Class Imbalance)** xảy ra khi số lượng mẫu của một lớp áp đảo hoàn toàn lớp còn lại:
- *Mất cân bằng nhẹ (1:3 đến 1:10):* Dự đoán khách hàng hủy dịch vụ viễn thông (Churn Prediction).
- *Mất cân bằng vừa (1:10 đến 1:100):* Phát hiện bình luận độc hại, vi phạm chính sách mạng xã hội.
- *Mất cân bằng cực độ (1:100 đến 1:1,000,000):* Phát hiện giao dịch gian lận thẻ tín dụng (Fraud Detection: 99.98% giao dịch bình thường, 0.02% ăn cắp), tầm soát ung thư y tế, phát hiện lỗi vi mạch bán dẫn Intel, phát hiện tấn công mạng thâm nhập hệ thống.

**2. Bản chất toán học của Nghịch lý Accuracy (Accuracy Paradox):**
Công thức tính Độ chính xác toàn thể (Accuracy):
$$\text{Accuracy} = \frac{\text{Số lượng mẫu đoán đúng}}{\text{Tổng số lượng mẫu}} = \frac{N_{\text{correct}}}{N}$$

Giả sử trong quần thể, xác suất tiên nghiệm của lớp âm tính là $P(Y=0) = 1 - \epsilon$ (với $\epsilon \ll 1$, ví dụ $\epsilon = 0.001 = 0.1\%$).
Một mô hình tầm thường (Trivial Classifier / Majority Class Predictor) luôn đưa ra dự đoán $\hat{Y} = 0$ cho mọi trường hợp:
$$\text{Accuracy} = P(\hat{Y} = Y) = P(\hat{Y}=0 \mid Y=0)P(Y=0) + P(\hat{Y}=0 \mid Y=1)P(Y=1)$$
$$= 1 \times (1 - \epsilon) + 0 \times \epsilon = 1 - \epsilon = 99.9\%$$

Mô hình không cần học bất kỳ đặc trưng nào (Features) từ dữ liệu, trọng số $w$ không cần tối ưu, nhưng vẫn hiển nhiên đạt điểm 99.9%!

**3. Tại sao thuật toán Machine Learning dễ bị tha hóa khi tối ưu Accuracy?**
Khi bạn huấn luyện mô hình bằng hàm mất mát tiêu chuẩn (như Cross-Entropy hoặc 0-1 Loss) mà không có trọng số điều chỉnh:
- Mô hình nhận thấy rằng: Nếu nó cố gắng học lớp thiểu số, việc đoán sai một vài mẫu đa số sẽ khiến Loss tăng vọt!
- Ngược lại, nếu nó 'chấp nhận buông xuôi', phán tất cả là 0, thì tổng Loss toàn cục lập tức chạm đáy cực tiểu!
- Kết quả: Gradient Descent sẽ kéo toàn bộ tham số về điểm cực tiểu giả tạo này. Mô hình trở nên 'mù' hoàn toàn trước các dấu hiệu của lớp thiểu số!

**4. Quy tắc bài học:**
Tuyệt đối không bao giờ dùng Accuracy làm chỉ số đánh giá duy nhất khi tỷ lệ mất cân bằng giữa hai lớp vượt quá 1:4!""",
                "formula": r"\text{Accuracy} = \frac{N_{\text{correct}}}{N_{\text{total}}}, \quad \lim_{\epsilon \to 0} \text{Accuracy}(\text{Majority Classifier}) = 100\%",
                "mathExplainer": [
                    { "sym": "N_{\\text{correct}}", "name": "Số mẫu đoán đúng", "mean": "Tổng số quan sát mà nhãn dự đoán trùng khớp hoàn toàn với nhãn thực tế." },
                    { "sym": "N_{\\text{total}}", "name": "Tổng kích thước dữ liệu", "mean": "Tổng số lượng tất cả các mẫu quan sát trong tập kiểm thử (Test Set)." },
                    { "sym": "\\epsilon (Epsilon)", "name": "Tỷ lệ lớp thiểu số", "mean": "Tỷ lệ phần trăm rất nhỏ của các mẫu mang tính nguy hiểm hoặc mục tiêu cần tìm (ví dụ 0.1%)." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 160" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="160" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(30, 20)">
                        <text x="290" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Ảo Tưởng Accuracy Trong Dữ Liệu Mất Cân Bằng (1,000 Mẫu)</text>
                        <!-- Majority class 995 samples -->
                        <rect x="20" y="35" width="530" height="35" fill="#f0f0f0" stroke="#111" stroke-width="1.5"/>
                        <text x="280" y="57" font-family="Georgia" font-size="11" text-anchor="middle">995 Người Khỏe Mạnh (Âm tính - Negative) - Dự đoán đúng: 995/995</text>
                        <!-- Minority class 5 samples -->
                        <rect x="550" y="35" width="25" height="35" fill="#111"/>
                        <text x="562" y="57" font-family="Georgia" font-size="9" fill="#fff" text-anchor="middle">5</text>

                        <!-- Outcome labels -->
                        <g transform="translate(20, 85)">
                          <rect x="0" y="0" width="260" height="45" fill="#fff" stroke="#111" stroke-width="1"/>
                          <text x="130" y="18" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">Chỉ Số Bề Nổi (Báo Chí)</text>
                          <text x="130" y="36" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Accuracy = 99.5% (Rất cao!)</text>
                        </g>

                        <g transform="translate(295, 85)">
                          <rect x="0" y="0" width="280" height="45" fill="#111"/>
                          <text x="140" y="18" font-family="Georgia" font-size="10" font-weight="bold" fill="#fff" text-anchor="middle">Bản Chất Thực Tế (Y Tế &amp; Đời Sống)</text>
                          <text x="140" y="36" font-family="Georgia" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">Bắt trúng bệnh nhân: 0/5 = 0%!</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "Mô hình đoán bừa toàn bộ là Âm tính vẫn đạt Accuracy 99.5% nhưng để lọt 100% bệnh nhân tử vong (Nghịch lý Accuracy Paradox)."
                },
                "commonPitfalls": "Cạm bẫy phòng thi VAIO: Đề bài cho một tập dữ liệu phát hiện giao dịch gian lận với tỷ lệ 99.9% bình thường và 0.1% gian lận. Một mô hình Baseline đoán toàn bộ giao dịch là bình thường. Nếu câu hỏi trắc nghiệm hỏi: 'Mô hình này có hoạt động tốt không?', đáp án khẳng định 'Rất tốt vì Accuracy đạt 99.9%' là SAI HOÀN TOÀN! Độ chính xác cao ở đây chỉ là ảo ảnh toán học.",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Một ngân hàng có 100,000 giao dịch mỗi ngày, trong đó có 200 giao dịch là gian lận tín dụng (Fraud). Một kỹ sư dữ liệu xây dựng một mô hình luôn gán nhãn 'Giao dịch hợp lệ' cho tất cả mọi giao dịch. Độ chính xác Accuracy của mô hình này là bao nhiêu và mô hình có giá trị thực tế không?",
                    "options": [
                        "A. Accuracy = 99.8%, mô hình cực kỳ xuất sắc và nên triển khai ngay",
                        "B. Accuracy = 99.8%, nhưng mô hình hoàn toàn vô dụng vì không ngăn chặn được bất kỳ vụ trộm tiền nào",
                        "C. Accuracy = 0.2%, mô hình rất tệ",
                        "D. Accuracy = 50.0%, tương đương đoán mò ngẫu nhiên"
                    ],
                    "correctIndex": 1,
                    "hint": "Tính tỷ lệ mẫu hợp lệ trên tổng số mẫu: (100,000 - 200) / 100,000 = 99,800 / 100,000 = 99.8%. Nhưng có kẻ trộm nào bị bắt không?",
                    "solution": [
                        "Bước 1: Tính số giao dịch hợp lệ thực tế: 100,000 - 200 = 99,800 giao dịch.",
                        "Bước 2: Vì mô hình đoán tất cả là hợp lệ, nên nó đoán đúng toàn bộ 99,800 giao dịch này. Số mẫu đoán đúng = 99,800.",
                        "Bước 3: Tính Accuracy: 99,800 / 100,000 = 0.998 = 99.8%.",
                        "Bước 4: Đánh giá giá trị thực tiễn: Toàn bộ 200 vụ trộm tiền đều trót lọt thành công mà không bị phát hiện. Mô hình hoàn toàn vô dụng trên thực tế.",
                        "Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 6.2: MA TRẬN NHẦM LẪN (CONFUSION MATRIX) & LỖI LOẠI 1 VS LOẠI 2
            # =================================================================
            {
                "heading": "6.2. Ma Trận Nhầm Lẫn (Confusion Matrix 2×2): Giải Mã TP, FP, TN, FN & Cuộc Đối Đầu Giữa Lỗi Loại 1 và Lỗi Loại 2",
                "content": "Để bóc trần toàn bộ sự thật về hiệu năng của mô hình phân loại, ta không thể dùng một con số duy nhất. Ta bắt buộc phải lập bảng Ma Trận Nhầm Lẫn (Confusion Matrix) nhằm giải phẫu chi tiết 4 khả năng ghép cặp giữa Thực Tế và Dự Đoán.",
                "deepDive": r"""**1. Cấu trúc bảng Ma Trận Nhầm Lẫn (Confusion Matrix 2×2):**
Bảng gồm 2 hàng và 2 cột phân chia theo hai chiều:
- **Chiều dọc (Hàng):** Giá trị Thực Tế ngoài đời (Ground Truth / Actual Class).
- **Chiều ngang (Cột):** Giá trị Máy Dự Đoán (Predicted Class).

*(Lưu ý: Quy ước hàng/cột có thể hoán đổi tùy tài liệu, nhưng bản chất 4 đại lượng bên trong là bất biến).*

| | Máy Đoán: DƯƠNG TÍNH (+1) | Máy Đoán: ÂM TÍNH (-1) |
|---|---|---|
| **Thực Tế: DƯƠNG TÍNH (+1)** | **TP (True Positive)** | **FN (False Negative)** |
| **Thực Tế: ÂM TÍNH (-1)** | **FP (False Positive)** | **TN (True Negative)** |

**2. Giải mã ý nghĩa từng chữ cái (Mẹo nhớ vĩnh viễn không bao giờ lú):**
Mỗi ký hiệu gồm đúng 2 chữ cái:
- **Chữ cái đầu tiên (True / False):** Trả lời câu hỏi: *'Cái máy đoán ĐÚNG (True) hay SAI (False) so với thực tế?'*
- **Chữ cái thứ hai (Positive / Negative):** Trả lời câu hỏi: *'Cái máy vừa NÓI RA chữ gì (Positive hay Negative)?'*

Cụ thể:
1. **TP (True Positive - Thật Dương):**
   - Máy nói: Positive (+). Thực tế: Đúng là (+). $\implies$ **Máy đoán trúng ca bệnh!** (Thành công vang dội).
2. **TN (True Negative - Thật Âm):**
   - Máy nói: Negative (-). Thực tế: Đúng là (-). $\implies$ **Máy nhận diện đúng người lành!** (Thành công).
3. **FP (False Positive - Giả Dương - LỖI LOẠI 1 / Type I Error):**
   - Máy nói: Positive (+). Thực tế: Sai rồi, người ta (-)!
   - **Bản chất đời sống:** **BÁO ĐỘNG GIẢ (False Alarm)**.
   - Ví dụ: Chuông báo cháy hú inh ỏi khi chỉ có người hút thuốc lá; Thư mời phỏng vấn xin việc bị Gmail tống nhầm vào hòm thư Rác (Spam).
4. **FN (False Negative - Giả Âm - LỖI LOẠI 2 / Type II Error):**
   - Máy nói: Negative (-). Thực tế: Sai rồi, người ta CÓ BỆNH (+) mà máy bảo không!
   - **Bản chất đời sống:** **BỎ SÓT HIỂM HỌA (Missed Hazard / Bỏ lọt tội phạm)**.
   - Ví dụ: Bệnh nhân ung thư bị máy bảo 'bình thường' đi về nhà; Kẻ khủng bố mang vũ khí vượt qua cổng quét an ninh máy bay mà không bị phát hiện.

**3. Cuộc đối đầu triết học: Lỗi Loại 1 vs Lỗi Loại 2 - Cái giá nào đắt hơn?**
Tùy thuộc vào bản chất của lĩnh vực ứng dụng, cái giá phải trả của hai loại lỗi này hoàn toàn khác nhau:

- **Khi Lỗi Loại 2 (FN) là thảm họa chết người (Ưu tiên giảm FN bằng mọi giá):**
  - Chẩn đoán y khoa hiểm nghèo, an toàn hàng không, cảnh báo động đất, phát hiện lỗi phanh ô tô tự lái.
  - *Quy tắc:* Thà báo động nhầm 10 lần (chấp nhận FP cao) để kiểm tra lại, còn hơn bỏ sót 1 ca tử vong (không thể chấp nhận FN)!

- **Khi Lỗi Loại 1 (FP) là tai họa phá hủy uy tín (Ưu tiên giảm FP bằng mọi giá):**
  - Tòa án hình sự (Nguyên tắc suy đoán vô tội): *"Thà tha lầm 10 kẻ có tội (FN), còn hơn kết án oan 1 người vô tội (FP)"*.
  - Bộ lọc thư rác (Spam Filter): Thà để lọt vài email quảng cáo vào Inbox (FN) còn hơn xóa nhầm một hợp đồng triệu đô của khách hàng (FP).""",
                "formula": r"\text{Total} = \text{TP} + \text{TN} + \text{FP} + \text{FN}, \quad \text{Error Rate} = \frac{\text{FP} + \text{FN}}{\text{Total}}",
                "mathExplainer": [
                    { "sym": "\\text{TP}", "name": "True Positive (Dương tính thật)", "mean": "Thực tế Có (+), Máy đoán Có (+) => Đúng." },
                    { "sym": "\\text{TN}", "name": "True Negative (Âm tính thật)", "mean": "Thực tế Không (-), Máy đoán Không (-) => Đúng." },
                    { "sym": "\\text{FP (Type I Error)}", "name": "False Positive (Dương tính giả)", "mean": "Báo động nhầm: Thực tế Không (-), Máy đoán Có (+) => Lỗi loại 1." },
                    { "sym": "\\text{FN (Type II Error)}", "name": "False Negative (Âm tính giả)", "mean": "Bỏ sót nguy hiểm: Thực tế Có (+), Máy đoán Không (-) => Lỗi loại 2." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 220" width="100%" height="220" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="220" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(60, 20)">
                        <text x="260" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">MA TRẬN NHẦM LẪN (CONFUSION MATRIX 2×2)</text>
                        <!-- Headers -->
                        <text x="200" y="45" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Máy Đoán: DƯƠNG (+)</text>
                        <text x="370" y="45" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Máy Đoán: ÂM (-)</text>
                        <text x="20" y="95" font-family="Georgia" font-size="11" font-weight="bold">Thực Tế: DƯƠNG (+)</text>
                        <text x="20" y="165" font-family="Georgia" font-size="11" font-weight="bold">Thực Tế: ÂM (-)</text>

                        <!-- Cell 1: TP -->
                        <rect x="120" y="60" width="160" height="60" fill="#fff" stroke="#111" stroke-width="2"/>
                        <text x="200" y="82" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">TP (True Positive)</text>
                        <text x="200" y="102" font-family="Georgia" font-size="10" fill="#333" text-anchor="middle">Đúng: Bắt trúng mục tiêu</text>

                        <!-- Cell 2: FN -->
                        <rect x="290" y="60" width="160" height="60" fill="#111"/>
                        <text x="370" y="82" font-family="Georgia" font-size="12" font-weight="bold" fill="#fff" text-anchor="middle">FN (False Negative)</text>
                        <text x="370" y="102" font-family="Georgia" font-size="10" fill="#ccc" text-anchor="middle">LỖI LOẠI 2: Bỏ sót hiểm họa!</text>

                        <!-- Cell 3: FP -->
                        <rect x="120" y="130" width="160" height="60" fill="#eee" stroke="#111" stroke-width="1.5"/>
                        <text x="200" y="152" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">FP (False Positive)</text>
                        <text x="200" y="172" font-family="Georgia" font-size="10" fill="#444" text-anchor="middle">LỖI LOẠI 1: Báo động giả!</text>

                        <!-- Cell 4: TN -->
                        <rect x="290" y="130" width="160" height="60" fill="#fff" stroke="#111" stroke-width="2"/>
                        <text x="370" y="152" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">TN (True Negative)</text>
                        <text x="370" y="172" font-family="Georgia" font-size="10" fill="#333" text-anchor="middle">Đúng: Nhận diện an toàn</text>
                      </g>
                    </svg>""",
                    "caption": "Cấu trúc 4 ô của Ma Trận Nhầm Lẫn: Phân biệt rạch ròi Lỗi Loại 1 (Báo động giả) và Lỗi Loại 2 (Bỏ sót hiểm họa)."
                },
                "commonPitfalls": "Nhầm lẫn giữa chữ cái thứ nhất và thứ hai: Nhiều học sinh nghĩ FP nghĩa là 'False' nên thực tế là Sai. HÃY NHỚ: Chữ cái thứ 2 là LỜI DỰ ĐOÁN CỦA MÁY (Positive = Máy đoán Dương). Chữ cái thứ 1 là PHÁN QUYẾT (False = Máy đoán Sai). Máy đoán Dương mà lại đoán Sai => Thực tế là Âm tính! Ngược lại, FN là máy đoán Âm tính mà lại đoán Sai => Thực tế là Dương tính!",
                "practiceQuestion": {
                    "level": "Cơ bản",
                    "question": "Trong câu chuyện ngụ ngôn nổi tiếng 'Chú bé chăn cừu', chú bé nghịch ngợm hét to: 'Có sói! Có sói!' để lừa dân làng chạy lên đồi, trong khi thực tế không hề có con sói nào. Hành vi của chú bé tương ứng với loại lỗi nào trong Thống kê và Học máy?",
                    "options": [
                        "A. True Positive (Dương tính thật)",
                        "B. False Positive (Lỗi Loại 1 - Báo động giả)",
                        "C. False Negative (Lỗi Loại 2 - Bỏ sót mục tiêu)",
                        "D. True Negative (Âm tính thật)"
                    ],
                    "correctIndex": 1,
                    "hint": "Chú bé đưa ra dự đoán Dương tính (+ Có sói) nhưng thực tế là Âm tính (- Không có sói). Máy đoán Có nhưng thực tế Không => Báo động giả.",
                    "solution": [
                        "Bước 1: Xác định thực tế (Ground Truth): Không có sói (- Negative).",
                        "Bước 2: Xác định dự đoán đưa ra: Chú bé hét 'Có sói!' (+ Positive).",
                        "Bước 3: So sánh: Dự đoán là Positive nhưng bị Sai (False) => False Positive (FP).",
                        "Bước 4: Đây chính là Lỗi Loại 1 (Type I Error) - hiện tượng Báo động giả kinh điển.",
                        "Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 6.3: PRECISION, RECALL & ĐIỂM F1-SCORE (HARMONIC MEAN)
            # =================================================================
            {
                "heading": "6.3. Bộ Ba Thước Đo Cốt Lõi: Precision, Recall & Điểm Cân Bằng Điều Hòa F1-Score ($F_\\beta$)",
                "content": "Từ 4 ô cơ bản của Confusion Matrix, cộng đồng khoa học dữ liệu đã phát triển nên bộ ba thước đo quyền lực nhất: Precision (Độ chuẩn xác), Recall (Độ nhạy) và F1-Score (Trung bình điều hòa).",
                "deepDive": r"""**1. Precision (Độ chuẩn xác / Độ chính xác dương):**
- **Câu hỏi cốt lõi:** *"Trong số tất cả những lần mô hình lớn tiếng khẳng định là DƯƠNG TÍNH, có bao nhiêu phần trăm là đúng sự thật?"*
- **Công thức:**
  $$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}}$$
- **Phân tích mẫu số:** Mẫu số $(\text{TP} + \text{FP})$ chính là **Toàn bộ những mẫu được mô hình dự đoán là Positive** (Tổng cột 1).
- **Ý nghĩa:** Đo lường **Độ tin cậy của lời cảnh báo**. Nếu mô hình cảnh báo giao dịch gian lận có Precision = 95%, nhân viên ngân hàng biết rằng hễ hệ thống 'hú còi' thì 95% khả năng đó là trộm thật, yên tâm khóa thẻ mà không sợ làm phiền oan khách hàng.

**2. Recall / Sensitivity / Hit Rate (Độ nhạy / Độ bao phủ / Tỷ lệ thu hồi):**
- **Câu hỏi cốt lõi:** *"Trong số tất cả những trường hợp THỰC SỰ LÀ DƯƠNG TÍNH tồn tại ngoài đời, mô hình đã bắt trúng được bao nhiêu phần trăm?"*
- **Công thức:**
  $$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$
- **Phân tích mẫu số:** Mẫu số $(\text{TP} + \text{FN})$ chính là **Tổng số mẫu Dương tính thật trong tự nhiên** (Tổng hàng 1).
- **Ý nghĩa:** Đo lường **Năng lực không bỏ sót hiểm họa**. Nếu hệ thống tầm soát ung thư có Recall = 98%, nghĩa là cứ 100 người mắc ung thư thật, máy phát hiện ra 98 người, chỉ để lọt 2 người.

**3. Specificity (Độ đặc hiệu):**
- Tỷ lệ nhận diện đúng người khỏe mạnh trong toàn bộ những người khỏe mạnh thật:
  $$\text{Specificity} = \frac{\text{TN}}{\text{TN} + \text{FP}}$$

**4. Cuộc xung đột vĩnh cửu: Sự đánh đổi Precision-Recall (Precision-Recall Trade-off):**
Mọi mô hình phân loại đều có một ngưỡng quyết định xác suất $\theta$ (mặc định $\theta = 0.5$):
- **Nếu tăng ngưỡng $\theta$ lên rất cao (ví dụ $\theta = 0.95$):**
  - Mô hình trở nên 'cực kỳ cẩn trọng'. Chỉ khi nào chắc chắn 95% nó mới dám đoán Dương tính.
  - Hậu quả: FP giảm mạnh về 0 $\implies$ **Precision tăng vọt**, nhưng sẽ có vô số mẫu bị bỏ sót $\implies$ FN tăng $\implies$ **Recall giảm thê thảm**!
- **Nếu hạ ngưỡng $\theta$ xuống rất thấp (ví dụ $\theta = 0.05$):**
  - Mô hình trở nên 'cực kỳ nhạy cảm'. Thấy hơi nghi ngờ là phán Dương tính ngay.
  - Hậu quả: FN giảm về 0 $\implies$ **Recall tăng vọt chạm 100%**, nhưng tiếng chuông báo động giả vang lên khắp nơi $\implies$ FP tăng vọt $\implies$ **Precision rớt chạm đáy**!
$\implies$ Hai chỉ số này luôn hoạt động như hai đầu của một chiếc bập bênh: Kéo một đầu lên thì đầu kia tụt xuống!

**5. F1-Score: Tại sao lại là Trung bình điều hòa (Harmonic Mean)?**
Ta cần một chỉ số tổng hợp duy nhất dung hòa cả Precision ($P$) và Recall ($R$).
Tại sao ta không lấy Trung bình cộng: $\frac{P + R}{2}$?

*Hãy xem xét một ví dụ phản chứng cực đoan:*
Giả sử một mô hình chỉ đoán đúng duy nhất 1 mẫu và từ chối đoán tất cả các mẫu còn lại:
$\text{Precision} = 1.0$ (100%), nhưng $\text{Recall} = 0.01$ (1%).
- Nếu tính bằng Trung bình cộng (Arithmetic Mean):
  $$\bar{A} = \frac{1.0 + 0.01}{2} = 0.505 \quad (50.5\%)$$
  Con số $50.5\%$ tạo cảm giác mô hình 'ở mức trung bình chấp nhận được', che đậy sự thật là nó đã bỏ sót $99\%$ mục tiêu!
- Nếu tính bằng Trung bình điều hòa (Harmonic Mean):
  $$F_1 = \frac{2}{\frac{1}{P} + \frac{1}{R}} = \frac{2 \cdot P \cdot R}{P + R} = \frac{2 \times 1.0 \times 0.01}{1.0 + 0.01} = \frac{0.02}{1.01} \approx 0.0198 \quad (1.98\%)$$
  Trung bình điều hòa kéo tụt điểm số về sát 0 ngay lập tức!
  **Bản chất:** Trung bình điều hòa phạt cực kỳ nặng nề nếu có bất kỳ thành phần nào bị sụp đổ. $F_1$ chỉ có thể đạt điểm cao khi CẢ HAI $P$ và $R$ đều đồng thời ở mức cao!

**6. Mở rộng nâng cao: Điểm $F_\beta$-Score:**
Khi một bài toán coi trọng một bên hơn bên kia, ta dùng công thức tổng quát $F_\beta$:
$$F_\beta = (1 + \beta^2) \frac{\text{Precision} \cdot \text{Recall}}{\beta^2 \cdot \text{Precision} + \text{Recall}}$$
- $\beta = 1$: $F_1$-score (Coi trọng $P$ và $R$ ngang nhau).
- $\beta = 2$ ($F_2$-score): Coi trọng **Recall gấp đôi** Precision (Thích hợp cho y tế, cứu nạn).
- $\beta = 0.5$ ($F_{0.5}$-score): Coi trọng **Precision gấp đôi** Recall (Thích hợp cho lọc spam, gợi ý mua sắm).""",
                "formula": r"\text{Precision} = \frac{\text{TP}}{\text{TP}+\text{FP}}, \quad \text{Recall} = \frac{\text{TP}}{\text{TP}+\text{FN}}, \quad F_\beta = (1+\beta^2)\frac{P \cdot R}{\beta^2 P + R}",
                "mathExplainer": [
                    { "sym": "\\text{Precision} (P)", "name": "Độ chuẩn xác", "mean": "TP / (TP + FP): Tỷ lệ dự đoán đúng trong số tất cả những ca máy tuyên bố là Dương tính." },
                    { "sym": "\\text{Recall} (R)", "name": "Độ nhạy / Thu hồi", "mean": "TP / (TP + FN): Tỷ lệ bắt trúng trong số tất cả các ca thực sự Dương tính ngoài tự nhiên." },
                    { "sym": "F_1", "name": "Điểm F1", "mean": "Trung bình điều hòa của Precision và Recall: 2PR / (P + R)." },
                    { "sym": "\\beta (Beta)", "name": "Hệ số ưu tiên Recall", "mean": "Hệ số điều chỉnh mức độ quan trọng: beta > 1 ưu tiên Recall; beta < 1 ưu tiên Precision." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 20)">
                        <text x="280" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Chiếc Bập Bênh Đánh Đổi Giữa Precision Và Recall</text>

                        <!-- Seesaw fulcrum -->
                        <polygon points="280,110 260,140 300,140" fill="#111"/>
                        <line x1="100" y1="90" x2="460" y2="130" stroke="#111" stroke-width="4"/>

                        <!-- Left box: High Precision -->
                        <g transform="translate(70, 45)">
                          <rect x="0" y="0" width="120" height="45" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="60" y="18" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Precision TĂNG</text>
                          <text x="60" y="34" font-family="Georgia" font-size="9" fill="#555" text-anchor="middle">Siết ngưỡng θ cao (0.9)</text>
                        </g>

                        <!-- Right box: Low Recall -->
                        <g transform="translate(390, 110)">
                          <rect x="0" y="0" width="120" height="45" fill="#111"/>
                          <text x="60" y="18" font-family="Georgia" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">Recall GIẢM</text>
                          <text x="60" y="34" font-family="Georgia" font-size="9" fill="#ccc" text-anchor="middle">Bỏ sót nhiều mẫu hiểm</text>
                        </g>

                        <text x="280" y="165" font-family="Georgia" font-size="11" font-style="italic" text-anchor="middle">Điểm cân bằng lý tưởng được đo bằng F1 = 2 × (P × R) / (P + R)</text>
                      </g>
                    </svg>""",
                    "caption": "Sự đánh đổi tất yếu (Trade-off): Tăng Precision thường phải trả giá bằng việc giảm Recall và ngược lại."
                },
                "commonPitfalls": "Nhầm lẫn mẫu số giữa Precision và Recall: Hãy nhớ quy tắc 'Nhìn Cột hay Nhìn Hàng'. Precision nhìn theo CỘT DỰ ĐOÁN (Mẫu số là TP + FP). Recall nhìn theo HÀNG THỰC TẾ (Mẫu số là TP + FN). Không bao giờ nhầm lẫn hai mẫu số này trong phòng thi!",
                "practiceQuestion": {
                    "level": "Trung bình",
                    "question": "Một hệ thống phát hiện tin nhắn lừa đảo phân loại 1,000 tin nhắn. Kết quả thu được: TP = 80, FP = 20, FN = 20, TN = 880. Giá trị Precision, Recall và F1-Score của hệ thống lần lượt là:",
                    "options": [
                        "A. Precision = 80%, Recall = 80%, F1 = 0.80",
                        "B. Precision = 80%, Recall = 88.8%, F1 = 0.84",
                        "C. Precision = 88.8%, Recall = 80%, F1 = 0.84",
                        "D. Precision = 80%, Recall = 20%, F1 = 0.32"
                    ],
                    "correctIndex": 0,
                    "hint": "Tính Precision = TP / (TP + FP) = 80 / (80 + 20). Tính Recall = TP / (TP + FN) = 80 / (80 + 20).",
                    "solution": [
                        "Bước 1: Tính Precision = TP / (TP + FP) = 80 / (80 + 20) = 80 / 100 = 0.80 = 80%.",
                        "Bước 2: Tính Recall = TP / (TP + FN) = 80 / (80 + 20) = 80 / 100 = 0.80 = 80%.",
                        "Bước 3: Vì Precision = Recall = 0.8, nên F1-score hiển nhiên bằng đúng 0.80 (2 * 0.8 * 0.8 / (0.8 + 0.8) = 0.80).",
                        "Đáp án chính xác: A."
                    ]
                }
            },

            # =================================================================
            # MỤC 6.4: ĐƯỜNG CONG ROC-AUC VS PR-CURVE
            # =================================================================
            {
                "heading": "6.4. Đường Cong ROC-AUC vs PR-Curve: Đánh Giá Mô Hình Độc Lập Với Ngưỡng Quyết Định (Threshold-Independent)",
                "content": "Các mô hình phân loại xác suất không trực tiếp gán nhãn 0 hay 1 mà xuất ra xác suất p ∈ [0, 1]. Đường cong ROC và đường cong PR sinh ra để đánh giá năng lực phân loại của mô hình trên toàn bộ phổ ngưỡng quyết định có thể có.",
                "deepDive": r"""**1. Sự hạn chế của việc chọn ngưỡng cố định:**
Khi ta tính Confusion Matrix tại ngưỡng $\theta = 0.5$, ta chỉ đang chụp một 'bức ảnh tĩnh' của mô hình tại duy nhất một điểm cắt. Nếu một kỹ sư khác chọn ngưỡng $\theta = 0.3$, các chỉ số TP, FP, TN, FN sẽ thay đổi hoàn toàn!
Làm thế nào để đánh giá xem thuật toán nào thực sự thông minh hơn mà không phụ thuộc vào việc ai chọn ngưỡng khéo hơn? Ta cần đánh giá **Khả năng xếp hạng (Ranking ability / Discrimination power)** của mô hình!

**2. Đường cong ROC (Receiver Operating Characteristic):**
- *Lịch sử:* Phát minh trong Thế chiến II bởi các kỹ sư radar của quân đội Anh nhằm phân biệt tín hiệu máy bay ném bom Đức với nhiễu sóng của các đàn chim biển.
- *Hệ trục tọa độ:*
  - **Trục tung (Trục Y):** $\text{TPR (True Positive Rate)} = \text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$.
  - **Trục hoành (Trục X):** $\text{FPR (False Positive Rate)} = \frac{\text{FP}}{\text{FP} + \text{TN}} = 1 - \text{Specificity}$.
- *Cách hình thành đường cong:* Ta dịch chuyển ngưỡng $\theta$ liên tục từ $1.0 \to 0.0$:
  - Tại $\theta = 1.0$: Mô hình đoán tất cả là Âm tính $\implies \text{TPR}=0, \text{FPR}=0$ (Điểm gốc $(0,0)$).
  - Khi $\theta$ giảm dần: Mô hình đoán nhiều mẫu thành Dương tính hơn $\implies$ Cả TPR và FPR cùng tăng dần.
  - Tại $\theta = 0.0$: Mô hình đoán tất cả là Dương tính $\implies \text{TPR}=1, \text{FPR}=1$ (Điểm góc trên phải $(1,1)$).
- *Điểm lý tưởng (Perfect Classifier):* Tọa độ $(0, 1)$ — Tức $\text{FPR} = 0$ (Không báo động nhầm nào) và $\text{TPR} = 1$ (Bắt trúng 100% mục tiêu). Đường cong càng uốn cong áp sát góc trên bên trái $(0, 1)$ thì mô hình càng hoàn hảo!
- *Đường chéo ngẫu nhiên (Random Guess):* Nối từ $(0,0)$ đến $(1,1)$ tương ứng với mô hình tung đồng xu ngẫu nhiên ($\text{AUC} = 0.5$).

**3. Ý nghĩa xác suất sâu sắc của chỉ số ROC-AUC:**
AUC (Area Under the Curve) là diện tích nằm dưới đường cong ROC, nhận giá trị trong đoạn $[0.5, 1.0]$:
- $\text{AUC} = 0.5$: Đoán mò ngẫu nhiên.
- $\text{AUC} = 1.0$: Phân tách tuyệt đối hoàn hảo.
- **Định lý xác suất cốt lõi:**
  $$\text{AUC} = P\big(\hat{p}(X_{\text{positive}}) > \hat{p}(X_{\text{negative}})\big)$$
  *Nghĩa là:* Nếu bạn bốc ngẫu nhiên một mẫu Dương tính thật và một mẫu Âm tính thật, AUC chính là xác suất mà mô hình gán điểm tin cậy cho mẫu Dương tính CAO HƠN mẫu Âm tính!

**4. Đường cong PR (Precision-Recall Curve) & Điểm cốt tử trong đề thi Olympic:**
- Trục tung là Precision, Trục hoành là Recall.
- **Tại sao ROC-AUC có thể 'lừa dối' bạn khi dữ liệu mất cân bằng nặng?**
  Hãy nhìn vào mẫu số của FPR:
  $$\text{FPR} = \frac{\text{FP}}{\text{FP} + \text{TN}}$$
  Trong bài toán phát hiện gian lận thẻ tín dụng, số giao dịch hợp lệ $\text{TN}$ là hàng triệu mẫu!
  Nếu mô hình báo động nhầm $\text{FP} = 1,000$ lần:
  $$\text{FPR} = \frac{1,000}{1,000 + 1,000,000} \approx 0.001 \quad (0.1\%)$$
  FPR vẫn cực kỳ bé ($\approx 0$), khiến đường ROC vẫn nằm sát trục tung và cho ra **ROC-AUC cao ngất ngưởng đạt 0.98 hoặc 0.99**!
  Nhưng trên thực tế, nếu số ca gian lận thật chỉ có 100 ca ($\text{TP} \approx 90$), thì:
  $$\text{Precision} = \frac{90}{90 + 1,000} \approx 8.2\%!$$
  Người dùng phải chịu đựng 1,000 cuộc gọi làm phiền chỉ để bắt được 90 vụ trộm!
- **Quy tắc vàng phân định:**
  - Khi hai lớp cân bằng $\implies$ Dùng **ROC-AUC**.
  - Khi lớp Dương tính cực kỳ hiếm hoi và việc báo động giả gây hậu quả nghiêm trọng $\implies$ **BẮT BUỘC DÙNG ĐƯỜNG CONG PR (PR-AUC / Average Precision)** vì PR không chứa $\text{TN}$ khổng lồ trong mẫu số!""",
                "formula": r"\text{TPR} = \frac{\text{TP}}{\text{TP}+\text{FN}}, \quad \text{FPR} = \frac{\text{FP}}{\text{FP}+\text{TN}}, \quad \text{ROC-AUC} = \int_0^1 \text{TPR}(\text{FPR}) \, d\text{FPR}",
                "mathExplainer": [
                    { "sym": "\\text{TPR} (Recall)", "name": "True Positive Rate", "mean": "Tỷ lệ dương tính thật (Trục tung của đường cong ROC)." },
                    { "sym": "\\text{FPR}", "name": "False Positive Rate", "mean": "FP / (FP + TN): Tỷ lệ báo động giả trên toàn bộ mẫu âm tính (Trục hoành đường cong ROC)." },
                    { "sym": "\\text{ROC-AUC}", "name": "Area Under ROC Curve", "mean": "Diện tích dưới đường cong ROC (0.5 = đoán mò, 1.0 = hoàn hảo tuyệt đối)." },
                    { "sym": "\\text{PR-AUC}", "name": "Area Under PR Curve", "mean": "Diện tích dưới đường Precision-Recall, bắt buộc dùng khi dữ liệu mất cân bằng nặng." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 190" width="100%" height="190" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="190" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 20)">
                        <!-- ROC Chart -->
                        <g transform="translate(20, 10)">
                          <text x="90" y="0" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Đường Cong ROC (Cân Bằng)</text>
                          <line x1="20" y1="130" x2="160" y2="130" stroke="#111" stroke-width="1.5"/>
                          <line x1="20" y1="10" x2="20" y2="130" stroke="#111" stroke-width="1.5"/>
                          <!-- diagonal -->
                          <line x1="20" y1="130" x2="160" y2="10" stroke="#888" stroke-dasharray="3,3"/>
                          <!-- curve -->
                          <path d="M 20 130 Q 25 10 160 10" fill="none" stroke="#111" stroke-width="2.5"/>
                          <text x="90" y="145" font-family="Georgia" font-size="9" text-anchor="middle">FPR (0 → 1)</text>
                          <text x="10" y="75" font-family="Georgia" font-size="9" transform="rotate(-90 10 75)" text-anchor="middle">TPR (0 → 1)</text>
                          <text x="65" y="40" font-family="Georgia" font-size="10" font-weight="bold">AUC = 0.96</text>
                        </g>

                        <!-- Divider -->
                        <line x1="260" y1="10" x2="260" y2="150" stroke="#ccc" stroke-dasharray="2,2"/>

                        <!-- PR Chart -->
                        <g transform="translate(320, 10)">
                          <text x="90" y="0" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Đường Cong PR (Mất Cân Bằng)</text>
                          <line x1="20" y1="130" x2="160" y2="130" stroke="#111" stroke-width="1.5"/>
                          <line x1="20" y1="10" x2="20" y2="130" stroke="#111" stroke-width="1.5"/>
                          <!-- baseline horizontal line for PR -->
                          <line x1="20" y1="120" x2="160" y2="120" stroke="#888" stroke-dasharray="3,3"/>
                          <!-- PR curve -->
                          <path d="M 20 20 Q 90 25 160 120" fill="none" stroke="#111" stroke-width="2.5"/>
                          <text x="90" y="145" font-family="Georgia" font-size="9" text-anchor="middle">Recall (0 → 1)</text>
                          <text x="10" y="75" font-family="Georgia" font-size="9" transform="rotate(-90 10 75)" text-anchor="middle">Precision (0 → 1)</text>
                          <text x="50" y="70" font-family="Georgia" font-size="10" font-weight="bold">PR-AUC = 0.72</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "So sánh ROC Curve (phản ánh toàn cục) và Precision-Recall Curve (phơi bày sự thật khi dữ liệu mất cân bằng nghiêm trọng)."
                },
                "commonPitfalls": "Đường chéo ngẫu nhiên của đường cong PR không phải lúc nào cũng là 0.5: Trong đường cong ROC, đường cơ sở ngẫu nhiên luôn cố định là đường chéo có AUC = 0.5. Nhưng trong đường cong PR, đường cơ sở ngẫu nhiên là một đường thẳng nằm ngang bằng đúng tỷ lệ mẫu dương tính P / (P + N) (ví dụ nếu dữ liệu chỉ có 1% mẫu hiếm thì đường cơ sở của PR là 0.01!).",
                "practiceQuestion": {
                    "level": "Nâng cao",
                    "question": "Trong một bài toán phát hiện giao dịch rửa tiền với 999,900 giao dịch sạch và 100 giao dịch rửa tiền, mô hình A đạt ROC-AUC = 0.98 nhưng khi kiểm tra thực tế thì Precision chỉ đạt 5%. Nguyên nhân cốt lõi của hiện tượng này là gì?",
                    "options": [
                        "A. Do tính toán sai công thức ROC-AUC",
                        "B. Do số lượng TN quá khổng lồ làm cho FPR bị đè xuống cực nhỏ, thổi phồng điểm ROC-AUC",
                        "C. Do Precision luôn tỷ lệ nghịch với ROC-AUC",
                        "D. Do tập kiểm thử quá nhỏ không đủ đại diện"
                    ],
                    "correctIndex": 1,
                    "hint": "Nhìn vào công thức FPR = FP / (FP + TN). Khi TN = 999,900, mẫu số cực lớn khiến FPR luôn gần bằng 0 dù FP có lên tới hàng trăm.",
                    "solution": [
                        "Bước 1: Phân tích công thức FPR: FPR = FP / (FP + TN).",
                        "Bước 2: Vì TN = 999,900 rất lớn, ngay cả khi FP = 1,900 (báo động giả rất nhiều), FPR vẫn chỉ là 1,900 / 1,001,800 ≈ 0.0019 (0.19%).",
                        "Bước 3: Vì FPR rất nhỏ nên đồ thị ROC vẫn ép sát trục tung, tạo ra diện tích ROC-AUC cao chót vót (0.98).",
                        "Bước 4: Nhưng với Precision = TP / (TP + FP) = 90 / (90 + 1900) ≈ 4.5% (quá thấp).",
                        "Kết luận: TN quá lớn đã che giấu sự yếu kém của mô hình trên đường cong ROC. Bài toán này bắt buộc phải dùng PR-AUC.",
                        "Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 6.5: CÁC CHIẾN THUẬT XỬ LÝ DỮ LIỆU MẤT CÂN BẰNG
            # =================================================================
            {
                "heading": "6.5. Các Chiến Thuật Xử Lý Dữ Liệu Mất Cân Bằng: SMOTE, Resampling, Class Weights & Threshold Tuning",
                "content": "Để chế ngự dữ liệu mất cân bằng trong thực tế công nghiệp, kỹ sư Machine Learning sử dụng một hệ thống chiến thuật 3 cấp độ: Cấp độ dữ liệu (Resampling/SMOTE), Cấp độ thuật toán (Cost-Sensitive/Class Weights) và Cấp độ hậu xử lý (Threshold Tuning).",
                "deepDive": r"""**1. Cấp độ 1: Can thiệp dữ liệu (Data-level Resampling):**
Mục tiêu là đưa tỷ lệ giữa hai lớp về mức cân bằng nhân tạo trước khi cho mô hình học:

- **Random Undersampling (Giảm mẫu ngẫu nhiên lớp đa số):**
  - *Cách làm:* Bỏ bớt ngẫu nhiên các mẫu của lớp đa số cho đến khi số lượng hai lớp tương đương.
  - *Ưu điểm:* Giảm dung lượng tập dữ liệu, mô hình học cực nhanh.
  - *Nhược điểm chí mạng:* **Mất mát thông tin (Information Loss)**! Bạn có thể vô tình xóa bỏ những ranh giới phân loại quan trọng của lớp đa số.

- **Random Oversampling (Nhân bản ngẫu nhiên lớp thiểu số):**
  - *Cách làm:* Sao chép (copy-paste) lặp lại các mẫu hiếm có sẵn.
  - *Ưu điểm:* Giữ lại toàn bộ thông tin.
  - *Nhược điểm chí mạng:* **Gây ra Quá khớp (Overfitting)**! Mô hình sẽ học thuộc lòng chính xác từng điểm dữ liệu bị nhân bản thay vì học quy luật tổng quát.

- **Kỹ thuật đột phá SMOTE (Synthetic Minority Over-sampling Technique):**
  - Đề xuất bởi Chawla et al. (2002). Thay vì sao chép thô thiển điểm cũ, SMOTE **tạo ra các điểm dữ liệu nhân tạo mới** bằng cách nội suy hình học!
  - *Thuật toán 4 bước của SMOTE:*
    1. Với mỗi điểm dữ liệu lớp thiểu số $x_i$, tìm $k$ điểm láng giềng gần nhất (k-Nearest Neighbors) cũng thuộc lớp thiểu số.
    2. Chọn ngẫu nhiên một láng giềng $x_{(k)}$.
    3. Vẽ một đoạn thẳng nối giữa $x_i$ và $x_{(k)}$.
    4. Sinh ra một mẫu nhân tạo mới $x_{\text{new}}$ nằm ngẫu nhiên trên đoạn thẳng đó:
       $$x_{\text{new}} = x_i + \lambda \cdot (x_{(k)} - x_i), \quad \text{với } \lambda \sim U(0, 1)$$
  - *Nguyên tắc vàng:* **CHỈ ĐƯỢC CHẠY SMOTE TRÊN TẬP HUẤN LUYỆN (TRAIN SET)!** Tuyệt đối không bao giờ chạy SMOTE trước khi chia tập Train/Test (sẽ gây ra rò rỉ dữ liệu - Data Leakage nghiêm trọng).

**2. Cấp độ 2: Can thiệp thuật toán (Algorithm-level: Cost-Sensitive Learning & Class Weights):**
Không cần sửa đổi dữ liệu gốc, ta thay đổi **Hàm mất mát (Loss Function)** để phạt nặng hơn khi đoán sai lớp hiếm:

- **Hàm Binary Cross-Entropy có trọng số (Weighted BCE):**
  $$\mathcal{L} = - \left[ w_1 \cdot y \log(\hat{p}) + w_0 \cdot (1-y) \log(1-\hat{p}) \right]$$
- **Công thức tính trọng số tự động chuẩn Scikit-learn (Balanced Class Weights):**
  $$w_c = \frac{N}{K \cdot N_c}$$
  - $N$: Tổng số mẫu dữ liệu.
  - $K$: Số lượng lớp ($K = 2$).
  - $N_c$: Số mẫu của lớp $c$.
  *Ví dụ:* Tập gồm 900 mẫu âm tính ($N_0 = 900$) và 100 mẫu dương tính ($N_1 = 100$), tổng $N = 1000$:
  $$w_0 = \frac{1000}{2 \times 900} \approx 0.556, \quad w_1 = \frac{1000}{2 \times 100} = 5.0$$
  Lỗi đoán sai một mẫu dương tính bị phạt nặng gấp 9 lần lỗi đoán sai mẫu âm tính! Mô hình bị ép phải chú ý đặc biệt đến lớp thiểu số.

- **Focal Loss (Lin et al., 2017):**
  $$\text{FL}(p_t) = -\alpha_t (1 - p_t)^\gamma \log(p_t)$$
  Thêm hệ số điều biến $(1 - p_t)^\gamma$ nhằm triệt tiêu gradient của các mẫu 'quá dễ' (Easy examples) và dồn toàn bộ sức mạnh tối ưu vào các mẫu 'khó' (Hard examples).

**3. Cấp độ 3: Hậu xử lý dịch chuyển ngưỡng (Threshold Tuning / Moving):**
Nếu mô hình đã được huấn luyện xong và ta không muốn train lại:
Thay vì dùng ngưỡng mặc định $\theta = 0.5$, ta hạ ngưỡng xuống $\theta = 0.1$ hoặc $\theta = 0.2$ để tối đa hóa Recall cho các bài toán y tế hoặc cứu nạn.""",
                "formula": r"x_{\text{new}} = x_i + \lambda (x_{(k)} - x_i), \quad w_c = \frac{N}{K \cdot N_c}, \quad \text{FL}(p_t) = -\alpha_t (1 - p_t)^\gamma \log(p_t)",
                "mathExplainer": [
                    { "sym": "x_{\\text{new}}", "name": "Mẫu nhân tạo SMOTE", "mean": "Điểm dữ liệu mới được sinh ra bằng phép nội suy tuyến tính giữa 2 mẫu thiểu số láng giềng." },
                    { "sym": "\\lambda (Lambda)", "name": "Hệ số ngẫu nhiên", "mean": "Số thực ngẫu nhiên trong khoảng [0, 1] quyết định vị trí điểm mới trên đoạn thẳng nối." },
                    { "sym": "w_c", "name": "Trọng số cân bằng lớp", "mean": "Hệ số phạt trong hàm mất mát tỷ lệ nghịch với số lượng mẫu của lớp c." },
                    { "sym": "\\gamma (Gamma)", "name": "Hệ số tập trung Focal Loss", "mean": "Hệ số làm giảm đóng góp của các mẫu dễ phân loại (thường chọn gamma = 2.0)." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 20)">
                        <text x="280" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">Trực Quan Thuật Toán SMOTE: Nội Suy Điểm Nhân Tạo Giữa Các Láng Giềng</text>

                        <!-- Minority point 1 -->
                        <circle cx="100" cy="90" r="8" fill="#111"/>
                        <text x="100" y="70" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">x_i (Gốc)</text>

                        <!-- Line segment -->
                        <line x1="100" y1="90" x2="280" y2="60" stroke="#111" stroke-width="2" stroke-dasharray="4,4"/>

                        <!-- Synthetic point -->
                        <circle cx="190" cy="75" r="7" fill="#fff" stroke="#111" stroke-width="2.5"/>
                        <text x="190" y="55" font-family="Georgia" font-size="10" font-weight="bold" text-anchor="middle">x_new (SMOTE)</text>

                        <!-- Minority point 2 (neighbor) -->
                        <circle cx="280" cy="60" r="8" fill="#111"/>
                        <text x="280" y="40" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">x_(k) (Láng giềng)</text>

                        <!-- Majority points around -->
                        <circle cx="220" cy="130" r="6" fill="#ccc" stroke="#111"/>
                        <circle cx="340" cy="110" r="6" fill="#ccc" stroke="#111"/>
                        <circle cx="80" cy="140" r="6" fill="#ccc" stroke="#111"/>
                        <circle cx="300" cy="140" r="6" fill="#ccc" stroke="#111"/>
                        <text x="270" y="155" font-family="Georgia" font-size="9" fill="#666">Các mẫu lớp đa số</text>

                        <!-- Formula label -->
                        <text x="440" y="85" font-family="Georgia" font-size="11" font-weight="bold">x_new = x_i + λ(x_(k) - x_i)</text>
                        <text x="440" y="105" font-family="Georgia" font-size="10" fill="#444">λ ~ U(0, 1) chọn ngẫu nhiên</text>
                      </g>
                    </svg>""",
                    "caption": "Cơ chế sinh mẫu nhân tạo SMOTE: Nội suy hình học giữa 2 điểm thiểu số láng giềng để mở rộng vùng quyết định mà không bị Overfitting."
                },
                "commonPitfalls": "Lỗi Rò Rỉ Dữ Liệu (Data Leakage) khi dùng SMOTE: Đây là lỗi phổ biến nhất của sinh viên và kỹ sư mới ra trường. Áp dụng SMOTE lên toàn bộ tập dữ liệu TRƯỚC KHI chia Train/Test! Hậu quả: Tập Test sẽ chứa các mẫu nhân tạo được sinh ra từ tập Train, dẫn tới điểm kiểm thử cao ảo tưởng nhưng mô hình thất bại thảm hại khi triển khai thực tế!",
                "practiceQuestion": {
                    "level": "Trung bình",
                    "question": "Cho một tập dữ liệu nhị phân gồm tổng cộng N = 2,000 mẫu, trong đó có 1,800 mẫu thuộc lớp 0 (Bình thường) và 200 mẫu thuộc lớp 1 (Gian lận). Khi sử dụng công thức cân bằng trọng số chuẩn của Scikit-learn (w_c = N / (K * N_c)), trọng số phạt w_1 dành cho lớp gian lận bằng bao nhiêu?",
                    "options": [
                        "A. w_1 = 1.0",
                        "B. w_1 = 5.0",
                        "C. w_1 = 0.556",
                        "D. w_1 = 10.0"
                    ],
                    "correctIndex": 1,
                    "hint": "Thay số: N = 2000, K = 2 (nhị phân), N_1 = 200. Tính w_1 = 2000 / (2 * 200).",
                    "solution": [
                        "Bước 1: Xác định các tham số:",
                        "  Tổng số mẫu N = 2,000.",
                        "  Số lớp K = 2.",
                        "  Số mẫu lớp 1 là N_1 = 200.",
                        "Bước 2: Áp dụng công thức trọng số Scikit-learn:",
                        "  w_1 = N / (K * N_1) = 2000 / (2 * 200) = 2000 / 400 = 5.0.",
                        "Bước 3: Tương tự, w_0 = 2000 / (2 * 1800) = 2000 / 3600 ≈ 0.556.",
                        "Ý nghĩa: Đoán sai một mẫu lớp 1 sẽ bị phạt nặng gấp 5.0 / 0.556 = 9 lần so với đoán sai lớp 0.",
                        "Đáp án chính xác: B."
                    ]
                }
            },

            # =================================================================
            # MỤC 6.6: BÀI TOÁN TÍNH TAY CHUẨN ĐỀ THI VAIO (CÂU 1 IAIO 2024 / VAIO 2025)
            # =================================================================
            {
                "heading": "6.6. Bài Toán Tính Tay Chuẩn Đề Thi VAIO: Phân Tích Toàn Diện Mô Hình Chẩn Đoán Y Tế & Gian Lận Thẻ",
                "content": "Để sẵn sàng 100% cho kỳ thi Olympic AI, ta cùng giải quyết một bài toán tính tay toàn diện mô phỏng Câu 1 đề thi IAIO 2024 / VAIO 2025: Lập ma trận nhầm lẫn, tính toán Accuracy, Precision, Recall, F1, F2 và giải mã sự thất bại của mô hình ngây thơ.",
                "deepDive": r"""**1. Đề bài chuẩn Olympic AI:**
Một bệnh viện đa khoa ứng dụng hệ thống chẩn đoán AI để phát hiện sớm bệnh ung thư phổi cho $10,000$ bệnh nhân tham gia tầm soát định kỳ.
Theo thống kê dịch tễ, tỷ lệ mắc bệnh ung thư phổi trong nhóm đối tượng này là $2\%$ (nghĩa là có đúng $200$ ca thực sự mang mầm bệnh và $9,800$ người hoàn toàn khỏe mạnh).

Hội đồng chuyên môn độc lập đánh giá mô hình AI trên $10,000$ bệnh nhân này và ghi nhận kết quả:
- Trong số $200$ người thực sự mắc bệnh, mô hình AI chẩn đoán chính xác được $180$ người.
- Trong số $9,800$ người hoàn toàn khỏe mạnh, mô hình AI đã chẩn đoán nhầm $200$ người là 'Có bệnh' (báo động giả).
- Các trường hợp còn lại được mô hình kết luận tương ứng.

**YÊU CẦU THÍ SINH:**
1. Lập bảng Ma Trận Nhầm Lẫn (Confusion Matrix 2×2) hoàn chỉnh với đầy đủ các giá trị $\text{TP}, \text{TN}, \text{FP}, \text{FN}$.
2. Tính Độ chính xác toàn thể ($\text{Accuracy}$).
3. Tính Độ chuẩn xác ($\text{Precision}$) và Độ nhạy ($\text{Recall}$). Giải thích ý nghĩa của 2 con số này cho Giám đốc bệnh viện.
4. Tính Điểm cân bằng điều hòa $F_1\text{-Score}$.
5. Ban giám đốc yêu cầu: *"Chi phí bỏ sót 1 ca bệnh (FN) nguy hiểm gấp 2 lần sự phiền toái khi báo động nhầm (FP)"*. Hãy tính chỉ số $F_2\text{-Score}$ ($\beta = 2$) để làm căn cứ nghiệm thu.
6. So sánh mô hình AI này với một 'Mô hình ngây thơ (Naive Baseline)' luôn phán tất cả mọi người đều khỏe mạnh. Mô hình nào có Accuracy cao hơn? Mô hình nào thực sự có giá trị cứu người?

---

**2. Lời giải chi tiết từng bước (Step-by-Step Derivation):**

**Bước 1: Xác định 4 ô của Confusion Matrix:**
- Tổng số ca có bệnh thực tế: $P = \text{TP} + \text{FN} = 200$.
  - Mô hình chẩn đoán đúng: $\text{TP} = 180$.
  - Mô hình bỏ sót (âm tính giả): $\text{FN} = 200 - 180 = 20$.
- Tổng số người khỏe mạnh thực tế: $N_{\text{neg}} = \text{TN} + \text{FP} = 9,800$.
  - Mô hình báo động nhầm (dương tính giả): $\text{FP} = 200$.
  - Mô hình chẩn đoán đúng là khỏe mạnh: $\text{TN} = 9,800 - 200 = 9,600$.
- Tổng số mẫu: $\text{Total} = 180 + 20 + 200 + 9600 = 10,000$ mẫu.

Bảng Ma Trận Nhầm Lẫn hoàn chỉnh:
$$\begin{bmatrix} \text{TP} = 180 & \text{FN} = 20 \\ \text{FP} = 200 & \text{TN} = 9600 \end{bmatrix}$$

**Bước 2: Tính Accuracy:**
$$\text{Accuracy} = \frac{\text{TP} + \text{TN}}{\text{Total}} = \frac{180 + 9600}{10,000} = \frac{9,780}{10,000} = 0.9780 = 97.80\%$$

**Bước 3: Tính Precision và Recall:**
- Độ chuẩn xác (Precision):
  $$\text{Precision} = \frac{\text{TP}}{\text{TP} + \text{FP}} = \frac{180}{180 + 200} = \frac{180}{380} \approx 0.4737 = 47.37\%$$
  *Giải thích ý nghĩa:* Trong số 380 người bị máy kết luận có bệnh, chỉ có $47.37\%$ là bệnh thật, hơn một nửa ($52.63\%$) là báo động giả!
- Độ nhạy (Recall):
  $$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}} = \frac{180}{180 + 20} = \frac{180}{200} = 0.9000 = 90.00\%$$
  *Giải thích ý nghĩa:* Mô hình đã bắt trúng $90\%$ tổng số bệnh nhân ung thư, chỉ để lọt $10\%$ ($20$ người).

**Bước 4: Tính Điểm Cân Bằng $F_1$-Score:**
$$F_1 = \frac{2 \cdot P \cdot R}{P + R} = \frac{2 \times 0.4737 \times 0.9000}{0.4737 + 0.9000} = \frac{0.85266}{1.3737} \approx 0.6207 \quad (62.07\%)$$

**Bước 5: Tính $F_2$-Score ($\beta = 2$):**
$$F_2 = (1 + 2^2) \frac{P \cdot R}{2^2 \cdot P + R} = 5 \times \frac{0.4737 \times 0.9000}{4 \times 0.4737 + 0.9000}$$
$$= 5 \times \frac{0.42633}{1.8948 + 0.9000} = \frac{2.13165}{2.7948} \approx 0.7627 \quad (76.27\%)$$
*Nhận xét:* Vì bài toán y tế ưu tiên Recall (đạt 90%), điểm $F_2$ đạt tới $76.27\%$, cao hơn hẳn điểm $F_1$ ($62.07\%$).

**Bước 6: So sánh với Mô hình Ngây Thơ (Naive Baseline):**
Xét mô hình ngây thơ luôn phán mọi người là 'Khỏe mạnh' ($\hat{y} = 0$):
- $\text{TP} = 0, \text{FN} = 200, \text{FP} = 0, \text{TN} = 9800$.
- $\text{Accuracy}_{\text{Naive}} = \frac{0 + 9800}{10,000} = 98.00\%$!
- $\text{Recall}_{\text{Naive}} = \frac{0}{200} = 0.00\%$! $\text{F1}_{\text{Naive}} = 0.00\%$!

**BẢNG SO SÁNH QUYẾT ĐỊNH:**
| Chỉ Số | Mô Hình Ngây Thơ (Lười) | Mô Hình AI Đang Xét | Ý Nghĩa Thực Tế |
|---|---|---|---|
| **Accuracy** | **98.00% (Cao hơn!)** | 97.80% | Accuracy bị bóp méo bởi 9,800 người lành! |
| **Recall** | **0.00%** | **90.00%** | AI cứu sống 180 người, mô hình lười giết cả 200 người! |
| **Precision** | Không xác định (0/0) | 47.37% | AI giúp khoanh vùng chính xác 380 người cần chụp CT. |
| **F1-Score** | 0.000 | 0.621 | AI vượt trội hoàn toàn về năng lực học máy. |

**KẾT LUẬN VÀNG:**
Nếu ban giám khảo chỉ căn cứ vào Accuracy, mô hình lười biếng sẽ chiến thắng (98% > 97.8%). Nhưng trên thực tế cứu người, mô hình AI là chiếc phao cứu sinh với Recall 90%! Đây là bài học sâu sắc nhất trong kỳ thi VAIO 2025.""",
                "formula": r"\text{TP}=180, \, \text{FN}=20, \, \text{FP}=200, \, \text{TN}=9600 \implies \text{Acc}=97.8\%, \, P=47.4\%, \, R=90.0\%, \, F_1=0.621, \, F_2=0.763",
                "mathExplainer": [
                    { "sym": "\\text{TP}=180", "name": "Bắt đúng ca bệnh", "mean": "180 bệnh nhân ung thư được phát hiện kịp thời và cứu sống." },
                    { "sym": "\\text{FN}=20", "name": "Bỏ sót ca bệnh", "mean": "20 bệnh nhân ung thư bị chẩn đoán nhầm là khỏe mạnh (Lỗi Loại 2 nguy hiểm)." },
                    { "sym": "\\text{FP}=200", "name": "Báo động nhầm", "mean": "200 người khỏe mạnh bị báo nhầm là có bệnh, cần đi làm sinh thiết lại (Lỗi Loại 1)." },
                    { "sym": "F_2 = 0.763", "name": "Điểm F2-score", "mean": "Thước đo dung hòa ưu tiên Recall gấp đôi Precision phù hợp tiêu chuẩn y khoa." }
                ],
                "diagram": {
                    "svg": """<svg viewBox="0 0 640 180" width="100%" height="180" xmlns="http://www.w3.org/2000/svg">
                      <rect width="640" height="180" fill="#fafafa" stroke="#111" stroke-width="1"/>
                      <g transform="translate(40, 20)">
                        <text x="280" y="15" font-family="Georgia" font-size="12" font-weight="bold" text-anchor="middle">SO SÁNH MÔ HÌNH AI VS MÔ HÌNH NGÂY THƠ TRONG Y TẾ (10,000 BỆNH NHÂN)</text>

                        <!-- Box 1: Naive Model -->
                        <g transform="translate(20, 35)">
                          <rect x="0" y="0" width="240" height="110" fill="#fff" stroke="#111" stroke-width="1.5"/>
                          <text x="120" y="22" font-family="Georgia" font-size="11" font-weight="bold" text-anchor="middle">Mô Hình Ngây Thơ (Luôn đoán Khỏe)</text>
                          <text x="20" y="48" font-family="Georgia" font-size="11">• Accuracy: 98.0% (Rất cao!)</text>
                          <text x="20" y="70" font-family="Georgia" font-size="11">• Recall: 0.0% (Bỏ sót 100%)</text>
                          <text x="20" y="95" font-family="Georgia" font-size="12" font-weight="bold" fill="#111">Bỏ sót cả 200 ca tử vong!</text>
                        </g>

                        <!-- Arrow vs -->
                        <text x="280" y="95" font-family="Georgia" font-size="14" font-weight="bold" text-anchor="middle">VS</text>

                        <!-- Box 2: AI Model -->
                        <g transform="translate(300, 35)">
                          <rect x="0" y="0" width="240" height="110" fill="#111"/>
                          <text x="120" y="22" font-family="Georgia" font-size="11" font-weight="bold" fill="#fff" text-anchor="middle">Mô Hình AI (Chẩn Đoán Thực Tế)</text>
                          <text x="20" y="48" font-family="Georgia" font-size="11" fill="#eee">• Accuracy: 97.8% (Thấp hơn một chút)</text>
                          <text x="20" y="70" font-family="Georgia" font-size="11" fill="#eee">• Recall: 90.0% (Rất xuất sắc!)</text>
                          <text x="20" y="95" font-family="Georgia" font-size="12" font-weight="bold" fill="#fff">Cứu sống 180 bệnh nhân!</text>
                        </g>
                      </g>
                    </svg>""",
                    "caption": "Mô hình ngây thơ có Accuracy cao hơn (98% vs 97.8%) nhưng bỏ mặc bệnh nhân tử vong; Mô hình AI thực sự cứu sống 180 người."
                },
                "commonPitfalls": "Sai lầm tính mẫu số Precision là 200: Rất nhiều thí sinh nhầm lẫn lấy Precision = 180 / 200 = 90%. Đây là lỗi SAI NGHIÊM TRỌNG! 200 là tổng số người bệnh thật (đây là mẫu số của Recall). Để tính Precision, mẫu số phải là TỔNG SỐ NGƯỜI MÁY BẢO CÓ BỆNH: TP + FP = 180 + 200 = 380!",
                "practiceQuestion": {
                    "level": "Nâng cao (Câu 1 Đề Thi IAIO 2024 / VAIO 2025)",
                    "question": "Cho bảng Confusion Matrix: TP = 90, FN = 10, FP = 30, TN = 870. Giá trị F1-Score của mô hình xấp xỉ bằng:",
                    "options": [
                        "A. 0.818",
                        "B. 0.750",
                        "C. 0.900",
                        "D. 0.960"
                    ],
                    "correctIndex": 0,
                    "hint": "Tính Precision = 90 / (90 + 30) = 90 / 120 = 0.75. Tính Recall = 90 / (90 + 10) = 90 / 100 = 0.90. F1 = 2 * P * R / (P + R).",
                    "solution": [
                        "Bước 1: Tính Precision = TP / (TP + FP) = 90 / (90 + 30) = 90 / 120 = 0.75 (75.0%).",
                        "Bước 2: Tính Recall = TP / (TP + FN) = 90 / (90 + 10) = 90 / 100 = 0.90 (90.0%).",
                        "Bước 3: Tính F1-score:",
                        "  F1 = 2 * (0.75 * 0.90) / (0.75 + 0.90) = 2 * 0.675 / 1.65 = 1.35 / 1.65 = 9 / 11 ≈ 0.8181 (81.8%).",
                        "Đáp án chính xác: A."
                    ]
                }
            }
        ],
        "interactiveWidget": "widget-confusion-matrix",
        "examConnection": {
            "questionTitle": "Điểm Trọng Tâm Về Metrics & Imbalanced Data Trong Đề Thi VAIO 2025",
            "items": [
                {
                    "code": "Accuracy Paradox & Câu 1 IAIO",
                    "problem": "Tại sao trong bài toán chẩn đoán bệnh hiếm hoặc gian lận thẻ tín dụng, chỉ số Accuracy cao không chứng minh được mô hình hoạt động tốt?",
                    "solution": [
                        "1. Hiện tượng: Lớp đa số chiếm tỷ lệ áp đảo (ví dụ 99%), mô hình chỉ cần dự đoán toàn bộ là lớp âm tính thì Accuracy đã đạt 99% một cách tầm thường.",
                        "2. Bản chất: Mô hình không bắt được bất kỳ ca bệnh hiếm nào (Recall = 0%), khiến toàn bộ người bệnh bị bỏ sót và tử vong.",
                        "3. Khắc phục: Bắt buộc chuyển sang dùng Precision, Recall, F1-Score, Balanced Accuracy hoặc PR-AUC."
                    ]
                },
                {
                    "code": "ROC-AUC vs PR-AUC & Câu 85 VAIO",
                    "problem": "Khi nào đường cong ROC-AUC gây ra ảo giác sai lệch và khi nào bắt buộc phải dùng PR-AUC?",
                    "solution": [
                        "1. Khi dữ liệu cực kỳ mất cân bằng (Severe Class Imbalance), số lượng TN khổng lồ trong mẫu số của FPR = FP / (FP + TN) khiến FPR luôn ở mức cực nhỏ gần 0.",
                        "2. Hệ quả: Đường cong ROC vẫn áp sát trục tung và ROC-AUC vẫn đạt 0.98 - 0.99 dù số lượng báo động giả FP nhiều gấp hàng chục lần TP.",
                        "3. Bắt buộc: Sử dụng đường cong PR (Precision-Recall) vì cả hai trục của PR đều chỉ tập trung vào lớp thiểu số và loại bỏ hoàn toàn đại lượng TN khỏi mẫu số."
                    ]
                },
                {
                    "code": "Lỗi Data Leakage với SMOTE & Câu 89 VAIO",
                    "problem": "Sai lầm nguy hiểm nhất khi áp dụng thuật toán cân bằng dữ liệu SMOTE trong quy trình Machine Learning là gì?",
                    "solution": [
                        "1. Áp dụng SMOTE trên toàn bộ tập dữ liệu TRƯỚC KHI chia Train/Validation/Test.",
                        "2. Hậu quả: Dữ liệu nhân tạo được sinh ra từ các cặp điểm láng giềng sẽ bị rò rỉ vào tập Test, khiến điểm số kiểm thử cao ảo tưởng nhưng mô hình thất bại khi triển khai thực tế.",
                        "3. Quy tắc bắt buộc: Luôn chia Train/Test trước; chỉ áp dụng SMOTE trên tập Train; giữ nguyên vẹn tập Test với phân phối thực tế tự nhiên."
                    ]
                }
            ]
        },
        "takeaways": [
            "Nghịch lý Accuracy (Accuracy Paradox): Khi dữ liệu mất cân bằng, mô hình tầm thường đoán toàn bộ lớp đa số vẫn đạt Accuracy cao giả tạo.",
            "Confusion Matrix gồm 4 ô: TP (Đúng dương), TN (Đúng âm), FP (Lỗi Loại 1 - Báo động giả), FN (Lỗi Loại 2 - Bỏ sót hiểm họa).",
            "Precision đo độ tin cậy của lời cảnh báo (nhìn theo Cột dự đoán); Recall đo khả năng không bỏ sót mục tiêu (nhìn theo Hàng thực tế).",
            "F1-Score là Trung bình điều hòa của Precision và Recall, phạt cực nặng khi có một thành phần bị sụp đổ.",
            "Khi dữ liệu mất cân bằng nặng, ROC-AUC bị thổi phồng bởi TN lớn => BẮT BUỘC dùng đường cong Precision-Recall (PR-AUC).",
            "3 Cấp độ xử lý mất cân bằng: Resampling (SMOTE nội suy hình học), Cost-Sensitive (Class Weights w_c = N / (K * N_c)), và Dịch chuyển ngưỡng (Threshold Tuning)."
        ]
    }
