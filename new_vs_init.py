"""
__new__ is responsible for creating a new object.
__init__ is responsible for initializing a new object.
"""
from decimal import Decimal, ROUND_DOWN


class DecimalTwoPlaces(Decimal):
    """
    Always return a Decimal with two decimal places rounded down.
    """
    def __new__(cls, arg):
        obj = super(DecimalTwoPlaces, cls).__new__(cls)
        obj._from_base_class = type(obj) == DecimalTwoPlaces
        return Decimal.__new__(cls, arg).quantize(Decimal('.01'), rounding=ROUND_DOWN)


dtp = DecimalTwoPlaces(1.2368)
# >>> Decimal('1.23')


class ArgList:
    def __new__(cls, *args, **kwargs):
        """
        New has to return an object. But it can be any object.
        This is powerful but requires some attention.
        """
        print(cls, args, **kwargs)
        return list(args)

    def __init__(self, x, y):
        self.x = x
        self.y = y


ab = ArgList(1, 2)
# >>> ab
# >>> [1, 2]
