
students = {
    "Aarav": [85, 78, 92, 88, 76],
    "Priya": [91, 95, 89, 93, 87],
    "Rahul": [65, 72, 68, 74, 70],
    "Neha": [78, 82, 80, 85, 79]
}

TOTAL_SUBJECTS = 5
MAX_MARKS_PER_SUBJECT = 100


def analyze_student(name, marks):
    total = sum(marks)
    average = total / len(marks)
    percentage = (total / (len(marks) * MAX_MARKS_PER_SUBJECT)) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "Needs Improvement"

    return {
        "name": name,
        "total": total,
        "average": average,
        "percentage": percentage,
        "grade": grade
    }


print("=" * 48)
print("        STUDENT MARKS ANALYZER")
print("=" * 48)

results = []

for name, marks in students.items():
    result = analyze_student(name, marks)
    results.append(result)

    print(f"\nStudent: {result['name']}")
    print(f"Total Marks: {result['total']}/{len(marks) * MAX_MARKS_PER_SUBJECT}")
    print(f"Average: {result['average']:.2f}")
    print(f"Percentage: {result['percentage']:.2f}%")
    print(f"Grade: {result['grade']}")

topper = max(results, key=lambda student: student["percentage"])
class_average = sum(r["percentage"] for r in results) / len(results)

print("\n" + "=" * 48)
print(f"Class Average: {class_average:.2f}%")
print(f"Top Performer: {topper['name']}")
print(f"Highest Percentage: {topper['percentage']:.2f}%")
print("=" * 48)
