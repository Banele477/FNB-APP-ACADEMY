# grade_report.py

# 1. Store 5 students as a list of dictionaries
class_students = [
    {"name": "Alice", "maths": 85, "english": 90, "science": 88},
    {"name": "Bob", "maths": 60, "english": 72, "science": 65},
    {"name": "Charlie", "maths": 92, "english": 88, "science": 95},
    {"name": "Diana", "maths": 45, "english": 55, "science": 50},
    {"name": "Ethan", "maths": 78, "english": 82, "science": 80}
]

# Initialize lists and statistics for tracking
results = []
class_total = 0
highest_mark = 0
lowest_mark = 100

# 2. Loop through all students and calculate averages, grades, and status
for student in class_students:
    total_marks = student["maths"] + student["english"] + student["science"]
    average = total_marks / 3
    
    # Grade and Status logic (Unit 5 threshold examples)
    if average >= 90:
        grade = "A"
        status = "Pass (Excellent)"
    elif average >= 75:
        grade = "B"
        status = "Pass (Good)"
    elif average >= 50:
        grade = "C"
        status = "Pass"
    else:
        grade = "F"
        status = "Fail"
        
    # Store result
    results.append({
        "name": student["name"],
        "average": round(average, 2),
        "grade": grade,
        "status": status
    })
    
    # Update class aggregates
    class_total += average
    if average > highest_mark:
        highest_mark = average
    if average < lowest_mark:
        lowest_mark = average

# Calculate class average
class_average = class_total / len(class_students)

# 3. Display formatted class report
print("="*45)
print("           CLASS SUMMARY REPORT           ")
print("="*45)
for res in results:
    print(f"Name: {res['name']}")
    print(f"  Average: {res['average']}%  |  Grade: {res['grade']}  |  Status: {res['status']}")
    print("-" * 45)

print("\nCLASS STATISTICS:")
print(f"Class Average: {round(class_average, 2)}%")
print(f"Highest Average: {round(highest_mark, 2)}%")
print(f"Lowest Average: {round(lowest_mark, 2)}%")
print("="*45)

# 4. Use a while loop to search for a student
search_active = True
while search_active:
    search_name = input("\nEnter student name to search (or type 'quit' to exit): ").strip().capitalize()
    
    if search_name.lower() == 'quit':
        print("Exiting search mode. Goodbye!")
        break
        
    # Search for the student in results
    found = False
    for res in results:
        if res["name"] == search_name:
            print(f"\n--- Result for {search_name} ---")
            print(f"Average: {res['average']}% | Grade: {res['grade']} | Status: {res['status']}")
            found = True
            break # Exit the inner loop early once student is found
            
    if not found:
        print(f"Student '{search_name}' not found. Please try again.")
