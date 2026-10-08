def validate_row(box, row, col, val):
    #we need to check whether for the given row and val in argument is there a duplicate in the same row
    #so if val = 1 and we're in row 1(out of 9), how would we search for the duplicate across the entire row?
    # now we know the box, if box is 4 and row is 3 then we need to start search from 4 - (4 % 3) 

    box_start = box - (box % 3)
    for i in range(box_start, box_start+3):
        for k in range(0, 3):
            if val == board[i][row][k] and k != col:
                return False


def validate_entry(box, row, col):
    for i in range(1,10):
        if validate_row(box, row, i) and validate_col(box, col, i) and validate_box(box, i):
            return i
    return -1

def sudoku_checker(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            for k in range(len(board[k])):
                if board[i][j][k] == 0:
                    value = validate_entry(i,j,k)
                    if value == -1:
                        return False
                    else:
                        #logic for caching the value somewhere

