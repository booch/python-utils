python-utils
============

Various helpful Python utility classes and functions.


func_utils
----------

  * memoized_property - Simple memoization (caching) decorator for a method that takes no arguments and is used as a property.

```python
    class MyClass(object):
        @memoized_property
        def name_of_method(self):
            value = something_that_takes_a_while_to_compute_or_has_size_effects()
            return value
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
            value = something_that_takes_a_while_to_compute_or_has_size_effects()
            return value
    MyClass.name_of_method
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
