import critter
DOG = 1
CAT = 2
RABBIT = 3

def start():
    critterType = int(input("""What type of critter would you like?
                           1 - Dog
                           2 - Cat
                           3 - Rabbit
                           """))
    userCritter = input("What would you like to name your critter? ")
    if critterType == DOG:
        userCritter = critter.Dog(userCritter)
    elif critterType == CAT:
        userCritter = critter.Cat(userCritter)
    if critterType == RABBIT:
        userCritter = critter.Rabbit(userCritter)
    while userCritter.isAlive == True:
        action = input(f"What would you like {userCritter.name} to do? ").lower()
        if action == "eat":
            userCritter.eat(userCritter.name)
        elif action == "sleep":
            userCritter.sleep(userCritter.name)
        elif action == "exercise":
            userCritter.exercise(userCritter.name)
        else:
            print("Please type 'eat', 'sleep', or 'exercise'.")

start()