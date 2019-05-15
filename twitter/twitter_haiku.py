
#coding: UTF-8

import twitter

# 取得したキーとアクセストークンを設定する
auth = twitter.OAuth(consumer_key='fKZ3cldhN5CxZrmtQsSsdAsVY',
                     consumer_secret='be8WrdAd9LvTfjpnDXL81o7GJtjMlS98hMRpWhJBmLSl3jRisD',
                     token='1120628485158871040-PQd3lNIUxV8fyhNCcNI6RV9pYuHUfR',
                     token_secret='x3jhRRgiWWlSfsaQb69NNHqytiDrqpxGEGK9GAzQ9qEBn')

t = twitter.Twitter(auth=auth)

# twitterへメッセージを投稿する
t.statuses.update(status="目線が気になるお年頃")
