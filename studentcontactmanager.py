import json
import os
import re

file_name = 'student_contacts.json'

contacts = {}
emails = set()
phones = set()

# Load contacts from json file
def load_contacts():
    global contacts, emails, phones

    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            try:
                contacts = json.load(file)

                for contact in contacts.values():
                    emails.add(contact['email'])
                    phones.add(contact['phone'])

            except json.JSONDecodeError:
                contacts = {}

# Save contacts to json file
def save_contacts():
    with open(file_name, 'w') as file:
        json.dump(contacts, file, indent=4)

# Validate email
def valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

# Validate phone
def valid_phone(phone):
    return phone.isdigit() and len(phone) >= 10

# Add contact
def add_contact():
    student_id = input('Enter Student ID: ')

    if student_id in contacts:
        print('A contact with this ID already exists.')
        return
    
    name = input('Full Name: ')
    email = input('Email: ')

    if not valid_email(email):
        print('Invalid email format.')
        return
    
    if email in emails:
        print('This email already exists.')
        return
    
    phone = input('Phone Number: ')

    if not valid_phone(phone):
        print('Invalid phone number.')
        return
    
    role = input('Role (Student/Parent/Teacher): ').title()

    contacts[student_id]= {
        'name': name,
        'email': email,
        'phone': phone,
        'role': role
    }

    emails.add(email)
    phones.add(phone)

    save_contacts()

    print('Contact added successfully.')

# Update contact
def update_contact():
    student_id = input('Enter Student ID to update: ')

    if student_id not in contacts:
        print('Contact not found')
        return
    
    contact = contacts[student_id]

    emails.remove(contact['email'])
    phones.remove(contact['phone'])

    print('Press Enter to keep existing value.')

    name = input(f'Name ({contact["name"]}): ')
    if name == '':
        name = contact['name']

    email = input(f'Email ({contact["email"]}): ')
    if email == '':
        email = contact['email']

    if not valid_email(email):
        print('Invalid email.')
        emails.add(contact['email'])
        phones.add(contact['phone'])
        return
    
    if email in emails:
        print('Email already exists.')
        emails.add(contact['email'])
        phones.add(contact['phones'])
        return
    
    phone = input(f'Phone ({contact["phone"]}): ')
    if phone == '':
        phone = contact['phone']

    if not valid_phone(phone):
        print('Invalid phone number.')
        emails.add(contact['email'])
        phones.add(contact['phone'])
        return
    
    if phone in phones:
        print('Phone number already exists.')
        emails.add(contact['email'])
        phones.add(contact['phone'])
        return
    
    role = input(f'Role ({contact["role"]}): ')
    if role == '':
        role = contact['role']

    contacts[student_id] = {
        'name': name,
        'email': email,
        'phone': phone,
        'role': role
    }

    emails.add(email)
    phones.add(phone)

    save_contacts()

    print('Contact updated successfully.')

# Delete contact
def delete_contact():
    student_id = input('Enter Student ID to delete: ')

    if student_id not in contacts:
        print('Contact not found.')
        return
    
    emails.remove(contacts[student_id]['email'])
    phones.remove(contacts[student_id]['phone'])

    del contacts[student_id]

    save_contacts

    print('Contact deleted successfully.')

# Search contact
def search_contact():
    keyword = input('Enter Student ID or Name: ').lower()

    found = False

    for student_id, contact in contacts.items():
        if keyword == student_id.lower() or keyword in contact['name'].lower():

            print('\n--------------------------')
            print('Student ID:', student_id)
            print('Name      :', contact['name'])
            print('Email     :', contact['email'])
            print('Phone     :', contact['phone'])
            print('Role      :', contact['role'])
            print('----------------------------')

            found = True

    if not found:
        print('No matching contact found.')

# List contacts
def list_contacts():

    if not contacts:
        print('No contacts available.')
        return
    
        print('\n---------- CONTACT LIST ----------')

    for student_id, contact in contacts.items():

        print(f"""
        Student ID : {student_id}
        Name       : {contact['name']}
        Email      : {contact['email']}
        Phone      : {contact['phone']}
        Role       : {contact['role']}
        ----------------------------------
        """)
        
# Main menu

def menu():
    load_contacts()

    while True:
        print("""
        ----------------------------------
              Student Contact Manager
        ----------------------------------
        1. Add Contact
        2. Update Contact
        3. Delete Contact
        4. Search Contact
        5. List Contacts
        6. Exit
        ----------------------------------
        """)

        choice = input('Choose an option: ')

        if choice == '1':
            add_contact()

        elif choice == '2':
            update_contact()

        elif choice == '3':
            delete_contact()

        elif choice == '4':
            search_contact()

        elif choice == '5':
            list_contacts()

        elif choice == '6':
            print('Contacts saved successfully.')
            break

        else:
            print('Invalid choice. Please try again.')

menu()
