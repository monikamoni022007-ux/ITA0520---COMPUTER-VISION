
import cv2
import easyocr

# Create OCR reader
reader = easyocr.Reader(['en'], gpu=False)

# Open video
cap = cv2.VideoCapture("D:\\github\\Computer-vision\\Exp40_input.mp4")

if not cap.isOpened():
    print("Video not found. Check the file name and location.")

else:
    frame_number = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Process one frame every 20 frames
        if frame_number % 20 == 0:

            # Convert frame to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Extract text using EasyOCR
            results = reader.readtext(gray)

            # Display detected text
            for detection in results:
                text = detection[1]
                confidence = detection[2]

                if confidence > 0.3:
                    print("Detected Text:", text)

        frame_number += 1

    cap.release()

    print("Text extraction completed.")
