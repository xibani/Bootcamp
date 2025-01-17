def add(*args):
    print(args[-1])

    sum = 0
    for num in args:
        sum += num
    return sum

print(add(1,2,3,4,5,6,7,8,9,4,5,8,5,1,6,6,8,1))






def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)






class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(model="EL del plan")
print(my_car.make)



