import copy

# Papan awal (0 artinya kosong)
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_board(b):
    print("\n   SUDOKU BOARD")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) if b[i][j] != 0 else ".", end=" ")

def is_valid(b, row, col, num):
    # Cek baris
    for x in range(9):
        if b[row][x] == num:
            return False
    # Cek kolom
    for x in range(9):
        if b[x][col] == num:
            return False
    # Cek 3x3 box
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if b[startRow + i][startCol + j] == num:
                return False
    return True

def is_solved(b):
    for row in b:
        if 0 in row:
            return False
    return True

def play_game():
    current_board = copy.deepcopy(board)

    while True:
        print_board(current_board)
        if is_solved(current_board):
            print("Selamat! Sudoku selesai dengan benar!")
            break

        try:
            print("\nMasukkan posisi dan angka (contoh: 1 3 5 artinya baris 1 kolom 3 isi 5)")
            row, col, num = map(int, input("Input Anda: ").split())

            if current_board[row][col] != 0:
                print("Posisi sudah terisi. Ulangi.")
                continue

            if not (1 <= num <= 9):
                print("Angka harus 1-9.")
                continue

            if is_valid(current_board, row, col, num):
                current_board[row][col] = num
            else:
                print("Langkah tidak valid (melanggar aturan Sudoku).")
        except Exception as e:
            print("Input tidak valid. Gunakan format: baris kolom angka (contoh: 2 1 9)")

# Jalankan game
if __name__ == "__main__":
    play_game()
