# 🔁 Python Unit Converter Tool
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def convert_length():
    print(Fore.CYAN + "\n📏 Convert Length:")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Miles")
    print("3. Miles to Meters")
    choice = input("Choose conversion (1-3): ")
    val = float(input("Enter value: "))
    if choice == '1':
        print(f"{val} meters = {val / 1000} kilometers")
    elif choice == '2':
        print(f"{val} km = {val * 0.621371} miles")
    elif choice == '3':
        print(f"{val} miles = {val * 1609.34} meters")
    else:
        print(Fore.RED + "❌ Invalid choice.")

def convert_temperature():
    print(Fore.CYAN + "\n🌡 Convert Temperature:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    choice = input("Choose conversion (1-3): ")
    val = float(input("Enter value: "))
    if choice == '1':
        print(f"{val}°C = {(val * 9/5) + 32}°F")
    elif choice == '2':
        print(f"{val}°F = {(val - 32) * 5/9}°C")
    elif choice == '3':
        print(f"{val}°C = {val + 273.15} K")
    else:
        print(Fore.RED + "❌ Invalid choice.")

def convert_weight():
    print(Fore.CYAN + "\n⚖ Convert Weight:")
    print("1. Grams to Kilograms")
    print("2. Kilograms to Pounds")
    print("3. Pounds to Grams")
    choice = input("Choose conversion (1-3): ")
    val = float(input("Enter value: "))
    if choice == '1':
        print(f"{val} g = {val / 1000} kg")
    elif choice == '2':
        print(f"{val} kg = {val * 2.20462} lb")
    elif choice == '3':
        print(f"{val} lb = {val * 453.592} g")
    else:
        print(Fore.RED + "❌ Invalid choice.")

def convert_time():
    print(Fore.CYAN + "\n⏱ Convert Time:")
    print("1. Seconds to Minutes")
    print("2. Minutes to Hours")
    print("3. Hours to Seconds")
    choice = input("Choose conversion (1-3): ")
    val = float(input("Enter value: "))
    if choice == '1':
        print(f"{val} seconds = {val / 60} minutes")
    elif choice == '2':
        print(f"{val} minutes = {val / 60} hours")
    elif choice == '3':
        print(f"{val} hours = {val * 3600} seconds")
    else:
        print(Fore.RED + "❌ Invalid choice.")

def main():
    while True:
        print(Style.BRIGHT + "\n=== UNIT CONVERTER ===")
        print("1. Convert Length")
        print("2. Convert Temperature")
        print("3. Convert Weight")
        print("4. Convert Time")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == '1':
            convert_length()
        elif choice == '2':
            convert_temperature()
        elif choice == '3':
            convert_weight()
        elif choice == '4':
            convert_time()
        elif choice == '5':
            print(Fore.GREEN + "👋 Thanks for using the Unit Converter!")
            break
        else:
            print(Fore.RED + "❌ Invalid input. Try again.")

if __name__ == "__main__":
    main()
