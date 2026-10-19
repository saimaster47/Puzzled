# random puzzle generator and test suite
import random

def generate_solved_board():
    """
    Generates a fully valid, randomized solved 9x9 board
    """
    board = [[0] * 9 for _ in range(9)]

    def is_valid_cell(b, num, pos):
        row, col = pos
        for j in range(9):
            if b[row][j] == num and j != col:
                return False

        for i in range(9):
            if b[i][col] == num and i != row:
                return False

        subgrid_row = (row // 3) * 3
        subgrid_col = (col // 3) * 3
        for i in range(subgrid_row, subgrid_row + 3):
            for j in range(subgrid_col, subgrid_col + 3):
                if b[i][j] == num and (i, j) != pos:
                    return False

        return True

    def fill_board(b):
        for i in range(9):
            for j in range(9):
                if b[i][j] == 0:
                    numbers = list(range(1, 10))
                    random.shuffle(numbers) 
                    for num in numbers:
                        if is_valid_cell(b, num, (i, j)):
                            b[i][j] = num
                            if fill_board(b):
                                return True
                            b[i][j] = 0
                    return False
        return True

    fill_board(board)
    return board    

def generate_puzzle(difficulty="Medium"):
    """
    Generates a randomized puzzle of a given difficulty level
    Difficulty levels: Easy, Medium, Hard
    """

    board = generate_solved_board()

    # number of cells removed based on difficulty
    if difficulty == "Easy":
        # leaves 43-49 clues
        removals = random.randint(32, 38)
    elif difficulty == "Medium":
        # leaves 33-39 clues
        removals = random.randint(42, 48)
    elif difficulty == "Hard":
        # leaves 23-29 clues
        removals = random.randint(52, 58)
    else:
        removals = 40

    # randomly selects and clears cells
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)

    removed = 0
    for r, c in cells:
        if removed >= removals:
            break
        board[r][c] = 0
        removed += 1

    return board


TEST_SUITES = {
    " Static Easy Puzzle": [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ],

    "Random Easy Puzzle": generate_puzzle("Easy"),

    "Random Medium Puzzle": generate_puzzle("Medium"),

    "Random Hard Puzzle": generate_puzzle("Hard")
}