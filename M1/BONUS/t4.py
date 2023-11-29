'''
обмеження 15 рядків
Створіть програму, яка зчитує довжину та ширину поля фермера від користувача
у футах. Відобразити площу поля в акрах

TODO Hint: There are 43,560 square feet in an acre
'''
length_feet = float(input("Введіть довжину поля у футах: "))
width_feet = float(input("Введіть ширину поля у футах: "))

area_acres = (length_feet * width_feet) / 43560  # 1 акр = 43,560 кв. футів

print(f"Площа поля: {area_acres} акрів")
