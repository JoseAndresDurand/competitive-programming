import sys

def solve():
    try:
        n = int(sys.stdin.readline().strip())
    except (ValueError, IndexError):
        return

    for _ in range(n):
        palabra = sys.stdin.readline().strip()
        
        if len(palabra) > 10:
            print(f"{palabra[0]}{len(palabra)-2}{palabra[-1]}")
        else:
            print(palabra)
solve()
            