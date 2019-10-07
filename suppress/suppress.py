from contextlib import contextmanager, ContextDecorator
from typing import List


""" first solution
@contextmanager
def suppress(*suppressed_exceptions: List[Exception]):
    try:
        yield
    except suppressed_exceptions:
        return
"""    

class SupressedException:
    def __init__(self, _exception_type = None, _traceback = None):
        self.exception = _exception_type
        self.traceback = _traceback

    def update(self, _exception_type, _traceback):
        self.exception = _exception_type
        self.traceback = _traceback

class suppress(ContextDecorator):

    def __init__(self, *_suppressed_exceptions: List[Exception]):
        self.suppressed_exceptions = _suppressed_exceptions
        self.return_val = SupressedException()

    def __enter__(self):
        return self.return_val
    
    def __exit__(self, exception_type, exception_value, traceback):
        if exception_type:
            if any(issubclass(exception_type, e) for e in self.suppressed_exceptions):
                self.return_val.update(exception_type(), traceback)
                
                return True


if __name__ == "__main__":
    with suppress(NameError):
        print("Hi!")
        print(name)
        print("Goodbye!")
    
    x = 0
    with  suppress(ValueError):
        x = int("hello")
    print(x)

    with suppress(ValueError, TypeError) as context:
        print(context.exception)
        x = int("hello")

    print(context.exception)

    @suppress(TypeError)
    def len_or_none(thing):
        return len(thing)

    print(len_or_none("hello"))
    print(len_or_none(64))

    with suppress(LookupError) as context:
        my_dict = {'key': 'value'}
        my_dict[4]

    print(context.exception)
        