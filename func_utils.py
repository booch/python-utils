'''
Function helper functions.

by Craig Buchek

These took a lot of trial and error to get right, but seem to be working well now.
I read through a lot of various other attempts to implement these (separately).
I don't claim to understand Python decorators well - just well enough to get these to work like I wanted.
'''


class memoized_property(object):
    '''
        Simple memoization (caching) decorator for a method that takes no arguments and is used as a property.
        NOTE: This works only for read-only properties; it does not handle getters, setters, or deleters like the built-in @property decorator.
        
        Usage:
            class MyClass(object):
                @memoized_property
                def name_of_method(self):
                    value = something_that_takes_a_while_to_compute_or_has_size_effects()
                    return value
            my_obj = MyClass()
            my_obj.name_of_method
    '''
    def __init__(self, func):
        self.func = func

    def __call__(self, obj):
        if not hasattr(obj, '_memoization_cache'):
            obj._memoization_cache = {}
        if not obj._memoization_cache.has_key(self.func.__name__):
            obj._memoization_cache[self.func.__name__] = self.func(obj)
        return obj._memoization_cache[self.func.__name__]

    def __get__(self, obj, objtype):
        return self.__call__(obj)


class memoized_class_property(classmethod):
    '''
        Simple memoization (caching) decorator for a class method that takes no arguments and is used as a property.
        NOTE: This works only for read-only properties; it does not handle getters, setters, or deleters like the built-in @property decorator.

        Usage:
            class MyClass(object):
                @memoized_class_property
                def name_of_method(cls):
                    value = something_that_takes_a_while_to_compute_or_has_size_effects()
                    return value
            MyClass.name_of_method
            
    '''
    def __init__(self, func):
        self.func = func

    def __call__(self, obj):
        if not hasattr(obj, '_memoization_cache'):
            obj._memoization_cache = {}
        if not obj._memoization_cache.has_key(self.func.__name__):
            obj._memoization_cache[self.func.__name__] = self.func(obj)
        return obj._memoization_cache[self.func.__name__]

    def __get__(self, obj, objtype):
        return self.__call__(objtype)
