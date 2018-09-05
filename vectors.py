from __future__ import annotations
import math


class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Vector({self.x}, {self.y})'

    def __abs__(self) -> float:
        '''
        >>> v = Vector(3, 4)
        >>> abs(v)
        5.0
        '''
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, other: Vector) -> Vector:
        '''
        >>> v1 = Vector(2, 4)
        >>> v2 = Vector(2, 1)
        >>> v1 + v2
        Vector(4, 5)
        '''
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar: float) -> Vector:
        '''
        Note : this only implements the multiplication operator in the
        specific order : self * scalar
        See __rmul__ for scalar * self

        >>> v = Vector(3, 4)
        >>> v * 3
        Vector(9, 12)
        >>> abs(v * 3)
        15.0
        '''
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)

    def __rmul__(self, scalar: float) -> Vector:
        '''
        Note : this only implements the multiplication operator in the
        specific order : scalar * self
        See __mul__ for self * scalar

        >>> v = Vector(3, 4)
        >>> 3 * v
        Vector(9, 12)
        '''
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)

    def __bool__(self) -> bool:
        '''
        >>> v = Vector(3, 4)
        >>> bool(v)
        True
        >>> v = Vector(0, 0)
        >>> bool(v)
        False
        '''
        return bool(abs(self))


if __name__ == '__main__':
    import doctest
    doctest.testmod()
