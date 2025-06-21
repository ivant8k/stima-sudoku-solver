import time

class BacktrackingSolver:
    """
    Solver yang menggunakan algoritma backtracking rekursif
    dengan batas waktu dan langkah untuk mencegah proses tak terbatas.
    """
    def __init__(self, board, step_limit=20_000_000, time_limit_sec=5):
        self.board = [row[:] for row in board]
        self.recursion_steps = 0
        self.step_limit = step_limit
        self.time_limit_sec = time_limit_sec
        self.start_time = 0

    def solve(self):
        """Metode publik untuk memulai proses backtracking."""
        self.recursion_steps = 0
        self.start_time = time.perf_counter()
        result = self._backtrack()
        
        if result == "limit_reached":
            return "Batas Tercapai (Timeout/Steps)"
        
        return "Terpecahkan" if result else "Tidak Dapat Dipecahkan"

    def _find_empty(self):
        """Mencari sel kosong pertama (0) di papan."""
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return (r, c)
        return None

    def _is_valid(self, digit, pos):
        """Memeriksa apakah sebuah angka valid untuk ditempatkan di posisi tertentu."""
        r, c = pos
        # Cek baris, kolom, dan kotak 3x3
        for i in range(9):
            if self.board[r][i] == digit and i != c: return False
            if self.board[i][c] == digit and i != r: return False
        
        start_row, start_col = 3 * (r // 3), 3 * (c // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == digit and (start_row + i, start_col + j) != pos:
                    return False
        return True

    def _backtrack(self):
        """Fungsi rekursif inti dengan pemeriksaan batas."""
        self.recursion_steps += 1
        
        # Pemeriksaan batas
        if self.recursion_steps > self.step_limit:
            return "limit_reached"
        if time.perf_counter() - self.start_time > self.time_limit_sec:
            return "limit_reached"

        empty_pos = self._find_empty()
        if not empty_pos:
            return True  # Basis rekursi: puzzle terpecahkan

        r, c = empty_pos
        for digit in range(1, 10):
            if self._is_valid(digit, (r, c)):
                self.board[r][c] = digit
                
                recursive_result = self._backtrack()
                if recursive_result is not False:
                    # Propagasi hasil 'True' atau 'limit_reached' ke atas
                    return recursive_result
                
                self.board[r][c] = 0 # Backtrack
        
        return False