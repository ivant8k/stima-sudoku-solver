# Solver Sudoku 

##  Author

| Nama | NIM |
|------|-----|
| [Ivant Samuel Silaban] | [13523129] | 

## Latar Belakang Proyek

Proyek ini dikembangkan sebagai tugas akhir untuk mata kuliah IF2211 - Strategi Algoritma. Tujuan utamanya bukan hanya untuk menciptakan solver Sudoku yang fungsional, tetapi untuk menggunakan solver tersebut sebagai alat eksperimen. Eksperimen ini dirancang untuk memvisualisasikan dan menganalisis perbedaan fundamental antara algoritma yang berjalan dalam waktu polinomial (diwakili oleh solver berbasis logika-heuristik) dan algoritma yang berjalan dalam waktu eksponensial (diwakili oleh solver backtracking murni) saat dihadapkan pada masalah NP-Complete seperti Sudoku.

## Fitur Utama

###  **Solver Logika-Heuristik (Advanced)**
- **Hidden Singles**: Mencari angka yang hanya bisa ditempatkan di satu posisi dalam baris/kolom/kotak
- **Naked Singles**: Mencari sel yang hanya memiliki satu kandidat angka
- **Naked Pairs**: Mengeliminasi kandidat berdasarkan pasangan angka yang saling terkait
- **Pointing Pairs/Triples**: Menggunakan kandidat yang terbatas dalam satu kotak untuk eliminasi
- **X-Wing**: Teknik advanced untuk puzzle yang sangat sulit
- **Efisiensi**: Menyelesaikan ~80% puzzle Sudoku standar tanpa backtracking

###  **Solver Backtracking (Murni)**
- **Algoritma rekursif**: Memecahkan puzzle yang tidak bisa diselesaikan dengan logika murni
- **Batas waktu dan langkah**: Mencegah proses tak terbatas (5 detik, 20 juta langkah)
- **Pencarian sistematis**: Mencoba semua kombinasi yang valid secara efisien
- **Optimasi**: Hanya dijalankan untuk puzzle yang sangat sulit


## Analisis Performa

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

## Persyaratan Sistem

- **Python 3.6+**
- **Tidak ada dependensi eksternal** - semua implementasi murni Python

## Konsep Algoritma

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

## Struktur Proyek

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

## Cara Penggunaan

### 1. **Menjalankan Perbandingan Langsung**
```bash
cd solver
python main.py
```

Program akan menjalankan semua puzzle dalam `test/puzzles.txt` dengan perbandingan langsung antara:
- **Solver Logika-Heuristik (Advanced)**: Menggunakan semua teknik logika
- **Solver Backtracking (Murni)**: Algoritma rekursif dengan batas waktu


### 2. **Contoh puzzle**

File `test/puzzles.txt` berisi 4 kategori puzzle:

1. **Mudah**: Dapat diselesaikan hanya dengan teknik logika dasar
2. **Sulit**: Membutuhkan teknik X-Wing untuk penyelesaian
3. **Diabolical**: Tidak dapat diselesaikan dengan logika murni, butuh backtracking
4. **Kosong**: Papan kosong untuk menguji performa backtracking

### 3. **Contoh Output yang Dihasilkan**
```
==================== MENGUJI PUZZLE: MUDAH (BISA DISELESAIKAN HANYA DENGAN LOGIKA DASAR) ====================
Papan Awal:
5 3 .  | . 7 .  | . . .
6 . .  | 1 9 5  | . . .
. 9 8  | . . .  | . 6 .
- - - - - - - - - - - -
8 . .  | . 6 .  | . . 3
4 . .  | 8 . 3  | . . 1
7 . .  | . 2 .  | . . 6
- - - - - - - - - - - -
. 6 .  | . . .  | 2 8 .
. . .  | 4 1 9  | . . 5
. . .  | . 8 .  | . 7 9

--- Hasil Solver Logika-Heuristik (Advanced) ---
Status: Terpecahkan
5 3 4  | 6 7 8  | 9 1 2
6 7 2  | 1 9 5  | 3 4 8
1 9 8  | 3 4 2  | 5 6 7
- - - - - - - - - - - -
8 5 9  | 7 6 1  | 4 2 3
4 2 6  | 8 5 3  | 7 9 1
7 1 3  | 9 2 4  | 8 5 6
- - - - - - - - - - - -
9 6 1  | 5 3 7  | 2 8 4
2 8 7  | 4 1 9  | 6 3 5
3 4 5  | 2 8 6  | 1 7 9
Waktu: 0.6026 ms | Langkah: 153 (estimasi eliminasi kandidat)

--- Hasil Solver Backtracking (Murni) ---
Status: Terpecahkan
5 3 4  | 6 7 8  | 9 1 2
6 7 2  | 1 9 5  | 3 4 8
1 9 8  | 3 4 2  | 5 6 7
- - - - - - - - - - - -
8 5 9  | 7 6 1  | 4 2 3
4 2 6  | 8 5 3  | 7 9 1
7 1 3  | 9 2 4  | 8 5 6
- - - - - - - - - - - -
9 6 1  | 5 3 7  | 2 8 4
2 8 7  | 4 1 9  | 6 3 5
3 4 5  | 2 8 6  | 1 7 9
Waktu: 23.4820 ms | Langkah: 4,209 pemanggilan rekursif
======================================================================

==================== MENGUJI PUZZLE: SULIT (MEMBUTUHKAN SETIDAKNYA SATU KALI X-WING) ====================
Papan Awal:
. . .  | 8 . 1  | . . .
. . .  | . . .  | . 4 3
5 . .  | . . .  | . . .
- - - - - - - - - - - -
. . .  | . 7 .  | 8 . .
. . .  | . . .  | 1 . .
. 2 .  | . 3 .  | . . .
- - - - - - - - - - - -
6 . .  | . . .  | . 7 5
. . 3  | 4 . .  | . . .
. . .  | 2 . .  | 6 . .

--- Hasil Solver Logika-Heuristik (Advanced) ---
Status: Terpecahkan
2 3 7  | 8 4 1  | 5 6 9
1 8 6  | 7 9 5  | 2 4 3
5 9 4  | 3 2 6  | 7 1 8
- - - - - - - - - - - -
3 1 5  | 6 7 4  | 8 9 2
4 6 9  | 5 8 2  | 1 3 7
7 2 8  | 1 3 9  | 4 5 6
- - - - - - - - - - - -
6 4 2  | 9 1 8  | 3 7 5
8 5 3  | 4 6 7  | 9 2 1
9 7 1  | 2 5 3  | 6 8 4
Waktu: 5.8374 ms | Langkah: 227 (estimasi eliminasi kandidat)

--- Hasil Solver Backtracking (Murni) ---
Status: Batas Tercapai (Timeout/Steps)
2 3 4  | 8 5 1  | 7 6 9
1 9 8  | 7 6 2  | 5 4 3
5 6 7  | 9 4 3  | 2 8 1
- - - - - - - - - - - -
3 5 9  | 1 7 4  | 8 2 6
4 7 6  | 5 . .  | 1 . .
. 2 .  | . 3 .  | . . .
- - - - - - - - - - - -
6 . .  | . . .  | . 7 5
. . 3  | 4 . .  | . . .
. . .  | 2 . .  | 6 . .
Waktu: 5000.0169 ms | Langkah: 836,740 pemanggilan rekursif
======================================================================

==================== MENGUJI PUZZLE: DIABOLICAL (TIDAK BISA DISELESAIKAN DENGAN LOGIKA X-WING, BUTUH BACKTRACKING) ====================
Papan Awal:
8 . .  | . . .  | . . .
. . 3  | 6 . .  | . . .
. 7 .  | . 9 .  | 2 . .
- - - - - - - - - - - -
. 5 .  | . . 7  | . . .
. . .  | . 4 5  | 7 . .
. . .  | 1 . .  | . 3 .
- - - - - - - - - - - -
. . 1  | . . .  | . 6 8
. . 8  | 5 . .  | . 1 .
. 9 .  | . . .  | 4 . .

--- Hasil Solver Logika-Heuristik (Advanced) ---
Status: Macet
8 . .  | . . .  | . . .
. . 3  | 6 . .  | . . .
. 7 .  | . 9 .  | 2 . .
- - - - - - - - - - - -
. 5 .  | . . 7  | . . .
. . .  | . 4 5  | 7 . .
. . .  | 1 . .  | . 3 .
- - - - - - - - - - - -
. . 1  | . . .  | . 6 8
. . 8  | 5 . .  | . 1 .
. 9 .  | . . .  | 4 . .
Waktu: 0.5257 ms | Langkah: 0 (estimasi eliminasi kandidat)

--- Hasil Solver Backtracking (Murni) ---
Status: Terpecahkan
8 1 2  | 7 5 3  | 6 4 9
9 4 3  | 6 8 2  | 1 7 5
6 7 5  | 4 9 1  | 2 8 3
- - - - - - - - - - - -
1 5 4  | 2 3 7  | 8 9 6
3 6 9  | 8 4 5  | 7 2 1
2 8 7  | 1 6 9  | 5 3 4
- - - - - - - - - - - -
5 2 1  | 9 7 4  | 3 6 8
4 3 8  | 5 2 6  | 9 1 7
7 9 6  | 3 1 8  | 4 5 2
Waktu: 279.9553 ms | Langkah: 49,559 pemanggilan rekursif
======================================================================

==================== MENGUJI PUZZLE: KOSONG ====================
Papan Awal:
. . .  | . . .  | . . .
. . .  | . . .  | . . .
. . .  | . . .  | . . .
- - - - - - - - - - - -
. . .  | . . .  | . . .
. . .  | . . .  | . . .
. . .  | . . .  | . . .
- - - - - - - - - - - -
. . .  | . . .  | . . .
. . .  | . . .  | . . .
. . .  | . . .  | . . .

--- Hasil Solver Logika-Heuristik (Advanced) ---
Status: Macet
. . .  | . . .  | . . .
. . .  | . . .  | . . .
. . .  | . . .  | . . .
- - - - - - - - - - - -
. . .  | . . .  | . . .
. . .  | . . .  | . . .
. . .  | . . .  | . . .
- - - - - - - - - - - -
. . .  | . . .  | . . .
. . .  | . . .  | . . .
. . .  | . . .  | . . .
Waktu: 0.6131 ms | Langkah: 0 (estimasi eliminasi kandidat)

--- Hasil Solver Backtracking (Murni) ---
Status: Terpecahkan
1 2 3  | 4 5 6  | 7 8 9
4 5 6  | 7 8 9  | 1 2 3
7 8 9  | 1 2 3  | 4 5 6
- - - - - - - - - - - -
2 1 4  | 3 6 5  | 8 9 7
3 6 5  | 8 9 7  | 2 1 4
8 9 7  | 2 1 4  | 3 6 5
- - - - - - - - - - - -
5 3 1  | 6 4 2  | 9 7 8
6 4 2  | 9 7 8  | 5 3 1
9 7 8  | 5 3 1  | 6 4 2
Waktu: 1.9377 ms | Langkah: 392 pemanggilan rekursif
======================================================================
```
