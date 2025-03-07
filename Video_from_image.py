import os

from PIL import Image, ImageDraw, ImageFont
import subprocess
from gtts import gTTS

def process_image(input_path, output_path, text):
    # Process an image with basic transformation and text overlay
    try:
        # Load image
        img = Image.open(input_path).convert("RGB")

        # Basic transformation : grayscale
        img = img.convert("L").convert("RGB")

        
        # Get current dimensions
        width, height = img.size
        
        # Ensure dimensions are even
        width, height = img.size
        if height % 2 != 0:
            height += 1
            img = img.resize((width, height), Image.Resampling.LANCZOS)
        if width % 2 != 0:  # Also ensure width is even, just in case
            width += 1
            img = img.resize((width, height), Image.Resampling.LANCZOS)

        # Add Text
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            font = ImageFont.load_default()

        draw.text((50, 50), text, font=font, fill=(255, 255, 255))

        # Save result
        img.save(output_path)
        return True

    except Exception as e:
        print(f"Error processing image: {e}")
        return False


def generate_narration(text, output_path):
    """Generate narration audio from text"""
    try:
        tts = gTTS(text=text, lang='en')
        tts.save(output_path)
        return True
    except Exception as e:
        print(f"Error generating narration: {e}")
        return False

def create_video(image_path, music_path, narration_path, output_video, duration=5):
    """Create a video with image and audio"""
    try:

        ffmpeg_cmd = [
        'ffmpeg',
        '-y',
        '-loop', '1',
        '-i', image_path,        # Input image
        '-i', music_path,        # Input background music
        '-i', narration_path,    # Input narration audio
        '-filter_complex', '[1:a][2:a]amix=inputs=2:duration=shortest[a]',  # Mix both audio inputs
        '-map', '0:v',           # Map video from the first input (image)
        '-map', '[a]',           # Map the mixed audio
        '-c:v', 'libx264',
        '-t', str(duration),
        '-pix_fmt', 'yuv420p',
        '-c:a', 'aac',
        output_video
]
        subprocess.run(ffmpeg_cmd, check=True, stderr=subprocess.PIPE)
        print(f"Video generated at {output_video}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg error: {e.stderr.decode()}")
        return False


def main():
    input_image = "files/input.png"
    processed_image = "files/output.png"
    music_file = "files/background_music.mp3"
    temp_audio = "files/temp_narration.mp3"
    output_video = "files/output_video.mp4"





    for f in [input_image, music_file]:
        if not os.path.exists(f):
            print(f"Required file {f} not found!")
            return
        
    
    text = "This is a test video. The background music is also playing along with this in the background"
    if process_image(input_image, processed_image, text):
        if generate_narration(text, temp_audio):
            create_video(processed_image, music_file, temp_audio, output_video)

if __name__ == "__main__":
    main()
