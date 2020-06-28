'''
Create a race car game with 6 cars
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



#have the user chose a race distance
print('Welcome to the race!')

#create a list of cars
cars = ['bob', 'ancarr', 'carcar', 'dave', 'nocarcar','teslacar' ]
for car in cars:
    print(car)

#keep track of distances travled
#inital distance_traveled = [0,0,0,0,0,0]

distance_traveled = [1, 2, 4, 0, 6, 9]

distance_traveled = [2, 4, 8, 4, 8, 10]

def print_snapshot(mylist):
    counter=1
    for car_distance in mylist:
        print('car {} has moved \n'.format(counter)+"*"*car_distance)
        counter+= 1
    #pass

print_snapshot(distance_traveled)
drawText('traveled', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3)+30)

#pygame.print("traveled")


# Done! Time to quit.
pygame.quit()
