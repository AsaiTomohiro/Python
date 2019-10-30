#idfの計算をします。log(総文書数/単語が出現する文書数)で出しました。
# -*- coding: utf-8

import numpy as np 
#文書数カウント
count = 0
#入っていた時にcountupするもの
in_count = 0
#文書内に入っているかどうか　検索したい文字
tokutei_moji = "猫"

with open("test.txt") as f:
    for line in f:
        if tokutei_moji in line:
            in_count += 1
        count += 1
print(count)
print(in_count)


#対数計算

kekka = np.log(count/in_count)

print(kekka)

    