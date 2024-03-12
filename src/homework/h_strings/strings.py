def get_hamming_distance(dna1, dna2):
    if len(dna1)==len(dna2):
        hamlength = 0
        for i in range(len(dna1)):
            if(dna1[i] != dna2[i]):
                hamlength += 1
        return hamlength
    else:
        return "Length Mismatch"
def get_dna_complement(dna):
    dnaX = ["X"]*len(dna)
    for i in range(len(dna)):
        if dna[i]=="A":
            dnaX[len(dna)-(1+i)] = "T"
            continue
        elif dna[i]=="T":
            dnaX[len(dna)-(1+i)] = "A"
            continue
        elif dna[i]=="G":
            dnaX[len(dna)-(1+i)] = "C"
            continue
        elif dna[i]=="C":
            dnaX[len(dna)-(1+i)] = "G"
            continue
        else:
            return "Base Mismatch ERROR"
    final = ''.join(dnaX)
    return final