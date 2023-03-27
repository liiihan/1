#https://asecuritysite.com/encryption/sss_crt
# https://asecuritysite.com/encryption/sss_crt?val1=999
from libnum import solve_crt,generate_prime
from random import randint
import sys

base_path = sys.argv[1]

sharing_path = base_path + '/recover/denecrypt/origin/'
# print(secret)

secret_num = 20
recover_num = 10
if (len(sys.argv)>3):
	secret_num=int(sys.argv[2])
	recover_num=int(sys.argv[3])
secret_num = secret_num + 1
recover_num = recover_num + 1


with open(sharing_path + '0_m.txt','r') as f:
	m_0 = int(f.read())


share=[]
mod=[]
for i in range(2,recover_num+2):
	sharing_file = sharing_path + str(i) + '_s_m.txt'
	with open(sharing_file,'r') as f:
		_share,_mod = f.read().split(' ')
		# print('{} : {} {}'.format(str(i), str(_share), str(_mod)))
		share.append(int(_share))
		mod.append(int(_mod))
		

# print(share)
# print(mod)
res=solve_crt(share,mod) % m_0
print(res)
