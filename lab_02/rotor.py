from collections import deque
from copy import copy
from alphabet import EnigmaAlphabet


class Rotor:
    def __init__(self, alphabet: EnigmaAlphabet, number: int):
        self.__alphabet: deque = copy(alphabet.get_alphabet())
        self.__initial_alphabet = copy(self.__alphabet)
        self.__map: deque = alphabet.get_rotor(number)
        self.__position: int = alphabet.get_positions()[number]

    def __get_index(self, element):
        return self.__initial_alphabet.index(element)

    def __get_element(self, index):
        return self.__initial_alphabet[index]

    def rotate(self):
        self.__alphabet.rotate(-1)

    def get_current_element(self) -> int:
        return self.__initial_alphabet[self.__position]

    def forward(self, element, previous_element):
        diff: int = self.__position - self.__get_index(previous_element)
        upd_index: int = (self.__get_index(element) + diff) % len(self.__alphabet)
        print(self.__map)
        print(self.__alphabet)
        print(upd_index)
        return self.__map[upd_index]

    def backward(self):
        pass
