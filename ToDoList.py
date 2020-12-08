# Isaac Bordfeld and Karley Conroy
# ToDoList

class ToDoList:
    def __init__(self):
        self.ToDo = {}
        self.OpenList()

    # function used to add a new list in the program
    def addParentList(self, ListName):
        self.ToDo[ListName] = list()

    # function used to remove a list from a program
    def removeParentList(self, ListName):
        try: 
            del self.ToDo[ListName]
        except:
            # will print if the list name entered doesnt exist or it is spelt wrong
            print("Not a current list, make sure you have correct spelling and capitalization!")
    
    # function that will add a task to an existing list
    def addToDoList(self, ListName, task):
        self.ToDo.get(ListName).append(task)

    # function that will remove a task from an existing list
    def removeFromToDoList(self, ListName, task):
        try: 
            self.ToDo.get(ListName).remove(task)
        except:
            #will print if the item is not in the list or it is spelt incorrectly
            print("\nItem not found in list! Make sure capitalization is correct!\n")

    #used to save the list
    def SaveLists(self):
        #writes to the text file
        fptr = open("ToDo.txt", "w")

        for listName, task in self.ToDo.items():
            fptr.write(listName + ":")
            run_time = len(task)
            for i in range(run_time - 1):
                fptr.write(task[i] + ",")
            fptr.write(task[-1] + "\n")

        fptr.close()
        print("List saved! Have a good day!")

    # used to open the text file 
    def OpenList(self):
        # will read from the text
        fptr = open("ToDo.txt", "r")

        for ToDo in fptr.readlines():
            tempList = ToDo.split(":")
            tempList = [tempList[0], tempList[1].strip("\n").split(",")]
            self.ToDo[tempList[0]] = tempList[1]

        fptr.close()

    # will print the context of the list 
    def printList(self):
        listString = ""
        for name, listItems in self.ToDo.items():
            listString += name + ":\n"
            for task in listItems:
                listString += f"- {task}\n"
        return listString[:-1]

    def getList(self):
        return self.ToDo
