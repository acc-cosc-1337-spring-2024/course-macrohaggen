import unittest
from src.homework.h_strings.strings import get_hamming_distance
from src.homework.h_strings.strings import get_dna_complement

class Test_Config(unittest.TestCase):
    
    def test_case():

        if(get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")==7):
            
            if(get_dna_complement("AAAACCCGGT")=="ACCGGGTTTT"):
                return True
            else:
                return False
        else:
            return False
