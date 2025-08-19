# WisdomBot

WisdomBot is a Discord bot that posts random inspirational quotes on demand. 
Built entirely in Python, it integrates with Discord and uses a local SQLite database for managing quotes.

## Features
 - Responds to /quote commands with a random inspirational quote.
 - Supports easy quote updates via a text file.
 - Always online (not for a while, unfortunately!), thanks to Flask and a cron job to prevent idle shutdowns.

## Tech Stack
 - Discord.py: Handles communication with Discord servers.
 - Flask: Keeps the bot alive using a REST endpoint hosted on Render.
 - SQLite: Stores and retrieves quotes efficiently.
