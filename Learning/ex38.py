ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding:", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.") # len() 函数用于获取列表的长度

print("There we go:", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])  # whoa! fancy
print(stuff.pop())
print(' '.join(stuff))  # 用空格连接stuff列表中的所有元素
print('#'.join(stuff[3:5]))  # 用#连接stuff列表中索引3到4的元素，即第四个和第五个元素
# .join() 方法用于将列表中的元素连接成一个字符串，指定的字符串作为分隔符