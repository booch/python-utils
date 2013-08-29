'''
Function helper functions.

by Craig Buchek

These took a lot of trial and error to get right, but seem to be working well now.
I read through a lot of various other attempts to implement these (separately).
I don't claim to understand Python decorators well - just well enough to get these to work like I wanted.
'''


class decorator(object):
    '''
        Base class for "polite" decorators.
        Adapted from https://gist.github.com/kylebgorman/5878715 and http://www.artima.com/weblogs/viewpost.jsp?thread=240845.

        Usage - subclass from decorator, and override _do_():
            class my_decorator(decorator):
                def _do_(self, instance, *args, **kwargs):
                    do_something_before_decorated_function()
                    result = self.function(instance, *args, **kwargs)
                    do_something_after_decorated_function()
                    return result
    '''

    def __init__(self, *args, **kwargs):
        if callable(args[0]):
            self.function = args[0]
            self.args = list(args).remove(args[0])
            self.kwargs = kwargs
        else:
            self.function = None
            self.args = args
            self.kwargs = kwargs
 
    def __doc__(self):
        return self.function.__doc__
 
    def __repr__(self):
        return repr(self.function)
 
    def __str__(self):
        return str(self.function)
 
    def __name__(self):
        return self.function.__name__

    def __call__(self, *args, **kwargs):
        if self.function:
            return self._do_(self, *args, **kwargs)
        else:
            self.function = args[0]
            def wrapped_function(instance, *wrapped_args, **wrapped_kwargs):
                return self._do_(instance, *wrapped_args, **wrapped_kwargs)
            return wrapped_function

    # Override this!
    def _do_(self, instance, *args, **kwargs):
        return self.function(instance, *args, **kwargs)

    # Define __get__ if you want to make the function behave like a property instead of a method.


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


class class_property(classmethod):
    '''
        Simple decorator for a class method that takes no arguments and is used as a property.
        NOTE: This works only for read-only properties; it does not handle getters, setters, or deleters like the built-in @property decorator.

        Usage:
            class MyClass(object):
                @class_property
                def name_of_method(cls):
                    return some_value
            MyClass.name_of_method
            
    '''
    def __init__(self, func):
        self.func = func

    def __call__(self, obj):
        return self.func(obj)

    def __get__(self, obj, objtype):
        return self.__call__(objtype)


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
