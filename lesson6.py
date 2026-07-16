# Initialize the shopping cart
cart = ["Apples", "Eggs", "Milk"]

# Print the first item in the cart
print(f"First item: {cart[0]}")

# Add a new item and print the entire updated list
cart.append("Bread")
print(f"Updated cart: {cart}")

# Loop through and print each item on a new line
print("\nItems in your cart:")
for item in cart:
    print(f"- {item}")

# Working with dictionaries
student = {
    "name": "Thabo",
    "age": 25,
    "course": "Intro to Python"
}

# 1. Cleaner printing using f-strings
print(f"Student Name: {student['name']}")
print(f"Age: {student['age']}")

# 2. Repeating tasks: Looping through the dictionary keys and values
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")
