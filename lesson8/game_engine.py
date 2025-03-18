from math import fabs
from gamee_logik import get_random_user, save_result

def guess_number():
    secret_num = get_random_user()
    attems = 0

    print("добро пожоловать в игру ")
    print("компютер загадаал число от 1 до 100")

    while attems <10:
        try:
            user = int(input("введите число: "))
        except ValueError:
            print("ОШИБКА!")
            continue

        attems += 1

        if user < secret_num:
            print("число больше")

        elif user > secret_num:
            print("число меньше")

        else:
            print(f"ты угадал число {secret_num} за {attems} попыток")
            save_result(attems,True)
            break

    else:
        print(f"ты не угадал число {secret_num}")
        save_result(attems, False)

guess_number()
