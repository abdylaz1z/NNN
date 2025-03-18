import random

def get_random(language_list):
    if not language_list:
        language_list = ['Python', 'Java', 'C++', 'Kotlin', 'Golang', 'Ruby']

    choices = random.choice(language_list)

    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write(f"Случайно выбраннный язык: {choices}")

    return choices
