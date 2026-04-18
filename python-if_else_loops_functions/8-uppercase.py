#!/usr/bin/python3

def uppercase(str):
    """Sətirdəki bütün kiçik hərfləri böyük hərflə çap edən funksiya."""
    for char in str:
        # Simvolun ASCII kodunu alırıq
        code = ord(char)
        # Əgər simvol 'a' (97) və 'z' (122) arasındadırsa (yəni kiçik hərfdirsə)
        if code >= 97 and code <= 122:
            # Ondan 32 çıxıb böyük hərfi tapırıq
            char = chr(code - 32)
        
        # Simvolu çap edirik (end="" istifadə edirik ki, yan-yana düzülsün)
        print("{}".format(char), end="")
    
    # Bütün sətir bitdikdən sonra yeni sətirə keçmək üçün bir boş print
    print("")
