import os
import time
#Critter Caretaker
#a virtual pet caretaker

class Critter:
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def face(self):
        if self.mood == "happy":
            print("""
                ^   ^
               \_____/
            """)
        elif self.mood == "okay":
            print("""
                .   .
                _____
            """)
        elif self.mood == "frustrated":
            print("""
                \   /
                .   .
                _____
            """)
        else:
            print("""
                \   /
                .   .
                _____
               |     |
            """)
    @property
    def mood(self): 
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 10 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        response = "I'm " + self.name + " and I feel " + self.mood + " now.\n"
        self.__pass_time()
        return response

    def eat(self, food = 4):
        food = int(input("How many pieces of food would you like to give to your critter?: "))
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()
        return "Buurp! Thanks"

    def play(self, fun = 4):
        fun = int(input("How many minutes would you like to spend playing with your critter?: "))
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()
        return "Whee!"

    def diagnose(self):
        if(self.hunger >= 5):
            diagnosis = "I'm so hungry"
        elif(3 <= self.hunger < 5):
            diagnosis = "I'm pretty hungry"
        elif(1 < self.hunger <= 2):
            diagnosis = "I'm a bit hungry"
        else:
            diagnosis = "I feel fine"

        if(self.boredom >= 5):
            diagnosis += " and I'm so bored"
        elif(3 <= self.boredom < 5):
            diagnosis += " and I'm pretty bored"
        elif(1 < self.boredom <= 2):
            diagnosis += " and I'm a bit bored"
        else:
            diagnosis += ""
        self.__pass_time()
        return diagnosis

def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        os.system('cls')
        crit.face()
        print \
        ("""
        Critter Caretaker

        0 - Quit
        1 - Listen to your Critter
        2 - Feed your Critter
        3 - Play with your Critter
        4 - Diagnose your Critter
        """)
        choice = input("Choice: ")
        print()

        #exit
        if choice == "0":
            print("Good-bye.")
        #listen to your critter
        elif choice == "1":
            print(crit.talk())
            time.sleep(2)
        #feed your critter
        elif choice == "2":
            print(crit.eat())
            time.sleep(2)
        #play with your critter
        elif choice == "3":
            print(crit.play())
            time.sleep(2)
        #diagnose your critter
        elif choice == "4":
            print(crit.diagnose())
            time.sleep(2)
        #some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")
            time.sleep(2)

main()