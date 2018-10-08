from random import randint
import simplegui

#basic declaration of key variables that will quickly be utilized in range1000 and range100
secret_number = 0
failures = 0
max_guess = 7

def new_game():
	range100()

def range100():
	global max_guess
	global secret_number
	global failures
	failures = 0
	secret_number = randint(0,99)
	max_guess = 7
	print("\nA new game has been started with the range [0,100). You have 7 tries.")
def range1000():
	global max_guess
	global secret_number
	global failures
	failures = 0
	secret_number = randint(0,999)
	max_guess = 10
	print("\nA new game has been started with the range [0,1000). You have 10 tries left.")	
def input_guess(guess):
	global failures
	try:
		guessInt = int(guess)
		print("Your guess was %s" % guessInt)	
		if guessInt > secret_number:
			failures = failures + 1
			print("Lower. you have %s tries left." % (max_guess - failures))
		elif guessInt < secret_number:
			failures = failures +1
			print("Higher. You have %s tries left." % (max_guess - failures))
		else:
			print("Correct! A new game will begin.")
			range100()
		if failures >= max_guess:
			print("You Lost. The answer was %s. A new game will begin." % secret_number)
			range100()
	except:
		print("That was an invalid input. Please Try Again.")

# create frame
frame = simplegui.create_frame("Guessing Game",0,0)
inputa = frame.add_input("Enter Guess Here",input_guess,75)
inputa.set_text("Number")
frame.add_button("[1,100)",range100,50)
frame.add_button("[1,000)",range1000,50)
frame.canvas_width=0
frame.control_width=0
frame.start()

new_game()




