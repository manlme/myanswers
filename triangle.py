#!/usr/local/bin/python

def tell_triangle(a,b,c):
    if all(x > 0 for x in [a,b,c]):
        pass
    else:
        return 'not a triangle'
    precision = 0.00000001
    if a+b > c and a+c> b and b+c>a:
        pass
    else:
        return 'not a triangle'
    if a == b == c:
        return "equilateral"
    elif abs(a-b) < precision or abs(a-c) < precision or abs(b-c) < precision:
        return  "isosceles"
    else:
        return "scalene"
