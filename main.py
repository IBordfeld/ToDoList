import tkinter as tk
import ToDoList


def menu():
    menu_selector = ""
    test = ToDoList.ToDoList("home", "Groceries")
    test.addToList("Milk")
    test.addToList("cookies")
    test.addToList("cake")
    while menu_selector is not "q":
        menu_selector = input("Option: ")
        if menu_selector == "1":
            print(test.print_list)


if __name__ == '__main__':
    menu()
