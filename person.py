class Person:
    def get_age(self):
        return self._age
    def set_age(self,age):
        if 0<=age<=120:
            self._age = age
        else:
            print("Invalid age!")

p = Person()
p.set_age(25)
print(p.get_age())  # 期望输出：25

p.set_age(150)
# 期望输出：类似 "Invalid age!" 或抛出异常
