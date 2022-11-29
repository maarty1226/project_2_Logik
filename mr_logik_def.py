"""
projekt_2.py: projekt č. 2 - Engeto Online Python Akademie
author: Martin Rechtorik
email: martin.rechtorik@nacr.cz
discord: Maarty#1226
"""

import random

Welcome = "\nWelcome in Bulls and Cows game\n"
Rules = "\nHello player, your task is to guess a secret number in less then 20 tries!\n"
Separator = "="
print(Welcome)
print(len(Welcome) * Separator)
print(Rules)
print(len(Rules) * Separator)


def gen_number():
    """Generates secret number with unique digits using random.randrange"""
    while True:
        secret_number = (random.randrange(1001,9999))
        if len(str(secret_number)) != len(set(str(secret_number))):
            continue
        else:
            print("Secret number is: " + (str(secret_number)))
            # Please comment line 28 to hide "Secret number".
            return secret_number
            break


def game(secret_number):
    tries = 0
    while tries <= 20:
        tries += 1

        def user_guess():
            """Function checks users input to 4 unique digits and > 1001 and < 9999"""
            while True:
                try:
                    user_number = int(input("Hint: Secret number´s length is 4 and "
                                            "does not start with zero."
                                            "\nNow let´s try your guess:"))
                except ValueError:
                    print("Please enter digits and not characters")
                    continue
                if user_number <= 1000:
                    print("Secret number is higher 1000")
                elif user_number >= 10000:
                    print("Secret number is lower 10000")
                elif len(str(user_number)) != len(set(str(user_number))):
                    print("Digits are unique within secret number")
                else:
                    return user_number
                    break

        user_number = user_guess()


        def compare(secret_number, user_number):
            """
            Checks player´s input against randomly generated secret number and when player is not
            out of number of tries function returns:
            Bull -- a number for digit guessed correctly and at a correct place.
            Cow -- a number for digit guessed but at a wrong place.
            """
            cow_bull = [0, 0]
            for i, j in zip((str(secret_number)), (str(user_number))):

                # common digit present
                if j in (str(secret_number)):

                    # Counts Bulls in user number
                    if j == i:
                        cow_bull[0] += 1

                    # Counts Cows in user number
                    else:
                        cow_bull[1] += 1
            return cow_bull


        cow_bull = compare(secret_number, user_number)


        def result(cow_bull, secret_number, user_number, tries):
            """Reports result from user´s guesses"""
            if secret_number == user_number:
                    print("Wow, you won, 4 Bulls!")
                    print("Secret number was: " + (str(secret_number)) +
                          " You needed " + (str(tries)) + " tries to find it!")
                    if tries < 5:
                        print("Great job!")
                    elif tries > 5 and 10 > tries:
                        print("Good job, Next you´ll do better!")
                    else:
                        print("Nothing special, but don´t worry.")
                    return True
            else:
                tries += 1
                print(f"{cow_bull[0]} bulls, {cow_bull[1]} cows")
                return False


        result = result(cow_bull, secret_number, user_number, tries)

        if result == True:
            break
        else:
            continue


def new_game():
        """Function for game restart."""
        restart = input("Do want to play again?(y/n)")
        if restart == "y" or restart == "Y":
            print("Game restarted...")
            main()

        else:
            print("Thanks for playing.")
            quit()


def main():
    secret_number = gen_number()
    game(secret_number)
    new_game()


if __name__ == "__main__":
    main()
