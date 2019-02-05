import pygame
import random


class conjunto():
    def __init__(self):
        pygame.init()
        #COLORS
        black = [0,0,0]
        white = [255,255,255]

        #windows
        #cards will have a resolution of x = 130 and y = 170
        size_x = 1000
        size_y = 800
        size = [size_x, size_y]
        screen = pygame.display.set_mode(size)
        screen.fill(white)
        pygame.display.set_caption("Test 1")

    def graphics(self):
        self.cards_list = ["img\circle\ccgg1.png", "img\circle\ccgg2.png", "img\circle\ccgg3.png", "img\circle\ccgl1.png", "img\circle\ccgl2.png", "img\circle\ccgl3.png", "img\circle\ccgw1.png", "img\circle\ccgw2.png",  "img\circle\ccgw3.png",
                      "img\circle\ccpp1.png", "img\circle\ccpp2.png", "img\circle\ccpp3.png", "img\circle\ccpl1.png", "img\circle\ccpl2.png", "img\circle\ccpl3.png", "img\circle\ccpw1.png", "img\circle\ccpw2.png",  "img\circle\ccpw3.png",
                      "img\circle\ccrr1.png", "img\circle\ccrr2.png", "img\circle\ccrr3.png", "img\circle\ccrl1.png", "img\circle\ccrl2.png", "img\circle\ccrl3.png", "img\circle\ccrw1.png", "img\circle\ccrw2.png",  "img\circle\ccrw3.png",
                      "img\diamon\cdgg1.png", "img\diamon\cdgg2.png", "img\diamon\cdgg3.png", "img\diamon\cdgl1.png", "img\diamon\cdgl2.png", "img\diamon\cdgl3.png", "img\diamon\cdgw1.png", "img\diamon\cdgw2.png",  "img\diamon\cdgw3.png",
                      "img\diamon\cdpp1.png", "img\diamon\cdpp2.png", "img\diamon\cdpp3.png", "img\diamon\cdpl1.png", "img\diamon\cdpl2.png", "img\diamon\cdpl3.png", "img\diamon\cdpw1.png", "img\diamon\cdpw2.png",  "img\diamon\cdpw3.png",
                      "img\diamon\cdrr1.png", "img\diamon\cdrr2.png", "img\diamon\cdrr3.png", "img\diamon\cdrl1.png", "img\diamon\cdrl2.png", "img\diamon\cdrl3.png", "img\diamon\cdrw1.png", "img\diamon\cdrw2.png",  "img\diamon\cdrw3.png",
                      "img\square\csgg1.png", "img\square\csgg2.png", "img\square\csgg3.png", "img\square\csgl1.png", "img\square\csgl2.png", "img\square\csgl3.png", "img\square\csgw1.png", "img\square\csgw2.png",  "img\square\csgw3.png",
                      "img\square\cspp1.png", "img\square\cspp2.png", "img\square\cspp3.png", "img\square\cspl1.png", "img\square\cspl2.png", "img\square\cspl3.png", "img\square\cspw1.png", "img\square\cspw2.png",  "img\square\cspw3.png",
                      "img\square\csrr1.png", "img\square\csrr2.png", "img\square\csrr3.png", "img\square\csrl1.png", "img\square\csrl2.png", "img\square\csrl3.png", "img\square\csrw1.png", "img\square\csrw2.png",  "img\square\csrw3.png"]
              

# POS: X,Y screen.blit(pygame.image.load(list_cards[counter]), cards[i][j])
cards_positions = [[(10, 10), (160, 10), (310, 10)],
                   [(10, 200), (160, 200), (310, 200)],
                   [(10, 390), (160, 390), (310, 390)],
                   [(10, 580), (160, 580), (310, 580)]]

clock = pygame.time.Clock()

#Flags
done = False

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill(white)
    if counter > 1:
        for i in range(len(cards_positions)):
            for j in range(len(cards_positions[0])):
                print("counter: ", counter)
                print("len: ", len(cards_list))
                c = random.randint(0,counter)
                print("card:", c)
                print("             ")
                screen.blit(pygame.image.load(cards_list.pop(c)), cards_positions[i][j])
                counter -= 1 
    
    pygame.draw.rect(screen, white, [pos_x, pos_y, 10, 10])

    pygame.display.flip()

pygame.quit()

"""
    pos_x += speed_x
    pos_y += speed_y

    if (pos_x + 10) > size_x:
        speed_x *=  -1
        speed_y *=  -1
    elif (pos_y + 10) > size_y:
        speed_y *=  -1
        speed_x *=  -1
    elif pos_y < 0:
        speed_x *=  -1
        speed_y *=  -1
    elif pos_x < 0:
        speed_x *=  -1
        speed_y *=  -1
    """
