from upgrade_lesson_5 import get_masterpiece_lesson_5
from upgrade_lesson_6 import get_masterpiece_lesson_6
from upgrade_lesson_7 import get_masterpiece_lesson_7
from upgrade_lesson_8 import get_masterpiece_lesson_8

# -*- coding: utf-8 -*-
"""
build_deep_lessons_5_to_8.py - Masterclass Lessons 5 to 8 for VAIO 2025 AI Olympiad.
Written with full pedagogical depth:
Trực giác -> Bản chất -> Cách hoạt động -> Công thức -> Giải mã ký hiệu ->
Ví dụ tính toán bằng số -> Cạm bẫy thường gặp -> Luyện tập trắc nghiệm.
"""

def get_deep_lessons_5_to_8():
    lessons = []

    # =========================================================================
    # BÀI HỌC 5: HỒI QUY TUYẾN TÍNH & REGULARIZATION (MASTERPIECE)
    # =========================================================================
    lessons.append(get_masterpiece_lesson_5())

    # =========================================================================
    # BÀI HỌC 6: METRIC ĐÁNH GIÁ & XỬ LÝ DỮ LIỆU MẤT CÂN BẰNG (MASTERPIECE)
    # =========================================================================
    lessons.append(get_masterpiece_lesson_6())

    # =========================================================================
    # BÀI HỌC 7: CÂY QUYẾT ĐỊNH & ENSEMBLE (RANDOM FOREST, XGBOOST) (MASTERPIECE)
    # =========================================================================
    lessons.append(get_masterpiece_lesson_7())

    # =========================================================================
    # BÀI HỌC 8: MÁY VECTOR HỖ TRỢ (SVM), KERNEL TRICK & k-NN (MASTERPIECE)
    # =========================================================================
    lessons.append(get_masterpiece_lesson_8())

    return lessons

if __name__ == "__main__":
    lessons = get_deep_lessons_5_to_8()
    print(f"Deep lessons 5-8 generated successfully: {len(lessons)} lessons.")
