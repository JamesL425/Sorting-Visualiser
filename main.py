import pygame, time, random, sorts
pygame.init()
#settings (can be changed)
WIDTH, HEIGHT = 900, 600
FPS = 60
WHITE = (250,250,250)
BLACK = (150,25,25)
STEP = 0.03
FONT = pygame.font.SysFont("comic sans", 150)
BUTTON_WIDTH, BUTTON_HEIGHT = 350, 100
#makes screen and caption
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Sorting Visualiser")

def generateRandomList(n, lim):
    """generates a random list
    """
    lst = []
    for i in range(n):
        lst.append(random.randint(1,lim))
    return lst

class Button:
    def __init__(self, txt, rect, x, y, func):
        """Assigns text and hitbox (rect)
        x and y and function of button (func).
        """
        self.txt = txt
        self.rect = rect #hitbox
        
        #x and y position here for reference when writing the text
        self.x = x
        self.y = y
        
        #size
        self.width = 60
        self.height = 30

        self.func = func #function of button

    def draw_button(self):
        """Makes button text, then draws it.
        """
        #pygame.draw.rect(WIN, (50,90,0), self.rect) #turn on to check the hitbox
        draw_txt = FONT.render(self.txt, 1, WHITE)
        WIN.blit(draw_txt, (self.x, self.y))

def make_buttons():
    buttons = []
    buttons.append(Button("Bubble", pygame.Rect((WIDTH//2)-BUTTON_WIDTH//2,100-BUTTON_HEIGHT//2,BUTTON_WIDTH,BUTTON_HEIGHT),(WIDTH//2)-BUTTON_WIDTH//2,100-BUTTON_HEIGHT//2,sorts.bubbleSort))
    buttons.append(Button("Insertion", pygame.Rect((WIDTH//2)-500//2,300-BUTTON_HEIGHT//2,500,BUTTON_HEIGHT),(WIDTH//2)-500//2,300-BUTTON_HEIGHT//2,sorts.insertionSort))
    buttons.append(Button("Selection", pygame.Rect((WIDTH//2)-500//2,500-BUTTON_HEIGHT//2,500,BUTTON_HEIGHT),(WIDTH//2)-500//2,500-BUTTON_HEIGHT//2,sorts.selectionSort))
    return buttons
def draw_menu(buttons):
    """Draws background then draws all buttons on top (using button.draw_button()).
    """
    WIN.fill(BLACK)
    
    #draws each button
    for button in buttons:
        button.draw_button()

    #refreshes display
    pygame.display.flip()

class Sort:
    """Takes a sorting algorithm from sorts.py and gets an object from running the function on an array (using yields)
    """
    def __init__(self, sort, arr):
        self.arr = arr
        self.size = len(arr)
        self.sort_object = sort(arr)

    def display(self):
        interval = WIDTH//self.size
        for state in self.sort_object:
            WIN.fill(BLACK)
            for n in range(self.size):
                pygame.draw.rect(WIN, WHITE, (n*interval, 0, interval, 6*state[n] ), 0)
            pygame.display.flip()
            time.sleep(STEP)
        time.sleep(1)
        
def main_menu():
    """Main function (everything runs from this function)
    when mousebutton1 is pressed, it gets pos (mouse position)
    and runs the button's function. 
    """
    #when run is false, the game ends
    run = True

    #makes buttons
    buttons = make_buttons()
    
    #assigns clock for later
    clock = pygame.time.Clock()


    #main game loop
    while run:
        for event in pygame.event.get():
            
            #if tab is closed, game ends (a safety feature)
            if event.type == pygame.QUIT:
                run = False

            #if mouse button is pressed
            if event.type == pygame.MOUSEBUTTONDOWN:

                #gets mouse position
                pos = pygame.mouse.get_pos()

                #iterating through buttons, then if one is where mouse position is, it does button.func
                for button in buttons:

                    if button.rect.collidepoint(pos):

                        xSort = Sort(button.func, generateRandomList(50,100))
                        xSort.display()

                        
        
        #draws the menu every frame
        draw_menu(buttons)

        #sets fps
        clock.tick(FPS)

        

    #closes the pygame engine    
    pygame.quit()

#safety feature: only runs if this is the file that is being run
if __name__ == "__main__":
    main_menu()


            
            


