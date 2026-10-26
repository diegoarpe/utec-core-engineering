#!/usr/bin/env python3
"""Módulo con una función para añadir texto al final de un archivo."""


def append_write(filename="", text=""):
    """Append al final + devuelve los caracteres."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
