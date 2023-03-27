#https://asecuritysite.com/encryption/sss_crt
# https://asecuritysite.com/encryption/sss_crt?val1=999
from libnum import solve_crt,generate_prime
from random import randint
import sys

bitsize=60 # 60-bit primes
secret_num = 20
recover_num = 10
secret_num = secret_num + 1
recover_num = recover_num + 1
m=[0] * secret_num # Array with five values
share=[0] * (secret_num-1) # Array with five values

for i in range(0,secret_num):
	m[i]=generate_prime(bitsize)

m = sorted(m)

# while ((m[1]*m[2]*m[3] < m[0]*m[3]*m[4]) and m[4]<m[3]):
#     m[4]=generate_prime(bitsize)

M=1
for i in range(1,recover_num):
	M = M * m[i]
# for 3 from 4 we must have m1*m2*m3>m0xm3xm4

secret=100
if (len(sys.argv)>1):
	secret=int(sys.argv[1])

alpha= randint(1, M)

for i in range(0,secret_num-1):
	share[i] = (secret+alpha*m[0])  % m[i+1]

print ("Secret: ",secret)

print ("Alpha: ",alpha)


# print ("\nPrime0: ",m[0])
# print ("Prime1: ",m[1])
# print ("Prime2: ",m[2])
# print ("Prime3: ",m[3])
# print ("Prime4: ",m[4])


# print ("\nShare 1 (s1,m1): ",share[0],m[1])
# print ("Share 2 (s2,m2): ",share[1],m[2])
# print ("Share 3 (s3,m3): ",share[2],m[3])
# print ("Share 4 (s4,m4): ",share[3],m[4])
# print ("Public part (m0): ",m[0])

sharex=[]
modx=[]
for i in range(0,recover_num):
	# sharing_file = sharing_path + str(i) + '_s_m.txt'
	# with open(sharing_file,'r') as f:
		# _share,_mod = f.read().split(' ')
	_share = share[i]
	_mod = m[i+1]
	print('{} : {} {} : {}'.format(str(i), str(_share), str(i+1), str(_mod)))
	sharex.append(_share)
	modx.append(_mod)
res=solve_crt(sharex,modx) % m[0]
print(res)