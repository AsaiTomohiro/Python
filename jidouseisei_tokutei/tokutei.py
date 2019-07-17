#! /usr/bin/python
#
#   get_tweet_tweepy.py
#
#                       Nov/29/2018
# ------------------------------------------------------------------
import  sys
import  tweepy



Consumer_key = 
Consumer_secret = 
Access_token = 
Access_secret = 

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
