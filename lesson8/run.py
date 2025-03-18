from ranndom_lang import get_random

def main():
    user = input("введиите язык прог: ")

    language_list = [lang.strip() for lang in user.split(",")] if user.strip() else []

    choces_language = get_random(language_list)

    print(f"выбранный язык:{choces_language} ")

main()
