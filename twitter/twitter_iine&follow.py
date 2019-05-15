import tweepy

# 以下4つ「xxxxx」を、先ほど控えた値で書き換える。
consumer_key = 'fKZ3cldhN5CxZrmtQsSsdAsVY'
consumer_secret = 'be8WrdAd9LvTfjpnDXL81o7GJtjMlS98hMRpWhJBmLSl3jRisD'
access_token_key = '1120628485158871040-PQd3lNIUxV8fyhNCcNI6RV9pYuHUfR'
access_token_secret = 'x3jhRRgiWWlSfsaQb69NNHqytiDrqpxGEGK9GAzQ9qEBn'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

word = ["m"]
set_count = 10
results = api.search(q=word, count=set_count)

for result in results:
    username = result.user._json['screen_name']
    user_id = result.id
    print("ユーザーID："+str(user_id))
    user = result.user.name
    print("ユーザー名："+user)
    tweet = result.text
    print("ユーザーのコメント："+tweet)

    try:
        api.create_favorite(user_id)
        api.create_friendship(username)
        print(user+"をフォローと「いいね」をしました\n\n")
    except:
        print(user+"はもうフォローしてます\n\n")
