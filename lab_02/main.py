from enigma import Enigma
from alphabet import CharAlphabet, ByteAlphabet


def test_char_encipher():
    alphabet = CharAlphabet()
    enigma = Enigma(alphabet)

    text = 'HELLOXBAUMANXMOSCOWXSTATEXTECHNICALXUNIVERSITY'
    print(f'Input text:     \'{text}\'')

    enc_text = enigma.encipher(text)
    print(f'Encrypted text: \'{enc_text}\'')

    dec_text = enigma.encipher(enc_text)
    print(f'Decrypted text: \'{dec_text}\'')


def main():
    test_char_encipher()


if __name__ == '__main__':
    main()
