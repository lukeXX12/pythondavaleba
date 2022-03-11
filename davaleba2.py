# class Book:
#     def __init__(self,name, author, year,pages):
#         self.__name = name
#         self.__author = author
#         self.__year = year
#         self.__pages = pages
#     def info(self):
#         print(f"წიგნის სახელია{self.__name}, იგი დაიბეჭდა{self.__year} ,"
#               f"წიგნის ავტორია {self.__author} და იგი შედგება {self.__pages} gverdisgan ")
#
#
#     def set_name(self,name):
#         self.__name = name
# book1= Book("80000 კილომეტრი წყალქვეშ", "ჟიულ ვერნი", 1869,458)
# book2= Book("80000 კილომეტრიშ", "ჟიულ რნი", 1829,438)
#
# print(book1.info())
# print(book2.info())







# class Minormax:
#     def __init__(self,listi):
#         self.__listi = listi
#
#     def min(self):
#
#         print(min(self.__listi))
#
#
#     def max(self):
#         print(max(self.__listi))
#
# listi1=Minormax(list[5,11,2,33])
# print(listi1.max)
#
# class Animal:
#     def __init__(self, name="", age="", **kwargs):
#         self._name=name
#         self._age=age
#     def info(self):
#         print(self._name,"-",self._age,)
#
# class Dog(Animal):
#     def __init__(self, variety="", color="", **kwargs):
#         super().__init__(**kwargs)
#         self._variety=variety
#         self._color=color
#     def info(self):
#         print(self._variety,"-",self._color,)
#
#
#
#
# firstAnimal= Dog(variety="cuga", color="brown",name="doggo", age="12")
# Animal.info(firstAnimal)



class Person:
    def __init__(self,fname="",lname="",phone=""):
        self.fname= fname
        self.lname= lname
        self.phone= phone


class CallMixin(Person):
    def call(self):
        print(f"დაირეკოს",{self.fname},{self.lname},"-სთან, ნომერზე:",{self.phone})


person1=CallMixin(fname="luka",lname="nebieridze",phone="558462211")
person1.call()