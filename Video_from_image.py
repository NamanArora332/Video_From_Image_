import os

from PIL import Image, ImageDraw, ImageFont
import subprocess

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

def create_Video(image_path, output_video , duration = 5):
    # Create a video from an image using FFmpeg
    try:
        ffmpeg_cmd = [
            'ffmpeg',
            '-y',  # Overwrite output
            '-loop', '1',
            '-i', image_path,
            '-c:v', 'libx264',
            '-t', str(duration),
            '-pix_fmt', 'yuv420p',
            output_video
        ]
        subprocess.run(ffmpeg_cmd, check=True, stderr=subprocess.PIPE)
        print(f"Video generated at {output_video}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"FFmpeg error: {e.stderr.decode()}")
        return False







def main():
    input_image = "images/input.png"
    processed_image = "images/output.png"
    output_video = "images/output_video.mp4"
    if not os.path.exists(input_image):
        print(f"Input image {input_image} not found!")
        return
    
    if process_image(input_image, "images/output.png", "Test Text"):
        create_Video(processed_image , output_video)

if __name__ == "__main__":
    main()
