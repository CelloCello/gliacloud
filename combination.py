# -*- coding: utf-8 -*-

def combcount(n,r):
    f = lambda n, r: n * f(n-1, r) if n>r else 1
    return f(n, n-r)/f(r, 0)

print combcount(990, 33)