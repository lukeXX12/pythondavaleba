
#davaleba1

# class fruit:
#     def __init__(self, name, weight):
#         self.name=name
#         self.weight=weight
#     def __add__(self, other):
#         return self.weight+other.weight
#     def __eq__(self, other):
#         return self.name==other.name
# fruit1=fruit("peach",0.4)
# fruit2=fruit("peach",0.5)
# fruit3=fruit("apple",0.3)
# saertowona=fruit1+fruit3
# equality=fruit1==fruit2
# print(saertowona)
# print(equality)


# import sqlite3
# conn=sqlite3.connect('morty.db')
# c=conn.cursor()
# c.execute("""CREATE TABLE dogs(
#             name text,
#             age integer,
#             color text
#     )""")
# c.execute("INSERT INTO dogs VALUES ('ტობი', '4', 'ყავისფერი')")
# c.execute("INSERT INTO dogs VALUES('მიკი',9,'შავი')")
# conn.commit()
# conn.close()
