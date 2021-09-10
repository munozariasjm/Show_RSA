import numpy as np
import string
import numba
from creatorRSA import *



num_alfa = {i: chr(i) for i in range(128)}


alfa_num = {value : key for (key, value) in num_alfa.items()}


@numba.jit
def mapear(l: int, n: int, e: float):
    val = alfa_num[l];
    return (val**e)%n
    
@numba.jit    
def encriptar(mensaje: str, sec: str) -> int:
    n,e = getPUBLIC(sec)
    letras = list(mensaje.lower())
    numeros = [mapear(l,n,e) for l in letras]
    return numeros 
    
