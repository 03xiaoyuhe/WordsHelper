import re

def is_alpha(s: str) -> bool:
    """
    检测字符串中是否只有英文字母，和允许的字符包括字母、单引号、双引号、方括号和圆括号
    :param s: 输入字符串
    :return: 如果字符串只包含英文字母，和常见符号，则返回 True，否则返回 False
    """
    return bool(re.match(r'^[a-zA-Z\'\"\]\[\(\)]+$', s))