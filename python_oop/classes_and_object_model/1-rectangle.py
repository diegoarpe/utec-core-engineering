#!/usr/bin/env python3
"""Módulo que define la clase Rectangle para representar un rectángulo."""


class Rectangle:
    """Clase que define un rectángulo."""
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Ancho del rectángulo."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setea el ancho del rectángulo."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Alto del rectángulo."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setea el alto del rectángulo."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calcula el área del rectángulo."""
        return self.__width * self.__height

    def perimeter(self):
        """Calcula el perímetro del rectángulo."""
        return 2 * (self.__width + self.__height)
