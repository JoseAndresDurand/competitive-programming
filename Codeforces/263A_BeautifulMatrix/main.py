# Problema:   263A - A. Beautiful Matrix
# Plataforma: Codeforces
# Enlace:     https://codeforces.com/problemset/problem/263/A
# Veredicto:  Accepted
# Notas:      Reforcé el uso de string, int con sys.stdin...

import sys

def solve():
    for i in range(5):
        fila = sys.stdin.readline().strip().split()
        for j in range(5):
            if fila[j]=='1':
                print(f"{abs(i-2)+abs(j-2)}")
                return        
solve()