from email.mime import base
from typing import ByteString
import rncryptor
import sys
import numpy as np
# base_path = sys.argv[1]

# face_Random = base_path + '/recover/face/new_fuzzyRandom.txt'                                                                            
# saltEncrypt_path = base_path + 'recover/denecrypt/salt'


# password = np.loadtxt(face_Random, dtype=str, delimiter=',')
# with open(face_Random,'rb') as f:
#     password = f.read()
# with open(saltEncrypt_file,'rb') as f:
#     encrypted_data=f.read()


# print('face fuzzyRandom: ',password)
# print('salt Encrypt-------------\n{}'.format(encrypted_data))

# data = '30525'
# password = b'(M\x97E\xef\x13&\x06\x9b\xce\xfaP)\x10\x9a"'

# rncryptor.RNCryptor's methods
# cryptor = rncryptor.RNCryptor()

# decrypted_data = cryptor.decrypt(encrypted_data, password)
# print(decrypted_data)
# assert data == decrypted_data

# print(encrypted_data, '\n', decrypted_data)

# # rncryptor's functions
# encrypted_data = rncryptor.encrypt(data, password)
# decrypted_data = rncryptor.decrypt(encrypted_data, password)
# assert data == decrypted_data


base_path = sys.argv[1]
face_Random = base_path + '/recover/face/new_fuzzyRandom.txt' 

sk1_sharing_origin = base_path + '/recover/denecrypt/origin/'
sk1_sharing_salt = base_path + '/recover/denecrypt/salt/'
secret_num = 20
recover_num = 10

with open(face_Random,'rb') as f:
	_Random2 = f.read()




if (len(sys.argv)>3):
	secret_num=int(sys.argv[2])
	recover_num=int(sys.argv[3])
secret_num = secret_num + 1
recover_num = recover_num + 1



# 去盐0_m.txt
sharing_file = sk1_sharing_origin + '0_m.txt'
salt_file = sk1_sharing_salt + '0_m.txt'
with open(salt_file,'rb') as f:
	m_0 = f.read()
	cryptor = rncryptor.RNCryptor()
	decrypted_data = cryptor.decrypt(m_0, _Random2)

with open(sharing_file,'w') as f:
	f.write(decrypted_data)
print('m_0_: {}'.format(str(decrypted_data)))
# 去盐i_s_m.txt
for i in range(2,recover_num+2):
	sharing_file = sk1_sharing_origin + str(i) + '_s_m.txt'
	salt_file = sk1_sharing_salt + str(i) + '_s_m.txt'
	with open(salt_file,'rb') as f:
		ttemp = f.read()
	cryptor = rncryptor.RNCryptor()
	decrypted_data = cryptor.decrypt(ttemp, _Random2)
	
	with open(sharing_file,'w') as f:
		f.write(decrypted_data)
	