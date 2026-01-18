from wordcloud import WordCloud
import jieba
from src.bilibili_api import get_commments

def get_cloud(text):
    # 分词
    words = jieba.lcut(text)
    s = ' '.join(words)

    # 词云
    w = WordCloud(scale=7, font_path='方正字体.TTF', background_color='white')
    w.generate(s)
    w.to_file('词云.png')

def main():
    bvid = "BV1xYBrBxEof"
    max_chars = 300

    comments = get_commments(bvid,max_chars=max_chars)
    get_cloud(comments)

if __name__ == '__main__':
    main()