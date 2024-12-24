# from functools import wraps


def wraps(src_func):  # Фабрика декораторов
    def inside_decorator(fn):  # Декоратор
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)

        wrapper.__name__ = src_func.__name__
        wrapper.__doc__ = src_func.__doc__

        # Тут буду перезаписывать name и doc
        return wrapper
    return inside_decorator

# inside_decorator = wraps("fn")
# fn = inside_decorator(fn)
# fn = wraps("fn")(fn)


def decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # До вызова функции
        return fn(*args, **kwargs)
        # После вызова функции
    return wrapper


@decorator
def some_func():
    """Docstring on `some_func`"""
    ...


if __name__ == "__main__":
    print(some_func.__name__)
    print(some_func.__doc__)
