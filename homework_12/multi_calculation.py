import math
import threading
from typing import List


def split_list(l_data: list, num: int) -> list[int]:
    """
    split list into few lists
    :param l_data:
    :param num:
    :return:
    """
    length = len(l_data)
    s = math.ceil(length / num)
    new_list = []
    for i in range(s):
        to_el = i + 1
        new_list.append(l_data[num * i:num * to_el])
    return new_list


list_info = [2, 4, 7, 8, 9, 1, 12, 78, 44, 22]

new_list = split_list(list_info, 3)

results = [0] * len(new_list)


def sum_(list_data, index):
    results[index] = sum(list_data)


threads: List[threading.Thread] = []

for i, l_ in enumerate(new_list):
    t = threading.Thread(target=sum_, args=(l_, i))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Суммы по частям:", results)
print("Общая сумма:", sum(results))
