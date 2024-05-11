#!/usr/bin/env python3

import math
import statistics
import time

def power_iter(b, x):
    res = 1
    for i in range(x):
        res *= b
    return res


def power_iter_opt(b, x):
    res = 1
    while x > 0:
        if x % 2 == 0:
            b  *= b
            x //= 2
        else:
            res *= b
            x   -= 1
    return res


def power_rec(b, x):
    if x == 0:
        return 1
    else:
        return b * power_rec(b, x-1)


def power_dc(b, x):
    if x == 0:
        return 1
    if x % 2 == 0:
        return power_dc(b, x//2) * power_dc(b, x//2)
    else:
        return b * power_dc(b, x//2) * power_dc(b, x//2)


def power_dc_opt(b, x):
    if x == 0:
        return 1
    res = power_dc_opt(b, x//2)
    if x % 2 == 0:
        return  res * res
    else:
        return b * res * res


def pow_builtin(b, x):
    return b ** x

base = 2
exponent = 50
funs = [ pow, math.pow, pow_builtin, power_iter, power_rec, power_dc, power_dc_opt, power_iter_opt ]
for fun in funs:
    times = []
    for i in range(0, 41):
        start = time.perf_counter_ns()
        res = fun(base, exponent)
        times.append(time.perf_counter_ns() - start)
    print(f"{fun}: {statistics.median(times)} ns, result: {res}")
