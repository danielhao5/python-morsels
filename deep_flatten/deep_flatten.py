

def deep_flatten(deep_list):
    try:
        it = iter(deep_list)
    except TypeError as err:
        return deep_list

    yield next()



if __name__ == "__main__":
    print(deep_flatten([[1,2], [3]]))