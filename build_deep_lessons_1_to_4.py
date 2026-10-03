# -*- coding: utf-8 -*-
"""
build_deep_lessons_1_to_4.py - Masterclass Lessons 1 to 4 for VAIO 2025 AI Olympiad.
Written with full pedagogical depth:
Trực giác -> Bản chất -> Cách hoạt động -> Công thức -> Giải mã ký hiệu ->
Ví dụ tính toán bằng số -> Cạm bẫy thường gặp -> Luyện tập trắc nghiệm.
"""

from upgrade_lesson_1 import get_masterpiece_lesson_1
from upgrade_lesson_2 import get_masterpiece_lesson_2
from upgrade_lesson_3 import get_masterpiece_lesson_3
from upgrade_lesson_4 import get_masterpiece_lesson_4

def get_deep_lessons_1_to_4():
    lessons = []

    # =========================================================================
    # BÀI HỌC 1: GIẢI TÍCH NỀN TẢNG & VECTOR GRADIENT CHO MACHINE LEARNING (MASTERPIECE)
    # =========================================================================
    lessons.append(get_masterpiece_lesson_1())

    # =========================================================================
    # BÀI HỌC 2: ĐẠI SỐ TUYẾN TÍNH, MA TRẬN & COSINE SIMILARITY (MASTERPIECE)
    # =========================================================================
    lessons.append(get_masterpiece_lesson_2())

    # =========================================================================
    # BÀI HỌC 3: XÁC SUẤT & BỘ PHÂN LOẠI NAIVE BAYES (MASTERPIECE)
    # =========================================================================
    lessons.append(get_masterpiece_lesson_3())

    # =========================================================================
    # BÀI HỌC 4: GRADIENT DESCENT & CÁC BỘ TỐI ƯU HÓA (MASTERPIECE)
    # =========================================================================
    lessons.append(get_masterpiece_lesson_4())

    return lessons

if __name__ == "__main__":
    lessons = get_deep_lessons_1_to_4()
    print(f"Deep lessons 1-4 generated successfully: {len(lessons)} lessons.")
