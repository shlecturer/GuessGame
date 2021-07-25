import random
from time import sleep


class GuessGame:
    @staticmethod
    def intro():
        sleep(1)
        print("\nWelcome to the Guessing Game! ", end="")
        sleep(1.5)
        contributors = "Designed by Karl and Subhman."
        for char in contributors:
            print(char, end="")
            sleep(0.21)
        sleep(2)
        print("\nThe purpose of the game is simple, the algorithm will randomly pick up a number into a certain range of number "
              "that you will be aware of.")
        sleep(4)
        print("Afterward your will have to guess what is the secret number that was picked up. If you get stuck you can access "
            "to a hint by pressing 'H'.")
        sleep(4)
        print("Then let's start and Good Luck!")
        start = input("Ready to start? Type 'y' or 'n'").lower()
        return start

    @staticmethod
    def pick_up():
        n1 = random.choice(range(1, 501))
        n2 = random.choice(range(501, 1001))
        ranges = range(n1, n2)
        number = random.choice(ranges)
        return number, n1, n2


def main():
    count = 1
    guesses = ''
    guess_of_count = 5
    out_of_guesses = True
    user = GuessGame.intro()
    while True:
        if user == "y":
            number, n1, n2 = GuessGame.pick_up()
            print("\nSuper! Let's go!")
            print(f"The number selected is between {n1} to {n2}. Time to guess!")
            break
        elif user == "n":
            exit()
        else:
            print("Please enter a valid input.")
            user = input("Ready to start? Tape 'y' or 'n'").lower()

    while count <= guess_of_count:
        while True:
            if count >= 2:
                hint = input("Do you want a hint? Press 'H' or 'Enter' to pass: ").lower()
                if hint == "h":
                    if guesses < number:
                        print("The number was too low!")
                        break
                    elif guesses > number:
                        print("The number was too high")
                        break
                elif hint == "":
                    break
                else:
                    print("Please enter a valid input.")
            else:
                break

        while True:
            try:
                guesses = int(input("Please enter your guess: "))
                if guesses < n1 or guesses > n2:
                    print("Out of the range!")
                    continue
                else:
                    break
            except:
                print("Invalid guesses! Try again.")

        if guesses != number:
            print("Sorry. Try again!")
        else:
            print("That's the correct number well done!")
            out_of_guesses = False
            break
        count += 1

    if out_of_guesses:
        print(f"Sorry you run out of guesses.The number was {number}.Try again!")
    else:
        print(f"Congratulations you win! The number was '{number}'.")


if __name__ == '__main__':
    main()
