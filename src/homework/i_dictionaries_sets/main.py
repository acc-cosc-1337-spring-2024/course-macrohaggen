from dictionary import add_inventory
from dictionary import remove_inventory_widget
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