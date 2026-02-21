def process_scores(students):
    """Return a dict mapping student name to average score (rounded to 2 decimals)."""
    averages = {}
    for name, scores in students.items():
        if scores:
            avg = sum(scores) / len(scores)
        else:
            avg = 0.0
        averages[name] = round(avg, 2)
    return averages


def classify_grades(averages):
    """Return dict mapping name to (average, grade).

    Grading thresholds are defined locally per instructions.
    """
    a_threshold = 90
    b_threshold = 75
    c_threshold = 60

    classified = {}
    for name, avg in averages.items():
        if avg >= a_threshold:
            grade = "A"
        elif avg >= b_threshold:
            grade = "B"
        elif avg >= c_threshold:
            grade = "C"
        else:
            grade = "F"
        classified[name] = (avg, grade)
    return classified


def generate_report(classified, passing_avg=70):
    """Print a formatted report and return number of students who passed.

    A student passes if their average >= `passing_avg`.
    """
    print("===== Student Grade Report =====")
    passed = 0
    for name, (avg, grade) in classified.items():
        status = "PASS" if avg >= passing_avg else "FAIL"
        if status == "PASS":
            passed += 1
        print(f"{name.ljust(10)} | Avg: {avg:.2f} | Grade: {grade} | Status: {status}")
    print("================================")
    total = len(classified)
    failed = total - passed
    print(f"Total Students : {total}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed}")
    return passed


if __name__ == "__main__":
    # Demo dataset matching the example in the prompt
    students = {
        "Alice": [90, 85, 83, 87],
        "Bob": [60, 65],
        "Clara": [100, 95, 96, 94],
    }

    averages = process_scores(students)
    classified = classify_grades(averages)
    generate_report(classified)
