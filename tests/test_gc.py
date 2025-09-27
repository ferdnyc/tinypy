from tinypy.runtime.testing import UnitTest

class Create:
    def __init__(self, **args):
        self.__dict__.update(args)

    def _create_with_a(a):
        return Create(a=a)
    create_with_a = staticmethod(_create_with_a)

    def _create_with_b(b):
        return Create(b=b)
    create_with_b = staticmethod(_create_with_b)


class GcTest(UnitTest):
    objA = None
    objB = None
    scrap_objects = []

    def test_create(self):
        self.objA = Create.create_with_a(3)
        assert self.objA.a == 3
        self.objB = Create.create_with_b(3)
        assert self.objB.b == 3

    def test_delete(self):
        assert self.objA is not None
        assert self.objB is not None
        del self.objA
        for i in range(1000):
            self.scrap_objects.append(Create(a=i))
        del self.objB
        #assert not hasattr(self, "objA")
        #assert not hasattr(self, "objB")

t = GcTest()

t.run()
