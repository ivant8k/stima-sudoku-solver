class LogicSolver:
    """
    Solver yang menggunakan teknik logika-heuristik.
    Dapat dikonfigurasi untuk menggunakan set teknik yang berbeda.
    """
    def __init__(self, board, techniques={'singles', 'naked_pairs', 'pointing_pairs', 'xwing'}):
        self.board = [row[:] for row in board]
        self.techniques = techniques
        self.candidates = self._initialize_candidates()

    def solve(self):
        """Loop utama untuk menerapkan teknik logika yang aktif secara berulang."""
        total_steps = 0
        while True:
            progress_made = False
            
            if 'singles' in self.techniques:
                single_found, single_steps = self._apply_singles()
                if single_found:
                    progress_made = True
                    total_steps += single_steps
                    continue

            if 'naked_pairs' in self.techniques:
                pairs_found, pairs_steps = self._apply_naked_pairs()
                if pairs_found:
                    progress_made = True
                    total_steps += pairs_steps
                    continue

            if 'pointing_pairs' in self.techniques:
                pointing_found, pointing_steps = self._apply_pointing_pairs()
                if pointing_found:
                    progress_made = True
                    total_steps += pointing_steps
                    continue

            if 'xwing' in self.techniques:
                xwing_found, xwing_steps = self._apply_x_wing()
                if xwing_found:
                    progress_made = True
                    total_steps += xwing_steps

            if not progress_made:
                break
        
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    return "Macet", total_steps
        return "Terpecahkan", total_steps

    # --- FUNGSI-FUNGSI PEMBANTU (Helper Functions) ---
    
    def _initialize_candidates(self):
        candidates = {}
        for r in range(9):
            for c in range(9):
                if self.board[r][c] == 0:
                    possible = set(range(1, 10))
                    for i in range(9):
                        possible.discard(self.board[r][i])
                        possible.discard(self.board[i][c])
                    start_row, start_col = 3 * (r // 3), 3 * (c // 3)
                    for i in range(3):
                        for j in range(3):
                            possible.discard(self.board[start_row + i][start_col + j])
                    candidates[(r, c)] = possible
        return candidates

    def _update_peers(self, r, c, digit):
        steps = 0
        peers = set()
        for i in range(9):
            peers.add((r, i))
            peers.add((i, c))
        start_row, start_col = 3 * (r // 3), 3 * (c // 3)
        for i in range(3):
            for j in range(3):
                peers.add((start_row + i, start_col + j))
        
        for pr, pc in peers:
            if (pr, pc) != (r, c) and digit in self.candidates.get((pr, pc), set()):
                self.candidates[(pr, pc)].remove(digit)
                steps += 1
        return steps

    def _place_digit(self, r, c, digit):
        if self.board[r][c] == 0:
            self.board[r][c] = digit
            steps = self._update_peers(r, c, digit) + 1
            if (r, c) in self.candidates:
                del self.candidates[(r, c)]
            return True, steps
        return False, 0
    
    # --- IMPLEMENTASI TEKNIK LOGIKA ---

    def _apply_singles(self):
        steps = 0
        made_change = False
        
        for (r, c), cand_set in list(self.candidates.items()):
            if len(cand_set) == 1:
                digit = cand_set.pop()
                changed, s = self._place_digit(r, c, digit)
                if changed:
                    steps += s
                    made_change = True
        if made_change: return True, steps

        for unit_type in ["row", "col", "box"]:
            for i in range(9):
                counts = {d: [] for d in range(1, 10)}
                if unit_type == "row": cells = [(i, c) for c in range(9)]
                elif unit_type == "col": cells = [(r, i) for r in range(9)]
                else: start_row, start_col = 3 * (i // 3), 3 * (i % 3); cells = [(start_row + r_off, start_col + c_off) for r_off in range(3) for c_off in range(3)]
                
                for r, c in cells:
                    if self.board[r][c] == 0:
                        for digit in self.candidates.get((r, c), set()):
                            counts[digit].append((r, c))
                
                for digit, pos_list in counts.items():
                    if len(pos_list) == 1:
                        r, c = pos_list[0]
                        changed, s = self._place_digit(r, c, digit)
                        if changed:
                           steps += s
                           made_change = True
        return made_change, steps
    
    def _get_units(self):
        """Generator untuk semua unit (baris, kolom, kotak)."""
        for i in range(9):
            yield [(i, c) for c in range(9)] # Baris
            yield [(r, i) for r in range(9)] # Kolom
        for br in range(3):
            for bc in range(3):
                yield [(br*3 + r, bc*3 + c) for r in range(3) for c in range(3)] # Kotak

    def _apply_naked_pairs(self):
        """Menerapkan teknik Naked Pairs."""
        steps = 0
        made_change = False
        for unit in self._get_units():
            # Cari sel dengan tepat 2 kandidat
            cells_with_two_cands = [cell for cell in unit if len(self.candidates.get(cell, set())) == 2]
            if len(cells_with_two_cands) < 2:
                continue

            # Kelompokkan sel berdasarkan kandidatnya
            from collections import defaultdict
            pairs = defaultdict(list)
            for cell in cells_with_two_cands:
                pairs[tuple(sorted(self.candidates[cell]))].append(cell)

            # Jika ada grup berisi 2 sel (naked pair ditemukan)
            for pair_cands, pair_cells in pairs.items():
                if len(pair_cells) == 2:
                    digit1, digit2 = pair_cands
                    # Eliminasi kandidat dari sel lain di unit yang sama
                    for r, c in unit:
                        if (r, c) not in pair_cells:
                            if digit1 in self.candidates.get((r, c), set()):
                                self.candidates[(r,c)].remove(digit1)
                                steps += 1
                                made_change = True
                            if digit2 in self.candidates.get((r, c), set()):
                                self.candidates[(r,c)].remove(digit2)
                                steps += 1
                                made_change = True
        return made_change, steps

    def _apply_pointing_pairs(self):
        """Menerapkan teknik Pointing Pairs/Triples."""
        steps = 0
        made_change = False
        for i in range(9): # Iterasi melalui 9 kotak
            start_row, start_col = 3 * (i // 3), 3 * (i % 3)
            box_cells = [(start_row + r, start_col + c) for r in range(3) for c in range(3)]

            for digit in range(1, 10):
                cand_pos = [cell for cell in box_cells if digit in self.candidates.get(cell, set())]
                if len(cand_pos) < 2: continue

                # Cek apakah semua kandidat ada di baris yang sama
                in_same_row = all(r == cand_pos[0][0] for r, c in cand_pos)
                if in_same_row:
                    row_to_check = cand_pos[0][0]
                    for c in range(9):
                        if (row_to_check, c) not in box_cells:
                             if digit in self.candidates.get((row_to_check, c), set()):
                                self.candidates[(row_to_check, c)].remove(digit)
                                steps += 1
                                made_change = True
                
                # Cek apakah semua kandidat ada di kolom yang sama
                in_same_col = all(c == cand_pos[0][1] for r, c in cand_pos)
                if in_same_col:
                    col_to_check = cand_pos[0][1]
                    for r in range(9):
                        if (r, col_to_check) not in box_cells:
                            if digit in self.candidates.get((r, col_to_check), set()):
                                self.candidates[(r, col_to_check)].remove(digit)
                                steps += 1
                                made_change = True
        return made_change, steps

    def _apply_x_wing(self):
        steps = 0
        made_change = False
        for digit in range(1, 10):
            # Analisis berbasis baris
            rows_with_two = {r: [c for c in range(9) if digit in self.candidates.get((r, c), set())] for r in range(9)}
            rows_with_two = {r: tuple(cols) for r, cols in rows_with_two.items() if len(cols) == 2}
            
            cand_cols = list(rows_with_two.values())
            for i in range(len(cand_cols)):
                for j in range(i+1, len(cand_cols)):
                    if cand_cols[i] == cand_cols[j]:
                        # X-Wing ditemukan
                        c1, c2 = cand_cols[i]
                        r_pair1 = [r for r, cols in rows_with_two.items() if cols == cand_cols[i]]
                        
                        for r_other in range(9):
                            if r_other not in r_pair1:
                                if digit in self.candidates.get((r_other, c1), set()):
                                    self.candidates[(r_other, c1)].remove(digit)
                                    steps +=1; made_change = True
                                if digit in self.candidates.get((r_other, c2), set()):
                                    self.candidates[(r_other, c2)].remove(digit)
                                    steps +=1; made_change = True
        return made_change, steps