# solve.py
import numpy as np
import time

def permut(a: np.ndarray) -> bool:
    i = a.size - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i < 0:
        return False

    j = a.size - 1
    while a[j] <= a[i]:
        j -= 1

    a[i], a[j] = a[j], a[i]
    a[i + 1:] = a[i + 1:][::-1]
    return True

def wilayahyah(perm: np.ndarray, board: np.ndarray) -> bool:
    n = len(perm)
    dipakai = set()

    for r in range(n):
        c = perm[r]
        reg = board[r][c]
        if reg in dipakai:
            return False
        dipakai.add(reg)

    return True

def valadj(perm: np.ndarray) -> bool:
    n = len(perm)

    for r1 in range(n):
        c1 = perm[r1]
        for r2 in range(r1 + 1, n):
            c2 = perm[r2]

            if abs(r1 - r2) <= 1 and abs(c1 - c2) <= 1:
                return False

    return True

import numpy as np
import time

def SolBF(board: np.ndarray):
    n = board.shape[0]
    perm = np.arange(n, dtype=int)
    cases = 0
    t0 = time.perf_counter()
    found = False
    best = None
    while True:
        cases = cases + 1
        if wilayahyah(perm, board) and valadj(perm):
            found = True
            best = perm.copy()
            break
        ok = permut(perm)
        if ok == False:
            break
    t1 = time.perf_counter()
    ms = (t1 - t0) * 1000.0
    if found:
        return best, cases, ms
    else:
        return None, cases, ms
