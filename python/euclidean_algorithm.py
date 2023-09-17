#author Jackson Volesky github.com/jjvolesky
import sys

def gcd(a,b):
    return b % a == 0 ? a : gcd(b % a, a)

def euclidean(a,b):
    print(f'gcd({a}, {b}) = {a} * {int(b/a)} + {b % a}')
    return b % a == 0 ? a : gcd(b%a, a)
