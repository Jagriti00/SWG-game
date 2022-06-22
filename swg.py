import random
print("Welcome to the SNAKE WATER GUN game")
inpName = input("Enter Your Name: ")
itemList = ["Snake", "Water", "Gun"]
numberTry = 10

while True:

    selectName = input("Please Select From (Snake, Water, Gun): ")
    if selectName == "Snake":
        a = random.choice(itemList)
        print(a)
        numberTry -= 1
        print("Try Left : ", numberTry)

    elif numberTry == 1:
        if selectName >= random.choice(itemList):
            print("Hurray!, ",inpName, " Is the Winner")
            exit()
        else:
            print("Computer is the Winner")
        print("Game Over !")
        break

    elif selectName == "Water":
        a = random.choice(itemList)
        print(a)
        numberTry -= 1
        print("Try Left : ", numberTry)

    elif selectName == "Gun":
        a = random.choice(itemList)
        print(a)
        numberTry -= 1
        print("Try Left : ", numberTry)

    else:
        print("Invalid Selection")
