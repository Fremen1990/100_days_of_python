from datetime import datetime
from typing import Final

# 10 Important Python Concepts In 20 Minutes
# https://www.youtube.com/watch?v=Gx5qb1uHss4&ab_channel=Indently

# Basic data types with type annotations
number: int = 10
decimal: float = 2.5
text: str = " ersfs"
active: bool = True

names: list = ['ann', 'tom']
coordinates: tuple = (1.5,2.2)
unique: set = {1 ,4, 6}
data:dict = {'name': 'Bob', 'age': 44}

# Constants - with types not able to be override
VERSION: Final[str] = '1.0.4'
PI: Final[float] = 3.1415

# Functions
def show_date() -> None:
    print(f"This is current date and time: {datetime.now()}")
show_date()
show_date()

def greet(name:str) -> None:
    print(f"Hello {name}!")
greet("Luigi")

def add(a:float, b: float) -> float:
    return a + b
print(add(1,3))

# Classes
class Car:
    def __init__(self, brand: str, series: int, model: str, colour: str, horsepower:int) -> None:
        self.brand = brand
        self.series = series
        self.model = model
        self.colour = colour
        self.horsepower = horsepower

    def drive(self) -> None:
        print(f"{self.brand} series{self.series} {self.model} is driving")

    def get_info(self, top_separator:str, bottom_separator: str) -> None:
        print(f"{top_separator}\nBrand: {self.brand}\nSeries: {self.series}\nColour: {self.colour}\nHorsepower: {self.horsepower}\n{bottom_separator}")

    def __str__(self) -> str:
        return f'{self.brand}, {self.horsepower}'

    def __add__(self, other) -> str:
        return f'{self.brand} & {other.brand}'


myCar: Car = Car('BMW',3,'e91','black', 168)
myOldCar: Car = Car('Open', 1, 'Astra', 'purple', 75)
print(myCar.drive())
print(myCar.get_info('------------------', '-----------------'))
print(myOldCar.get_info('==================', '=================='))

print(myCar)
print(myCar + myOldCar)
