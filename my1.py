def func1(a):
    for i in range(1, 7):
        print(i)
        a = a * i
        print(a)


def funcx():
    func1()


func1(6)
