'''
Створіть програму, яка читає місяць і день від користувача.
Користувач введе назву місяця як рядок, а потім день у межах місяця як ціле число. 
Потім у вашій програмі повинен відобразитися сезон, пов'язаний з датою, 
яка була введена.

'''
# Зчитування місяця та дня від користувача
month = input("Введіть місяць: ").lower()
day = int(input("Введіть день: "))

# Перевірка введеного місяця та визначення сезону
if month in ("грудень", "січень", "лютий"):
    season = "зима"
elif month in ("березень", "квітень", "травень"):
    season = "весна"
elif month in ("червень", "липень", "серпень"):
    season = "літо"
elif month in ("вересень", "жовтень", "листопад"):
    season = "осінь"
else:
    print("Невірно введений місяць.")
    season = None

# Перевірка введеного дня та корекція сезону для грудня та березня
if month == "грудень" and day > 21:
    season = "зима"
elif month == "березень" and day > 20:
    season = "весна"

# Виведення результату
if season:
    print(f"Сезон: {season}.")
