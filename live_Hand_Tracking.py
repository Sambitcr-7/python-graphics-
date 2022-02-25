from _typeshed import HasFileno
import cv2
import mediapipe as mp

mpHands = mp.solutions.hands
Hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    success , img = cap.read()
    converted_image = cv2.cvtColor(img, cv2.COLOR_BG2BGR)
    results = Hands.prcess(converted_image)

    if results.multi_hand_landmarks:
        for hand_in_frame in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, hand_in_frame, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Hand Tracking - AIINDIA", img)

    cv2.waitKey(1)        