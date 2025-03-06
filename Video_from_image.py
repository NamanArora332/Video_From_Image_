import os

from PIL import Image, ImageDraw, ImageFont

def process_image(input_path, output_path, text):
    # Process an image with basic transformation and text overlay
    try:
        # Load image
        img = Image.open(input_path).convert("RGB")

        # Basic transformation : grayscale
        img = img.convert("L").convert("RGB")

        
        # Add Text
        draw = ImageDraw.Draw(img)
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            font = ImageFont.load_default()

        draw.text((50, 50), text, font=font, fill=(255, 255, 255))

        # Save result
        img.save(output_path)
        print(f"Image processed and saved to {output_path}")

    except Exception as e:
        print(f"Error processing image: {e}")

def main():
    input_image = "images/input.png"
    if not os.path.exists(input_image):
        print(f"Input image {input_image} not found!")
        return
    
    process_image(input_image, "images/output.png", "Test Text")

if __name__ == "__main__":
    main()
