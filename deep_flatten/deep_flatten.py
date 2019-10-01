from collections.abc import Iterable


def deep_flatten(deep_list):
    for e1 in deep_list:
        if isinstance(e1, Iterable) and type(e1) != str:
            yield from deep_flatten(e1)
        else:
            yield e1


if __name__ == "__main__":
    print(list(deep_flatten([[(1, 2), (3, 4)], [(5, 6), (7, 8)]])))
    print(list(deep_flatten(["hi", "there"])))