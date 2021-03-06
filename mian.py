# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool
# windows, actions, and settings.
# import abc
from module1 import *
from typing import Type



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
print(__name__)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# import module1
# module1.test11()
# module1.test2()


test11()
# test2()
if __name__ == '__main__':
    myname = ' geeo'
    seesky = '1'


class A():
    def display(self):
        print('hello world!')

    def AA(self):
        print()

    @abc.abstractmethod  # 定义抽象方法，无需实现功能
    def read(self):
        '子类必须定义读功能'
        pass


class B(A):
    '''
    这是一个类名字为B，继承A
    '''
    #TODO:需要修改1
    def display(self):
        super().display()
        pass




a = [dfkadlsfkasdfasdfasfa]


b = [dfkadlsfkasdfasdfasfa]
c = [dfkadlsfkasdfasdfasfa]

if a <= b:
    print('hello')
bb=B()
bb.display()

#TODO:需要修改2
print(bb)
#todo:kandaohuifu
#FIXME

#todo:已经修改提交
#todo:ok

