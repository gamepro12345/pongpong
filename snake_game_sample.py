import pyxel
import time
import random

# 画面サイズ
W = 160
H = 120
CELL = 8  # 1マスの大きさ（8x8）

# グリッドのマス数
GRID_W = W // CELL  # 20
GRID_H = H // CELL  # 15

# スネークの初期状態（マス単位で管理）
snake = [(10, 7), (9, 7), (8, 7)]  # (x, y) のタプルのリスト
dx = 1  # 移動方向（x）
dy = 0  # 移動方向（y）

# エサ
food = (5, 5)

# ゲーム状態
game_over = False

# 移動のスピード調整用
last_move_time = time.time()

def place_food():
    """スネークの体と重ならないランダムな位置にエサを置く"""
    global food
    while True:
        x = random.randrange(GRID_W)
        y = random.randrange(GRID_H)
        if (x, y) not in snake:
            food = (x, y)
            break


def update():
    global dx, dy, last_move_time, game_over

    # 方向転換（逆走は不可にしている）
    if pyxel.btnp(pyxel.KEY_LEFT) and dx != 1:
        dx, dy = -1, 0
    if pyxel.btnp(pyxel.KEY_RIGHT) and dx != -1:
        dx, dy = 1, 0
    if pyxel.btnp(pyxel.KEY_UP) and dy != 1:
        dx, dy = 0, -1
    if pyxel.btnp(pyxel.KEY_DOWN) and dy != -1:
        dx, dy = 0, 1

    now = time.time()

    # 0.2秒毎に1マス進む
    if now - last_move_time < 0.2:
        return
    
    last_move_time = now

    # 新しい頭の位置
    head_x, head_y = snake[0]
    new_x = head_x + dx
    new_y = head_y + dy

    # 壁にぶつかったらゲームオーバー
    if new_x < 0 or new_x >= GRID_W or new_y < 0 or new_y >= GRID_H:
        game_over = True
        return

    # 自分の体にぶつかったらゲームオーバー
    if (new_x, new_y) in snake:
        game_over = True
        return

    # 頭を先頭に追加
    snake.insert(0, (new_x, new_y))

    # エサを食べたかどうか
    if (new_x, new_y) == food:
        # 体を伸ばす
        place_food()
    else:
        # 何も食べていないので、しっぽを削除して長さを保つ
        snake.pop()


def draw():
    pyxel.cls(0)

    # エサの描画
    fx, fy = food
    pyxel.rect(fx * CELL, fy * CELL, CELL, CELL, 8)

    # スネークの描画
    for i, (x, y) in enumerate(snake):
        color = 11 if i == 0 else 7  # 頭だけ色を変える
        pyxel.rect(x * CELL, y * CELL, CELL, CELL, color)


# ゲーム開始
pyxel.init(W, H, title="Snake Sample")
pyxel.run(update, draw)
