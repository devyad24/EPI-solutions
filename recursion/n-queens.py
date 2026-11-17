def n_queen(n):
    col = set()
    posDiag = set()
    negDiag = set()

    board = [["."] * n for _ in range(n)]
    result = []

    def solve(r):
        if r == n:
            copy = ["".join(i) for i in board]
            result.append(copy)
            return
        
        for c in range(n):
            if c in col or (r+c) in posDiag or (r-c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r+c)
            negDiag.add(r-c)
            board[r][c] = "Q"

            solve(r+1)

            col.remove(c)
            posDiag.remove(r+c)
            negDiag.remove(r-c)
            board[r][c] = "."

    solve(0)

    return result

print(n_queen(4))


