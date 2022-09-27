from enigma import Enigma
from alphabet import CharAlphabet, ByteAlphabet


def main():
    alphabet = CharAlphabet()
    enigma = Enigma(alphabet)

    text = 'A'
    enc_text = enigma.encipher(text)
    print(enc_text)


if __name__ == '__main__':
    main()
