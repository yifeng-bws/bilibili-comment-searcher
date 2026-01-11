from wordcloud import WordCloud
import jieba

def get_cloud(text):
    # 分词
    words = jieba.lcut(text)
    s = ' '.join(words)

    # 词云
    w = WordCloud(scale=7, font_path='方正字体.TTF', background_color='white')
    w.generate(s)
    w.to_file('词云.png')

if __name__ == '__main__':
    with open('comments.txt','r',encoding='utf-8') as file:
        comments = file.read()

    get_cloud(comments)