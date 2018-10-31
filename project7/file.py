# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
DELTA_T=0.01
ANGLE_VELOC = math.pi/75
ACC=150
MISSILE_AGE=75

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# alternative upbeat soundtrack by composer and former IIPP student Emiel Stopler
# please do not redistribute without permission from Emiel at http://www.filmcomposer.nl
#soundtrack = simplegui.load_sound("https://storage.googleapis.com/codeskulptor-assets/ricerocks_theme.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)



# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.missiles = []
        
    def draw(self,canvas):
        if self.thrust:
            canvas.draw_image(ship_image,[ship_info.get_center()[0]+90,45],ship_info.get_size(),self.pos,self.image_size,self.angle)
        else:
            canvas.draw_image(ship_image,ship_info.get_center(),ship_info.get_size(),self.pos,self.image_size,self.angle)
        
    def update(self):
        global DELTA_T, ACC, ship_thrust_sound
        
        #update position
        if self.pos[0]-self.radius < WIDTH and self.pos[0] + self.radius > 0 and self.pos[1] - self.radius < HEIGHT and self.pos[1] + self.radius > 0:
            self.pos = [self.pos[0]+self.vel[0]*DELTA_T,self.pos[1]+self.vel[1]*DELTA_T]
        else:
            self.pos = [self.pos[0]%800, self.pos[1]%600]
        if self.thrust:
            #update velocity
            angles = angle_to_vector(self.angle)
            self.vel = [self.vel[0]+ACC*angles[0]*DELTA_T,self.vel[1]+ACC*angles[1]*DELTA_T]
            ship_thrust_sound.play()
        else: #friction to bring ship to zero when ship is not thrusting
            self.vel = [self.vel[0]*0.98,self.vel[1]*0.98]
            ship_thrust_sound.pause()
            ship_thrust_sound.rewind()
        self.angle+=self.angle_vel
    def change_angle(self,multiple):
        global ANGLE_VELOC
        self.angle_vel = multiple * ANGLE_VELOC
    def change_thrust(self,thrust):
        self.thrust = thrust
        
    def shoot(self):
        global missile_sound
        self.missiles.append(Sprite(self.pos, [500*math.cos(self.angle),500*math.sin(self.angle)], self.angle, 0, missile_image, missile_info,missile_sound))
        print('bam!')
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        self.isCollided=False #each astroied is by default not collided
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image,self.image_center,self.image_size, self.pos, self.image_size, self.angle )
    
    def update(self):
        global DELTA_T, ANGLE_VELOC
        if self.pos[0]-self.radius < WIDTH and self.pos[0] + self.radius > 0 and self.pos[1] - self.radius < HEIGHT and self.pos[1] + self.radius > 0:
            self.pos = [self.pos[0]+self.vel[0]*DELTA_T,self.pos[1]+self.vel[1]*DELTA_T]
        else:
            self.pos = [self.pos[0]%800, self.pos[1]%600]        
        self.pos = [self.pos[0]+self.vel[0]*DELTA_T,self.pos[1]+self.vel[1]*DELTA_T]
        self.angle+=self.angle_vel*DELTA_T
        self.age+=1
    def collide(self,other_object):
        range_x = [self.pos[0]-self.radius,self.pos[0]+self.radius]
        range_y = [self.pos[1]-self.radius,self.pos[1]+self.radius]
        if other_object.pos[0] > range_x[0] and other_object.pos[0] < range_x[1] and other_object.pos[1] > range_y[0] and other_object.pos[1] < range_y[1]:
            self.isCollided=True #used to check if astroid is collided and is ignored later
            return True
        self.isCollided=False
        return False

def group_collide(sprite_list, other_object):
    for sprite in sprite_list:
        if sprite.isCollided==False and sprite.collide(other_object)==True: #ignores if isCollided already true
            return True
    return False
           
def draw(canvas):
    global time,lives,score,WIDTH, a_rock, MISSILE_AGE
    
    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))

    # draw ship and sprites
    my_ship.draw(canvas)
    for rock in a_rock:
        if rock.isCollided == False: rock.draw(canvas)
    #a_rock.draw(canvas)
    for missile in my_ship.missiles:
        if missile.age < MISSILE_AGE: missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    for rock in a_rock:
        if rock.isCollided == False: rock.update()
    for missile in my_ship.missiles:
        if missile.age < MISSILE_AGE: missile.update()
        
    #collision checks
    if group_collide(a_rock,my_ship)==True:
        lives-=1
    
    canvas.draw_text("Lives: %s" %lives, [20,20],20,"White")
    canvas.draw_text("Score: %s" %score, [WIDTH-80,20],20,"White")
            
# timer handler that spawns a rock    
#calls 3 every tick, which triggers every 5 seconds
def rock_spawner():
    global a_rock
    #a_rock = Sprite([random.randint(0,WIDTH),random.randint(0,HEIGHT)], [random.randint(-100,100), random.randint(-100,100)], random.randint(0,2*3), 0, asteroid_image, asteroid_info)
    for i in range(3):
        a_rock.append(Sprite([random.randint(0,WIDTH),random.randint(0,HEIGHT)], [random.randint(-50,50), random.randint(-50,50)], random.randint(-6,2*3), random.randint(-6,2*3), asteroid_image, asteroid_info))
    print('test')

def keydown_handler(key):
    if key == simplegui.KEY_MAP['right']:
        my_ship.change_angle(1)
    elif key == simplegui.KEY_MAP['left']:
        my_ship.change_angle(-1)
    elif key == simplegui.KEY_MAP['up']:
        my_ship.change_thrust(True)
    elif key == simplegui.KEY_MAP['space']:
        my_ship.shoot()

def keyup_handler(key):
    if key == simplegui.KEY_MAP['right'] or key == simplegui.KEY_MAP['left']:
        my_ship.change_angle(0)
    elif key == simplegui.KEY_MAP['up']:
        my_ship.change_thrust(False)
        
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
#a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [50, 2], 0, 0, asteroid_image, asteroid_info)
a_rock = []
#a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown_handler)
frame.set_keyup_handler(keyup_handler)
timer = simplegui.create_timer(5000.0, rock_spawner) #increased time to make life easier for playyer
rock_spawner() #gets rocks on the canvas immediately
# get things rolling
timer.start()
frame.start()