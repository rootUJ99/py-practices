class SomeClass:

    object_initiated_count = 0

    @classmethod
    def change_object_initiated_count(cls):
        cls.object_initiated_count += 1

    @staticmethod
    def change_static_count():
       return 10 + 15

    def compute_some_random_sum(self):
        return self.change_static_count()

if __name__ == "__main__":
    s1 = SomeClass()
    s1.change_object_initiated_count()
    s2 = SomeClass()
    s2.change_object_initiated_count()
    print(SomeClass.change_static_count())
    print(s2.compute_some_random_sum())
    print(s1.object_initiated_count, s2.object_initiated_count)
