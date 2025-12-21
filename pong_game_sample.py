import pyxel
import time
import random
# 画面サイズ
W = 160
H = 120
#基本変数の定義5
hp=5
pong_time=0
game_over=False
level=1
# ボールのリスト（位置と速度を辞書で管理）
balls = [{"x": random.randint(0, 150), "y": random.randint(0, 110), "vx": 1, "vy": 1}]

# プレイヤー（パドル）の位置と大きさ
pad_x = 70
pad_y = 110
pad_w = 20
pad_h = 4


def update():
    global pad_x, hp, pong_time, game_over, level, balls
    # --- ゲームループの変数管理　---
    if hp<=0:
        pyxel.text(60, 60, "GAME OVER", 8)
        game_over=True
        time.sleep(1)
    if pong_time>=4:
        level+=1
        balls.append({"x": random.randint(0, 150), "y": random.randint(0, 110), "vx": 1, "vy": 1})
        hp+=1
        pong_time=0
    
    # ボールがなくなったら復活
    if len(balls) == 0:
        time.sleep(1)
        balls.append({"x": 80, "y": 60, "vx": 1, "vy": 1})
    # --- パドルの操作 ---
    if pyxel.btn(pyxel.KEY_LEFT):
        pad_x -= 3
    if pyxel.btn(pyxel.KEY_RIGHT):
        pad_x += 3

    # --- ボールの移動と反射 ---
    for ball in balls[:]:
        ball["x"] += ball["vx"]
        ball["y"] += ball["vy"]

        # 壁との反射
        if ball["x"] < 0 or ball["x"] > W - 3:
            ball["vx"] = -ball["vx"]
            pong_time
        if ball["y"] < 0:
            ball["vy"] = -ball["vy"]
            pong_time+=1

        # パドルとの当たり判定
        if ((pad_x <= ball["x"] and ball["x"] <= pad_x + pad_w) and
            (pad_y - 3 <= ball["y"] and ball["y"] <= pad_y)):
            ball["vy"] = -ball["vy"]
            pong_time+=1

        # 下に落ちたらリセット
        if ball["y"] > H:
            balls.remove(ball)
            hp-=1


def draw():
    pyxel.cls(0)
    #hp
    pyxel.text(5, 5, "HP:"+str(hp), 7)
    #レベル
    pyxel.text(5, 15, "LEVEL:"+str(level), 7)
    #ゲームがオーバー
    if game_over:
        pyxel.text(60, 60, "GAME OVER", 8)
        return
    # パドル
    pyxel.rect(pad_x, pad_y, pad_w, pad_h, 7)

    # ボール（複数描画）
    for ball in balls:
        pyxel.rect(ball["x"], ball["y"], 3, 3, 10)

pyxel.init(W, H, title="PONG Sample")
pyxel.run(update, draw)