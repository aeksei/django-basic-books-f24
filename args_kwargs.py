def my_print(*args, sep=" "):
    # print(args)
    # first_item, *other_items = args  # *other_items, last_item = args
    # print(first_item, other_items)
    # print("-----")
    print(sep.join(args))


def common_func(*args, **kwargs):
    print(args, kwargs)


def person_print(first_name, second_name):
    print(f"Hello, {first_name} {second_name}")


if __name__ == '__main__':
    # my_print()
    my_print("1")
    my_print("1", "2")
    my_print("1", "2", "3")
    my_print("1", "2", "3", ",")
    my_print("1", "2", "3", sep=",")

    str_ = "abc"
    my_print(str_)
    my_print(*str_)

    # person_print(first_name="Вася", second_name="Пупкин")
    dict_args = {
        "first_name": "Вася",
        "second_name": "Пупкин",
    }
    person_print(**dict_args)

    common_func()
    common_func(a=1)
    common_func("test", "Happy", new="Year")