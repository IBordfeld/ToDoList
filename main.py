# Isaac Bordfeld and Karley Conroy
# ToDoList

from ToDoList import ToDoList

class Menu:
    def __init__(self):
        self.MyList = ToDoList()
        self.state = "Start"
        self.current = None # Current name of list user is on

    def showMenu(self):
        menuString = self.StartMenu()
        while 1:
            print(menuString) # Prints menu

            # Takes user input as a string and make sure it's an integer. If user
            # input is not an integer, then allow will be set to False and will rerun menu
            user = input("Select Option: ")
            allow = True 
            try:
                user = int(user)
            except ValueError:
                print("Not a valid option!")
                allow = False
                
            if allow:
                if self.state == "Start":
                    self.current, option = self.findOption(user) # Option that user selected in start menu
                    lengthList = len(self.MyList.getList()) # gets the length of list so we can determine what option was selected
                    
                    # used when a list is selected and then will go to the current state 
                    if option <= lengthList:
                        self.state = "Current"
                        menuString = self.CurrentList(self.current)
                    else:
                        extraOptions = user - lengthList # will find the number that the three extra options are at to access them 
                        if extraOptions == 1:
                            # if the option is equal to 1 it will add a parent list to the program
                            name = input("What would you like to call your new list?: ")
                            self.MyList.addParentList(name) # uses the add function made 
                        elif extraOptions == 2:
                            # if the option is equal to 2  it will remove a parent list
                            name = input("What list would you like to remove?: ")
                            self.MyList.removeParentList(name) # uses the remove function
                        elif extraOptions == 3:
                            # if the option is equal to 3 it will save and exit the program
                            self.MyList.SaveLists()
                            exit() #built in exit program 
                        else:
                            # will go here if the option is not present in the program 
                            print("Not a valid option!")
                        menuString = self.StartMenu() # updates the menu

                elif self.state == "Current":
                    if user == 1:
                        # if the input is one then it will add to the parent list 
                        task = input("What task would you like to add?: ")
                        self.MyList.addToDoList(self.current, task) # adds item to the list 
                        menuString = self.CurrentList(self.current) # the list with the new item
                    elif user == 2:
                        # if the input is two then it will remove from the parent list 
                        task = input("What task would you like to remove?: ")
                        self.MyList.removeFromToDoList(self.current, task) # removes the inputted item
                        menuString = self.CurrentList(self.current) # list without the item
                    elif user == 3:
                        # if the input is three then it will go back to the start menu
                        self.state = "Start" # sets the state
                        menuString = self.StartMenu()
                    else:
                        # if they input an option that is not there it will print this statement 
                        print("Not a valid option!")

    def StartMenu(self):
        # will add the numbers for the options in the program 
        position = 1
        startMenuString = "Your current Lists:\n"

        # for each list it will display a number in front for the user to select
        for ListName, task in self.MyList.getList().items():
            startMenuString += f"{position}. " + ListName + "\n" # format of items in list
            position += 1

        for extraOptions in self.getStateOptions():
            # will add the numbers for the three extra options in the start menu
            startMenuString += f"{position}" + extraOptions + "\n" # format of items in list
            position += 1

        return startMenuString # returns the options

    def CurrentList(self, ListName):
        myListString = f"{ListName}:\n"
        listSelected = self.MyList.getList().get(ListName)

        # displays the contents of the list choosen 
        for task in listSelected:
            myListString += f"- {task} \n" # format of items in list

        position = 1 # Position of extra options on list
        # numbers the extra options for what you can do to a list
        for extraOptions in self.getStateOptions():
            myListString += f"{position}" + extraOptions + "\n" # format of items in list
            position += 1

        return myListString # returns the contents and the new options

    def findOption(self, option):
        optionPosition = 1

        for ListName, task in self.MyList.getList().items():
            if optionPosition == option:
                # Open list that was selected (if one was, other three options could have been selected)
                return ListName, option
            optionPosition += 1

        return "", option

    def getStateOptions(self):
        # the different options that are displayed depending on where you are in the program 
        if self.state == "Start":
            # start menu options
            return [". Add a list", ". Remove a List", ". Save Lists and Exit"]
        else:
            # list menu options 
            return [". Add to list", ". Remove from List", ". Go back to all my lists"]


if __name__ == "__main__":
    test = Menu()
    test.showMenu()
