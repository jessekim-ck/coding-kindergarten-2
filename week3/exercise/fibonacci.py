class Fibonacci:
    def __init__(self):
        self._previous = 0
        self._current = 1

    def next(self):
        print(self._current)
        self._next = self._previous + self._current
        self._previous = self._current
        self._current = self._next


f = Fibonacci()
while True:
    f.next()
