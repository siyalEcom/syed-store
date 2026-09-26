import os
import subprocess

print("=== TikTok AI Automation Pipeline Started ===")

# Yahan aap jitne marzi YouTube shorts ya videos ke links daal dein
YOUTUBE_URLS = [
    "https://www.youtube.com/shorts/YOUR_VIDEO_ID_HERE", # Yahan apna link dalein
]

def download_videos():
    print("Step 1: Downloading videos from YouTube...")
    
    for i, url in enumerate(YOUTUBE_URLS):
        output_filename = f"video_{i+1}.mp4"
        
        # yt-dlp command to download best quality mp4
        command = [
            "yt-dlp",
            "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]",
            "-o", output_filename,
            url
        ]
        
        try:
            subprocess.run(command, check=True)
            print(f"Successfully downloaded: {output_filename}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")

if __name__ == "__main__":
    download_videos()
    print("=== Pipeline Step Finished ===")
