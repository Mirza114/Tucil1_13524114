from game import baca, validasi, solusi, print_board, simpan_file
from solve import SolBF

def main():
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

    ans = input("Apakah Anda ingin menyimpan solusi? (Ya/Tidak): ").strip().lower()
    if ans in ("ya", "y", "yes"):
        out_path = input("Masukkan nama file output (misal: solusi.txt): ").strip()
        if out_path == "":
            out_path = "solusi.txt"
        simpan_file(out_path, solved, ms, cases)
        print(f"Solusi disimpan ke: {out_path}")

if __name__ == "__main__":
    main()
