formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print (formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))   # 不加引号被视为变量，加引号被视为字符串
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format)
print(formatter.format(
        "Try your",
        "Own text here","\n"
        "Maybe a poem","\n"
        "Or a song about fear"
    ))