# implementation of card game - Memory

import simplegui
import random

cards = []
exposed = []
for i in range(8):
    cards.append(i)
    cards.append(i)
    print(cards)
for i in range(16):
    exposed.append(False)

# helper function to initialize globals
def new_game():
    global cards
    random.shuffle(cards)  

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    left_coord=0

    for i in range(16):
        canvas.draw_polygon([(left_coord,0),(left_coord+50,0),(left_coord+50,100),(left_coord,100)],5,"White")
        if exposed[i]:
            canvas.draw_text(str(cards[i]),(left_coord + 17,55),30,"White")
        left_coord+=50
        


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric