from itertools import count

# increment ID by 1 every time function is called
class CallableCount(count):
    def __call__(self):
        return next(self)