types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print (x)
print (y)

print (f"I said: {x}")
print (f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?!{}"

print (joke_evaluation.format(hilarious))       # .format(hilarious) "."调用该字符串的format方法
                                                # {} 被替换为 hilarious 的值 (False)
                                                # 实际上相当于print(f"Isn't that joke so funny?!{hilarious}")
# print(f"Isn't that joke so funny?!{hilarious}")


w = "This is the left side of ..."
e = "a string with a right side."

print (w + e)