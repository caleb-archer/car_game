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
- the user will then have the option to chose if they want to restart the entire game

Version information:
- as in previous versions, this version has a function that will produce a first, second and third place winner
- this version has a loop function called restart
    - the loop runs over the whole game
- this version also has a function called start
    - it asks the user if they want to start the race
'''
import random
import time
import sys

#---- VARIABLES -----
MAX_CARS = 12
MIN_CARS = 1

MIN_DIS = 5
MAX_DIS = 15

#---- option for player to restart [loop] -----
restart = True
while restart:

    #----- INTRODUCTION -----
    print("\nkia ora\nwelcome to my car game! :) peasant")
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
                    time.sleep(2)
                    # I am happy with the loop
                    break
                else: #the number is out of bounds
                    print("oi!\npeasant, do what you are told and please enter a car number between", min, "and", max, "\n")
                    time.sleep(2)
                    continue
            except ValueError:
                print("oi!\npeasant, do what you are told and enter a valid car number\nbetween", min, "and", max, "\n")
                time.sleep(2)
    #run function - call
    carcheck("Choose a car number (between {} - {}) ".format(MIN_CARS, MAX_CARS), MIN_CARS , MAX_CARS)


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
                    time.sleep(2)
                    # I am happy with the loop
                    break
                else: #the number is out of bounds
                    print("oi!\npeasant, do what you are told and enter a race distance between", min, "and", max, "\n")
                    time.sleep(2)
                    continue
            except ValueError:
                print("oi!\npeasant, do what you are told and enter a valid race distance\nbetween", min, "and", max, "\n")
                time.sleep(2)
    #run function - call
    discheck("Choose a race distance(between {} - {}) ".format(MIN_DIS, MAX_DIS), MIN_DIS, MAX_DIS)
    #race_distance: int=(int(discheck()))




    print("\n_______________________")

    #----- user choice - is the user ready to start the race? -----
    def start_race (question):
        #def = define
        # levelcheck is the name of my fucntion in python
        # question - will be the question asked to the user
        # low and high boundaries will be set up by the progarmmer
        valid = False
        while not valid:
            yes_no = (input(question))
            if yes_no == "yes":
                    print('Ok, lets start')
                    time.sleep(2.5)
                    # I am happy with the loop
                    break
            else: #the number is out of bounds
                    print("Please enter 'yes' when you want to start, my bro")
                    time.sleep(1)
                    continue
    start_race("Would you like to start? ")

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


    #----- 2nd place winner -----
    #place_2nd=""
    valid = False
    while not valid:
        #chose a random number from cars list
        place_2nd = random.choice(cars)
        #print(add_car)
        distance_traveled[place_2nd-1] += 1

        if distance_traveled[place_2nd-1] == 15:
            #print("yay")
            #print(add_car)
            if place_2nd==place_1st:
                continue
            break
        else:
            continue

    #----- 3rd place winner -----
    #place_3rd=""
    valid = False
    while not valid:
        #chose a random number from cars list
        place_3rd = random.choice(cars)
        #print(add_car)
        distance_traveled[place_3rd-1] += 1

        if distance_traveled[place_3rd-1] == 15:
            #print("yay")
            #print(add_car)
            if place_3rd==place_1st:
                continue
            if place_3rd==place_2nd:
                continue
            break
        else:
            continue

    #---- time delay -----

    print("please wait peasant, the race is in progress")
    for i in range(race_distance*2):
        sys.stdout.write(".")
        time.sleep(0.3)

    #---- summary of winners -----
    print("\n \n")
    print_snapshot(distance_traveled)
    print("\n_______________________")
    print('you chose car {}' .format(user_car))
    time.sleep(1)
    print("the winner is car {}" .format(place_1st))
    time.sleep(1)
    print("the 2nd place car is {}" .format(place_2nd))
    time.sleep(1)
    print("the 3rd place car is {}" .format(place_3rd))


    #---- did the user place or win? -----
    print("\n_______________________")

    valid = False
    while not valid:
        if user_car == place_1st:
            print("Congratulations, you won the race!")
            time.sleep(2)
            break
        elif user_car == place_2nd:
            print("well done, you got second place in the race")
            time.sleep(2)
            break
        elif user_car == place_3rd:
            print("nice try, you got third place in the race")
            time.sleep(2)
            break
        else:
            print("sorry peasant, you didn't score in the race")
            time.sleep(2)
            break


#---- option for player to restart [loop] -----
    print("\n_______________________")
    restart = input("Press any key to restart or q to quit! ")
    if restart == "q":
        restart = False
