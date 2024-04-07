from dictionary import add_inventory
from dictionary import remove_inventory_widget
from sets import get_students_who_took_prog1_and_prog2, get_students_who_took_prog1_or_prog2, get_students_who_took_prog1_not_prog_2, get_students_who_took_prog2_not_prog_1
k = 0
prog1 = {"Student1","Student2","Student3"}
prog2 = {"Student3","Student4","Student5"}
while k != 3:
    option = int(input("Inventory Menu (1), Student Menu (2), or Exit (3)?\n"))
    if option == 1:
        i = 0
        while i != 3:
            choice = int(input("Inventory Menu\n1-Add or Update Item\n2-Delete Item\n3-Exit\n"))
            if choice == 1:
                dicted = str(input("Enter dictionary name:\n"))
                widgeting = str(input("Enter widget name:\n"))
                quantity = int(input("Enter quantity:\n"))
                add_inventory(dicted, widgeting, quantity)
                print("Adjusted.\n")
                continue
            elif choice == 2:
                dictName = str(input("Enter dictionary name:\n"))
                widgetName = str(input("Enter widget name:\n"))
                remove_inventory_widget(dictName, widgetName)
                print("Adjusted.\n")
                continue
            elif choice == 3:
                i += 3
            else:
                continue
    elif option == 2:
        j = 0
        while j != 5:
            decision = int(input("Student Menu\n1-Students who took prog1 and prog2\n2-Students who took prog1 or prog2\n3-Students who took prog1 not prog2\n4-Students who took prog2 not prog1\n5-Exit\n")) 
            if decision == 1:
                print(get_students_who_took_prog1_and_prog2(prog1, prog2),"\n")
                continue
            elif decision == 2:
                print(get_students_who_took_prog1_or_prog2(prog1, prog2),"\n")
                continue
            elif decision == 3:
                print(get_students_who_took_prog1_not_prog_2(prog1, prog2),"\n")
                continue
            elif decision == 4:
                print(get_students_who_took_prog2_not_prog_1(prog1, prog2),"\n")
                continue
            elif decision == 5:
                j += 5
            else:
                continue
    elif option == 3:
        k += 3
    else:
        continue