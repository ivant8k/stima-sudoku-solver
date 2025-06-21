# 🧩 Solver Sudoku 

## 👥 Author

| Nama | NIM |
|------|-----|
| [Ivant Samuel Silaban] | [13523129] | 


## 🎯 Fitur Utama

### 🔍 **Solver Logika-Heuristik (Advanced)**
- **Hidden Singles**: Mencari angka yang hanya bisa ditempatkan di satu posisi dalam baris/kolom/kotak
- **Naked Singles**: Mencari sel yang hanya memiliki satu kandidat angka
- **Naked Pairs**: Mengeliminasi kandidat berdasarkan pasangan angka yang saling terkait
- **Pointing Pairs/Triples**: Menggunakan kandidat yang terbatas dalam satu kotak untuk eliminasi
- **X-Wing**: Teknik advanced untuk puzzle yang sangat sulit
- **Efisiensi**: Menyelesaikan ~80% puzzle Sudoku standar tanpa backtracking

### ⚡ **Solver Backtracking (Murni)**
- **Algoritma rekursif**: Memecahkan puzzle yang tidak bisa diselesaikan dengan logika murni
- **Batas waktu dan langkah**: Mencegah proses tak terbatas (5 detik, 20 juta langkah)
- **Pencarian sistematis**: Mencoba semua kombinasi yang valid secara efisien
- **Optimasi**: Hanya dijalankan untuk puzzle yang sangat sulit

## 📁 Struktur Proyek

```
stima-sudoku-solver/
├── solver/
│   ├── main.py              # Entry point utama dengan perbandingan langsung
│   ├── solver_logic.py      # Implementasi solver logika (singles, pairs, x-wing)
│   ├── solver_backtracking.py # Implementasi algoritma backtracking
│   └── utils.py             # Fungsi pembantu (load puzzle, print board)
├── test/
│   └── puzzles.txt          # Kumpulan puzzle untuk testing
└── README.md               # Dokumentasi ini
```

## 🚀 Cara Penggunaan

### 1. **Menjalankan Perbandingan Langsung**
```bash
cd solver
python main.py
```

Program akan menjalankan semua puzzle dalam `test/puzzles.txt` dengan perbandingan langsung antara:
- **Solver Logika-Heuristik (Advanced)**: Menggunakan semua teknik logika
- **Solver Backtracking (Murni)**: Algoritma rekursif dengan batas waktu

### 2. **Contoh Output yang Dihasilkan**
```
=============== MENGUJI PUZZLE: MUDAH ===============
Papan Awal:
5 3 . | . 7 . | . . .
6 . . | 1 9 5 | . . .
. 9 8 | . . . | . 6 .
- - - - - - - - - - - -
8 . . | . 6 . | . . 3
4 . . | 8 . 3 | . . 1
7 . . | . 2 . | . . 6
- - - - - - - - - - - -
. 6 . | . . . | 2 8 .
. . . | 4 1 9 | . . 5
. . . | . 8 . | . 7 9

--- Hasil Solver Logika-Heuristik (Advanced) ---
Status: Terpecahkan
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
- - - - - - - - - - - -
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
- - - - - - - - - - - -
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
Waktu: 2.3456 ms | Langkah: 1,234 (estimasi eliminasi kandidat)

--- Hasil Solver Backtracking (Murni) ---
Status: Terpecahkan
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
- - - - - - - - - - - -
8 5 9 | 7 6 1 | 4 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 4 | 8 5 6
- - - - - - - - - - - -
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
Waktu: 15.6789 ms | Langkah: 45,678 pemanggilan rekursif
======================================================================
```

## 🧪 Kumpulan Puzzle Test

File `test/puzzles.txt` berisi 4 kategori puzzle:

1. **Mudah**: Dapat diselesaikan hanya dengan teknik logika dasar
2. **Sulit**: Membutuhkan teknik X-Wing untuk penyelesaian
3. **Diabolical**: Tidak dapat diselesaikan dengan logika murni, butuh backtracking
4. **Kosong**: Papan kosong untuk menguji performa backtracking

## 🔧 Implementasi Teknik

### **Hidden & Naked Singles**
```python
# Mencari sel dengan hanya satu kandidat
if len(cand_set) == 1:
    digit = cand_set.pop()
    self._place_digit(r, c, digit)
```

### **Naked Pairs**
```python
# Mencari dua sel dengan kandidat yang sama
if len(pair_cells) == 2:
    # Eliminasi kandidat dari sel lain dalam unit yang sama
```

### **X-Wing**
```python
# Mencari pola X-Wing dalam baris/kolom
if cand_cols[i] == cand_cols[j]:
    # Eliminasi kandidat dari baris/kolom lain
```

### **Backtracking dengan Batas**
```python
def _backtrack(self):
    # Pemeriksaan batas waktu dan langkah
    if self.recursion_steps > self.step_limit:
        return "limit_reached"
    if time.perf_counter() - self.start_time > self.time_limit_sec:
        return "limit_reached"
    
    empty_pos = self._find_empty()
    if not empty_pos:
        return True  # Puzzle terpecahkan
    
    for digit in range(1, 10):
        if self._is_valid(digit, empty_pos):
            # Coba tempatkan digit
            if self._backtrack():
                return True
            # Backtrack jika gagal
```

## 📊 Analisis Performa

### **Keunggulan Pendekatan Perbandingan Langsung**
1. **Transparansi**: Perbandingan langsung antara dua pendekatan
2. **Efisiensi**: Solver logika jauh lebih cepat dari backtracking
3. **Kompleksitas**: Menghindari eksplorasi ruang pencarian yang tidak perlu
4. **Skalabilitas**: Performa tetap baik untuk puzzle yang sangat sulit

### **Metrik yang Diukur**
- **Waktu eksekusi** (dalam milidetik)
- **Jumlah langkah** (estimasi eliminasi kandidat untuk logika, rekursi untuk backtracking)
- **Status penyelesaian** (Terpecahkan/Macet/Batas Tercapai)

### **Batas Waktu dan Langkah**
- **Backtracking**: Maksimal 5 detik dan 20 juta langkah rekursif
- **Logika**: Tidak ada batas, berhenti ketika tidak ada kemajuan

## 🛠️ Persyaratan Sistem

- **Python 3.6+**
- **Tidak ada dependensi eksternal** - semua implementasi murni Python

## 🎓 Konsep Algoritma

### **Constraint Satisfaction Problem (CSP)**
Sudoku adalah contoh klasik CSP dengan:
- **Variabel**: 81 sel dalam grid 9x9
- **Domain**: Angka 1-9 untuk setiap sel
- **Constraints**: Aturan Sudoku (unik dalam baris, kolom, kotak)

### **Heuristik Logika**
- **Singles**: Menerapkan aturan "jika hanya ada satu pilihan, pilih itu"
- **Pairs**: Menggunakan informasi tentang kandidat yang saling terkait
- **X-Wing**: Menerapkan eliminasi berdasarkan pola geometris

### **Backtracking dengan Forward Checking**
- **Pencarian sistematis** dengan validasi real-time
- **Pruning** otomatis berdasarkan constraint violation
- **Efisiensi** melalui pemilihan sel kosong yang optimal
- **Batas waktu** untuk mencegah proses tak terbatas

## 🤝 Kontribusi

Proyek ini dikembangkan sebagai bagian dari mata kuliah **Strategi Algoritma** untuk mendemonstrasikan:
- Implementasi algoritma constraint satisfaction
- Perbandingan performa antara pendekatan logika dan backtracking
- Analisis kompleksitas algoritma
- Optimasi performa melalui hybrid approach

Dan proyek ini dibuat sebagai pendukung makalah.

