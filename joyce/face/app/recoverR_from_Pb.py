import sys
sys.path.insert(0, '/home/joyce/face/face_recognition/face_recognition')
import face_recognition
sys.path.insert(0, '/root/fingerprint/python-fuzzy-extractor/fuzzy_extractor')
from __init__ import FuzzyExtractor
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

def getPointImage(face_landmarks_list, contorl_point, base_path, input_name):
    _face_KeyPoint = []
    point_img = base_path + '/' + input_name + '_point.jpg'
    for face_landmarks in face_landmarks_list:
        for facial_feature in face_landmarks.keys():
            # print("{}: {}".format(facial_feature, len(face_landmarks[facial_feature])))
            for i in face_landmarks[facial_feature]:
                # print(i, end='\n')
                _face_KeyPoint.append(i)
        
    blue = np.array(["blue"])
    red = np.array(["red"])
    plt.figure('Draw')
    for point in _face_KeyPoint:
        plt.scatter(point[1], point[0],c=blue)
    
    plt.scatter(contorl_point[0][1], contorl_point[0][0],c=red)
    plt.scatter(contorl_point[1][1], contorl_point[1][0],c=red)
    plt.scatter(contorl_point[2][1], contorl_point[2][0],c=red)
    # plt.draw()
    # plt.pause(10)
    plt.savefig(point_img)
    plt.close()

def getMiddlePoint(face_KeyPoint, temp):
    # contorl_point = np.zeros((3,2))

    # for point in face_KeyPoint:
    #     # print(point[0], end='\n')
    #     points = np.array([point[0], point[1]])
    #     contorl_point[0] = contorl_point[0] + points
    # contorl_point[0] = contorl_point[0] / len(face_KeyPoint)

    i = 0
    matrix_A = np.zeros((len(face_KeyPoint),2))
    for point in face_KeyPoint:
        points = np.array([point[0], point[1]])
        points = points - temp[0]
        matrix_A[i] = points
        i = i + 1
    # _matrix_A = np.transpose(matrix_A)
    # matrix_ATA = np.dot(_matrix_A, matrix_A)
    # eigenvalue, eigenvector = np.linalg.eig(matrix_ATA)
    
    # contorl_point[1] = contorl_point[0] + np.sqrt(eigenvalue[0]) * eigenvector[0]
    # contorl_point[2] = contorl_point[0] + np.sqrt(eigenvalue[1]) * eigenvector[1]
    # test = contorl_point
    # print(test)
    # contorl_point = np.transpose(contorl_point)
    # _contorl_point = np.ones((3,3))
    # _contorl_point[0] = contorl_point[0]
    # _contorl_point[1] = contorl_point[1]

    temp = np.transpose(temp)
    _temp = np.ones((3,3))
    _temp[0] = temp[0]
    _temp[1] = temp[1]

    Weighting_factor = np.zeros((len(face_KeyPoint), 3))
    i = 0
    for point in face_KeyPoint:
        points = np.array([point[0], point[1], 1.])
        points = np.transpose(points)
        Weighting_factor[i] = np.linalg.solve(_temp, points) * 10
        # print(np.linalg.solve(_contorl_point, points))
        i = i + 1
    # Weighting_factor    

    return Weighting_factor


if __name__ == "__main__":

    base_path = sys.argv[1]
    input_name = sys.argv[2]
    image_name = base_path + '/recover/face/outIMG/' + input_name + '.jpg'

    image = face_recognition.load_image_file(image_name)

    face_KeyPoint = []
    face_landmarks_list = face_recognition.face_landmarks(image)


    k = 0
    for face_landmarks in face_landmarks_list:
        for i in face_landmarks['chin']:
            if k <= 6:
                k = k + 1
                continue
            face_KeyPoint.append(i)        
        for i in face_landmarks['left_eyebrow']:
            face_KeyPoint.append(i)
        for i in face_landmarks['right_eyebrow']:
            face_KeyPoint.append(i)
        for i in face_landmarks['nose_bridge']:
            face_KeyPoint.append(i)    

    contorl_point = np.zeros((3,2))
    contorl_point[0] = face_landmarks['left_eyebrow'][2]
    contorl_point[1] = face_landmarks['right_eyebrow'][2]
    contorl_point[2] = face_landmarks['nose_bridge'][3]
    # print(contorl_point)

    getPointImage(face_landmarks_list, contorl_point, base_path, input_name)
    Weighting_factor = getMiddlePoint(face_KeyPoint, contorl_point)
    # print(Weighting_factor)

    Binary_descriptor = []
    for i in Weighting_factor:
        temp = np.linalg.norm(i)
        Binary_descriptor.append("{0:05b}".format(int(round(temp))))
    # print(Binary_descriptor)
    Hex_Distance = ''
    for i in Binary_descriptor:
        Hex_Distance = Hex_Distance + str(i)
    add_zero = 128 - len(Hex_Distance)
    if add_zero > 0:
        for i in range(0,add_zero):
            Hex_Distance = Hex_Distance + '0'

    # print(Hex_Distance)
    arr = bytes(int(Hex_Distance[i : i + 8], 2) for i in range(0, len(Hex_Distance), 8))
    extractor = FuzzyExtractor(16, 8)



    new_Ciphers = np.loadtxt(base_path + '/SecretSharing/fuzzyPublic/face/fuzzyCiphers.txt', dtype=np.uint8,delimiter=' ')
    new_Masks = np.loadtxt(base_path + '/SecretSharing/fuzzyPublic/face/fuzzyMasks.txt', dtype=np.uint8,delimiter=' ')
    new_Nonces = np.loadtxt(base_path + '/SecretSharing/fuzzyPublic/face/fuzzyNonces.txt', dtype=np.uint8,delimiter=' ')
    new_fuzzyPublic = (new_Ciphers, new_Masks, new_Nonces)
    new_fuzzyRandom = extractor.reproduce(arr, new_fuzzyPublic)
    with open(base_path + '/recover/face/new_descriptor.txt', 'w') as fo:
        fo.write(Hex_Distance)
    with open(base_path + '/recover/face/new_fuzzyRandom.txt', 'wb') as fo:
        fo.write(new_fuzzyRandom)
    print('face_Random1_: {}'.format(str(new_fuzzyRandom)))