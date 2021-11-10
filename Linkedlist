class LinkedNode:
    def __init__(self, data=None):
        self.__data = data      # 数据域
        self.__next = None      # 引用域1 后继
        self.__pre = None       # 引用域2 前驱

    # 为这两个字段写属性，写读写属性
    def __get_data(self):
        return self.__data

    def __set_data(self, data):
        self.__data = data

    Data = property(__get_data, __set_data)

    def __get_next(self):
        return self.__next

    def __set_next(self, next):
        self.__next = next

    Next = property(__get_next, __set_next)

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def __get_count(self):
        return self.__count
    Count = property(__get_count)       # 只读属性

    def count(self):
        c = 0
        p = self.__head
        while p:
            c += 1
            p = p.Next
        return c
    # 时间复杂度是多少 秦梓元 刘靳宇 O(n)

    def clear(self):
        while self.__head:
            p = self.__head
            self.__head = p.Next
            del p
        self.__count = 0

    def __del(self):
        self.clear()

    def insert_before(self, value, new_value):
        new_node = LinkedNode(new_value)
        if self.__head:
            if self.__head.Data == value:
                new_node.Next = self.__head
                self.__head = new_node
            else:
                p = self.__head
                while p.Next and p.Next.Data != value:
                    p = p.Next
                new_node.Next = p.Next
                p.Next = new_node
        else:
            self.__head = new_node
        self.__count += 1

    def remove_by_value(self, value):
        if self.__head:
            if self.__head.Data == value:
                p = self.__head
                self.__head = p.Next
                del p
                self.__count -= 1
                return True
            else:
                p = self.__head
                while p.Next and p.Next.Data != value:
                    p = p.Next
                if p.Next:
                    q = p.Next
                    p.Next = q.Next
                    del q
                    self.__count -= 1
                    return True
                else:
                    return False
        else:
            return False

    def find(self, value):
        p = self.__head
        while p and p.Data != value:
            p = p.Next
        return p        # p可能是空的，就说明没找到

    def get_max(self):
        if self.__head:
            max = self.__head.Data  # max等于第一个元素的值
            p = self.__head.Next    # p取下一个
            while p:     # p非空
                if p.Data > max:
                    max = p.Data
                p = p.Next
            return max
        else:
            return None

    def output(self):
        p = self.__head
        while p:
            print("id:{},Data_value:{},next:{}".format(id(p),p.Data,id(p.Next)))
            p = p.Next
        print('over')

if __name__ == '__main__':
    my_lst = LinkedList()
    my_lst.insert_before(0,1)
    my_lst.insert_before(0,2)
    my_lst.output()
    my_lst.remove_by_value(2)
    my_lst.output()
    my_lst.insert_before(1,3)
    my_lst.insert_before(1,2)
    my_lst.output()
    del my_lst








