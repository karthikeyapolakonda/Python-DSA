Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
-> Each row must contain the digits 1-9 without repetition.
-> Each column must contain the digits 1-9 without repetition.
-> Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            seen = set()
            for i in range(len(board)):
                if board[row][i] == '.':
                    continue
                if board[row][i] in seen:
                    return False
                seen.add(board[row][i])
        for col in range(len(board)):
            seen = set()
            for i in range(len(board)):
                if board[i][col] == '.':
                    continue
                if board[i][col] in seen:
                    return False
                seen.add(board[i][col])
        for sq in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (sq//3)*3 + i
                    col = (sq%3)*3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False   
                    seen.add(board[row][col])            
        return True
#or
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        return True




class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate Rows
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
        
        # Validate Cols
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
            
        # Validate Boxes
        starts = [(0, 0), (0, 3), (0, 6),
                  (3, 0), (3, 3), (3, 6),
                  (6, 0), (6, 3), (6, 6)]
        
        for i, j in starts:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        return True

# Time Complexity: O(n^2)
# Space Complexity: O(n)
