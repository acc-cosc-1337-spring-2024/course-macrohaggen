from strings import get_dna_complement
from strings import get_hamming_distance
choice = 0
while choice != 3:
    choice = int(input("1-Hamming Distance\n2-Dna Complement\n3-Exit\n\n2"))
    if choice==1:
        str1 = input("\nEnter First DNA Strand:\n")
        str2 = input("Enter Second DNA Strand\n")
        print(get_hamming_distance(str1, str2),"\n")
        continue
    elif choice==2:
        strA = input("\nEnter DNA Base Strand:\n")
        print(get_dna_complement(strA),"\n")
        continue
    else:
        continue