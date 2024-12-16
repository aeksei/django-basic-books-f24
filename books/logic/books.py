from typing import Any


def get_book_or_none(books: list[dict[str, Any]], book_id: int) -> dict[str, Any] | None:
    """

    :param book_id:
    :param books:
    :return:
    """
    for book in books:
        if book["id"] == book_id:
            return book

    return None
