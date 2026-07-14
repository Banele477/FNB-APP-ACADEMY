first_name = input("Enter your first name: ").strip()
surname = input("Enter your surname: ").strip()
age = int(input("Enter your age (Enter your age as an integer): ").strip())

favourite_number =float(input("Enter your favourite number(Enter your favourite number as a float): ").strip())
full_name=(f"Welcome, {first_name.upper().title()} {surname.upper().title()}. You are {age} years old and your favourite number is {favourite_number}.")
print(f"Welcome,{full_name}!.upper().title()")

age_in_months = age * 12
print(f"You are {age_in_months} months old.")
round_favourite_number = round(favourite_number, 2)

print(f"Your favourite number rounded to 2 decimal places is {round_favourite_number}.")

print("\n --- Data types --- ")
print(f"First name: {first_name} (Type: {type(first_name)})")
print(f"Surname: {surname} (Type: {type(surname)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"Favourite number: {favourite_number} (Type: {type(favourite_number)})")
print(f"Full name: {full_name} (Type: {type(full_name)})")