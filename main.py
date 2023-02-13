import json
from dataclasses import dataclass, field
from typing import Dict, List

from fastapi import FastAPI, HTTPException, Response

app = FastAPI()


@dataclass
class Channel:
    id: str
    name: str
    frequencies: List[int]
    modulation: str = field(default_factory=str)
    tags: List[str] = field(default_factory=List)
    playbackURL: str = ""
    description: str = ""


channels: Dict[str, Channel] = {}

with open("channels.json", encoding="utf8") as file:
    channels_raw = json.load(file)
    for channel_raw in channels_raw:
        channel = Channel(**channel_raw)
        channels[channel.id] = channel


@app.get('/')
def read_root() -> Response:
    return Response("The server is running.")


@app.get('/channels/{channel_id}', response_model=Channel)
def read_item(channel_id: str) -> Channel:
    if channel_id not in channels:
        raise HTTPException(status_code=404, detail="Channel not found")
    return channels[channel_id]


if __name__ == '__main__':
    print('Hello me')
