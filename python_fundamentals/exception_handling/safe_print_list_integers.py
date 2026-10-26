#!/usr/bin/env python3
def safe_print_list_integers(my_list=[], x=0):
    """Imprime x enteros de my_list y devuelve cuántos imprimió."""
    count = 0
    printed = 0
    while count < x:
        value = my_list[count]
        count += 1
        try:
            print("{:d}".format(value), end="")
            printed += 1
        except (TypeError, ValueError):
            pass
    print()
    return printed
