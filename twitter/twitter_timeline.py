import tweepy

# 先ほど取得した各種キーを代入する
CK=''
CS=''
AT=''
AS=''


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
