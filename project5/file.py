# implementation of card game - Memory

import simplegui
import random

cards = []
exposed = []

selected=-1


# helper function to initialize globals
def new_game():
    global exposed
    global cards
    cards = []
    exposed = []
    for i in range(8):
        cards.append(i)
        cards.append(i)
        random.shuffle(cards)  
    for i in range(16):
        exposed.append(False)


     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed
    global selected
    if exposed[pos[0]/50] == True:
        pass
    elif selected == -1:
        exposed[pos[0]/50]=True #for FIRST card
        selected = pos[0]/50
    elif selected == pos[0]/50:
        exposed[pos[0]/50]=True #for SECOND card
        #note: selected has already been set to True by this point
        selected =-1
    else:
        #how to handle when loss given?
        exposed[selected]=False
        exposed[pos[0]/50]=False
        selected=-1
        
    
                        
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