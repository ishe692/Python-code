import random

# clear terminal
import os
os.system('cls')

import threading
import keyboard

def on_esc_pressed():
    exit(0)

def esc_listener():
    keyboard.add_hotkey('esc', on_esc_pressed)
    keyboard.wait()

listener_thread = threading.Thread(target=esc_listener, daemon=True)
listener_thread.start()

def guesser(bottom, top):
    guess = input(f'\nGuess a number from between {bottom} and {top}: \n  ')
    if not guess.isdigit:
        print('sorry the guess has to be a number. You lose')
        exit()

    r = random.randrange(int(bottom),int(top)+1)
    print(f'The number was: {r}\n')
    if int(guess) == r:
        print(correct[random.randrange(-1,len(correct))])
    else:
        print(incorrect[random.randrange(-1,len(incorrect))])
    print('\n')
    guesser(bottom,top)





correct = ["Correct!! you guessed right?! its a miracle, maybe you are not such a dissapointment after all\n although... you could try again?", "Bravo, you've cracked the code of guessing the same number repeatedly.\n Maybe you should apply to be a government spy or something.\n we will try again to make sure you're up for the task", "Congratulations, you've won absolutely nothing but the opportunity to try again!", "I can see that you're a fan of repetition. Have you considered watching paint dry for entertainment?", ]

incorrect = ["So close, yet so far... from being right.", "Wrong number, but you're still a winner in our hearts! (Just kidding, you're still a loser.)", "That guess was so bad, I'm not even mad. I'm impressed.", "Sorry, that's not the right number. But hey, at least you're consistent in being consistently wrong!", "The correct number has alluded you like your Dad going out to get milk.", "I am sorry, the numbers have obviously reduced you to a bumbling idiot; sorry, did I say reduce? I am sure that is an improvement for you", "You won't get it, ever, ever, ever, ever....", "Your brain called, it said it needs a break from the current task as it is too cognitively challanging.", "Wrong again, but keep going! Remember, in the words of Dory from Finding Nemo, \"Just keep swimming.\"", "Incorrect, but don't worry, you still have a better success rate than the Stormtroopers."]



def main():
    bottom = input('Type a number for bottom range: \n')
    top = input('Type a number for top range: \n')
    guesser(bottom, top)

main()