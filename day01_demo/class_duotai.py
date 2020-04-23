class Dog():
    def work(self):
        return "狗狗"


class FangBoDog(Dog):
    def work(self):
        return "防爆狗"


class JDDog(Dog):
    def work(self):
        return "缉毒狗"


fn1 = lambda dog: dog.work()

fbd = FangBoDog()
jdd = JDDog()

print(fn1(fbd))
print(fn1(jdd))
