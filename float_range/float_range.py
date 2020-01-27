import doctest
from typing import Iterator
from math import ceil


class float_range:
    """[summary]
    
    Arguments:
        start {float} -- [description]
        end {float} -- [description]
        step {float} -- [description]
    
    Returns:
        list -- [description]
    
    Yields:
        list -- [description]

    Examples:
    >>> for n in float_range(0.5, 2.5, 0.5):
    ...     print(n)
    0.5
    1.0
    1.5
    2.0
    >>> list(float_range(3.5, 0, -1))
    [3.5, 2.5, 1.5, 0.5]
    >>> for n in float_range(0.0, 3.0):
    ...     print(n)
    0.0
    1.0
    2.0
    >>> for n in float_range(3.0):
    ...     print(n)
    0.0
    1.0
    2.0
    >>> float_range(1,1,1,1) #doctest: +ELLIPSIS
    Traceback (most recent call last):
    ...
    TypeError: __init__() takes from 2 to 4 positional arguments but 5 were given
    """
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            start, stop = 0., start

        (self.start, self.stop, self.step) = (start, stop, step)

        self.item_count = ceil((stop-start) / step)

    def __len__(self):
        return max(self.item_count, 0) # ReLu...

    def __iter__(self):
        for i in range(
            len(self)):
            yield self.start + i * self.step

    def __reversed__(self):
        last = self.start + (len(self) - 1) * self.step
        for _ in range(len(self)):
            yield last
            last -= self.step

    def __eq__(self, other):
        if isinstance(other, (float_range, range)):
            return float_range._attrs(self) == float_range._attrs(other)
        else:
            return NotImplemented    

    @staticmethod
    def _attrs(iterable):
        if len(iterable) == 0:
            return ()
        return (next(iter(iterable)), next(reversed(iterable)), len(iterable))

        
if __name__ == "__main__":
    print(list(float_range(5, 5)))
    #doctest.testmod()