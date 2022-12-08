'''
Class: 具有相同的属性和方法的的对象的集合。class定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
类变量: 类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不用做实例变量使用。
数据成员：类变量或者实例变量，用于处理类及其实例对象的相关的数据
方法重写：荣国从父类继承的方法不能满足子类的需求，可以对其进行改写（override）、
局部变量：定义在方法中的变量，只作用于当前实例的类
实例变量：在类的声明中，属性是用变量来表示的，在类声明内部但在类的其他成员方法之外声明的
继承：一个派生类（derived class）继承基类（base class）的字段和方法。
实例化：创建一个类的实例，类的具体对象
方法：类中定义的函数
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法
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

    def displayCount(self): 
        print("Total Employee %d" % Employee.employCount)
    
    def displayEmployee(self):
        print("Name: {}, Salary: {}".format(self.name, self.salary))

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
__module__ 类定义所在的模块
'''