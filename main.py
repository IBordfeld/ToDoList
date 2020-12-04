# Isaac Bordfeld and Karley Conroy
# ToDoList

from ToDoList import ToDoList

class Menu:
    def __init__(self):
        self.MyList = ToDoList()
        self.state = "Start"
        self.current = None

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
                    lengthList = len(self.MyList.getList())
                    if option <= lengthList:
                        self.state = "Current"
                        menuString = self.CurrentList(self.current)
                    else:
                        extraOptions = user - lengthList
                        if extraOptions == 1:
                            name = input("What would you like to call your new list?: ")
                            self.MyList.addParentList(name)
                        elif extraOptions == 2:
                            name = input("What list would you like to remove?: ")
                            self.MyList.removeParentList(name)
                        elif extraOptions == 3:
                            self.MyList.SaveLists()
                            exit()
                        else:
                            print("Not a valid option!")
                        menuString = self.StartMenu()

                elif self.state == "Current":
                    if user == 1:
                        task = input("What task would you like to add?: ")
                        self.MyList.addToDoList(self.current, task)
                        menuString = self.CurrentList(self.current)
                    elif user == 2:
                        task = input("What task would you like to remove?: ")
                        self.MyList.removeFromToDoList(self.current, task)
                        menuString = self.CurrentList(self.current)
                    elif user == 3:
                        self.state = "Start"
                        menuString = self.StartMenu()
                    else:
                        print("Not a valid option!")

    def StartMenu(self):
        position = 1
        startMenuString = "Your current Lists:\n"
        for ListName, task in self.MyList.getList().items():
            startMenuString += f"{position}. " + ListName + "\n"
            position += 1

        for extraOptions in self.getStateOptions():
            startMenuString += f"{position}" + extraOptions + "\n"
            position += 1

        return startMenuString

    def CurrentList(self, ListName):
        myListString = f"{ListName}:\n"
        listSelected = self.MyList.getList().get(ListName)
        for task in listSelected:
            myListString += f"- {task} \n"

        position = 1
        for extraOptions in self.getStateOptions():
            myListString += f"{position}" + extraOptions + "\n"
            position += 1

        return myListString

    def findOption(self, option):
        optionPosition = 1
        for ListName, task in self.MyList.getList().items():
            if optionPosition == option:
                # Open list that was selected (if one was, other three options could have been selected)
                return ListName, option
            optionPosition += 1

        return "", option

    def getStateOptions(self):
        if self.state == "Start":
            return [". Add a list", ". Remove a List", ". Save Lists and Exit"]
        else:
            return [". Add to list", ". Remove from List", ". Go back to all my lists"]


if __name__ == "__main__":
    test = Menu()
    test.showMenu()
