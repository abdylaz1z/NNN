import random 

def get_random_user():
    return random.randint(1,100)

def save_result(attems, guessed):
    with open("game_result.txt", "a",encoding="utf-8") as file:
        if guessed:
            file.write(f"игрок угадал число за {attems} попыток")

        else:
            file.write("игрок не угадал чиссло за 10 попыток")