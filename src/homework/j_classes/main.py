from class_a import die
intA = 0
classy = die()
while intA != 4:
    intA = int(input('Die Menu\n1 - Roll Die\n2 - Check Die\n3 - Exit\n'))
    if intA == 1:
        classy.roll()
        print("Die Rolled!")
        continue
    elif intA == 2:
        print(classy.get_rolled_value())
        continue
    elif intA == 3:
        intA += 1
    else:
        continue