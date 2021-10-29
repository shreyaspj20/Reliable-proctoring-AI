from video_processing.face_recognition import Recognizer
from video_processing.face_spoofing import spoof_detector
from video_processing.face_markers import detect_landmarks
from video_processing.face_orientation import headpose_est
from audio_and_oral_movements.microphone import recorder
from audio_and_oral_movements.oral_movement import mouth_open
from cheating import *
from results import *
from helper import *

font = cv2.FONT_HERSHEY_SIMPLEX
pTime = [0]

# Face recognizer
fr = Recognizer(threshold=0.8)

# Register User
fr.input_embeddings = register_user(fr, num_pics=5, skipr=False)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('PROCTORING REPORT')
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = print_fps(cv2.flip(frame, 1), pTime)

        faces = detect_faces(frame, confidence=0.7)
        if faces:
            fr.verify_faces(faces)
            spoof_detector(faces)
            if len(faces) == 1:
                hland = detect_landmarks(frame, faces)
                if faces[0].landmarks:
                    faces[0].head = headpose_est(frame, faces, hland)
                    faces[0].mouth = mouth_open(frame, faces)
            frame = print_faces(frame, faces)
        cheat_temp = detect_cheating_frame(faces, frames)
        frames.append(cheat_temp)
        if cheat_temp.cheat > 0:
            cv2.putText(frame, "Please focus on the screen", (15, 105), font, 0.5, (0, 0, 255), 2)
        cv2.imshow('PROCTORING WINDOW', frame)

        recorder()

        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
    plot_main(frames)
    segments = segment_count(frames)
    print_stats(segments)
    plot_segments(segments)

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    file = open("audio_and_oral_movements/test.txt")  # Student speech file
    data = file.read()
    file.close()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(data)  # tokenizing sentence
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = []

    for w in word_tokens:  # Removing stop words
        if w not in stop_words:
            filtered_sentence.append(w)

        # creating a final file
    f = open('audio_and_oral_movements/final.txt', 'w')
    for ele in filtered_sentence:
        f.write(ele + ' ')
    f.close()

    # checking whether proctor needs to be alerted or not
    file = open("audio_and_oral_movements/paper.txt")  # Question file
    data = file.read()
    file.close()
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(data)  # tokenizing sentence
    filtered_questions = [w for w in word_tokens if not w in stop_words]
    filtered_questions = []

    for w in word_tokens:  # Removing stop words
        if w not in stop_words:
            filtered_questions.append(w)


    def common_member(a, b):
        a_set = set(a)
        b_set = set(b)

        # check length
        if len(a_set.intersection(b_set)) > 0:
            return a_set.intersection(b_set)
        else:
            return []


    comm = common_member(filtered_questions, filtered_sentence)
    print('Number of common elements in recorded voice and question paper:', len(comm))
    print(comm)
