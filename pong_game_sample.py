import pyxel

# 画面サイズ
W = 160
H = 120

#基本変数の定義
hp=3
ball_many=1
speed=1
# プレイヤー（パドル）の位置と大きさ
pad_x = 70
pad_y = 110
pad_w = 20
pad_h = 4

# ボールの位置と速さ
ball_x = 80
ball_y = 60
vx = speed
vy = speed

def update():
    global pad_x, ball_x, ball_y, vx, vy

    # --- パドルの操作 ---
    if pyxel.btn(pyxel.KEY_LEFT):
        pad_x -= 2
    if pyxel.btn(pyxel.KEY_RIGHT):
        pad_x += 2

    # --- ボールの移動 ---
    ball_x += vx
    ball_y += vy

    # --- 壁との反射 ---
    if ball_x < 0 or ball_x > W - 3:
        vx = -vx
    if ball_y < 0:
        vy = -vy

    # --- パドルとの当たり判定 ---    
    if ((pad_x <= ball_x and ball_x <= pad_x + pad_w) and
        (pad_y - 3 <= ball_y and ball_y <= pad_y)):
        vy = -vy

    # --- 下に落ちたらリセット ---
    if ball_y > H:
        # 初期位置にもどす
        ball_x = 80
        ball_y = 60
        vx = 1
        vy = 1


def draw():
    pyxel.cls(0)

    # パドル
    pyxel.rect(pad_x, pad_y, pad_w, pad_h, 7)

    # ボール
    pyxel.rect(ball_x, ball_y, 3, 3, 10)

pyxel.init(W, H, title="PONG Sample")
pyxel.run(update, draw)