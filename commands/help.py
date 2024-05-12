import json
import asyncio
import random
import discord
from discord.ext import commands
import sys

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
client.remove_command('help')

def lang_comprove(guild_id):
    with open("lang.json", "r") as f:
        guilds = json.load(f)
    if str(guild_id) in guilds:
        language = guilds[str(guild_id)]["lang"]
        return language
    else:
        return False

class help_commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command(aliases=['helpme'])
    async def help(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                respuesta = es.help(1, 0)
            elif lang == 'en':
                respuesta = en.help(1, 0)
            embed = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
            embed.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
            embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            embed.add_field(name='---------------------------------------------------------------------------', value=respuesta[2], inline=False)
            embed.add_field(name=respuesta[3], value=respuesta[4], inline=True)
            embed.add_field(name=respuesta[5], value=respuesta[6], inline=True)
            embed.add_field(name=respuesta[7], value=respuesta[8], inline=True)
            embed.add_field(name=respuesta[9], value=respuesta[10],inline=True)
            embed.add_field(name=respuesta[11], value=respuesta[12],inline=False)
            embed.set_footer(text=respuesta[13],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            msg = await ctx.send(embed=embed)
            await msg.add_reaction("🔰")
            await msg.add_reaction("📑")
            await msg.add_reaction("🔞")
            await msg.add_reaction("📚")
            await msg.add_reaction("📖")
            await msg.add_reaction("🎲")
            await msg.add_reaction("🎶")
            await msg.add_reaction("📸")
            await msg.add_reaction("💞")
            await msg.add_reaction("🔨")
            await msg.add_reaction("❌")
            def check(reaction, user):
                return int(user.id) != 761359894791192596 and str(reaction.emoji) in ['🔰', '📑','🔞','📚','📖','🎲','🎶','📸','💞','🔨','❌']
            try:
                while True:
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=180.0, check=check)                 
                    if reaction.emoji == '🔰':
                        if lang == 'es':
                            respuesta = es.help(1, 0)
                        elif lang == 'en':
                            respuesta = en.help(1, 0)
                        try:
                            await msg.remove_reaction("🔰", user)
                        except:
                            pass
                        embed = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
                        embed.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
                        embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        embed.add_field(name='---------------------------------------------------------------------------', value=respuesta[2], inline=False)
                        embed.add_field(name=respuesta[3], value=respuesta[4], inline=True)
                        embed.add_field(name=respuesta[5], value=respuesta[6], inline=True)
                        embed.add_field(name=respuesta[7], value=respuesta[8], inline=True)
                        embed.add_field(name=respuesta[9], value=respuesta[10],inline=True)
                        embed.add_field(name=respuesta[11], value=respuesta[12],inline=False)
                        embed.set_footer(text=respuesta[13],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        await msg.edit(embed=embed)
                    elif reaction.emoji == '📑':
                        if lang == 'es':
                            respuesta = es.help(1, 2)
                        elif lang == 'en':
                            respuesta = en.help(1, 2)
                        try:
                            await msg.remove_reaction("📑", user)
                        except:
                            pass
                        embed = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
                        embed.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
                        embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        embed.add_field(name=respuesta[2], value=respuesta[3],inline=False)
                        embed.set_footer(text=respuesta[4] ,icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        await msg.edit(embed=embed)
                    elif reaction.emoji == '🔞':
                        if lang == 'es':
                            respuesta = es.help(1, 3)
                        elif lang == 'en':
                            respuesta = en.help(1, 3)
                        try:
                            await msg.remove_reaction("🔞", user)
                        except:
                            pass
                        embed = discord.Embed(title=respuesta[0], color=ctx.author.color)
                        embed.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
                        embed.set_thumbnail(url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        embed.add_field(name=respuesta[2], value=respuesta[3], inline=False)
                        embed.add_field(name=respuesta[4], value=respuesta[5], inline=False)
                        embed.add_field(name=respuesta[6], value=respuesta[7], inline=False)
                        embed.set_footer(text=respuesta[8],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        await msg.edit(embed=embed)
                    elif reaction.emoji == '📚':
                        if lang == 'es':     
                            respuesta = es.help(1, 4)
                        elif lang == 'en':
                            respuesta = en.help(1, 4)
                        try:
                            await msg.remove_reaction("📚", user)
                        except:
                            pass
                        embed = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
                        embed.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
                        embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        embed.add_field(name=respuesta[2], value=respuesta[3],inline=False)
                        embed.set_footer(text=respuesta[4] ,icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        await msg.edit(embed=embed)
                    elif reaction.emoji == '📖':
                        if lang == 'es':     
                            respuesta = es.help(1, 5)
                        elif lang == 'en':
                            respuesta = en.help(1, 5)
                        try:
                            await msg.remove_reaction("📖", user)
                        except:
                            pass
                        embed = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
                        embed.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
                        embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        embed.add_field(name=respuesta[2], value=respuesta[3],inline=False)
                        embed.set_footer(text=respuesta[4] ,icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        await msg.edit(embed=embed)
                    elif reaction.emoji == '🎲':
                        if lang == 'es':     
                            respuesta = es.help(1, 6)
                        elif lang == 'en':
                            respuesta = en.help(1, 6)
                        try:
                            await msg.remove_reaction("🎲", user)
                        except:
                            pass 
                        embed = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
                        embed.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
                        embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        embed.add_field(name=respuesta[2], value=respuesta[3],inline=False)
                        embed.set_footer(text=respuesta[4] ,icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        await msg.edit(embed=embed)
                    elif reaction.emoji == '🎶':
                        if lang == 'es':     
                            respuesta = es.help(1, 7)
                        elif lang == 'en':
                            respuesta = en.help(1, 7)
                        try:
                            await msg.remove_reaction("🎶", user)
                        except:
                            pass 
                        embed = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
                        embed.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
                        embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        embed.add_field(name=respuesta[2], value=respuesta[3], inline=False)
                        embed.set_footer(text=respuesta[4],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        await msg.edit(embed=embed)
                    elif reaction.emoji == '📸':
                        if lang == 'es':     
                            respuesta = es.help(1, 8)
                        elif lang == 'en':
                            respuesta = en.help(1, 8)
                        try:
                            await msg.remove_reaction("📸", user)
                        except:
                            pass    
                        embed = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
                        embed.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
                        embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        embed.add_field(name=respuesta[2], value=respuesta[3],inline=False)
                        embed.set_footer(text=respuesta[4] ,icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        await msg.edit(embed=embed)
                    elif reaction.emoji == '💞':
                        if lang == 'es':     
                            respuesta = es.help(1, 9)
                        elif lang == 'en':
                            respuesta = en.help(1, 9)
                        try:
                            await msg.remove_reaction("💞", user)
                        except:
                            pass
                        embed = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
                        embed.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
                        embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        embed.add_field(name=respuesta[2], value=respuesta[3],inline=False)
                        embed.set_footer(text=respuesta[4] ,icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        await msg.edit(embed=embed)
                    elif reaction.emoji == '🔨':
                        if lang == 'es':     
                            respuesta = es.help(1, 10)
                        elif lang == 'en':
                            respuesta = en.help(1, 10)
                        try:
                            await msg.remove_reaction("🔨", user)
                        except:
                            pass
                        embed = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
                        embed.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
                        embed.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        embed.add_field(name=respuesta[2], value=respuesta[3],inline=False)
                        embed.set_footer(text=respuesta[4] ,icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                        await msg.edit(embed=embed)
                    elif reaction.emoji == '❌':
                        try:
                            await msg.remove_reaction("❌", user)
                        except:
                            pass
                        if lang == 'es':     
                            respuesta = es.help(1, 11)
                        elif lang == 'en':
                            respuesta = en.help(1, 11)
                        msg2 = await ctx.send(respuesta)
                        await asyncio.sleep(5.0)
                        await msg.delete()
                        await msg2.delete()
            except asyncio.TimeoutError:
                try: 
                    await msg.delete()
                except:
                    pass

    @commands.command(aliases=['commands'])
    async def comandos(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                respuesta = es.command()
            elif lang == 'en':
                respuesta = en.command()
            commands = discord.Embed(title=respuesta[0], color=ctx.author.color)
            commands.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
            commands.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            commands.add_field(name=respuesta[2], value=respuesta[3], inline=True)
            commands.add_field(name=respuesta[4], value=respuesta[5], inline=False)
            commands.add_field(name=respuesta[6], value=respuesta[7], inline=False)
            commands.add_field(name=respuesta[8], value=respuesta[9], inline=False)
            commands.add_field(name=respuesta[10], value=respuesta[11], inline=False)
            commands.add_field(name=respuesta[12], value=respuesta[13], inline=False)
            commands.add_field(name=respuesta[14], value=respuesta[15], inline=False)
            commands.add_field(name=respuesta[16], value=respuesta[17], inline=False)
            commands.add_field(name=respuesta[18], value=respuesta[19], inline=True)
            commands.add_field(name=respuesta[20], value=respuesta[21], inline=False)
            commands.add_field(name=respuesta[22], value=respuesta[23], inline=False)
            commands.add_field(name=respuesta[24], value=respuesta[25])
            commands.add_field(name=respuesta[26], value=respuesta[27], inline=False)
            commands.add_field(name=respuesta[28], value=respuesta[29], inline=False)
            commands.add_field(name=respuesta[30], value=respuesta[31], inline=False)
            commands.add_field(name=respuesta[32], value=respuesta[33], inline=False)
            commands.set_footer(text=respuesta[35],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            await ctx.author.send(embed=commands)
            mensage = await ctx.send(f'{ctx.author.display_name} {respuesta[34]}')
            await mensage.add_reaction("📩")

    @commands.command(aliases=['nodmcommands'])
    async def nodmcommandos(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                respuesta = es.command()
            elif lang == 'en':
                respuesta = en.command()
            commands = discord.Embed(title=respuesta[0], color=ctx.author.color)
            commands.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
            commands.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            commands.add_field(name=respuesta[2], value=respuesta[3], inline=True)
            commands.add_field(name=respuesta[4], value=respuesta[5], inline=False)
            commands.add_field(name=respuesta[6], value=respuesta[7], inline=False)
            commands.add_field(name=respuesta[8], value=respuesta[9], inline=False)
            commands.add_field(name=respuesta[10], value=respuesta[11], inline=False)
            commands.add_field(name=respuesta[12], value=respuesta[13], inline=False)
            commands.add_field(name=respuesta[14], value=respuesta[15], inline=False)
            commands.add_field(name=respuesta[16], value=respuesta[17], inline=False)
            commands.add_field(name=respuesta[18], value=respuesta[19], inline=True)
            commands.add_field(name=respuesta[20], value=respuesta[21], inline=False)
            commands.add_field(name=respuesta[22], value=respuesta[23], inline=False)
            commands.add_field(name=respuesta[24], value=respuesta[25])
            commands.add_field(name=respuesta[26], value=respuesta[27], inline=False)
            commands.add_field(name=respuesta[28], value=respuesta[29], inline=False)
            commands.add_field(name=respuesta[30], value=respuesta[31], inline=False)
            commands.add_field(name=respuesta[32], value=respuesta[33], inline=False)
            commands.set_footer(text=respuesta[35],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            await ctx.send(embed=commands, delete_after=360.0)

    @commands.command(aliases=['help nsfw'])
    async def help_nsfw(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                respuesta = es.help_nsfw()
            elif lang == 'en':
                respuesta = en.help_nsfw()
            commands = discord.Embed(title=respuesta[0], color=ctx.author.color)
            commands.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
            commands.set_thumbnail(url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            #commads.add_field(name=':bookmark_tabs:  Funny! :bookmark_tabs: ', value='```Comandos divertidos```', inline=True)
            commands.add_field(name=respuesta[2], value=respuesta[3], inline=False)
            commands.add_field(name=respuesta[4], value=respuesta[5], inline=False)
            commands.add_field(name=respuesta[6], value=respuesta[7], inline=False)
            commands.set_footer(text=respuesta[8],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            await ctx.send(embed=commands)    

    @commands.command(aliases=['help read'])
    async def help_read(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                respuesta = es.help_read()
            elif lang == 'en':
                respuesta = en.help_read()
            commands = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
            commands.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
            commands.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            commands.add_field(name=respuesta[2], value=respuesta[3], inline=False)
            commands.set_footer(text=respuesta[4],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            await ctx.send(embed=commands)

    @commands.command()
    async def help_info(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                respuesta = es.help_info()
            elif lang == 'en':
                respuesta = en.help_info()
            commands = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
            commands.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
            commands.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            commands.add_field(name=respuesta[2], value=respuesta[3], inline=False)
            commands.set_footer(text=respuesta[4],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            await ctx.send(embed=commands)

    @commands.command()
    async def help_media(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                respuesta = es.help_media()
            elif lang == 'en':
                respuesta = en.help_media()
            commands = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
            commands.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
            commands.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            commands.add_field(name=respuesta[2], value=respuesta[3], inline=False)
            commands.set_footer(text=respuesta[4],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            await ctx.send(embed=commands)

    @commands.command()
    async def help_games(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                respuesta = es.help_games()
            elif lang == 'en':
                respuesta = en.help_games()
            commands = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
            commands.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
            commands.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            commands.add_field(name=respuesta[2], value=respuesta[3], inline=False)
            commands.set_footer(text=respuesta[4],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            await ctx.send(embed=commands)

    @commands.command()
    async def help_music(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                respuesta = es.help_music()
            elif lang == 'en':
                respuesta = en.help_music()
            commands = discord.Embed(title=respuesta[0], color=ctx.author.color)
            commands.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
            commands.set_thumbnail(url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            #commads.add_field(name=':bookmark_tabs:  Funny! :bookmark_tabs: ', value='```Comandos divertidos```', inline=True)
            commands.add_field(name=respuesta[2], value=respuesta[3], inline=False)
            commands.set_footer(text=respuesta[4],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            await ctx.send(embed=commands)

    @commands.command()
    async def help_moder(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                respuesta = es.help_moder()
                commands = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
                commands.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
                commands.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                commands.add_field(name=respuesta[2], value=respuesta[3], inline=False)
                commands.set_footer(text=respuesta[4],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                await ctx.send(embed=commands)
            elif lang == 'en':
                commands = discord.Embed(title=":heartpulse: Here is a list of moder commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------", color=ctx.author.color) #,color=Hex code
                commands.set_author(name=f'{ctx.author.display_name} \n ❤️ We thank you for using Mitsuri  ❤️  ', icon_url=f'{ctx.author.avatar_url}')
                commands.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                commands.add_field(name=f':hammer: Moder :hammer:', value=f'```Moderation Commands \n Comming soon```')
                commands.set_footer(text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181",icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                await ctx.send(embed=commands)

    @commands.command()
    async def help_reacts(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                respuesta = es.help_reacts()
            elif lang == 'en':
                respuesta = en.help_reacts()
            commands = discord.Embed(title=respuesta[0], color=ctx.author.color)
            commands.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
            commands.set_thumbnail(url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            commands.add_field(name=respuesta[2], value=respuesta[3], inline=False)
            commands.add_field(name=respuesta[4], value=respuesta[5], inline=False)
            commands.add_field(name=respuesta[6], value=respuesta[7], inline=False)
            commands.set_footer(text=respuesta[8],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            await ctx.send(embed=commands)            

    @commands.command()
    async def help_useful(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                respuesta = es.help_useful()
            elif lang == 'en':
                respuesta = en.help_useful()
            commands = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
            commands.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
            commands.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            commands.add_field(name=respuesta[2], value=respuesta[3], inline=False)
            commands.set_footer(text=respuesta[4],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            await ctx.send(embed=commands)

    @commands.command()
    async def help_lang(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                respuesta = es.help_lang()
            elif lang == 'en':
                respuesta = en.help_lang()
            commands = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
            commands.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
            commands.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            commands.add_field(name=respuesta[2], value=f'```{respuesta[3]}\naf: afrikaans, \nsq: albanian, \nam: amharic, \nar: arabic, \nhy: armenian, \naz: azerbaijani, \neu: basque, \nbe: belarusian, \nbn: bengali, \nbs: bosnian, \nbg: bulgarian, \nca: catalan, \nceb: cebuano, \nny: chichewa, \nzh-cn: chinese (simplificado), \nzh-tw: chinese (tradicional), \nco: corsican, \nhr: croatian, \ncs: czech, \nda: danish, \nnl: dutch, \nen: english, \neo: esperanto, \net: estonian, \ntl: filipino, \nfi: finnish, \nfr: french, \nfy: frisian, \ngl: galician, \nka: georgian, \nde: german, \nel: greek, \ngu: gujarati, \nht: haitian creole, \nha: hausa, \nhaw: hawaiian, \niw: hebrew, \nhe: hebrew, \nhi: hindi, \nhmn: hmong, \nhu: hungarian, \nis: icelandic, \nig: igbo, \nid: indonesian, \nga: irish, \nit: italian, \nja: japanese, \njw: javanese, \nkn: kannada, \nkk: kazakh, \nkm: khmer, \nko: korean, \nku: kurdish (kurmanji)```', inline=True)
            commands.add_field(name=f'--------------------------------------------------------------------------', value=f'```\nky: kyrgyz, \nlo: lao, \nla: latin, \nlv: latvian, \nlt: lithuanian, \nlb: luxembourgish, \nmk: macedonian, \nmg: malagasy, \nms: malay, \nml: malayalam, \nmt: maltese, \nmi: maori, \nmr: marathi, \nmn: mongolian, \nmy: myanmar (burmese), \nne: nepali, \nno: norwegian, \nor: odia, \nps: pashto, \nfa: persian, \npl: polish, \npt: portuguese, \npa: punjabi, \nro: romanian, \nru: russian, \nsm: samoan, \ngd: scots gaelic, \nsr: serbian, \nst: sesotho, \nsn: shona, \nsd: sindhi, \nsi: sinhala, \nsk: slovak, \nsl: slovenian, \nso: somali, \nes: spanish, \nsu: sundanese, \nsw: swahili, \nsv: swedish, \ntg: tajik, \nta: tamil, \nte: telugu, \nth: thai, \ntr: turkish, \nuk: ukrainian, \nur: urdu, \nug: uyghur, \nuz: uzbek, \nvi: vietnamese, \ncy: welsh, \nxh: xhosa, \nyi: yiddish, \nyo: yoruba, \nzu: zulu```', inline=False)
            commands.set_footer(text=respuesta[4],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
            await ctx.send(embed=commands, delete_after=360.0)

def setup(bot: commands.Bot):
    bot.add_cog(help_commands(bot))
