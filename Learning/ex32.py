the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:        # 重复执行列表中的每一个元素，直到列表结束
    print(f"This is count {number}")

# same as above
for fruit in fruits:    # fruit 直接被定义，循环结束后fruit = 'apricots'
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []   # 创建一个空列表，用于存放后续添加的元素

# then use the range function to do 0 to 5 counts
for i in range(0, 6):   # range(0,6) 生成从0到5的整数序列,不包括6
    print(f"Adding {i} to the list.")
# append is a function that lists understand
    elements.append(i)  # 将当前的 i 添加到 elements 列表的末尾
"""
第1次循环:i=0 → elements = [0]
第2次循环:i=1 → elements = [0, 1]
第3次循环:i=2 → elements = [0, 1, 2]
第4次循环:i=3 → elements = [0, 1, 2, 3]
第5次循环:i=4 → elements = [0, 1, 2, 3, 4]
第6次循环:i=5 → elements = [0, 1, 2, 3, 4, 5]  """





# now we can print them out too
for i in elements:
    print(f"Element was: {i}")