#!/usr/bin/python3
# -*- coding:utf-8 -*-
import urllib.request,re,time,random,os,urllib.parse,gzip

def saveImage(data,i):
    path = "F:\\dirty\\page_" + str(i + 1)
    if not os.path.isdir(path):
        os.mkdir(path)

    with open(path + "\\data", 'w') as f:
        f.write(str(data))

    for link,t,s in set(re.findall(r'(https:(//[a-zA-Z0-9\./_=,&]*\.(jpg|jpeg|gif|png)))', str(data))):
        #print(link)
        t = lambda l:os.path.join(path, l[l.rindex('/')+1:])
        try:
            urllib.request.urlretrieve(link, t(link))
        except:
            print('失败')

def ungzip(data):  
    try:  
        data = gzip.decompress(data)
    except:  
        print("未经压缩，无需解压...")  
    return data

class myspider:
    def __init__(self, pageIdx = 0, url = "https://image.baidu.com/search/flip?tn=baiduimage&word=%C3%C0%C5%AE&pn=0"):
        self.pageIdx = pageIdx
        self.url = url[0:url.rfind('&') + 1] + urllib.parse.urlencode({'pn':str(pageIdx)})
        self.headers = {
            'Accept':'text/html,application/xhtml+xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, sdch, br',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection':'keep-alive',
            'Host':'image.baidu.com',
            'Upgrade-Insecure-Request':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
            }

    def setPage(self,idx,kw):
        self.url = self.url[0:self.url.find('&') + 1] + urllib.parse.urlencode({'word':kw,'pn':str(idx)})
        print(self.url)

    def getData(self):
        req = urllib.request.Request(self.url, headers = self.headers)
        data = urllib.request.urlopen(req).read()
        data = ungzip(data)
        return data


sp = myspider()

for idx in range(10):
    sp.setPage(idx*20,'美女')
    pages = sp.getData()
    saveImage(pages,idx)

print('done!')
