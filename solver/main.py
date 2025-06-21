import time
from utils import load_puzzles_from_file, print_board
from solver_logic import LogicSolver
from solver_backtracking import BacktrackingSolver

def run_experiment(puzzles):
    """
    Fungsi untuk menjalankan perbandingan langsung antara
    Solver Logika Advanced dan Solver Backtracking.
    """
    if not puzzles:
        return

    for name, board in puzzles.items():
        print(f"\n{'='*20} MENGUJI PUZZLE: {name.upper()} {'='*20}")
        print("Papan Awal:")
        print_board(board)
        
        print("\n--- Hasil Solver Logika-Heuristik (Advanced) ---")
        board_for_logic = [row[:] for row in board]
        advanced_techniques = {'singles', 'naked_pairs', 'pointing_pairs', 'xwing'}
        logic_solver = LogicSolver(board_for_logic, techniques=advanced_techniques)
        
        start_time_logic = time.perf_counter()
        status_logic, steps_logic = logic_solver.solve()
        duration_logic = (time.perf_counter() - start_time_logic) * 1000
        
        print(f"Status: {status_logic}")
        print_board(logic_solver.board)
        print(f"Waktu: {duration_logic:.4f} ms | Langkah: {steps_logic:,} (estimasi eliminasi kandidat)")

        print("\n--- Hasil Solver Backtracking (Murni) ---")
        board_for_backtrack = [row[:] for row in board]
        
        # Inisialisasi solver dengan batas waktu 5 detik dan 20 juta langkah
        backtrack_solver = BacktrackingSolver(board_for_backtrack, time_limit_sec=5, step_limit=20_000_000)
        
        start_time_backtrack = time.perf_counter()
        status_backtrack = backtrack_solver.solve()
        duration_backtrack = (time.perf_counter() - start_time_backtrack) * 1000
        
        print(f"Status: {status_backtrack}")
        print_board(backtrack_solver.board)
        print(f"Waktu: {duration_backtrack:.4f} ms | Langkah: {backtrack_solver.recursion_steps:,} pemanggilan rekursif")
        
        print(f"{'='*70}")
            
if __name__ == "__main__":
    all_puzzles = load_puzzles_from_file("../test/puzzles.txt") 
    run_experiment(all_puzzles)