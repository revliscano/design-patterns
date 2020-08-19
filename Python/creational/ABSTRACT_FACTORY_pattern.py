from abc import ABC, abstractmethod


# FACTORIES
class PlayerFactory(ABC):
    """
    This class is meant to be an interface
    """
    @abstractmethod
    def create_goalkeeper(self):
        pass

    @abstractmethod
    def create_defender(self):
        pass


class FootballPlayerFactory(PlayerFactory):
    """
    Football here refers to International Football (Soccer)
    """
    def create_goalkeeper(self):
        return FootballGoalkeeper()

    def create_defender(self):
        return FootballDefender()


class HockeyPlayerFactory(PlayerFactory):
    """
    Hockey here refers to Field Hockey, the 11-vs-11 game.
    """
    def create_goalkeeper(self):
        return HockeyGoalkeeper()

    def create_defender(self):
        return HockeyDefender()

# FOOTBALL PLAYERS
class FootballPlayer:
    def __init__(self, uses_hands):
        self.uses_hands = uses_hands

    def play(self):
        print("I'm playing football!")


class FootballGoalkeeper(FootballPlayer):
    def __init__(self):
        super(FootballGoalkeeper, self).__init__(uses_hands=True)


class FootballDefender(FootballPlayer):
    def __init__(self):
        super(FootballDefender, self).__init__(uses_hands=False)

#HOCKEY PLAYERS
class HockeyPlayer:
    def play(self):
        print("I'm playing hockey!")


class HockeyGoalkeeper(HockeyPlayer):
    pass


class HockeyDefender(HockeyPlayer):
    pass

# CLIENT
class Team:
    def __init__(self, factory):
        self.factory = factory()

    def buy_new_goalkeeper(self):
            return self.factory.create_goalkeeper()

    def buy_new_defender(self):
            return self.factory.create_defender()

# USAGE
real_madrid = Team(FootballPlayerFactory)
courtois = real_madrid.buy_new_goalkeeper()
courtois.play()
