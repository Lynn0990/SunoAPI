# Suno Song Generation API Integration Instructions

As the application of AI expands, various AI programs have gradually become popular. AI has deeply penetrated various aspects of people's work and life. Moreover, the industries involved in AI are increasing, from initial writing and medical education to now, music.

Suno is a professional high-quality AI song and music creation platform. Users only need to input simple text prompts to generate songs with vocals according to genre style and lyrics. This AI music generator has been developed by team members from well-known tech companies like Meta, TikTok, and Kensho, aiming to allow everyone to create wonderful music without any musical instruments.

Suno has recently upgraded its music generation model to version V3, capable of generating 2-minute songs.

However, Suno does not officially provide an API. AceDataCloud offers a set of Suno APIs that simulate integration with the official Suno, making it convenient and quick to generate desired music.

## Application and Usage
To use the Suno Audios API, you can first visit the [Suno Audios Generation API](https://platform.acedata.cloud/documents/4da95d9d-7722-4a72-857d-bf6be86036e9?inviter_id=66b756d7-b5ed-40eb-9c0e-dee2c81dbce5 "Suno Audios Generation API") 
page and click the “Acquire” button to obtain the credentials needed for requests:

![](https://cdn.acedata.cloud/nyq0xz.png)

If you are not logged in or registered, you will be automatically redirected to the login page inviting you to register and log in. After logging in or registering, you will automatically return to the current page.

When applying for the first time, you'll receive a free quota, allowing you to use this API for free.

## Basic Usage
To generate songs, you can input any text, for example, if I want to create `a song about Christmas`, I can enter a song for Christmas, as shown in the image:

![](https://cdn.acedata.cloud/tsragd.png)

The generated code is as follows:

![](https://cdn.acedata.cloud/ohgrs3.png)

You can click the “Try” button to test the API directly, and after waiting for 1-2 minutes, the result is as follows:

```json
{
  "success": true,
  "data": [
    {
      "state": "succeeded",
      "id": "2f16f7bc-4135-42c6-b3c5-6d6c49dc8cd5",
      "title": "Winter Wonderland",
      "image_url": "https://cdn1.suno.ai/image_2f16f7bc-4135-42c6-b3c5-6d6c49dc8cd5.png",
      "lyric": "[Verse]\nSnowflakes falling all around\nGlistening white\nCovering the ground\nChildren laughing\nFull of delight\nIn this winter wonderland tonight\nSanta's sleigh\nUp in the sky\nRudolph's nose shining bright\nOh my\nHear the jingle bells\nRinging so clear\nBringing joy and holiday cheer\n[Verse 2]\nRoasting chestnuts by the fire's glow\nChristmas lights\nThey twinkle and show\nFamilies gathering with love and cheer\nSpreading warmth to everyone near",
      "audio_url": "https://cdn1.suno.ai/2f16f7bc-4135-42c6-b3c5-6d6c49dc8cd5.mp3",
      "video_url": "https://cdn1.suno.ai/2f16f7bc-4135-42c6-b3c5-6d6c49dc8cd5.mp4",
      "created_at": "2024-05-10T16:21:37.624Z",
      "model": "chirp-v3",
      "prompt": "A song for Christmas",
      "style": "holiday"
    },
    {
      "state": "succeeded",
      "id": "5dca232b-17cc-4896-a2d1-4b59178bf410",
      "title": "Winter Wonderland",
      "image_url": "https://cdn1.suno.ai/image_5dca232b-17cc-4896-a2d1-4b59178bf410.png",
      "lyric": "[Verse]\nSnowflakes falling all around\nGlistening white\nCovering the ground\nChildren laughing\nFull of delight\nIn this winter wonderland tonight\nSanta's sleigh\nUp in the sky\nRudolph's nose shining bright\nOh my\nHear the jingle bells\nRinging so clear\nBringing joy and holiday cheer\n[Verse 2]\nRoasting chestnuts by the fire's glow\nChristmas lights\nThey twinkle and show\nFamilies gathering with love and cheer\nSpreading warmth to everyone near",
      "audio_url": "https://cdn1.suno.ai/5dca232b-17cc-4896-a2d1-4b59178bf410.mp3",
      "video_url": "https://cdn1.suno.ai/5dca232b-17cc-4896-a2d1-4b59178bf410.mp4",
      "created_at": "2024-05-10T16:21:37.624Z",
      "model": "chirp-v3",
      "prompt": "A song for Christmas",
      "style": "holiday"
    }
  ]
}
```

You can see that we have obtained the contents of two songs at this point, including the title, preview image, lyrics, audio, video, and other content.

The field descriptions are as follows:

- success: Indicates whether the generation was successful; it will be true if successful, otherwise false.
- data: A list containing detailed information about the generated songs.
  - state: The song generation status, primarily includes four types as follows:
    - succeeded: Generation successful
    - pending: In queue
    - running: In process
    - error: Failed
- id: Song ID
- title: Title of the song
- image_url: Cover image of the song
- lyric: Lyrics of the song
- audio_url: Audio file of the song, opening it will play an mp3 audio.
- video_url: Video file of the song, opening it will play an mp4 video.
- created_at: Creation time
- model: The model used, generally the latest v3 model
- style: Style

## Custom Generation
If you want to customize the generation of lyrics, you can input the lyrics:

At this point, the `lyric` field can accept content like:

```
[Verse]\nSnowflakes falling all around\nGlistening white\nCovering the ground\nChildren laughing\nFull of delight\nIn this winter wonderland tonight\nSanta's sleigh\nUp in the sky\nRudolph's nose shining bright\nOh my\nHear the jingle bells\nRinging so clear\nBringing joy and holiday cheer\n[Verse 2]\nRoasting chestnuts by the fire's glow\nChristmas lights\nThey twinkle and show\nFamilies gathering with love and cheer\nSpreading warmth to everyone near
```

>Note that in the lyrics \n is a newline character. If you do not know how to generate lyrics, you can use the lyrics generation API provided by AceDataCloud to generate lyrics via prompt. The API is [Suno Lyrics Generation API](https://platform.acedata.cloud/documents/514d82dc-f7ab-4638-9f21-8b9275916b08 "Suno Lyrics Generation API").

Next, to customize the generation of songs based on lyrics, title, and style, you can specify the following content:

- lyric: Lyric text
- custom: Set to true, indicating custom generation; this parameter defaults to false, indicating use of prompt generation.
- file: Title of the song.
- style: Style of the song, optional.

Fill out a sample like the following:

![](https://cdn.acedata.cloud/quw76r.png)

After filling out, the code is generated automatically as follows:

![](https://cdn.acedata.cloud/d1jv3i.png)

The corresponding code:

```json
curl -X POST 'https://api.acedata.cloud/suno/audios' \
-H 'authorization: Bearer {token}' \
-H 'accept: application/json' \
-H 'content-type: application/json' \
-d '{
"lyric": "[Verse]\\nSnowflakes falling all around\\nGlistening white\\nCovering the ground\\nChildren laughing\\nFull of delight\\nIn this winter wonderland tonight\\nSanta's sleigh\\nUp in the sky\\nRudolph's nose shining bright\\nOh my\\nHear the jingle bells\\nRinging so clear\\nBringing joy and holiday cheer\\n[Verse 2]\\nRoasting chestnuts by the fire's glow\\nChristmas lights\\nThey twinkle and show\\nFamilies gathering with love and cheer\\nSpreading warmth to everyone near",
"custom": true
}'

```

Testing is allowed, and the generated effect is similar.

## Error Handling

If an error occurs, you will receive an error message similar to the following:

```json
{
  "success": false,
  "error": {
    "code": "forbidden",
    "message": "Song Description contained artist name: eminem"
  },
  "trace_id": "9bb7c2f4-3b7b-4965-b50a-f663874b1b6f",
  "task_id": "9bb3a2a6-c438-436d-a9f3-fa466abc077c"
}
```

For more details, please refer to https://surl.id/1uKeq9S17s