# main.py (Diperbarui untuk alur kerja 3-lapis)

import time
from utils import load_puzzles_from_file, print_board
from solver_logic import LogicSolver
from solver_backtracking import BacktrackingSolver

def run_experiment(puzzles):
    """Fungsi untuk menjalankan seluruh rangkaian eksperimen tiga-lapis."""
    if not puzzles:
        return

    for name, board in puzzles.items():
        print(f"\n{'='*15} MENGUJI PUZZLE: {name.upper()} {'='*15}")
        print("Papan Awal:")
        print_board(board)
        
        current_board = [row[:] for row in board]
        
        # === TAHAP 1: SOLVER LOGIKA SEDERHANA ===
        print("\n--- Tahap 1: Hasil Solver Logika Sederhana (Singles) ---")
        simple_techniques = {'singles'}
        simple_solver = LogicSolver([row[:] for row in current_board], techniques=simple_techniques)
        start_time = time.perf_counter()
        status_simple, steps_simple = simple_solver.solve()
        duration_simple = (time.perf_counter() - start_time) * 1000
        
        print(f"Status: {status_simple}")
        print_board(simple_solver.board)
        print(f"Waktu: {duration_simple:.4f} ms | Langkah: {steps_simple:,} (estimasi)")
        current_board = simple_solver.board # Perbarui papan untuk tahap selanjutnya

        # === TAHAP 2: SOLVER LOGIKA ADVANCED (JIKA PERLU) ===
        if status_simple == "Macet":
            print("\n--- Tahap 2: Hasil Solver Logika Advanced (Semua Heuristik) ---")
            advanced_techniques = {'singles', 'naked_pairs', 'pointing_pairs', 'xwing'}
            advanced_solver = LogicSolver([row[:] for row in current_board], techniques=advanced_techniques)
            start_time = time.perf_counter()
            status_advanced, steps_advanced = advanced_solver.solve()
            duration_advanced = (time.perf_counter() - start_time) * 1000

            print(f"Status: {status_advanced}")
            print_board(advanced_solver.board)
            print(f"Waktu: {duration_advanced:.4f} ms | Langkah: {steps_advanced:,} (estimasi)")
            current_board = advanced_solver.board # Perbarui papan lagi

        # === TAHAP 3: SOLVER BACKTRACKING (JIKA PERLU) ===
        # Cek apakah papan sudah terpecahkan setelah semua logika
        is_solved = all(all(cell != 0 for cell in row) for row in current_board)

        if not is_solved:
            print("\n--- Tahap 3: Melanjutkan dengan Solver Backtracking ---")
            backtrack_solver = BacktrackingSolver([row[:] for row in current_board])
            start_time = time.perf_counter()
            solved = backtrack_solver.solve()
            duration_backtrack = (time.perf_counter() - start_time) * 1000
            
            print(f"Status: {'Terpecahkan' if solved else 'Tidak Dapat Dipecahkan'}")
            print_board(backtrack_solver.board)
            print(f"Waktu: {duration_backtrack:.4f} ms | Langkah: {backtrack_solver.recursion_steps:,} pemanggilan rekursif")
            
if __name__ == "__main__":
    # Ganti "puzzles.txt" dengan nama file Anda jika berbeda
    all_puzzles = load_puzzles_from_file("../test/puzzles.txt") 
    run_experiment(all_puzzles)