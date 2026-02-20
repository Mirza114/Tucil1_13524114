import numpy as np

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
        raise ValueError(" Ga ada file")

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

def simpan_file(out_path: str, solved: np.ndarray, ms: float, cases: int):
    with open(out_path, "w", encoding="utf-8") as f:
        for r in range(solved.shape[0]):
            f.write("".join(solved[r].tolist()) + "\n")
        f.write("\n")
        f.write(f"Waktu pencarian: {ms:.0f} ms\n")
        f.write(f"Banyak kasus yang ditinjau: {cases} kasus\n")
