import requests
import re

# 设置BV号以及最大字符数
bvid = "BV1xYBrBxEof"
max_chars = 300


def clean_text(text):
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'@\S+', '', text)
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def get_commments(bvid,max_chars):
    # 获取视频信息
    info_url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
    info_res = requests.get(info_url, headers={
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://www.bilibili.com'
    }, timeout=10)

    info_data = info_res.json()

    if info_data['code'] == 0:
        aid = info_data['data']['aid']

        # 获取评论
        comment_url = "https://api.bilibili.com/x/v2/reply"
        params = {
            'type': 1,
            'oid': aid,
            'pn': 1,
            'ps': 20,
            'sort': 2
        }

        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Referer': f'https://www.bilibili.com/video/{bvid}',
            'Accept': 'application/json'
        }

        response = requests.get(comment_url, params=params, headers=headers, timeout=10)
        data = response.json()

        all_text = ""

        if data['code'] == 0:
            replies = data['data'].get('replies', [])

            for reply in replies:
                msg = reply['content']['message']
                clean_msg = clean_text(msg)
                if clean_msg:
                    all_text += clean_msg + " "

                if len(all_text) >= max_chars:
                    break

        # 保存到文件
        #with open('comments.txt', 'w', encoding='utf-8') as f:
        #    f.write(all_text[:max_chars])
        return all_text[:max_chars]

if __name__ == '__main__':
    comments = get_commments(bvid,max_chars)
    with open('comments.txt','w',encoding='utf-8') as file:
        file.write(comments)