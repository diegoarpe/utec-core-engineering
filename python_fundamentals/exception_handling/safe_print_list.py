#!/usr/bin/env python3
def safe_print_list(my_list=[], x=0):
    """Imprime hasta x elementos de my_list en una línea y devuelve cuántos imprimió."""
    count = 0
    try:
        while count < x:
            print("{}".format(my_list[count]), end="")
            count += 1
    except IndexError:
        pass
    print()
    return count
