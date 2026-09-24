import asyncio
import os
import random
from collections import defaultdict, deque
from urllib.parse import parse_qs, urlparse

import discord
import yt_dlp
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise SystemExit("Missing DISCORD_TOKEN. Copy .env.example to .env and paste your token.")

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

MAX_PLAYLIST_TRACKS = 80
LEAVE_AFTER_SECONDS = 30
LOOKUP_TIMEOUT = 90
