import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        columns = collections.defaultdict(set)
        square = collections.defaultdict(set)
        for row in range(9):
            for column in range(9):
                num = board[row][column]
                if num == ".":
                    continue
                if num in rows[row] or num in columns[column] or num in square[row//3, column//3]:
                    return False
                columns[column].add(num)
                rows[row].add(num)
                square[row//3, column//3].add(num)
        return True