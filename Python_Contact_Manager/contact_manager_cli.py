import os
import csv

FILENAME = "contacts.csv"

# Create the CSV file with header if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    with open(FILENAME, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])

    print(f"✅ Contact '{name}' added.")

def view_contacts():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(f"📇 Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")

def search_contacts():
    keyword = input("Search name or phone: ").lower()

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        found = False
        for row in reader:
            if keyword in row[0].lower() or keyword in row[1]:
                print(f"🔎 {row[0]} | {row[1]} | {row[2]}")
                found = True
        if not found:
            print("❌ No matching contact.")

def update_contact():
    target = input("Enter name to update: ").strip()
    contacts = []

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        contacts = list(reader)

    for i in range(1, len(contacts)):
        if contacts[i][0].lower() == target.lower():
            print(f"Editing: {contacts[i]}")
            contacts[i][1] = input("New Phone: ").strip()
            contacts[i][2] = input("New Email: ").strip()
            break
    else:
        print("❌ Contact not found.")
        return

    with open(FILENAME, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)

    print("✅ Contact updated.")

def delete_contact():
    target = input("Enter name to delete: ").strip()
    contacts = []

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        contacts = list(reader)

    new_contacts = [contacts[0]]
    deleted = False
    for contact in contacts[1:]:
        if contact[0].lower() != target.lower():
            new_contacts.append(contact)
        else:
            deleted = True

    if deleted:
        with open(FILENAME, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_contacts)
        print("🗑️ Contact deleted.")
    else:
        print("❌ Contact not found.")

def menu():
    while True:
        print("\n=== Contact Manager CLI ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    menu()
