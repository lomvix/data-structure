class List:
    def __init__(self):
        self.__lst = []

    def clear(self):
        # 遍历lst，挨个删除
        # for 循环不允许对序列进行修改
        while self.__lst:  # 还有元素可以删除，当lst中还有元素时，条件为真
            del self.__lst[0]

    def __del__(self):
        self.clear()
        del self.__lst

    def empty(self):
        return not self.__lst

    def length(self):
        return len(self.__lst)

    def insert(self, i, value):
        if self.length() < i:
            print('i范围越界')
        elif self.length() == i:
            self.__lst.append(value)
        else:
            # self.__lst.insert(i, value)
            self.__lst.append(self.__lst[-1])    # 1.增加一个元素的位置保存原来列表中的最后一个元素
            for j in range(len(self.__lst) - 3, i-1, -1):     # 2.下标是i的元素及后续元素的向后移动
                self.__lst[j + 1] = self.__lst[j]
            self.__lst[i] = value     # 3.新元素加进来

    def erase(self, i):
        if self.length() <= i:
            print('i范围越界')
        else:
            # self.__lst.pop(i)
            for j in range(i, self.length()-1):
                self.__lst[j] = self.__lst[j + 1]
            self.__lst.pop(-1)

    def push_back(self, value):
        self.__lst.append(value)

    def pop_back(self):
        if self.length():
            self.__lst.pop(-1)
        else:
            print('列表中没有可以删除的元素')

    def remove(self, value):
        i, j = 0, 0
        while j < self.length():
            if self.__lst[j] == value:
                j += 1
            else:
                self.__lst[i] = self.__lst[j]
                i += 1
                j += 1
        while self.length() > i:
            self.__lst.pop(-1)

    def output(self):
        print("size:{}".format(len(self.__lst)), "elements:", end=' ')
        for i in self.__lst:
            print(i, end=' ')
        print()

    def __getitem__(self, index):
        if index >= self.length() or index < -self.length():
            print('要求索引越界')
        else:
            return self.__lst[index]

    def __setitem__(self, index, value):
        if index >= self.length() or index < -self.length():
            print('要求索引越界')
        else:
            self.__lst[index] = value


if __name__ == '__main__':
    '''
    # 导入 random(随机数) 模块
    import random
    print(random.randint(0,9))
    '''
    my_lst = List()
    for i in range(10):
        my_lst.push_back(i+1)
        my_lst.output()
    my_lst[1] = 100
    my_lst.output()
    my_lst.insert(1, 200)
    my_lst.output()
    my_lst.erase(1)
    my_lst.output()
    my_lst.insert(1,20)
    my_lst.insert(3, 20)
    my_lst.output()
    my_lst.remove(20)
    my_lst.output()
    my_lst.clear()
    my_lst.output()
    del my_lst
#
#     print('啊'>'唉')

# list只可能是索引结构或者顺序结构
lst = list()
lst.append(1)
lst.append(2)
lst.append(3)
lst.append(4)
for i in range(len(lst)):
    print(id(lst[i]))
lst.pop(1)
print()
for i in range(len(lst)):
    print(id(lst[i]))
