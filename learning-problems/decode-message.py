"""
@problem: Decode the message from the sequence of comma separated integers
@description: The sequence of integers will be provided. Each integer represents a char from the message.
There are totally three possible letters. They are Upper Case Alphabets, Lower Case Alphabets, and Punctuations.
The modulo value of the integer represents the character as follows.
A -> 1, B -> 2, C -> 3, D -> 4, ...... , Z -> 26
a -> 1, b -> 2, c -> 3, d -> 4, ...... , z -> 26
! -> 1, ? -> 2, "," -> 3, "." -> 4, " "(space) -> 5, ; -> 6," -> 7, "'" -> 8 [Only 8 available]
If the modulo is 0 change the mode. Upper -> Lower -> Punctuation -> Upper
The mode always starts with the Upper Case Alphabets.
"""


class Modes:
    UPPER = 0
    LOWER = 1
    PUNCTUATION = 2


# Defined values of punctuations
PUNCTUATIONS = {
    1: '!',
    2: '?',
    3: ',',
    4: '.',
    5: ' ',
    6: ';',
    7: '"',
    8: "'",
}


class Resolver:

    def __init__(self, encoded_sequence):
        self.encoded_sequence = encoded_sequence
        self.mode = Modes.UPPER
        self.mode_divisor = 27

    @staticmethod
    def get_punctuation(value: int):
        return PUNCTUATIONS[value]

    def __change_mode(self):
        if self.mode == Modes.UPPER:
            self.mode = Modes.LOWER
            self.mode_divisor = 27
        elif self.mode == Modes.LOWER:
            self.mode = Modes.PUNCTUATION
            self.mode_divisor = 9
        else:
            self.mode = Modes.UPPER
            self.mode_divisor = 27

    def __find_char(self, integer: int):
        modulo_value = integer % self.mode_divisor
        if modulo_value == 0:
            self.__change_mode()
            return ''

        if self.mode == Modes.UPPER:
            return chr(ord('A') + modulo_value - 1)
        elif self.mode == Modes.LOWER:
            return chr(ord('a') + modulo_value - 1)
        else:
            return self.get_punctuation(modulo_value)

    def solve(self):
        output = ''
        for value in self.encoded_sequence:
            output += self.__find_char(int(value))
        return output


if __name__ == "__main__":
    input_1 = '18,12312,171,763,98423,1208,216,11,500,18,241,0,32,20620,27,10'
    print('Encoded Message:', input_1)
    input_1 = map(int, input_1.split(','))
    print('Decoded Message:', Resolver(input_1).solve())
