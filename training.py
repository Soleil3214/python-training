"""
このプログラムは日本語でのあいさつを３行に分けて表示するものとなっています
このプログラムは練習用です。
複数行のコメントはダブルクオート*3で対応
Pythonのインデント(:)に注意
"""


# Say Hello!と表示
print("Say Hello!")
# こんにちはと表示
print("こんにちは")
#\はoption+\で対応
print("おはよう \nこんにちは \nこんばんは")

print(3 + 2*2)

print("15分は" +str(15/60) + "時間です")
#変数のテスト
minutes = 25
print(str(minutes) + "分は" + str(minutes / 60) + "時間です")
#入力プログラム
parrot = input("何か入力してw")
print(parrot)

#input関数の戻り値はstr型
minutes_p = input("求めたい分数を入力して下さい:")
minutes_p = int(minutes_p)
print(str(minutes_p) + "分は" + str(minutes_p / 60) + "時間です")




