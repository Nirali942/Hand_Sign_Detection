# ✋ Hand Sign Detection using OpenCV and MediaPipe

This project uses **OpenCV and **MediaPipe** to perform real-time hand gesture detection through your webcam. 
It recognizes simple hand signs like Fist, Open Hand, Pointing, and Peace sign based on finger position tracking.


## 🚀 Features

- Real-time hand detection using webcam
- Recognizes basic hand gestures:
  - ✊ Fist  
  - 🖐 Open Hand  
  - ☝️ Pointing  
  - ✌️ Peace
- Simple gesture classification based on landmark positions
- 

## 🛠️ Tech Stack

- [Python](https://www.python.org/)
- [OpenCV](https://opencv.org/) – for video capture and image processing
- [MediaPipe](https://developers.google.com/mediapipe) – for hand tracking and landmarks


🧠 How It Works


MediaPipe detects 21 hand landmarks per frame.

The get_finger_status() function analyzes the relative positions of these landmarks.

Based on finger status (up/down), specific gestures are classified and displayed.


📈 Future Improvements


Add support for more hand signs

Train a gesture classification model (ML/DL)

Use gestures for app or IoT control
