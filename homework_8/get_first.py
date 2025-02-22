
from typing import List, TypeVar
def get_first(lst: List) -> object:
    return lst[0] if lst else None


print(get_first([1, 2, 3]))       # 1
print(get_first(["a", "b", "c"])) # "a"
print(get_first([]))              # None