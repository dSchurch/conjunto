import random
import pygame
import time

class window:
    #This object represents the window of the game. Here we can change the propierties of the window or draw elements into it.
    def __init__(self):
        pygame.init()
        self.colors = {"white":(255,255,255), "black":(0,0,0), "red":(255,0,0), "silver":(229, 242, 255)}
        self.screen = pygame.display.set_mode([800, 920])
        self.screen.fill(self.colors["silver"])

        pygame.display.set_caption("Conjunto 1")

        self.sprites_list = pygame.sprite.Group()
        self.grap_selected_list = []

        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        # This flag will show if it is the first set. His function is to draw a deck when cards are drag from the board
        self.firstSet = False

    #This method see all the elements in the draw list and draw them into the window
    def update(self):
        self.screen.fill(self.colors["silver"])
        self.sprites_list.draw(self.screen)
        pygame.display.flip()

    #This method set the position of the card from the deck to his corresponding place in the board. This algorithm increase the position of the card with the objective of seeing it moving.
    def deal_animation(self, target, obj):
        #self.add_obj_screen(obj)
        self.sprites_list.add(obj)
        if obj.rect.x - target[0] < 0:
            x_inc = 1
        else:
            x_inc = -1
        if obj.rect.y - target[1] < 0:
            y_inc = 1
        else:
            y_inc = -1

        while obj.rect.x != target[0] or obj.rect.y != target[1]:
            if obj.rect.x != target[0]:
                obj.rect.x += x_inc
            if obj.rect.y != target[1]:
                obj.rect.y += y_inc
            self.update()
            #time.sleep(.00008) #debbug time is .008 stagin time is .0011
        self.sprites_list.remove(obj)

    #This method will do the drag animation
    #This method drag the 3 cards selected if this are a set
    def drag_cards(self, objList, target, deck):
        for i in objList:
            if i.rect.x - target[0] < 0:
                x_inc = 1
            else:
                x_inc = -1
            if i.rect.y - target[1] < 0:
                y_inc = 1
            else:
                y_inc = -1
            while i.rect.x != target[0] or i.rect.y != target[1]:
                if i.rect.x != target[0]:
                    i.rect.x += x_inc
                if i.rect.y != target[1]:
                    i.rect.y += y_inc
                self.update()
            if not (self.firstSet):
                self.firstSet = True
                self.sprites_list.add(deck)
            self.sprites_list.remove(i)

    #This method is the one that handle all the events in the window
    def event_handler(self):
        for events in pygame.event.get():
            #It returns the card clicked
            if events.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in self.sprites_list if (s.rect.collidepoint(pos) and type(s).__name__ == "card")]
                return clicked_sprites
            #Close the game if the X is clicked
            elif events.type == pygame.QUIT:
                return "Close"

class card(pygame.sprite.Sprite):
    #this is the object that represents a card model. This card model has Figure,Color, Fill, Number (ex: Circle, Red, Lines, 3). Also it has a position in the board and image with his code
    def __init__(self, image_name, pos):
        super().__init__()
        self.figure = image_name[1]
        self.color = image_name[2]
        self.fill = image_name[3]
        self.number = int(image_name[4])
        self.position = pos
        self.image = pygame.image.load("img\\" + self.figure +  "\\" + image_name + ".png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = self.position[0]
        self.rect.y = self.position[1]
        self.selected = False
        self.selected_image = pygame.image.load("img\sf.png")
    #This method return an array with the propieties of the card.
    def show_attributes(self):
        return [self.figure, self.color, self.fill, self.number]

class deck(pygame.sprite.Sprite):
    #This is a object that represents a deck this contains an array with all the cards (81) and a position where the deck supposed to be.
    def __init__(self, position):
        super().__init__()
        self.cards_list = ["ccgf1", "ccgf2", "ccgf3",
                           "ccgl1", "ccgl2", "ccgl3",
                           "ccgw1", "ccgw2", "ccgw3",
                           "ccpf1", "ccpf2", "ccpf3",
                           "ccpl1", "ccpl2", "ccpl3",
                           "ccpw1", "ccpw2", "ccpw3",
                           "ccrf1", "ccrf2", "ccrf3",
                           "ccrl1", "ccrl2", "ccrl3",
                           "ccrw1", "ccrw2", "ccrw3",
                           "cdgf1", "cdgf2", "cdgf3",
                           "cdgl1", "cdgl2", "cdgl3",
                           "cdgw1", "cdgw2", "cdgw3",
                           "cdpf1", "cdpf2", "cdpf3",
                           "cdpl1", "cdpl2", "cdpl3",
                           "cdpw1", "cdpw2", "cdpw3",
                           "cdrf1", "cdrf2", "cdrf3",
                           "cdrl1", "cdrl2", "cdrl3",
                           "cdrw1", "cdrw2", "cdrw3",
                           "csgf1", "csgf2", "csgf3",
                           "csgl1", "csgl2", "csgl3",
                           "csgw1", "csgw2", "csgw3",
                           "cspf1", "cspf2", "cspf3",
                           "cspl1", "cspl2", "cspl3",
                           "cspw1", "cspw2", "cspw3",
                           "csrf1", "csrf2", "csrf3",
                           "csrl1", "csrl2", "csrl3",
                           "csrw1", "csrw2", "csrw3"]
        self.image = pygame.image.load("img\\"+ "cb" + ".png").convert()
        self.rect = self.image.get_rect()
        self.rect.x = position[0] #x position
        self.rect.y = position[1] #y position

    #This method return a random card from the deack.In this case return a card code, this implies that the numbers of cards in the deck decrease
    def deal_cards(self):
        if len(self.cards_list) <= 0:
            return False
        else:
            rand_card = random.randint(0, len(self.cards_list)- 1)
            return self.cards_list.pop(rand_card)

    #This method returns the number of cards left in the deck
    def get_numCards(self):
        return len(self.cards_list) + 1

class board:
    #Object that represent the board this will have a background color and the positions where the card are placed
    def __init__(self):
        #self.color = [255,255,255] #WHITE
        x_position = 170
        y_position = 15
        self.card_positions = [[[(x_position, y_position), False], [(x_position + 150, y_position), False], [(x_position + 300, y_position), False]],
                              [[(x_position, y_position + 175), False], [(x_position + 150, y_position + 175), False], [(x_position + 300, y_position + 175), False]],
                              [[(x_position, y_position + 350), False], [(x_position + 150, y_position + 350), False], [(x_position + 300, y_position + 350), False]],
                              [[(x_position, y_position + 525), False], [(x_position + 150, y_position + 525), False], [(x_position + 300, y_position + 525), False]],
                              [[(x_position, y_position + 700), False], [(x_position + 150, y_position + 700), False], [(x_position + 300, y_position + 700), False]]]

    #This method return an array with the cordenates of the places that don't have a card placed "TESTED"
    def card_noPlaced(self):
        cards = []
        for i in range(len(self.card_positions)):
            for j in range(len(self.card_positions[i])):
                if self.card_positions[i][j][1] == False:
                    cards.append((i,j))
        if cards == []:
            return False
        return cards

    #Sets the status of the card to false. The status is the one that shows if in that place we have a card
    def set_status_true(self, x, y):
        self.card_positions[x][y][1] = True
    #It does the same that the method above but in this case sets a False
    def set_status_false(self, x, y):
        self.card_positions[x][y][1] = False

    #This method change to True the cordinates of the places that has a card placed this should be use everthing that a card is placed in a positon "NO TESTED"
    def place_card(self, position):
        for i in position:
            self.card_positions[i[0]][i[1]][1] = True
"""
class selector_frame(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = pygame.image.load("img\\" + "sf" + ".png").convert()

        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
"""

if __name__ == "__main__":
    #debbug area
    card = card()
    deck = deck()
    board = board()
    print(board.card_noPlaced())


