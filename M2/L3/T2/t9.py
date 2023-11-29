'''
А тепер перед Вами програма робота-маляра: 
програма запитує колір, яким треба намалювати лінію. 
Зараз робот вміє малювати тільки червону лінію, 
навчіть його малювати також синю (blue) і зелену (green) лінії.
'''

from turtle import *

turtle_color = input("Який колір використовувати?")

if turtle_color == "червоний":
    color("red")
elif turtle_color == "синій":
    color("blue")
elif turtle_color == "зелений":
    color("green")
else:
    print("Вибачте, такий колір не підтримується.")

forward(100)
exitonclick()

