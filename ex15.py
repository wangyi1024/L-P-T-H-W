from sys import argv

script, filename = argv

txt = open(filename)    # 打开指定的文件，将文件对象赋值给变量txt

print(f"Here's your file {filename}:")
print(txt.read())   # 读取文件内容，并打印出来

print("Type the filename again:")   # 显示提示信息
file_again = input("> ")    # 等待用户输入，将输入的文件名赋值给变量file_again

txt_again = open(file_again)

print(txt_again.read())