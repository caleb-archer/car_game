import random
cars = [1,2,3,4,5,6,7,8,9,10,11,12]





#keep track of distances travled
#inital distance_traveled = [0,0,0,0,0,0]

distance_traveled = [0,0,0,0,0,0,0,0,0,0,0,0]

# to add 1 to position 3
#distance_traveled[add_car] +=1
#print(distance_traveled)

#add_car=""
valid = False
while not valid:
    #chose a random number from cars list
    add_car = random.choice(cars)
    #print(add_car)
    distance_traveled[add_car-1] += 1

    if distance_traveled[add_car-1] == 15:
        #print("yay")
        #print(add_car)
        break

    else:
        continue


#print(distance_traveled)
#check who has won


def print_snapshot(mylist):
    counter=1
    for car_distance in mylist:
        print('car {} has moved \n'.format(counter)+"*"*car_distance)
        counter+= 1
    #pass

print_snapshot(distance_traveled)

print("the winner is car {}" .format(add_car))
