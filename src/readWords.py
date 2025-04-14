from tkinter import Tk, filedialog
import model as m
import helper as h


def load_file():
    """
    使用文件对话框选择单词文件并读取内容
    :return: 单词列表
    """
    # 使用 tkinter 文件对话框选择单词文件路径
    Tk().withdraw()  # 隐藏主窗口
    file_path = filedialog.askopenfilename(
        filetypes=[("文本文件", "*.txt"), ("所有文件", "*.*")],
        title="选择单词文件"
    )
    if not file_path:
        print("未选择单词文件，操作已取消。")
        return None

    # 读取单词列表
    words = get_words(file_path)
    return words

def read_lines(file_path):
    """
    读取文件内容，将每一行作为一个字符串存入列表
    :param file_path: 文件路径
    :return: 包含每一行内容的列表
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            # 读取所有行并去除每行末尾的换行符
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
        return []
    except Exception as e:
        print(f"读取文件时出错: {e}")
        return []


def get_words(file_path):
    lines = read_lines(file_path)
    words = []
    for line in lines:
        # 假设每行的单词用空格分隔
        temp = line.split(" ")
        word = m.Word(temp[0])
        if len(temp) > 1:
            for i in temp[1:]:
                if h.is_alpha(i):
                    word.word += " " + i
                else:
                    if word.chinese_definition is None:
                        word.set_chinese_definition(i)
                    else:
                        word.chinese_definition += " " + i
        words.append(word)
    # 去除重复的单词
    words = list(set(words))

    return words


def group_words(words, group_size=20):
    """
    将单词列表按指定大小分组，并智能处理剩余单词
    :param words: 单词列表
    :param group_size: 每组的单词数量
    :return: 分组后的列表
    """
    # 初步分组
    groups = [words[i:i + group_size] for i in range(0, len(words), group_size)]
    
    # 检查最后一组的长度
    if len(groups) > 1 and len(groups[-1]) // (len(groups) - 1) <= group_size // 5:
        # 将最后一组的单词均匀分配到前面的组中
        remaining_words = groups.pop()  # 取出最后一组
        for i, word in enumerate(remaining_words):
            groups[i % len(groups)].append(word)  # 均匀分配到前面的组中
    return groups