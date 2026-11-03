#!/usr/bin/env python3
"""Module that defines the BaseGeometry class."""


class BaseGeometry:
    """Base class for geometric shapes with shared behavior."""

    def area(self):
        """Raise an exception because area is not implemented here."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
