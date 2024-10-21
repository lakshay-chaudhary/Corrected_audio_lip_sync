# getcorrection.py

import requests

def correct_transcription(transcribed_text, azure_openai_key, azure_openai_endpoint):
    headers = {
        "Content-Type": "application/json",
        "api-key": azure_openai_key
    }
    
    data = {
        "messages": [
            {"role": "user", "content": f"Correct this transcription: {transcribed_text}"}
        ],
        "max_tokens": 200
    }

    try:
        response = requests.post(azure_openai_endpoint, headers=headers, json=data)

        if response.status_code == 200:
            corrected_text = response.json()["choices"][0]["message"]["content"]
            return corrected_text
        else:
            return f"Failed to correct transcription: {response.status_code} - {response.text}"

    except Exception as e:
        return f"Error occurred while correcting transcription: {str(e)}"
