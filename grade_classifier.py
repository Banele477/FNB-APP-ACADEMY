# grade_classifier.py

def main():
    # 1. Collect learner name and marks for three subjects (as floats) using input()
    learner_name = input("Enter learner's name: ")
    
    try:
        mark1 = float(input("Enter mark for Subject 1: "))
        mark2 = float(input("Enter mark for Subject 2: "))
        mark3 = float(input("Enter mark for Subject 3: "))
    except ValueError:
        print("Invalid input. Please run the program again and enter numeric values for marks.")
        return

    # 2. Calculate the average mark across the three subjects
    average_mark = (mark1 + mark2 + mark3) / 3

    # 3. Assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else
    if average_mark >= 80:
        grade = 'A'
    elif average_mark >= 70:
        grade = 'B'
    elif average_mark >= 60:
        grade = 'C'
    elif average_mark >= 50:
        grade = 'D'
    else:
        grade = 'F'

    # 4. Assign Pass status if the average is 50 or above, Fail otherwise
    if average_mark >= 50:
        status = 'Pass'
    else:
        status = 'Fail'

    # 5. Flag any individual subject mark below 40 as 'needs intervention'
    interventions = []
    if mark1 < 40:
        interventions.append(f"Subject 1 ({mark1})")
    if mark2 < 40:
        interventions.append(f"Subject 2 ({mark2})")
    if mark3 < 40:
        interventions.append(f"Subject 3 ({mark3})")

    # 6. Display a formatted report card
    print("\n" + "=" * 30)
    print("       STUDENT REPORT CARD       ")
    print("=" * 30)
    print(f"Learner Name: {learner_name}")
    print("-" * 30)
    print(f"Subject 1 Mark:  {mark1:.2f}")
    print(f"Subject 2 Mark:  {mark2:.2f}")
    print(f"Subject 3 Mark:  {mark3:.2f}")
    print("-" * 30)
    print(f"Average Mark:    {average_mark:.2f}")
    print(f"Letter Grade:    {grade}")
    print(f"Status:          {status}")
    print("-" * 30)
    
    if interventions:
        print("Intervention Flags:")
        for flag in interventions:
            print(f" - {flag} needs intervention")
    else:
        print("Intervention Flags: None")
        
    print("=" * 30)

if __name__ == "__main__":
    main()
