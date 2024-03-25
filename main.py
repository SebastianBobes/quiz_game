# create a quiz_game with admin and players. A player has to login, if player then he can play,
# if admin he can add questions
import json
import random
import string
import pwinput
import user


OKBLUE = '\033[94'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


if __name__ == '__main__':
    welcome_msg = "Welcome to Quiz Game "
    print(f"{len(welcome_msg) * '='} {welcome_msg} {len(welcome_msg) * '='}  {ENDC}")

    MENU = """
    1."""
    login(path="users.json")
