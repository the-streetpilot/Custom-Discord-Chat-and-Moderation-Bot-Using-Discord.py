# Discord Bot

## Overview

it is a Discord bot designed to assist with managing a Discord server. It includes features such as announcements, rule postings, social media links, and moderation commands. This README file will guide you through setting up and using the bot.

## Prerequisites

Before you start, make sure you have the following:

- A Discord account
- A Discord server where you have administrative privileges
- Python 3.8 or higher installed on your machine
- The `discord.py` library installed (`pip install discord.py`)

## Setting Up the Bot

### Step 1: Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on "New Application" and give your bot a name.
3. Navigate to the "Bot" tab and click "Add Bot".
4. Copy the bot token. You'll need this to run your bot.

### Step 2: Invite the Bot to Your Server

1. Go to the "OAuth2" tab and then the "URL Generator" sub-tab.
2. Select `bot` in the "Scopes" section.
3. In "Bot Permissions", select the necessary permissions (e.g., `Send Messages`, `Manage Messages`, `Kick Members`, `Ban Members`).
4. Copy the generated URL and open it in your browser.
5. Select the server you want to add the bot to and authorize it.

### Step 3: Set Up Your Project

1. Create a new directory for your project and navigate to it.
2. Create a new Python file (e.g., `bot.py`).
3. Install the `discord.py` library if you haven't already:

```bash
pip install discord.py
```

4. Copy the provided code into your `bot.py` file.

### Step 4: Configure the Bot

Replace the placeholders in the code with appropriate values:

- `PLACE_LOGO_URL_HERE`: URL for the logo image.
- `PLACE_HUSKY_LOGO_URL_HERE`: URL for the Husky logo image.
- `PLACE_GIF_URL_HERE`: URL for the GIF to be displayed in announcements.
- `PLACE_YOUTUBE_CHANNEL_URL_HERE`: URL for your YouTube channel.
- `PLACE_INSTAGRAM_PROFILE_URL_HERE`: URL for your Instagram profile.
- `PLACE_DISCORD_INVITE_URL_HERE`: URL for your Discord invite link.
- `PLACE_WHATSAPP_GROUP_URL_HERE`: URL for your WhatsApp group link.
- `PLACE_WELCOME_IMAGE_URL_HERE`: URL for the welcome image.

### Step 5: Run the Bot

Replace `YOUR_BOT_TOKEN` in the code with your actual bot token. Then, run the bot:

```bash
python bot.py
```

## Bot Commands

### General Commands

- `n.announce <message>`: Make an announcement.
- `n.say <message>`: Make the bot say something.
- `n.rules <message>`: Set the server rules.
- `n.yt`: Get the YouTube channel link.
- `n.ig`: Get the Instagram profile link.
- `n.dcinvite`: Get the Discord invite link.
- `n.whatsapp`: Get the WhatsApp group link.
- `n.live <message>`: Announce that the user is live.
- `n.reply <user> <message>`: Reply to a user's DM.
- `n.dm <user> <message>`: Send a direct message to a user.
- `n.warn <user> <message>`: Warn a user.
- `n.help`: Display the help information.

### Moderation Commands

- `n.mute <user>`: Mute a user.
- `n.unmute <user>`: Unmute a user.
- `n.kick <user> <reason>`: Kick a user.
- `n.ban <user> <reason>`: Ban a user.

### Event Handlers

- `on_ready()`: Event triggered when the bot is ready.
- `on_member_join(member)`: Event triggered when a new member joins the server.

## Customizing the Bot

### Changing the Bot's Status

The bot's status message can be customized by modifying the `status` variable. By default, it is set to 'WATCHING WITCH S LOCUS - Created by HuskY Op'.

### Adding New Commands

To add new commands, use the `@bot.command()` decorator. For example:

```python
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')
```

## Troubleshooting

- Ensure you have the correct bot token.
- Make sure the bot has the necessary permissions on your server.
- Check that you have installed all required dependencies.

## Conclusion

Discord Bot provides a variety of useful commands to manage your Discord server efficiently. Follow this guide to set up and customize the bot according to your needs. For further customization, refer to the `discord.py` documentation. Happy managing!
