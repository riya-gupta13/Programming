# import cx_Oracle
#
# connection = cx_Oracle.makedsn(host="", port="", service_name="")
# conn = cx_Oracle.connect(username="", password="", dsn=connection)
# cursor = conn.cursor()
# cursor.execute("select col1 || col2 || col3 from table1")
# concatenatedValue = cursor.fetchall([0])
# cursor.execute("insert into table2 (col1) values (:1), (conca")

# n = int(input("enter a number"))


# if n % 2 != 0:
#     print("Odd")
# else:
#     print("even")


class OddEven:
    def __init__(self, n):
        try:
            self.n = n
        except ValueError:
            raise ValueError("input invalid")

    def find(self):
        if self.n == 0:
            raise ValueError
        try:
            if self.n % 2 != 0:
                return "ODD"
            else:
                return "Even"
        except Exception as e:
            print(e)


o = OddEven(0)
o.find()
