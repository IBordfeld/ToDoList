# Isaac Bordfeld
# ToDoList

class ToDoList:
    def __init__(self, category, listName):
        self.Category = category
        self.Name = listName
        self.ToDo = list()
        self.addToList()

    def updateToDoList(self):
        ...

    def addToList(self, task):
        self.ToDo.append(task)

    def removeFromToDoList(self, task):
        if task in self.ToDo:
            self.ToDo.remove(task)
