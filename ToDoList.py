# Isaac Bordfeld and Karley Conroy
# ToDoList

class ToDoList:
    def __init__(self):
        self.ToDo = {}
        self.OpenList()

    def addParentList(self, ListName):
        self.ToDo[ListName] = list()

    def removeParentList(self, ListName):
        try: 
            del self.ToDo[ListName]
        except:
            print("Not a current list, make sure you have correct spelling and capitalization!")
    
    def addToDoList(self, ListName, task):
        self.ToDo.get(ListName).append(task)

    def removeFromToDoList(self, ListName, task):
        try: 
            self.ToDo.get(ListName).remove(task)
        except:
            print("\nItem not found in list! Make sure capitalization is correct!\n")

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
        fptr = open("ToDo.txt", "r")

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
