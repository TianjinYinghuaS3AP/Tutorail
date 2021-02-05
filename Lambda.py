# -*- coding: UTF-8 -*-
''' Last editing date: 2021/02/05 16:53:46'''


'''
Python中，lambda函数也叫匿名函数，及即没有具体名称的函数，它允许快速定义单行函数。
'''

'''
lambda与def的区别：
    1）def创建的方法是有名称的，而lambda没有。
    2）lambda会返回一个函数对象，但这个对象不会赋给一个标识符，而def则会把函数对象赋值给一个变量（函数名）。
    3）lambda只是一个表达式，而def则是一个语句。
    4）lambda表达式” : “后面，只能有一个表达式，def则可以有多个。
    5）像if或for或print等语句不能用于lambda中，def可以。
    6）lambda一般用来定义简单的函数，而def可以定义复杂的函数。
    7）lambda函数不能共享给别的程序调用，def可以。
'''

'''
Lambda语法格式：
    lambda 变量1, 变量2, ..., 变量n : 表达式
'''

#----------------例----------------#

#单变量
add1 = lambda a : a + 1
print(add1(1), '\n')



#多变量
mul = lambda a, b : a * b
print(mul(2, 2), '\n')



#在lambda里使用if else
if_lambda = lambda x : x + 1 if x!=1 else 0
print(if_lambda(1))
print(if_lambda(2), '\n')



#在lambda中使用for
for_lambda = [lambda x : x * i for i in range(4)]
    #展开
def f():
    l = []
    for i in range(4):
        def _lambda(x):
            return x * i
        #注意这里添加到list里的是函数而不是返回的结果
        l.append(_lambda)
    return l

'''
原理：
   def f():
       这里新建list
    l = []
    
    这里循环range对象里的元素(0,1,2,3)
    for i in range(4):
        
        定义函数
        def _lambda(x):
            
            这里很重要！！
                因为程序的编译顺序根据late binding执行，所以函数_lambda中的 i 只会寻找最晚定义的 i
            return x * i

        这里把——lambda添加到list里
        l.append(_lambda)

        返回
    return l 
'''

f = f()
#因为最晚定义的 i 是 3，所以 print得到相同的结果
print (f[0](3)) # ====> 9
print (f[1](3)) # ====> 9
print (f[2](3)) # ====> 9
print (f[3](3)) # ====> 9


