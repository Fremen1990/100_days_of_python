from typing import Callable, Iterator
from itertools import starmap

def int_to_x(n:int) -> str:
    return n * 'X'

print(int_to_x(10))

# without type annotation
# int_to_x2 = lambda n: n*'X'
# with type annotation (type safety)
int_to_x2: Callable[[int], str] = lambda n:  n * 'X'
print(int_to_x2(40))

# without type annotation
# mapped: map(int_to_x, [1,2,3,4])
# with type annotation (type safety)
mapped: Iterator[str] = map(int_to_x, [1,2,3,4])
print(list(mapped))

mappedLambda: Iterator[str] = map(lambda n: n*'X', [1,2,3,4])
print(list(mappedLambda))

# ==============================

def multiply_str(text:str, n:int) -> str:
    return text * n

# alternative in lambda
multiply_str2: Callable[[str, int], str] = lambda text, n: text*n
print(multiply_str2("Tomek", 7))

# ==============================
data: list[tuple[str, int]]= [('Bob', 3), ('X', 5), ('Python', 2)]
star_map: Iterator[str] = starmap(multiply_str, data)

star_map_with_lambda: [Iterator[str]] = starmap(lambda s,n: s*n, data)
print(list(star_map_with_lambda))

# ===============================
# Self called lambda
(lambda s: print(f'{(s * 3).capitalize()}!!!'))("Yo")

display_list: Callable[[list], None] = lambda l: print(*l, sep=',', end='.\n')
print(display_list(["Tom", "Ann", "Mis"]))
print(display_list([1,2,3,4]))