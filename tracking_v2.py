import random
cars = [1,2,3,4,5,6,7,8,9,10,11,12]

#keep track of distances travled
#inital distance_traveled = [0,0,0,0,0,0]

distance_traveled = [0,0,0,0,0,0,0,0,0,0,0,0]
add_car = 0

def itterate():
    returncar = 0
    while True:
        #chose a random number from cars list
        add_car = random.choice(range(len(cars)))
        distance_traveled[add_car-1] += 1

        if distance_traveled[add_car-1] == 15:
            print_snapshot(distance_traveled)
            returncar = add_car
            cars.pop(add_car-1)
            distance_traveled.pop(add_car-1)
            return returncar



# to add 1 to position 3
def first_place():
    return itterate()


#print(distance_traveled)
# this is for dev - to check who has won


def print_snapshot(mylist):
    counter=1
    for car_distance in mylist:
        print('car {} has moved \n'.format(counter)+"*"*car_distance)
        counter+= 1
    #pass

#----- 2nd place ------
def second_placeeee():
    return itterate()



#---- anouncing the places -----
winner = first_place()
place_2nd = second_placeeee()

print("\n1st place is car {}" .format(winner))
print("\n2nd place is car {}" .format(place_2nd))
