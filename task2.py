#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import prod


def main(lst: list[float]) -> list[int]:
    negative_sum = sum([num for num in lst if num < 0])
    max_ind, min_ind = lst.index(max(lst)), lst.index(min(lst))
    source_prod = prod(lst[min_ind+1:max_ind])
    return [negative_sum, source_prod]


if __name__ == "__main__":
    print(main([1.5, 2.0, 3.0, 4.0, -8.1241, -1.0, 3, 2, 4.5]))
