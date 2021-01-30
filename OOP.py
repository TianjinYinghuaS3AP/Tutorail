# -*- coding: UTF-8 -*-

import random

class BankAccount:
    '简单的银行账户类'


    '''
    包含：
        类变量 usrCount
        构造器 __init__
        类中的函数
        运算符重载
    '''
    usrCount = 0
    IDList = []

    def __init__(self, name = None, money = 0):
        self.name = name
        self.money = money


        #生成ID
        while True:

            ID = [str(inter) for inter in random.sample([0,1,2,3,4,5,6,7,8,9], 8)]
            ID = "".join(ID)

            if ID not in BankAccount.IDList:
                BankAccount.IDList.append(ID)
                break

        self.ID = ID

        #加一个User
        BankAccount.usrCount += 1

    def getName(self):
        return self.name

    def getMoney(self):
        return self.money

    def getID(self):
        return self.ID

    def setMoney(self, money):
        self.money = money

    def deposit(self, value):
        self.money += value

    def withdraw(self, value):
        self.money -= value

    #运算符重载
    def __lt__(self, other):
        if(self.money < other.money):
            return True
        else:
            return False

    def __gt__(self, other):
        if(self.money > other.money):
            return True
        else:
            return False


#--------------------分割线--------------------#

'''
应用例子:
    实例化BankAccount类:
        对象 MrA 和 MrB
    
    访问类变量 usrCount 与 类方法 getName() 和 getmoney()


    重点思考: 为什么访问 usrCount 要用 "BankAccount.usrCount" 而不是 "MrA.usrCount" 或 "Mr.B usrCount"
'''

MrA = BankAccount("Mr.A", 10)
MrB = BankAccount("Mr.B", 100)

print("Account Number: " + str(BankAccount.usrCount))

print("Name: " + MrA.getName())
print("Money: " + str(MrA.getMoney()))
print("ID: " + MrA.getID())

print("Name: " + MrB.getName())
print("Money: " + str(MrB.getMoney()))
print("ID: " + MrB.getID())

print(MrA > MrB)
print(MrA < MrB)

