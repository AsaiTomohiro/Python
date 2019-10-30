#文書の改行に応じて数値を足し合わせる改行数をカウントするプログラム　= これにより文書数がわかるようになる。
#発展させて特定の単語が入っていたらカウントするようなプログラムを作りました。




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

    