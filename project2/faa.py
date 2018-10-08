from random import randint
import simplegui

# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

secret_number=0
failures=0
max_guess = 7

# helper function to start and restart the game
def new_game():
    global secret_number 
    secret_number = randint(0,99)


# define event handlers for control panel
def range100():
    global max_guess
    new_game()
    max_guess=7
    print("\n A new game has been started with range [0,99). You have 7 tries")

def range1000():
    global secret_number
    global max_guess
    max_guess = 10
    secret_number = randint(0,999)
    # button that changes the range to [0,1000) and starts a new game     
    print("\n A new game has been started with range [0,999). You have 10 tries")
    
def input_guess(guess):
    global failures
    try:
        guessInt = int(guess)
        
        print("The guess was %s" % guessInt)
        if guessInt - secret_number < 0:
            failures=failures+1
            print("Higher. You have %s tries left." % (max_guess - failures))
            
        elif guessInt - secret_number > 0:
            failures=failures+1
            print("Lower. You have %s tries left." % (max_guess - failures))
            
        else:
            print("Correct! A New Game will begin.\n")
            new_game()
            failures = 0
        if failures == max_guess:
            print("You've used all attempts. The correct answer was %s. A new game will begin.\n" % secret_number)
            new_game()
            max_guess=7
            print("\n A new game has been started with range [0,99). You have %s tries" % max_guess)
            failures = 0
    except:
        print("That was an invalid input. Please Try Again.")

    # main game logic goes here	


    
# create frame
frame = simplegui.create_frame("Guessing Game",0,0)
inputa = frame.add_input("Enter Guess Here",input_guess,75)
inputa.set_text("Number")
frame.add_button("[1,100)",range100,50)
frame.add_button("[1,000)",range1000,50)
frame.canvas_width=0
frame.control_width=0
frame.start()

# register event handlers for control elements and start frame


# call new_game 
new_game()
print("\n A new game has been started with range [0,99). You have 7 tries")
#input_guess("2")


# always remember to check your completed program against the grading rubric

