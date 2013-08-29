python-utils
============

Various helpful Python utility classes and functions.


func_utils
----------

  * memoized - Simple memoization (caching) decorator for an instance method.

```python
class MyClass(object):
    @memoized
    def name_of_method(self, arg1):
        return something_that_takes_a_while_to_compute_or_has_side_effects(arg1)
my_obj = MyClass()
my_obj.name_of_method(123)
```

  * memoized_property - Simple memoization (caching) decorator for a method that takes no arguments and is used as a property.

```python
class MyClass(object):
    @memoized_property
    def name_of_method(self):
        return something_that_takes_a_while_to_compute_or_has_side_effects()
my_obj = MyClass()
my_obj.name_of_method
```

  * class_property - Simple decorator for a class method that takes no arguments and is used as a property.

```python
class MyClass(object):
    @class_property
    def name_of_method(cls):
        return some_value
MyClass.name_of_method
```

  * memoized_class_property - Simple memoization (caching) decorator for a class method that takes no arguments and is used as a property.

```python
class MyClass(object):
    @memoized_class_property
    def name_of_method(cls):
        value = something_that_takes_a_while_to_compute_or_has_side_effects()
        return value
MyClass.name_of_method
```

  * memoized_class_method - Simple memoization (caching) decorator for a class method.

```python
class MyClass(object):
    @memoized_class_method
    def name_of_method(cls, arg):
        value = something_that_takes_a_while_to_compute_or_has_side_effects(arg)
        return value
MyClass.name_of_method(arg)
```

  * deprecated

```python
class MyClass(object):
    @deprecated
    def deprecated_method(self):
        print 'Should see a deprecation warning when calling this.'
    @deprecated('custom deprecation message')
    def deprecated_method_with_custom_message(self):
        print 'Should see a custom deprecation warning when calling this.'
```
