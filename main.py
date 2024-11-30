def print_board(board):
    """Функция для печати игрового поля."""
    print("\n".join([" | ".join(row) for row in board]))
    print("\n")


def check_win(board):
    """Функция для проверки завершённости игры."""
    # Проверяем строки, столбцы и диагонали
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True, f"Победил {row[0]}!"
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True, f"Победил {board[0][col]}!"
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True, f"Победил {board[0][0]}!"
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True, f"Победил {board[0][2]}!"
    # Проверяем на ничью
    if all(cell != " " for row in board for cell in row):
        return True, "Ничья!"
    return False, ""


def is_valid_move(board, x, y):
    """Функция для проверки корректности хода."""
    return 0 <= x < 3 and 0 <= y < 3 and board[x][y] == " "


def main():
    """Основная функция игры."""
    board = [[" " for _ in range(3)] for _ in range(3)]  # Создаём пустое поле
    print("Добро пожаловать в игру Крестики-Нолики!")
    print("Игрок 1: X, Игрок 2: O")
    print("Введите координаты хода в формате: строка столбец (например, 1 2)\n")

    current_player = "X"

    while True:
        print_board(board)
        try:
            move = input(f"Ходит {current_player}. Введите координаты от 0 до 2 (пример 0 1): ")
            x, y = map(int, move.split())
        except ValueError:
            print("Неверный формат ввода. Попробуйте ещё раз.\n")
            continue

        if not is_valid_move(board, x, y):
            print("Некорректный ход. Попробуйте ещё раз.\n")
            continue

        board[x][y] = current_player
        game_over, message = check_win(board)

        if game_over:
            print_board(board)
            print(message)
            break

        current_player = "O" if current_player == "X" else "X"  # Меняем игрока


if __name__ == "__main__":
    main()
