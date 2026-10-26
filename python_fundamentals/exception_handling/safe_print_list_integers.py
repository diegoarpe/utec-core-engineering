#!/usr/bin/env python3
def safe_print_list_integers(my_list=[], x=0):
    """Imprime x enteros de my_list y devuelve cuántos imprimió."""
    count = 0
    printed = 0
    try:
        while count < x:
            value = my_list[count]
            count += 1
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                printed += 1
    except IndexError:
        pass
    print()
    return printed
