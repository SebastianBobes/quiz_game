# create a quiz_game with admin and players. A player has to login, if player then he can play,
# if admin he can add questions
import json
import random
import string
import pwinput

OKBLUE = '\033[94'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def add_user(player_id:str, all_players: dict, path: str = "users.json") -> dict:
    full_name = input("Introdu numele tau (optional) ")
    full_name = player_id if full_name == "" or not full_name.isalnum() else full_name
    passwd = ""
    confirm_password = " "
    while len(passwd) < 3:
            while passwd!= confirm_password:
                passwd = input("Introdu parola ta: ")
                confirm_password = input("Confirma parola: ")
            if len(passwd) < 3:
                print("Parola este prea mica!")
    new_user = {player_id: {"full_name": full_name, "high_score": 0}, "password": passwd}
    all_players.update(new_user)
    with open(path, "r+") as f:
        users = f.write(json.dumps(all_players, indent=4))

    return new_user


def login(path: str = "user.json"):
    is_new_user = False
    new_user = {}
    user = input("Logheaza-te: ")
    with open(path, "r") as f:
        users = json.loads(f.read())

    if user not in users:
        user_pick = input("Doresti sa te inscrii ca nou jucator ? Y/N")
        if user_pick.lower() == "y":
            new_user = add_user(player_id = user, all_players = users)
            is_new_user = True
        else:
            while user not in users:
                user = input("Logheaza-te! Utilizatorul nu exista! ")
    if not is_new_user:
        passwd = input("Introduceti parola: ")
        counter = 1
        while passwd != users[user]['password']:
            passwd = input("Introduceti parola: ")
            counter += 1
            if counter == 3:
                raise Exception("Parola a fost introdusa de prea multe ori!")
    else:
        return {user: users[user]}


if __name__ == '__main__':
    welcome_msg = "Welcome to Quiz Game "
    print(f"{len(welcome_msg) * '='} {welcome_msg} {len(welcome_msg) * '='}  {ENDC}")

    MENU = """
    1."""
    login(path="users.json")
