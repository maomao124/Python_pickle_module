"""
 * Project name(项目名称)：Python_pickle模块
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 19:28
 * Version(版本): 1.0
 * Description(描述)： pickle.dumps()函数
此函数用于将 Python 对象转为二进制对象
dumps(obj, protocol=None, *, fix_imports=True)
此格式中各个参数的含义为：
obj：要转换的 Python 对象；
protocol：pickle 的转码协议，取值为 0、1、2、3、4，其中 0、1、2 对应 Python 早期的版本，
3 和 4 则对应 Python 3.x 版本及之后的版本。未指定情况下，默认为 3。
其它参数：为了兼容 Python 2.x 版本而保留的参数，Python 3.x 中可以忽略。

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
    list1 = [1, 5, 6, 8, 9, 5]
    print(pickle.dumps(list1))
    c = C(4, 7, 8, 4)
    c.display()
    print(pickle.dumps(c))
