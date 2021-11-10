class Student:

    def __init__(self,no=None,name='',En=None,math=None):
      self.no= no
      self.name= name
      self.En= En
      self.math= math    
      self.next = None      
#      self.pre = None  
    def __get_data(self):
        return self.no,self.name,self.En,self.math

    def __set_data(self, no,name,En,math):
        self.__data = data
        self.En= En
        self.math = math
        self.name= name
        self.no = no

    Data = property(__get_data, __set_data)

    def __get_next(self):
        return self.__next

    def __set_next(self, next):
        self.__next = next
class Studentlist:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count= 0 

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

    def insert_before(self, new_value):
        if not self.__head:
            self.__head =new_value
        else:
            new_value.next = self.__head
            self.__head =new_value
        self.__count += 1

    def remove_by_value(self, no):
        p = self.__head
        while p.next and p.next.no != no :
            p=p.next
        q= p.next
        p.next = q.next

    def find(self, no):
        p = self.__head
        while p and p.no != no:
            p = p.next
        return p 

    def output(self):
        p = self.__head
        while p:
            print("id:{},Data_value:{},next:{}".format(id(p),p.Data,id(p.next)))
            p = p.next
        print('over')

    def insert_find(self,no,datas):
        p = self.find(no)
        datas.next = p.next
        p.next = datas

    def update(self,no,datas):
        p = self.find(no)
        p.no = datas

if __name__ == '__main__':

    ListXS = Studentlist()
    with open('test.txt','r') as f:
      data = f.read()

    data=str(data)

    for i in range(9):

      datas = str(data.splitlines()[i])
      no = int(datas[0])
      name = str(datas[2:4])
      En = int(datas[5:7])
      math= int(datas[8:])
      new_code=Student(no,name,En,math)
      ListXS.insert_before(new_code)

    ListXS.output()

    
    #new_code = Student(1,'张三',100,100)
    #ListXS.insert_before(new_code)
    #new_code_1 = Student(2,'李四',20,20)
    #ListXS.insert_before(new_code_1)
    #new_code_1 = Student(3,'钱五',40,73)
    #ListXS.insert_before(new_code_1)
    #ListXS.output()
    i =int(input())
    ListXS.insert_find(i,Student(4,'王六',77,88))
    ListXS.output()
    ListXS.update(4,0)
    ListXS.output()
    ListXS.remove_by_value(0)
    ListXS.output()
