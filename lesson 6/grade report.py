# grade_report.py

# List of student dictionaries
students = [
    {"name": "Thabiso", "maths": 85, "english": 78, "science": 90},
    {"name": "Ayanda", "maths": 67, "english": 72, "science": 70},
    {"name": "Lerato", "maths": 58, "english": 64, "science": 61},
    {"name": "Sipho", "maths": 45, "english": 52, "science": 48},
    {"name": "Nomsa", "maths": 92, "english": 88, "science": 95}
]

results = []
all_averages = []

# Process each student
for student in students:
    average = (student["maths"] + student["english"] + student["science"]) / 3

    # Determine grade
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    # Determine pass or fail
    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    # Store the results
    results.append({
        "name": student["name"],
        "average": average,
        "grade": grade,
        "status": status
    })

    all_averages.append(average)

# Class statistics
class_average = sum(all_averages) / len(all_averages)
highest_mark = max(all_averages)
lowest_mark = min(all_averages)

# Display report
print("=" * 55)
print("               CLASS GRADE REPORT")
print("=" * 55)

print(f"{'Name':<12}{'Average':<10}{'Grade':<8}{'Status'}")
print("-" * 55)

for result in results:
    print(f"{result['name']:<12}{result['average']:.2f}%{'':<3}{result['grade']:<6}{result['status']}")

print("-" * 55)
print(f"Class Average : {class_average:.2f}%")
print(f"Highest Average: {highest_mark:.2f}%")
print(f"Lowest Average : {lowest_mark:.2f}%")
print("=" * 55)

# Search for a student
while True:
    search = input("\nEnter a student name to search (or 'exit' to quit): ").strip()

    if search.lower() == "exit":
        print("Program ended.")
        break

    found = False

    for result in results:
        if result["name"].lower() == search.lower():
            print("\nStudent Found")
            print(f"Name    : {result['name']}")
            print(f"Average : {result['average']:.2f}%")
            print(f"Grade   : {result['grade']}")
            print(f"Status  : {result['status']}")
            found = True
            break

    if not found:
        print("Student not found.")
