import json
import os
import re

FILE_NAME = "student_contacts.json"

# Main storage
contacts = {}

# Sets for duplicate prevention
emails = set()
phones = set()

# Tuple (fixed immutable data)
VALID_ROLES = ("Student", "Parent", "Teacher")



# Load data from file

def load_contacts():
    global contacts, emails, phones

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                contacts = json.load(file)

                for cid, data in contacts.items():
                    emails.add(data["email"])
                    phones.add(data["phone"])

            except json.JSONDecodeError:
                contacts = {}



# Save data

def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)



# Validation

def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


def valid_phone(phone):
    return phone.isdigit() and len(phone) >= 10



# Add Contact

def add_contact():
    student_id = input("Student ID: ")

    if student_id in contacts:
        print("ID already exists.")
        return

    name = input("Full Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    role = input("Role (Student/Parent/Teacher): ").title()

    # validations
    if not valid_email(email):
        print("Invalid email format.")
        return

    if email in emails:
        print("Email already exists.")
        return

    if not valid_phone(phone):
        print("Invalid phone number.")
        return

    if phone in phones:
        print("Phone already exists.")
        return

    if role not in VALID_ROLES:
        print("Invalid role.")
        return

    # store
    contacts[student_id] = {
        "name": name,
        "email": email,
        "phone": phone,
        "role": role
    }

    emails.add(email)
    phones.add(phone)

    save_contacts()
    print("Contact added successfully.")



# Convert dict to list 

def get_contact_list():
    return list(contacts.items())



# List Contacts (uses list, sort, slicing, indexing)

def list_contacts():
    if not contacts:
        print("No contacts found.")
        return

    contact_list = get_contact_list()

    # sorting 
    contact_list.sort(key=lambda x: x[1]["name"])

    print("\n===== ALL CONTACTS =====")

    for i, (cid, data) in enumerate(contact_list):
        print(f"\nIndex: {i}")
        print(f"ID   : {cid}")
        print(f"Name : {data['name']}")
        print(f"Email: {data['email']}")
        print(f"Phone: {data['phone']}")
        print(f"Role : {data['role']}")

    # slicing 
    print("\n===== FIRST 2 CONTACTS =====")
    for cid, data in contact_list[:2]:
        print(f"{cid} - {data['name']}")



# Search (uses list + indexing)

def search_contact():
    keyword = input("Search by ID or Name: ").lower()

    contact_list = get_contact_list()

    results = []

    for cid, data in contact_list:
        if keyword in cid.lower() or keyword in data["name"].lower():
            results.append((cid, data))

    if not results:
        print("No match found.")
        return

    print("\n===== SEARCH RESULTS =====")

    # indexing demo
    first_result = results[0]
    print("\nFIRST MATCH:")
    print(first_result)



# Delete Contact 

def delete_contact():
    student_id = input("Enter ID to delete: ")

    if student_id not in contacts:
        print("Not found.")
        return

    data = contacts[student_id]

    emails.remove(data["email"])
    phones.remove(data["phone"])

    del contacts[student_id]

    save_contacts()
    print("Deleted successfully.")



# Update Contact

def update_contact():
    student_id = input("Enter ID to update: ")

    if student_id not in contacts:
        print("Not found.")
        return

    data = contacts[student_id]

    emails.remove(data["email"])
    phones.remove(data["phone"])

    name = input(f"Name ({data['name']}): ") or data["name"]
    email = input(f"Email ({data['email']}): ") or data["email"]
    phone = input(f"Phone ({data['phone']}): ") or data["phone"]
    role = input(f"Role ({data['role']}): ") or data["role"]

    if role not in VALID_ROLES:
        print("Invalid role.")
        return

    contacts[student_id] = {
        "name": name,
        "email": email,
        "phone": phone,
        "role": role
    }

    emails.add(email)
    phones.add(phone)

    save_contacts()
    print("Updated successfully.")



# MENU
def menu():
    load_contacts()

    while True:
        print("""
========================
 CONTACT MANAGER
========================
1. Add Contact
2. Update Contact
3. Delete Contact
4. Search Contact
5. List Contacts
6. Exit
========================
""")

        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            list_contacts()
        elif choice == "6":
            print("Goodbye ")
            break
        else:
            print("Invalid option.")


menu()
