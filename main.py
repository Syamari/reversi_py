import random


# 初期化→表示→入力→バリデーション→判定→相手の手→判定→表示
# の順でやってみる、２次元配列が使えそうなので、適宜しらべつつやる
#


# もっと最適化する
def reverse_stone(x, y, board, player_stone, enemy_stone):
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]
    for x_add, y_add in directions:
        nx = x + x_add
        ny = y + y_add
        flip_stones = []

        while 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == enemy_stone:
            flip_stones.append((nx, ny))
            nx += x_add
            ny += y_add

        if 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == player_stone:
            for x_flip, y_flip in flip_stones:
                board[x_flip][y_flip] = player_stone


def reverse_stone_exist(x, y, board, player_stone, enemy_stone):
    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (1, -1),
        (-1, 1),
        (-1, -1),
    ]
    for x_add, y_add in directions:
        nx = x + x_add
        ny = y + y_add
        flip_stones = []

        while 0 <= nx < 8 and 0 <= ny < 8 and board[nx][ny] == enemy_stone:
            flip_stones.append((nx, ny))
            nx += x_add
            ny += y_add

        if (
            0 <= nx < 8
            and 0 <= ny < 8
            and board[nx][ny] == player_stone
            and len(flip_stones) > 0
        ):
            return True


def validation(x, y, board):
    if x < 0 or x > 7 or y < 0 or y > 7:
        print("error1: out of range")
        return
    # x, yの位置に既に石があるかどうかを確認
    elif board[x][y] != "-":
        print("error2: already exists")
        return
    # x, yのそれぞれプラスマイナス1の位置に石があるかどうかを確認
    elif (
        board[x + 1][y] == "-"
        and board[x - 1][y] == "-"
        and board[x][y + 1] == "-"
        and board[x][y - 1] == "-"
    ):
        print("error3: no stone around")
        return
    elif not reverse_stone_exist(x, y, board, "o", "x"):
        print("error4: no stone to reverse")
        return
    else:
        return True


def main():
    # 8x8の盤面を作成
    board = [["-" for j in range(8)] for i in range(8)]

    # 初期配置を設定
    board[3][3] = "o"
    board[3][4] = "x"
    board[4][3] = "x"
    board[4][4] = "o"

    # 初期盤面を表示
    print("---------------")
    for i in board:
        print(" ".join(i))

    # メインのループはここで
    while True:

        # 手の入力を受付
        print("---------------")
        print("input your move separated by space. ↓")
        print("(type exit to quit.)")
        input_str = input()
        if input_str == "exit":
            break

        x, y = [int(i) for i in input_str.split()]

        # バリデーション
        if not validation(x, y, board):
            print("Invalid move. Try again.")
            continue

        # 入力された手を適用
        board[x][y] = "o"

        # リバーシのルールに従って石を裏返す
        reverse_stone(x, y, board, "o", "x")

        # 盤面を表示
        print("-- your move --")
        for i in board:
            print(" ".join(i))

        # 相手(CPU)のターン
        # 可能な手をリストアップ
        possible_moves = []
        for i in range(8):
            for j in range(8):
                if board[i][j] == "-" and reverse_stone_exist(i, j, board, "x", "o"):
                    possible_moves.append((i, j))

        # 可能な手が存在すれば、ランダムに選択
        if possible_moves:
            x, y = random.choice(possible_moves)
            board[x][y] = "x"
            reverse_stone(x, y, board, "x", "o")
        else:
            print("no CPU move")

        # 盤面を表示
        print("-- CPU move --")
        for i in board:
            print(" ".join(i))


if __name__ == "__main__":
    main()
