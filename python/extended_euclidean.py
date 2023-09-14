import sys

def extended_euclidean(a, b):
    quotients = []
    u = a
    v = b
    while (a != 0):
        quotients.append(int(b/a))
        r = b % a
        b = a
        a = r
    print(f'gcd({u}, {v}) = {b}\n')
    Q = [1, 0, 1]
    P = [0, 1, quotients[0]]
    for i in range(3, len(quotients) + 2):
        Qi = (Q[i-1] * quotients[i - 2]) + Q[i-2]
        Pi = (P[i-1] * quotients[i - 2]) + P[i-2]
        Q.append(Qi)
        P.append(Pi)
    magic_box(quotients, P, Q)
    x_and_y = find_x_and_y(u, v, b, P[len(P) -2], Q[len(Q) - 2])

def find_x_and_y(a, b, gcd, x, y):
    if a*x - b*y == gcd:
        y = -y
    elif b*y - a*x == gcd:
        x = -x
    else:
        print(f'no x and y such that {a}x + {b}y = {gcd}')
        return
    print(f'x = {x}, y = {y}', end=" => ")
    print(f'{a}({x}) + {b}({y}) = {gcd}')    

def magic_box(quotients, P, Q):
    print('    ', end='')
    for q in quotients:
        print(f'{q} ', end='')
    print()
    for p in P:
        print(f'{p} ', end='')
    print()
    for q in Q:
        print(f'{q} ', end='')
   #print(x_and_y)
    print('\n')

if __name__ == "__main__":
    argv = sys.argv
    extended_euclidean(int(argv[1]), int(argv[2]))
    
