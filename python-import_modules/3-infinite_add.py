#!/usr/bin/python3
import sys

if __name__ == "__main__":
    # sys.argv[0] fayl adıdır, [1:] ilə yalnız daxil edilən rəqəmləri götürürük
    args = sys.argv[1:]
    total = 0

    # Hər bir arqumenti tam ədədə (int) çevirib toplayırıq
    for arg in args:
        total += int(arg)

    print("{}".format(total))
