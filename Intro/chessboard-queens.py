board = [[x=='*' for x in input()] for _ in range(8)]
cols = [0] * 8
leftDiag = [0] * 15
rightDiag = [0] * 15
count = 0

def findPositions(row):
    global cols, leftDiag, rightDiag, count
    if row==8:
        count += 1
        return
    for col in range(8):
        if cols[col] or leftDiag[row+col] or rightDiag[col-row+7] or board[row][col]:
            continue
        cols[col], leftDiag[row+col], rightDiag[col-row+7], board[row][col] = 1, 1, 1, 1
        findPositions(row+1)
        cols[col], leftDiag[row+col], rightDiag[col-row+7], board[row][col] = 0, 0, 0, 0

findPositions(0)
print(count)

