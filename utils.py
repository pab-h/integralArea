from typing import Callable

functionType = Callable[[float], float]

class Interval:
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b
        self.size = self.b - self.a

        if not self.size > 0:
            raise Exception("b - a > 0")