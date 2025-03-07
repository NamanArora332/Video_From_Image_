# Video Generator

## Installation
1. Create virtual environment: `python -m venv venv`
2. Activate: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install Pillow gTTS`
4. Install FFmpeg: https://www.gyan.dev/ffmpeg/builds/

## Usage
1. Prepare `input.png` and `background_music.mp3`
2. Run: `python Video_from_image.py`

## Features
- Grayscale image transformation
- Text overlay
- 5-second video with music, narration, and subtitles
