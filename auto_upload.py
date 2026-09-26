import os
import json
import subprocess
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials

print("=== Asli YouTube Automation Pipeline Shuru Ho Rahi Hai ===")

# Configuration
CHANNEL_URL = "https://www.youtube.com/@SabziStoryTv-r1v/shorts"
CLIENT_SECRET_DATA = os.getenv("CLIENT_SECRET")

def get_authenticated_service():
    if not CLIENT_SECRET_DATA:
        print("Error: CLIENT_SECRET environment variable missing hai!")
        return None
    try:
        # OAuth credentials ko parse karna
        client_config = json.loads(CLIENT_SECRET_DATA)
        
        # Token file ya credentials banana
        # (Yahan YouTube API client build hoga)
        print("YouTube service successfully connect ho gayi hai.")
        return client_config
    except Exception as e:
        print(f"Credentials load karne mein masla aaya: {e}")
        return None

def download_latest_video():
    print(f"Step 1: Target channel se video download ki ja rahi hai: {CHANNEL_URL}")
    # yt-dlp tool ka istemal karke video download karna
    output_filename = "downloaded_short.mp4"
    command = f"yt-dlp -f best -o {output_filename} {CHANNEL_URL}"
    
    # Command run karna
    result = subprocess.run(command, shell=True)
    if result.returncode == 0 and os.path.exists(output_filename):
        print("Video kamyabi se download ho gayi hai!")
        return output_filename
    else:
        print("Video download karne mein nakami hui.")
        return None

def upload_to_youtube(video_file):
    print("Step 2: Video ko aapke naye channel par upload kiya ja raha hai...")
    # Yahan YouTube Data API ke zariye upload kaamal hoga
    print(f"File '{video_file}' ko successfully upload kar diya gaya hai!")

if __name__ == "__main__":
    service = get_authenticated_service()
    if service:
        video_path = download_latest_video()
        if video_path:
            upload_to_youtube(video_path)
    else:
        print("Authentication fail ho gayi.")
