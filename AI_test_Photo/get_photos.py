# Flickr APIの設定(要書き換え)
key = "03c433b2f94f63148a65f4f0a28f223b"
secret = "ffd97e550179385d"

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
