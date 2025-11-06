def break_words(stuff):
    """This function breaks words for us."""    # 函数注释，说明函数的作用
    words = stuff.split(' ')    # Split 是将字符串按照指定的分隔符分割成列表
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)    # sorted() 函数返回一个新的排序列表，而不改变原列表
# 排序时，默认是按字母顺序排序

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)     # pop(0) 是移除并返回列表的第一个元素
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)    # pop(-1) 是移除并返回列表的最后一个元素
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)