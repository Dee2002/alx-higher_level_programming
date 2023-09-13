#!/usr/bin/python3

# Documentation for the module
"""
This module provides a function for
looking up the attributes and methods of an object.

Usage:
    import lookup_module
    result = lookup_module.lookup(obj)

Where:
    - obj: The object to inspect.

Example:
    import lookup_module

    class SampleClass:
        def sample_method(self):
            pass

    sample_obj = SampleClass()

    attributes_and_methods = lookup_module.lookup(sample_obj)
    print(attributes_and_methods)

This module can be used to inspect
the attributes and methods of any Python object.
"""

# Documentation for the class
"""

Attributes:
    None

Methods:
    None

"""

# Documentation for the method
"""
This is a method inside the class for demonstration

Args:
    None

Returns:
    None

"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the attributes and methods of the object.
    """
    return dir(obj)
