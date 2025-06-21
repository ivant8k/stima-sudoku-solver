# solver_backtracking.py

class BacktrackingSolver:
    """Solver yang menggunakan algoritma backtracking rekursif."""
    def __init__(self, board):
        self.board = [row[:] for row in board]
        self.recursion_steps = 0

    def solve(self):
        """Metode publik untuk memulai proses backtracking."""
        self.recursion_steps = 0
        return self._backtrack()

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
        # Cek baris
        if any(self.board[r][i] == digit for i in range(9)): return False
        # Cek kolom
        if any(self.board[i][c] == digit for i in range(9)): return False
        # Cek kotak 3x3
        start_row, start_col = 3 * (r // 3), 3 * (c // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == digit:
                    return False
        return True

    def _backtrack(self):
        """Fungsi rekursif inti."""
        self.recursion_steps += 1
        empty_pos = self._find_empty()
        
        if not empty_pos:
            return True  # Basis rekursi: tidak ada sel kosong, puzzle terpecahkan

        r, c = empty_pos
        for digit in range(1, 10):
            if self._is_valid(digit, (r, c)):
                self.board[r][c] = digit
                
                if self._backtrack():
                    return True
                
                # Jika rekursi gagal, batalkan langkah (backtrack)
                self.board[r][c] = 0
        
        return False