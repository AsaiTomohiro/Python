import random

print("予定とやる時間は一対一の関係と仮定する\n")
val = input("予定(Task)を大文字空白区切りで入力して\n")
yoteilist = val.split("　")
print(val)

youbi = input("時間or曜日(TIME)を大文字空白区切りで入力して\n")
youbilist = youbi.split("　")
print(youbi)

print(yoteilist)
print(youbilist)

#リストの長さ分だけ数字のリストを作る(予定)
math_list1 = list(range(len(yoteilist)))
"""
print(leng)
math_list = []
for i in range(leng):
    math_list.append(i)
"""

print(math_list1)




#リストの長さ分だけ数字のリストを作る(曜日)
math_list2 = list(range(len(youbilist)))
"""
print(leng2)
math_list2 = []
for j in range(leng2):
    math_list2.append(j)
"""

print(math_list2)



#辞書型作成(予定)
yotei_jisyo = dict(zip(math_list1,yoteilist))
print(yotei_jisyo)
#辞書型作成(曜日)
youbi_jisyo = dict(zip(math_list2,youbilist))
print(youbi_jisyo)

#ランダムに並び替える
#rankey_list = random.choice(list(yotei_jisyo.keys()))
#print(list(yotei_jisyo.keys()))
#print(rankey_list)


#リストが空になるまでずっとkeyを出力し続けるもの
key_list_yotei = list(yotei_jisyo.keys())
#print(key_list_yotei)
key_list_youbi = list(youbi_jisyo.keys())



#キーをランダムで並び替える。

list_one = random.sample(key_list_yotei,len(key_list_yotei))
list_two = random.sample(key_list_youbi,len(key_list_youbi))
"""
while key_list_yotei:
    s = random.choice(key_list_yotei)
    key_list_yotei.pop(ramdom(len(key_list_yotei)))
"""


print(list_one)
print(list_two)
#ランダムで並べ替えたキーを利用して予定と曜日のリストを作成。
list_henkan1 = []
list_henkan2 = []

while list_one:
    list_henkan1.append(yotei_jisyo[list_one.pop()])

while list_two:
    list_henkan2.append(youbi_jisyo[list_two.pop()])


print(list_henkan1)
print(list_henkan2)

#予定とやる時間をくっつける。
list_kekka = []

while list_henkan1:
    list_kekka.append([list_henkan1.pop(),list_henkan2.pop()])

print(list_kekka)
