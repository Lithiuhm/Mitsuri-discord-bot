import sys
import json
import asyncio
import random
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_option, create_choice

import es
import en
from typing import Optional
from discord import VoiceChannel
from discord.ext import commands
from dcactivity import DCApplication
from dcactivity.errors import InvalidChannel
from discord import Client, VoiceChannel
from dcactivity import DCActivity, DCApplication

def get_prefix(client, message):
    try:
        with open('prefix.json', 'r') as f:
            prefixes = json.load(f)
        return prefixes[str(message.guild.id)]
    except:
        return "mi!"

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=get_prefix, intents=intents)
slash = SlashCommand(client, sync_commands=True)
client.remove_command('help')
dcactivity = DCActivity(client)

def lang_comprove(guild_id):
    with open("lang.json", "r") as f:
        guilds = json.load(f)
    if str(guild_id) in guilds:
        language = guilds[str(guild_id)]["lang"]
        return language
    else:
        return False

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def youtube(self, ctx, channel=None):
        if not channel:
            if not ctx.author.voice:
                return await ctx.send("You need to connect to a voice channel first")
            if not isinstance(ctx.author.voice.channel, VoiceChannel):
                return await ctx.send("This feature is not supported in Stage Channels.")
            _channel = ctx.author.voice.channel
        else:
            _channel = channel

        invite = await self.bot.dcactivity.create_invite(
            _channel, DCApplication.youtube, max_age=0, max_users=10)
        await ctx.send(invite)

    @youtube.error
    async def youtube_error(self, ctx, exc):
        exc = getattr(exc, "original", exc)
        if isinstance(exc, InvalidChannel):
            await ctx.send("Invalid Channel given as argument.")

def setup(bot):
    bot.add_cog(MyCog(bot))