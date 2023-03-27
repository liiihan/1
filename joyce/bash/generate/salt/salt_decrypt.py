from email.mime import base
from typing import ByteString
import rncryptor
import sys
import numpy as np
base_path = sys.argv[1]

face_Random = base_path + '/generate/face/fuzzyRandom.txt'                                                                            
saltEncrypt_file = base_path + '/generate/saltEncrypt.txt'


# password = np.loadtxt(face_Random, dtype=str, delimiter=',')
with open(face_Random,'rb') as f:
    password = f.read()
with open(saltEncrypt_file,'rb') as f:
    encrypted_data=f.read()


print('face fuzzyRandom: ',password)
print('salt Encrypt-------------\n{}'.format(encrypted_data))

# data = '30525'
# password = b'(M\x97E\xef\x13&\x06\x9b\xce\xfaP)\x10\x9a"'

# rncryptor.RNCryptor's methods
cryptor = rncryptor.RNCryptor()

decrypted_data = cryptor.decrypt(encrypted_data, password)
print(decrypted_data)
# assert data == decrypted_data

# print(encrypted_data, '\n', decrypted_data)

# # rncryptor's functions
# encrypted_data = rncryptor.encrypt(data, password)
# decrypted_data = rncryptor.decrypt(encrypted_data, password)
# assert data == decrypted_data