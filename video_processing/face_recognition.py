import cv2
import tensorflow as tf
import numpy as np


class Recognizer:
    def __init__(self, threshold=0.2):
        self.model = tf.keras.models.load_model('models/FaceNet.h5')
        self.input_embeddings = None
        self.threshold = threshold

    def face_to_embedding(self, face):
        image = cv2.resize(face, (96, 96))
        img = image[..., ::-1]
        img = np.around(np.transpose(img, (0, 1, 2)) / 255.0, decimals=12)
        x_train = np.array([img])
        embedding = self.model.predict_on_batch(x_train)
        return embedding

    def recognize_face(self, face):
        embedding = self.face_to_embedding(face)
        minimum_distance = 200  # just initiating min variable
        name = None
        # Loop over  names and encodings.
        for (input_name, input_embedding) in self.input_embeddings.items():
            euclidean_distance = np.linalg.norm(embedding - input_embedding)
            if euclidean_distance < minimum_distance:
                minimum_distance = euclidean_distance
                name = input_name

        if minimum_distance < self.threshold:
            return str(name), minimum_distance
        else:
            return "Unknown", minimum_distance  # str(name), minimum_distance

    def verify_faces(self, faces):
        for face in faces:
            face.name, face.distance = self.recognize_face(face.img)
        return
