from abc import ABC, abstractmethod


# TARGET INTERFACE
class AndroidGame(ABC):
    @abstractmethod
    def get_slide(self, slide_direction):
        pass

# ADAPTEE
class PCGame:
    def __init__(self, name):
        self.name = name

    def get_key(self, key_name):
        if key_name == 'SPACE':
            print('Jumping!')

# ADAPTER
class PCtoAndroidGameAdapter(PCGame, AndroidGame):
    def get_slide(self, slide_direction):
        if slide_direction == 'up':
            return self.get_key('SPACE')

# CLIENT
class AndroidGamer:
    def __init__(self, current_game):
        self.current_game = current_game

    def perform_slide(self, slide_direction):
        print(f"I moved my finger {slide_direction}")
        self.current_game.get_slide(slide_direction)

# USAGE
old_pc_game = PCtoAndroidGameAdapter('Quake')
gamer = AndroidGamer(old_pc_game)
gamer.perform_slide('up')
