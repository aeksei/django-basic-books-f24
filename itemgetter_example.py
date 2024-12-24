# from operator import itemgetter
from typing import Any, Callable


def itemgetter(i: int) -> Callable[[list], Any]:
    def itemgetter_(seq: list):
        """
        От любой последовательности должна нам возвращать
        элемент по одному и тому же  указанному индексу.
        """
        return seq[i]
    return itemgetter_


if __name__ == "__main__":
    itemgetter_0 = itemgetter(0)
    itemgetter_1 = itemgetter(1)
    list_ = [0, 1, 2]
    print(itemgetter_0(list_))
    print(itemgetter_1([4, 5, 6]))

    list_tuples = [(3, "b"), (2, "a"), (1, "c")]
    by_char = itemgetter(1)
    print(sorted(list_tuples, key=by_char))
