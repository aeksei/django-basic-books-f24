import time


list_ = [1, 2, 3]


def timeit(fn):  # Декоратор
    func_name = fn.__name__
    print(f"Вызов один раз на момент декорирования функции {func_name}")

    def wrapper(*args, **kwargs):  # Обёртка или задекорированная функция
        print("Вызываюсь каждый раз, когда вызывается основная функция")
        # До вызова основной функции
        t0 = time.time()

        result = fn(*args, **kwargs)  # Вызов основной функции

        # После вызова основной функции
        dt = time.time() - t0
        print(f"Время выполнения функции {func_name} {dt}")

        return result

    return wrapper


@timeit  # first_sort = timeit(first_sort) Декорирование функций
def first_sort(seq):
    return sorted(seq)  # Вызов основной функции


@timeit  # second_sort = timeit(second_sort) Декорирование функций
def second_sort(seq):
    seq.sort()  # Вызов основной функции
    return seq





for _ in range(3):
    print(first_sort([3, 2, 1]))
    print(second_sort([3, 2, 1]))

    print("------")
