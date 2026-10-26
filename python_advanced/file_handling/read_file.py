#!/usr/bin/env python3
"""Módulo con una función para leer e imprimir un archivo de texto."""

def read_file(filename=""):
    """Lee un archivo de texto UTF-8 y lo imprime en stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
