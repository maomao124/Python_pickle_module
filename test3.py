"""
 * Project name(项目名称)：Python_pickle模块
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 19:38
 * Version(版本): 1.0
 * Description(描述)： pickle.dump()函数
此函数用于将 Python 对象转换成二进制文件，其基本语法格式为：
dump (obj, file,protocol=None, *, fix mports=True)
其中各个参数的具体含义如下：
obj：要转换的 Python 对象。
file：转换到指定的二进制文件中，要求该文件必须是以"wb"的打开方式进行操作。
protocol：和 dumps() 函数中 protocol 参数的含义完全相同
其他参数：为了兼容以前 Python 2.x版本而保留的参数，可以忽略。
 """
import pickle
import random


class C:
    def __init__(self, a, b, c, d):
        """
        初始化
        :param a:
        :param b:
        :param c:
        :param d:
        """
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def display(self):
        """
        显示
        :return:
        """
        print(self.a, self.b, self.c, self.d)


if __name__ == '__main__':
    with open("objects1.txt", "wb") as file1:
        list1 = []
        for i in range(0, 100):
            list1.append(random.randint(100, 900))
        print(list1)
        pickle.dump(list1, file1)

    with open("objects2.txt", "wb") as file2:
        c = C(3, 5, 1, 2)
        c.display()
        pickle.dump(c, file2)
