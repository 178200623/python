import re
import csv
import requests
from tqdm import tqdm
from urllib.parse import urlencode
from requests.exceptions import RequestException

def get_one_page(city,keyword,region,page):
    '''
    获取网页HTML内容并返回
    :param city:
    :param keyword:
    :param region:
    :param page:
    :return:
    '''
    #请求地址
    paras = {
        'jl': city,             #搜索城市 '天津+北京'
        'kw': keyword,       #职位 'python开发工程师'
        'isadv': 0,                    #是否打开更加详细搜索选项
        'isfilter': 1,                 #是否对结果过滤
        'p': page,                        #页数
        're': region                     #region的缩写，地区，2006代表朝阳
    }

    #请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
        'Host': 'sou.zhaopin.com',
        'Referer': 'https://sou.zhaopin.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9'
    }

    url = 'https://sou.zhaopin.com/jobs/searchresult.ashx?' + urlencode(paras)

    try:
        response = requests.get(url, headers = headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException as e :
        return None


def parse_one_page(html):
    '''
    解析HTML代码，提取有用的信息返回
    :param html:
    :return:
    '''
    #正则表达式进行解析

    pattern = re.compile('<a style=.*? target="_blank">(.*?)</a>.*?'  # 匹配职位信息
                         '<td class="gsmc"><a href="(.*?)" target="_blank">(.*?)</a>.*?'  # 匹配公司网址和公司名称
                         '<td class="zwyx">(.*?)</td>', re.S)  # 匹配月薪

    #匹配符合所有条件的内容
    items = re.findall(pattern,html)

    for item in items:
        job_name = item[0]
        job_name = job_name.replace('<b>','')
        job_name = job_name.replace('</b>','')
        ''''''
        yield {
            'job': job_name,
            'website': item[1],
            'company': item[2],
            'salary': item[3]
        }

def write_csv_file(path,headers,rows):
    '''
    将标题头和行写入csv文件
    :param path:
    :param headers:
    :param sows:
    :return:
    '''
    with open(path,'a',encoding='gb18030',newline='') as f:
        f_csv = csv.DictWriter(f,headers)
        f_csv.writeheader()
        f_csv.writerows(rows)


def write_csv_headers(path,headers):
    '''
    写入行
    :param path:
    :param henders:
    :return:
    '''
    with open(path,'a',encoding='gb18030',newline='') as f:
        f_csv = csv.DictWriter(f,headers)
        f_csv.writeheader()


def write_csv_rows(path, headers, rows):
    '''
    写入行
    :param path:
    :param henders:
    :return:
    '''
    with open(path, 'a', encoding='gb18030', newline='') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writerows(rows)


def main(city,keyword,region,pages):
    '''
    主函数
    :param city:
    :param keyword:
    :param region:
    :param pages:
    :return:
    '''
    filename = 'zl_' + city + '_' + keyword + '.csv'
    headers = ['job','website','company','salary']
    write_csv_headers(filename,headers)
    for i in tqdm(range(pages)):
        '''
        获取该网页中所有职位信息，写入csv文件
        '''
        jobs = []
        html = get_one_page(city,keyword,region,i)
        items = parse_one_page(html)
        for item in items :
            jobs.append(item)
        write_csv_rows(filename,headers,jobs)


if __name__ == '__main__' :
    main('北京','python开发工程师', 2006, 2)