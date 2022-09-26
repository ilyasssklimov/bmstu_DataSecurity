import abc
import os
import config as cfg


class EnigmaAlphabet(metaclass=abc.ABCMeta):
    def __init__(self):
        self._alphabet = ...
        self._rotor_1 = ...
        self._rotor_2 = ...
        self._rotor_3 = ...
        self._reflector = ...

        self._init_alphabet()
        self._init_rotors()
        self._init_reflector()

    @abc.abstractmethod
    def _init_alphabet(self): ...

    @abc.abstractmethod
    def _init_rotors(self): ...

    @abc.abstractmethod
    def _init_reflector(self): ...

    def get_alphabet(self):
        return self._alphabet

    def get_rotor_1(self):
        return self._rotor_1

    def get_rotor_2(self):
        return self._rotor_2

    def get_rotor_3(self):
        return self._rotor_3

    def get_reflector(self):
        return self._reflector


class CharAlphabet(EnigmaAlphabet):
    def _init_alphabet(self):
        with open(os.path.join(cfg.CHAR_DIR, 'alphabet.txt')) as f:
            self._alphabet = f.read().split()

    def _init_rotors(self):
        for i in range(1, 4):
            with open(os.path.join(cfg.CHAR_DIR, f'rotor_{i}.txt')) as f:
                self.__setattr__(f'_rotor_{i}', f.read().split())

    def _init_reflector(self):
        with open(os.path.join(cfg.CHAR_DIR, 'reflector.txt')) as f:
            self._reflector = f.read().split()


class ByteAlphabet(EnigmaAlphabet):
    def _init_alphabet(self):
        pass

    def _init_rotors(self):
        pass

    def _init_reflector(self):
        pass


class Enigma:
    def __init__(self, alphabet: EnigmaAlphabet):
        pass

    def encipher(self, text: str) -> str:
        pass
