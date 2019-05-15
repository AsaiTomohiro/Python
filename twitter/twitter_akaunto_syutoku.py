import tweepy

# 以下4つ「xxxxx」を、先ほど控えた値で書き換える。
CONSUMER_KEY = 'fKZ3cldhN5CxZrmtQsSsdAsVY'
CONSUMER_SECRET = 'be8WrdAd9LvTfjpnDXL81o7GJtjMlS98hMRpWhJBmLSl3jRisD'
ACCESS_TOKEN = '1120628485158871040-PQd3lNIUxV8fyhNCcNI6RV9pYuHUfR'
ACCESS_TOKEN_SECRET = 'x3jhRRgiWWlSfsaQb69NNHqytiDrqpxGEGK9GAzQ9qEBn'
# ↓探したいユーザーの「@」以降のアカウント名を入れる
screen_name = 'TwitterJP'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
user_info = api.get_user(screen_name=screen_name)

name = user_info.name
screen_name = user_info.screen_name
description = user_info.description
image_url = user_info.profile_image_url_https
follow_count = user_info.friends_count
follower_count = user_info.followers_count

print('【名前】{}\n【アカウント名】{}\n【自己紹介】{}\n【画像URL】{}\n【フォロー数】:{}\n【フォロワー数】:{}'
      .format(name, screen_name, description, image_url, follow_count, follower_count))
