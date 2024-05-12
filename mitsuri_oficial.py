#!/usr/bin/python3.8.6
import discord
from discord.ext import commands as command
import json
import time
import sys
import asyncio
from discord.utils import get
from discord import message
from discord.ext.commands import has_permissions
import discord_slash
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from dotenv import load_dotenv
from os import getenv
from typing import Optional
from discord import VoiceChannel
from discord.ext import commands
from dcactivity import DCApplication, DCActivity
from dcactivity.errors import InvalidChannel
import os
import es
import en
import dbl
import logging
import random
import wavelink
from discord import Client, VoiceChannel
from youtube_search import YoutubeSearch
from typing import Union
from itertools import islice
import urllib.request
import re
import lxml
from lxml import etree
from pytube import Playlist
import requests

#Carga el token del bot
token = ""

def get_prefix(client, message):
    try:
        with open('prefix.json', 'r') as f:
            prefixes = json.load(f)
        return prefixes[str(message.guild.id)]
    except:
        return "mi!"

#Configuración primaria de discord
client = command.Bot(command_prefix=get_prefix)
Client = discord.Client()
#configuración slash commands
slash = SlashCommand(client, sync_commands=True)

#Elimina el comando help por defecto de discord.py
client.remove_command('help')

#activity (youtube, juegos y demás)
dcactivity = DCActivity(client)

#declaración para cosas de comandos de tiempo
ltime = time.asctime(time.localtime())

#declaraciones varias
prefijo = get_prefix

async def statuschange(variable):
	while True:
		await client.change_presence(activity=discord.Game(name='Making your server cuteㅤㅤㅤㅤ\nHaciendo tu servidor cute \nㅤㅤㅤㅤVersión : Beta 4.000'))
		await asyncio.sleep(15)
		await client.change_presence(activity=discord.Game(name=f'mi!help ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ\nㅤㅤㅤ[On {variable} Servers]ㅤㅤㅤㅤㅤㅤㅤㅤ\nㅤㅤㅤ[En {variable} Servidores]'))
		await asyncio.sleep(45)
@client.event
async def on_ready():
    variable = len(client.guilds)
    channel = client.get_channel(777353937883103304)
    print('-------------------------------------------------------------------------------------')
    print(f'¡Estoy en linea! ---> [INFO {ltime}]: en linea como {client.user.name}!')
    print('-------------------------------------------------------------------------------------')
    emoji = client.get_emoji(777339891465453578)
    emoji1 = client.get_emoji(777335701309489172)
    emoji2 = client.get_emoji(777339891663110165)
    embed = discord.Embed(color=0xF9B7FF)
    embed.set_author(name='Estado de Mitsuri')
    embed.add_field(name='Mitsuri:', value='Estoy en línea de nuevo')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/770274146704949278/777319803072282624/iu.png?width=684&height=684')
    embed.set_footer(text=f'{ltime}')
    msg = await channel.send(embed=embed)
    await msg.add_reaction(emoji)
    await msg.add_reaction(emoji1)
    await msg.add_reaction(emoji2)
    await statuschange(variable)
 
#Carga de todos los cogs
client.load_extension("commands.activity")
client.load_extension("commands.help")
client.load_extension("commands.game")
client.load_extension("commands.reacciones")
client.load_extension("commands.media")
client.load_extension("commands.useful")
client.load_extension("commands.info")
client.load_extension("commands.nsfw")
client.load_extension("slash.slash_help")
client.load_extension("slash.slash_game")
client.load_extension("slash.slash_reactions")
client.load_extension("slash.slash_media")
client.load_extension("slash.slash_useful")
client.load_extension("slash.slash_info")

@client.command()
@commands.is_owner()
async def restart_(ctx):
    os.system('^C')
    os.system('python3 mitsuri_oficial.py')
    exit()

    
class TopGG(command.Cog):
    """Handles interactions with the top.gg API"""

    def __init__(self, bot):
        self.bot = bot
        self.token = '' # set this to your DBL token
        self.dblpy = dbl.DBLClient(self.bot, self.token, autopost=True) # Autopost will post your guild count every 30 minutes

client.add_cog(TopGG(client))



#comprobación de lenguaje del servidor del comando
def lang_comprove(guild_id):
    with open("lang.json", "r") as f:
        guilds = json.load(f)
    if str(guild_id) in guilds:
        language = guilds[str(guild_id)]["lang"]
        return language
    else:
        return False

#Registra el prefijo base en el servidor nuevo
@client.event
async def on_guild_join(guild):

    with open('prefix.json', 'r') as f: 
        prefixes = json.load(f) 

    prefixes[str(guild.id)] = 'mi!'

    with open('prefix.json', 'w') as f: 
        json.dump(prefixes, f, indent=4)

prefix = [
    create_option(
        name = "prefix",
        description = "hange bot prefix",
        required = True,
        option_type = 3
    )
]

lang = [
        create_option(
        name = "lang",
        description = "Change bot language",
        required = True,
        option_type = 3,
        choices=[
            create_choice(
                name = "Español",
                value = "es"
            ),
            create_choice(
                name = "English",
                value = "en"
            )
        ]
        )
]

#Cambio de prefijo del servidor 
@slash.slash(name = 'prefix', description = 'Change bot prefix', guild_ids = [], options = prefix)
@client.command(aliases=['Prefix','PREFIX','prefijo','Prefijo''PREFIJO'])
@has_permissions(administrator=True) 
async def prefix(ctx, prefix=None):
    guild_id = ctx.author.guild.id
    lang = lang_comprove(guild_id)
    if lang == False:
        text = es.lang_comprove()
        em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
        await ctx.send(embed=em)
    else:
    
        with open('prefix.json', 'r') as f: 
            prefixes = json.load(f) 
            prefijo = prefixes[str(ctx.guild.id)] 
            if prefix == None:
                if lang == 'es':
                    respuesta = es.prefix(1)
                elif lang == 'en':
                    respuesta = en.prefix(1)
                embed = discord.Embed(color=discord.Color.blue())
                embed.add_field(name=respuesta[0], value=respuesta[1])
                await ctx.send(embed=embed)
            else:
                if lang == 'es':
                    respuesta = es.prefix(2)
                elif lang == 'en':
                    respuesta = en.prefix(2)
                with open('prefix.json', 'r') as f:
                    prefixes = json.load(f)
                prefixes[str(ctx.guild.id)] = prefix
                embed = discord.Embed(description=f'{respuesta} `{prefix}`', color=discord.Color.blue())
                await ctx.send(embed=embed)
                with open('prefix.json', 'w') as f: 
                    json.dump(prefixes, f, indent=4)

#Cambio de idioma para cada servidor
@slash.slash(name = 'lang', description = 'Change bot language', guild_ids = [], options = lang)
@client.command()
@has_permissions(administrator=True) 
async def lang(ctx, lang=None):
    guild_id = ctx.author.guild.id
    if lang == None:
        respuesta = es.lang(1, 0, 0, lang)
        embed = discord.Embed(color=ctx.author.color)
        embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
        embed.add_field(name=respuesta[0], value=respuesta[1])
        await ctx.send(embed=embed)
    else:
        lang_es = ["Español", "español", "espanyol", "Espanyol", "Es", "es", "ES", "Sp", "SP", "sp"]
        lang_en = ["English", "english", "Inglés", "inglés", "En", "en", "EN"]
        lang_fr = ["français", "Français", "Fr", "fr", "FR"]
        langu = ["Español", "español", "espanyol", "Espanyol", "Es", "es", "ES", "Sp", "SP", "sp", "English", "english", "Inglés", "inglés", "En", "en", "EN", "français", "Français", "Fr", "fr", "FR"]
        if not lang in langu:
            respuesta = es.lang(2, 0, 0, lang)
            embed = discord.Embed(color=ctx.author.color)
            embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            embed.add_field(name=respuesta[0], value=respuesta[1])
            await ctx.send(embed=embed)
        else:
            with open("lang.json", "r") as f:
                guilds = json.load(f)
            try:
                language = guilds[str(guild_id)]["lang"]
                if language == "es":
                    respuesta = es.lang(3, 1, 0, lang)
                    embed = discord.Embed(color=ctx.author.color)
                    embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                    embed.add_field(name=f'{respuesta[0]}`{language}`', value=f'{respuesta[1]}`{lang}`')
                    a = await ctx.send(embed=embed)
                    await asyncio.sleep(8)
                    await a.delete()
                    if lang in lang_es:
                        language  = "es"
                        respuesta = es.lang(3, 1, 1, lang)
                    elif lang in lang_en:
                        language  = "en"
                        respuesta = es.lang(3, 1, 2, lang)
                    elif lang in lang_fr:
                        language  = "fr"
                        respuesta = es.lang(3, 1, 3, lang)
                    embed = discord.Embed(color=ctx.author.color)
                    embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                    embed.add_field(name=respuesta[0], value=respuesta[1])
                    await ctx.send(embed=embed)
                elif language == "en":
                    respuesta = es.lang(3, 2, 0, lang)
                    embed = discord.Embed(color=ctx.author.color)
                    embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                    embed.add_field(name=f'{respuesta[0]}`{language}`', value=f'{respuesta[1]}`{lang}`')
                    a = await ctx.send(embed=embed)
                    await asyncio.sleep(8)
                    await a.delete()
                    if lang in lang_es:
                        language  = "es"
                        respuesta = es.lang(3, 2, 1, lang)
                    elif lang in lang_en:
                        language  = "en"
                        respuesta = es.lang(3, 2, 2, lang)
                    elif lang in lang_fr:
                        language  = "fr"
                        respuesta = es.lang(3, 2, 3, lang)
                    embed = discord.Embed(color=ctx.author.color)
                    embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                    embed.add_field(name=respuesta[0], value=respuesta[1])
                    await ctx.send(embed=embed)
                elif language == "fr":
                    respuesta = es.lang(3, 3, 0, lang)
                    embed = discord.Embed(color=ctx.author.color)
                    embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                    embed.add_field(name=f'{respuesta[0]}`{language}`', value=f'{respuesta[1]}`{lang}`')
                    a = await ctx.send(embed=embed)
                    await asyncio.sleep(8)
                    await a.delete()
                    if lang in lang_es:
                        language  = "es"
                        respuesta = es.lang(3, 3, 1, lang)
                    elif lang in lang_en:
                        language  = "en"
                        respuesta = es.lang(3, 3, 2, lang)
                    elif lang in lang_fr:
                        language  = "fr"
                        respuesta = es.lang(3, 3, 3, lang)
                    embed = discord.Embed(color=ctx.author.color)
                    embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                    embed.add_field(name=respuesta[0], value=respuesta[1])
                    await ctx.send(embed=embed)
                guilds[str(guild_id)]["lang"] = language
                with open("lang.json", "w") as f:
                    json.dump(guilds,f, indent=4)
            except:
                respuesta = es.lang(4, 0, 0, lang)
                embed = discord.Embed(color=ctx.author.color)
                embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                embed.add_field(name=respuesta[0], value=respuesta[1])
                msg = await ctx.send(embed=embed)
                await asyncio.sleep(8)
                await msg.delete()
                if lang in lang_es:
                    language  = "es"
                    respuesta = es.lang(4, 1, 0, lang)
                elif lang in lang_en:
                    language  = "en"
                    respuesta = es.lang(4, 2, 0, lang)
                elif lang in lang_fr:
                    language  = "fr"
                    respuesta = es.lang(4, 3, 0, lang)
                embed = discord.Embed(color=ctx.author.color)
                embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                embed.add_field(name=respuesta[0], value=respuesta[1])
                await ctx.send(embed=embed)
                guilds[str(guild_id)] = {}
                guilds[str(guild_id)]["lang"] = language
                with open("lang.json", "w") as f:
                    json.dump(guilds,f, indent=4)

#comando activity / hay que implementarlo con cogs
@client.command()
async def ytactivity(ctx, channel=None):
    if not channel:
        if not ctx.author.voice:
            return await ctx.send("You need to connect to a voice channel first")
        if not isinstance(ctx.author.voice.channel, VoiceChannel):
            return await ctx.send("This feature is not supported in Stage Channels.")
        _channel = ctx.author.voice.channel
    else:
        _channel = channel
    invite = await dcactivity.create_invite(_channel, DCApplication.youtube, max_age=0)
    await ctx.send(invite)

@client.command()
async def fishactivity(ctx, channel=None):
    if not channel:
        if not ctx.author.voice:
            return await ctx.send("You need to connect to a voice channel first")
        if not isinstance(ctx.author.voice.channel, VoiceChannel):
            return await ctx.send("This feature is not supported in Stage Channels.")
        _channel = ctx.author.voice.channel
    else:
        _channel = channel
    invite = await dcactivity.create_invite(_channel, DCApplication.fishing, max_age=0)
    await ctx.send(invite)

@client.command()
async def betractivity(ctx, channel=None):
    if not channel:
        if not ctx.author.voice:
            return await ctx.send("You need to connect to a voice channel first")
        if not isinstance(ctx.author.voice.channel, VoiceChannel):
            return await ctx.send("This feature is not supported in Stage Channels.")
        _channel = ctx.author.voice.channel
    else:
        _channel = channel
    invite = await dcactivity.create_invite(_channel, DCApplication.betrayal, max_age=0)
    await ctx.send(invite)

@client.command()
async def pokeractivity(ctx, channel=None):
    if not channel:
        if not ctx.author.voice:
            return await ctx.send("You need to connect to a voice channel first")
        if not isinstance(ctx.author.voice.channel, VoiceChannel):
            return await ctx.send("This feature is not supported in Stage Channels.")
        _channel = ctx.author.voice.channel
    else:
        _channel = channel
    invite = await dcactivity.create_invite(_channel, DCApplication.poker, max_age=0)
    await ctx.send(invite)
    
@client.command()
async def chessactivity(ctx, channel=None):
    if not channel:
        if not ctx.author.voice:
            return await ctx.send("You need to connect to a voice channel first")
        if not isinstance(ctx.author.voice.channel, VoiceChannel):
            return await ctx.send("This feature is not supported in Stage Channels.")
        _channel = ctx.author.voice.channel
    else:
        _channel = channel
    invite = await dcactivity.create_invite(_channel, DCApplication.chess, max_age=0)
    await ctx.send(invite)
    
class MusicController:

    def __init__(self, bot, guild_id):
        self.bot = bot
        self.guild_id = guild_id
        self.channel = None

        self.next = asyncio.Event()
        self.queue = asyncio.Queue()

        self.volume = 40
        self.now_playing = None

        self.bot.loop.create_task(self.controller_loop())

    async def controller_loop(self):
        await self.bot.wait_until_ready()

        player = self.bot.wavelink.get_player(self.guild_id)
        await player.set_volume(self.volume)

        while True:
            if self.now_playing:
                await self.now_playing.delete()

            self.next.clear()

            song = await self.queue.get()
            await player.play(song)
            self.now_playing = await self.channel.send(f'Reproduciendo: `{song}`')

            await self.next.wait()

class Music(command.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.controllers = {}

        if not hasattr(bot, 'wavelink'):
            self.bot.wavelink = wavelink.Client(bot=self.bot)

        self.bot.loop.create_task(self.start_nodes())

    async def start_nodes(self):
        await self.bot.wait_until_ready()

        # Initiate our nodes. For this example we will use one server.
        # Region should be a discord.py guild.region e.g sydney or us_central (Though this is not technically required)
        node = await self.bot.wavelink.initiate_node(host='lava.link',
                                              port=80,
                                              rest_uri='http://lava.link:80',
                                              password='youshallnotpass',
                                              identifier='customwelcomer',
                                              region='eu_central'
                                              )

        # Set our node hook callback
        node.set_hook(self.on_event_hook)

    async def on_event_hook(self, event):
        """Node hook callback."""
        if isinstance(event, (wavelink.TrackEnd, wavelink.TrackException)):
            controller = self.get_controller(event.player)
            controller.next.set()

    def get_controller(self, value: Union[command.Context, wavelink.Player]):
        if isinstance(value, command.Context):
            gid = value.guild.id
        else:
            gid = value.guild_id

        try:
            controller = self.controllers[gid]
        except KeyError:
            controller = MusicController(self.bot, gid)
            self.controllers[gid] = controller

        return controller

    async def cog_check(self, ctx):
        """A local check which applies to all command in this cog."""
        if not ctx.guild:
            raise command.NoPrivateMessage
        return True

    async def cog_command_error(self, ctx, error):
        """A local error handler for all errors arising from command in this cog."""
        if isinstance(error, command.NoPrivateMessage):
            try:
                return await ctx.send('Este comando no puede ser usado en chats privados')
            except discord.HTTPException:
                pass

        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


    @command.command(aliases = ["p", "pl", "pla"])
    async def play(self, ctx, *, query: str):
        try:      
            player = self.bot.wavelink.get_player(ctx.guild.id)
            if not player.is_connected:
                await ctx.invoke(self)
        except:
            return
        playlist_con = 0
        if 'https://open.spotify.com' in query:
            query = query
        elif 'https://www.youtube.com/watch?v=' and '&list=' in query:
            p = Playlist(query)
            play_list = []
            for url in p.video_urls:
                play_list += [url]
            playlist_con = 1
        elif not "https://www.youtube.com/watch?v=" in query and not "https://youtu.be/" in query:
            results = YoutubeSearch(f'{query}', max_results=10).to_dict()
            songss = ''
            títulos = []
            links = []
            #idd = results["videos"]
            for x in range(10):
                título = results[x]['title']
                títulos += [results[x]['title']]
                temp = results[x]['url_suffix']
                links += [f'https://youtu.be/{temp}']
                songss += f'**{[x+1]}**. {título}\n'
            em = discord.Embed(title=f'Resultados de la búsqueda {query}', description=songss, colour=random.randint(0, 16777215))
            await ctx.send(embed=em)
            
            def check(m):
                return m.author.id == ctx.author.id
            try:
                    
                response = await client.wait_for('message', timeout=30.0,check=check)
            
            except:
                await ctx.send("Se ha agotado el tiempo de selección, vuelve a intentarlo")
                return
                
            try:
                ent = int(response.content)
                if ent < 1 or ent > 10:
                    await ctx.send("Has intorducido un número no válido, vuelve a intentarlo")
                    return
                query = títulos[ent-1]
            except:
                await ctx.send("Has intorducido un número no válido, vuelve a intentarlo")
                return

        if playlist_con == 0:
            tracks = await self.bot.wavelink.get_tracks(f'ytsearch:{query}')

            track = tracks[0]

            controller = self.get_controller(ctx)
        
            await controller.queue.put(track)
            await ctx.send(f'**{str(track)}** Se ha agregado a la lista de canciones')
        else:
            controller = self.get_controller(ctx)
            await ctx.send(f'Se ha agregado **{len(play_list)}** canciones a la lista de canciones')
            for x in play_list:
              await asyncio.sleep(5)
              try:
                tracks = await self.bot.wavelink.get_tracks(f'ytsearch:{x}')
                track = tracks[0]
                await controller.queue.put(track)
              except:
                pass
            

    @command.command(aliases=["pa", "pau"])
    async def pause(self, ctx):
        """Pause the player."""
        player = self.bot.wavelink.get_player(ctx.guild.id)
        if not player.is_playing:
            return await ctx.send('Actualmente no estoy reproduciendo música')

        await ctx.send('Música pausada!')
        await player.set_pause(True)

    @command.command(aliases=["re", "resu"])
    async def resume(self, ctx):
        """Resume the player from a paused state."""
        player = self.bot.wavelink.get_player(ctx.guild.id)
        if not player.paused:
            return await ctx.send('Actualmente no hay ninguna música pausada')

        await ctx.send('Repreduciendo la música de nuevo!')
        await player.set_pause(False)

    @command.command(aliases=["sk", "n", "ski", "next"])
    async def skip(self, ctx):
        """Skip the currently playing song."""
        player = self.bot.wavelink.get_player(ctx.guild.id)

        if not player.is_playing:
            return await ctx.send('Actualmente no estoy reproduciendo música')

        await ctx.send('Siguiente canción!')
        await player.stop()

    @command.command(aliases = ["v", "vol", "vo"])
    async def volume(self, ctx, *, vol: int):
        """Set the player volume."""
        player = self.bot.wavelink.get_player(ctx.guild.id)
        controller = self.get_controller(ctx)

        vol = max(min(vol, 1000), 0)
        controller.volume = vol

        await ctx.send(f'Actualizando el volumen a: `{vol}`')
        await player.set_volume(vol)

    @command.command()
    async def stop(self, ctx):
        """Stop and disconnect the player and controller."""
        player = self.bot.wavelink.get_player(ctx.guild.id)

        try:
            del self.controllers[ctx.guild.id]
        except KeyError:
            await player.disconnect()
            return await ctx.send('Actualmente no estoy reproduciendo música')

        await player.destroy()
        await ctx.send('Desconectando..., nos vemos luego!')

    @command.command(aliases=['disconnect', 'dc', 'left'])
    async def leave(self, ctx):
        """Stop and disconnect the player and controller."""
        player = self.bot.wavelink.get_player(ctx.guild.id)

        try:
            del self.controllers[ctx.guild.id]
        except KeyError:
            await player.disconnect()
            return await ctx.send('Actualmente no estoy reproduciendo música')

        await player.disconnect()
        await player.destroy()
        await ctx.send('Desconectando..., nos vemos luego!')

client.add_cog(Music(client))



@client.command()
async def say(ctx, *, men):
    await ctx.message.delete()
    await ctx.send(men)

client.run(token)
