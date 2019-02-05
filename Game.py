import Entities as ent
import pygame

class game:
    #This class is the one that allows the entities of the game interact with each.
    def __init__(self):
        self.selectedCardCounter = 0
        self.selectedCardsList = []
        #We create an instance of each of the entities
        self.window = ent.window()
        self.deck_position = [640,190]
        self.deck = ent.deck(self.deck_position)
        self.deck2_position = [640,540]
        self.deck2 = ent.deck(self.deck2_position)
        self.board = ent.board()
        #We add the deck grapichs to the draw list
        self.window.sprites_list.add(self.deck)
        #And we update the screen
        self.window.update()
        #This list will be filled with the cards that has to be drag from the board
        self.drag_cards_list = []
        #This part deal 12 cards to populate the board. Each of the card has a deck deal animation and also creates a instance for each card and it adds them to draw list
        self.deal_cards()
        self.window.update()

    #This method blits a red frame into the cards clicked. Because in the game you can only select 3 cards it only allows to select 3 card, then it removes the frames.
    def select_unselect_cards(self, card):
        cards_trio_selected = False
        #cardsCoordanates = []
        #Checks if the card selected is in the selected cards list. If the card was already selected it does the unselection of the card
        if card in self.selectedCardsList:
            self.selectedCardCounter -= 1
            self.selectedCardsList.remove(card)
            card.selected = False
        #This parts means that the cards that enters is a unselected card. So it does the selections of the card
        else:
            card.selected = True
            self.selectedCardCounter += 1
            self.selectedCardsList.append(card)
            #if we select 3 cards it will run the set rule and it will unselect the cards.
            if self.selectedCardCounter == 3:
                isSet = self.conjunto()
                print("IS SET?:" + str(isSet))
                # if the trio selected is a set, then remove that cards from the board
                if isSet:
                    #Because the position of the cards in the board are in a matrix first we need to get their coordinates
                    cardsCoordanates = self.get_card_coordinates(self.selectedCardsList)
                    #In this matrix each position has the attribute of is a card placed or no (True if a card is placed)
                    #So because we remove cards from the board we have to tell to the board that in those spots there is no cards anymore
                    for x, y in cardsCoordanates:
                        self.board.set_status_false(int(x), int(y))
                    #This method remove do the animation of removing the cards that are set in the board.
                    self.window.drag_cards(self.selectedCardsList, self.deck2_position, self.deck2)
                    #This is the one that deal cards to the correspoding empty fields
                    self.deal_cards()
                self.selectedCardCounter = 0
                self.selectedCardsList = []
                cards_trio_selected = True
        self.window.update()
        #Draw the frame for the selected cards
        for i in self.selectedCardsList:
            if i.selected:
                self.window.screen.blit(i.selected_image, i.position)
        pygame.display.flip()
        return cards_trio_selected

    #This method deal cards. Create cards objects and it use ".card_noPlace" Method to get the spots that doesn't have cards.
    def deal_cards(self):
        for i,j in self.board.card_noPlaced():
            self.board.set_status_true(i, j)
            card_image = self.deck.deal_cards()
            #If we had a image card returned then assign it to a card object.
            if card_image:
                card = ent.card(card_image, self.board.card_positions[i][j][0])
                self.window.deal_animation(card.position, ent.deck([640,190]))
                self.window.sprites_list.add(card)
            else:
                print("No more cards")
        print("cards left: " + str(self.deck.get_numCards()))

    #Returns the cordinates of the cards selected.
    #The board has an attribute that shows if a spot doesn't have a card. For getting this spot we need to know the cordinates in the board from the card selected.
    def get_card_coordinates(self, cardList):
        cards = []
        for i in cardList:
            cards.append([(i.rect.y - 15) / 175, (i.rect.x - 170) / 150])
        return cards

    #This method constructs a list of card selected and throws true if it is a set or false if it isn't a set
    def conjunto(self):
        #checks every attribute of the cards and returns True if the attribute is a set and if the cards is not a set it return False
        def set(list):
            l = []
            for i in list:
                if not(i in l):
                    l.append(i)

            if len(l) == 1 or len(l) == 3:
                return True
            return False

        #create and populate the a list with the card attributes
        cards_attributes_list = []
        for i in self.selectedCardsList:
            cards_attributes_list.append(i.show_attributes())

        #create a variable for every attribute. We use this variables for cheking if it is a set or no
        shapeList = [cards_attributes_list[0][0], cards_attributes_list[1][0], cards_attributes_list[2][0]]
        colorsList = [cards_attributes_list[0][1], cards_attributes_list[1][1], cards_attributes_list[2][1]]
        fillList = [cards_attributes_list[0][2], cards_attributes_list[1][2], cards_attributes_list[2][2]]
        numberList = [str(cards_attributes_list[0][3]), str(cards_attributes_list[1][3]), str(cards_attributes_list[2][3])]

        if set(shapeList) and set(colorsList) and set(fillList) and set(numberList):
            return True
        else:
            return False

if __name__ == "__main__":
    #debbug area
    game = game()
    while True:
        events = game.window.event_handler()
        if events == "Close":
            break
        elif events != [] and events:
            set_flag = game.select_unselect_cards(events[0])
    pygame.quit()

