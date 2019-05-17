# Flickr APIの設定(要書き換え)
key = ""
secret = ""

# ライブラリを取り込む
import flickr_downloader as fli

# レモン(lemon)のダウンロード
#引数はそれぞれ検索キーワード,保存場所、keyとsecretの指定
fli.download("lemon", "./lemon",
        api_key=key, api_secret=secret)
# イチゴ(strawberry)のダウンロード
fli.download("strawberry", "./strawberry",
        api_key=key, api_secret=secret)
print("ok")
