# Problema:   158A - A. Next Round
# Plataforma: Codeforces
# Enlace:     https://codeforces.com/problemset/problem/158/A
# Veredicto:  Accepted
# Notas:      Reforcé el uso de strip, split y leer mejor los problemas.

import sys

def solve():
    n,k = map(int,sys.stdin.readline().strip().split())
    scores = list(map(int, sys.stdin.readline().strip().split()))
    corte = scores[k-1]
    c = 0
    for i in scores: 
        if i >= corte and i>0:
            c += 1
    print(f"{c}")

solve()