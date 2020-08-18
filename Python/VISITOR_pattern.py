class LivingBeing:
    """
    This class is intended to be an interface.
    I know there is an ABC module that helps implementing abstrac clases and interfaces
    in Python, but I'm still not very much familiar with it.
    """
    def born(self):
        raise NotImplementedError('Not implemented')

    def accept(self, visitor):
        raise NotImplementedError('Not implemented')


class Person(LivingBeing):
    def __init__(self):
        self.number_of_legs = 2
        self.born()

    def born(self):
        print("I'm a new person!")

    def accept(self, visitor):
        visitor.visit_person(self)


class Dog(LivingBeing):
    def __init__(self):
        self.number_of_legs = 4
        self.born()

    def born(self):
        print("Whoof whoof I'm a new dog")

    def accept(self, visitor):
        visitor.visit_dog(self)


class Visitor:
    """
    Again, a class meant to be an interface.
    """
    def visit_person(self, person):
        raise NotImplementedError('Not implemented')

    def visit_dog(self, dog):
        raise NotImplementedError('Not implemented')


class LivingBeingWalkVisitor(Visitor):
    def visit_person(self, person):
        print(f"I'm walking on my {person.number_of_legs} legs")

    def visit_dog(self, dog):
        print(f"Whoof whoof moving my {dog.number_of_legs} legs whooof")


class God:
    def __init__(self):
        self.beings = [Dog(), Person()]

    def let_beings_walk(self, visitor):
        for being in self.beings:
            being.accept(visitor)


god = God()
god.let_beings_walk(LivingBeingWalkVisitor())
