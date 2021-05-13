from typing import Text
import cv2
import face_recognition
from face_recognition.api import face_locations, load_image_file
import numpy as np

def face_list(path,known_faces):
    img = face_recognition.load_image_file(path)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img_encod = face_recognition.face_encodings(img)[0]
    known_faces.append(img_encod)
    return known_faces

def face_recog(path):
    detected_faces = []
    known_faces = []
    known_faces = face_list('images\kedar.jpg',known_faces)
    known_faces = face_list('images\prem1.jpeg',known_faces)
    known_faces = face_list('images\kanishk.jpeg',known_faces)
    known_faces = face_list('images\krutik.jpeg',known_faces)
    known_faces = face_list('images\_vaishnav.jpeg',known_faces)
    known_faces = face_list('images\shubham.jpeg',known_faces)
    known_faces = face_list('images\chirag.jpeg',known_faces)   


    names = ['Kedar', 'Prem','Kanishk','Krutik','Vaishnav','Shubham','Chirag']
    image = face_recognition.load_image_file(path)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    locations = face_recognition.face_locations(image)[0]
    cv2.rectangle(image,(locations[0],locations[3]),(locations[1],locations[2]),(255,0,255),2)
    image_encode = face_recognition.face_encodings(image)
    print(len(image_encode))
    faceLoc = face_recognition.face_locations(image)
    print(len(faceLoc))
    
        
    cv2.imshow('frame',image)
    cv2.waitKey(0)
    for curr_face in image_encode:
        for x in range(0,len(known_faces)):
            match = face_recognition.compare_faces([known_faces[x]],curr_face)
            if match[0] == True:            
                detected_faces.append(names[x])
                break
    return detected_faces
        

print(face_recog('_vaishnav.jpeg'))


