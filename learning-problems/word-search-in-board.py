from typing import List

"""
@problem: Find the given word in the board
@description: There will be an mxn tiles. [m - rows, n - columns]. Each tile will contains a letter.
We can traverse through tiles to create a sequence of letters to form the word given.
If we can form the word return True else False
@example: m = 3, n = 4, Tiles below
 --- --- --- ---
| A | B | C | E |
 --- --- --- ---
| S | F | C | S |
 --- --- --- ---
| A | D | E | E |
 --- --- --- ---
Given word: ABCCE -> Output: True. Because we can form a sequence as below
 --- --- --- ---
| A-|-B-|-C | E |
 --- --- -|- ---
| S | F | C | S |
 --- --- -|- ---
| A | D | E | E |
 --- --- --- ---
"""


class Resolver:

    def __init__(self, board: List[List[str]]):
        self.board = board
        self.rows = len(board)
        self.columns = len(board[0])

    def __find(self, row, col, word: str, letter_index: int, visited: set[tuple[int, int]]) -> bool:
        if (row, col) in visited:
            return False

        if letter_index == len(word):
            return True

        if row + 1 < self.rows and self.board[row + 1][col] == word[letter_index]:
            if self.__find(row + 1, col, word, letter_index + 1,  visited.union({(row, col), })):
                return True

        if row - 1 > -1 and self.board[row - 1][col] == word[letter_index]:
            if self.__find(row - 1, col, word, letter_index + 1, visited.union({(row, col), })):
                return True

        if col + 1 < self.columns and self.board[row][col + 1] == word[letter_index]:
            if self.__find(row, col + 1, word, letter_index + 1,  visited.union({(row, col), })):
                return True

        if col - 1 > -1 and self.board[row][col - 1] == word[letter_index]:
            if self.__find(row, col - 1, word, letter_index + 1,  visited.union({(row, col), })):
                return True

        return False

    def solve(self, word: str) -> bool:
        for row in range(self.rows):
            for col in range(self.columns):
                if word[0] == self.board[row][col] and self.__find(row, col, word, 1, set()):
                    return True
        return False


if __name__ == "__main__":
    print(f'Word exist: {Resolver([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]).solve("ABCCED")}')
    print(f'Word exist: {Resolver([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]).solve("SEE")}')
    print(f'Word exist: {Resolver([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]).solve("ABCB")}')
    print(f'Word exist: {Resolver([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]).solve("ABCESEEEFS")}')
