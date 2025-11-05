#   this one is like your scripts with argv
def print_two(*args):    # 定义函数print_two，使用*args接收任意数量的参数
    arg1, arg2 = args    # 将args元组中的值赋给arg1和arg2
    print(f"arg1: {arg1}, arg2: {arg2}")    # 函数的表达式

#   ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):    # 定义函数print_two_again，直接接收两个参数
    print(f"arg1: {arg1}, arg2: {arg2}")    # 函数的表达式

#   this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#   this one takes no arguments
def print_none():   # 定义函数print_none，不接收任何参数
    print("I got nothin'.")  # 函数的表达式


print_two("1", "2")  # 调用函数print_two，传入参数"1"和"2"
print_two_again("1", "2")   # 此时的函数为print_two_again，不等于print
                            # 此时args为("1", "2"),因此输出为arg1: 1, arg2: 2
print_one("First!")  # 调用函数print_one，传入参数"First!"
print_none()