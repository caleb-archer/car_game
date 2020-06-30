#create an introduction to the game. and ask what car number the user would like to choose.


print("Welcome to my car game! :) simp")
print("_______________________")
level = input('which level would you like to play, easy or difficult?')
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
                print("Please enter a valid car number\nsimp! \nBetween 1 and 12")
                continue
        except ValueError:
            print("Please enter a valid number\nPeasant! This must be a number, please try again")
#run function - call
carcheck("Choose a car number... (1-12)? ", 1 , 12)
