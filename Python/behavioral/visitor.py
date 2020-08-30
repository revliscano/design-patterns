from abc import ABC, abstractmethod


class LivingBeing(ABC):
    """
    Living being Base class
    """
    def __init__(self, number_of_legs):
        self.number_of_legs = number_of_legs
        self.born()

    @abstractmethod
    def born(self):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass


class Person(LivingBeing):
    """
    Concrete living being
    """
    def __init__(self):
        super().__init__(number_of_legs=2)    

    def born(self):
        print("I'm a new person!")

    def accept(self, visitor):
        visitor.visit_person(self)


class Dog(LivingBeing):
    """
    Concrete living being
    """
    def __init__(self):
        super().__init__(number_of_legs=4)

    def born(self):
        print("Whoof whoof I'm a new dog")

    def accept(self, visitor):
        visitor.visit_dog(self)


class Visitor:
    """
    Visitor Interface
    """
    @abstractmethod
    def visit_person(self, person):
        pass

    @abstractmethod
    def visit_dog(self, dog):
        pass


class LivingBeingWalkVisitor(Visitor):
    """
    Concrete visitor
    """
    def visit_person(self, person):
        print(f"I'm walking on my {person.number_of_legs} legs")

    def visit_dog(self, dog):
        print(f"Whoof whoof moving my {dog.number_of_legs} legs whooof")


class God:
    """
    Client
    """
    def __init__(self):
        self.beings = [Dog(), Person()]

    def let_beings_walk(self, visitor):
        for being in self.beings:
            being.accept(visitor)


god = God()
god.let_beings_walk(LivingBeingWalkVisitor())
