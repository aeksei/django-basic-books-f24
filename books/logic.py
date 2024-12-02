from typing import Any

from random import choice


def get_random_book(books: list[dict[str, Any]]) -> dict[str, Any]:
    """

    :param books:
    :return:
    """
    return choice(books)
