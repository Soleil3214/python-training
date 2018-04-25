string = input("求めたい分数を入力してください")
minutes = float(string)
hours = round(minutes/ 60, 2)
def minutes_to_hours():
    output = string + "分は" + str(hours) + "時間です"
    print(output)
#自分で定義した関数を実行する
minutes_to_hours()
