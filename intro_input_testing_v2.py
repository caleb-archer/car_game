#create an introduction to the game. and ask what car number the user would like to choose.


print("kia ora\nwelcome to my car game! :) peasant")
print("_______________________")
#level = input('which level would you like to play, easy or difficult?')
def carcheck (question, min, max):
    #def = define
    # intcheck is the name of my fucntion in python
    # question - will be the question asked to the user
    # low and high boundaries will be set up by the progarmmer
    valid = False
    while not valid:
        try: #try to convet input to interger
            initial_car = int(input(question))
            if min<= initial_car<=max:
                print('Yay you chose car', initial_car)
                # I am happy with the loop
                break
            else: #the number is out of bounds
                print("oi!\npeasant, do what you are told and enter a number between 1 and 12")
                continue
        except ValueError:
            print("oi!\npeasant, do what you are told and enter a valid car number\nbetween 1 and 12")
#run function - call
carcheck("Choose a car number... (1-12)? ", 1 , 12)
print("\n_______________________")
#CHOSE RACE DISTANCE
def discheck (question, min, max):
    #def = define
    # intcheck is the name of my fucntion in python
    # question - will be the question asked to the user
    # low and high boundaries will be set up by the progarmmer
    valid = False
    while not valid:
        try: #try to convet input to interger
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
#run function - call
discheck("Choose a race distance... (5-15)? ", 5 , 15)
