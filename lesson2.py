#tracking individual letters
name = ("Python")

print(name[0])
print(name[-1])
print(name[2])

#Using string methods'
town="  Jonnesburg "

print(town.upper())
print(town.strip())

#Creating a professional system email generator

first = input("Enter your first name: ").strip()
last = input("Enter your last name: ").strip()

username = f"{first[0]}{last}"
print(f"Your email is: {username.lower()}@gmail.com")