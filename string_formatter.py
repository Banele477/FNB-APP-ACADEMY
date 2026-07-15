first_name = input("Enter your first name: ").strip()
surname = input("Enter your surname: ").strip()
bio_message=input("Enter a short bio about yourself: ").strip()

username = f"{first_name[0]}{surname}".lower()
full_name = f"{first_name.title()} {surname.title()}"
print(f"Your username is: {username}")

print(f"Your full name is: {full_name}")
print(f"Your bio message is: {bio_message}".strip())
bio_message_length = len(bio_message)

print(f"Your bio message has {bio_message_length} characters.")
bio_message = bio_message.replace("I am ", "I'm ")
print(f"Your bio message is: {bio_message}")

print(f"Your full name is: {full_name}")
print(f"Your bio message is: {bio_message}".strip())
surname = input("Enter your surname: ").strip()
full_name = f"{first_name.title()} {surname.title()}"