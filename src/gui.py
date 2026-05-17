import tkinter as tk
from bilibili_api import get_comments
from wordcloud_gen import get_cloud
from tkinter import messagebox

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('b站词云生成器')
        self.root.geometry('500x400')
        self.root.config(background='skyblue')
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="BV号:").pack(pady=5)
        self.bvid_entry = tk.Entry(self.root, width=30)
        self.bvid_entry.pack()
        
        tk.Label(self.root, text="最大字符数:").pack(pady=5)
        self.chars_entry = tk.Entry(self.root, width=30)
        self.chars_entry.pack()
        
        self.btn = tk.Button(self.root, text="生成词云", command=self.generate)
        self.btn.pack(pady=20)
        
        self.status = tk.Label(self.root, text="就绪", fg="gray")
        self.status.pack(side="bottom", pady=10)

    def generate(self):
        bvid = self.bvid_entry.get().strip()
        max_chars = int(self.chars_entry.get())
        
        self.status.config(text="获取评论中...")
        self.root.update()
        comments = get_comments(bvid, max_chars)
        get_cloud(comments)
        self.status.config(text="词云生成成功")
        messagebox.showinfo("完成", "词云已保存为 词云.png")

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = App()
    app.run()
