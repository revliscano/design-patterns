import copy


class Product:
    """
    Prototype, implementing clone() method
    """
    def __init__(self, parts):
        self.parts = parts
    
    def clone(self):
        return self.__class__(copy.deepcopy(self.parts))


class ProductionDepartment:
    """
    client, using prototype
    """
    def __init__(self):
        self.product = None

    def manufacture(self):
        print("creating a brand new product")
        parts = ['part a', 'part b', 'part c']
        self.product = Product(parts)

    def mass_production(self, n):
        print('Copying the prototype')
        return [self.product.clone() for _ in range(n)]


dept = ProductionDepartment()
dept.manufacture()
products = dept.mass_production(10)
