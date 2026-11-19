
import cv2

# Open input video
cap = cv2.VideoCapture("D:\\github\\Computer-vision\\Exp39_input_video.mp4")

if not cap.isOpened():
    print("Video not found. Keep the video in the same folder as this Python file.")

else:
    frames = []

    # Read all frames
    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frames.append(frame)

    # Get original FPS
    fps = cap.get(cv2.CAP_PROP_FPS)
    cap.release()

    if len(frames) == 0:
        print("No frames found in the video.")

    else:
        # Reverse frame order
        frames.reverse()

        height, width = frames[0].shape[:2]

        # Half FPS = slow motion
        slow_fps = fps / 2 if fps > 0 else 12

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")

        output = cv2.VideoWriter(
            "reverse_slow_motion.mp4",
            fourcc,
            slow_fps,
            (width, height)
        )

        # Write reversed frames
        for frame in frames:
            output.write(frame)

        output.release()

        print("Reverse slow-motion video created successfully.")
        print("Output file: reverse_slow_motion.mp4")
        print("Total frames:", len(frames))
        print("Output FPS:", slow_fps)
