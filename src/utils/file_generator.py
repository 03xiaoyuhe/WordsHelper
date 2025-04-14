from tkinter import Tk, filedialog
import os
from datetime import datetime

from config.settings import *

def makefile(words: list, stories_with_summaries):
    """
    将单词和故事写入文件
    :param words: 单词列表
    :param stories_with_summaries: 每个故事及其对应的大意
    """
    # 检查是否配置了 output_path
    if output_dir:
        # 使用配置的输出路径，并按照日期命名文件
        date_str = datetime.now().strftime("%Y-%m-%d")  # 获取当前日期
        file_path = os.path.join(output_dir, f"{date_str}.md")
        print(f"文件将保存到配置的路径：{file_path}")
    else:
        # 使用 tkinter 文件对话框选择保存路径
        Tk().withdraw()  # 隐藏主窗口
        file_path = filedialog.asksaveasfilename(
            defaultextension=".md",
            filetypes=[("Markdown 文件", "*.md"), ("所有文件", "*.*")],
            title="选择保存文件的位置"
        )
        if not file_path:
            print("未选择保存路径，操作已取消。")
            return

    # 生成文件内容
    words_str = "\n".join([f"|{word.word}|{word.phrase}|{word.phrase_translation}|{word.pronunciation}|{word.chinese_definition}|" for word in words])
    stories_content = "\n\n".join([f"{story}\n\n{summary}" for story, summary in stories_with_summaries])
    content = f"""
# 生词速查
|    生词   |   短语   |  短语释义  |词汇读音|词汇中文释义|
| --------- | ------- | --------- |--------|-----------|
{words_str}

# 生成的故事
{stories_content}
    """
    # 写入文件
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"文件已生成：{file_path}")
