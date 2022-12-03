import cv2
import mediapipe as mp
import time
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose
from datetime import datetime
i=0
y_1=0
s=0
n=0
y_2=0
cap = cv2.VideoCapture(0)
now=datetime.now()
with mp_pose.Pose(
    min_detection_confidence=0.,
    min_tracking_confidence=0.) as pose:
  while cap.isOpened():
    i=i+1
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image)
    # while (not results.pose_landmarks.landmark[0]):
    #   pass
    # Draw the pose annotation on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
        landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
    #print(results.pose_landma0rks.landmark[32])
    time.sleep(0.1)
    y_1_prev=results.pose_landmarks.landmark[0].y
    if(y_1_prev>y_1):
      y_1=y_1_prev
    y_2=results.pose_landmarks.landmark[0].y

    if(len(results.pose_landmarks.landmark)!=33): continue 
    else :
      if (abs(results.pose_landmarks.landmark[0].y-results.pose_landmarks.landmark[28].y)<0.5) or (abs(results.pose_landmarks.landmark[0].y-results.pose_landmarks.landmark[27].y)<0.5) and (abs(results.pose_landmarks.landmark[24].y-results.pose_landmarks.landmark[28].y)<0.5) or (abs(results.pose_landmarks.landmark[0].y-results.pose_landmarks.landmark[27].y)<0.5): 
          if(n==0):
            res='fall position, alert Arm fall'
            then=datetime.now()
            #print(abs(y_1-y_2)/abs(float(now.timestamp())-float(then.timestamp())))
            now=datetime.now()
            col=(0,0,255)
            d=0
            n=1
            s=0
      else:
          if(s==0): 
            res='Normal position'
            # print()
            col=(0, 0, 0)
            s=1
            n=0
      # Flip the image horizontally for a selfie-view display.
    font = cv2.FONT_HERSHEY_SIMPLEX
    image=cv2.resize(image,(1300,700),interpolation = cv2.INTER_AREA)
    image=cv2.flip(image, 1)
    cv2.putText(image,res, (10,50), font, 2, col, 3, cv2.LINE_AA)
    cv2.imshow('MediaPipe Pose', image)

    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
