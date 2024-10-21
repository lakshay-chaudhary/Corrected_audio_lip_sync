# Corrected_audio_lip_sync 

Files are present in the master branch of this repo 
# Video Audio Transcription and Correction

This project allows users to upload a video file, extract audio, transcribe it using AssemblyAI, correct the transcription with Azure's GPT-4o, and synthesize the corrected audio back into the video. The Wav2Lip model is used for creating lip-sync videos.

## Features

- Upload a video file.
- Extract audio from the video.
- Transcribe the extracted audio.
- Correct transcription using AI.
- Synthesize corrected audio into the video.
- Display the final video with synced audio.

## Installation

To run this project, follow these steps:

### Prerequisites

Make sure you have Python 3.7 or later installed. You can download Python from [python.org](https://www.python.org/downloads/).

### Clone the Repository

```bash
git clone https://github.com/lakshay-chaudhary/Corrected_audio_lip_sync.git
cd YOUR_REPOSITORY
```
#Create a Virtual Env 
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
#Install Required Packages
```bash
pip install -r requirements.txt
```
#Set Up Environment Variables
Create a .env file in the root of your project directory and add your API keys:
```bash
ASSEMBLYAI_API_KEY=your_assemblyai_api_key
AZURE_OPENAI_KEY=your_azure_openai_key
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
```
#Wav2Lip Installation
To use the Wav2Lip model, follow these steps:

1)Clone the Wav2Lip repository:
```bash
git clone https://github.com/Rudrabha/Wav2Lip.git
```
2)Change directory to Wav2Lip and install required dependencies 
```bash
cd Wav2Lip
pip install -r requirements.txt
```
3)Download the pre-trained model weights (follow the instructions in the Wav2Lip repository).

#Usage
Run the Streamlit application:
```bash
streamlit run frontend.py
Open the provided URL in your web browser to access the application.
```
Upload a video file and follow the instructions to process the audio.

## Acknowledgments
Wav2Lip for lip-sync generation.
AssemblyAI for audio transcription.
Azure OpenAI for text correction and speech synthesis.


