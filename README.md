# Discord Music Bot

Self-hosted Discord music bot for YouTube links, searches, and playlists.

**Never commit `.env`.** That file holds your bot token.

## Features

- `/play` — YouTube URL, search, or playlist (`/playlist?list=`)
- Mix links (`list=RD...`) play the single video only
- Queue, skip, pause, resume, stop
- `/nowplaying`, `/volume`, `/shuffle`, `/loop`, `/remove` (dropdown)
- Resolves audio when a track starts so queued songs do not go stale
- Leaves after 30 seconds if the voice channel is empty
- One lookup at a time per server
- Playlists queue titles first (up to 80 tracks)

## Requirements

- Python 3.11+
- FFmpeg on PATH (`ffmpeg -version`)
- A Discord bot token from the [Developer Portal](https://discord.com/developers/applications)

Bot permissions: Connect, Speak, Send Messages, Use Slash Commands, View Channels.
Scopes when inviting: `bot` and `applications.commands`.

## Run on Windows

1. Copy `.env.example` to `.env` and paste your token:
   ```
   DISCORD_TOKEN=your_token_here
   ```
2. Double-click `start.bat`
3. Leave the window open. `Ctrl+C` stops the bot.

## Commands

| Command | Description |
|---|---|
| `/play` | Link, search, or playlist |
| `/skip` `/pause` `/resume` `/stop` | Playback |
| `/queue` | Upcoming tracks |
| `/nowplaying` | Current track |
| `/volume` | 0–150 |
| `/shuffle` | Shuffle queue |
| `/loop` | off / track / queue |
| `/remove` | Pick a queued song to drop |

## If YouTube stops working

```bat
.venv\Scripts\python.exe -m pip install -U yt-dlp
```

Then restart the bot.

## Releases

Use GitHub **Releases** for versioned source zips. Do not attach `.env`.
