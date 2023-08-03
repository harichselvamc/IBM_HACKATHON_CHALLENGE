# ocr.py
import cv2
from PIL import Image
import pytesseract
import time

# Function to perform OCR on an image
def perform_ocr_image(image):
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)

    return text

# Function to perform OCR on camera frames for a specified duration
def perform_ocr_camera(duration=4):
    # Start capturing frames from the webcam
    cap = cv2.VideoCapture(0)

    # Set a timeout based on the specified duration
    timeout = time.time() + duration

    # Perform OCR on the camera frames
    detected_text = ""
    while time.time() < timeout:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        # Convert the frame to a PIL Image
        pil_image = Image.fromarray(frame)

        # Perform OCR on the image
        text = perform_ocr_image(pil_image)

        # Accumulate the detected text
        detected_text += text

    # Release the webcam and close the camera window
    cap.release()
    cv2.destroyAllWindows()

    return detected_text
