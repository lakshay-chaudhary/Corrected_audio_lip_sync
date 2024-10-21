from moviepy.editor import VideoFileClip

# Function to extract audio from video
def extract_audio(video_file, output_audio_file):
    # Load the video file
    video = VideoFileClip(video_file)
    
    # Extract the audio
    audio = video.audio
    
    # Write the audio to a file
    audio.write_audiofile(output_audio_file)

# Example usage
video_file = "uploaded_video.mp4"  # Replace with your video file path
output_audio_file = "extracted_audio.wav"  # Output audio file name

extract_audio(video_file, output_audio_file)
print("Audio extracted successfully.")
