base_path=$1
input_name=$2

new_img=${input_name}_new
cd /root/face/app

# ## 提取人脸框从 /root/face/result/originIMG/$origin_img.jpg   到/root/face/result/outIMG/$new_img.jpg
# python step-2b_projecting-faces.py  $base_path $origin_img
# echo  ----------------      
# echo 生成Random, public
# echo  ----------------         
# # 提取特征点并转为描述子， 从描述子生成RP
# python getFaceKeyPoint.py $base_path $origin_img


# echo  ----------------     
# echo 从public恢复Random 
# echo  ----------------
# 提取新的人脸框
python recover_step-2b_projecting-faces.py $base_path $new_img         
# 从新的人脸和存储的P获得新的P
python recoverR_from_Pb.py $base_path $new_img
