# Problema:   112A - Petya and Strings
# Plataforma: Codeforces
# Enlace:     https://codeforces.com/problemset/problem/112/A
# Veredicto:  Accepted
# Notas:      Aprendí el uso de lower y comparación lexicográfica de string

import sys

def solve():
    p_min = sys.stdin.readline().strip().lower()
    q_min = sys.stdin.readline().strip().lower()
    
    if p_min < q_min:
        print("-1")
    elif p_min > q_min:
        print("1")
    else:
        print("0")
                   
solve()