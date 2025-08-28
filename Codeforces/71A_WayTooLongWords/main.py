# Problema:   71A - A. Way Too Long Words
# Plataforma: Codeforces
# Enlace:     https://codeforces.com/problemset/problem/71/A
# Veredicto:  Accepted
# Notas:      Aprendí el uso de la librería sys y sus métodos.

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
            