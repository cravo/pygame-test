import pygame

# First we need to initialise pygame
pygame.init()

# These values set the size of the window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the window, and call it "screen"
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the player, the numbers are x,y,width,height
player = pygame.Rect((300,250,50,50))

# Create a variable to say if the game is running or not
runGame = True

# A game clock, and a variable to tell us how long there was between frames, our frame-rate
clock = pygame.time.Clock()
frameTime = 0

# In our main loop, provided runGame is true, we:
# Process windows events - to handle the player closing the window
# Update the game
# Draw the game
def main_loop():
    while runGame:
        processWindowsEvents()
        calculateFrameTime()
        update()
        draw()

# Here we can handle windows events like closing the window
# Resizing the window etc.
def processWindowsEvents():
    for event in pygame.event.get():
        # If the player closed the window, we quit the game
        if event.type == pygame.QUIT:
            # Note that because 'runGame' is global we need to say that first
            # otherwise we're setting a local variable to False by accident
            global runGame
            runGame = False

# This function calculates the time between frames, in seconds
def calculateFrameTime():
    global clock
    global frameTime
    frameTimeMS = clock.tick(60)
    frameTime = frameTimeMS / 1000.0

# Here is where all our game logic goes
def update():
    keys = pygame.key.get_pressed()
    movePlayer(keys)
    checkForQuit(keys)

def movePlayer(keys):
    # We want the player to move at 100 pixels per second
    # so we multiply 100 by the time between frames
    playerSpeed = 100.0 * frameTime

    if keys[pygame.K_a]:
        player.move_ip(-playerSpeed,0)
    if keys[pygame.K_d]:
        player.move_ip(playerSpeed,0)
    if keys[pygame.K_w]:
        player.move_ip(0,-playerSpeed)
    if keys[pygame.K_s]:
        player.move_ip(0,playerSpeed)

# If the player presses ESCAPE we also want to quit the game
def checkForQuit(keys):
    if keys[pygame.K_ESCAPE]:
        global runGame
        runGame = False

# Here is where all our game drawing goes
def draw():
    clearScreen()
    drawPlayer()
    pygame.display.update()

def clearScreen():
    screen.fill((0,0,0))

def drawPlayer():
    pygame.draw.rect(screen, (255,0,0), player)


main_loop()

pygame.quit()