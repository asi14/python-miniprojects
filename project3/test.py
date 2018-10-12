import time
import simplegui
# template for "Stopwatch: The Game"

# define global variables
isRunning = False
elapsed=0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    t=int(t)
    if t < 600:
        filler = (2-len(str(t/10)))*'0'
        return '%s:%s.%s' % (0,filler + str(t/10),t%10)
    else:
        filler = (2-len(str((t%600)/10)))*'0'
        return '%s:%s.%s' % (t/600,filler + str((t%600)/10),t%10)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    print('a')
    global isRunning
    isRunning=True
    create_timer()

# define event handler for timer with 0.1 sec interval
#so apparently there's a CodeSkulptor timer...
def create_timer():
    
    start = time.time()
    iet=0
    global elapsed
    
    while isRunning and iet < 30:  
        end = time.time()
        deltat = int(10*(end-start))
        print(deltat)
        if deltat>=0 and deltat != elapsed:
            elapsed=deltat
            print(elapsed)
            iet+=1


# define draw handler
def draw(canvas):
    canvas.draw_text(str(elapsed), [50,112], 48, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
frame.set_draw_handler(draw)

# register event handlers
frame.add_button('Start Time',start)

frame.start()

# start frame


# Please remember to review the grading rubric
