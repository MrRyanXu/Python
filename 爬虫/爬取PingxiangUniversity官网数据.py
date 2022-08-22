'''
编写程序，爬取PingxiangUniversity官网的页面信息，将爬取到的页面保存到“D:\\PingxiangUniversity.html”(注意字符编码问题和UA伪装)。
'''
import requests
with open('D:\\PingxiangUniversity.html','w+',encoding='utf-8') as f:
    #创建需要访问的网页链接
    url = "http://www.pxc.jx.cn/"

    #设置请求头的UA用于身份伪装
    headers = {
        "User_Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }

    #使用requests.get的方法爬取页面
    res = requests.get(url, headers = headers)

    #设置已经爬取下来的网页的编码格式
    res.encoding = "utf-8"
    f.writelines(res.text)