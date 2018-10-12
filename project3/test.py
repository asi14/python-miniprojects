import simplegui
# template for "Stopwatch: The Game"

# define global variables
isRunning = False
elapsed=0
successes=0
total=0

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
    timer.start()
def stop():
    timer.stop()
def reset():
    global elapsed
    global total
    global successes
    elapsed=0
    successes=0
    total=0
    
def capture():
    global successes
    global total
    total+=1
    if elapsed%10==0 and elapsed != 0:
        successes+=1
    
    
# define event handler for timer with 0.1 sec interval
#so apparently there's a CodeSkulptor timer...
def time_handler():
    global elapsed
    elapsed+=1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(elapsed), [50,112], 48, "White")
    canvas.draw_text("Success/Total: %s/%s" % (successes,total),(5,20),20,"White")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
frame.set_draw_handler(draw)

# register event handlers
frame.add_button('Start Time',start)
frame.add_button('Stop Time',stop)
frame.add_button('Reset',reset)
frame.add_button('Capture!',capture)
timer = simplegui.create_timer(100, time_handler)

# start frame
frame.start()

# Please remember to review the grading rubric