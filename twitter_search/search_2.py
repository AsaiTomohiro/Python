import json, config
from requests_oauthlib import OAuth1Session
from janome.tokenizer import Tokenizer #形態素解析

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)
t = Tokenizer()#形態素のやつ




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
            print(token.surface)

else:
    print("ERROR: %d" % req.status_code)
