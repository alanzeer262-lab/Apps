"""Reproducible demonstration dataset and reference output for the Track 2 capstone video.

This is a teaching/reference example, not the hidden PyLearn exercise solution.
Run with Python 3: python capstone_reference_demo.py
"""
import csv
import io

CSV_TEXT = """name,topic,score,attempt_count,completion_status
Ada,Python,88,1,complete
Lin,python,72,2,complete
Sam,Data,,1,in_progress
Mira,Python,95,1,complete
Lin,python,72,2,complete
Noor,Data,150,3,complete
Ivy,Data,oops,1,in_progress
"""

def build_report(csv_text):
    rows = list(csv.DictReader(io.StringIO(csv_text)))
    rows_read = len(rows)
    seen = set()
    valid = []
    rejected = []

    for row in rows:
        normalized = (
            row["name"].strip().casefold(),
            row["topic"].strip().casefold(),
            row["score"].strip(),
            row["attempt_count"].strip(),
            row["completion_status"].strip().casefold(),
        )
        if normalized in seen:
            rejected.append((row["name"], "duplicate row"))
            continue
        seen.add(normalized)

        raw_score = row["score"].strip()
        if not raw_score:
            rejected.append((row["name"], "blank score"))
            continue
        try:
            score = int(raw_score)
        except ValueError:
            rejected.append((row["name"], "score is not numeric"))
            continue
        if not 0 <= score <= 100:
            rejected.append((row["name"], "score out of range"))
            continue

        valid.append({
            "name": row["name"].strip(),
            "topic": row["topic"].strip().title(),
            "score": score,
            "attempt_count": int(row["attempt_count"]),
            "completion_status": row["completion_status"].strip().lower(),
        })

    scores = [row["score"] for row in valid]
    grade_distribution = {
        "A (90-100)": sum(90 <= score <= 100 for score in scores),
        "B (80-89)": sum(80 <= score < 90 for score in scores),
        "C (70-79)": sum(70 <= score < 80 for score in scores),
        "D (60-69)": sum(60 <= score < 70 for score in scores),
        "F (below 60)": sum(score < 60 for score in scores),
    }
    top_performer = max(valid, key=lambda row: row["score"])["name"] if valid else None

    return {
        "rows_read": rows_read,
        "valid_rows": len(valid),
        "invalid_rows": len(rejected),
        "cleaning_decisions": [
            "Removed exact duplicate rows",
            "Rejected blank and non-numeric scores",
            "Rejected scores outside 0-100",
            "Normalized topic capitalization",
        ],
        "average_score": sum(scores) / len(scores) if scores else None,
        "top_performer": top_performer,
        "grade_distribution": grade_distribution,
        "warning": "Average and grade distribution use only valid, deduplicated rows.",
    }

def main():
    report = build_report(CSV_TEXT)
    print(f"Rows read: {report['rows_read']}")
    print(f"Valid rows: {report['valid_rows']}")
    print(f"Invalid rows: {report['invalid_rows']}")
    print("Cleaning decisions:")
    for decision in report["cleaning_decisions"]:
        print(f"- {decision}")
    print(f"Average score: {report['average_score']}")
    print(f"Top performer: {report['top_performer']}")
    print("Grade distribution:")
    for grade, count in report["grade_distribution"].items():
        print(f"{grade}: {count}")
    print(f"Warning: {report['warning']}")

if __name__ == "__main__":
    main()
