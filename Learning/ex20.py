from sys import argv

script, input_file = argv

def print_all(狗):
    print(狗.read())     # 读取并打印文件内容

def rewind(狗):
    狗.seek(0)       # 将文件指针移动到文件开头

def print_a_line(line_count, 狗):
    print(line_count, 狗.readline(), end = "")     # 读取并打印文件中的一行，指针会自动移动到下一行
# print 函数中的 end="" 参数用于避免在打印时添加额外的换行符
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)     # 调用函数，打印整个文件内容

print("Now let's rewind, kind of like a tape.")

rewind(current_file)        # 调用函数，回到文件开头

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)    # 调用函数，打印第一行

current_line += 1
print_a_line(current_line, current_file)    # 调用函数，打印第二行

current_line += 1   # 相当于 current_line = current_line + 1
print_a_line(current_line, current_file)    # 调用函数，打印第三行