import cv2
import os
import time
from datetime import datetime

# Open the video capture object
cap = cv2.VideoCapture(0)

# Create a folder to store images
os.makedirs("images", exist_ok=True)

# Variable to keep track of the time
start_time = time.time()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Apply a pencil sketch effect using cv2.stylization
    stylized = cv2.stylization(frame, sigma_s=150, sigma_r=0.25)

    # Get current time and date
    current_datetime = datetime.now()
    formatted_time = current_datetime.strftime("%H:%M:%S")
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    day_name = current_datetime.strftime("%A")

    # Add first line of text to the frame (bold, blue)
    first_line_text = f"Time: {formatted_time} | Date: {formatted_date} | Day: {day_name}"
    cv2.putText(stylized, first_line_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2, cv2.LINE_AA)

    # Add second line of text to the frame (bold, blue)
    second_line_text = "Created by Ahmed Alzeidi, Software Engineering"
    cv2.putText(stylized, second_line_text, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1, cv2.LINE_AA)

    # Display the stylized frame
    cv2.imshow("Pencil Sketch Frame", stylized)

    # Capture one photo every 10 seconds
    current_time = time.time() - start_time
    if current_time >= 10:
        timestamp = current_datetime.strftime("%Y%m%d_%H%M%S")
        image_filename = f"images/pencil_sketch_frame_{timestamp}.png"
        cv2.imwrite(image_filename, stylized)
        print(f"Image saved: {image_filename}")

        # Reset the start time
        start_time = time.time()

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
