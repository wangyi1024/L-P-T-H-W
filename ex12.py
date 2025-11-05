age = input ("How old are you?")            # print有end参数，input没有
height = input ("How tall are you?")
weight = input ("How much do you weigh?")

print (f"So, you're {age} old, {height} tall and {weight} heavy.")

print ("How old are you?", input())            # 这样写会让用户输入两次,函数参数是从内到外执行的