# implementation of card game - Memory

import simplegui
import random

cards = []
exposed = []

selected=[-1,-1]
isCorrect=True

turn_counter = 0

def timer_handler():
    timer.stop()


timer = simplegui.create_timer(1000,timer_handler)

def score_add():
    global turn_counter
    global label
    turn_counter+=1
    label.set_text("Turns = %s" % turn_counter)


# helper function to initialize globals
def new_game():
    global exposed
    global cards
    global turn_counter
    global label
    cards = []
    exposed = []
    for i in range(8):
        cards.append(i)
        cards.append(i)
        random.shuffle(cards)  
    for i in range(16):
        exposed.append(False)
    turn_counter=0
    label.set_text("Turns = %s" % turn_counter)
    if timer.is_running():
        timer.stop()
    

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed
    global selected
    global timer
    global isCorrect
    if exposed[pos[0]/50] == True or timer.is_running() == True:
        pass
    elif selected[0] == -1:
        exposed[pos[0]/50]=True #for FIRST card
        selected[0] = pos[0]/50
        score_add()
    elif cards[selected[0]] == cards[pos[0]/50]:
        exposed[pos[0]/50]=True #for SECOND card
        #note: selected has already been set to True by this point
        selected[0] =-1
        isCorrect=True
        score_add()
    else:
        #how to handle when loss given?
        isCorrect=False
        selected[1]=pos[0]/50
        exposed[selected[0]]=True
        exposed[selected[1]]=True
        timer.start()
        score_add()
        
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global timer
    global selected
    global isCorrect
    global exposed
    left_coord=0

    for i in range(16):
        canvas.draw_polygon([(left_coord,0),(left_coord+50,0),(left_coord+50,100),(left_coord,100)],5,"White")
        if exposed[i]:
            canvas.draw_text(str(cards[i]),(left_coord + 17,55),30,"White")
        left_coord+=50
    if timer.is_running() == False and isCorrect == False:
        print('d')
        exposed[selected[0]]=False
        exposed[selected[1]]=False
        isCorrect=True
        selected=[-1,-1]
        
            


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = %s" % turn_counter)


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric