# 1. Create the dictionary with 3 contacts (values kept as strings)
contacts = {
    "John": "0821112222",
    "Sarah": "0832223333",
    "David": "0843334444"
}

# 2. Ask the user to input the friend's name
search_name = input("Enter the name of the friend you want to look up: ")

# 3. Conditional check
if search_name in contacts:
    phone_number = contacts[search_name]
    print(f"Found! {search_name}'s number is {phone_number}")
    
# 4. Otherwise
else:
    print("Contact not found.")
