# Assignment 10.1
# Peter Domis Moutsos
#Aknowledgements
    #Elijah Wilson on medium: https://medium.com/@daetam/class-structure-in-python-297792428ef0
        #got a refresher on how to structure classes

class Coffeemaker:
    #class variable
    power = "off"
    #stores default settings for the program
    def __init__(self):
        self.__water = 2
        self.__beans = "whole"
        self.__heat = 2
        #calculates brew time based on the heat and amount of water
        self.__brewtime = 3 * self.__water - self.__heat
        Coffeemaker.power = "on"

#grinder will be called when the beans are whole
    def grinder(self):
        import time
        if self.__beans == "whole":
            print("Grinding...")
            time.sleep(5)
            print("Done.")
            #changes the value of __beans to ground, so that it may be brewed
            self.__beans = "ground"
            return self.__beans
        elif self.__beans == "ground":
            print("Beans are already ground")
        else:
            print("Invalid bean type")
#once the beans are ground, brew will be called
    def brew(self):

        if self.__beans == "ground" and 0 < self.__water <= 3 and 0 < self.__heat <= 3:
            import time
            steam = ''
            #if the heat value is one, add one steam wisp
            if self.__heat == 1:
                steam = ("     (\n")
            #if heat value is two, add two wisps of steam
            if self.__heat == 2:
                steam = ("   (  (  \n")
            #if heat value is 3, add 3 wisps of steam
            if self.__heat == 3:
                steam = (" (  (  (  \n")
            #This list represents the sides of the cup
            layers = ["|        |\n", "|        |\n","|        |\n","|        |\n"]
            #add the coffee level to the list, based on the water amount
            layers[-self.__water - 1] = "|~~~~~~~~|\n"
            #adds the bottom of the cup
            base = "|________|"
            cup = steam
            #adds the layers n the list under the steam
            for i in layers:
                cup += i
            cup += base
            print("Brewing...")
            #calls brewtime, calculate in __init__
            time.sleep(self.__brewtime)
            print("Done.")
            return cup
        elif self.__beans == "ground":
            print("Beans must be ground before brewing.")
            return None
        elif 1 > self.__water > 3 or 1 > self.__heat > 3:
            print("Heat and water values must be 1, 2 , or 3")
            return None
#set water value
    def set_water(self, water):
        self.__water = water
#return water value
    def get_water(self):
        return self.__water
#set heat leve
    def set_heat(self, heat):
        self.__heat = heat
#return heat level
    def get_heat(self):
        return self.__heat
#set bean type 
    def set_bean(self, bean):
        self.__beans = bean
#get bean type
    def get_bean(self):
        return self.__beans

def main():
    import time
    mrc = Coffeemaker()
    print('Welcome to the Mr. Coffee simulator!\n')
    answer1 = str(input("Would you like to view the current settings? (y/n): "))

    if answer1 == "y":
        #passes values for each parameter into the object
        w = str(mrc.get_water())
        h = str(mrc.get_heat())
        b = mrc.get_bean()
        print("Water(cups) : " + w + "\nHeat level : " + h + "\nBean type : "+ b)
    
    answer2 = str(input("Would you like to change the settings?(y/n): "))

    if answer2 == "y":
        #uses methods to change the data variables of the class
        mrc.set_water(int(input("Enter number of cups of water(1-3): ")))
        mrc.set_heat(int(input("Set heat level (1-3): ")))
        mrc.set_bean(input("Enter bean type ('whole'/'ground'): "))
        water = mrc.get_water()
        heat = mrc.get_heat()
        beannnn = mrc.get_bean()
        if 0 > water > 3 or 0 > heat > 3:
            print("Invalid water or heat level.")
            mrc.set_water(int(input("Enter number of cups of water(1-3): ")))
            mrc.set_heat(int(input("Set heat level (1-3): ")))
        if beannnn != "whole" and beannnn != "ground":
            print("Invalid bean type")
            mrc.set_bean(input("Enter bean type ('whole'/'ground'): "))
#gets the  private bean value, so that it can be used in an if statement
    beanstatus = mrc.get_bean()
#initiates grinder if the beans are whole
    if beanstatus == "whole":
        print("Whole beans must be ground before they can be brewed into coffee.\nInitializing grinder.")
        #grinder converts "whole" to "ground"
        mrc.grinder()
        time.sleep(1)
    
    answer4 = str(input("Begin brew now? (y/n)"))
    if answer4 == "y":
#runs the brew method
        x = mrc.brew()
        print(x)
        time.sleep(1)
        #restarts program if the answer is yes
        answer5 = str(input("Would you like to brew more coffee? (y/n): "))
        if answer5 == "y":
            main()
        elif answer5 == "n":
            print("Thanks for using Mr. Coffee")

    elif answer4 == "n":
        print("Brew cancelled, returning to main menu")
        time.sleep(2)
        main()
        
    
    




if __name__ == "__main__":
    main()

            


    
    
