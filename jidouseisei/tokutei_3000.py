import tweepy

from datetime import timedelta #※4



#各キーを取得 ※1

consumer_key=''

consumer_secret=''

access_token=''

access_token_secret=''



#認証情報を設定

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)



#APIインスタンスの作成

api=tweepy.API(auth)



def main():

    Account=input('Account:@') #ツイートを抽出するアカウントIDを入力するためのInput関数

    num=0 #取得するツイートを計算する

    pages=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17] #※2
    print('makefile名')
    makefile = input('>')
    makefile2 = "" + makefile + '.txt'
    f = open(makefile2, 'w')


    for page in pages:

        tweets=api.user_timeline(Account, count=200, page=page) #※3

        for tweet in tweets:

            tweet.created_at+=timedelta(hours=9) #※4


            #print(tweet.text) #各ツイート内容表示
            f.write(tweet.text)

            num+=1

    print(num, 'ツイート表示しました。')
    f.close()

if __name__=='__main__':

    main()
