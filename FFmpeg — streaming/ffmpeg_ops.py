"""FFmpeg control helpers"""
import subprocess

def transcode_video(input_path, output_path):
    subprocess.run([
        'ffmpeg', '-i', input_path,
        '-c:v', 'libx264', '-preset', 'fast', output_path
    ])
