import random
cars = [1,2,3,4,5,6,7,8,9,10,11,12]





#keep track of distances travled
#inital distance_traveled = [0,0,0,0,0,0]

distance_traveled = [0,0,0,0,0,0,0,0,0,0,0,0]

# to add 1 to position 3
#distance_traveled[add_car] +=1
#print(distance_traveled)

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

print(cars)
print(distance_traveled)
#check who has won


#---- car movements ----

def print_snapshot(mylist):
    counter=1
    for car_distance in mylist:
        print('car {} has moved \n'.format(counter)+"*"*car_distance)
        counter+= 1
    #pass

print_snapshot(distance_traveled)

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

#---- summary of winners -----
print("the winner is car {}" .format(place_1st))
print("the 2nd place car is {}" .format(place_2nd))
print("the 3rd place car is {}" .format(place_3rd))
