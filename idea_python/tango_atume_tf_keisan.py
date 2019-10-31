#これはtf-idfを出すためのやつを考えるためのサンプルプログラムである。
#つまり仮のやつ。




import tweepy
import datetime
import re
import unittest
import MeCab
import random




import sqlite3
from collections import defaultdict
import config


from janome.tokenizer import Tokenizer #形態素解析
from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter,TokenCountFilter

import linecache

from itertools import islice#設定範囲内の行を取得するもの




CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET




def re_1(path,makefile):
    #ファイルをオープンする
    text_data = open(path,"r")
    #全ての内容を読み込む
    text = text_data.read()



    text=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text=re.sub('RT', "", text)
    text=re.sub('お気に入り', "", text)
    text=re.sub('まとめ', "", text)
    text=re.sub(r'[!-~]', "", text)#半角記号,数字,英字
    text=re.sub(r'[︰-＠]', "", text)#全角記号
    text=re.sub('\n', " ", text)#改行文字
    text = re.sub(r'[。]',"",text)  # 読点のみ
    text = re.sub(r"<[^>]*?>","",text)    #HTMLタグ
    text = re.sub(r'[\s+]',"",text)  #１以上の空白文字
    text = re.sub(r"[0-9]","",text)
    #text = re.sub(r"\[","",text)

    makefile2 = ""+ makefile + ".txt"
    f = open(makefile2,'w')
    f.write(text)

    f.close()

    text_data.close()



def print_mandara(list_x,key_tuika):
    list1 = list_x[0:3]
    list2 = list_x[3:5]
    list3 = list_x[5:9]

    list2.insert(1,key_tuika)

    print(list1)
    print(list2)
    print(list3)

def print_mandara_taple(list_x,key_tuika):
    list1 = list_x[0:3]
    list2 = list_x[3:5]
    list3 = list_x[5:9]
    list4 = []
    list5 = []
    list6 = []

    for i in list1:
        list4.insert(len(list4),i[0])

    for j in list2:
        list5.insert(len(list5),j[0])

    for k in list3:
        list6.insert(len(list6),k[0])

    
        
    print(list4)
    list5.insert(1,key_tuika)
    print(list5)
    print(list6)





if __name__ == '__main__':

    print("プログラムを実行しました。")
    print("しばらくお待ちください。")
    
    #加工データを変数に入れて、その変数を単語頻度のjanomeに投げるやつ。
    #変数はsとする
    #makefile2は任意に入力したtextデータタイトルをテキストデータとしての文字列に変更したもの
    #作業用のやつなので作業用としてテキストデータを読み込んでいる。
    makefile2 = ""+ "作業用3" + ".txt"
    f = open(makefile2)
    s = f.read()
    f.close()

    a = Analyzer(token_filters=[POSKeepFilter(['名詞']), TokenCountFilter()])
    

    g_count = a.analyze(s)
    print("名詞をカウントし終えました。")
    #リスト化させる。
    l_count = list(g_count)
    
    #print(type(g_count))
    #print(type(l_count))
    # <class 'generator'>
    #全て表記させる。
    #for i in g_count:
     #   print(i)
    """
    print("sort前")
    print(l_count)
    """
    """
    print("sort後")
    #降順に変更された状態でソートが変わっている　状態はタプルなので注意
    """
    l_sorted=(sorted(l_count,key=lambda x:x[1],reverse=True))
    

    #ここから取得単語合計値を計算
    s1 = 0

    s1 = sum(n for _, n in l_sorted)

    #合計値
    print("取得単語合計値")
    print(s1)

    #ここまで

    #gyou = input("取り出したい行数は?")
    start = input("取得開始行数を半角数値で入力してください。")
    end = input("取得終了行数を半角数値で入力してください。")
    """
    target_line = linecache.getline("作業用3.txt",int(gyou))
    print(target_line)
    linecache.clearcache()


    tokutei_moji2 = "パリ"
    s2 = target_line.count(tokutei_moji2)
    #特定文字が何個入っているかについてプリントしていく
    print("特定文字出現回数")
    print(s2)
    """

    #適当にパリとしているので気にしないで大丈夫です。
    tokutei_moji2 = "パリ"


    #合計
    s3 = 0
    #文字列を結合させ、その文字列つまり文書Aの名詞の合計値を出せばいいのではないか。
    str_sum = ""
    

    with open(makefile2) as fin:
        for line in islice(fin,int(start),int(end)):
            print(line)
            s3 = s3 + line.count(tokutei_moji2)
            str_sum = str_sum + line

    

    l_count2 = list(a.analyze(str_sum))


    print("任意行における特定文字出現回数")
    print(s3)

    print("任意行結合結果")
    print(str_sum)
    print(l_count2)

    #任意行合計単語数
    nini_sum = sum(n for _, n in l_count2)
    print(nini_sum)


    #tf計算
    tf = s3 / nini_sum
    print("tfは")
    print(tf)
    
    



    
    



    
    




    #リストを宣言し、第一から第八までを切り取る
    #頻出度が高い順にする
    item_list = l_sorted[0:8]
    
    print(item_list)
    #リストの第一から第八までを順位ごとに並べたものをitem_listに入れた


    #randomで8こやる
    item_list2 = random.sample(l_count,k=8)

    #キーワードはこの時「パリ」としていた。よってkeyword変数にはパリを入れておく。
    keyword = "パリ"
    print_mandara_taple(item_list,keyword)
    print_mandara_taple(item_list2,keyword)