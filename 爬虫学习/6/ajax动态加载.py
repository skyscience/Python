import requests
import json

def get_category_from_url(url):
    response_data = download_data(url)
    if not response_data is None:
        data = json.loads(response_data)
        category = '、'.join(data['tags'])
        print('您可以从以下分类中筛选：'+category)

def get_movie_list_data(kw,startpage,endpage):
    url = 'https://movie.douban.com/j/search_subjects'
    suburl = 'https://movie.douban.com/j/subject_abstract'
    for i in range(startpage,endpage+1):
        parmas = {
            'type':'movie',
            'tag':kw,
            'sort':'recommend',
            'page_limit':20,
            'page_start':(i-1)*20
        }
        response_data = download_data(url,parmas)
        if not response_data is None:
            data = json.loads(response_data)['subjects']
            for item in data:
                subparmas = {
                    'subject_id':item['id']
                }
                response_data = download_data(suburl,subparmas)
                if not response_data is None:
                    data = json.loads(response_data)
                    print(data)
                    with open('movie.json','a') as f:
                        f.write(json.dumps(data,ensure_ascii=False)+'\n')

def download_data(url,parmas=None):
    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    response = requests.get(url,headers=header,params=parmas)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        print(response.url)
        return response.text
    else:
        return None

def main():
    url = 'https://movie.douban.com/j/search_tags?type=movie&source='
    get_category_from_url(url)
    kw = input('输入您想要的分类：')
    startpage = int(input('起始页'))
    endpage= int(input('截止页')) 
    get_movie_list_data(kw,startpage,endpage)

    


if __name__ == '__main__':
    main()