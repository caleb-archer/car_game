'''
Create a car racer game:
- where the user will chose their car number (from 1 - 12)
- where the user will chose the race distance (from 5 -15)
- where the user will then be asked if they want to start the race
- the game will then use these values to produce a output and a first, second and third place winner
    - this will be obtained by using a random number generator to decide which car moves forwards each time
    - this will be displayed in a list using '*' to indicate each position
    - there will be a sleep function that will act as a delay to imitate that the race is actually happening
    - there will be a function to check if the users car got first, second or third place
- the user will then have the option to chose if they want to repeat the race

Version information:
- this version has a very basic function to produce a winner of the race
    - it will only say who got first place in the race
'''
import random
import time
import sys

MAX_CARS = 12
MIN_CARS = 1

#----- INTRODUCTION -----
print("kia ora\nwelcome to my car game! :) peasant")
print("\n_______________________")


#----- user choice - car number -----
def carcheck (question, min, max):
    #def = define
    # intcheck is the name of my fucntion in python
    # question - will be the question asked to the user
    # low and high boundaries will be set up by the progarmmer
    valid = False
    while not valid:
        try: #try to convet input to interger
            global user_car
            user_car = int(input(question))
            if min<= user_car<=max:
                print('Yay you chose car', user_car)
                # I am happy with the loop
                break
            else: #the number is out of bounds
                print("oi!\npeasant, do what you are told and enter a number between", min, "and", max)
                continue
        except ValueError:
            print("oi!\npeasant, do what you are told and enter a valid car number\nbetween", min, "and", max)
#run function - call
carcheck("Choose a car number...? ", MIN_CARS , MAX_CARS)


print("\n_______________________")

#----- user choice - race distance -----
def discheck (question, min, max):
    #def = define
    # intcheck is the name of my fucntion in python
    # question - will be the question asked to the user
    # low and high boundaries will be set up by the progarmmer
    valid = False
    while not valid:
        try: #try to convet input to interger
            global race_distance
            race_distance = int(input(question))
            if min<= race_distance<=max:
                print('Your race distance is', race_distance, '\nGood Luck peasant')
                # I am happy with the loop
                break
            else: #the number is out of bounds
                print("oi!\npeasant, do what you are told and enter a race distance between 5 and 15")
                continue
        except ValueError:
            print("oi!\npeasant, do what you are told and enter a valid race distance\nbetween 5 and 15")
        #return race_distance
#run function - call
discheck("Choose a race distance... (5-15)? ", 5 , 15)
#race_distance: int=(int(discheck()))




print("\n_______________________")

#----- START RACE -----
cars = [1,2,3,4,5,6,7,8,9,10,11,12]
distance_traveled = [0,0,0,0,0,0,0,0,0,0,0,0]
#keep track of distances travled


#----- 1st place winner -----
#add_car=""
valid = False
while not valid:
    #chose a random number from cars list
    place_1st = random.choice(cars)
    #print(add_car)
    distance_traveled[place_1st-1] += 1

    if distance_traveled[place_1st-1] == 15:
        #print("yay")
        #print(place_1st)
        break
    else:
        continue

#print(cars)
#print(distance_traveled)
# for dev to check who has won for functionality testing


#---- car movements - this is to show user where each car is when a player wins----


def print_snapshot(mylist):
    counter=1
    for car_distance in mylist:
        print('car {} has moved \n'.format(counter)+"*"*car_distance)
        counter+= 1
    #pass

#print_snapshot(distance_traveled)


#---- time delay -----

print("please wait peasant, the race is in progress")
for i in range(race_distance):
    sys.stdout.write(".")
    time.sleep(0.3)

#---- summary of winners -----
print("\n \n")
print_snapshot(distance_traveled)
print("\n_______________________")
print("the winner is car {}" .format(place_1st))

