import random
import sys
print("Welcome to the SNAKE WATER GUN game")
inpName = input("Enter Your Name: ")
itemList = ["snake", "water", "gun"]


def Winner():
    print(a)
    print("Hurray!, ",inpName, " Is the Winner")
    sys.exit()

def game():
    # Changed from while loop to for loop and reverse counting
    for numberTry in range(9, 0, -1):

        def tryleft():
            print("Try Left : ", numberTry)

        selectName = str(input("Please Select From (Snake, Water, Gun): "))
        global a
        a = random.choice(itemList)
        selectName = selectName.lower()
        # a = "water"

        if selectName == "snake":
            if a == "water":
                Winner()
            else: 
                print(a)
                tryleft()

        elif selectName == "water":
            if a == "gun":
                Winner()
            else: 
                print(a)
                tryleft()

        elif selectName == "gun":
            if a == "snake":
                Winner()
            else: 
                print(a)
                tryleft()
        
        else :
            print("Invalid Selection")

if __name__=="__main__":
    game()