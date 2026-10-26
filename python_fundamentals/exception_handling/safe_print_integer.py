#!/usr/bin/env python3
def safe_print_integer(value):
    """Imprime value si es un entero y devuelve True; si no, devuelve False."""
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        return False
