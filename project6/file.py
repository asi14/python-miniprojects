# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
player_busted=False
outcome = "Game is in progress."
score = 0

#left margin for game text
text_constant = 20

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

wins = 0

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        output = 'Hand Contains '
        for card in self.cards:
            output+=str(card) + ' '
        return output
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        global VALUES
        value=0
        for card in self.cards:
            value+=VALUES[card.rank]
        return value
   
    def draw(self, canvas, pos):
        left_pos = 0
        iet=0
        global card_images
        #add indicator for more cards than 8
        for card in self.cards:
            if iet < 8:
                card.draw(canvas,[left_pos,pos[1]])
                left_pos+=CARD_SIZE[0]
            iet+=1
            
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = [Card(suit,rank) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        card_output = self.cards[len(self.cards)-1]
        self.cards.remove(card_output)
        return card_output
    
    def __str__(self):
        output = 'Deck Contains '
        for card in self.cards:
            output+=str(card) + ' '
        return output



#define event handlers for buttons
def deal():
    global outcome, in_play, CARD_DECK, PLAYER_HAND, DEALER_HAND,player_busted
    
    if in_play == True:
        outcome = "Deck Reshuffled, counts as loss"
    else:
        outcome = "Game is in progress."
    
    #resets deck and hands
    CARD_DECK = Deck()
    PLAYER_HAND = Hand()
    DEALER_HAND = Hand()

    CARD_DECK.shuffle()
    dealer = True
    for i in range(4):
        if dealer:
            DEALER_HAND.add_card(CARD_DECK.deal_card())
            dealer=False
        else:
            PLAYER_HAND.add_card(CARD_DECK.deal_card())
            dealer=True
    in_play = True
    player_busted=False
    

def hit():
    global outcome
    global PLAYER_HAND
    global CARD_DECK
    global player_busted, in_play
    if PLAYER_HAND.get_value() <=21:
        PLAYER_HAND.add_card(CARD_DECK.deal_card())
        outcome = "Game is in progress."
    else:
        outcome = "Player has Busted. Player loses."
        player_busted = True
        in_play = False
def stand():
    global player_busted, DEALER_HAND, CARD_DECK, in_play, outcome,wins
    if player_busted == True:
        outcome = 'Reminder: Player Busted. Player lost.'
    else:
        while DEALER_HAND.get_value() <= 16:
            DEALER_HAND.add_card(CARD_DECK.deal_card())
        if DEALER_HAND.get_value() >21: #dealer value more than 21
            outcome = 'The Dealer has Busted. Player wins.'
            wins+=1
        elif PLAYER_HAND.get_value() > DEALER_HAND.get_value():
            outcome = 'Player has higher value. Player wins'
            wins+=1
        else:
            outcome = 'Dealer has higher value. Dealer wins.'
    in_play = False
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global text_constant,outcome, in_play,card_back,CARD_BACK_CENTER,CARD_BACK_SIZE
    PLAYER_HAND.draw(canvas,[0,0])
    DEALER_HAND.draw(canvas,[0,600-CARD_SIZE[1]])
    canvas.draw_text("Blackjack",[text_constant,250],50,"Black")
    canvas.draw_text("Brian Lee, CAEN Python Project No. 7",[text_constant,280],25,"Black")
    canvas.draw_text("Number of Cards: %s" % len(PLAYER_HAND.cards),[text_constant,125],20,"Black")
    canvas.draw_text("Number of Cards: %s" % len(DEALER_HAND.cards),[text_constant,480],20,"Black")
    canvas.draw_text("Card Value: %s" % PLAYER_HAND.get_value(),[text_constant,150],20,"Black")
    canvas.draw_text("Card Value: %s" % DEALER_HAND.get_value(),[text_constant,455],20,"Black")
    canvas.draw_text("PLAYER", [450,137],35,"Black")
    canvas.draw_text("DEALER", [450,463],35,"Black")
    canvas.draw_text(outcome,[text_constant,310],25,"Black")
    canvas.draw_text("Player Wins: %s" % wins, [text_constant,340],25,"Black")
    if in_play == True:
        canvas.draw_image(card_back,CARD_BACK_CENTER,CARD_BACK_SIZE,(36,552),(CARD_SIZE))

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

CARD_DECK = Deck()
PLAYER_HAND = Hand()
DEALER_HAND = Hand()

# get things rolling
deal()
frame.start()


# remember to review the gradic rubric