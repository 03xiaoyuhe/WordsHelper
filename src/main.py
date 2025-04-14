import time
import random

from readWords import *
from makeFile import makefile  # 引入 makefile 函数
from mutiProcess import process_words_and_stories  # 引入多线程处理函数

def main():
    # 加载单词文件
    words = load_file()
    if not words:
        return  # 如果未选择文件，直接退出

    words = list(set(words))  # 去重
    random.shuffle(words)  # 随机打乱顺序
    
    # 将单词分组
    words_list = group_words([word.word for word in words], group_size=20)

    # 调用封装的多线程处理函数
    words_ans, stories_with_summaries = process_words_and_stories(words, words_list)

    # 写入文件
    makefile(words_ans, stories_with_summaries)
    
if __name__ == "__main__":
    try:
        main()
        # 运行主函数
    except Exception as e:
        # 捕获异常并打印错误信息
        print("\n程序运行时发生错误：")
        print(e)
        print("\n程序将在 10 秒后退出...")
        time.sleep(10)
    else:
        # 如果没有异常，正常退出
        input("按回车键退出...")