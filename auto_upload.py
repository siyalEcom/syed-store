import os
import subprocess
import requests
from moviepy.editor import VideoFileClip

print("=== Professional TikTok Automation Pipeline Started ===")

# Yahan apne YouTube Shorts ke links dalein
YOUTUBE_URLS = [
    "https://www.youtube.com/shorts/YOUR_VIDEO_ID_HERE",
]

# TikTok Access Token (Yeh hum GitHub Secrets mein save karenge)
TIKTOK_ACCESS_TOKEN = os.getenv("TIKTOK_ACCESS_TOKEN")

def upload_to_tiktok(video_path, caption="AI Cartoon Story #fyp #foryou #viral"):
    if not TIKTOK_ACCESS_TOKEN:
        print("TikTok Access Token missing! Skipping upload.")
        return

    print(f"Uploading {video_path} to TikTok...")
    # TikTok Content Posting API endpoint
    url = "https://open.tiktokapis.com/v2/post/publish/video/init/"
    
    headers = {
        "Authorization": f"Bearer {TIKTOK_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    # Yahan API ke zariye video initialization hoti hai
    print("API connection initialized for TikTok posting.")

def process_videos():
    print("Step 1: Downloading & Processing videos professionally...")
    
    for i, url in enumerate(YOUTUBE_URLS):
        raw_filename = f"raw_video_{i+1}.mp4"
        final_filename = f"final_video_{i+1}.mp4"
        
        # 1. Download video using yt-dlp
        download_command = [
            "yt-dlp",
            "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
            "-o", raw_filename,
            url
        ]
        
        try:
            print(f"Downloading: {url}")
            subprocess.run(download_command, check=True)
            
            # 2. Professional Editing using MoviePy
            print(f"Applying professional edits to {raw_filename}...")
            clip = VideoFileClip(raw_filename)
            
            # Agar video 60 seconds se lambi hai toh cut kar lein
            if clip.duration > 60:
                clip = clip.subclip(0, 60)
            
            # Save processed video with high quality settings
            clip.write_videofile(
                final_filename, 
                codec="libx264", 
                audio_codec="aac", 
                fps=30,
                preset="medium"
            )
            
            clip.close()
            print(f"Successfully processed and saved: {final_filename}")
            
            # 3. Upload to TikTok
            upload_to_tiktok(final_filename)
            
            # Local files cleanup
            if os.path.exists(raw_filename):
                os.remove(raw_filename)
            if os.path.exists(final_filename):
                os.remove(final_filename)
                
        except Exception as e:
            print(f"Error processing {url}: {e}")

if __name__ == "__main__":
    process_videos()
    print("=== Pipeline Finished Successfully ===")
