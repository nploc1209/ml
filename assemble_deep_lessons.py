# -*- coding: utf-8 -*-
"""
assemble_deep_lessons.py - Assembles all 13 textbook-grade deep lessons into lessons.js
Validates schema rigorously to ensure zero undefined/missing fields.
"""

import json
import build_deep_lessons_1_to_4 as p1
import build_deep_lessons_5_to_8 as p2
import build_deep_lessons_9_to_13 as p3

def assemble():
    print("Loading deep lessons 1-4...")
    l1 = p1.get_deep_lessons_1_to_4()
    print(f"Loaded {len(l1)} lessons from part 1.")

    print("Loading deep lessons 5-8...")
    l2 = p2.get_deep_lessons_5_to_8()
    print(f"Loaded {len(l2)} lessons from part 2.")

    print("Loading deep lessons 9-13...")
    l3 = p3.get_deep_lessons_9_to_13()
    print(f"Loaded {len(l3)} lessons from part 3.")

    all_lessons = l1 + l2 + l3
    print(f"Total master lessons: {len(all_lessons)}")

    # Validation pass
    total_sections = 0
    total_diagrams = 0
    total_explainers = 0
    total_questions = 0
    total_pitfalls = 0

    for idx, lesson in enumerate(all_lessons):
        lid = lesson.get("id")
        assert lid, f"Missing id in lesson {idx}"
        assert lesson.get("title"), f"Missing title in {lid}"
        assert lesson.get("summary"), f"Missing summary in {lid}"
        assert lesson.get("sections"), f"Missing sections in {lid}"

        # Check lesson diagram if present
        if "diagram" in lesson:
            ld = lesson["diagram"]
            assert isinstance(ld, dict) and "svg" in ld and "caption" in ld, f"Invalid lesson diagram in {lid}"

        for s_idx, sec in enumerate(lesson["sections"]):
            total_sections += 1
            assert sec.get("heading"), f"Missing heading in {lid} sec {s_idx}"
            assert sec.get("content"), f"Missing content in {lid} sec {s_idx}"
            assert sec.get("deepDive"), f"Missing deepDive in {lid} sec {s_idx}"

            if "diagram" in sec:
                diag = sec["diagram"]
                assert isinstance(diag, dict), f"Diagram is not a dict in {lid} sec {s_idx}"
                assert "svg" in diag and "caption" in diag, f"Diagram missing svg or caption in {lid} sec {s_idx}"
                total_diagrams += 1

            if "mathExplainer" in sec:
                me = sec["mathExplainer"]
                assert isinstance(me, list), f"mathExplainer not list in {lid} sec {s_idx}"
                for item in me:
                    assert "sym" in item and "name" in item and "mean" in item, f"Incomplete mathExplainer item in {lid} sec {s_idx}: {item}"
                total_explainers += 1

            if "commonPitfalls" in sec:
                cp = sec["commonPitfalls"]
                assert isinstance(cp, (str, list)), f"commonPitfalls invalid type in {lid} sec {s_idx}"
                total_pitfalls += 1

            if "practiceQuestion" in sec:
                pq = sec["practiceQuestion"]
                assert isinstance(pq, dict), f"practiceQuestion not dict in {lid} sec {s_idx}"
                for field in ["question", "options", "correctIndex", "hint", "solution"]:
                    assert field in pq, f"practiceQuestion missing {field} in {lid} sec {s_idx}"
                assert len(pq["options"]) >= 2, f"practiceQuestion options < 2 in {lid} sec {s_idx}"
                assert 0 <= pq["correctIndex"] < len(pq["options"]), f"Invalid correctIndex in {lid} sec {s_idx}"
                total_questions += 1

    print("\n--- Validation Statistics ---")
    print(f"Total Lessons: {len(all_lessons)}")
    print(f"Total Detailed Sections: {total_sections}")
    print(f"Total Vector SVG Diagrams: {total_diagrams}")
    print(f"Total Math Explainers: {total_explainers}")
    print(f"Total Exam Pitfall Boxes: {total_pitfalls}")
    print(f"Total Interactive Checkpoint Questions: {total_questions}")

    # Output to lessons.js
    json_str = json.dumps(all_lessons, ensure_ascii=False, indent=2)
    js_code = f"// lessons.js - 13 Master Textbook-Grade Lessons for VAIO 2025 AI Olympiad\nconst LESSONS_DATA = {json_str};\n"

    with open("lessons.js", "w", encoding="utf-8") as f:
        f.write(js_code)

    print(f"Successfully generated lessons.js ({len(js_code)} bytes / {len(js_code)//1024} KB).")

if __name__ == "__main__":
    assemble()
