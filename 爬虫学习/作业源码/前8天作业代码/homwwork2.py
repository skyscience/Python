import requests
import requests.exceptions
import json
def get_type_from_url(url):
    print(url)
    response_data = download_from_url(url)
    if not response_data is None:
        tags = '、'.join(json.loads(response_data)['tags'])
        print('以下分类菜单供您赛选：' + tags)
    else:
        print('请求出错')

def get_movielist_from_parmas(categry,startpage,endpage):
    print(categry)
    for page in range(startpage,endpage+1):
        #https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=0
        #https://movie.douban.com/j/search_subjects?type=movie&tag=热门&sort=recommend&page_limit=20&page_start=20
        parmas = {
            'type':'movie',
            'tag':categry,
            'sort':'recommend',
            'page_limit':20,
            'page_start':(page-1)*20
        }
        url = 'https://movie.douban.com/j/search_subjects'
        response_data = download_from_url(url,parmas)
        if not response_data is None:
            # print(response_data)
            response_data = json.loads(response_data)['subjects']
            for item in response_data:
                subparmas = {'subject_id':item['id']} 
                sub_data = download_from_url('https://movie.douban.com/j/subject_abstract',subparmas)
                write_data_to_db(sub_data)
        else:
            print('请求出错')

def write_data_to_db(json_data):
    print(json_data)

def download_from_url(url,params=None):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    try:
        response = requests.get(url,headers=headers,params=params)
    except requests.exceptions.ConnectTimeout as e:
        print(e)
    except requests.exceptions.HTTPError as e:
        print(e)
    except requests.exceptions.ConnectionError as e:
        print(e)
    else:
        response.encoding = 'utf-8'
        if response.status_code == 200:
            return response.text
        else:
            return None


def main():
    get_type_from_url('https://movie.douban.com/j/search_tags?type=movie&source=')
    categry = input('请输入您要筛选的分类:')
    startpage = int(input('请输入您要获取数据的起始页码：')) 
    endpage = int(input('请输入您要获取数据的截止页码：'))
    get_movielist_from_parmas(categry,startpage,endpage)

  
if __name__ == '__main__':
    main()