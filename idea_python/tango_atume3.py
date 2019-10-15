#このプログラムはツイッターのつぶやきをまずテキストデータにして
#そのデータから単語頻度を調べることを目標にしています。
#テキストデータを単語頻度含めたリスト化までは成功している。


import tweepy
import datetime
import re
import unittest
import MeCab
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





if __name__ == '__main__':

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
    print("データを解析中だと考える。")

    #加工データを変数に入れて、その変数を単語頻度のjanomeに投げるやつ。
    #変数はsとする
    #makefile2は任意に入力したtextデータタイトルをテキストデータとしての文字列に変更したもの
    makefile2 = ""+ makefile + ".txt"
    f = open(makefile2)
    s = f.read()
    f.close()

    a = Analyzer(token_filters=[POSKeepFilter(['名詞']), TokenCountFilter()])

    g_count = a.analyze(s)
    #リスト化させる。
    l_count = list(a.analyze(s))
    #print(type(g_count))
    print(type(l_count))
    # <class 'generator'>
    #全て表記させる。
    #for i in g_count:
     #   print(i)
    print(l_count)

