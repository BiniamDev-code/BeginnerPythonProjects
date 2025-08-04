# 📝 Smart Notes – Command Line Note Manager
import os
import datetime
from colorama import Fore, Style, init

init(autoreset=True)

NOTES_DIR = "notes"
os.makedirs(NOTES_DIR, exist_ok=True)

def create_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: \n")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    filename = f"{title.replace(' ', '_')}.txt"
    path = os.path.join(NOTES_DIR, filename)

    if os.path.exists(path):
        print(Fore.YELLOW + "⚠️ A note with this title already exists. Try another title.")
        return

    with open(path, 'w', encoding='utf-8') as f:
        f.write(f"Title: {title}\n")
        f.write(f"Created: {timestamp}\n\n")
        f.write(content)

    print(Fore.GREEN + f"✅ Note '{title}' created successfully!\n")

def view_all_notes():
    files = os.listdir(NOTES_DIR)
    if not files:
        print(Fore.YELLOW + "No notes found.\n")
        return

    print(Fore.CYAN + "\n📋 Your Notes:")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file.replace('_', ' ').replace('.txt', '')}")
    print()

def read_note():
    title = input("Enter the title of the note to read: ").strip()
    filename = f"{title.replace(' ', '_')}.txt"
    path = os.path.join(NOTES_DIR, filename)

    if not os.path.exists(path):
        print(Fore.RED + "❌ Note not found.\n")
        return

    print(Fore.CYAN + f"\n📄 Content of '{title}':")
    with open(path, 'r', encoding='utf-8') as f:
        print(f.read())
    print()

def delete_note():
    title = input("Enter the title of the note to delete: ").strip()
    filename = f"{title.replace(' ', '_')}.txt"
    path = os.path.join(NOTES_DIR, filename)

    if os.path.exists(path):
        os.remove(path)
        print(Fore.YELLOW + f"🗑️ Note '{title}' deleted successfully.\n")
    else:
        print(Fore.RED + "❌ Note not found.\n")

def search_notes():
    keyword = input("Enter keyword to search in note titles: ").strip().lower()
    files = os.listdir(NOTES_DIR)
    matches = [f for f in files if keyword in f.lower()]

    if not matches:
        print(Fore.RED + "❌ No matching notes found.\n")
        return

    print(Fore.CYAN + "\n🔎 Search Results:")
    for file in matches:
        print("- " + file.replace('_', ' ').replace('.txt', ''))
    print()

def main():
    while True:
        print(Style.BRIGHT + "\n=== Smart Notes Menu ===")
        print("1. Create a Note")
        print("2. View All Notes")
        print("3. Read a Note")
        print("4. Delete a Note")
        print("5. Search Notes")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            create_note()
        elif choice == '2':
            view_all_notes()
        elif choice == '3':
            read_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            search_notes()
        elif choice == '6':
            print(Fore.BLUE + "👋 Goodbye! Thanks for using Smart Notes.")
            break
        else:
            print(Fore.RED + "❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
