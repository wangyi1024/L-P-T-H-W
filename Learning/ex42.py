## Animal is-a object (yes, sort of confusing) look at the extra credit（附加练习）
class Animal(object):   # Animal 是一个基类，继承自 object
    pass    # 表示这个类暂时没有属性和方法

## ??
class Dog(Animal):      # Dog 继承自 Animal

    def __init__(self, name):    # __init__ 是构造函数，创建对象时自动调用
        ## ??
        self.name = name    # 给狗对象设置名字属性

## ??
class Cat(Animal):      # Cat 也继承自 Animal

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):   # Person 继承自 object

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):     # Employee 继承自 Person

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)    # 调用Person类的构造函数
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass
     
## ??
class Salmon(Fish):
    pass
      
## ??
class Halibut(Fish):
    pass
      
      
## rover is-a Dog
rover = Dog("Rover")
      
## ??
satan = Cat("Satan")
     
## ??
mary = Person("Mary")
      
## ??
mary.pet = satan
      
## ??
frank = Employee("Frank", 120000)
      
## ??
frank.pet = rover
      
## ??
flipper = Fish()
      
## ??
crouse = Salmon()
      
## ??
harry = Halibut()