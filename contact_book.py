# contact_book.py

# Global list to store contact dictionaries
contacts = []

def add_contact():
    """Appends a new contact dictionary to the list."""
    print("\n--- Add New Contact ---")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    # Create the contact dictionary
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email
    }
    
    # Append to the global list
    contacts.append(new_contact)
    print(f"Success: Contact for '{name}' has been added!")

def search_contact(name):
    """Searches by name and returns the matching dictionary (or None)."""
    for contact in contacts:
        # Case-insensitive comparison for better user experience
        if contact["name"].lower() == name.lower():
            return contact
    return None

def delete_contact(name):
    """Removes a contact by name."""
    contact = search_contact(name)
    if contact:
        contacts.remove(contact)
        print(f"Success: Contact for '{contact['name']}' has been deleted!")
    else:
        print(f"Error: Contact '{name}' not found.")

def view_all():
    """Displays all contacts in a formatted layout."""
    print("\n--- All Contacts ---")
    if not contacts:
        print("Your contact book is currently empty.")
        return
        
    # Print formatted headers
    print(f"{'Name':<20} | {'Phone':<15} | {'Email':<25}")
    print("-" * 66)
    
    # Iterate and print each contact row
    for contact in contacts:
        print(f"{contact['name']:<20} | {contact['phone']:<15} | {contact['email']:<25}")

def main():
    """Runs the main program loop and menu interface."""
    while True:
        print("\n===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")
        
        choice = input("Choose an action (1-5): ").strip()
        
        if choice == "1":
            add_contact()
            
        elif choice == "2":
            print("\n--- Search Contact ---")
            search_name = input("Enter the name to search for: ").strip()
            result = search_contact(search_name)
            if result:
                print("\nContact Found:")
                print(f"Name:  {result['name']}")
                print(f"Phone: {result['phone']}")
                print(f"Email: {result['email']}")
            else:
                print(f"No contact found matching '{search_name}'.")
                
        elif choice == "3":
            print("\n--- Delete Contact ---")
            delete_name = input("Enter the name to delete: ").strip()
            delete_contact(delete_name)
            
        elif choice == "4":
            view_all()
            
        elif choice == "5":
            print("\nThank you for using Contact Book. Goodbye!")
            break
            
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
