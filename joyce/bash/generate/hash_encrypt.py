#https://github.com/ecies/py
from email.mime import base
import hashlib
import sys
from ecies.utils import generate_eth_key, generate_key
from ecies import encrypt, decrypt
from os import environ, urandom
from eth_keys import keys

def _generate_eth_key() -> keys.PrivateKey:
	"""
	Generate random eth private key

	Returns
	-------
	eth_keys.keys.PrivateKey
		An ethereum key

	>>> k = generate_eth_key()
	"""
	return keys.PrivateKey(arr)

if __name__ == "__main__":
	base_path = sys.argv[1]
	secret_num = 20
	recover_num = 10
	if (len(sys.argv)>3):
		secret_num=int(sys.argv[2])
		recover_num=int(sys.argv[3])
	secret_num = secret_num + 1
	recover_num = recover_num + 1
	fingerRandom_file = base_path + '/generate/fingerprint/fuzzyRandom.txt'
	hash_fingerRandom_file = base_path + '/generate/fingerprint/hash_fuzzyRandom.txt'
	with open(fingerRandom_file,'rb') as f:
		fingerRandom = f.read()
	
	# print(fingerRandom.hex())
	fingerRandom = str(fingerRandom)
	# string='任性的90后boy'
	sha256 = hashlib.sha256()
	sha256.update(fingerRandom.encode('utf-8'))
	res = sha256.hexdigest()
	# print("sha256加密结果:",res)
	with open(hash_fingerRandom_file,'w') as f:
		f.write(res)
	arr = bytes.fromhex(res)

	sk2_file = base_path + '/generate/sk2.txt'
	pk2_file = base_path + '/generate/pk2.txt'

	eth_k = _generate_eth_key()
	
	sk2_hex = eth_k.to_hex()  # hex string
	pk2_hex = eth_k.public_key.to_hex()
	# print(sk2_hex,end='\n')
	# print(pk2_hex)
	with open(sk2_file,'w') as f:
		f.write(sk2_hex)
	with open(pk2_file,'w') as f:
		f.write(pk2_hex)

	salt_path = base_path + '/SecretSharing/enecrypt/salt/'
	hashRandom_path = base_path + '/SecretSharing/enecrypt/hashRandom/'
	# 加密0_m.txt
	salt_file = salt_path + '0_m.txt'
	hashRandom_file = hashRandom_path + '0_m.txt'
	with open(salt_file,'rb') as f:
		m_0 = f.read()
	# print(m_0)
	temp = encrypt(pk2_hex,m_0)
	print('encrypt_m_0: {}'.format(str(temp)))
	with open(hashRandom_file,'wb') as f:
		f.write(temp)
	
	# 加密i_s_m.txt
	s_m=[]
	for i in range(0,secret_num-1):
		salt_file = salt_path + str(i) + '_s_m.txt'
		with open(salt_file,'rb') as f:
			s_m.append(f.read())
		temp = encrypt(pk2_hex,s_m[i])
		hashRandom_file = hashRandom_path + str(i) + '_s_m.txt'
		with open(hashRandom_file,'wb') as f:
			f.write(temp)





