import os
import requests

def azure_text_to_speech(text, output_file):
    subscription_key = "146340bacc11415882f4b81e438f7bae"
    region = "centralindia"  # e.g., "eastus"
    
    # API endpoint
    endpoint = f"https://{region}.tts.speech.microsoft.com/cognitiveservices/v1"

    # Headers for the API call
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "riff-16khz-16bit-mono-pcm",
    }

    # SSML request body with the Indian male voice
    body = f"""
    <speak version='1.0' xml:lang='en-IN'>
        <voice name='en-IN-PrabhatNeural'>
            <prosody rate='0%' pitch='0%'>
                {text}
            </prosody>
        </voice>
    </speak>
    """

    # Making the API request
    response = requests.post(endpoint, headers=headers, data=body)

    # Saving the audio response to a file
    if response.status_code == 200:
        with open(output_file, "wb") as f:
            f.write(response.content)
        print(f"Audio saved as {output_file}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

