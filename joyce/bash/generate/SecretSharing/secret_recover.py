#https://asecuritysite.com/encryption/sss_crt
# https://asecuritysite.com/encryption/sss_crt?val1=999
from libnum import solve_crt,generate_prime
from random import randint
import sys

base_path = sys.argv[1]

sharing_path = base_path + '/SecretSharing/'

secret_num = 20
recover_num = 10

if (len(sys.argv)>3):
	secret_num=int(sys.argv[2])
	recover_num=int(sys.argv[3])
secret_num = secret_num + 1
recover_num = recover_num + 1

m=[]
share=[]
sharing_file = sharing_path + '0_m.txt'
with open(sharing_file, 'r') as f:
	m.append(int(f.read()))
for i in range(0,secret_num-1):
	sharing_file = sharing_path + str(i) + '_s_m.txt'
	with open(sharing_file,'r') as f:
		i_sharing, i_m = f.read().split(' ')
		m.append(int(i_m))
		share.append(int(i_sharing))
mod=[]
rem=[]
for i in range(4,recover_num+4):
	mod.append(m[i+1])
	rem.append(share[i])

res=solve_crt(rem,mod) % m[0]

print ("Recover Secret: ",res)

		