import random

def create_board(rows, cols, num_mines):
    # 创建空白游戏板
    board = [[' ' for _ in range(cols)] for _ in range(rows)]
    
    # 随机布雷
    mines = []
    while len(mines) < num_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        if (row, col) not in mines:
            mines.append((row, col))
            board[row][col] = '*'
    
    return board

def count_adjacent_mines(board, row, col):
    # 计算相邻雷的数量
    count = 0
    rows = len(board)
    cols = len(board[0])
    
    for i in range(max(0, row - 1), min(row + 2, rows)):
        for j in range(max(0, col - 1), min(col + 2, cols)):
            if board[i][j] == '*':
                count += 1
    
    return count

def reveal_square(board, row, col):
    # 揭开方块
    if board[row][col] == '*':
        return False
    
    rows = len(board)
    cols = len(board[0])
    
    # 计算相邻雷的数量
    count = count_adjacent_mines(board, row, col)
    board[row][col] = str(count)
    
    # 如果相邻雷的数量为0，则递归揭开相邻方块
    if count == 0:
        for i in range(max(0, row - 1), min(row + 2, rows)):
            for j in range(max(0, col - 1), min(col + 2, cols)):
                if board[i][j] == ' ':
                    reveal_square(board, i, j)
    
    return True

def print_board(board):
    # 打印游戏板
    for row in board:
        print(' '.join(row))
    print()

def play_game():
    rows = int(input("请输入游戏板的行数: "))
    cols = int(input("请输入游戏板的列数: "))
    num_mines = int(input("请输入雷的数量: "))
    
    board = create_board(rows, cols, num_mines)
    print_board(board)
    
    while True:
        row = int(input("请输入要揭开的方块行号: "))
        col = int(input("请输入要揭开的方块列号: "))
        
        if not reveal_square(board, row, col):
            print("游戏结束！你踩到了雷！")
            print_board(board)
            break
        
        print_board(board)

play_game()
