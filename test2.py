"""
 * Project name(项目名称)：Python_pickle模块
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/30 
 * Time(创建时间)： 19:34
 * Version(版本): 1.0
 * Description(描述)： pickle.loads()函数
此函数用于将二进制对象转换成 Python 对象
loads(data, *, fix_imports=True, encoding='ASCII', errors='strict')
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
    b1 = b'\x80\x04\x95\x11\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x05K\x06K\x08K\tK\x05e.'
    b2 = b'\x80\x04\x952\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x01C\x94\x93\x94)' \
         b'\x81\x94}\x94(\x8c\x01a\x94K\x04\x8c\x01b\x94K\x07\x8c\x01c\x94K\x08\x8c\x01d\x94K\x04ub.'
    list1 = pickle.loads(b1)
    print(list1)
    print(type(list1))
    c = pickle.loads(b2)
    c.display()
    print(type(c))
