#  "set"- изменяемый типп данных хранить только одно значение 
# add- добавляетть элемент в set
# remove- удаляет из set



# number1 = {1,2,3,4,5,6}
# number2 = {6,7,8,9,10}
# print(number1|number2) # объединение 
# print(number1 & number2) # пересичение


# import random

# words = ["python", "golang", 'django', 'fastapi', 'onion']

# sercer_word = random.choice(words)
# sercet_set = set(sercer_word)
# guessed_letters = set()
# attemts = 7

# print("Добро пожаловать в игру Собери слова")
# print(f"В слове {len(sercer_word)} букв. Попробуйте угадать его по буквам!")

# while attemts > 0:
#     word_display = "".join(letter if letter in guessed_letters else "_" for letter in sercer_word)
#     print("\nТекущее слово: ", word_display)
#     print(f"Осталось попыток: {attemts}")

#     letter = input("Введите букву: ").lower()

#     if len(letter) != 1 or not letter.isalpha():
#         print("Введите одну букву")
#         continue

#     if letter in guessed_letters:
#         print("Ты уже угадал эту букву")
#         continue

#     if letter in sercet_set:
#         guessed_letters.add(letter)
#         print(f"Отлично! Буква {letter} есть в слове" )
#     else:
#         attemts -= 1
#         print("Ошибка такой буквы нет")

#     if guessed_letters == sercet_set:
#         print("Поздравляем! Ты угадал", sercer_word.upper())
#         break
# else:
#     print("\n💀 Увы, попытки закончились. Загаданное слово было:", sercer_word.upper())

# frozenset- нельзя изменить

# set1 = frozenset({1,2,3,4})
# set2 = frozenset({3,4,5,6})
# print(set1|set2)

# list = [1,2,3,4,4,5,5,6,6,7,7]
# list2 = set(list)
# print(list2)

# list = ["word", "hello", "I", "am", "people"]
# list2 = frozenset(list)
# list2.add #нельзя добавить новый элемент

# text = """hello word, hello word, hello word, dili """
# list1 = set(text)
# list2 = len(list1)
# print(list2)


# dict- "словарь" изменяемый тип данных,  данные хпраняться в виде люч и значение 



# person = {
#     'name': 'abu',
#     'age':18,
#     'city': 'osh'
# }
# del person['name'] # удаляем по ключу

# for key in person:
#     print(key, ":", person[key])

# for key, Value in person.items():
#     print(f"{key} : {Value}")

# print(person.keys()) #выводит ключи
# print(person.values()) #выводит занчение ключа 
# print(person.items()) # выводит ключ и их значение 

# dict1 = {
#     "a": 1,
#     "b": 2
# }
# dict2 = {
#     "c": 3,
#     "d": 4
# }
# dict1.update(dict2) # добавьляем один словарь в другой
# print(dict1)

# prices = {
#     "apple": 100,
#     "banan": 150,
#     "watermelon": 123,
#     "груша": 100
# }

# product = input("введите название товара: ").lower()
# quantity = int(input("сколько ввам их нужно?"))

 
# if product in prices:
#     print(f"Цена {product}:{prices[product]*quantity} сом")
# else:
#     print(f"товар не найден!")


# students = {
#     "abu":5,
#     "urmat":5,
#     "bekzat":4
# }

# student = input("введите имя студента: ")
# if student in students:
#     print(f"оценка {student}:{students[student]}")
# else:
#     print("студент не найден!")


