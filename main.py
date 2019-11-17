import pygame   # importing Pygame module
pygame.init()   # initializing pygame

win = pygame.display.set_mode((500, 500))   # seting up the canvas size of the window
pygame.display.set_caption("Sujeet")    # Setting up the caption of the window
# pygame.display.set_icon()

# Declaring some variables
# Setting up the position of the character
x = 50          # character is 50 pixel away from the border of the left canvas (Padding of the object)
y = 50         # character is 50 pixel away from the border of the upper canvas (Padding of the object)
# Setting up the attributes of the character
width = 20      # Character's width is 20 pixel   
height = 20     # Character's height is 20 pixel  
vel = 1        # vel is the velocity so that the character or object can move by 1 pixel

run = True  # created variable for infinite loop
while run:  # creating an infinite loop
    pygame.time.delay(5)    # time delay of the moving character

    for event in pygame.event.get():       # for creating an event so that action can be performed that is clicked by mouse cursor
        if event.type == pygame.QUIT:       # pygame.QUIT is the name of an event which means close button
            run = False     # assigning false so that infinite loop can be stopped (breaked)

    keys = pygame.key.get_pressed()     # it is an event so that action can be performed that is any key is pressed by keyboard

    if keys[pygame.K_d] and x < 500 - width - vel:    # moves to right direction key on keyboard
        x += vel    # increases the position of the character by value of vel variable (increases the padding by val)
    if keys[pygame.K_a] and x > vel:     # moves to left direction key on keyboard
        x -= vel    # decreases the position of the character by value of vel variable (decreases the padding by val)
    if keys[pygame.K_w] and y > vel:       # moves to up direction key on the keyboard
        y -= vel    # decreases the position of the character by value of vel variable (decreases the padding by val)
    if keys[pygame.K_s] and y < 500 - height - vel:     # moves to down direction key on keyboard
        y += vel    # increases the position of the character by value of vel variable (increases the padding by val)
    win.fill((255, 255, 255))   # for setting upt the color of the background (Window)
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))   # for setting up the color of the character
    pygame.display.update()    # to refresh the display
pygame.quit()   # the quit() function closes the window after loop is breaked 