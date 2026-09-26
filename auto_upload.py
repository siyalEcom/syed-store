import os
import subprocess
from moviepy.editor import VideoFileClip

print("=== Professional TikTok Automation Pipeline Started ===")

# Yahan apna YouTube video ka link dalein
YOUTUBE_URLS = [
    "https://www.youtube.com/shorts/YOUR_VIDEO_ID_HERE",
]

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
            
            # Raw file delete kar dein taake cloud storage bache
            if os.path.exists(raw_filename):
                os.remove(raw_filename)
                
        except Exception as e:
            print(f"Error processing {url}: {e}")

if __name__ == "__main__":
    process_videos()
    print("=== Pipeline Step Finished Successfully ===")
