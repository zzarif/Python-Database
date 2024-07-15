from collections import defaultdict


class Solution:
    def isValidSudoku(self, board):
        # dictionary of sets
        dict_rows = defaultdict(set) # makes sure no duplicate in rows
        dict_cols = defaultdict(set) # makes sure no duplicate in cols
        dict_squares = defaultdict(set) # makes sure no duplicate in squares

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                elif (
                    board[i][j] in dict_rows[i] # check duplicate in row hash set
                 or board[i][j] in dict_cols[j] # check duplicate in col hash set
                 or board[i][j] in dict_squares[(i // 3, j // 3)] # check duplicate in squares hash set
                ):
                    return False
                
                # all rule OK, add unique element in hash set
                dict_rows[i].add(board[i][j])
                dict_cols[j].add(board[i][j])
                dict_squares[(i // 3, j // 3)].add(board[i][j])

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isValidSudoku([["5","3",".",".","7",".",".",".","."]
                                 ,["6",".",".","1","9","5",".",".","."]
                                 ,[".","9","8",".",".",".",".","6","."]
                                 ,["8",".",".",".","6",".",".",".","3"]
                                 ,["4",".",".","8",".","3",".",".","1"]
                                 ,["7",".",".",".","2",".",".",".","6"]
                                 ,[".","6",".",".",".",".","2","8","."]
                                 ,[".",".",".","4","1","9",".",".","5"]
                                 ,[".",".",".",".","8",".",".","7","9"]]))
