from email.mime import base
from typing import ByteString
import rncryptor
import sys
import numpy as np
# base_path = sys.argv[1]

# sk1_file = base_path + '/generate/sk1.txt'
# face_Random = base_path + '/generate/face/fuzzyRandom.txt'                                                                            
# saltEncrypt_file = base_path + '/generate/sk1_salt.txt'

# with open(sk1_file,'r') as f:
# 	data = f.read()

# with open(face_Random,'rb') as f:
# 	password = f.read()

# print('secret: ',data)
# print('face fuzzyRandom: ',password)

# # rncryptor.RNCryptor's methods
# cryptor = rncryptor.RNCryptor()
# encrypted_data = cryptor.encrypt(data, password)
# print(encrypted_data)
# with open(saltEncrypt_file,'wb') as f:
# 	f.write(encrypted_data)


base_path = sys.argv[1]
face_Random = base_path + '/generate/face/fuzzyRandom.txt' 
sk1_sharing_origin = base_path + '/SecretSharing/origin/'
sk1_sharing_salt = base_path + '/SecretSharing/enecrypt/salt/'
secret_num = 20
recover_num = 10
with open(face_Random,'rb') as f:
	password = f.read()
# print(password)

if (len(sys.argv)>3):
	secret_num=int(sys.argv[2])
	recover_num=int(sys.argv[3])
secret_num = secret_num + 1
recover_num = recover_num + 1

# 加盐0_m.txt
sharing_file = sk1_sharing_origin + '0_m.txt'
with open(sharing_file,'r') as f:
	m_0 = f.read()
	cryptor = rncryptor.RNCryptor()
	encrypted_data = cryptor.encrypt(m_0, password)
salt_file = sk1_sharing_salt + '0_m.txt'
with open(salt_file,'wb') as f:
	f.write(encrypted_data)
print('salt_m_0: {}'.format(str(encrypted_data)))


# face_Random = base_path + '/recover/face/new_fuzzyRandom.txt' 
# with open(salt_file,'rb') as f:
# 	encrypted_data = f.read()
# with open(face_Random,'rb') as f:
# 	password = f.read()
# print(password)
# decrypted_data = cryptor.decrypt(encrypted_data, password)
# print(decrypted_data)
# 加盐i_s_m.txt
s_m=[]
for i in range(0,secret_num-1):
	sharing_file = sk1_sharing_origin + str(i) + '_s_m.txt'
	with open(sharing_file,'r') as f:
		s_m.append(f.read())
	cryptor = rncryptor.RNCryptor()
	encrypted_data = cryptor.encrypt(s_m[i], password)
	salt_file = sk1_sharing_salt + str(i) + '_s_m.txt'
	with open(salt_file,'wb') as f:
		f.write(encrypted_data)

