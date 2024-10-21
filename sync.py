

import os
import requests
import time
import json

# Replace with your actual API key
api_key = "sk-hKR7GqzCShkE2qta1LRBlq0a820wpJVdLMPiboZpbN2Xeg3x"

# Paths to your video and audio files
video_path = "uploaded_video.mp4"
audio_path = "output.wav"

# API endpoint
api_url = "https://api.gooey.ai/v2/video-bots"

# Headers for authentication
headers = {
    "Authorization": f"bearer {api_key}",
    "Content-Type": "application/json"
}

# Step 1: Create the job and get upload URLs
payload = {
    "bot": "sync-audio-to-video"
}

response = requests.post(api_url, headers=headers, json=payload)

if not response.ok:
    print("Error creating job:", response.status_code, response.text)
    exit()

job_data = response.json()
job_id = job_data.get("id")
upload_urls = job_data.get("upload_urls", {})

if not job_id or not upload_urls:
    print("Error: Job ID or upload URLs not found in response")
    print("Response:", job_data)
    exit()

print("Job created with ID:", job_id)

# Step 2: Upload files using pre-signed URLs
files = {
    "video": ("video.mp4", open(video_path, "rb"), "video/mp4"),
    "audio": ("audio.mp3", open(audio_path, "rb"), "audio/mpeg")
}

for file_type, upload_url in upload_urls.items():
    if file_type in files:
        file_tuple = files[file_type]
        files_dict = {file_type: file_tuple}
        upload_response = requests.put(upload_url, files=files_dict)
        
        if not upload_response.ok:
            print(f"Error uploading {file_type}:", upload_response.status_code, upload_response.text)
            exit()
        
        print(f"{file_type.capitalize()} uploaded successfully")

# Close file handlers
for file in files.values():
    file[1].close()

# Step 3: Check job status and download result
max_attempts = 30
attempt = 0
while attempt < max_attempts:
    status_response = requests.get(f"{api_url}/{job_id}", headers=headers)
    if status_response.ok:
        status_data = status_response.json()
        status = status_data.get("status")
        
        if status == "completed":
            video_url = status_data.get("output", {}).get("video")
            if video_url:
                print("Synced video URL:", video_url)
                
                # Download the synced video
                video_response = requests.get(video_url)
                if video_response.status_code == 200:
                    output_path = os.path.join(os.getcwd(), "synced_video.mp4")
                    with open(output_path, "wb") as f:
                        f.write(video_response.content)
                    print(f"Synced video saved to: {output_path}")
                    break
                else:
                    print("Error downloading video:", video_response.status_code)
                    break
            else:
                print("Video URL not found in the response.")
                break
        elif status == "failed":
            print("Job failed:", status_data.get("error", "Unknown error"))
            break
        else:
            print(f"Job status: {status}. Waiting 10 seconds before checking again...")
            time.sleep(10)
            attempt += 1
    else:
        print("Error checking job status:", status_response.status_code, status_response.text)
        break

if attempt == max_attempts:
    print("Timed out waiting for job to complete")