```bash
docker import  biometric_blockchain.tar hipforth/rgbd_map:blockchain
docker run -it --rm -v /home/joyce:/root/ hipforth/rgbd_map:blockchain bash
```
chin
left_eyebrow
right_eyebrow
nose_bridge
nose_tip
left_eye
right_eye
top_lip
bottom_lip

下巴
左眉
右眉
鼻桥
<!-- 鼻尖 -->

<!-- 左眼 -->
<!-- 右眼 -->

<!-- 上唇 -->
<!-- 下唇      -->


## 生成过程
1. 人脸识别-普适描述子计算-模糊提取-R1 P1 ： 输出R1
2. 指纹识别-普适描述子计算-模糊提取-R2 P2 ： 输出R2
3. LWE生成公私钥对(sk1,pk1) : 输出 sk1
4. 私钥切片-中国剩余定理 : 输出m_0
5. 用人脸R1对切片加盐-RNCryptor : 输出加盐m_0
6. 用指纹R2-sha256-公私钥对(sk2,pk2)，对切片加密 ： 输出加密m_0
7. 把切片数据发送到以太网节点
```bash
cd /root/bash/generate
bash run_face.bash /root/result/ obama

bash run_finger.bash /root/result/ 01.bmp

cd /root/minimalist_lwe/
python minimalist_lwe.py /root/result/

cd /root/bash/generate/SecretSharing
python secret_sharing_test.py /root/result/

cd /root/bash/generate/salt/
python salt_encrypt.py /root/result/

conda activate secp256k1
cd /root/bash/generate
python hash_encrypt.py /root/result/
conda deactivate
```



## 恢复过程
1. **新的**人脸识别-普适描述子 + P1 生成 R1' ： 输出R1'
2. **新的**指纹识别-普适描述子 + P2 生成 R2' ： 输出R2'
3. 从以太网节点得到最小切片数量
4. **新的**指纹R2'(sha256)生成公私钥对(sk2',pk2'),对切片解密 : 输出加盐m_0
5. 人脸R1'对切片去盐-RNCryptor : 输出m_0
6. 基于最小切片数量生成sk1-中国剩余定理 ： 输出sk1
```bash
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
```