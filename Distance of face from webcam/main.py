import cv2 
from function import face_data
from function import Distance_finder
from function import FocalLength

previous_distance = 30 

width =14.3 


# To compare the distance we need another image 
img = cv2.imread("pic.jpg")
face_width = face_data(img)
Focal_length = FocalLength(previous_distance, width,face_width)

video = cv2.VideoCapture(0)
while True:
    ret, frame = video.read()
    if ret==True:
        face_width_in_frame = face_data(frame)
        if face_width_in_frame !=0:
            Distance = round(Distance_finder(Focal_length, width,face_width_in_frame),2)
            cv2.putText(frame, "Distance from Camera "+"{}".format(Distance)+"CM", (50,50), cv2.FONT_HERSHEY_COMPLEX,1, (123,246,123),3)
        cv2.imshow("frame", frame )
        if cv2.waitKey(1)==ord("q"):
            break 
video.release()
cv2.destroyAllWindows()
