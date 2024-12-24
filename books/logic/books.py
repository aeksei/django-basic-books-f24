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


def filter_books_by_published_year(
    books: list[dict[str, Any]],
    published_year: int,
) -> list[dict[str, Any]]:
    """

    :param books:
    :param published_year:
    :return:
    """
    return [book for book in books if book["published_year"] == published_year]
