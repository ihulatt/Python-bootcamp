import time
class Critter:
    def __init__(self, name):
        self.name = name
        self.foodQuantity = 5
        self.isAlive = True
        self.tiredness = 5
        self.fitness = 1

    def eat(self, name):
        print(f"{name} is eating ...")
        self.foodQuantity += 5
        self.tiredness += 1
        if self.foodQuantity >= 10:
            self.__die(name, "overeating")
        if self.tiredness >= 10:
            self.__die(name, "fatigue")

    def sleep(self, name):
        print(f"{name} is sleeping...")
        for sleep in range(5):
            print("Zzz...")
            time.sleep(1)
        self.foodQuantity -= 1
        self.tiredness -= 3
        if self.foodQuantity <= 0:
            self.__die(name, "hunger")

    def exercise(self, name):
        print(f"{name} is exercising...")
        self.foodQuantity -= 2
        self.tiredness += 2
        self.fitness += 1
        if self.foodQuantity <= 0:
            self.__die(name, "hunger")
        if self.tiredness >= 10:
            self.__die(name, "fatigue")
        if self.fitness == 10:
            self.__win(name)

    def __die(self, name, death):
        print(f"{name} died from {death}.")
        self.isAlive = False
    
    def __win(self, name):
        print(f"Well done! {name} has grown up to be fit and strong!")
        self.isAlive = False


class Dog (Critter):
    pass
class Cat (Critter):
    pass
class Rabbit (Critter):
    pass


