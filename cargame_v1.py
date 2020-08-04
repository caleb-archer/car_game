'''
Create a race car game with 12 cars
Users chose a car to race with
Users enter a race distance

'''

# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 99), (250, 250),100)
    pygame.draw.circle(screen, (0, 0, 77), (100, 100),50)

    #name = input("What is your name: ")
    #print(name)

    # Flip the display
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()
