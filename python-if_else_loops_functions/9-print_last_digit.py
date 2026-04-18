#!/usr/bin/python3

def print_last_digit(number):
    """Ədədin sonuncu rəqəmini çap edir və qaytarır."""
    # Ədədin mənfi olub-olmadığını yoxlayırıq və son rəqəmi tapırıq
    if number < 0:
        last_digit = (number * -1) % 10
    else:
        last_digit = number % 10
    
    # Rəqəmi çap edirik (end="" istifadə etmirik, çünki main-də yan-yana istənilir)
    print("{}".format(last_digit), end="")
    
    # Tapdığımız rəqəmi funksiyadan geri qaytarırıq (return)
    return last_digit
