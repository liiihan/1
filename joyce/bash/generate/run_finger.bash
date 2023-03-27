
base_path=$1
image_name=$2

# 生成私钥和公钥 in /root/result/publicKey.txt  /root/result/privateKey.txt
# cd /root/fingerprint/py_secp256k1/bash
# python getPri.py $base_path

# 对指纹图像进行增强 原始图像位于/root/result/image/origin 增强后图像位于/root/result/image/enhanced
cd /root/fingerprint/Fingerprint-Enhancement-Python
python main.py $base_path $image_name

# 对增强后指纹图像进行特征提取-提取特征中心-计算特征距离-生成特征描述子-生成fuzzyRandom和fuzzyPublic
# 1.征提取后图像位于/root/result/image/extracted
# 2.特征描述子位于/root/result/image/extracted/descriptor.txt 和 /root/result/image/extracted/changed_descriptor.txt
# 3.生成fuzzyRandom位于/root/result/fuzzyRandom.txt
# 4.生成fuzzyPublic位于/root/result/fuzzyPublic/fuzzyCiphers.txt  fuzzyMasks.txt  fuzzyNonces.txt
cd /root/fingerprint/Fingerprint-Feature-Extraction
python generateRP.py $base_path $image_name


# # 新的图像进来
# changed_image_name=changed_${image_name}
# cd /root/fingerprint/Fingerprint-Enhancement-Python
# python main.py $base_path $changed_image_name

# # 由改变后的指纹图提取b` , 由之前保存的fuzzyPublic/fuzzyCiphers.txt  fuzzyMasks.txt  fuzzyNonces.txt
# # 共同生成新的fuzzyRandom R` in /root/result/new_fuzzyRandom.txt
# cd /root/fingerprint/Fingerprint-Feature-Extraction
# python recoverR_from_Pb.py $base_path $changed_image_name