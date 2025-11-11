import whisper
import os
from pathlib import Path

def transcribe_videos():
    model = whisper.load_model("base")
    
    desktop_dir = Path("/Users/jbrelsf2/Desktop")
    
    for video_file in desktop_dir.glob("*"):
        if video_file.suffix.lower() in ['.mp4', '.avi', '.mov', '.mkv', '.webm']:
            output_file = desktop_dir / f"{video_file.stem}.txt"
            
            if output_file.exists():
                print(f"Skipping {video_file.name} - already transcribed")
                continue
                
            print(f"Transcribing: {video_file.name}")
            
            result = model.transcribe(str(video_file))
            
            with open(output_file, "w") as f:
                f.write(result["text"])
            
            print(f"Saved: {output_file.name}")

if __name__ == "__main__":
    transcribe_videos()