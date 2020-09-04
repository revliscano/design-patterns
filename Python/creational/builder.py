import random
from abc import ABC, abstractmethod


class Game:
    """
    Product
    """
    def start(self):
        print(f'starting game with: {vars(self)}')


class GameModeBuilder(ABC):
    """
    Builder abstract class
    """
    def __init__(self):
        self.reset()

    def reset(self):
        self.game = Game()

    def set_enemies(self, enemy_type):
        self.game.enemies = [enemy_type for _ in range(random.randint(5, 10))]

    @abstractmethod
    def set_floor_texture(self):
        pass

    @abstractmethod
    def set_trap(self):
        pass

    def get_game(self):
        game = self.game
        self.reset()
        return game


class SeaBattleBuilder(GameModeBuilder):
    """
    Concrete Builder
    """
    def set_enemies(self):
        print('creating ships')
        super().set_enemies('ship')
    
    def set_floor_texture(self):
        print('setting water')
        self.game.floor_texture = 'water'

    def set_trap(self):
        print('setting environment traps')
        self.game.trap = random.choice(['waterspout', 'tsunami'])


class GroundBattleBuilder(GameModeBuilder):
    """
    Concrete Builder
    """
    def set_enemies(self):
        print('creating tanks')
        super().set_enemies('tank')
    
    def set_floor_texture(self):
        print('setting grass')
        self.game.floor_texture = random.choice(['grass', 'sand'])

    def set_trap(self):
        print('setting environment traps')
        self.game.trap = 'lava'


class Director:
    """
    Director
    """
    @property
    def builder(self):
        return self.__builder

    @builder.setter
    def builder(self, builder_):
        self.__builder = builder_

    def construct(self):
        self.builder.set_enemies()
        self.builder.set_floor_texture()
        self.builder.set_trap()


class App:
    """
    Client
    """
    def __init__(self):
        self.director = Director()
        self.builders = {
            'sea': SeaBattleBuilder(),
            'ground': GroundBattleBuilder()}

    def sea_battle_game(self):
        print('creating a new sea battle game')
        self.director.builder = self.builders['sea']
        self.__start_game()

    def ground_battle_game(self):
        print('creating a new ground battle game')
        self.director.builder = self.builders['ground']
        self.__start_game()

    def __start_game(self):
        self.director.construct()
        game = self.director.builder.get_game()
        game.start()


# USAGE
app = App()
app.sea_battle_game()
app.ground_battle_game()
