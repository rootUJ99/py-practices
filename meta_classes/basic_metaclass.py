class MetaClass(type):
    def __new__(cls, name, bases, body):
        print(cls, "\n", name, "\n", bases, "\n", body)
        if "foo" in body:
            print("foo exists")
        else:
            raise TypeError(f"implement foo in {name}")
        return super().__new__(cls, name, bases, body)

class NormalClass(metaclass = MetaClass):
    def __init__(self):
        print("from init")

    def foo(self):
        print("this is foo")

class AnotherNormalClass(metaclass = MetaClass):
    def __init__(self):
        print("from init")

if __name__ == "__main__":
    n = NormalClass()
    # a = AnotherNormalClass() # will throw error because foo does not exists
