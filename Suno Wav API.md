# Suno Wav API docking instructions
SUNO allows us to obtain WAV format files of music, and this document explains the integration methods of related APIs.
This API only has one input parameter, which is' audio_id ', which is the official generated song ID.
The 'audio_id' we input here is' ec13e502-d043-4eb2-92ee-e900c6da69d1 '.
```python
import requests
url = " https://api.acedata.cloud/suno/wav "
headers = {
"accept": "application/json",
"authorization": "Bearer aa287fa4cc54401087a9fab3f99630af",
"content-type": "application/json"
}
payload = {
"audio_id": "ec13e502-d043-4eb2-92ee-e900c6da69d1"
}
response = requests.post(url, json=payload, headers=headers)
print(response.text)
```
The results are as follows:
```json
{
"success": true,
"task_id": "19787138-49e9-413a-8611-156c375aa99f",
"trace_id": "ec232cf9-8b75-42df-a8a3-fe6d7d6fd02e",
"data": [
{
"file_url": " https://cdn1.suno.ai/ec13e502-d043-4eb2-92ee-e900c6da69d1.wav "
}
]
}
```
As can be seen` The 'file_url' field of 'data' is the WAV format file of the obtained music, which is a publicly accessible CDN address that supports the MP3 suffix.