import cv2
from deepface import DeepFace

def analyze_video(video_file):
    cap = cv2.VideoCapture(video_file.name)
    emotions = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            emotions.append(result[0]['dominant_emotion'])
        except:
            pass

    cap.release()

    if emotions.count("neutral") + emotions.count("happy") > emotions.count("fear"):
        return "Confident"
    else:
        return "Nervous"
