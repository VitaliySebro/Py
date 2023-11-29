'''
Бонусне завдання. 
Придумайте свій чат-бот! 
Не соромтеся експериментувати з командами, які Ви вже знаєте!
Обов'язково придумайте і використовуйте свою власну ідею! 
'''
import random

def play_game(user_choice, bot_choice):
    if user_choice == bot_choice:
        return "Нічия!"
    elif (user_choice == "камінь" and bot_choice == "ножиці") or \
         (user_choice == "ножиці" and bot_choice == "папір") or \
         (user_choice == "папір" and bot_choice == "камінь"):
        return "Ви перемогли!"
    else:
        return "Ви програли!"

def main():
    print("Привіт! Давайте грати в 'камінь, ножиці, папір'!")

    user_choice = input("Введіть ваш вибір (камінь, ножиці, папір): ").lower()
    
    if user_choice not in ["камінь", "ножиці", "папір"]:
        print("Невірний ввід. Будь ласка, виберіть з 'камінь', 'ножиці' або 'папір'.")
        return

    bot_choices = ["камінь", "ножиці", "папір"]
    bot_choice = random.choice(bot_choices)

    print(f"Ваш вибір: {user_choice}")
    print(f"Вибір бота: {bot_choice}")

    result = play_game(user_choice, bot_choice)
    print(result)

if __name__ == "__main__":
    main()
