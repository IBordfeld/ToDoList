# Isaac Bordfeld
# ToDoList

class ToDoList:
    def __init__(self):
        self.ToDo = {}
        self.OpenList()

    def addParentList(self, ListName):
        self.ToDo[ListName] = list()

    def removeParentList(self, ListName):
        del self.ToDo[ListName]

    def addToDoList(self, ListName, task):
        self.ToDo.get(ListName).append(task)

    def removeFromToDoList(self, ListName, task):
        self.ToDo.get(ListName).remove(task)

    def SaveLists(self):
        fptr = open("ToDo.txt", "w")

        for listName, task in self.ToDo.items():
            fptr.write(listName + ":")
            run_time = len(task)
            for i in range(run_time - 1):
                fptr.write(task[i] + ",")
            fptr.write(task[-1] + "\n")

        fptr.close()
        print("List saved! Have a good day!")

    def OpenList(self):
        try:
            fptr = open("ToDo.txt", "r")
        except Exception as identifier:
            ...

        for ToDo in fptr.readlines():
            tempList = ToDo.split(":")
            tempList = [tempList[0], tempList[1].strip("\n").split(",")]
            self.ToDo[tempList[0]] = tempList[1]

        fptr.close()

    def printList(self):
        listString = ""
        for name, listItems in self.ToDo.items():
            listString += name + ":\n"
            for task in listItems:
                listString += f"- {task}\n"
        return listString[:-1]

    def getList(self):
        return self.ToDo

"""
Here are your lists
    1. Store
    2. Chores
    3. Remove a list
    4. Add a list
    5. Save List and Exit

SELECTS 1

Store:
    - Eggs
    - Milk
    - Bread
    - Poptarts
    1. Add to list
    2. Remove from List
    3. Go back to all my lists
"""


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
# test.SaveLists()
