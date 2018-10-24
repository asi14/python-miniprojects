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
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

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
        pass	# draw a hand on the canvas, use the draw method for cards
        
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
    global outcome, in_play, CARD_DECK, PLAYER_HAND, DEALER_HAND

    CARD_DECK.shuffle()
    dealer = True
    for i in range(4):
        if dealer:
            DEALER_HAND.add_card(CARD_DECK.deal_card())
            dealer=False
        else:
            PLAYER_HAND.add_card(CARD_DECK.deal_card())
            dealer=True
    print('PLAYER HAND: \n' +str(len(PLAYER_HAND.cards)))
    print('DEALER_HAND: \n' +str(len(DEALER_HAND.cards)))
    in_play = True

def hit():
    global PLAYER_HAND
    global CARD_DECK
    global player_busted
    if PLAYER_HAND.get_value() <=21:
        PLAYER_HAND.add_card(CARD_DECK.deal_card())
        print('PLAYER HAND: \n' +str(len(PLAYER_HAND.cards)))
    else:
        print("You have Busted")
        player_busted = True
def stand():
    global player_busted, DEALER_HAND, CARD_DECK
    if player_busted == True:
        print('Reminder: You have Busted')
    else:
        while DEALER_HAND.get_value() <= 16:
            DEALER_HAND.add_card(CARD_DECK.deal_card())
            print('DEALDER HAND: ' + str(DEALER_HAND.get_value()))
    print('PLAYER HAND: ' + str(PLAYER_HAND.get_value()))
    print('DEALDER HAND: ' + str(DEALER_HAND.get_value()))
    if PLAYER_HAND.get_value() <= DEALER_HAND.get_value():
        print('You Lose')
    else:
        print('You Win')
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    
    card = Card("S", "A")
    card.draw(canvas, [300, 300])


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