import cv2
import mediapipe as mp

# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize Webcam
cap = cv2.VideoCapture(0)

def get_finger_status(landmarks):
    """
    Returns a list indicating which fingers are up
    [Thumb, Index, Middle, Ring, Pinky]
    """
    fingers = []

    # Tip landmarks index
    tips = [4, 8, 12, 16, 20]

    # Thumb (check x axis)
    if landmarks[tips[0]].x < landmarks[tips[0] - 1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers (check y axis)
    for tip in tips[1:]:
        if landmarks[tip].y < landmarks[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    gesture = "No Hand"

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Detect finger status
            finger_status = get_finger_status(hand_landmarks.landmark)

            # Simple gesture recognition
            if finger_status == [0, 0, 0, 0, 0]:
                gesture = "Fist ✊"
            elif finger_status == [1, 1, 1, 1, 1]:
                gesture = "Open Hand 🖐"
            elif finger_status == [0, 1, 0, 0, 0]:
                gesture = "Pointing ☝️"
            elif finger_status == [0, 1, 1, 0, 0]:
                gesture = "Peace ✌️"

            # Display gesture
            cv2.putText(img, f'Gesture: {gesture}', (10, 50), 
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Sign Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
