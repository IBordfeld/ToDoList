from ToDoList import ToDoList

# test = ToDoList()
# test.addParentList("Store")
# test.addToDoList("Store", "Eggs")
# test.addToDoList("Store", "Milk")
# test.addToDoList("Store", "Bread")
# test.addToDoList("Store", "Poptarts")
# test.addParentList("Chores")
# test.addToDoList("Chores", "Clean")
# test.addToDoList("Chores", "Pet cat")
# test.addToDoList("Chores", "Cook")
# print(test.printList())
# test.removeFromToDoList("Chores", "Pet cat")
# print(test.printList())

class Menu:
    def __init__(self):
        self.MyList = ToDoList()
        self.state = "Start"

    def showMenu(self):
        menuString = self.StartMenu()
        while 1:
            print(menuString)
            user = int(input("Select Option: "))
            
            if user == 9:
                exit()

            
            if self.state == "Start":
                option = self.findOption(user) # Option that user selected in start menu
                if option >= len(self.MyList.getList()): # If user's option was a list
                    menuString = self.CurrentList(option)
                    self.state = "Current"
                else: # If any of the extra options were selected
                    ...
            elif self.state == "Current":
                ...

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
                return ListName
            optionPosition += 1

        return option

    def findExtraOption(self):
        ...

    def getStateOptions(self):
        if self.state == "Start":
            return [". Add a list", ". Remove a List", ". Save Lists and Exit"]
        else:
            return [". Add to list", ". Remove from List", ". Go back to all my lists"]


test = Menu()
test.MyList.addParentList("Homework")
test.showMenu()
