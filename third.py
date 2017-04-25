# -*- coding:utf-8 -*-
import urllib,urllib.request,socket,re,sys,os

picDir = "F:\dirty\_pic"

def saveFile(data):
    path = "F:\dirty\_douban"
    with open(path, 'w') as f:
        f.write(data)

def saveImage(path):
    if not os.path.isdir(picDir):
        os.mkdir(picDir)

    pos = path.rindex('/')
    t = os.path.join(picDir, path[pos+1:])
    return t

url = "https://image.baidu.com/search/index?tn=baiduimage&"
skey = {'wd':'美女'}
finalurl = url + urllib.parse.urlencode(skey)
print(finalurl)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
           '(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}

req = urllib.request.Request(url=finalurl, headers=headers)

data = urllib.request.urlopen(req).read()

#saveFile(str(data))

for link,t,s in set(re.findall(r'(https:(//[a-zA-Z0-9\./_=,&]*\.(jpg|jpeg|gif|png)))', str(data))):
    print(link)
    try:
        urllib.request.urlretrieve(link, saveImage(link))
    except:
        print('失败')

print('done!')
