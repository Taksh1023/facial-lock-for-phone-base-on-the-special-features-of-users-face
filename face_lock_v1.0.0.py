import cv2
import numpy as np
import face_recognition

# Load a sample image of the user's face
user_image = face_recognition.load_image_file("user.jpg")
user_encoding = face_recognition.face_encodings(user_image)[0]

# Initialize some variables
face_locations = []
face_encodings = []

# Open the webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture a frame from the webcam
    ret, frame = video_capture.read()

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        # Compare the face encoding in the current frame with the user's face encoding
        matches = face_recognition.compare_faces([user_encoding], face_encoding)
        
        if True in matches:
            # If a match is found, it's the user's face
            print("User's face detected. Access granted!")
        else:
            # No match found, face is not recognized
            print("Unknown face detected. Access denied!")

    # Display the resulting frame
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
