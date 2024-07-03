import discord
from discord.ext import commands, tasks
from datetime import datetime

# Configure intents
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

# Bot initialization
bot = commands.Bot(command_prefix="n.", intents=intents)

# URLs for images (replace placeholders with actual URLs)
logo = 'PLACE_LOGO_URL_HERE'
logohusky = 'PLACE_HUSKY_LOGO_URL_HERE'

# Remove default help command
bot.remove_command("help")

@bot.event
async def on_ready():
    """Event triggered when the bot is ready."""
    print("The bot is ready")
    change_status.start()

# Status message to be displayed by the bot
status = 'WATCHING WITCH S LOCUS - Created by HuskY Op'

@tasks.loop(seconds=20)
async def change_status():
    """Task to change the bot's status message periodically."""
    await bot.change_presence(activity=discord.Game(status))

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def announce(ctx, *, message):
    """Command to make an announcement."""
    msg = "**" + message + "**"
    embed = discord.Embed(title="ANNOUNCEMENT", description=msg, color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.set_thumbnail(url=logo)
    url1 = "PLACE_GIF_URL_HERE"
    embed.set_image(url=url1)
    embed.set_footer(icon_url=logohusky, text="Powered by HuskY Op")
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)
    everyone = "@everyone"
    await ctx.send(everyone)

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def say(ctx, *, message):
    """Command to make the bot say something."""
    await ctx.channel.purge(limit=1)
    await ctx.send(message)

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def rules(ctx, *, message):
    """Command to set the server rules."""
    msg = "**" + message + "**"
    embed = discord.Embed(title="DISCORD SERVER RULES", description=msg, color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.set_thumbnail(url=logo)
    url1 = "PLACE_GIF_URL_HERE"
    embed.set_image(url=url1)
    embed.set_footer(icon_url=logohusky, text="Created by HuskY Op")
    await ctx.send('PLACE_LOGO_URL_HERE')
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(send_messages=True)
async def yt(ctx):
    """Command to get the YouTube channel link."""
    embed = discord.Embed(title="YOUTUBE CHANNEL LINK", description="**[NUVOLO](PLACE_YOUTUBE_CHANNEL_URL_HERE)**", color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.set_thumbnail(url=logo)
    embed.set_footer(icon_url=logohusky, text="Powered by HuskY Op")
    url1 = "PLACE_IMAGE_URL_HERE"
    embed.set_image(url=url1)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(send_messages=True)
async def ig(ctx):
    """Command to get the Instagram profile link."""
    embed = discord.Embed(title="INSTAGRAM PROFILE LINK", description="**[@miss__edwardz](PLACE_INSTAGRAM_PROFILE_URL_HERE)**", color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.set_thumbnail(url=logo)
    embed.set_footer(icon_url=logohusky, text="Powered by HuskY Op")
    url1 = "PLACE_IMAGE_URL_HERE"
    embed.set_image(url=url1)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(send_messages=True)
async def dcinvite(ctx):
    """Command to get the Discord invite link."""
    embed = discord.Embed(title="DISCORD INVITE LINK", description="PLACE_DISCORD_INVITE_URL_HERE", color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.set_thumbnail(url=logo)
    embed.set_footer(icon_url=logohusky, text="Powered by HuskY Op")
    url1 = "PLACE_IMAGE_URL_HERE"
    embed.set_image(url=url1)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(send_messages=True)
async def whatsapp(ctx):
    """Command to get the WhatsApp group link."""
    embed = discord.Embed(title="WHATSAPP GROUP LINK", description="**[WhatsApp](PLACE_WHATSAPP_GROUP_URL_HERE)**", color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.set_thumbnail(url=logo)
    embed.set_footer(icon_url=logohusky, text="Powered by HuskY Op")
    url1 = "PLACE_IMAGE_URL_HERE"
    embed.set_image(url=url1)
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(send_messages=True)
async def live(ctx, *, message):
    """Command to announce that the user is live."""
    embed = discord.Embed(title="WITCH IS LIVE GUYS", description=message, color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.set_thumbnail(url=logo)
    url1 = "PLACE_GIF_URL_HERE"
    embed.set_image(url=url1)
    embed.set_footer(icon_url=logohusky, text="Powered by HuskY Op")
    await ctx.channel.purge(limit=1)
    await ctx.send(embed=embed)
    everyone = "@everyone"
    await ctx.send(everyone)

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def reply(ctx, user: discord.Member = None, *, message):
    """Command to reply to a user's DM."""
    msg = "**" + message + "**"
    embed = discord.Embed(title="REPLY TO YOUR DM - WITCH GAMING", description=msg, color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.set_thumbnail(url=logo)
    url1 = "PLACE_GIF_URL_HERE"
    embed.set_image(url=url1)
    embed.set_footer(icon_url=logohusky, text="Created by HuskY Op")
    await user.send(embed=embed)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f'{user} HAS BEEN REPLIED BY {ctx.author}', description='', color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.add_field(name='REPLY', value=msg, inline=False)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def dm(ctx, user: discord.Member = None, *, message):
    """Command to send a direct message to a user."""
    msg = "**" + message + "**"
    embed = discord.Embed(title="DM FROM WITCH GAMING", description=msg, color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.set_thumbnail(url=logo)
    embed.set_footer(icon_url=logohusky, text="Created by HuskY Op")
    url1 = "PLACE_GIF_URL_HERE"
    embed.set_image(url=url1)
    await user.send(embed=embed)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f'{user} HAS BEEN MESSAGED BY {ctx.author}', description='', color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.add_field(name='REASON', value=msg, inline=False)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, user: discord.Member = None, *, message):
    """Command to warn a user."""
    embed = discord.Embed(title="YOU HAVE BEEN WARNED", description=message, color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.set_thumbnail(url=logo)
    embed.set_footer(icon_url=logohusky, text="Created by HuskY Op")
    url1 = "PLACE_GIF_URL_HERE"
    embed.set_image(url=url1)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def mute(ctx, user: discord.Member = None):
    """Command to mute a user."""
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await user.add_roles(role)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f'{user} HAS BEEN MUTED', description=f'{ctx.author.mention} has muted {user.mention}', color=discord.Color.random(), timestamp=datetime.utcnow())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unmute(ctx, user: discord.Member = None):
    """Command to unmute a user."""
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await user.remove_roles(role)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f'{user} HAS BEEN UNMUTED', description=f'{ctx.author.mention} has unmuted {user.mention}', color=discord.Color.random(), timestamp=datetime.utcnow())
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def kick(ctx, user: discord.Member = None, *, reason=None):
    """Command to kick a user."""
    await user.kick(reason=reason)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f'{user} HAS BEEN KICKED', description=f'{ctx.author.mention} has kicked {user.mention}', color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.add_field(name='REASON', value=reason, inline=False)
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member = None, *, reason=None):
    """Command to ban a user."""
    await user.ban(reason=reason)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title=f'{user} HAS BEEN BANNED', description=f'{ctx.author.mention} has banned {user.mention}', color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.add_field(name='REASON', value=reason, inline=False)
    await ctx.send(embed=embed)

@bot.event
async def on_member_join(member):
    """Event triggered when a new member joins the server."""
    embed = discord.Embed(title="WELCOME TO NUVOLO", description=f"Welcome to Witch Gaming, {member.mention}! Enjoy your stay and be sure to check out the rules!", color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.set_thumbnail(url=logo)
    embed.set_footer(icon_url=logohusky, text="Created by HuskY Op")
    url1 = "PLACE_WELCOME_IMAGE_URL_HERE"
    embed.set_image(url=url1)
    general_channel = discord.utils.get(member.guild.text_channels, name='general')
    await general_channel.send(embed=embed)

@bot.command()  
@commands.has_permissions(send_messages=True)
async def help(ctx):
    """Command to display help information."""
    embed = discord.Embed(title="HELP", description="**Available Commands**", color=discord.Color.random(), timestamp=datetime.utcnow())
    embed.set_thumbnail(url=logo)
    embed.set_footer(icon_url=logohusky, text="Created by HuskY Op")
    embed.add_field(name="announce", value="`n.announce <message>` - Make an announcement", inline=False)
    embed.add_field(name="say", value="`n.say <message>` - Make the bot say something", inline=False)
    embed.add_field(name="rules", value="`n.rules <message>` - Set the server rules", inline=False)
    embed.add_field(name="yt", value="`n.yt` - Get the YouTube channel link", inline=False)
    embed.add_field(name="ig", value="`n.ig` - Get the Instagram profile link", inline=False)
    embed.add_field(name="dcinvite", value="`n.dcinvite` - Get the Discord invite link", inline=False)
    embed.add_field(name="whatsapp", value="`n.whatsapp` - Get the WhatsApp group link", inline=False)
    embed.add_field(name="live", value="`n.live <message>` - Announce that the user is live", inline=False)
    embed.add_field(name="reply", value="`n.reply <user> <message>` - Reply to a user's DM", inline=False)
    embed.add_field(name="dm", value="`n.dm <user> <message>` - Send a direct message to a user", inline=False)
    embed.add_field(name="warn", value="`n.warn <user> <message>` - Warn a user", inline=False)
    embed.add_field(name="mute", value="`n.mute <user>` - Mute a user", inline=False)
    embed.add_field(name="unmute", value="`n.unmute <user>` - Unmute a user", inline=False)
    embed.add_field(name="kick", value="`n.kick <user> <reason>` - Kick a user", inline=False)
    embed.add_field(name="ban", value="`n.ban <user> <reason>` - Ban a user", inline=False)
    await ctx.send(embed=embed)

# Run the bot with the token (replace 'YOUR_BOT_TOKEN' with your actual bot token)
bot.run('YOUR_BOT_TOKEN')
