from collections import UserDict
import doctest


class PermaDict(UserDict):
    """a custom dictionary implementation that has immutable key-value-pairs

    :param UserDict: [description]
    :type UserDict: [type]
    :raises KeyError: [description]

    Examples:
    >>> locations = PermaDict({'Trey': "San Diego", 'Al': "San Francisco"})
    >>> locations['Harry'] = "London"
    >>> locations.update({'Russell': "Perth", 'Katie': "Sydney"})
    >>> locations['Trey']
    'San Diego'
    >>> locations = PermaDict([('Kojo', "Houston"), ('Tracy', "Toronto")])
    >>> list(locations)
    ['Kojo', 'Tracy']
    >>> list(locations.keys())
    ['Kojo', 'Tracy']
    >>> list(locations.values())
    ['Houston', 'Toronto']
    >>> locations = PermaDict({'David': "Boston"})
    >>> locations['David'] = "Amsterdam"
    Traceback (most recent call last):
    ...
    KeyError: "'David' already in dictionary."
    """
    def __init__(self, *args, silent: bool = False, **kwargs):
        super().__init__(*args, **kwargs)
        self.silent = silent

    def __setitem__(self, key, item):
        if key not in self:
            super().__setitem__(key, item)

        if not self.silent:
                raise KeyError(f"'{key}' already in dictionary.")

    def force_set(self, key, item):
        super().__setitem__(key, item)

    def update(self, *args, force: bool = False, **kwargs):
        if force:
            self.data.update(*args, **kwargs)
        else:
            super().update(other)


if __name__ == "__main__":
    p = PermaDict({'Trey': "San Diego", 'Al': "San Francisco"})

    doctest.testmod()