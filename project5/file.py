# implementation of card game - Memory

import simplegui
import random

cards = []
exposed = []

selected=[-1,-1]
isCorrect=True


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
    elif selected[0] == -1:
        exposed[pos[0]/50]=True #for FIRST card
        selected[0] = pos[0]/50
    elif selected[0] == pos[0]/50:
        exposed[pos[0]/50]=True #for SECOND card
        #note: selected has already been set to True by this point
        selected[0] =-1
        isCorrect=True
    else:
        print('ran')
        #how to handle when loss given?
        selected[1]=exposed[pos[0]/50]
        exposed[pos[0]/50]=True
        isCorrect=False
        
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    print('b')
    left_coord=0

    for i in range(16):
        canvas.draw_polygon([(left_coord,0),(left_coord+50,0),(left_coord+50,100),(left_coord,100)],5,"White")
        if exposed[i]:
            canvas.draw_text(str(cards[i]),(left_coord + 17,55),30,"White")
        left_coord+=50
    left_coord=0
    if isCorrect == False:
        print('a')
        global selected
        exposed[select[0]]=False
        exposed[select[1]]=False
        selected=[-1,-1]
        
        
        


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