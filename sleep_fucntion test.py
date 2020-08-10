import time
import sys

restart = True
while restart:

    print("hello, how are you today")

    for i in range(8):
        sys.stdout.write(".")
        time.sleep(0.3)

    print("\nthats very good to hear")

    print("hello")

    #x = "....."
    #for i in range(10):
        #print(x)
       # time.sleep(4)
        #x += x


    restart = input("Press any key to restart or q to quit!")
    if restart == "q":
        restart = False
