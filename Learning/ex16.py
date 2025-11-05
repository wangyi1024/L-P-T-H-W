from sys import argv

script, filename = argv

print(f"We's going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

try:
    input("?")  # 用户按下回车继续
except KeyboardInterrupt:       # 捕获用户按下 CTRL-C 的情况
    print("\n操作已取消！")     # 提示用户操作已取消
    exit()      # 退出程序

print("Opening the file...")
target = open(filename, 'w')    # 'w' 模式会清空文件内容

print("Truncating the file. Goodbye!")
target.truncate()   # 清空文件内容，在 'w' 模式下其实不需要这一步

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")   # 获取用户输入的三行内容
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n")   # 写入第一行并添加换行符
target.write(line2 + "\n")   # 写入第二行并添加换行符
target.write(line3 + "\n")   # 写入第三行并添加换行符


print("And finally, we close it.")
target.close()      # 关闭文件，应该是close而不是Close

text = open(filename)

print("Here is the content of the file:")
print(text.read())

text.close()