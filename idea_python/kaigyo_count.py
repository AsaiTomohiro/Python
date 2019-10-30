#文書の改行に応じて数値を足し合わせる改行数をカウントするプログラム　= これにより文書数がわかるようになる。


count = 0
with open("作業用3.txt") as f:
    for line in f:
        count += 1
print(count)

    