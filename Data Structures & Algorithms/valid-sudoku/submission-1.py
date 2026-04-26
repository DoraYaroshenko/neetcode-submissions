class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_dict={}
        cols_dict={}
        squares_dict={}
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    if i in rows_dict.keys():
                        if board[i][j] in rows_dict[i]:
                            return False
                        rows_dict[i].add(board[i][j])
                    else:
                        rows_dict[i]=set()
                        rows_dict[i].add(board[i][j])

                    if j in cols_dict.keys():
                        if board[i][j] in cols_dict[j]:
                            return False
                        cols_dict[j].add(board[i][j])
                    else:
                        cols_dict[j]=set()
                        cols_dict[j].add(board[i][j])

                    box_index=(i // 3) * 3 + (j // 3)
                    if box_index in squares_dict.keys():
                        if board[i][j] in squares_dict[box_index]:
                            return False
                        squares_dict[box_index].add(board[i][j])
                    else:
                        squares_dict[box_index]=set()
                        squares_dict[box_index].add(board[i][j])
        return True