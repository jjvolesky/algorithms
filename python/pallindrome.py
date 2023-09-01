#@author Jackson Volesky github.com/jjvolesky

import sys

def pallindrome(str):
    return str.lower() == str[::-1].lower()

def main():
    args = sys.argv[1:]
    return pallindrome(args[0])

if __name__ == "__main__":
    print(main())