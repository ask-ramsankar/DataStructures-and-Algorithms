from enum import Enum


class NumberBase(Enum):
    DECIMAL = 10
    OCTAL = 8
    HEXADECIMAL = 16
    BINARY = 2


class Resolver:

    @staticmethod
    def get_repr(number: int, base: NumberBase):
        if base == NumberBase.HEXADECIMAL and number > 9:
            return chr(ord('A') + number - 10)
        return str(number)

    @staticmethod
    def get_value(_repr: str, base: NumberBase):
        if base == NumberBase.HEXADECIMAL and _repr.isalpha():
            return 10 + ord(_repr.upper()) - ord('A')
        return int(_repr)

    @staticmethod
    def convert_decimal(number: int, to_base: NumberBase):
        output = Resolver.get_repr(number % to_base.value, to_base)
        number = number // to_base.value
        while number != 0:
            output = Resolver.get_repr(number % to_base.value, to_base) + output
            number = number // to_base.value
        return output

    @staticmethod
    def convert_to_decimal(number: str, from_base: NumberBase):
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
