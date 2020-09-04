import random
from abc import ABC, abstractmethod


FIRST_PLATFORM = 0


class PlatformSeeker(ABC):
    """
    Abstract handler
    """
    next_platform = None

    def set_next_platform(self, platform):
        self.next_platform = platform
        return platform

    def search_movie(self, movie):
        if self.next_platform:
            return self.next_platform.search_movie(movie)
        return f"{movie} hasn't been found anywhere"

    @abstractmethod
    def is_movie_in_db(self):
        pass


class NetflixSeeker(PlatformSeeker):
    """
    Concrete handler
    """
    def search_movie(self, movie):
        if self.is_movie_in_db():
            return f'{movie} is on Netflix'
        return super().search_movie(movie)

    def is_movie_in_db(self):
        print('Looking into Netflix catalog...')
        return random.choice((True, False))


class DisneyPlusSeeker(PlatformSeeker):
    """
    Concrete handler
    """
    def search_movie(self, movie):
        if self.is_movie_in_db():
            return f'{movie} is on Disney'
        return super().search_movie(movie)

    def is_movie_in_db(self):
        print('Looking into Disney catalog...')
        return random.choice((True, False))


class App:
    """
    Client
    """
    def __init__(self):
        self.platforms = [NetflixSeeker(), DisneyPlusSeeker()]
        self._link_platforms()

    def _link_platforms(self):
        for platform, next_platform in zip(self.platforms, self.platforms[1:]):
            platform.set_next_platform(next_platform)

    def search(self, movie):
        result = self.platforms[FIRST_PLATFORM].search_movie(movie)
        print(f'Result: {result}')


# EXAMPLE USAGE
app = App()
app.search('Titanic')
