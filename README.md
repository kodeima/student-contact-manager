# Student Contact Manager

## Overview
The student contact manager is a python-based console aplication designed for users to efficiently store, manage, and organise contact details for students, parents, and teachers.

The system stores contacts using a dictionary, ensures data integrity using sets for duplicate prevention, and persists data using a `json` file so information is saved between sessions.

---

## Features
- Add new contacts (Student, Parent, or Teacher)
- Update existing contact information
- Delete contacts from the system
- Search contacts by ID or name
- Display all contacts in a structured format
- Automatically prevent duplicate emails
- Automatically prevent duplicate phone numbers
- Validate email format using regular expressions
- Validate phone numbers (digits and minimum length)
- Store contacts in a dictionary using unique IDs
- Persist data using a JSON file (`student_contacts.json`)
- Sort contacts alphabetically by name
- Use indexing and slicing to access subsets of data
- Demonstrates list operations (`append`, `remove`, `sort`)
- Uses tuples for fixed role definitions

---

## Data Structures Used

### 1. Dictionary (Main Storage)

Each contact is stored using a unique ID:

```python
contacts = {
    "ST001": {
        "name": "John Doe",
        "email": "john@gmail.com",
        "phone": "08012345678",
        "role": "Student"
    }
}
```

### 2. Sets (Duplicate Prevention)

Used to ensure no duplicate emails or phone numbers exist:
- emails = set()
- phones = set()

### 3. Lists (Data Handling and Learning concepts)

Contacts are converted into a list for:
- Sorting
- Indexing
- Slicing
- Searching
- Display formatting

Example:
```python
contact_list = list(contacts.items()
```

### 4. Tuples (Fixed Data)

Used for roles that should not change:

```python
VALID_ROLES = ("Student", "Parent", "Teacher")
```

---

## Libraries Used

This project uses only Python built-in libraries.

Libraries used: json, os, and re.

No external installations are required.

---

## How to Run

1. Save the program.
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run the script.

---

## Usage

```text
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
```

---

## Data Storage

All data is stored in `student_contacts.json`
