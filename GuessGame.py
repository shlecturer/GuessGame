import random
from time import sleep
import keyboard

class GuessGame:
    @staticmethod
    def intro():
        sleep(1)
        print("\nWelcome to the Guessing Game! ", end="")
        sleep(1.5)
        contributors = "Designed by Karl and Sander."
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
        print("Press <enter> to start or <escape> to quit.")

        while True:
            if keyboard.is_pressed('enter'): #Keyboard listener check if the key 'Enter' is pressed
                break #If pressed start to play
            elif keyboard.is_pressed('esc'): #Keyboard listener check if the key 'Esc' is pressed
                exit() #If pressed exit the program



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
    GuessGame.intro()
    while True:
        number, n1, n2 = GuessGame.pick_up()
        print("\nSuper! Let's go!")
        print(f"The number selected is between {n1} to {n2}. Time to guess!")
        break
    while count <= guess_of_count:
        if count >= 2:
            print("Do you want a hint? Press 'H' or 'P' to pass.")
            while True:
                if keyboard.is_pressed('h') or keyboard.is_pressed('H'): #Keyboard listener check if the key 'H' is pressed
                    # if pressed the user can have a hint
                    if guesses < number:
                        print("The number was too low!")
                        break
                    elif guesses > number:
                        print("The number was too high")
                        break
                elif keyboard.is_pressed('p') or keyboard.is_pressed('P'):#Keyboard listener check if the key 'P' is pressed
                    #if pressed the user pass and doesn't get a hint
                    break

        while True:
            try:
                guesses = int(input("Please enter your guess: "))
                if not n1 <= guesses <= n2:
                    print("Out of the range!")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid guesses! Try again.")

        if guesses != number:
            print("Sorry. Try again!")
        else:
            print("That's the correct number well done!")
            out_of_guesses = False
            break
        count += 1

    if out_of_guesses:
        print(f"Sorry you run out of guesses.The number was {number}. Try again!")
    else:
        print(f"Congratulations you win! The number was '{number}'.")


if __name__ == '__main__':
    main()
