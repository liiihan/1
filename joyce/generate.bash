cd /root/bash/generate
bash run_face.bash /root/result/ obama

bash run_finger.bash /root/result/ 01.bmp

cd /root/minimalist_lwe/
python minimalist_lwe.py /root/result/

cd /root/bash/generate/SecretSharing
python secret_sharing_test.py /root/result/

cd /root/bash/generate/salt/
python salt_encrypt.py /root/result/

source ~/.bashrc
conda activate secp256k1
cd /root/bash/generate
python hash_encrypt.py /root/result/
conda deactivate