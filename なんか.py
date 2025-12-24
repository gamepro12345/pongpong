import pyxel
import random


# 画面サイズ
W = 160
H = 120

# プレイヤー（パドル）の位置と大きさ
pad_x = 70
pad_y = 110
pad_w = 20
pad_h = 4

# ボールの位置と速さ
ball_x = 80
ball_y = 60
vx = 1
vy = 1

#ブロックの位置と大きさ
blk_x = 12
blk_y = 40
blk_w = 20
blk_h = 1


#ブロック2の位置と大きさ
blk2_x = 64
blk2_y = 40
blk2_w = 20
blk2_h = 1

#ブロック3の位置と大きさ
blk3_x = 116
blk3_y = 40
blk3_w = 20
blk3_h = 1

# ボール2の位置と速さ
ball2_x = 70
ball2_y = 60
vx2= 2
vy2 = 2

# ボール3の位置と速さ
ball3_x = 70
ball3_y = 60
vx3= 4
vy3 = 4

kaunnto = 0

def update():
    global pad_x, ball_x, ball_y,ball2_x, ball2_y ,vx, vy, vx2,vy2,kaunnto,blk_x,blk_y,blk_w,blk_h,blk2_x,blk2_y,blk2_w,blk2_h,blk3_x,blk3_y,blk3_w,blk3_h,ball3_x,ball3_y,vx3,vy3  
    # --- パドルの操作 ---
    if pyxel.btn(pyxel.KEY_LEFT):
        pad_x -= 3
    if pyxel.btn(pyxel.KEY_RIGHT):
        pad_x += 3

    # --- ボールの移動 ---
    ball_x += vx
    ball_y += vy


    # --- ボールの移動2 ---
    ball2_x += vx2
    ball2_y += vy2

   # --- ボールの移動3 ---
    ball3_x += vx3
    ball3_y += vy3

    # --- 壁との反射 ---
    if ball_x < 0 or ball_x > W - 3:
        vx = -vx
    if ball_y < 0:
        vy = -vy
 #ボールとブロックの当たり判定
    if ((blk_x <= ball_x and ball_x <= blk_x + blk_w) and
        (blk_y - 3 <= ball_y and ball_y <= blk_y)):
        vy = -vy        

     #ボールとブロック2の当たり判定
    if ((blk2_x <= ball_x and ball_x <= blk2_x + blk2_w) and
        (blk2_y - 3 <= ball_y and ball_y <= blk2_y)):
        vy = -vy        

     #ボールとブロック3の当たり判定
    if ((blk3_x <= ball_x and ball_x <= blk3_x + blk3_w) and
        (blk3_y - 3 <= ball_y and ball_y <= blk3_y)):
        vy = -vy    

    # --- パドルとの当たり判定 ---    
    if ((pad_x <= ball_x and ball_x <= pad_x + pad_w) and
        (pad_y - 3 <= ball_y and ball_y <= pad_y)):
        vy = -vy
        kaunnto += 1
 

    # --- 下に落ちたらリセット ---
    if ball_y > H:
        # 初期位置にもどす
        ballv_x = random.randint(1,160)
        ballv_y = random.randint(1,40)
        ball_x = ballv_x
        ball_y = ballv_y
        vx = 1
        vy = 1
        # --- 壁との反射2 ---
    if ball2_x < 0 or ball2_x > W - 3:
        vx2 = -vx2
    if ball2_y < 0:
        vy2 = -vy2

     #ボール2とブロックの当たり判定
    if ((blk_x <= ball2_x and ball2_x <= blk_x + blk_w) and
        (blk_y - 3 <= ball2_y and ball2_y <= blk_y)):
        vy2 = -vy2        

     #ボール2とブロック2の当たり判定
    if ((blk2_x <= ball2_x and ball2_x <= blk2_x + blk2_w) and
        (blk2_y - 3 <= ball2_y and ball2_y <= blk2_y)):
        vy2 = -vy2        

     #ボール2とブロック3の当たり判定
    if ((blk3_x <= ball2_x and ball2_x <= blk3_x + blk3_w) and
        (blk3_y - 3 <= ball2_y and ball2_y <= blk3_y)):
        vy2 = -vy2    

    # --- パドルとの当たり判定2 ---    
    if ((pad_x <= ball2_x and ball2_x <= pad_x + pad_w) and
        (pad_y - 3 <= ball2_y and ball2_y <= pad_y)):
        vy2 = -vy2
        kaunnto += 10
    # --- 下に落ちたらリセット2 ---
    if ball2_y > H:
        # 初期位置にもどす2
        ball2v_x =  random.randint(1,160)
        ball2v_y = random.randint(1,40)
        ball2_x = ball2v_x
        ball2_y = ball2v_y
        vx2 = 2
        vy2= 2

        # --- 壁との反射3 ---
    if ball3_x < 0 or ball3_x > W - 3:
        vx3 = -vx3
    if ball3_y < 0:
        vy3 = -vy3

     #ボール3とブロックの当たり判定
    if ((blk_x <= ball3_x and ball3_x <= blk_x + blk_w) and
        (blk_y - 3 <= ball3_y and ball3_y <= blk_y)):
        vy3 = -vy3        

     #ボール3とブロック2の当たり判定
    if ((blk2_x <= ball3_x and ball3_x <= blk2_x + blk2_w) and
        (blk2_y - 3 <= ball3_y and ball3_y <= blk2_y)):
        vy3 = -vy3        

     #ボール3とブロック3の当たり判定
    if ((blk3_x <= ball3_x and ball3_x <= blk3_x + blk3_w) and
        (blk3_y - 3 <= ball3_y and ball3_y <= blk3_y)):
        vy3 = -vy3    

    # --- パドルとの当たり判定3 ---    
    if ((pad_x <= ball3_x and ball3_x <= pad_x + pad_w) and
        (pad_y - 3 <= ball3_y and ball3_y <= pad_y)):
        vy3 = -vy3
        kaunnto -= 500
    # --- 下に落ちたらリセット3 ---
    if ball3_y > H:
        # 初期位置にもどす3
        ball3v_x =  random.randint(1,160)
        ball3v_y = random.randint(1,40)
        ball3_x = ball3v_x
        ball3_y = ball3v_y
        vx3 = 4
        vy3= 4

def draw():
    pyxel.cls(0)

    # パドル
    pyxel.rect(pad_x, pad_y, pad_w, pad_h, 7)
    
    #ブロック1
    pyxel.rect(blk_x,blk_y,blk_w,blk_h,5)

    #ブロック2
    pyxel.rect(blk2_x,blk2_y,blk2_w,blk2_h,5)

    #ブロック3
    pyxel.rect(blk3_x,blk3_y,blk3_w,blk3_h,5)

    # ボール
    pyxel.rect(ball_x, ball_y, 3, 3, 4)

    # ボール2
    pyxel.rect(ball2_x, ball2_y, 3, 3, 10)

 # ボール3
    kara3= random.randint(1,16)
    pyxel.rect(ball3_x, ball3_y, 3, 3, kara3)

    #カウント
    pyxel.text(66,5,f"score:{kaunnto}",10)

pyxel.init(W, H, title="PONG Sample")
pyxel.run(update, draw)