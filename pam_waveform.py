import numpy as np
from kam import pam_constellation
from scipy import special

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

def Qfunction(x):
    return 0.5 * special.erfc(x/np.sqrt (2.0))

def gray_code(m): 
    if m==1:
        g = ['0','1']
    elif m>1:
        gs = gray_code(m-1)
        gsr = gs[::-1]
        gs0 = ['0' + x for x in gs] 
        gs1 = ['1' + x for x in gsr] 
        g= gs0 + gs1
    return g

name = "Grigoris Arfanis"
print (toBinary(name))
print (len(gray_code(8)))

pam = pam_constellation(M=2,title="This is a test")
pam.set_symbols(toBinary(name))
pam.set_gray_bits(m=4)
pam.plot()