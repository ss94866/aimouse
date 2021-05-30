import time
import mediapipe as mp
import cv2


hand = mp.solutions.hands
draw = mp.solutions.drawing_utils
mp_hand = hand.Hands(max_num_hands = 1)

class AIMOUSE():
    def __init__(self, image):
        self.image = image
        self.height,self.width,_ = self.image.shape

    def calc_fps(stime,etime):
        etime = time.time()
        fps = 1/(etime - stime)
        stime = etime
        return fps, stime
    
    def pre_process(self):
        self.image = cv2.cvtColor(cv2.flip(self.image, 1), cv2.COLOR_BGR2RGB)
        return self.image

    def tip_reult(self, preprocessed_image):
        result = mp_hand.process(preprocessed_image)
        
        if result.multi_hand_landmarks:
            for hand_landmark in result.multi_hand_landmarks:
                x = hand_landmark.landmark[hand.HandLandmark.INDEX_FINGER_TIP].x * self.width
                y = hand_landmark.landmark[hand.HandLandmark.INDEX_FINGER_TIP].y * self.height
                xm = hand_landmark.landmark[hand.HandLandmark.MIDDLE_FINGER_TIP].x * self.width
                ym = hand_landmark.landmark[hand.HandLandmark.MIDDLE_FINGER_TIP].y * self.height
                return int(x), int(y), int(xm), int(ym)

        return None,None,None,None
    def get_box(self):
        p1x = self.width / 6
        p1y = self.height / 12
        p2x = (5 * self.width) / 6
        p2y = (7 *self.height) / 12
        return int(p1x), int(p1y),int(p2x),int(p2y)

    def get_point(self, x, y, x1, y1, x2, y2):
        w = (x - x1) / (x2 - x1)              
        h = (y - y1) / (y2 - y1)
        return round(w, 2), round(h, 2)

    def dist(self,x,y,xm,ym):
        if x and y and xm and ym is not None:
            distance = (xm - x) ** 2 + (ym - y) ** 2
            return int(distance ** 0.5)
        return None