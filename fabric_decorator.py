import time


def fabric_timeit(count: int = 3):
    def timeit(fn):  # Декоратор
        func_name = fn.__name__
        print(f"Вызов один раз на момент декорирования функции {func_name}")

        def wrapper(*args, **kwargs):  # Обёртка или задекорированная функция
            print("Вызываюсь каждый раз, когда вызывается основная функция")
            # До вызова основной функции
            times = []
            for _ in range(count):
                t0 = time.time()

                result = fn(*args, **kwargs)  # Вызов основной функции

                # После вызова основной функции
                dt = time.time() - t0

                times.append(dt)

            mean_dt = sum(times) / len(times)
            print(f"Время выполнения функции {func_name} {mean_dt} в результате {count} запусков")

            return result

        return wrapper
    return timeit


@fabric_timeit(100)  # first_sort = timeit(first_sort) Декорирование функций
def first_sort(seq):
    return sorted(seq)  # Вызов основной функции


@fabric_timeit(100)  # second_sort = timeit(second_sort) Декорирование функций
def second_sort(seq):
    seq.sort()  # Вызов основной функции
    return seq


if __name__ == '__main__':
    first_sort(list(range(10 ** 6, 1, -1)))
    second_sort(list(range(10 ** 6, 1, -1)))
