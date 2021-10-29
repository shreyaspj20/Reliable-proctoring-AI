from scipy.spatial import distance as dist
import numpy as np


class Mouth:
    def __init__(self):
        self.mar = None
        self.status = None


def mouth_aspect_ratio(landmarks):
    A = dist.euclidean(landmarks[37, :], landmarks[84, :])  # 51, 59 # media(37,84)
    B = dist.euclidean(landmarks[267, :], landmarks[314, :])  # 53, 57 # media(267,314)
    C = dist.euclidean(landmarks[61, :], landmarks[291, :])  # 49, 55 #media(61,291)
    mar = (A + B) / (2.0 * C)
    return mar


MOUTH_AR_THRESH = 0.6


# (mStart, mEnd) = (49, 68)

def mouth_open(frame, faces):
    landmarks = np.array(faces[0].landmarks)[:, :2]
    outer_bottom = [61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291]
    outer_top = [61, 185, 40, 39, 37, 0, 267, 269, 270, 409, 291]
    inner_bottom = [78, 95, 88, 178, 87, 14, 317, 402, 318, 324, 308]
    inner_top = [78, 191, 80, 81, 82, 13, 312, 311, 310, 415, 308]

    mouth_obj = Mouth()
    mouth = landmarks[outer_bottom.extend(inner_top), :]
    mouthMAR = mouth_aspect_ratio(landmarks)
    mar = mouthMAR
    mouth_obj.mar = mar

    if mar >= MOUTH_AR_THRESH:
        mouth_obj.status = "mouth open"
    elif mar < MOUTH_AR_THRESH:
        mouth_obj.status = "mouth close"

    return mouth_obj
