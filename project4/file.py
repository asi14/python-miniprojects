# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

DELTA_T=0.03
PADDLE_VEL=100
paddle1_vel=0
paddle2_vel=0
paddle1_pos=[PAD_WIDTH,HEIGHT/2]
paddle2_pos=[WIDTH-PAD_WIDTH,HEIGHT/2]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[300,200]
    ball_vel = [0,0]
    ball_vel[0] = (1 if direction else -1)*random.randrange(120,240)
    ball_vel[1] = -random.randrange(60,180)

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(random.randrange(1,10)>5)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos=[ball_pos[0]+ball_vel[0]*DELTA_T,ball_pos[1]+ball_vel[1]*DELTA_T]
    
    #checks if hits ceiling/floor or sides
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT-BALL_RADIUS:
        ball_vel[1]=-ball_vel[1]
    if ball_pos[0] <= PAD_WIDTH+BALL_RADIUS:
        spawn_ball(RIGHT)
    elif ball_pos[0] >= WIDTH-PAD_WIDTH-BALL_RADIUS:
        spawn_ball(LEFT)
            
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,1,'White','White')
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1]+paddle1_vel*DELTA_T+(0.5)*PAD_HEIGHT <= 400 and paddle1_pos[1]+paddle1_vel*DELTA_T-(0.5)*PAD_HEIGHT >= 0:
        paddle1_pos=[paddle1_pos[0],paddle1_pos[1]+paddle1_vel*DELTA_T]
    if paddle2_pos[1]+paddle2_vel*DELTA_T+(0.5)*PAD_HEIGHT <= 400 and paddle2_pos[1]+paddle2_vel*DELTA_T-(0.5)*PAD_HEIGHT >= 0:
        paddle2_pos=[paddle2_pos[0],paddle2_pos[1]+paddle2_vel*DELTA_T]
    print(paddle1_pos[1])
    
    # draw paddles
    canvas.draw_line((paddle1_pos[0],paddle1_pos[1]+(0.5)*PAD_HEIGHT),(paddle1_pos[0],paddle1_pos[1]-(0.5)*PAD_HEIGHT),PAD_WIDTH,'White')
    canvas.draw_line((paddle2_pos[0],paddle2_pos[1]+(0.5)*PAD_HEIGHT),(paddle2_pos[0],paddle2_pos[1]-(0.5)*PAD_HEIGHT),PAD_WIDTH,'White')
    # determine whether paddle and ball collide    
    
    # draw scores
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = PADDLE_VEL
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel= -PADDLE_VEL
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = PADDLE_VEL
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel= -PADDLE_VEL
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['down'] or key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['s'] or key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
