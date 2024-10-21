from moviepy.editor import VideoFileClip, AudioFileClip

# Load your video file
video_path = "result_voice.mp4"
audio_path = "output.wav"

# Create VideoFileClip object
video_clip = VideoFileClip(video_path)

# Create AudioFileClip object
audio_clip = AudioFileClip(audio_path)

# Set the audio of the video clip
video_with_audio = video_clip.set_audio(audio_clip)

# Write the result to a file
output_path = "finalvideo.mp4"
video_with_audio.write_videofile(output_path, codec='libx264', audio_codec='aac')

# Close the clips to free resources
video_clip.close()
audio_clip.close()
