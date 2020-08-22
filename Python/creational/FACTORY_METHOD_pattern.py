from abc import ABC, abstractmethod


class Warrior():
    """
    Product base class
    """
    def fight(self):
        print(f'Attacking with my {self.weapon}')


class Knight(Warrior):
    """
    Concrete product
    """
    def __init__(self):
        self.weapon = 'sword'


class Archer(Warrior):
    """
    Another concrete product
    """
    def __init__(self):
        self.weapon = 'bow'


class WarriorFactory(ABC):
    """
    Factory abstract class
    """
    def send_warrior_to_war(self):
        warrior = self._create_warrior()
        warrior.fight()

    @abstractmethod
    def _create_warrior():
        pass


class KnightFactory(WarriorFactory):
    """
    Concrete factory class
    """
    def _create_warrior(self):
        """
        concrete factory method
        """
        print("Creating new knight.")
        return Knight()


class ArcherFactory(WarriorFactory):
    """
    Concrete factory class
    """
    def _create_warrior(self):
        """
        concrete factory method
        """
        print('Creating new archer.')
        return Archer()


# EXAMPLE USAGE
barracks = KnightFactory()
archery_range = ArcherFactory()
for facility in barracks, archery_range:
    facility.send_warrior_to_war()
