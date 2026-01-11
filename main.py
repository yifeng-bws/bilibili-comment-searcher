from bilibili_api import get_commments
from wordcloud_gen import get_cloud

print('=' * 30)
print('bilibili评论获取器')

bvid = input('请输入视频BV号')
max_chars = int(input('请输入获取的最大字符数量'))

comments = get_commments(bvid,max_chars=max_chars)
get_cloud(comments)