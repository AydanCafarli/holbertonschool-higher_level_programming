#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # sys.argv[0] hər zaman proqramın adıdır (./2-args.py)
    # Ona görə biz 1-ci indeksdən başlayaraq arqumentləri götürürük
    args = sys.argv[1:]
    count = len(args)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # Hər bir arqumenti nömrələyib çap edirik
    for i in range(count):
        print("{}: {}".format(i + 1, args[i]))
