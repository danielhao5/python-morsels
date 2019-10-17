def format_ranges(list_of_numbers: list) -> str:
    """takes a list of numbers and returns a string that groups ranges of consecutive numbers together
        
    Arguments:
        list_of_numbers {list} -- [description]
    
    Returns:
        str -- [description]
    
    Example:
    >>> format_ranges([1, 2, 3, 4, 5, 6, 7, 8])
    '1-8'
    >>> format_ranges([1, 2, 3, 5, 6, 7, 8, 10, 11])
    '1-3,5-8,10-11'
    >>> format_ranges([4])
    '4'
    >>> format_ranges([1, 3, 5, 6, 8])
    '1,3,5-6,8'
    >>> format_ranges([9, 1, 7, 3, 2, 6, 8])
    '1-3,6-9'
    >>> format_ranges([1, 9, 1, 7, 3, 8, 2, 4, 2, 4, 7])
    '1-2,1-4,4,7,7-9'
    >>> format_ranges([1, 3, 5, 6, 8])
    '1,3,5-6,8'
    """
    list_of_numbers = sorted(list_of_numbers)
    pairs = make_ranges(list_of_numbers)

    return ",".join(f'{start}-{end}' if start != end else f'{start}' for start, end in pairs)


def make_ranges(numbers: list):
    pairs = []
    leftover = []

    start = end = None

    for n in numbers:
        if start is None:
            start = n
        elif n > end+1:
            pairs.append((start, end))
            start = n
        elif n == end:
            leftover.append(n)
        end = n

    pairs.append((start, end))  # last pair

    if leftover:
        pairs += make_ranges(leftover)  # recursive call for all leftovers

    return sorted(pairs)    


if __name__ == "__main__":
    import doctest

    doctest.testmod()