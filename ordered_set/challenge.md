
# OrderedSet

Assigned from Intermediate Level on 10/21/2019

Hello!

This week I'd like you to make an OrderedSet class. This class should work like a set, but it should also maintain the insertion order of the items added to it (unlike Python's built-in set which is unordered).

```python
ordered_words = ['these', 'are', 'words', 'in', 'an', 'order']
>>> print(*set(ordered_words))
order these are in an words
>>> print(*OrderedSet(ordered_words))
these are words in an order
>>> print(*OrderedSet(['repeated', 'words', 'are', 'not', 'repeated']))
repeated words are not
```

This set should be relatively memory efficient and containment checks should be relatively time efficient:

```python
>>> words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
>>> len(words)
4
>>> 'hello' in words
True
```

Initially you don't have to worry about allowing sets to be modified after they've been made. Just focus on getting len and the in operator.

For the first bonus, I'd like you to make sure your set works with the add and discard methods:

```python
>>> words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
>>> words.add('doing')
>>> print(*words)
hello how are you doing
>>> words.discard('are')
>>> print(*words)
hello how you doing
```

For the second bonus, I'd like you to make your OrderedSet class support equality. If an OrderedSet is compared to another OrderedSet, they'll only be seen as equal if the order is the same. If an OrderedSet is compared to an unordered set, the order is ignored during the comparison. If an OrderedSet is compared to a non-set, the comparison should evaluate as False (unless the other object implements equality with ordered sets.

```python
>>> OrderedSet(['how', 'are', 'you']) == OrderedSet(['how', 'you', 'are'])
False
>>> OrderedSet(['how', 'are', 'you']) == {'how', 'you', 'are'}
True
>>> OrderedSet(['how', 'are', 'you']) == ['how', 'are', 'you']
False
```

For the third bonus, I'd like your OrderedSet class to support indexing:

```python
>>> words = OrderedSet(['hello', 'hello', 'how', 'are', 'you'])
>>> words[1]
'how'
>>> words[-1]
'you'
```

Automated tests for this week's exercise can be found here. You'll need to write your function in a module named orderedset.py next to the test file. To run the tests you'll run "python test_orderedset.py" and check the output for "OK". You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.
