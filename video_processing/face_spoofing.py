import cv2
import numpy as np
from tensorflow.keras.models import model_from_json

# Load Anti-Spoofing Model graph
json_file = open('models/spoof/antispoofing_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

# load antispoofing model weights
model.load_weights('models/spoof/antispoofing_model.h5')


def spoof_detector(faces):
    for face in faces:
        x, y, w, h = face.bbox[0], face.bbox[1], face.bbox[2], face.bbox[3]
        resized_face = cv2.resize(face.img, (160, 160))
        resized_face = resized_face.astype("float") / 255.0
        resized_face = np.expand_dims(resized_face, axis=0)
        # pass the face ROI through the trained liveness detector
        # model to determine if the face is "real" or "fake"
        preds = model.predict(resized_face)[0]
        face.spoof_score = preds[0]
        if preds > 0.8:
            face.spoof = False
        else:
            face.spoof = True
