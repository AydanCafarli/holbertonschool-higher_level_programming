#!/usr/bin/python3
"""
hidden_4.pyc modulundan daxili adları kəşf edən və çap edən skript.
"""
import hidden_4


def discover_hidden():
    """
    hidden_4 modulundakı "__" ilə başlamayan bütün adları
    əlifba sırası ilə çap edir.
    """
    # dir() funksiyası modulun içindəki bütün adları siyahı şəklində qaytarır
    all_names = dir(hidden_4)

    # Siyahını əlifba sırası ilə sıralayırıq
    all_names.sort()

    # Adları tək-tək yoxlayıb şərtə uyğun çap edirik
    for name in all_names:
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    # Bu blok kodun başqa fayl tərəfindən import edildikdə
    # icra olunmamasını təmin edir.
    discover_hidden()
