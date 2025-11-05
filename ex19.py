def cheese_and_crackers(cheese_count, boxes_of_crackers):   # 定义函数
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)     # 调用函数，传入数字参数


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)   # 调用函数，传入变量参数

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)     # 调用函数，传入数学表达式参数



print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)  
# 调用函数，传入变量和数学表达式参数