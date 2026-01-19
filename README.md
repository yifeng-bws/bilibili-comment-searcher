# Bilibili评论词云生成器

这是一个用于生成B站（bilibili）视频评论词云的 Python 项目。通过输入视频的 BV 号，程序可以抓取评论并自动生成词云图片，帮助用户快速了解视频评论区的高频词汇。

## 🚀 功能特点

- 📥 自动抓取指定B站视频的评论区
- 🧹 评论内容清洗（去除表情、@用户、链接等）
- ☁️ 自动生成中文词云图片
- 🌐 可选择是否用浏览器打开对应视频页面
- ⚙️ 支持自定义最大字符数量

## 📁 项目结构
bilibili-comment-searcher/

├── src/

│ ├── main.py # 主程序入口

│ ├── bilibili_api.py # 评论获取与清洗模块

│ └── wordcloud_gen.py # 词云生成模块

├── requirements.txt # 依赖包列表

├── README.md # 项目说明文档

└── LICENSE # 许可证文件

## 🔧 安装与运行

### 1. 克隆仓库

```bash
git clone https://github.com/你的用户名/bilibili-comment-searcher.git
cd bilibili-comment-searcher
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 运行程序

```bash
python main.py
```

按照提示输入视频 BV 号和最大字符数即可

## 📦 依赖库

- requests
- jieba
- wordcloud

可通过以下命令一键安装：

```bash
pip install requests jieba wordcloud
```

## 📸 示例运行

```text
==============================
bilibili评论获取器
请输入视频BV号：BV1xYBrBxEof
请输入获取的最大字符数量：500
是否使用浏览器打开当前网页？是/否
```

运行后会在当前目录生成 词云.png

## 📌 注意事项

- 需要确保已安装中文字体（如 方正字体.TTF），否则词云可能无法正常显示中文
- 评论抓取受B站API限制，可能无法获取全部评论
- 请遵守B站用户协议，合理使用数据
- 输入参数后，程序运行时可能会出现英文字符，属于jieba使用时的正常现象


## 🔍 文件说明

- main.py: 主程序入口，处理用户交互
- bilibili_api.py: 负责从B站API获取评论并清洗数据
- wordcloud_gen.py: 使用jieba分词和wordcloud生成词云图片


## 📄 许可证

本项目基于 MIT 许可证开源


## 📝 TODO

- 添加更多评论分页获取功能
- 支持自定义词云形状和颜色
- 添加停用词过滤功能
- 支持导出清洗后的评论文本