import sys
import json
import time
import asyncio
import random
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_option, create_choice
from typing import Optional

import es
import en

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

def lang_comprove(guild_id):
    with open("lang.json", "r") as f:
        guilds = json.load(f)
    if str(guild_id) in guilds:
        language = guilds[str(guild_id)]["lang"]
        return language
    else:
        return False

optional = [
        create_option(
        name = "mention",
        description = "Mention a friend",
        required = False,
        option_type = 6,
        )
]

class info_slash_commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @cog_ext.cog_slash(name = 'servericon', description = 'Sends the number of pages the doujin has entered', guild_ids = [], options = [])
    async def servericon(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            icon_url = str(ctx.guild.icon_url)
            if not "https" in icon_url:
                if lang == 'es':
                    text = es.servericon(1)
                elif lang == 'en':
                    text = en.servericon(1)
                await ctx.send(text, delete_after=10.0)
            else:
                if lang == 'es':
                    text = es.servericon(2)
                elif lang == 'en':
                    text = en.servericon(2)
                embed = discord.Embed(title=text[0], color=ctx.author.color)
                embed.set_image(url=icon_url)
                embed.set_footer(text=f'{text[1]} {ctx.author.display_name}<-')
                await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'serverinfo', description = 'Send a detailed description of the current server', guild_ids = [], options = [])
    async def serverinfo(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:

            icon_url = str(ctx.guild.icon_url)
            if "https" in icon_url:
                if lang == 'es':
                    text = es.serverinfo(1)
                elif lang == 'en':
                    text = en.serverinfo(1)
                embed = discord.Embed(color=0xea7938)
                embed.set_thumbnail(url=f'{icon_url}')
                embed.add_field(name=text[0], value=f'{ctx.guild.name}')
                embed.add_field(name=text[1], value=f'{ctx.guild.id}')
                embed.add_field(name=text[2], value=f'{ctx.guild.region}', inline=True)
                embed.add_field(name=text[3], value=f'{ctx.guild.owner}')
                embed.add_field(name=text[4], value=str(ctx.guild.verification_level))
                embed.add_field(name=text[5], value=text[16])
                embed.add_field(name=text[6], value=f'{ctx.guild.member_count}')
                embed.add_field(name=text[7], value=f'{len(ctx.guild.channels)}')
                embed.add_field(name=text[8], value=f'{len(ctx.guild.text_channels)}')
                embed.add_field(name=text[9], value=f'{len(ctx.guild.voice_channels)}')
                embed.add_field(name=text[10], value=f'{len(ctx.guild.roles)}')
                embed.add_field(name=text[11], value=f'{ctx.guild.roles[-1]}')
                embed.add_field(name=text[12], value=f'{len(ctx.guild.emojis)}')
                embed.add_field(name=text[13], value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                embed.add_field(name=text[14], value=f'[Icono link]({icon_url})')
                embed.set_footer(text=f'{text[15]} {ctx.author.display_name}')
                await ctx.send(embed=embed)
            else:
                if lang == 'es':
                    text = es.serverinfo(2)
                elif lang == 'en':
                    text = en.serverinfo(2)
                embed = discord.Embed(color=0xea7938)
                embed.set_thumbnail(url=f'{icon_url}')
                embed.add_field(name=text[0], value=f'{ctx.guild.name}')
                embed.add_field(name=text[1], value=f'{ctx.guild.id}')
                embed.add_field(name=text[2], value=f'{ctx.guild.region}', inline=True)
                embed.add_field(name=text[3], value=f'{ctx.guild.owner}')
                embed.add_field(name=text[4], value=str(ctx.guild.verification_level))
                embed.add_field(name=text[5], value=text[16])
                embed.add_field(name=text[6], value=f'{ctx.guild.member_count}')
                embed.add_field(name=text[7], value=f'{len(ctx.guild.channels)}')
                embed.add_field(name=text[8], value=f'{len(ctx.guild.text_channels)}')
                embed.add_field(name=text[9], value=f'{len(ctx.guild.voice_channels)}')
                embed.add_field(name=text[10], value=f'{len(ctx.guild.roles)}')
                embed.add_field(name=text[11], value=f'{ctx.guild.roles[-1]}')
                embed.add_field(name=text[12], value=f'{len(ctx.guild.emojis)}')
                embed.add_field(name=text[13], value=ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
                embed.add_field(name=text[14], value=text[17])
                embed.set_footer(text=f'{text[15]} {ctx.author.display_name}')
                await ctx.send(embed=embed)    

    @cog_ext.cog_slash(name = 'profile', description = 'Send a detailed description to a person from the server or yours if you do not specify person', guild_ids = [], options = optional)
    async def profile(self, ctx: SlashContext,mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            
            if mention == None:
                user = str(client.get_user(ctx.author.id))
                usu = ctx.author.display_name
                user_init = ctx.author.created_at.__format__('%A, %d. %B %Y \n@ %H:%M:%S')
                user_join = ctx.author.joined_at.__format__('%A, %d. %B %Y \n@ %H:%M:%S')
                roles = ctx.author.roles
                filt = roles[::-1]
                if user[0:len(user)-5] == usu:
                    apodo = "Ninguno"
                else:
                    apodo = ctx.author.display_name
                final_roles = ""
                i = 0
                for role in filt:
                    if str(role) == "@everyone":
                        final_roles += f",{role}"
                    else:
                        if i == 0:
                            final_roles += "<@&" + str(role.id) + ">"
                            i += 1
                        else:
                            final_roles += ",<@&" + str(role.id) + ">"
                if lang == 'es':
                    text = es.profile()
                elif lang == 'en':
                    text = en.profile()
                embed = discord.Embed(color=0xea7938)
                embed.set_author(name=f'{text[0]} {ctx.author.display_name}')
                embed.set_thumbnail(url=f'{ctx.author.avatar_url}')
                embed.add_field(name=text[1], value=f'{user}')
                embed.add_field(name=f'{text[2]}', value=f'{ctx.author.id}')
                embed.add_field(name=f' ‏‏‎ ', value=f' ‏‏‎ ')
                embed.add_field(name=f'{text[3]}', value=f'{apodo}')
                embed.add_field(name=f'{text[4]}', value=f'{roles[-1]}')
                embed.add_field(name=f' ‏‏‎ ', value=f' ‏‏‎ ')
                embed.add_field(name=f'{text[5]}', value=f'{user_init}')
                embed.add_field(name=f'{text[6]}', value=f'{user_join}')
                embed.add_field(name=f' ‏‏‎ ', value=f' ‏‏‎ ')
                embed.add_field(name=f'{text[7]}', value=f'{final_roles}')
                embed.set_footer(text=f'{text[8]} {ctx.author.display_name}')
                await ctx.send(embed=embed)
            else:
                user = str(mention)
                user2 = int(mention.id)
                user3 = self.bot.get_user(user2)
                user = user[0:len(user)-5]
                user_init = mention.created_at.__format__('%A, %d. %B %Y \n@ %H:%M:%S')
                user_join = mention.joined_at.__format__('%A, %d. %B %Y \n@ %H:%M:%S')
                roles = mention.roles
                filt = roles[::-1]
                apodo = mention.display_name
                final_roles = ""
                i = 0
                for role in filt:
                    if str(role) == "@everyone":
                        final_roles += f",{role}"
                    else:
                        if i == 0:
                            final_roles += "<@&" + str(role.id) + ">"
                            i += 1
                        else:
                            final_roles += ",<@&" + str(role.id) + ">"
                if lang == 'es':
                    text = es.profile()
                elif lang == 'en':
                    text = en.profile()
                embed = discord.Embed(color=0xea7938)
                embed.set_author(name=f'{text[0]} {ctx.author.display_name}')
                embed.add_field(name=text[1], value=f'{user}')
                embed.add_field(name=f'{text[2]}', value=f'{ctx.author.id}')
                embed.add_field(name=f' ‏‏‎ ', value=f' ‏‏‎ ')
                embed.add_field(name=f'{text[3]}', value=f'{apodo}')
                embed.add_field(name=f'{text[4]}', value=f'{roles[-1]}')
                embed.add_field(name=f' ‏‏‎ ', value=f' ‏‏‎ ')
                embed.add_field(name=f'{text[5]}', value=f'{user_init}')
                embed.add_field(name=f'{text[6]}', value=f'{user_join}')
                embed.add_field(name=f' ‏‏‎ ', value=f' ‏‏‎ ')
                embed.add_field(name=f'{text[7]}', value=f'{final_roles}')
                embed.set_footer(text=f'{text[8]} {ctx.author.display_name}')
                await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'ping', description = 'Shows ping between message and message, and Mitsuri ping', guild_ids = [], options = [])
    async def ping(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                text = es.ping()
            elif lang == 'en':
                text = en.ping()
            before = time.monotonic()
            message =  await ctx.send(".")
            ping = (time.monotonic() - before) * 1000
            mitsu = client.latency * 1000
            temp = discord.Embed(title=text[0], color=ctx.author.color)
            temp.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            temp.add_field(name=text[1], value=f'{int(ping)}{text[2]}', inline=False)
            temp.add_field(name=text[3], value=f'{mitsu}{text[4]}', inline=True)
            temp.set_footer(text=f'{text[5]} {ctx.author.display_name}')
            await message.edit(embed=temp)

    @cog_ext.cog_slash(name = 'vote', description = 'Send the link to Mitsuri!\'S top.gg page to vote!', guild_ids = [], options = [])
    async def vote(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                text = es.vote()
            elif lang == 'en':
                text = en.vote()
            embed = discord.Embed(color=ctx.author.color)
            embed.set_thumbnail(url='https://64.media.tumblr.com/d8841e84219ae53081bda00495cddb3d/5be347091e1ad9ec-55/s640x960/6141959d7cda3f3794d19a9bfffce0c088e19ca8.png')
            embed.add_field(name=text[0], value=text[1])
            embed.set_footer(text=f'{text[2]} {ctx.author.display_name}, {text[3]}')
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'feedback', description = 'Send a github link to report any bugs or suggestions', guild_ids = [], options = [])
    async def feedback(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                text = es.feedback()
            elif lang == 'en':
                text = en.feedback()
            embed = discord.Embed(color=ctx.author.color)
            embed.set_thumbnail(url='https://64.media.tumblr.com/8fac83ee7351cd6ac1c02587cbcac030/ec237f4a7d01db1a-22/s640x960/6a13f71d4812524d705130aa040dde8dea886d6b.jpg')
            embed.add_field(name=text[0], value=text[1])
            embed.set_footer(text=f'{text[2]} {ctx.author.display_name}, {text[3]}')
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'bughunter', description = 'Send a list of our helpers who have contributed ideas and found bugs to improve the bot', guild_ids = [], options = [])
    async def bughunter(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                f = open("casadores.txt", "r")
                lines = f.read().splitlines()
                f.close()
                stri = ""
                for x in range(len(lines)):
                    stri += "-|-" + str(lines[x]) + "-|-"
                embed = discord.Embed(color=ctx.author.color)
                embed.set_thumbnail(url='https://64.media.tumblr.com/d8841e84219ae53081bda00495cddb3d/5be347091e1ad9ec-55/s640x960/6141959d7cda3f3794d19a9bfffce0c088e19ca8.png')
                embed.add_field(name=f':warning: :exclamation: ¿Quienes son nuestros cazadores de bugs? :exclamation: :warning:\n Aquí muestro a las personitas que han encontrado fallos en mi y me han ayudado a corregirlos', value=f'\n```{stri}```')
                embed.set_footer(text=f'IMPORTANTE\nSi quieres estar aquí, encuentra un bug y contacta con el primero de esta lista')
                await ctx.send(embed=embed)
            elif lang == 'en':
                f = open("casadores.txt", "r")
                lines = f.read().splitlines()
                f.close()
                stri = ""
                for x in range(len(lines)):
                    stri += "-|-" + str(lines[x]) + "-|-"
                embed = discord.Embed(color=ctx.author.color)
                embed.set_thumbnail(url='https://64.media.tumblr.com/d8841e84219ae53081bda00495cddb3d/5be347091e1ad9ec-55/s640x960/6141959d7cda3f3794d19a9bfffce0c088e19ca8.png')
                embed.add_field(name=f':warning: :exclamation: Who are our bug hunters? :exclamation: :warning:\n Here I show the people who have found faults in me and have helped me to correct them', value=f'\n```{stri}```')
                embed.set_footer(text=f'IMPORTANT\nIf you want to be here, find a bug and contact with the first on this list')
                await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'partners', description = 'servers that have supported me from the beginning', guild_ids = [], options = [])
    async def partners(self, ctx: SlashContext):
        embed = discord.Embed(color=ctx.author.color)
        embed.set_thumbnail(url='https://64.media.tumblr.com/d8841e84219ae53081bda00495cddb3d/5be347091e1ad9ec-55/s640x960/6141959d7cda3f3794d19a9bfffce0c088e19ca8.png')
        embed.add_field(name=f':handshake: :gift_heart:  ¿Quienes son mis partners? :gift_heart: :handshake: ', value='\nTengo 2 servidores donde empecé a dar mis primeros pasos, ellos me ayudaron a crecer y a corregir mis errores y poco a poco fui mejorando y llegar a ser lo que soy ahora mismo')
        embed.add_field(name=f'\n-----Tenemos como primer Partner a: Valpo | Role & Game-----', value=f'Descripción: \n\n┌────────────────────────┐\n✦ ──────𝒱𝒶𝓁𝓅𝑜  𝓇𝑜𝓁𝑒  𝒶𝓃𝒹  𝒢𝒶𝓂𝑒───── ✦\n└────────────────────────┘\n\nSpanish server for gamers and role community\nServer en Español para la comunidad de gamers y role\n\n༄Roles por Nivel \n༄Roles de Colores \n༄Sorteos \n༄Eventos\n༄Apuestas\n༄Múltiples canales de chat\n༄Ciudad de Role\n༄Confesiones\n༄Juegos\n༄Familias\n༄Clubs\n༄Un bot 24/7 en cada canal de música\n⋘▬▬▬▬▬▬▬▬▬༺★༻▬▬▬▬▬▬▬▬▬▬⋙\n ✦ Invite Link: [Invitación al servidor de Valpo | Role & Game](https://discord.gg/JCR9Zjz)', inline=False)
        embed.add_field(name=f'\n------------Tenemos como segundo Partner a: WABI-SABI-----------', value=f'Descripción: \n\n┌────── ∘°❉°∘ ──────┐\n•---------- WABI-SABI---------•\n└────── °∘❉∘° ──────┘\n¿Quienes somos?\n\n✎﹏﹏﹏﹏﹏﹏﹏\n:sparkles:    Somos una comunidad que nace de la idea de tres amigos de tener un lugar agradable para charlar , opinar, compartir cositas sobre temática anime, videojuegos, arte,  y mucho más!\n﹏﹏﹏﹏\n¿Qué ofrecemos?\n\n➤ En Wabi-Sabi  puedes encontrar\n꒰:rice_ball:꒱↝ Comunidad activa\n꒰:dancer_tone1:꒱↝ Ambiente no tóxico\n꒰:slot_machine:꒱↝ Actividades y concursos\n꒰:game_die: ꒱↝ Autoroles \n꒰:crown:꒱↝ Premio especial a usuario del mes\n꒰:gift:꒱↝ Tienda con artículos especiales (Juegos, camisetas, skins, vales amazon, netflix, llaveros...)\n꒰:moneybag:꒱↝ Banco con tus puntos acumulados\n꒰:video_camera: ꒱↝ Streamings de todo tipo\n꒰:performing_arts: ꒱↝ Variedad de bots\n꒰:trophy: ꒱↝ Wabis!\n△▽△▽△▽△▽△▽△▽△▽△▽\n¿Qué esperas para unirte?\n➤ ¡Te estamos esperando! \n ✦ Invite Link: [Invitación al servidor de WABI-SABI](https://discord.gg/n3dAgSt)', inline=True)
        #embed.add_field(name=f'\n---------Tenemos como tercer Partner a: Otakus Shin Sekai--------', value='Descripción: \n\n┌────────────────────────┐\nঔৣ͜͡ঔৣ═════OTAKUS SHIN SEKAI ═════ঔৣ͜͡ঔৣ\n└────────────────────────┘\n\n𝚀𝚞𝚎 𝚝𝚎𝚗𝚎𝚖𝚘𝚜 𝚎𝚗 𝚎𝚜𝚝𝚎 𝚛𝚎𝚒𝚗𝚘?. 𝙼𝚞𝚌𝚑𝚒𝚜𝚒𝚖𝚊𝚜 𝚌𝚘𝚜𝚊𝚜!\n▬▬▬▬▬▬▬▬▬▬▬▬⌘⋆⋆⌘▬▬▬▬▬▬▬▬▬▬▬▬▬\n:pinching_hand: ␥ ⩩ 𝚁𝚎𝚐𝚕𝚊𝚜 𝚜𝚎𝚗𝚌𝚒𝚕𝚕𝚊𝚜\n:dizzy:  ␥ ⩩ 𝙰𝚕𝚒𝚊𝚗𝚣𝚊𝚜 𝚌𝚘𝚗 𝚌𝚞𝚊𝚕𝚚𝚞𝚒𝚎𝚛 𝚝𝚒𝚙𝚘 𝚍𝚎 𝚜𝚎𝚛𝚟𝚎𝚛𝚜.\n:muscle:  ␥ ⩩ 𝙾𝚠𝚗𝚎𝚛𝚎𝚜 𝚊𝚌𝚝𝚒𝚟𝚘𝚜, 𝚊𝚍𝚖𝚒𝚗𝚜 𝚊𝚌𝚝𝚒𝚟𝚘𝚜 𝚢 𝚜𝚎 𝚋𝚞𝚜𝚌𝚊 𝚎𝚗𝚌𝚊𝚛𝚐𝚊𝚍𝚘 𝚍𝚎 𝚊𝚕𝚒𝚊𝚗𝚣𝚊 𝚢 𝚙𝚊𝚛𝚊 𝚖𝚘𝚍𝚎𝚛𝚊𝚛 𝚎𝚕 𝚜𝚎𝚛𝚟𝚒𝚍𝚘𝚛\n:envelope:  ␥ ⩩ 𝙲𝚑𝚊𝚝 𝚊𝚌𝚝𝚒𝚟𝚘 𝚍𝚘𝚗𝚍𝚎 𝚙𝚘𝚍𝚛𝚊𝚜 𝚌𝚘𝚗𝚘𝚌𝚎𝚛 𝚐𝚎𝚗𝚝𝚎 𝚖𝚞𝚢 𝚍𝚒𝚟𝚎𝚛𝚝𝚒𝚍𝚊, 𝚌𝚑𝚊𝚛𝚕𝚊𝚛 𝚢 𝚓𝚞𝚐𝚊𝚛 𝚌𝚘𝚗 𝚎𝚕𝚕𝚘𝚜\n:robot: ␥ ⩩ 𝙱𝚘𝚝𝚜 𝚙𝚊𝚛𝚊 𝚍𝚒𝚟𝚎𝚛𝚝𝚒𝚛𝚜𝚎 𝚊 𝚖𝚘𝚗𝚝𝚘𝚗\n:boom:  ␥ ⩩ 𝙰𝚞𝚝𝚘-𝚛𝚘𝚕𝚎𝚜 𝚍𝚎: 𝚍𝚊𝚝𝚘𝚜 𝚗𝚘 𝚝𝚊𝚗 𝚙𝚎𝚛𝚜𝚘𝚗𝚊𝚕𝚎𝚜, 𝚌𝚘𝚕𝚘𝚛𝚎𝚜, 𝚓𝚞𝚎𝚐𝚘𝚜 𝚏𝚊𝚟𝚘𝚛𝚒𝚝𝚘𝚜, 𝙽𝚂𝙵𝚆, 𝚑𝚘𝚋𝚋𝚒𝚎𝚜, 𝚛𝚎𝚐𝚒ó𝚗, 𝚎𝚝𝚌.\n:projector:  ␥ ⩩ 𝙷𝚊𝚢 𝚙𝚎𝚕í𝚌𝚞𝚕𝚊 𝟷 𝚟𝚎𝚜 𝚊 𝚕𝚊 𝚜𝚎𝚖𝚊𝚗𝚊!.\n:hotsprings:  ␥ ⩩ 𝙷𝚊𝚌𝚎𝚖𝚘𝚜 𝚜𝚘𝚛𝚝𝚎𝚘𝚜 𝚌𝚊𝚍𝚊 𝟹 𝚖𝚎𝚜𝚎𝚜!.\n:rocket:  ␥ ⩩ Canales de sugerencia!, soporte técnico y reportes(por si alguien molesta)\n▬▬▬▬▬▬▬▬▬▬▬▬⌘⋆⋆⌘▬▬▬▬▬▬▬▬▬▬▬▬▬\n▬▬▬▬▬▬▬▬▬▬▬▬⌘⋆⋆⌘▬▬▬▬▬▬▬▬▬▬▬▬▬\n✦ Invite Link: [Invitación al servidor de Otakus Shin Sekai](https://discord.gg/tcdr429)', inline=False)
        embed.set_footer(text=f'¡Informacion de partners pedida por: {ctx.author.display_name}, Gracias!')
        await ctx.send(embed=embed, delete_after=120.0)

def setup(bot: commands.Bot):
    bot.add_cog(info_slash_commands(bot))