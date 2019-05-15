import tweepy

# 先ほど取得した各種キーを代入する
CK='fKZ3cldhN5CxZrmtQsSsdAsVY'
CS='be8WrdAd9LvTfjpnDXL81o7GJtjMlS98hMRpWhJBmLSl3jRisD'
AT='1120628485158871040-PQd3lNIUxV8fyhNCcNI6RV9pYuHUfR'
AS='x3jhRRgiWWlSfsaQb69NNHqytiDrqpxGEGK9GAzQ9qEBn'


auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)

api = tweepy.API(auth)

        # ツイートを取得
def on_status(self, status):

            # ユーザーネームとユーザーIDを表示
    print(status.user.name + "  @" + str(status.user.screen_name)            # ツイートの内容を表示
    print(status.text)    # 分かりやすいように線を入れる
    print("-----------------------")
    return True

    # エラー時の処理
def on_error(self, status_code):
    print('Got an error with status code: ' + str(status_code))
    return True

listener = Listener()
stream = tweepy.Stream(auth, listener, secure=True)
stream.userstream()
