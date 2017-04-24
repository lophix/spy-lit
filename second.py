# -*- coding:UTF-8 -*-
import urllib.request

def saveFile(data):
    path = "F:\dirty\_douban"
    with open(path, 'wb') as f:
        f.write(data)

url = "https://www.douban.com/"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
           '(KHTML, like Gecko) Chrome/51.0.2704.63 Safari/537.36'}
req = urllib.request.Request(url=url, headers=headers)

data = urllib.request.urlopen(req).read()

saveFile(data)

print('done!')
