# GCJ 2013 Qualification round problem B https://code.google.com/codejam/contest/2270488/dashboard#s=p1
def get_cases(fo):
    cases = []
    T = int(next(fo))
    for t in range(T):
        case = []
        n, m = map(int, next(fo).split())
        for row in range(n):
            case.append(list(map(int, next(fo).split())))
        cases.append(case)
    return cases

def solve_case(case):
    N = len(case)
    M = len(case[0])
    new = [[100 for i in range(M)] for j in range(N)]
    columns = list(zip(*case))
    for r, row in enumerate(case):
        length = max(row)
        for c, x in enumerate(new[r]):
            if x > length:
                new[r][c] = length
    for c, column in enumerate(columns):
        length = max(column)
        for r in range(len(column)):
            if new[r][c] > length:
                new[r][c] = length
    return new == case

with open('lawnmower.basic.in') as fo:
    cases = get_cases(fo)
    for i, case in enumerate(cases):
        print('Case #{}: {}'.format(i + 1, 'YES' if solve_case(case) else 'NO'))
