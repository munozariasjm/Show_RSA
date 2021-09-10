import numpy as np
import math
import numba

@numba.jit
def isPrime(k: int) -> bool:
	"""
	input: The integer to evaluate
    output: Whether its prime
	"""
    ban=True
    for z in range(2,k): 
        if k%z==0: ban=False
    return ban

sec=100
def setSec(secs): sec=secs
    
def generarVals(numerito: int):
	"""
	input: Number to generate the seed to
    output: The generated encription for this number 
	"""
    
    e=65537
    p=11;q=17    
    phi=(p-1)*(q-1)
    n=p*q
    
    while True:
        e=np.random.randint(2,phi/2)
        if p%e!=1 and q%e!=1: break
    e=3
    
    return n,e,phi


def getPUBLIC(sec=100): 
    """
	input: Secret number to generate
    output: Public values relating to encription
	"""
    n,e,f=generarVals(sec)
    return int(n),int(e)

i=np.random.randint(1,4)


def getPRIVATE(sec=100):
    """
	input: Secret number to generate
    output: Secret values relating to encription
	"""
    n,e,phi=generarVals(sec)
    
    d=((2*phi)+1)/e
    return int(d)
