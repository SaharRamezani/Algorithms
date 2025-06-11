res = 0
def solve(row, cols, diag1, diag2):
    global res
    if row == 8:
        res += 1
        return
    for col in range(8):
        if not free[row][col]:
            continue
        c_mask = 1 << col
        d1_mask = 1 << (row + col)
        d2_mask = 1 << (row - col + 7)
        if cols & c_mask or diag1 & d1_mask or diag2 & d2_mask:
            continue
        solve(row + 1, cols | c_mask, diag1 | d1_mask, diag2 | d2_mask)

board = [input().strip() for _ in range(8)]
free = [[cell == '.' for cell in row] for row in board]

solve(0, 0, 0, 0)
print(res)