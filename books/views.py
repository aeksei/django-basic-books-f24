from datetime import datetime

from django.http import HttpRequest, HttpResponse, JsonResponse

from books.models import BOOKS
from books import logic


def get_current_datetime(request: HttpRequest) -> HttpResponse:
    now = datetime.now()
    return HttpResponse(now)


def index(request: HttpRequest) -> HttpResponse:
    boby = """<h1>Hello, world!!!</h1>"""
    return HttpResponse(boby)


def get_books(request: HttpRequest) -> HttpResponse:
    return JsonResponse(
        BOOKS,
        safe=False,
        json_dumps_params={
            "ensure_ascii": False,
            "indent": 4,
        }
    )


def get_random_book(request: HttpRequest) -> HttpResponse:
    random_book = logic.get_random_book(BOOKS)
    return JsonResponse(
        random_book,
        json_dumps_params={
            "ensure_ascii": False,
            "indent": 4,
        }
    )
