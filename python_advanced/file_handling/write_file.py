#!/usr/bin/env python3
"""Módulo con una función para escribir texto en un archivo."""


def write_file(filename="", text=""):
    """Devuelve la cantidad de caracteres escritos."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
