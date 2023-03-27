#https://asecuritysite.com/encryption/sss_crt
# https://asecuritysite.com/encryption/sss_crt?val1=999
from libnum import solve_crt,generate_prime
from random import randint
import sys

base_path = sys.argv[1]
secret_file = base_path + '/generate/sk1.txt'
with open(secret_file,'r') as f:
	secret = int(f.read())
sharing_path = base_path + '/SecretSharing/origin/'
# print(secret)
bitsize=60 # 60-bit primes
secret_num = 20
recover_num = 10

if (len(sys.argv)>3):
	secret_num=int(sys.argv[2])
	recover_num=int(sys.argv[3])
secret_num = secret_num + 1
recover_num = recover_num + 1
m=[0] * secret_num # Array with five values
share=[0] * (secret_num-1) # Array with five values

for i in range(0,secret_num):
	m[i]=generate_prime(bitsize)

m = sorted(m)

#这一段可能是必要的，遇到问题可以看一下
# while ((m[1]*m[2]*m[3] < m[0]*m[3]*m[4]) and m[4]<m[3]):
#     m[4]=generate_prime(bitsize)

M=1
for i in range(1,recover_num):
	M = M * m[i]
# for 3 from 4 we must have m1*m2*m3>m0xm3xm4

alpha= randint(1, M)

for i in range(0,secret_num-1):
	share[i] = (secret+alpha*m[0])  % m[i+1]

print ("Input Secret: ",secret)
# print ("Alpha: ",alpha)
# print ("Public part (m0): ",m[0])

# 保存所有碎片(s1,m1)
sharing_file = sharing_path + '0_m.txt'
with open(sharing_file,'w') as f:
	f.write(str(m[0]))
print('m_0: {}'.format(m[0]))
for i in range(0,secret_num-1):
	sharing_file = sharing_path + str(i) + '_s_m.txt'
	with open(sharing_file,'w') as f:
		f.write('{} {}'.format(str(share[i]),str(m[i+1])))

# sharex=[]
# modx=[]
# for i in range(0,recover_num):
# 	# sharing_file = sharing_path + str(i) + '_s_m.txt'
# 	# with open(sharing_file,'r') as f:
# 		# _share,_mod = f.read().split(' ')
# 	_share = share[i]
# 	_mod = m[i+1]
# 	print('{} : {} {} : {}'.format(str(i), str(_share), str(i+1), str(_mod)))
# 	sharex.append(_share)
# 	modx.append(_mod)
# res=solve_crt(sharex,modx) % m[0]
# print(res)