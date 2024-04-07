def get_students_who_took_prog1_and_prog2(prog1, prog2):
    sameSet = prog1.intersection(prog2)
    return sameSet
def get_students_who_took_prog1_or_prog2(prog1, prog2):
    setA = prog1.difference(prog2) 
    setB = prog2.difference(prog1)
    setC = prog1.intersection(prog2)
    setD = setA|setB|setC
    return setD
def get_students_who_took_prog1_not_prog_2(prog1, prog2):
    setFirst = prog1.difference(prog2)
    return setFirst
def get_students_who_took_prog2_not_prog_1(prog1, prog2):
    setSecond = prog2.difference(prog1)
    return setSecond