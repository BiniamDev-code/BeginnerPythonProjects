# Simple Python Login App

import os
import re
import getpass
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

USER_DIR = "users"
os.makedirs(USER_DIR, exist_ok=True)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def create_account():
    username = input("Enter a Username: ")
    path = os.path.join(USER_DIR, f"{username}.txt")

    if os.path.exists(path):
        print(Fore.YELLOW + "⚠️ This username already exists. Try another one.\n")
        return

    roll_no = input("Enter your Roll Number: ")
    email = input("Enter your Email: ")
    
    if not is_valid_email(email):
        print(Fore.RED + "❌ Invalid email format.\n")
        return

    password = getpass.getpass("Create a Password: ")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(path, 'w') as file:
        file.write(f"{username}\n{roll_no}\n{email}\n{password}\n{created_at}")

    print(Fore.GREEN + "✅ Account created successfully!\n")

def login():
    username = input("Enter your Username: ")
    password = getpass.getpass("Enter your Password: ")
    path = os.path.join(USER_DIR, f"{username}.txt")

    if not os.path.exists(path):
        print(Fore.RED + "❌ Account not found. Please create an account first.\n")
        return

    with open(path, 'r') as file:
        data = file.read().splitlines()
        stored_username = data[0]
        stored_password = data[3]

    attempts = 3
    while attempts > 0:
        if username == stored_username and password == stored_password:
            print(Fore.GREEN + f"✅ Welcome back, {username}!\n")
            return
        else:
            attempts -= 1
            print(Fore.RED + f"❌ Incorrect password. Attempts left: {attempts}")
            if attempts == 0:
                print(Fore.RED + "🚫 Too many failed attempts. Returning to menu.\n")
                return
            password = getpass.getpass("Try again: ")

def view_account():
    username = input("Enter your Username to view details: ")
    path = os.path.join(USER_DIR, f"{username}.txt")

    if not os.path.exists(path):
        print(Fore.RED + "❌ Account not found.\n")
        return

    with open(path, 'r') as file:
        data = file.read().splitlines()
        print(Fore.CYAN + "\n📄 Account Details:")
        print(f"👤 Username  : {data[0]}")
        print(f"🆔 Roll No   : {data[1]}")
        print(f"📧 Email     : {data[2]}")
        print(f"📅 Created At: {data[4]}\n")

def delete_account():
    username = input("Enter your Username to delete your account: ")
    path = os.path.join(USER_DIR, f"{username}.txt")

    if os.path.exists(path):
        os.remove(path)
        print(Fore.YELLOW + "🗑️ Account deleted successfully.\n")
    else:
        print(Fore.RED + "❌ Account not found.\n")

def list_accounts():
    users = os.listdir(USER_DIR)
    if not users:
        print(Fore.YELLOW + "No accounts found.\n")
        return

    print(Fore.CYAN + "\n📜 All Usernames:")
    for user_file in users:
        print("- " + user_file.replace(".txt", ""))
    print()

def main():
    while True:
        print(Style.BRIGHT + "=== Python Login App ===")
        print("1. Create Account")
        print("2. Login")
        print("3. View Account Details")
        print("4. Delete Account")
        print("5. List All Accounts")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            view_account()
        elif choice == '4':
            delete_account()
        elif choice == '5':
            list_accounts()
        elif choice == '6':
            print(Fore.BLUE + "👋 Goodbye!")
            break
        else:
            print(Fore.RED + "❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
