import urllib.request as request
import ssl

#将获取的图片写入本地文件
def write_image_data(image_data,url):
    #wb表示写入二进制文件
    with open('image'+'.jpg','wb') as f:
        print('写入图片')
        f.write(image_data)

#将获取的视频写入本地文件
def write_video_data(video_data,url):
    print('正在获取')
    filename = url[-10:]
    with open(filename + '.mp4','wb') as f:
        f.write(video_data)
        print('视频下载成功'+filename)
        
def main():
    # 图片的地址
    imageurl = 'https://qnwww2.autoimg.cn/youchuang/g27/M05/AC/4C/autohomecar__wKgHHls8sYOAZc13AATZCypW09E301.JPG?imageView2/1/w/590/h/344'
    #视频地址
    videourl = 'https://n6-pl-agv.autohome.com.cn/video-0/E3BD4E39114FD258/2018-07-04/92484984FFA5F958-300.mp4?key=D59711FBF6AF700E27D41B04181F8C92&time=1530689417'
    #构造亲求对象
    headers = {
         'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }

    context = ssl._create_unverified_context()

    image_req = request.Request(imageurl,headers=headers)

    video_req = request.Request(videourl,headers=headers)


    #获取响应结果
    image_response = request.urlopen(image_req,context=context)
    video_response = request.urlopen(video_req,context=context)
    
    #打印请求状态码
    print('图片请求成功'+str(image_response.status))
    print('视频请求成功'+str(video_response.status))
    #读取数据，此时为字节流类型
    #写入视频后者音频、图片文件的时候不要打印
    # 边打印边写入数据到文件，是会出问题的
    # print(image_response.read())

    # if image_response.status == 200:
    #     #字节流（二进制）
    #     image_data = image_response.read()
    #     write_image_data(image_data,imageurl)

    #视频数据
    if video_response.status == 200:
        video_data = video_response.read()
        #调用方法将视频写入本地文件
        write_video_data(video_data,videourl)
    
if __name__ == '__main__':
    main()

