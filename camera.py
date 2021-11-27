import cv2

faceDetector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


class Video(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.relaese()

    def get_frame(self):
        ret, frame = self.video.read()
        faces = faceDetector.detectMultiScale(frame, 1.3, 5)
        for(x, y, w, h) in faces:
            x1, y1 = x+w, y+h
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)

            cv2.line(frame, (x, y), (x+30, y), (0, 0, 255), 12)
            cv2.line(frame, (x, y), (x, y+30), (0, 0, 255), 12)

            cv2.line(frame, (x1, y), (x1-30, y), (0, 0, 255), 12)
            cv2.line(frame, (x1, y), (x1, y+30), (0, 0, 255), 12)

            cv2.line(frame, (x, y1), (x+30, y1), (0, 0, 255), 12)
            cv2.line(frame, (x, y1), (x, y1 - 30), (0, 0, 255), 12)

            cv2.line(frame, (x1, y1), (x1 - 30, y1), (0, 0, 255), 12)
            cv2.line(frame, (x1, y1), (x1, y1 - 30), (0, 0, 255), 12)
        ret, jpg = cv2.imencode('.jpg', frame)
        return jpg.tobytes()


# fungsi camera
# import cv2

# class Video(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#     def __del__(self):
#         self.video.relaese()
#     def get_frame(self):
#         ret,frame = self.video.read()
#         ret,jpg = cv2.imencode('.jpg',frame)
#         return jpg.tobytes()
