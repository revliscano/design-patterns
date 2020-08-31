class Game:
    """
    Product
    """
    def __init__(self):
        self.number_of_enemies = None
        self.response_time = None
        self.lava = False

    def start(self):
        print(f'starting game with: {vars(self)}')


class GameBuilder:
    """
    Builder
    """
    def __init__(self):
        self.reset()

    def reset(self):
        self.game = Game()

    def set_enemies(self, number_of_enemies: int):
        print('setting num. of enemies')
        self.game.number_of_enemies = number_of_enemies
    
    def set_response_time(self, miliseconds: int):
        print('setting resp. time')
        self.game.response_time = miliseconds

    def enable_lava(self):
        print('enabling lava')
        self.game.lava = True

    def get_game(self) -> Game:
        game = self.game
        self.reset()
        return game


class Director:
    """
    Director
    """
    def __init__(self, builder: GameBuilder):
        self.builder = builder

    def make_easy_mode(self):
        self.builder.set_enemies(2)
        self.builder.set_response_time(1000)

    def make_hard_mode(self):
        self.builder.set_enemies(10)
        self.builder.set_response_time(250)
        self.builder.enable_lava()


class App:
    """
    Client
    """
    def __init__(self):
        self.game_builder = GameBuilder()
        self.director = Director(self.game_builder)

    def new_game(self, difficulty: str):
        if difficulty == 'easy':
            self.director.make_easy_mode()
        elif difficulty == 'hard':
            self.director.make_hard_mode()
        game = self.game_builder.get_game()
        game.start()


# USAGE
app = App()
app.new_game('easy')
app.new_game('hard')
