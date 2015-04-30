rg=range
def moves(m, row, c):
    
    at = set([x for x in m[row]])
    for x in rg(len(m)):
        at.add(m[x][c])
    first_row = (row // 3) * 3
    first_c = (c // 3) * 3
    for x in rg(first_row, first_row + 3):
        for y in rg(first_c, first_c + 3):
            at.add(m[x][y])
    rm = set([x for x in rg(1, 10)])
    av = rm.difference(at)
    return av

def display(m):
    for x in m:
        for y in x:
            print(y,end=" ")
def flatten_count(m, i):
    li = [y for x in m for y in x]
    return li.count(i)
def make_move(m, move, x, y, no):
    m[x][y] = move
    no -= 1
    return no
def undo_move(m, x, y, na):
    m[x][y] = 0
    na += 1
    return na
def _solve(m, na, a):
    if na <= 0:
        return True
    for x in rg(a, len(m)):
        for y in rg(len(m)):
            if m[x][y] == 0:
                t = moves(m, x, y)
                if len(t) == 0:
                    return False
                for move in t:
                    na = make_move(m, move, x, y, na)
                    if _solve(m, na, x):
                        return True
                    na = undo_move(m, x, y, na)
                return False

def solve_game(m):
    nab = flatten_count(m, 0)
    _solve(m, nab, 0)
    display(nab)
for x in rg(int(input())):
    b = [[int(w) for w in input().split() ] for r in rg(9)]
    solve_game(b)