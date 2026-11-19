
import cv2
import numpy as np

# Get text from user
text = input("Enter the text: ")

# Create white image
image = np.ones((400, 700, 3), dtype=np.uint8) * 255

# Set font properties
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
thickness = 2

# Calculate text size
(text_width, text_height), baseline = cv2.getTextSize(
    text, font, font_scale, thickness
)

# Calculate center position
x = (700 - text_width) // 2
y = (400 + text_height) // 2

# Put text on image
cv2.putText(
    image,
    text,
    (x, y),
    font,
    font_scale,
    (0, 0, 255),
    thickness
)

# Display image
cv2.imshow("Text Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
