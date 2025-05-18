class ProductMixin:


    def __init__(self):
        print(repr(self))


    def __repr__(self):
        attrs = ', '.join(f"{v}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"