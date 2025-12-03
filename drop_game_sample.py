import pyxel

pyxel.init(250, 200, title="apples")

apples = [
    {"x": 30, "y": 10, "speed": 1, "score": 10, "alive": True},
    {"x": 80, "y": 20, "speed": 1.5, "score": 10, "alive": True}
]

player = {"x": 10, "y": pyxel.height - 25, "w": 15, "h": 20, "speed": 2}

score = 0

# 当たり判定を調べる関数
def is_hit(player, apple):
    if(player["x"] < apple["x"] + 10 and
           player["x"] + player["w"] > apple["x"] and
           player["y"] < apple["y"] + 10 and
           player["y"] + player["h"] > apple["y"]):
        return True
    else:
        return False

def update():
    global apples, score

    # プレイヤーの移動
    # 右移動
    if pyxel.btn(pyxel.KEY_RIGHT):
        player["x"] += player["speed"]
    
    # 左移動
    if pyxel.btn(pyxel.KEY_LEFT):
        player["x"] -= player["speed"]

    # リンゴの落下
    for apple in apples:
        apple["y"] += apple["speed"]

        # もしリンゴが画面の下端を超えたら
        if apple["y"] > pyxel.height:
            # 生存フラグをFalseにする
            apple["alive"] = False
        
        # リンゴとプレイヤーの衝突判定
        if(is_hit(player, apple)):
            
            # 当たった場合の処理
            apple["alive"] = False
            score += apple["score"]
    

    # 生きているリンゴ(alive = True)だけを集めて新しいリストを作る
    new_apples = [] # 新しいリストを用意
    for apple in apples:
        if apple["alive"]: # もしリンゴが生きていたら
            new_apples.append(apple) # 新しいリストに追加
    
    # 元のリストを新しいリストで上書き
    apples = new_apples



def draw():
    pyxel.cls(0)
    for apple in apples:
        if apple["alive"]:
            pyxel.rect(apple["x"], apple["y"], 10, 10, 8)
        else:
            apple["y"] = 10
            apple["alive"] = True
            pyxel.rect(apple["x"], apple["y"], 10, 10, 8)
    
    pyxel.rect(player["x"], player["y"], player["w"], player["h"], 5)
    pyxel.text(200, 10, f"Score: {score}", 7)

pyxel.run(update, draw)