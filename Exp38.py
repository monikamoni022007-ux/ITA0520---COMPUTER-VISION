
import cv2
from mtcnn import MTCNN

# Read input image
image = cv2.imread(
    r"D:\github\Computer-vision\Exp38_input_img.jpeg"
)

if image is None:
    print("Image not found. Check the image path.")

else:
    detector = MTCNN()
    height, width = image.shape[:2]

    # Store detected face boxes
    boxes = []

    # Function to detect faces in an image region
    def detect_region(region, offset_x=0, offset_y=0):
        h, w = region.shape[:2]

        # Enlarge region for better detection
        enlarged = cv2.resize(
            region,
            (w * 2, h * 2),
            interpolation=cv2.INTER_CUBIC
        )

        rgb = cv2.cvtColor(enlarged, cv2.COLOR_BGR2RGB)

        faces = detector.detect_faces(rgb)

        for face in faces:
            x, y, fw, fh = face["box"]

            # Convert coordinates to original image scale
            x = int(x / 2) + offset_x
            y = int(y / 2) + offset_y
            fw = int(fw / 2)
            fh = int(fh / 2)

            x = max(0, x)
            y = max(0, y)

            boxes.append((x, y, fw, fh))

    # Detect faces in the complete image
    detect_region(image)

    # Detect faces separately in the right half
    right_start = width // 2
    right_region = image[:, right_start:]

    detect_region(right_region, right_start, 0)

    # Remove duplicate overlapping detections
    final_boxes = []

    for box in boxes:
        x, y, w, h = box
        duplicate = False

        for existing in final_boxes:
            ex, ey, ew, eh = existing

            ix1 = max(x, ex)
            iy1 = max(y, ey)
            ix2 = min(x + w, ex + ew)
            iy2 = min(y + h, ey + eh)

            intersection = max(0, ix2 - ix1) * max(0, iy2 - iy1)

            area1 = w * h
            area2 = ew * eh
            union = area1 + area2 - intersection

            if union > 0 and intersection / union > 0.3:
                duplicate = True
                break

        if not duplicate:
            final_boxes.append(box)

    # Draw rectangles
    result = image.copy()

    for (x, y, w, h) in final_boxes:
        cv2.rectangle(
            result,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

    # Count detected faces
    print("Number of faces detected:", len(final_boxes))

    # Resize for display
    max_width = 800
    max_height = 600

    scale = min(
        max_width / width,
        max_height / height,
        1
    )

    new_size = (
        int(width * scale),
        int(height * scale)
    )

    original_display = cv2.resize(image, new_size)
    result_display = cv2.resize(result, new_size)

    # Display output
    cv2.imshow("Original Image", original_display)
    cv2.imshow("Faces Detected", result_display)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
