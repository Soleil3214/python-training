import csv #csv読み込んで〜

f = open('stock.csv', 'r') #ファイル開いて〜

reader = csv.reader(f)
header = next(reader)
for row in reader: #1行づつ読み込むよ
    print(row)

f.close()



#おまけ
CsvFile = csv.reader(open('stock.csv'),delimiter=',') #csvファイルを読み込む
CsvList = [] #空のcsvファイルを用意してあげて
for i in CsvFile:
    CsvList.append(i)

print(CsvList)