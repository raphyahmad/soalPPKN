from Crypto.Util.number import *

flag = b'SIJAQUIZ{53l4m47_4nd4_73l4h_m3nd4p47k4n_fl49ny4}'
m = bytes_to_long(flag)

p = getPrime(256)

q = getPrime(256)

n = p * q
print(n)
e = 65537

phi = (p-1)*(q-1)
d = pow(e, -1, phi)
print(d)

c = pow(m, e, n)
print('Ciphertext:', c)

decrypted = pow(c, d, n)
print(long_to_bytes(decrypted))
