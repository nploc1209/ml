from upgrade_lesson_13 import get_masterpiece_lesson_13
from upgrade_lesson_12 import get_masterpiece_lesson_12
from upgrade_lesson_11 import get_masterpiece_lesson_11
from upgrade_lesson_9 import get_masterpiece_lesson_9
from upgrade_lesson_10 import get_masterpiece_lesson_10
# -*- coding: utf-8 -*-
"""
build_deep_lessons_9_to_13.py - Masterclass Lessons 9 to 13 for VAIO 2025 AI Olympiad.
Written with full pedagogical depth:
Trực giác -> Bản chất -> Cách hoạt động -> Công thức -> Giải mã ký hiệu ->
Ví dụ tính toán bằng số -> Cạm bẫy thường gặp -> Luyện tập trắc nghiệm.
"""

def get_deep_lessons_9_to_13():
    lessons = []

    # =========================================================================
    # BÀI HỌC 9: PHÂN CỤM K-MEANS & GIẢM CHIỀU DỮ LIỆU PCA (MASTERPIECE)
    # =========================================================================
    lessons.append(get_masterpiece_lesson_9())
    # =========================================================================
    # BÀI HỌC 10: MẠNG NƠ-RON (MLP) & THUẬT TOÁN LAN TRUYỀN NGƯỢC (MASTERPIECE)
    # =========================================================================
    lessons.append(get_masterpiece_lesson_10())

    # =========================================================================
    # BÀI HỌC 11: THỊ GIÁC MÁY TÍNH: CNN, RESNET & NHẬN DIỆN VẬT THỂ (MASTERPIECE)
    # =========================================================================
    lessons.append(get_masterpiece_lesson_11())

    # =========================================================================
    # BÀI HỌC 12: XỬ LÝ NGÔN NGỮ TỰ NHIÊN (NLP), ATTENTION & LLMS (MASTERPIECE)
    # =========================================================================
    lessons.append(get_masterpiece_lesson_12())

    # =========================================================================
    # BÀI HỌC 13: HỌC TỰ GIÁM SÁT, GANS & MÔ HÌNH KHUẾCH TÁN (MASTERPIECE)
    # =========================================================================
    lessons.append(get_masterpiece_lesson_13())

    return lessons

if __name__ == "__main__":
    lessons = get_deep_lessons_9_to_13()
    print(f"Deep lessons 9-13 generated successfully: {len(lessons)} lessons.")
