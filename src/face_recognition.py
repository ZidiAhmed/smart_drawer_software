import cv2
import dlib
import numpy as np

def cartoonize_image(img, face_rects, shape_predictor):
    img_copy = img.copy()

    for rect in face_rects:
        landmarks = shape_predictor(img, rect)
        points = landmarks_to_np(landmarks)

        mask = np.zeros_like(img)
        cv2.fillPoly(mask, [points[0:17]], (255, 255, 255))
        cv2.fillPoly(mask, [points[48:60]], (255, 255, 255))

        img_copy = cv2.bilateralFilter(img_copy, 9, 300, 300)
        img_copy = cv2.bitwise_and(img_copy, mask)
    
    return img_copy

def landmarks_to_np(landmarks, dtype="int"):
    coords = np.zeros((68, 2), dtype=dtype)
    for i in range(0, 68):
        coords[i] = (landmarks.part(i).x, landmarks.part(i).y)
    return coords
