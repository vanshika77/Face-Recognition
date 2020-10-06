import glob
import csv
import cv2
import face_recognition
import pandas as pd
from numpy.core.multiarray import ndarray

x_data = []
files=glob.glob("C:/Users/DELL/Desktop/faces/a/*.pgm")

for i in files:
    image: ndarray = face_recognition.load_image_file(i)
    fe = face_recognition.face_encodings(image)
    
    if len(fe) == 0:
        print("no face")
        print(i)
        
    else:
        first_face_encoding = list(fe[0])
        with open('outputnew.csv','a') as f:
            csv_writer = csv.writer(f, delimiter=';')
            csv_writer.writerow(first_face_encoding)