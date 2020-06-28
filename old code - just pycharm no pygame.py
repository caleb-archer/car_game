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

#print("traveled")
