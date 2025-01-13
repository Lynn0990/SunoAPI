from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware

import schemas
from deps import get_token
from utils import (
    generate_lyrics,
    generate_music_with_prompt,
    generate_music_with_lyrics,
    get_feed_by_clip_id,
    get_lyrics,
    concat_music,
)


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get_root():
    return schemas.Response()


@app.post("/generate")
async def generate(
    data: schemas.CustomModeGenerateParam, token: str = Depends(get_token)
):
    try:
        resp = await generate_music_with_lyrics(data.dict(), token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@app.post("/generate/description-mode")
async def generate_with_song_description(
    data: schemas.DescriptionModeGenerateParam, token: str = Depends(get_token)
):
    try:
        resp = await generate_music_with_prompt(data.dict(), token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@app.get("/feed/{aid}")
async def fetch_feed(aid: str, token: str = Depends(get_token)):
    try:
        resp = await get_feed_by_clip_id(aid, token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@app.post("/generate/lyrics/")
async def generate_lyrics_post(
    data: schemas.GenerateLyricsParam, token: str = Depends(get_token)
):
    try:
        resp = await generate_lyrics(data.prompt, token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@app.get("/lyrics/{lid}")
async def fetch_lyrics(lid: str, token: str = Depends(get_token)):
    try:
        resp = await get_lyrics(lid, token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@app.post("/generate/concat")
async def concat(data: schemas.ConcatParam, token: str = Depends(get_token)):
    try:
        resp = await concat_music(data.dict(), token)
        return resp
    except Exception as e:
        raise HTTPException(
            detail=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
