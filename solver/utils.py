# utils.py

def print_board(board):
    """Mencetak papan Sudoku dengan format yang mudah dibaca."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            # Cetak angka atau titik untuk sel kosong
            cell = board[i][j]
            print(cell if cell != 0 else ".", end=" ")
        print()

def load_puzzles_from_file(filename):
    """
    Memuat beberapa puzzle dari satu file teks.
    Format: Baris yang diawali '#' adalah nama puzzle, diikuti 9 baris grid.
    """
    puzzles = {}
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            
            current_puzzle_name = ""
            current_board = []
            
            for line in lines:
                line = line.strip()
                if not line:
                    continue
                
                if line.startswith('#'):
                    if current_puzzle_name and current_board:
                        puzzles[current_puzzle_name] = current_board
                    current_puzzle_name = line[1:].strip()
                    current_board = []
                elif len(line) == 9 and line.isdigit():
                    current_board.append([int(c) for c in line])
            
            # Simpan puzzle terakhir di file
            if current_puzzle_name and current_board:
                puzzles[current_puzzle_name] = current_board
                
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan.")
        return None
        
    return puzzles