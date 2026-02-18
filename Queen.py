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

def baca(path: str) -> np.ndarray:
    f = open(path, "r", encoding="utf-8")
    lines = []
    for ln in f:
        ln = ln.strip()          
        ln = ln.replace(" ", "") 
        if ln != "":             
            lines.append(ln)

    f.close()

    if len(lines) == 0:
        raise ValueError("Ga ada file")

    n = len(lines)
    i = 0
    while i < n:
        if len(lines[i]) != n:
            raise ValueError("data ndak persegi lo")
        i += 1

    board_list = []
    i = 0
    while i < n:
        row = []
        j = 0
        while j < n:
            row.append(lines[i][j])
            j += 1
        board_list.append(row)
        i += 1

    board = np.array(board_list, dtype="<U1")
    return board

def validasi(board: np.ndarray) -> None:
    if len(board.shape) != 2:
        raise ValueError("2D kan")

    n_baris = board.shape[0]
    n_kolom = board.shape[1]
    if n_baris != n_kolom:
        raise ValueError("Persegi kan")

    n = n_baris

    wilayah = set()
    i = 0
    while i < n:
        j = 0
        while j < n:
            wilayah.add(board[i][j])
            j += 1
        i += 1

    if len(wilayah) != n:
        raise ValueError("Input ndak sama")

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

def solusi(board: np.ndarray, perm: np.ndarray) -> np.ndarray:
    out = board.copy()
    n = len(perm)
    for r in range(n):
        c = perm[r]
        out[r][c] = "#"
    return out

def print_board(board: np.ndarray) -> None:
    for r in range(board.shape[0]):
        print("".join(board[r].tolist()))

def main():
    # sesuai spesifikasi: program memberi arahan pilih file
    path = input("Masukkan path file test case (.txt): ").strip().strip('"').strip("'")

    try:
        board = baca(path)
        validasi(board)
    except Exception as e:
        print(f"Input tidak valid: {e}")
        return

    perm, cases, ms = SolBF(board)
    if perm is None:
        print("Tak ada solusi")
        print(f"Waktunya: {ms:.0f} ms")
        print(f"Jumlah : {cases} kasus")
        return
    solved = solusi(board, perm)
    # Output papan + info seperti contoh
    print_board(solved)
    print()
    print(f"Waktu pencarian: {ms:.0f} ms")
    print(f"Banyak kasus yang ditinjau: {cases} kasus")

    ans = input("Apakah ingin menyimpan solusi? (Ya/Tidak): ").strip().lower()
    if ans in ("ya", "y", "yes"):
        out_path = input("Masukkan nama file output (misal: solusi.txt): ").strip()
        if out_path == "":
            out_path = "solusi.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            for r in range(solved.shape[0]):
                f.write("".join(solved[r].tolist()) + "\n")
            f.write("\n")
            f.write(f"Waktu pencarian: {ms:.0f} ms\n")
            f.write(f"Banyak kasus yang ditinjau: {cases} kasus\n")
        print(f"Solusi disimpan ke: {out_path}")

if __name__ == "__main__":
    main()


