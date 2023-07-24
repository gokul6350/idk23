import os
import cv2

# Folder path containing the videos
def editf():
    folder_path = "videos"

  # Load logo
    logo_path = "logo.png"
    logo = cv2.imread(logo_path, cv2.IMREAD_UNCHANGED)

    # Convert logo image to have 3 channels
    if logo.shape[2] == 4:
      logo = logo[:, :, :3]

# Process each video in the folder
    for filename in os.listdir(folder_path):
      if filename.endswith(".mp4"):
        video_path = os.path.join(folder_path, filename)
        print(f'Loding:{filename}')
        # Load video
        cap = cv2.VideoCapture(video_path)

    # Get video dimensions
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

    # Calculate logo position
        logo_width = logo.shape[1]
        logo_height = logo.shape[0]
        logo_x = int((width - logo_width) / 2)  # Centered horizontally
        logo_y = int(height - logo_height - 400)  # 10 pixels above the bottom

    # Create video writer
        output_path = os.path.join(folder_path, "output_" + filename)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
        print(f"done {fourcc}")
    # Process each frame
        while cap.isOpened():
          ret, frame = cap.read()
          if not ret:
            break

      # Add the logo to the frame
          frame[logo_y:logo_y + logo_height, logo_x:logo_x + logo_width] = logo

      # Write the modified frame to the output video
          out.write(frame)

    # Release video capture and writer
        cap.release()
        out.release()
