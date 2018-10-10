from time import *
# template for "Stopwatch: The Game"

# define global variables
isRunning = False
start=time()

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
    pass

# define event handler for timer with 0.1 sec interval
def create_timer():
    isRunning=True
    iet=0
    while isRunning and iet < 10:
        #sleep(1) not supported in CodeSkulptor...
        #print(int(10*(time.time()-time())))
        iet+=1

# define draw handler

    
# create frame


# register event handlers


# start frame
create_timer()


# Please remember to review the grading rubric

