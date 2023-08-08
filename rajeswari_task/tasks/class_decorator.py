# creating class A

class A :
    def Decorators(func) :
        def inner(self) :
            print('Decoration started.')
            func(self)
            print('Decoration completed.\n')
        return inner

    @Decorators
    def fun1(self) :
        print('Class A methods.')

# creating class B
class B(A) :
    @A.Decorators
    def fun2(self) :
        print('Class B methods.')

obj = B()
obj.fun1()
obj.fun2()
