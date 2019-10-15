#search_3_keitaisoを改変させたものになる。これにより単語を収集し、アイデア作成の助けになるはず。

import json, config
from requests_oauthlib import OAuth1Session
from janome.tokenizer import Tokenizer #形態素解析
from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter,TokenCountFilter
import random #ランダム

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)
t = Tokenizer()#形態素のやつ
#動詞のリスト
dousi_list = []
#名詞のリスト
meisi_list = ["https","/","//","://",":","|","."]
#助詞リスト
josi_list = []

#a = Analyzer(token_filters=[POSKeepFilter('動詞')])




url = "https://api.twitter.com/1.1/search/tweets.json"

print("何を調べますか?")
keyword = input('>> ')
print('----------------------------------------------------')


params = {'q' : keyword, 'count' : 10}

req = twitter.get(url, params = params)

if req.status_code == 200:
    search_timeline = json.loads(req.text)
    for tweet in search_timeline['statuses']:
        print()
        print("--------------調べたツイート-----------------")
        print(tweet['user']['name'] + '::' + tweet['text'])
        s = tweet['text']

        print(tweet['created_at'])
        print('----------------------------------------------------')
        print()
        print('===============形態素解析=================')
        for token in t.tokenize(s,stream = True):
            print(token)
        print("===============名詞だけ抽出=============")
        for token in t.tokenize(s):
            if token.part_of_speech.split(",")[0] == '名詞':
                print("名詞 :",token.surface)
                meisi_list.append(token.surface)

        print("===============動詞だけ抽出=============")
        for token in t.tokenize(s):
            if token.part_of_speech.split(",")[0] == '動詞':
                print("動詞 :",token.surface)
                dousi_list.append(token.surface)

        print("===============助詞だけ抽出=============")
        for token in t.tokenize(s):
            if token.part_of_speech.split(",")[0] == '助詞':
                print("助詞 :",token.surface)
                josi_list.append(token.surface)


        print("===========形態素リスト================")
        print(t.tokenize(s,wakati = True))

        #単語出現回数をみる。
        a = Analyzer(token_filters=[POSKeepFilter(['名詞']), TokenCountFilter()])

        g_count = a.analyze(s)
        print(type(g_count))
        # <class 'generator'>


    print("====動詞リスト===")
    #print(dousi_list)
    dousi_list_kai = list(set(dousi_list))
    print(dousi_list_kai)
    #print("====名詞リスト前===")
    #print(meisi_list)
    print("====名詞リスト===")
    #重複を一つにする
    meisi_list_kai = list(set(meisi_list))
    #いらないもの削除
    meisi_list_kai.remove("https")
    meisi_list_kai.remove("/")
    meisi_list_kai.remove("//")
    meisi_list_kai.remove("://")
    meisi_list_kai.remove(":")
    meisi_list_kai.remove("|")
    meisi_list_kai.remove(".")
    print(meisi_list_kai)
    print("====助詞リスト===")
    josi_list_kai = list(set(josi_list))
    print(josi_list_kai)

    print("=======名詞ランダム====")
    print(random.choice(meisi_list))



    #単語出現回数をみる。
    
   # a = Analyzer(token_filters=[POSKeepFilter(['名詞']), TokenCountFilter()])

    #g_count = a.analyze(s)
    #print(type(g_count))
    ## <class 'generator'>
  

    for i in g_count:
        print(i)
  



else:
    print("ERROR: %d" % req.status_code)
