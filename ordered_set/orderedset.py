import doctest
from collections.abc import MutableSet, Sequence


class OrderedSet(Sequence, MutableSet):
    """set that keeps order of words

    >>> ordered_words = ['these', 'are', 'words', 'in', 'an', 'order']
    >>> print(*OrderedSet(ordered_words))
    these are words in an order
    >>> print(*OrderedSet(['repeated', 'words', 'are', 'not', 'repeated']))
    repeated words are not
    >>> words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
    >>> len(words)
    4
    >>> 'hello' in words
    True
    >>> words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
    >>> words.add('doing')
    >>> print(*words)
    hello how are you doing
    >>> words.discard('are')
    >>> print(*words)
    hello how you doing
    >>> OrderedSet(['how', 'are', 'you']) == OrderedSet(['how', 'you', 'are'])
    False
    >>> OrderedSet(['how', 'are', 'you']) == {'how', 'you', 'are'}
    True
    >>> OrderedSet(['how', 'are', 'you']) == ['how', 'are', 'you']
    False
    >>> words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
    >>> words[1]
    'how'
    >>> words[-1]
    'you'
    """    
    def __init__(self, iterable):
        self.items = set()
        self.order = []
        self |= iterable # or implementation

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, pos):
        return self.order[pos]

    def __eq__(self, other):
        if isinstance(other, type(self)):
            return (
                len(self) == len(other) and
                all(x == y for x,y in zip(self, other))
            )
        
        return super().__eq__(other)
        
    def add(self, item):
        if item not in self.items:
            self.order.append(item)
        self.items.add(item)
    
    def discard(self, item):
        if item in self.items:
            self.order.remove(item)
            self.items.remove(item)
        


if __name__ == "__main__":
    doctest.testmod()