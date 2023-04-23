# open close prenciple
# example one

# wrong way


class Person:
    """
    wrong way
    """

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person(name={self.name})"


class PersonStorage:
    """
    wrong way
    """

    def save_to_database(self, person):
        print(f"Save the {person} to database")

    def save_to_json(self, person):
        print(f"Save the {person} to a JSON file")


# correct way

from abc import ABC, abstractmethod


class PersonStorageCurrect(ABC):
    """
    correct way
    """

    @abstractmethod
    def save(self, person):
        pass


class PersonDB(PersonStorageCurrect):
    """
    correct way
    """

    def save(self, person):
        print(f"Save the {person} to database")


class PersonJSON(PersonStorageCurrect):
    """
    correct way
    """

    def save(self, person):
        print(f"Save the {person} to a JSON file")


# *************************************
# example two
class Rectangle:
    """
    wrong way
    """

    def __init__(self):
        pass

    def width(self):
        pass

    def height(self):
        pass


class Circle:
    """
    wrong way
    """

    def __init__(self):
        pass

    def radius(self):
        pass


import math


class AreaCalculator:
    """
    wrong way
    """

    def area(self, shapes):
        area = 0
        for item in shapes:
            if item is Rectangle:
                rectangle = item()
                area += rectangle.width() * rectangle.height()
            else:
                circle = item
                area += circle.radius() * circle.radius * math.pi

        return area


# correct way
class Shape(ABC):
    @abstractmethod
    def area(self, shapes):
        pass


class RectangleCorrect(Shape):
    """
    correct way
    """

    def __init__(self, width: int = 1, height: int = 1):
        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    @width.setter
    def width(self, a):
        self._width = a

    @height.setter
    def height(self, a):
        self._height = a

    def area(self, shapes):
        return self.width * self.height


class CircleCorrect(Shape):
    """
    correct way
    """

    def __init__(self, radius: int = 1) -> None:
        self._radius = radius

    @property
    def radius(self) -> int:
        return self._radius

    @radius.setter
    def radius(self, a):
        self._radius = a

    def area(self, shapes):
        return self.radius * self.radius * math.pi


def area(shapes):
    area = 0
    for item in shapes:
        area += item.area()
    return area
