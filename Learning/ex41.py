import random   # 导入Python内置的随机数模块
from urllib.request import urlopen  # 用于打开和读取URL（网页地址），返回一个类似文件的对象
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []  # 存储从网络加载的单词

PHRASES = {             # 定义编程概念模板字典
    "class %%%(%%%):":  # 类继承模板
        "Make a class named %%% that is-a %%%.",    # 对应的英文描述
    "class %%%(object):\n\tdef __init__(self, ***)" :   # 构造函数模板
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":     # 类方法模板
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":                                  # 创建对象实例模板
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":                                 # 方法调用模板
        "From *** get the *** function, call it with params self @@@.",
    "***.*** = '***'":                              # 属性赋值模板
        "From *** get the *** attribute and set it to '***'."
}

  # do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":     # 检查命令行参数
      PHRASE_FIRST = True            # 如果参数是"english"，先显示英文描述
else:
      PHRASE_FIRST = False           # 否则先显示代码片段

  # load up the words from the website
for word in urlopen(WORD_URL).readlines():      # 读取所有行，.readline()只读取一行，并且返回的是字节字符串
    WORDS.append(str(word.strip(), encoding="utf-8"))    # 处理并添加到列表
# word.strip() - 去除字节字符串两端的空白字符
# str(..., encoding="utf-8") - 将字节字符串用UTF-8编码解码为普通字符串


def convert(snippet, phrase):       # 将模板转换为具体代码和描述
    class_names = [狗.capitalize() for 狗 in
    random.sample(WORDS, snippet.count("%%%"))]    
# snippet.count("%%%") - 统计代码模板中包含多少个 %%% 占位符
# .sample() - random 模块中的一个函数
# random.sample(WORDS, snippet.count("%%%")) - 从 WORDS 列表中随机选择指定数量的单词
# .capitalize() - 将单词首字母大写（类名的命名规范）
# 狗.capitalize() for 狗 in random_words - 对每个“狗”执行capitalize() 方法

    other_names = random.sample(WORDS, snippet.count("***"))    # 生成其他名称
    results = []        # 存储结果
    param_names = []    # 存储参数名

    for i in range(0, snippet.count("@@@")):    # 为每个参数位置生成参数
        param_count = random.randint(1,3)       # 随机参数数量(1-3)，可能的结果：1、2 或 3
        param_names.append(', '.join(           # 连接参数名为字符串
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:            # 处理代码和描述
        result = sentence[:]                    # [:] - 创建sentence副本赋值给result

          # fake class names
        for word in class_names:                 
            result = result.replace("%%%", word, 1) # 替换%%%占位符，字符串.replace(旧内容, 新内容, 替换次数)

          # fake other names
        for word in other_names:
            result = result.replace("***", word, 1) # 替换***占位符
          # fake parameter lists
        for word in param_names:                   
            result = result.replace("@@@", word, 1) # 替换@@@占位符

        results.append(result)                  # 将result的字符串赋值给results，并做成列表    

    return results                              # 返回转换后的代码和描述


try:            # 尝试执行 try 块中的代码，如果发生 EOFError 异常，就执行 except 块
    while True:                                 # 条件 True 永远为真，所以循环会一直执行
        snippets = list(PHRASES.keys())         
        # .key() - 字典形式，不能直接用，要用list转化成列表形式
        random.shuffle(snippets)                # -shuffle() - 随机打乱顺序

        for snippet in snippets:                # 遍历每个模板
            phrase = PHRASES[snippet]           # 获取对应的描述
            question, answer = convert(snippet, phrase) # 将question和answer分别解包为snippet, phrase的值
            if PHRASE_FIRST:                    
                question, answer = answer, question # 根据设置交换问题和答案

            print(question)                     # 显示问题

            input("> ")                         
            print(f"ANSWER: {answer}\n\n")      # 显示答案
except EOFError:                                # 捕获Ctrl-D退出信号
    print("\nBye")                              # 退出程序