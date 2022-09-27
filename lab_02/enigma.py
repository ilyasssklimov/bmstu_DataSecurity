from alphabet import EnigmaAlphabet
from reflector import Reflector
from rotor import Rotor


class Enigma:
    def __init__(self, alphabet: EnigmaAlphabet):
        self.__alphabet = alphabet
        self.__rotor_0 = Rotor(alphabet, 0)
        self.__rotor_1 = Rotor(alphabet, 1)
        self.__rotor_2 = Rotor(alphabet, 2)

        self.__reflector = Reflector(alphabet)

    def encipher(self, target):
        self.__rotor_0.rotate()
        self.__rotor_1.rotate()

        element = self.__forward(target)
        # element = self.__backward(element)

    def __forward(self, target):
        element = self.__rotor_0.forward(target, self.__alphabet.get_first_element())
        element = self.__rotor_1.forward(element, self.__rotor_0.get_current_element())
        element = self.__rotor_2.forward(element, self.__rotor_1.get_current_element())
        element = self.__reflector.forward(element, self.__rotor_2.get_current_element())

        print(element)
        return element

    def __backward(self, target):
        print(f'{target = }')
        element_index = self.__reflector.backward(target, self.__rotor_2.get_current_element())
        element_index = self.__rotor_2.backward(element_index, self.__rotor_1.get_current_element())

        element = self.__rotor_0.get_element(element_index)
        print(element)
        return element
