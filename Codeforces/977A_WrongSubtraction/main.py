# Problema:   977A - A. Wrong Subtraction
# Plataforma: Codeforces
# Enlace:     https://codeforces.com/problemset/problem/977/A
# Veredicto:  Accepted
# Notas:      Reforcé el uso de % y abreviaciones //= y -=

import sys

def solve():
    n,k = map(int, sys.stdin.readline().strip().split())   
    for _ in range(k):
        if n%10 == 0:
            n //= 10
        else:
            n -= 1
    print(f"{n}")    
    
solve()