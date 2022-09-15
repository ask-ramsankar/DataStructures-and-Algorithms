"""
@title:     LUHN Checksum Validation
@notice:    Double the odd or even position digits of Identification number
            (if the doubled digit is not a single digit number sum the digits again) and
            find the sum each doubled values.
            If the sum is divisible by 10 it is valid else not
"""


class Resolver:

    def __init__(self, number):
        self.number = number

    @staticmethod
    def doubled_digit(digit: int):
        doubled = digit * 2
        if doubled >= 10:
            doubled = 1 + doubled % 10
        return doubled

    def solve(self):
        odd_pos_checksum = 0
        even_pos_checksum = 0
        current_pos = 0
        for char in self.number:
            if current_pos % 2 == 0:
                odd_pos_checksum += self.doubled_digit(int(char))
            else:
                even_pos_checksum += self.doubled_digit(int(char))

            current_pos += 1

        checksum = odd_pos_checksum
        if current_pos % 2 == 0:
            checksum = even_pos_checksum

        if checksum % 10 == 0:
            return "Valid"
        return "Invalid"


if __name__ == "__main__":
    _number = input("Enter the ID: ")
    if not _number.isnumeric():
        raise Exception("Invalid ID")
    status = Resolver(_number).solve()
    print(f"The ID ({_number}) is {status}")
