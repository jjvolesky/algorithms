import sys



def gcd(a,b):
    print(f'gcd({a}, {b}) = {a} * {int(b/a)} + {b % a}')
    if b % a == 0:
        return a
    else:
        return gcd(b % a, a)

if __name__ == "__main__":
    argv = sys.argv
    print(f'gcd({argv[1]}, {argv[2]}) = {gcd(int(argv[1]), int(argv[2]))}')
