class Word:
    def __init__(self, word: str):
        self.word = word.lower()
        self.chinese_definition = None
        self.phrase = None
        self.phrase_translation = None
        self.pronunciation = None
        self.count = 0

    def set_chinese_definition(self, chinese_definition: str):
        self.chinese_definition = chinese_definition.replace("\n", ";").replace("，", ";").replace("。", ";")  # 去除换行符

    def set_phrase(self, phrase: str):
        self.phrase = phrase.replace("\n", ";").replace("，", ";").replace("。", ";")  # 去除换行符

    def set_phrase_translation(self, phrase_translation: str):
        self.phrase_translation = phrase_translation.replace("\n", ";").replace("，", ";").replace("。", ";")  # 去除换行符

    def set_pronunciation(self, pronunciation: str):
        self.pronunciation = pronunciation.replace("\n", ";").replace("，", ";").replace("。", ";")  # 去除换行符

    def set_count(self, count: int):
        self.count = count

    def increment_count(self):
        self.count += 1

    def __repr__(self):
        return f"Word({self.word}, {self.phrase}, {self.phrase_translation}, {self.pronunciation}, {self.chinese_definition})"

    def __eq__(self, other):
        """
        判断两个 Word 对象是否相等
        """
        if isinstance(other, Word):
            return self.word == other.word
        return False

    def __hash__(self):
        """
        返回 Word 对象的哈希值
        """
        return hash(self.word)
