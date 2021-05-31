'''
药监局网站如下：“http://scxk.nmpa.gov.cn:81/xk/”，
爬取前5页所有的“企业名称”、“许可证编号”，“发证机关”，“有效期至”和“发证日期”等几项信息，保存在文件“id.txt”文件中
'''
import requests
import json

if __name__ == '__main__':
    # 获取不同企业的ID值
    id_list = []
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)  AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    for page in range(1, 6):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }

        response = requests.post(url=url, data=data, headers=headers).json()
        for dic in response['list']:
            id_list.append(dic['ID'])

    # 获取企业详细数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    fp = open('D:\\id.txt', 'w', encoding='utf-8')
    for id_data in id_list:
        param = {'id': id_data}
        response_data = requests.post(url=post_url, data=param, headers=headers).json()
        for k, v in response_data.items():  # 以元组的形式分行打印
            all_data = str((k, v))
            fp.write(all_data+'\n')
        fp.write("================================================================================\n")
    print('爬取完成！')
    fp.close()
