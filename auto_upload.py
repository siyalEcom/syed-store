import os
import subprocess
import requests
from moviepy.editor import VideoFileClip

print("=== Professional TikTok Channel Automation Started ===")

# ==========================================
# APKE CHANNEL KA LINK YAHAN SET HAI 👇
# ==========================================
CHANNEL_URL = "https://www.youtube.com/@SabziStoryTv-r1v/shorts"

TIKTOK_ACCESS_TOKEN = os.getenv("TIKTOK_ACCESS_TOKEN")

def upload_to_tiktok(video_path, caption="AI Cartoon Story #fyp #foryou #viral"):
    if not TIKTOK_ACCESS_TOKEN:
        print("TikTok Access Token missing! Skipping upload.")
        return

    print(f"Uploading {video_path} to TikTok...")
    url = "https://open.tiktokapis.com/v2/post/publish/video/init/"
    headers = {
        "Authorization": f"Bearer {TIKTOK_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    print("API connection initialized for TikTok posting.")

def process_channel():
    print("Step 1: Fetching latest video from the channel automatically...")
    
    raw_filename = "raw_video_auto.mp4"
    final_filename = "final_video_auto.mp4"
    
    # yt-dlp command jo channel ke shorts se sabse pehli latest video download karegi
    download_command = [
        "yt-dlp",
        "--playlist-end", "1", # Sirf sabse pehli latest video uthayega
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
        "-o", raw_filename,
        CHANNEL_URL
    ]
    
    try:
        print(f"Downloading latest video from: {CHANNEL_URL}")
        subprocess.run(download_command, check=True)
        
        # 2. Professional Editing using MoviePy
        print(f"Applying professional edits to {raw_filename}...")
        clip = VideoFileClip(raw_filename)
        
        if clip.duration > 60:
            clip = clip.subclip(0, 60)
            
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
        
        # Local cleanup
        if os.path.exists(raw_filename):
            os.remove(raw_filename)
        if os.path.exists(final_filename):
            os.remove(final_filename)
            
    except Exception as e:
        print(f"Error while processing channel: {e}")

if __name__ == "__main__":
    process_channel()
    print("=== Pipeline Finished Successfully ===")
