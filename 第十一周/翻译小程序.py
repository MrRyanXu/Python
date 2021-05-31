import requests
import json
word = input("请输入需要翻译的单词：")
while word!='':
    url = "http://fanyi.baidu.com/sug"
    parms = {
        'kw':word
    }
    res= requests.get(url = url, params = parms)
    res.encoding = "utf-8"
    content = res.json()
    dic = content['data'][0]
    print(dic['k'],dic['v'])
    word = input("请输入需要翻译的单词：")