# 🎰 Python Lottery App
import random
from colorama import Fore, Style, init

init(autoreset=True)

user_money = 0

# Prize money for each number
value_of_numbers = {
    1: 5, 2: 10, 3: 15, 4: 20, 5: 25,
    6: 30, 7: 35, 8: 40, 9: 45, 10: 50
}

print(Style.BRIGHT + Fore.MAGENTA + "🎉 Welcome to the Python Lottery Game 🎉")
username = input("What's your name?: ")
print(Fore.CYAN + f"Hi there, {username}! Let's test your luck.")

while True:
    print(Fore.YELLOW + "\n🔢 Guess a number between 1 and 10 (or type 0 to quit):")
    try:
        guess = int(input("Your guess: "))

        if guess == 0:
            print(Fore.BLUE + f"👋 Thanks for playing, {username}! You won a total of ${user_money}.")
            break

        if guess < 1 or guess > 10:
            print(Fore.RED + "⚠️ Please enter a number between 1 and 10.")
            continue

        random_num = random.randint(1, 10)

        if guess == random_num:
            value = value_of_numbers[random_num]
            user_money += value
            print(Fore.GREEN + f"🎯 Correct! You guessed {random_num} and won ${value}!")
            print(Fore.GREEN + f"💰 Total Money: ${user_money}")
        else:
            print(Fore.RED + f"❌ Wrong! The correct number was {random_num}. Try again!")

    except ValueError:
        print(Fore.RED + "⚠️ Please enter a valid number.")
