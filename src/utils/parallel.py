from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

import core.word_processor as function

def process_story_and_summary(words):
    """
    同时生成故事和对应的大意
    :param words: 单词列表
    :return: (story, summary)
    """
    try:
        story = function.story(words)
        summary = function.summary(story)
        return story, summary
    except Exception as e:
        print(f"处理故事和大意时出错：{e}")
        return None, None

def process_word(word):
    """
    处理单词扩展
    :param word: 单词
    :return: 单词扩展结果
    """
    try:
        return function.word(word)
    except Exception as e:
        print(f"处理单词扩展时出错：{e}")
        return None

def process_words_and_stories(words, words_list):
    """
    使用多线程并发处理单词扩展和故事生成
    :param words: 单词列表
    :param words_list: 分组后的单词列表
    :return: 处理后的单词扩展结果和故事与大意
    """
    with ThreadPoolExecutor() as executor:
        # 创建两个线程池任务
        print("正在生成故事和对应的大意...")
        story_summary_futures = [executor.submit(process_story_and_summary, group) for group in words_list]
        print("故事和大意任务提交完成，共有任务数：", len(story_summary_futures))
        
        print("正在生成单词扩展...")
        word_futures = [executor.submit(process_word, word) for word in words]
        print("单词扩展任务提交完成，共有任务数：", len(word_futures))
        
        # 等待所有任务完成
        print(f"正在等待任务完成...")

        # 并发处理故事和单词扩展
        stories_with_summaries = []
        words_ans = []

        for future in tqdm(as_completed(story_summary_futures + word_futures),
                           total=len(story_summary_futures) + len(word_futures),
                           desc="处理进度"):
            try:
                result = future.result()
                if isinstance(result, tuple):  # 如果是故事和大意
                    stories_with_summaries.append(result)
                elif result is not None:  # 如果是单词扩展
                    words_ans.append(result)
            except Exception as e:
                print(f"任务执行时出错：{e}")

    return words_ans, stories_with_summaries