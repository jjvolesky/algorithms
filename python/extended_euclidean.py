#author Jackson Volesky github.com/jjvolesky
import sys

def extended_euclidean(a, b):
    """
       parameters: integers a and b where a <= b

       returns: quotients - array; quotients produced by the algorithm
                P - array; the top row of the `magic box` algorithm
                Q - array; the bottom row of the `magic box` algorithm
                x, y - two integers such that a*x^-1*t + b*x^-1*t-1 = gcd(x,y) mod y
                     - if x and y do not exist, returns -1, -1
    """     
    quotients = []
    u = a
    v = b
    while (a != 0):
        quotients.append(int(b/a))
        r = b % a
        b = a
        a = r
    Q = [1, 0, 1]
    P = [0, 1, quotients[0]]
    for i in range(3, len(quotients) + 2):
        Qi = (Q[i-1] * quotients[i - 2]) + Q[i-2]
        Pi = (P[i-1] * quotients[i - 2]) + P[i-2]
        Q.append(Qi)
        P.append(Pi)
   return quotients, P, Q, find_x_and_y(P[len(P) - 1], Q[len(Q) -1]) 

def find_x_and_y(a, b, gcd, x, y):
    if a*x - b*y == gcd:
        y = -y
    elif b*y - a*x == gcd:
        x = -x
    else:
        print(f'no x and y such that {a}x + {b}y = {gcd}')
        return -1, -1
    return x, y

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
    
