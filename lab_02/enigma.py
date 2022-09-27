from alphabet import EnigmaAlphabet
from rotor import Rotor


class Enigma:
    def __init__(self, alphabet: EnigmaAlphabet):
        self.__alphabet = alphabet
        self.__rotor_0 = Rotor(alphabet, 0)
        self.__rotor_1 = Rotor(alphabet, 1)
        self.__rotor_2 = Rotor(alphabet, 2)

    def encipher(self, target):
        self.__forward(target)

    def __forward(self, target):
        # self.__rotor_0.rotate()
        # self.__rotor_1.rotate()
        element = self.__rotor_0.forward(target, self.__alphabet.get_first_element())
        # element = self.__rotor_1.forward(target, self.__rotor_1.get_current_element())

        print(element)