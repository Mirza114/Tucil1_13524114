import tkinter as tk
from tkinter import filedialog, messagebox

from game import baca, validasi, solusi, print_board, simpan_file
from solve import SolBF

def run_gui():
    root = tk.Tk()
    root.title("Queens BF (simple GUI)")

    path_var = tk.StringVar()

    def browse():
        p = filedialog.askopenfilename(
            title="Pilih file .txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if p:
            path_var.set(p)

    def proses():
        path = path_var.get().strip()
        if path == "":
            messagebox.showerror("Error", "pilih file dulu")
            return
        try:
            board = baca(path)
            validasi(board)
        except Exception as e:
            messagebox.showerror("Input tidak valid", str(e))
            return

        perm, cases, ms = SolBF(board)
        if perm is None:
            messagebox.showinfo("Hasil", f"Tak ada solusi\nWaktunya: {ms:.0f} ms\nJumlah : {cases} kasus")
            return

        solved = solusi(board, perm)
        # biar simpel: tampilkan di textbox
        out.delete("1.0", "end")
        for r in range(solved.shape[0]):
            out.insert("end", "".join(solved[r].tolist()) + "\n")
        out.insert("end", "\n")
        out.insert("end", f"Waktu pencarian: {ms:.0f} ms\n")
        out.insert("end", f"Banyak kasus yang ditinjau: {cases} kasus\n")

        def save():
            out_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt")]
            )
            if out_path:
                simpan_file(out_path, solved, ms, cases)
                messagebox.showinfo("Sukses", f"Solusi disimpan ke:\n{out_path}")

        btn_save.config(command=save, state="normal")

    tk.Label(root, text="File testcase (.txt):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    tk.Entry(root, textvariable=path_var, width=60).grid(row=0, column=1, padx=5, pady=5)
    tk.Button(root, text="Browse", command=browse).grid(row=0, column=2, padx=5, pady=5)

    tk.Button(root, text="Proses BF", command=proses).grid(row=1, column=1, padx=5, pady=5, sticky="w")
    btn_save = tk.Button(root, text="Simpan Solusi", state="disabled")
    btn_save.grid(row=1, column=1, padx=5, pady=5)

    out = tk.Text(root, width=80, height=22)
    out.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    root.mainloop()

