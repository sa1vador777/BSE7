#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main(lst: list[int]) -> list[int]:
    ind = lst.index(max(lst))
    lst[0], lst[ind] = max(lst), lst[0]
    return lst


if __name__ == "__main__":
    print(main([1, 2, 3, 4, 5]))
