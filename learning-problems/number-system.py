from enum import Enum
"""
@problem: Number Systems
@description: Converting one type of number system to another by changing the base
"""


class NumberBase(Enum):
    DECIMAL = 10
    OCTAL = 8
    HEXADECIMAL = 16
    BINARY = 2


class Resolver:

    @staticmethod
    def get_repr(number: int, to_base: NumberBase):
        """
        Returns the representation of "to_base" of a decimal "number"
        :param number: Number the find the representation [Eg, 2 -> 2, 11 -> B]
        :param to_base: Base of the Number System
        :return: Representation of a number
        """
        if to_base == NumberBase.HEXADECIMAL and number > 9:
            return chr(ord('A') + number - 10)
        return str(number)

    @staticmethod
    def get_value(_repr: str, from_base: NumberBase):
        """
        Return the value in decimals of the Representation of different NumberSystems
        :param _repr: Representation of the Number system with base of "from_base"
        :param from_base: Number System base of the Representation
        :return: Value in decimal
        """
        if from_base == NumberBase.HEXADECIMAL and _repr.isalpha():
            return 10 + ord(_repr.upper()) - ord('A')
        return int(_repr)

    @staticmethod
    def convert_decimal(number: int, to_base: NumberBase):
        """
        Helper method to convert the decimal number to the "to_base" NumberSystem
        :param number: Decimal number
        :param to_base: Number System base to convert the number
        :return: converted number in "to_base" Number system
        """
        output = Resolver.get_repr(number % to_base.value, to_base)
        number = number // to_base.value
        while number != 0:
            output = Resolver.get_repr(number % to_base.value, to_base) + output
            number = number // to_base.value
        return output

    @staticmethod
    def convert_to_decimal(number: str, from_base: NumberBase):
        """
        Helper method to convert other number system no to decimal no
        :param number: Representation of a decimal number in "from_base"
        :param from_base: Number System base of the "number"
        :return: Decimal number of the "number"
        """
        if from_base == NumberBase.DECIMAL:
            return int(number)

        number = '#' + number
        result = 0
        digit = 0
        index = -1
        while number[index] != '#':
            result += Resolver.get_value(number[index], from_base) * from_base.value ** digit
            digit += 1
            index -= 1
        return result

    @staticmethod
    def change_base(number: str, from_base: NumberBase, to_base: NumberBase):
        """
        Converts the number from one number system base to another base
        :param number: Number to convert
        :param from_base: Number system base of the "number"
        :param to_base: Number system base of the "number" to convert
        :return: Converted Number in "to_base"
        """
        decimal_number = Resolver.convert_to_decimal(number, from_base)
        return Resolver.convert_decimal(decimal_number, to_base)


if __name__ == '__main__':
    no = 689
    # Decimal Conversions
    decimal_no = Resolver.convert_decimal(no, NumberBase.DECIMAL)
    print(f"Decimal Number of {no} =>", decimal_no)
    print("Reversed to Original =>", Resolver.convert_to_decimal(decimal_no, NumberBase.DECIMAL))
    hexadecimal_no = Resolver.convert_decimal(no, NumberBase.HEXADECIMAL)
    print(f"Hexadecimal Number of {no} =>", hexadecimal_no)
    print("Reversed to Original =>", Resolver.convert_to_decimal(hexadecimal_no, NumberBase.HEXADECIMAL))
    octal_no = Resolver.convert_decimal(no, NumberBase.OCTAL)
    print(f"Octal Number of {no} =>", octal_no)
    print("Reversed to Original =>", Resolver.convert_to_decimal(octal_no, NumberBase.OCTAL))
    binary_no = Resolver.convert_decimal(no, NumberBase.BINARY)
    print(f"Binary Number of {no} =>", binary_no)
    print("Reversed to Original =>", Resolver.convert_to_decimal(binary_no, NumberBase.BINARY))

    # Different Base conversions
    print(f"Converting Binary Number to HexDecimal: "
          f"{binary_no} => {Resolver.change_base(binary_no, NumberBase.BINARY, NumberBase.HEXADECIMAL)}")
    print(f"Converting Octal Number to Binary: "
          f"{octal_no} => {Resolver.change_base(octal_no, NumberBase.OCTAL, NumberBase.BINARY)}")
