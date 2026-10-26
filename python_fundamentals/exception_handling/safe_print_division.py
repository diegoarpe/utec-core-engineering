#!/usr/bin/env python3
def safe_print_division(a, b):
    """Divide a entre b y muestra el resultado, o None si falla."""
    try:
        result = a / b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
