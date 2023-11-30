def dialog(question, right_answer, comment1, comment2):
    s = input(question)
    if s.lower() == right_answer.lower():
        print(comment1)
    else:
        print(comment2)

dialog("Яку мову програмування ми вивчаємо?", "Python",
       "Правильно!", "Неправильна відповідь. Ми вивчаємо Python.")
