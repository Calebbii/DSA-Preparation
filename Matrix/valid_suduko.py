def is_valid_sudoku(board):
    seen = set()
    
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                row_key = f"row {i} {board[i][j]}"
                col_key = f"col {j} {board[i][j]}"
                box_key = f"box {i//3} {j//3} {board[i][j]}"
                
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
    
    return True