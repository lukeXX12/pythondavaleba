class MyList:


        def __init__(self, data=[]):
            self.data = data

        def __str__(self):

            return str(self.data)

        def __add__(self, other):

            print(self.data + other.data)

        def __mul__(self, other):

            print(self.data * other)

l1=MyList([1,5,32,12])
l2=MyList([4,3,6,8])
l1 * 2
l1 + l2
print(str(11))