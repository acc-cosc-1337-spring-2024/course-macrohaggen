from homework.j_classes.class_a import die
def testhaven():
    die.roll
    if die.get_rolled_value != 0:
        die.roll
        if die.get_rolled_value != 0:
            die.roll
            if die.get_rolled_value != 0:
                return True
    else:
        return False