"""
 * Project name(项目名称)：Python_pickle模块
 * Package(包名): 
 * File(文件名): test4
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 19:44
 * Version(版本): 1.0
 * Description(描述)： pickle.load()函数
此函数和 dump() 函数相对应，用于将二进制对象文件转换成 Python 对象。
load(file, *, fix_imports=True, encoding='ASCII', errors='strict')
其中，file 参数表示要转换的二进制对象文件（必须以 "rb" 的打开方式操作文件）
 """
import pickle


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
    with open("objects1.txt", "rb") as file1:
        list1 = pickle.load(file1)
        print(list1)
        print(type(list1))
    with open("objects2.txt", "rb") as file2:
        c = pickle.load(file2)
        c.display()
        print(type(c))
