import numpy as np
import cv2

# Load the Haar Cascade for face detection
face_classifier = cv2.CascadeClassifier(r"C:\Users\91807\VSCodeProjects\PythonPractice\10. OPEN CV\haarcascade_frontalface_default.xml")

# Load the image
image = cv2.imread(r"C:\Venkat\Venkat_Photos\08-06-2022_M31_Photos\20211017_085614.jpg")

#print('height , width :',image.shape)

# Check if the image is loaded correctly
if image is None:
    print("Error: Image not found or cannot be loaded!")
    exit()  # Exit if image is not loaded

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#print(gray)

# Detect faces in the image
faces = face_classifier.detectMultiScale(gray, 1.3, 5)

# Check if faces are detected
if len(faces) == 0:
    print("No faces found!")
else:
    # Draw rectangles around the faces
    for (x, y, w, h) in faces:  # (x, y) is the top-left corner, and (w, h) is the width and height of the face
        cv2.rectangle(image, (x, y), (x + w, y + h), (60, 0, 60), 2)

    # Display the output image
    cv2.imshow('Face Detection', image)
    cv2.waitKey(0)  # Wait for a key press to close the window

# Close all OpenCV windows
cv2.destroyAllWindows()