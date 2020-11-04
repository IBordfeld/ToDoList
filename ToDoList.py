# Isaac Bordfeld
# ToDoList

class ToDoList:
    def __init__(self, category, listName):
        self.Category = category
        self.Name = listName
        self.ToDo = list()

    def addToList(self, task):
        self.ToDo.append(task)

    def removeFromToDoList(self, task):
        if task in self.ToDo:
            self.ToDo.remove(task)

    def print_list(self):
        printed_list = ""
        for item in self.ToDo:
            printed_list += "- {}\n".format(item)
        return printed_list
