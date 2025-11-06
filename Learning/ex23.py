import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()     # 读取一行

    if line:    # 如果还有内容（非空行）
        print_line(line, encoding, errors)      #处理该行
        return main(language_file, encoding, errors)    # 递归调用自己
  # 递归结束条件：读到空行时不再调用自己   

def print_line(line, encoding, errors):
    next_lang = line.strip()    # 去掉换行符和空白符
    raw_bytes = next_lang.encode(encoding, errors=errors)   #字符串编码为字节
    cooked_string = raw_bytes.decode(encoding, errors=errors)   # 字节解码为字符串

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, encoding, error)

"""

main() 第1次调用
├── 读取第1行: "Afrikaans"
├── print_line() → 显示第1行
└── main() 第2次调用
    ├── 读取第2行: "አማርኛ"  
    ├── print_line() → 显示第2行
    └── main() 第3次调用
        ├── 读取第3行: "Аҧсшәа"
        ├── print_line() → 显示第3行
        └── main() 第4次调用
            ├── ...
            └── main() 第95次调用
                ├── 读取第95行: "中文"
                ├── print_line() → 显示第95行
                └── main() 第96次调用
                    ├── 读取第96行: "" (空行，文件结束)
                    └── 条件不满足，函数结束 ← 递归终止！
                    
                    """