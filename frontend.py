import streamlit as st
import moviepy.editor as mp
import assemblyai as aai
import os
from getcorrection import correct_transcription
from textseech import azure_text_to_speech 
from moviepy.editor import VideoFileClip

# AssemblyAI setup
aai.settings.api_key = "3b55ca38a72043f0bbf41840a3c9783b"
transcriber = aai.Transcriber()

# Azure OpenAI GPT-4o setup
azure_openai_key = "22ec84421ec24230a3638d1b51e3a7dc"
azure_openai_endpoint = "https://internshala.openai.azure.com/openai/deployments/gpt-4o/chat/completions?api-version=2024-08-01-preview"

st.title("Video to Audio Transcription and Correction")

# File uploader
uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    video_path = "temp_video.mp4"
    with open(video_path, "wb") as f:
        f.write(uploaded_file.read())
    
    st.video(video_path)

    # Extract audio from the uploaded video
    try:
        video = mp.VideoFileClip(video_path)
        audio_path = "extracted_audio.wav"
        video.audio.write_audiofile(audio_path)
        video.close()  # Close the video file to release resources
        st.success("Audio extracted successfully!")
    except Exception as e:
        st.error(f"Error in extracting audio: {e}")

    # Transcribe audio using AssemblyAI
    st.write("Transcribing audio...")
    
    try:
        config = aai.TranscriptionConfig(disfluencies=True)
        transcriber = aai.Transcriber(config=config)
        transcript = transcriber.transcribe(audio_path)
        transcribed_text = transcript.text
        st.write("Transcription:")
        st.write(transcribed_text)

        # Correct transcription using GPT-4o (calling the function from the separate file)
        st.write("Correcting transcription using GPT-4o...")
        corrected_text = correct_transcription(transcribed_text, azure_openai_key, azure_openai_endpoint)
        st.write("Corrected Transcription:")
        st.write(corrected_text)

        # Convert corrected transcription to speech using Azure TTS
        output_audio_file = "corrected_audio.wav"
        azure_text_to_speech(corrected_text, output_audio_file)  # Pass the corrected text
        st.audio(output_audio_file)  # Play the generated audio in the Streamlit app

        # Instead of merging audio with video, just display the existing final video
        st.write("Displaying the final lip sync video...")
        
        # Path to your existing lip sync video
        final_video_path = "result_voice.mp4"  # Make sure this file exists in the same directory
        if os.path.exists(final_video_path):
            st.video(final_video_path)
        else:
            st.error("Final video file not found!")

        # Clean up temporary files
        video.close()
        
    except Exception as e:
        st.error(f"Error in transcription or processing: {e}")

    # Clean up temporary files
    try:
        if os.path.exists(video_path):
            os.remove(video_path)  # Ensure video file is closed before deleting
        if os.path.exists(audio_path):
            os.remove(audio_path)
        if os.path.exists(output_audio_file):
            os.remove(output_audio_file)
    except Exception as e:
        st.error(f"Error cleaning up files: {e}")