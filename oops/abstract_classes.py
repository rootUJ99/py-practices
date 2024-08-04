from abc import ABC, abstractmethod

class MethodsToImplement(ABC):

    @abstractmethod
    def foo(self):
        print("this is foo")

    @abstractmethod
    def bar(self):
        print("this is foo")

    def baz(self):
        print("this is baz")

class NormalClass(MethodsToImplement):

    def foo(self):
        print("this is foo from normal class")

    def bar(self):
        print("this is bar from normal class")

if __name__ == "__main__":

    a = NormalClass()
    a.foo()
    a.bar()
    a.baz()

