# Main

def method(decorator):
    def wrapper(target):
        def inner(*args, **kwargs):
            return decorator(target).config(*args, **kwargs).method(*args, **kwargs)
        return inner
    return wrapper
