import random
from time import sleep
from pynput.keyboard import Key,Controller
class GuessGame:
    def Intro(self):
        sleep(1)
        print("\nWelcome to the Guessing Game! ",end="")
        sleep(1.5)
        contributors = "Designed by Karl and Subhman."
        for char in contributors:
            print(char,end="")
            sleep(0.21)
        sleep(2)
        print("\nThe purpose of the game is simple, the algorithm will randomly pick up a number into a certain range of number "
              "that you will be aware of.")
        sleep(4)
        print("Afterward your will have to guess what is the secret number that was picked up. If you get stuck you can access "
            "to a hint by pressing 'H'.")
        sleep(4)
        print("Then let's start and Good Luck!")
        start = input("Ready to start? (Press Enter) or (Esc to exit the program)")
        return start

    def pick_up(self):
        n1 = random.choice(range(1,501))
        n2 = random.choice(range(501,1001))
        ranges = range(n1,n2)
        number = random.choice(ranges)
        return number,n1,n2


class Main(GuessGame):
    number = 0
    count = 0
    n1 = 0
    n2 = 0
    guesses = ''
    guess_of_count = 6
    out_of_guesses = True
    user = GuessGame().Intro()
    if user == "y":
        lst = GuessGame().pick_up()
        number = lst[0]
        n1 = lst[1]
        n2 = lst[2]
        print("\nSuper! Let's go!")
        print(f"The number selected is between {n1} to {n2}. Time to guess!")
    elif user == "n":
        exit()
    else:
        print("Please enter a valid input.")
    while count <= guess_of_count:
        while True:
            try:
                guesses = int(input("Please enter your guess: "))
                break
            except:
                print("Invalid guesses! Try again.")
        if guesses < number:
            print("The number is too low!")
            count += 1
        elif guesses > number:
            print("The number is too high")
            count += 1
        else:
            print("That the correct number well done!")
            out_of_guesses = False
            break
        count += 1
    if out_of_guesses:
        print(f"Sorry you run out of guesses.The number was {number}.Try again!")
    else:
        print(f"Congratulations you win! The number was '{number}'.")


Main()




