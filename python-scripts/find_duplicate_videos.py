import os
import cv2
import numpy as np
import ffmpeg
import imagehash
from PIL import Image
from collections import defaultdict
from tqdm import tqdm


def get_video_duration(video_path):
    """ Get the video duration in seconds """
    try:
        probe = ffmpeg.probe(video_path)
        duration = float(probe['format']['duration'])
        return duration
    except Exception as e:
        print(f"\n⚠️ Failed to get duration for {video_path}: {e}")
        return None


def extract_frame(video_path, time_sec=10):
    """
    Extract a frame from the video at a specific timestamp.
    """
    duration = get_video_duration(video_path)
    if duration is None:
        return None

    # Choose a timestamp within the video length
    time_sec = min(1, duration - 0.5)  # ✅ Extract at 1s or 0.5s before end

    try:
        out, err = (
            ffmpeg.input(video_path, ss=time_sec)
            # ✅ Ensure output format is MJPEG
            .output('pipe:', vframes=1, f='mjpeg', strict='-1')
            .run(capture_stdout=True, capture_stderr=True)
        )

        # Debugging: Check if `out` is empty
        if not out or len(out) < 10:
            print("\n🚨 FFmpeg did not return valid image data!\n")
            print(
                f"FFmpeg stderr: {err.decode() if err else 'No additional info'}")
            return None

        # Convert FFmpeg output to an image
        image = np.frombuffer(out, np.uint8)
        frame = cv2.imdecode(image, cv2.IMREAD_GRAYSCALE)

        # Debugging: Check if the frame was successfully decoded
        if frame is None:
            print("\n🚨 OpenCV failed to decode the image from FFmpeg output!\n")
            return None

        return frame

    except ffmpeg.Error as e:
        print(f"\n🚨 FFmpeg failed for: {video_path}")
        print(
            f"🔴 FFmpeg Error Details:\n{e.stderr.decode() if e.stderr else 'No additional error info'}")
        return None
    except Exception as e:
        print(f"\n⚠️ Unexpected error processing {video_path}: {e}")
        return None


def get_video_hash(video_path):
    """
    Generate a perceptual hash (pHash) of the extracted frame.
    """
    frame = extract_frame(video_path)
    if frame is None:
        return None
    image = Image.fromarray(frame)
    return str(imagehash.phash(image))  # Convert to a hash string


def find_duplicate_videos(folder):
    """
    Recursively scan a folder (including subfolders) for duplicate videos based on perceptual hashing.
    """
    video_hashes = defaultdict(list)
    duplicates = []

    # Recursively find all video files
    video_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv')):
                video_files.append(os.path.join(root, file))

    # Process all video files
    for video_path in tqdm(video_files, desc="Scanning Videos"):
        video_hash = get_video_hash(video_path)
        if video_hash:
            video_hashes[video_hash].append(video_path)

    # Identify duplicates
    for hash_val, files in video_hashes.items():
        if len(files) > 1:
            duplicates.append(files)

    return duplicates


# **Run the script**
if __name__ == "__main__":
    folder_path = input('Enter File Path For Detection: ')
    print("Scanning Folder : {}".format(folder_path))
    duplicates = find_duplicate_videos(folder_path)

    if duplicates:
        print("\nDuplicate videos found:")
        for group in duplicates:
            print("\n".join(group))
            print("-" * 50)
    else:
        print("No duplicates found.")
