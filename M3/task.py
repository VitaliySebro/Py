'''
1. Напишіть програму на Python, щоб знайти ті числа, які 
діляться на 7 і кратні 5, між 1500 і 2700 (обидва включені).

2.Напишіть програму на Python для перетворення температуру 
та з Цельсія, за Фаренгейтом
[ Формула : c/5 = f-32/9 [ де c = температура в Цельсіях, 
а f = температура за Фаренгейтом ]

3. Напишіть програму на Python, щоб вгадати число від 1 до 99. 
Примітка: Користувачеві пропонується ввести припущення. 
Якщо користувач здогадується неправильно,то запит з'являється 
знову, поки припущення не будеправильним, після успішного вгадування 
користувач отримає повідомлення «Добре вгадано!», і програма вийде.

4. Напишіть програму на Python, щоб побудувати наступний 
шаблон, використовуючи вкладений цикл for.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

'''
result = [num for num in range(1500, 2701) if num % 7 == 0 and num % 5 == 0]
print(result)

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius_temperature = float(input("Enter temperature in Celsius: "))
result_fahrenheit = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature}°C is equal to {result_fahrenheit}°F")

import random

secret_number = random.randint(1, 99)

while True:
    guess = int(input("Guess the number (between 1 and 99): "))

    if guess == secret_number:
        print("Well done! You guessed the number.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

for i in range(1, 6):
    print('* ' * i)

for i in range(4, 0, -1):
    print('* ' * i)
