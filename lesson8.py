# with open("text.txt", "r",encoding="utf-8") as file:
#     test = file.read()
#     print(test)


# with open("text.txt", "w",encoding="utf-8") as file:
#     file.write("это новая строка \n")

# with open("text.txt", "a",encoding="utf-8") as file:
#     file.write("alym\n")

# with open("text.txt", "r+",encoding="utf-8") as file:
#     content  = file.read()
#     file.write("akjol")
#     print(file)

# import random
# def get_random_language():
#     user = input("введиите язык прог ")
    
#     if user.strip():
#         language = [lang.strip() for lang in user.split(",")]
#     else:
#         language = ['Python', 'Java', 'C++', 'Kotlin', 'Golang', 'Ruby']

#     choicen_language = random.choice(language)

#     with open("result.txt", "w",encoding="utf-8") as file:
#         file.write(f"язык{choicen_language}: ")

#     print(f"язык:{choicen_language}")

# get_random_language()