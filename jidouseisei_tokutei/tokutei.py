#! /usr/bin/python
#
#   get_tweet_tweepy.py
#
#                       Nov/29/2018
# ------------------------------------------------------------------
import  sys
import  tweepy



Consumer_key = 'fKZ3cldhN5CxZrmtQsSsdAsVY'
Consumer_secret = 'be8WrdAd9LvTfjpnDXL81o7GJtjMlS98hMRpWhJBmLSl3jRisD'
Access_token = '1120628485158871040-PQd3lNIUxV8fyhNCcNI6RV9pYuHUfR'
Access_secret = 'x3jhRRgiWWlSfsaQb69NNHqytiDrqpxGEGK9GAzQ9qEBn'

#認証
auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
auth.set_access_token(Access_token, Access_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)


sys.stderr.write("*** 開始 ***\n")


#screen_name の後に指定した人のアカウントのツイートをもらう
results = api.user_timeline(screen_name="@arm2_", count=10)

#
for result in results:
    #print(result.id)
    #print(result.created_at)
    print(result.text)
    #print()
#
sys.stderr.write("*** 終了 ***\n")
# ---------------------------------
