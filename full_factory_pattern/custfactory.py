from inspect import getmembers,  isclass, isabstract
import cust_objects


class CustFactory(object):
    custs = {}

    def __init__(self):
        self.load_custs()

    def load_custs(self):
        classes = getmembers(cust_objects,
                             lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, cust_objects.AbsCust):
                self.custs.update([[name, _type]])

    def create_instance(self, cust_type):
        if cust_type in self.custs:
            return self.custs[cust_type]()
        else:
            return cust_objects.NullCust(cust_type)