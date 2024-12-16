from datetime import datetime

from django.http import HttpRequest, HttpResponse, JsonResponse, Http404
from django.shortcuts import render

from books.models import BOOKS
from books import logic


def get_book_or_404(books, book_id):
    book = logic.books.get_book_or_none(books, book_id)
    if not book:
        raise Http404

    return book


def get_current_datetime(request: HttpRequest) -> HttpResponse:
    now = datetime.now()
    return HttpResponse(now)


def index(request: HttpRequest) -> HttpResponse:
    template_name = "index.html"
    context = {
        "book_list": BOOKS,
    }
    return render(request, template_name, context=context)


def about(request: HttpRequest) -> HttpResponse:
    template_name = "about.html"
    return render(request, template_name)

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


def get_book(request: HttpRequest, book_id: int) -> HttpResponse:
    template_name = "books/book_detail.html"
    book = get_book_or_404(BOOKS, book_id=book_id)
    context = {
        "book": book,
    }
    return render(request, template_name, context=context)
