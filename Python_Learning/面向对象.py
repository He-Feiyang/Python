'''
Class: 具有相同的属性和方法的的对象的集合。class定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
类变量（类属性）: 定义在类中且在函数体之外，类变量在整个实例化的对象中是公用的
实例变量（实例属性）：定义在类的函数内部，形式’self.变量名’。
局部变量：定义在方法中的变量，只作用于该方法内部，函数执行完成后局部变量也会被销毁

数据成员：类变量或者实例变量，用于处理类及其实例对象的相关的数据


方法：类中定义的函数
方法重写：荣国从父类继承的方法不能满足子类的需求，可以对其进行改写（override）、
继承：一个派生类（derived class）继承基类（base class）的字段和方法。
实例化：创建一个类的实例，类的具体对象

对象：通过类定义的数据结构实例。对象包括两个数据成员：（类变量、实例变量）和方法
对象的两个特征： 属性 行动

'''
# class ClassName:
#     '类文档字符串'
#     class_suite #类体

class Employee:
    '所有员工的基类'
    employCount = 0 #类变量,其值会在这个类的所有实例之间共享。

    def __init__(self, name, salary): #__init__()这是一个特殊的方法，称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
        self.name = name #self是类的实例
        self.salary = salary
        Employee.employCount += 1

    def displayCount(self): # 类的方法，用def定义，与函数定义不同，类方法必须包含参数self，且为第一个参数
        print("Total Employee %d" % Employee.employCount)
    
    def displayEmployee(self):
        print("Name: {}, Salary: {}".format(self.name, self.salary))
# 一旦定义了一个类，就会创建一个具有相同名称的新类对象。

#self是类的实例
class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()


#创建实例对象
'创建 Employee类的第一个对象'
emp1 = Employee('Zara', 2000) 
'创建 Employee类的第二个对象'
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print('Total Employee %d', Employee.employCount)

emp1.age = 7 # 添加一个'age'属性
emp1.age = 8 # 修改'age'属性
del emp1.age # 删除'age'属性

# getattr(obj, name[, default]) 访问对象的属性
# hasattr(obj, name)  检查是否存在属性
# setattr(obj, name[, vale])  设置属性。若属性不存在，则创建一个
# delattr(obj, name)  删除属性

print('emp1是否有age属性？{}'.format(hasattr(emp1,'age')))

setattr(emp2, 'age', 18)
print('emp2的age为{}'.format(getattr(emp2,'age')))


#python的内置类属性
'''
__dict__ 类的属性（包含一个字典，由类的数据属性组成）
__doc__ 类的文档字符串
__name__ 类名
__module__ 类定义所在的模块
__bases__ 类的所有父类构成元素（包含一个由所有父类组成的元组）
'''
print('Employee.__name__',Employee.__name__)
print('Employee.__doc__:',Employee.__doc__)
print('Employee.__bases__:',Employee.__bases__)
print('Employee.__module__:',Employee.__module__)
print('Employee.__dict__:',Employee.__dict__)



# python 对象销毁（垃圾回收）
# 使用”引用计数”来跟踪回收垃圾，当创建对象时，Python内部会创建一个该对象的引用计数器，
# 当引用计数器为0时，Python解释器会在适当的时机回收垃圾对象占用的内存空间
a = 40      # 创建对象<40>
b = a       # 增加对象<40>的引用计数
c = [b]     # 增加对象<40>的引用计数

del a       # 减少对象<40>的引用计数
b = 100     # 减少对象<40>的引用计数
c[0] = -1   # 减少对象<40>的引用计数


# 类的继承
# 通过继承创建的新类成为子类或派生类，被继承的类称为基类、父类或超类
class Parent:
    parentAttr = 100

    def __init__(self):
        print ('调用父类构造函数')

    def parentMethod(self):
        print('调用父类方法')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print('父类属性：', Parent.parentAttr)

    def myMethod(self):
        print('调用父类方法')

class child(Parent):
    def __init__(self):
        super(child,self).__init__()
        print('调用子类构造方法')

    def childMethod(self):
        print ('调用子类方法')

    def myMethod(self):   # 方法重写
        print('调用子类方法')

c = child() 
c.childMethod()
c.setAttr(200)
c.getAttr()
c.myMethod() # 子类调用重写方法

# 封装
# 类的私有属性
# 用两个下划线开头，声明该属性为私有。如：__privateAttrs。
# 私有属性不能在类的外部被使用或直接访问，在类的方法中使用self.__privateAttrs调用
class JustCounter:
    __secretCount = 0 # 类变量，私有变量
    publicCount = 0   # 类变量，公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
#print (counter.__secretCount) # 报错，实例不能访问私有变量


# 类的私有方法
# 用两个下划线开头，声明该方法为私有，不能在类的外部调用，比如： def __privateMethods
# 在类的内部使用 self.__privateMethods 的形式调用


# 命名空间
def outer_function():
    a = 20

    def inner_funciton():
        a = 30
        print('a1 =',a) 
    
    inner_funciton() # 此函数退出后，对象30已将被销毁
    print('a2 =',a)

a = 10
outer_function() # 此函数执行完成后，对象20已经被销毁
print('a3 =', a)
# 注意对象的作用域

# 通过global关键字，改变作用域
def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)

a = 10
outer_function()
print('a =', a)

print(JustCounter.count) # 好像地址啊哈哈

import sys
print(sys.path)

a =10
print(id(a),type(a),a)

