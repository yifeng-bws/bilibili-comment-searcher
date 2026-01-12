from bilibili_api import get_commments
from wordcloud_gen import get_cloud
import webbrowser

def main():
    print('=' * 30)
    print('bilibili评论获取器')

    bvid = input('请输入视频BV号')
    max_chars = int(input('请输入获取的最大字符数量'))

    comments = get_commments(bvid,max_chars=max_chars)
    get_cloud(comments)

    user = input('是否使用浏览器打开当前网页？')
    if user == '是':
        webbrowser.open(f'https://www.bilibili.com/video/{bvid}/')
    else:
        print('进程已结束')

if __name__ == '__main__':
    main()