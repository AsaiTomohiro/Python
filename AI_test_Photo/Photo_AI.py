#key: 03c433b2f94f63148a65f4f0a28f223b
#Secret: ffd97e550179385d


from PIL import Image
import numpy as np
import glob

#画像を読み込んでデータとラベルに追加する.
data = [] #画像を入れるリストを空で作成
target = [] #ラベル情報を入れるリストを空で作成

def glob_images(dir, label, size):
    files = glob.glob(dir + "/*.jpg")
    for f in files:
        img = Image.open(f)#画像を開く
        img = img.convert("RGB")#念のためRGB画質に変換
        img.thumbnail((size,size),Image.LANCZOS)#サイズを変換方法を指定してリサイズ
        ary = np.array(img).reshape(-1,)#一次元の配列にする
        data.append(ary)#データに追加
        target.append(label)#ラベルに追加

#画像ディレクトリとラベル、画像サイズを指定してデータを追加
glob_images("./lemon",label = 0, size=8)
glob_images("./strawberry",label = 1,size=8)


print(target)
#print(data)

#学習用とテスト用に分割
from sklearn.model_selection import train_test_split as split
x, x_test, y, y_test = split(data,target)#標準で学習データを0.75、テストデータを0.25に設定

#データを学習
from sklearn import svm
clf = svm.LinearSVC()
clf.fit(x,y)

#モデルを評価
pred = clf.predict(x_test)
result = list(pred == y_test).count(True) / len(y_test)
print("正解率=" + str(result))
