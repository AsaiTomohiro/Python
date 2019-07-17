import re


path = './青木.txt'
#ファイルをオープンする
text_data = open(path,"r")
#全ての内容を読み込む
text = text_data.read()



text1=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
text=re.sub('RT', "", text)
text=re.sub('お気に入り', "", text)
text=re.sub('まとめ', "", text)
text=re.sub(r'[!-~]', "", text)#半角記号,数字,英字
text=re.sub(r'[︰-＠]', "", text)#全角記号
#text=re.sub('\n', " ", text)#改行文字

f = open('青木1.txt','w')
f.write(text)

f.close()

text_data.close()
