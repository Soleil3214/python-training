import tkinter
import random

class FightManager:
    #constructor
    def __init__(self):
        self.dialog = tkinter.Frame(width=820, height=434)
        self.dialog.place(x=10, y=10)
        canvas = tkinter.Canvas(self.dialog, width=820, height=434)
        canvas.place(x=0, y=0)
        canvas.create_rectangle(0, 0, 620, 434, fill="black")
        #make a button
        winbutton = tkinter.Button(self.dialog, text="勝利")
        winbutton.place(x=180, y=340)
        winbutton["command"] = self.fight_win
        losebutton = tkinter.Button(self.dialog, text="負けた")
        losebutton.place(x=320, y=340)
        losebutton["command"] = self.fight_lose
        #hide
        self.dialog.place_forget()
    #start to battle
    def fight_start(self, map_data, x, y):
        self.dialog.place(x=10, y=10)
        self.map_data = map_data
        self.brave_x = x
        self.brave_y = y
    #win
    def fight_win(self):
        self.map_data[self.brave_y][self.brave_x] = 0
        self.dialog.place_forget()
    #lose
    def fight_lose(self):
        canvas = tkinter.Canvas(self.dialog, width=820, height=434)
        canvas.place(x=0, y=0)
        canvas.create_rectangle(0, 0, 620, 434, fill="red")
        canvas.create_text(300, 200, fill="white", font=("MS ゴシック", 15), text="""
        勇者は負けてしまった。
        最初からやり直してくれ・・・""")

    #base class
    class Character:
        #constructor
        def __new__(cls):
            obj = super().__new__(cls)
            obj.rsv = 1
            return obj
        #charge attack
        def reserve(self):
            self.rsv = self.rsv + 1

        #attack
        def get_atk(self):
            r = self.rsv
            self.rsv = 1
            return random.randint(1, self.atk * r)
        #defence
        def get_dfs(self):
            return random.randint(1, self.dfs)
        #hitpoint
        def culc_hp(self, atk, dfs):
            dmg = atk - dfs
            #no damage
            if dmg < 1:
                return self.hp
            #damage
            self.hp = self.hp - dmg
            if self.hp < 1:
                self.hp = 0
            return self.hp
        
        #brave class
        class Brave(Character):
            def __init__(self):
                self.name = "勇者ハル"
                self.hp = 30
                self.atk = 15
                self.dfs = 10
        #Monster1
        class Monster1(Character):
            def __init__(self):
                self.name = "マコデビル"
                self.hp = 20
                self.atk = 15
                self.dfs = 10
        #Monster2
        class Monster2(Character):
            def __init__(self):
                self.name = "リリース・ネーク"
                self.hp = 10
                self.atk = 8
                self.dfs = 5

#Monster　IXI
        class MonsterIXI(Character):
            def __init__(self):
                self.name = "オルタンシア"
                self.hp = 1000
                self.atk = 8000
                self.dfs = 14514
                
 #Monster　XII
        class MonsterXII(Character):
            def __init__(self):
                self.name = "ザ・ナドゥ"
                self.hp = 3000
                self.atk = 700
                self.dfs = 15000

#Monster　XIⅡ
        class MonsterXIⅡ(Character):
            def __init__(self):
                self.name = "グロスメギナ"
                self.hp = 18000
                self.atk = 9000
                self.dfs = 9000