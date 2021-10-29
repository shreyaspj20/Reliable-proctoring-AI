# Reliable-proctoring-AI

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)
![image](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white)
![image](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=Keras&logoColor=white)
![image](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)


## ✨Abstract

Remote proctoring is the act of invigilating an online exam from any location to clamp down on aberrant behavior or cheating instances to ensure a cheat-free assessment environment. A remotely proctored exam is administered by experienced human proctors, an AI Algorithm, or both to maintain integrity. In this project, we present ways to improve reliability of proctoring by generating plots of each parameter measured during the online evaluation. The project makes use of a webcam📷 and microphone🎙🎙 connected to the PC/Laptop. Real-time video processing is enabled and the user is warned if he/she is suspected of cheating.


## ✨Description

1. Video Processing :
     
     🔶Face detection : I used MediaPipe(open source cross-platform, customizable ML solutions for live and streaming media) for detecting faces in real-time and drawing bbxoes around the detected areas in the image.
     🔶Face markers : We make use of Mediapipe's "facemesh" for tracking eyes, mouth opening detection, and head pose estimation.
     🔶Face orientation : The orienation that the face makes with the assumed axis is noted and orientations are classifed into "Straight","right","left","up" or "down".
     🔶Face Recognition : The face detected from the face detector is compared with the registered faces(will talk about this below) and if an unknown face is detected, the user is suspected to be cheating. We use "Facenet" model for this purpose.
     🔶Face Spoofing : It is used for finding whether the face is real or a photograph/image from a phone. The anti-spoofing system is implemented by using a pre-trained model with its weights. The models used so far, could be found under models folder.
