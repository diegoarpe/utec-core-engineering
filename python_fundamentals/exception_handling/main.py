#!/usr/bin/env python3
safe_print_integer = __import__('safe_print_integer').safe_print_integer

print(safe_print_integer(42))
print(safe_print_integer(-7))
print(safe_print_integer(3.14))
print(safe_print_integer("Hello"))