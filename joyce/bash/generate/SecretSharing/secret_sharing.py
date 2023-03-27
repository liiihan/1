#https://asecuritysite.com/encryption/sss_crt
# https://asecuritysite.com/encryption/sss_crt?val1=999
from libnum import solve_crt,generate_prime
from random import randint
import sys

bitsize=60 # 60-bit primes

m=[0] * 5 # Array with five values
share=[0] * 5 # Array with five values

m[0]=generate_prime(bitsize)
m[1]=generate_prime(bitsize)
m[2]=generate_prime(bitsize)
m[3]=generate_prime(bitsize)
m[4]=generate_prime(bitsize)

m = sorted(m)

while ((m[1]*m[2]*m[3] < m[0]*m[3]*m[4]) and m[4]<m[3]):
    m[4]=generate_prime(bitsize)

M=m[1]*m[2]
# for 3 from 4 we must have m1*m2*m3>m0xm3xm4

secret=100
if (len(sys.argv)>1):
	secret=int(sys.argv[1])

alpha= randint(1, M)

share[0] = (secret+alpha*m[0])  % m[1]
share[1] = (secret+alpha*m[0])  % m[2]
share[2] = (secret+alpha*m[0])  % m[3]
share[3] = (secret+alpha*m[0])  % m[4]

print ("Secret: ",secret)

print ("Alpha: ",alpha)


print ("\nPrime0: ",m[0])
print ("Prime1: ",m[1])
print ("Prime2: ",m[2])
print ("Prime3: ",m[3])
print ("Prime4: ",m[4])


print ("\nShare 1 (s1,m1): ",share[0],m[1])
print ("Share 2 (s2,m2): ",share[1],m[2])
print ("Share 3 (s3,m3): ",share[2],m[3])
print ("Share 4 (s4,m4): ",share[3],m[4])
print ("Public part (m0): ",m[0])

print ("\nNow using the first three shares and solve CRT")
rem=[share[0],share[1],share[2]]
mod=[m[1],m[2],m[3]]


res=solve_crt(rem,mod) % m[0]

print ("Secret: ",res)

print ("\nNow using the first two shares and solve CRT")
mod=[m[1],m[2]]
rem=[share[0],share[1]]

res=solve_crt(rem,mod) % m[0]

print ("Secret: ",res)