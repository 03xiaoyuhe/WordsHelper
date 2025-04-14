from llm_client import query_llm
from word_model import Word

def story(words):
    prompt = f"""
在接下来的每一个对话，我都将为你提供一系列我在学习英语过程中遇到的困难单词，而你需要帮助我记住这些单词，你需要完成的任务是将这些单词连词成篇，写一篇英文故事，另外也要遵守以下要求：
1.将我提供给你的单词在文章中加粗
2.文章中出现的其他单词的难度应该比我的生词简单
3.行文逻辑通畅，注意上下文逻辑，最好浑然一体，使得我在阅读时推出单词意思是自然而然的
4.可以把故事写的生动有趣，或是生词妙用，让我一下就可以记住生词
5.确保故事中使用了提供的所有生词
6.请按照以下格式返回故事：

### <故事名>

<故事内容>

生词：
{words}

确保你遵守以上要求，只用提供英文故事，不要提供其他任何内容。请开始你的故事。
    """
    response = query_llm(prompt)
    return response

def summary(story):
    prompt = f"""
请你为我提供一篇英文故事的中文精翻，要求如下：
1.故事的内容是我提供给你的英文故事
2.精翻要突出故事的主要情节和主题
3.精翻要用中文表达
4.请按照以下格式返回大意：
### <故事名>
<故事内容的中文大意>

请开始你的工作，用户提供的故事是：
{story}
"""
    response = query_llm(prompt)
    return response


def word(word : Word) -> Word:
    """
    根据用户提供的单词生成短语、短语翻译、读音和词汇中文释义，并返回元组
    :param word: 用户提供的单词
    :return: (单词, 短语, 短语翻译, 读音, 词汇中文释义)
    """
    if word.chinese_definition is  None:
    # 生成词汇中文释义
        chinese_definition_prompt = f"""
你是一个非常聪明的英语学习助手，你现在要完成以下任务：
1. 用户会提供给你一个单词，而你需要提供该单词的主要中文释义，提供的中文释义要简短易懂，三个以内
2. 只需要返回中文释义，不要提供其他任何内容
请开始你的工作，用户提供的单词是：
{word.word}
"""
        chinese_definition = query_llm(chinese_definition_prompt)
        word.set_chinese_definition(chinese_definition)

    # 生成短语
    phrase_prompt = f"""
你是一个非常聪明的英语学习助手，你现在要完成以下任务：
1. 用户会提供给你一个单词及其中文释义，而你要把这个单词扩充为英文短语，以使用户记忆更加方便
2. 生词应该加粗显示
3. 短语应生动有趣，以达到方便记忆的效果
4. 短语应仅使用3-4个词语，简短易记
5. 短语中单词释义和用户提供的中文释义要一致
6. 仅提供一个英文短语，并恰当的反应用户所需记忆的所有中文释义
7. 只提供一行英文短语，不要提供其他任何内容
8. 短语中的其他词汇不能难于用户提供的单词
请开始你的工作，
用户提供的单词是：
{word.word}
中文释义是：
{word.chinese_definition}
"""
    phrase = query_llm(phrase_prompt)

    # 生成短语翻译
    phrase_translation_prompt = f"""
你是一个非常聪明的英语学习助手，你现在要完成以下任务：
1. 用户会提供给你一个或多个短语，而你需要提供这些短语的中文翻译
2. 只需要返回一行中文翻译，如果是多个短语翻译，使用"；"分割，不要提供其他任何内容
请开始你的工作，用户提供的短语是：
{phrase}
"""
    phrase_translation = query_llm(phrase_translation_prompt)
    word.set_phrase(phrase)
    word.set_phrase_translation(phrase_translation)

    # 生成读音
    pronunciation_prompt = f"""
你是一个非常聪明的英语学习助手，请你给出单词：{word.word} 的国际音标读音(英式)
只需要返回读音，不要提供其他任何内容
"""
    pronunciation = query_llm(pronunciation_prompt)
    word.set_pronunciation(pronunciation)

    # 返回元组
    return word