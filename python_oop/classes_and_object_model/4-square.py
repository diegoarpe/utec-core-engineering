#!/usr/bin/env python3
"""Módulo que define la clase Square para representar un cuadrado."""


class Square:
    """Clase que define un cuadrado."""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Area del cuadrado."""
        return self.__size ** 2

    @property
    def size(self):
        """Tamaño del cuadrado."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setea el tamaño del cuadrado."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
