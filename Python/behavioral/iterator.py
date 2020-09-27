from collections.abc import Iterator


class RepetitiveIterator(Iterator):
    """
    Iterator
    """
    def __init__(self, iterable, repetitions=float('inf')):
        self.iterable = iterable
        self.repetitions = repetitions
        self.position = 0
        self.loops = 0

    def __next__(self):
        try:
            return self._get_next()
        except IndexError:
            return self._repeat_or_finish()

    def _get_next(self):
        object_ = self.iterable[self.position]
        self.position += 1
        return object_

    def _repeat_or_finish(self):
        if self.loops < self.repetitions:
            return self._repeat()
        else:
            raise StopIteration()

    def _repeat(self):
        print('Starting over')
        self.loops += 1
        self.position = 0
        return next(self)


class RepetitiveList(list):
    """
    Iterable
    """
    def __init__(self, iterable, repetitions=float('inf')):
        super().__init__(iterable)
        self.repetitions = repetitions
        
    def __iter__(self):
        return RepetitiveIterator(self, self.repetitions)


# EXAMPLE USAGE: Python automatically calls the __iter__ method of the iterable
# object (RepetitiveList) whenever a for loop is used.
for x in RepetitiveList([1, 2, 3, 4], 5):
	print(x)
