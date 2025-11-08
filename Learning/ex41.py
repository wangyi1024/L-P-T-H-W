import random   # 导入Python内置的随机数模块
from urllib.request import urlopen  # 用于打开和读取URL（网页地址）
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
for word in urlopen(WORD_URL).readlines():      # 从网络读取单词
    WORDS.append(str(word.strip(), encoding="utf-8"))    # 处理并添加到列表


def convert(snippet, phrase):       # 将模板转换为具体代码和描述
    class_names = [w.capitalize() for w in
    random.sample(WORDS, snippet.count("%%%"))]     # 生成类名（首字母大写）
    other_names = random.sample(WORDS, snippet.count("***"))    # 生成其他名称
    results = []        # 存储结果
    param_names = []    # 存储参数名

    for i in range(0, snippet.count("@@@")):    # 为每个参数位置生成参数
        param_count = random.randint(1,3)       # 随机参数数量(1-3)
        param_names.append(', '.join(           # 连接参数名为字符串
            random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:            # 处理代码和描述
        result = sentence[:]                    # 复制字符串

          # fake class names
        for word in class_names:                 # 替换%%%占位符
            result = result.replace("%%%", word, 1) # 替换***占位符

          # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

          # fake parameter lists
        for word in param_names:                   # 替换@@@占位符
            result = result.replace("@@@", word, 1) 

        results.append(result)                  # 添加到结果列表    

    return results                              # 返回转换后的代码和描述


  # keep going until they hit CTRL-D
try:
    while True:                                 # 无限循环
        snippets = list(PHRASES.keys())         # 获取所有模板键
        random.shuffle(snippets)                # 随机打乱顺序

        for snippet in snippets:                # 遍历每个模板
            phrase = PHRASES[snippet]           # 获取对应的描述
            question, answer = convert(snippet, phrase) # 转换模板
            if PHRASE_FIRST:                    # 根据设置交换问题和答案
                question, answer = answer, question

            print(question)                     # 显示问题

            input("> ")                         
            print(f"ANSWER: {answer}\n\n")      # 显示答案
except EOFError:                                # 捕获Ctrl-D退出信号
    print("\nBye")                              # 退出程序