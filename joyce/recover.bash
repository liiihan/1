cd /root/bash/recover
bash run_face.bash /root/result obama

cd /root/bash/recover
bash run_finger.bash /root/result 01.bmp

source ~/.bashrc
conda activate secp256k1
cd /root/bash/recover
python hash_decrypt.py /root/result/
conda deactivate

cd /root/bash/recover
python salt_decrypt.py /root/result/

cd /root/bash/recover
python secret_recover.py /root/result/