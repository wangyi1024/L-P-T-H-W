from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line, how?
in_file = open(from_file, 'r', encoding='utf-16')
indata = in_file.read()     # 读取文件内容，存入变量indata

print(f"The input file is {len(indata)} bytes long")        # 显示文件的字符数
# len()函数用于获取字符串的长度

print(f"Does the output file exist? {exists(to_file)}")
# exists()函数用于检查文件是否存在，返回True或False

print("Ready, hit RETURN to continue, CTRL-C to abort.")
input(">")

out_file = open(to_file, 'w')   # 打开目标文件准备写入
out_file.write(indata)      # 将读取的内容写入目标文件

print("Alright, all done.")

out_file.close()
in_file.close()