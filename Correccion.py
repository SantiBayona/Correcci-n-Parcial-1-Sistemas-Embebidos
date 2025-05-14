import uctypes
import array
from machine import mem32

datos = array.array('i', [
    0, 0,     # P0 (x0, y0)
    1, 2,     # P1 (x1, y1)
    3, 3,     # P2 (x2, y2)
    4, 0      # P3 (x3, y3)
])

base_dir = uctypes.addressof(datos)
dir_P0 = base_dir
dir_P1 = base_dir + 8
dir_P2 = base_dir + 16
dir_P3 = base_dir + 24

def leer_punto(direccion):
    x = mem32[direccion]
    y = mem32[direccion + 4]
    return (x, y)

def bezier_mem32(dir_P0, dir_P1, dir_P2, dir_P3, n):
    P0 = leer_punto(dir_P0)
    P1 = leer_punto(dir_P1)
    P2 = leer_punto(dir_P2)
    P3 = leer_punto(dir_P3)
    
    resultado = []
    for i in range(n + 1):
        t = i / n
        x = (1 - t)**3 * P0[0] + 3 * (1 - t)**2 * t * P1[0] + 3 * (1 - t) * t**2 * P2[0] + t**3 * P3[0]
        y = (1 - t)**3 * P0[1] + 3 * (1 - t)**2 * t * P1[1] + 3 * (1 - t) * t**2 * P2[1] + t**3 * P3[1]
        resultado.append((int(x), int(y)))
    return resultado

n = 4
LR = bezier_mem32(dir_P0, dir_P1, dir_P2, dir_P3, n)

for i, punto in enumerate(LR):
    print("LR[{}] = ({}, {})".format(i, punto[0], punto[1]))
