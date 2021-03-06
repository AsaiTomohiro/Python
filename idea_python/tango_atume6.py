#このプログラムはツイッターのつぶやきをまずテキストデータにして
#そのデータから単語頻度を調べることを目標にしています。
#テキストデータを単語頻度含めたリスト化までは成功している。

#リストの単語出現頻度からランク付けして並べなおすことをする。 
#とりあえずマンダラートの初期段階である9つの並びまではできた。
# 課題点はキーワードと同じ文字が出力される点と
# ひらがなのしょうもないものが入ってしまうという点　ランダムにすると
# 意味があまりない　その部分を解消する必要がある。
# 次は拡張して　キーワードから出てきたものをさらにツイッターで検索をかけて
# キーワードを並べる工程をする必要がある。 
# 
# #tango_atume5では、tf idfまがいのことをしたい
# numpyを導入してlogの計算を増やす
# 11/10日最新

import numpy as np 
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



CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET


def gettwitterdata(keyword,dfile):



    #認証
    auth = tweepy.OAuthHandler(CK, CS)
    auth.set_access_token(AT, ATS)

    api = tweepy.API(auth, wait_on_rate_limit = True)

    #検索キーワード設定
    q = keyword

    #つぶやきを格納するリスト
    tweets_data =[]
    i = 1
    #カーソルを使用してデータ取得
    for tweet in tweepy.Cursor(api.search, q=q, count=100,tweet_mode='extended').items():

        #つぶやき時間がUTCのため、JSTに変換  ※デバック用のコード
        #jsttime = tweet.created_at + datetime.timedelta(hours=9)
        #print(jsttime)

        #つぶやきテキスト(FULL)を取得
        print("書き込み" + str(i) )
        tweets_data.append(tweet.full_text + '\n')
        i = i + 1
        if i > 5000:#ツイート数が数字以上になると自動でループを抜ける。・
            break

    #出力ファイル名
    fname = r"'"+ dfile + "'"
    fname = fname.replace("'","")

    #ファイル出力
    with open(fname, "w",encoding="utf-8") as f:
        f.writelines(tweets_data)


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
    #文書を増やすため改行は必要。と判断
    #text=re.sub('\n', " ", text)#改行文字
    
    text = re.sub(r'[。]',"",text)  # 読点のみ
    text = re.sub(r"<[^>]*?>","",text)    #HTMLタグ
    #なんかわからないが、このしたの空白文字を省略すると改行がされない。コメントアウトする。
    #text = re.sub(r'[\s+]',"",text)  #１以上の空白文字
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


 #tokutei_moji:調べたい文字 bunsyo:文書
def idf_keisan(tokutei_moji,bunsyo):
    count = 0
    #入っていた時にcountupするもの
    in_count = 0
    #文書内に入っているかどうか　検索したい文字

    idf_list = []
    

    with open(bunsyo) as f:
        for line in f:
            if tokutei_moji in line:
                in_count += 1
            count += 1
    kekka_idf = np.log(count/in_count)
    #少数3桁にしておく
    idf_list= [tokutei_moji,round(kekka_idf,3)]
        





    return (idf_list)

#リスト内のタプルから単語だけをリスト化させるもの。
def list_tango(list1):
    list2 = []
    for i in list1:
        list2.append(i[0])



    return (list2)






if __name__ == '__main__':

    """

    #検索キーワードを入力  ※リツイートを除外する場合 「キーワード -RT 」と入力
    print ('====== Enter Serch KeyWord   =====')
    keyword = input('>  ')
    keyword2 = keyword + " -RT"

    #input.txtにはデータ加工前のデータが書かれているので注意

    dfile = './data/input.txt'
    print('makefile名')
    makefile = input('> ')

    #自分で名前を記入したtxtデータに加工データがある。


    gettwitterdata(keyword2,dfile)
    re_1(dfile,makefile)

    print("おそらく書き込みは完了")
    """
    print("データを解析中だと考える。")

    #加工データを変数に入れて、その変数を単語頻度のjanomeに投げるやつ。
    #変数はsとする
    #makefile2は任意に入力したtextデータタイトルをテキストデータとしての文字列に変更したもの
    makefile = "パリ"
    makefile2 = ""+ makefile + ".txt"
    f = open(makefile2)
    s = f.read()
    f.close()

    a = Analyzer(token_filters=[POSKeepFilter(['名詞']), TokenCountFilter()])

    g_count = a.analyze(s)
    #リスト化させる。
    l_count = list(a.analyze(s))
    #print(type(g_count))
    #print(type(l_count))
    # <class 'generator'>
    #全て表記させる。
    #for i in g_count:
     #   print(i)

    """
    
    print("sort前")
    print(l_count)
    
    
    
    print("sort後")


    """


    #降順に変更された状態でソートが変わっている　状態はタプルなので注意
    
    l_count2=(sorted(l_count,key=lambda x:x[1],reverse=True))
    


   
    #ここからは、リスト内のタプルから名詞だけをリスト化して
    #そのあとに、idfとともにリスト化させるようにする。
    l_tango = list_tango(l_count2)

    list_idf = []

    for i in l_tango:
        list_idf.append(idf_keisan(i,makefile2))

    

    print(list_idf)


    ##ここまで

    """
    #ここからtfの計算を行う。


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
    
    """




    
    
    #タプルを宣言し、第一から第八までを切り取る
    #頻出度が高い順にする
    item_list = l_count2[0:8]
    print(item_list)
    """
    #リストの第一から第八までを順位ごとに並べたものをitem_listに入れた


    #randomで8こやる
    item_list2 = random.sample(l_count,k=8)


    print_mandara_taple(item_list,keyword)
    print_mandara_taple(item_list2,keyword)
    """
