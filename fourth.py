# -*- coding:utf-8 -*-
import urllib.request,re,urllib.parse,http.cookiejar,ssl

def composeHeaders(header):
    #设置cookie处理
    cookieJar = http.cookiejar.CookieJar()
    cp = urllib.request.HTTPCookieProcessor(cookieJar)
    opener = urllib.request.build_opener(cp)
    headers = []
    for key,value in header.items():
        elem = (key, value)
        headers.append(elem)

    opener.addheaders = headers
    return opener

headers = {
    'Accept':'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Host':'192.168.10.61',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
    }

url = "https://192.168.10.61"
req = urllib.request.Request(url, headers=headers)

#data = urllib.request.urlopen(req).read()

opener = composeHeaders(headers)

url += '/login'

postdata = {
    'loginName':'long',
    'pass':'e10adc3949ba59abbe56e057f20f883e'
    }

post = urllib.parse.urlencode(postdata).encode()
ssl.match_hostname = lambda cert, hostname: True
data = opener.open(url,post).read()

with open('F:\\dirty\\_douban', 'wb') as f:
    f.write(data)

print('done!')
