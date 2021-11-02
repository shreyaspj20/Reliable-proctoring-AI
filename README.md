# Reliable-proctoring-AI 👨‍💻📲📷🎤

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)
![image](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=TensorFlow&logoColor=white)
![image](https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=Keras&logoColor=white)
![image](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

## ✨Authors
Shreyas P J (github handle: shreyaspj20)

## ✨Abstract

Remote proctoring is the act of invigilating an online exam from any location to clamp down on aberrant behavior or cheating instances to ensure a cheat-free assessment environment. A remotely proctored exam is administered by experienced human proctors, an AI Algorithm, or both to maintain integrity. In this project, we present ways to improve reliability of proctoring by generating plots of each parameter measured during the online evaluation. The project makes use of a webcam📷 and microphone🎙🎙 connected to the PC/Laptop. Real-time video processing is enabled and the user is warned if he/she is suspected of cheating.


## ✨Description


### ❄Video Processing.
     
   1. **🎯Face detection** : 
   I used MediaPipe(open source cross-platform, customizable ML solutions for live and streaming media) for detecting faces in real-time and drawing bboxes around the detected areas in the image.

   2. **🎯Face markers** :
   We make use of Mediapipe's "facemesh" for tracking eyes, mouth opening detection, and head pose estimation.

   3. **🎯Face orientation** : 
   The orienation that the face makes with the assumed axis is noted and orientations are classifed into Straight,right,left,up or down.

   4. **🎯Face Recognition** : 
   The face detected from the face detector is compared with the registered faces(will talk about this below) and if an unknown face is detected, the user is suspected to be cheating. We use "Facenet" model for this purpose.

   5. **🎯Face Spoofing** :
   It is used for finding whether the face is real or a photograph/image from a phone. The anti-spoofing system is implemented by using a pre-trained model with its weights. The models used so far, could be found under models folder.






### ❄Audio Processing.

   1. **🎯Oral movements** :
     The software detects whether the user is trying to speak by observing his oral movements. The landmarks detected on the face are used for detecting whether the mouth is open or closed.


   2. **🎯Microphone** :
     I made use of libraries like PyAudio and speech_recognition. Audio from the microphone is recorded and converted to text using Google's speech recognition API. A different thread is used to call the API such that the recording portion is not disturbed a lot, which processes the last one, appends its data to a text file and deletes it. Using NLTK I removed the stopwods from that file. The question paper (in txt format) is taken whose stopwords are also removed and their contents are compared. Finally, the common words along with its number are presented to the proctor to determine whether the user cheated.



## ✨Libraries required.
1. PyAudio
2. SpeechRecognition
3. Mediapipe
4. Pillow
5. nltk
6. Keras API.


## ✨How to use.

💥 Clone the repository onto the local machine.

💥 Setup a virtual environment by installing all required packages as specified in requirements.txt

💥 Replace paper.txt with the required question paper.

💥 Run the file main.py 

💥 Register yourself with 5 captures of images.

💥 Proctoring window would open.

💥 After the end of the exam session, press ESC to close the proctoring window and generate reports which would be stored in proctoring_report folder.

![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)

To watch the whole recording, click on the image below.

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/p9TONa4UeFI/0.jpg)](https://www.youtube.com/watch?v=p9TONa4UeFI)


 ## ✨License
 This project is licensed under the MIT License - see the LICENSE.md file for details. However, the some facial models used is trained on non-commercial use datasets so I am not sure if that is allowed to be used for commercial purposes or not.















