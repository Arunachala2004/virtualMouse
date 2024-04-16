import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils =  mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
              x = int(landmark.x*frame_width)
              y = int(landmark.y*frame_height)

############################for cursor control###################################
                
              if id == 8:
                  cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255, 255))
                  index_x = screen_width/frame_width*x
                  index_y = screen_height/frame_height*y
                  pyautogui.moveTo((x/frame_width)*(screen_width), (y/frame_height)*(screen_height))


                
############################for click function##################################
              if id == 4:
                  cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255, 255))
                  thumb_x = screen_width/frame_width*x
                  thumb_y = screen_height/frame_height*y
                  print('Outside', abs(index_y - thumb_y))
                  if abs(index_y - thumb_y) < 20:
                      print('click')
                      pyautogui.click()
                      pyautogui.sleep(1)

                
                
                
 ############################for Double Click function###################################             
              if id == 12:
                      cv2.circle(img=frame, center=(x,y), radius=10,color=(255,0,255))
                      middle_x = screen_width/frame_width*x
                      middle_y = screen_height/frame_height*y
                      if abs(middle_y - thumb_y) < 20:
                          #print('double click')
                          pyautogui.doubleClick()
                          pyautogui.sleep(1)


############################for Right clicking function###################################                
               if id == 16:
                  cv2.circle(img=frame, center=(x, y), radius=10, color=(247, 217, 63))
                  ring_x = screen_width / frame_width * x
                  ring_y = screen_height / frame_height * y
                  if abs(ring_y - thumb_y) < 20:
                      #print('right click')
                      pyautogui.mouseDown(button = 'right')
                      pyautogui.mouseUp(button='right')
                      pyautogui.sleep(1)

############################for Scroll down function###################################
                
              if id == 20:
                  cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                  little_x = screen_width / frame_width * x
                  little_y = screen_height / frame_height * y
                  if abs(little_y - thumb_y) < 20:
                        #print('scroll')
                        pyautogui.scroll(-100)

    
    
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
