
#coding: UTF-8

import twitter

# 取得したキーとアクセストークンを設定する
auth = twitter.OAuth(consumer_key='',
                     consumer_secret='',
                     token='',
                     token_secret='')

t = twitter.Twitter(auth=auth)

# twitterへメッセージを投稿する
t.statuses.update(status="目線が気になるお年頃")
