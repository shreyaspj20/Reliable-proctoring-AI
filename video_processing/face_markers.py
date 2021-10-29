import cv2
import math
import mediapipe as mp
import numpy as np

mp_face_mesh = mp.solutions.face_mesh


def normalized_to_pixel_coordinates(normalized_x, normalized_y, image_width, image_height):
    """Converts normalized value pair to pixel coordinates."""

    # Checks if the float value is between 0 and 1.
    def is_valid_normalized_value(value: float) -> bool:
        return (value > 0 or math.isclose(0, value)) and (value < 1 or math.isclose(1, value))

    if not (is_valid_normalized_value(normalized_x) and is_valid_normalized_value(normalized_y)):
        return None
    x_px = min(math.floor(normalized_x * image_width), image_width - 1)
    y_px = min(math.floor(normalized_y * image_height), image_height - 1)
    return x_px, y_px


# # Extracting Landmark points
# print(results.multi_face_landmarks[0].landmark[0])
# results.multi_face_landmarks[0].landmark[0].x


def get_landmarks(image, face_landmarks):
    landmarks = []
    image_rows, image_cols, _ = image.shape
    for pt in face_landmarks:
        px = normalized_to_pixel_coordinates(pt.x, pt.y, image_cols, image_rows)
        if px:
            px = px[0], px[1], pt.z
            landmarks.append(px)
    return landmarks


def detect_landmarks(image, faces):  # shouldn't run when multiple faces
    hland = None
    if len(faces) != 1:
        return
    with mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True,
                               min_detection_confidence=0.7,
                               min_tracking_confidence=0.7) as face_mesh:

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image)

        # Draw the face mesh annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                faces[0].landmarks = get_landmarks(image, face_landmarks.landmark)
                hland = np.array([(lm.x, lm.y, lm.z) for lm in face_landmarks.landmark])
    return hland


