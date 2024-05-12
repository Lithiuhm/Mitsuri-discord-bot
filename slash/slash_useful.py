
import json
import random
import asyncio
import discord
import requests
from discord.ext import commands
from translate import Translator
import sys
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_option, create_choice

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

invite = [
        create_option(
        name = "time",
        description = "how long do you want the invitation to last [IN SECONDS]",
        required = True,
        option_type = 4,
        ),
        create_option(
        name='uses',
        description = 'how many times do you want the invitation to be used',
        required = True,
        option_type = 3,
        )
]

invite2 = [
        create_option(
        name = "time",
        description = "how long do you want the invitation to last [IN SECONDS]",
        required = True,
        option_type = 4,
        ),
        create_option(
        name='uses',
        description = 'how many times do you want the invitation to be used',
        required = True,
        option_type = 3,
        )
]

optional = [
        create_option(
        name = "mention",
        description = "Mention a friend",
        required = False,
        option_type = 6,
        )
]

tr = [
        create_option(
        name = "from_lang",
        description = "language the message comes from",
        required = True,
        option_type = 3,
        ),
        create_option(
        name='to_lang',
        description = 'language to which you want to translate the message',
        required = True,
        option_type = 3,
        ),
        create_option(
        name='message',
        description = 'message you want to translate',
        required = True,
        option_type = 3,
        )
]

we = [
        create_option(
        name = "city",
        description = "city or country of which you want to know the weather",
        required = True,
        option_type = 3,
        )
]

bug = [
        create_option(
        name = "bug",
        description = "what error have you found?",
        required = True,
        option_type = 3,
        )
]

def lang_comprove(guild_id):
    with open("lang.json", "r") as f:
        guilds = json.load(f)
    if str(guild_id) in guilds:
        language = guilds[str(guild_id)]["lang"]
        return language
    else:
        return False

class useful_slash_commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @cog_ext.cog_slash(name = 'invite', description = 'If you want to invite the bot to your server use this command', guild_ids = [], options = [])
    async def invite(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                text = es.invite()
            elif lang == 'en':
                text = en.invite()
            embed = discord.Embed(color=ctx.author.color)
            embed.set_thumbnail(url='https://64.media.tumblr.com/d8841e84219ae53081bda00495cddb3d/5be347091e1ad9ec-55/s640x960/6141959d7cda3f3794d19a9bfffce0c088e19ca8.png')
            embed.add_field(name=text[0], value=text[1])
            embed.set_footer(text=f'{text[2]} {ctx.author.display_name}, {text[3]}')
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'avatar', description = 'Send the avatar of the tagged person or your avatar if you don\'t tag anyone', guild_ids = [], options = optional)
    async def avatar(self, ctx: SlashContext, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            
            if mention == None:
                if lang == 'es':
                    text = es.avatar(1)
                elif lang == 'en':
                    text = en.avatar(1)
                data = ctx.author.avatar_url
                embed = discord.Embed(title=f'{text} \n{ctx.author.display_name}', color=ctx.author.color)
                embed.set_image(url=data)
            else:
                data = mention.avatar_url
                user = str(mention)
                user = user[0:len(user)-5]
                if user == "Mitsuri":
                    if lang == 'es':
                        text = es.avatar(2)
                    elif lang == 'en':
                        text = en.avatar(2)
                    embed = discord.Embed(title=f'{text}', color=ctx.author.color)
                    embed.set_image(url=data)
                else:
                    if lang == 'es':
                        text = es.avatar(3)
                    elif lang == 'en':
                        text = en.avatar(3)
                    embed = discord.Embed(title=f'{text} \n{user}', color=ctx.author.color)
                    embed.set_image(url=data)
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'supser', description = 'Send a description about the official Mitsuri support servery', guild_ids = [], options = [])
    async def supser(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                text = es.supser()
                command = discord.Embed(color=ctx.author.color)
                command.set_thumbnail(url='https://images-ext-1.discordapp.net/external/uGbgNcfn1k1PfI_QYfmPiYtVYXaCFHYQRZvzh0iA4fM/%3Fsize%3D1024/https/cdn.discordapp.com/icons/777307542778544129/cfdbe25970b61da23f129ac90471d606.webp?width=665&height=665')
                command.add_field(name=text[0], value=text[1], inline=True)
                command.set_image(url='https://i.ibb.co/Htrj06r/tumblr-n2846ngduu1s8tpd7o1-500.gif')
                await ctx.send(embed=command)
            elif lang == 'en':
                command = discord.Embed(color=ctx.author.color)
                command.set_thumbnail(url='https://images-ext-1.discordapp.net/external/uGbgNcfn1k1PfI_QYfmPiYtVYXaCFHYQRZvzh0iA4fM/%3Fsize%3D1024/https/cdn.discordapp.com/icons/777307542778544129/cfdbe25970b61da23f129ac90471d606.webp?width=665&height=665')
                command.add_field(name='Mitsuri Official Support Server', value=f'Here I introduce you my support server\n What is inside the support server?\n\n------------->:heartpulse: Mitsuri Bot Oficial :heartpulse: <-------------\n-----------------------------------------------------------\nʚ∙Support in Spanish and English\nʚ∙Advertisements\nʚ∙Direct or Private Ticket\nʚ∙Bug Reports\nʚ∙Command Test\n-----------------------------------------------------------\n:incoming_envelope: Invitation / Invite :incoming_envelope:\n[Invitation to support server](https://discord.gg/dYMhtbq7Jr)\n\n:white_check_mark: ---->Votar/Vote<---- :white_check_mark:\n[Top.gg page to vote for Mitsuri](https://top.gg/bot/761359894791192596)\n-----------------------------------------------------------', inline=True)
                command.set_image(url='https://i.ibb.co/Htrj06r/tumblr-n2846ngduu1s8tpd7o1-500.gif')
                await ctx.send(embed=command)
   

    

    @cog_ext.cog_slash(name = 'tr', description = 'Translate a text from one language to another', guild_ids = [], options = tr)
    async def tr(self, ctx: SlashContext, from_lang=None, to_lang=None, message=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if from_lang == None:
                if lang == 'es':
                    text = es.tr(1)
                    await ctx.send(text)
                elif lang == 'en':
                    text = en.tr(1)
                    await ctx.send(text)
            elif to_lang == None:
                if lang == 'es':
                    text = es.tr(2)
                    await ctx.send(text)
                elif lang == 'en':
                    text = en.tr(2)
                    await ctx.send(text)
            elif message == None:
                if lang == 'es':
                    text = es.tr(3)
                    await ctx.send(text)
                elif lang == 'en':
                    text = en.tr(3)
                    await ctx.send(text)
            else:
                
                translator= Translator(from_lang=from_lang, to_lang=to_lang)
                translation = translator.translate(str(message))
                if "IS AN INVALID TARGET LANGUAGE" in translation:
                    if lang == 'es':
                        text = es.tr(4)
                        await ctx.send(text)
                    elif lang == 'en':
                        text = en.tr(4)
                        await ctx.send(text)
                else:
                    if lang == 'es':
                        text = es.tr(5)
                    elif lang == 'en':
                        text = en.tr(5)
                    embed = discord.Embed(title =text[0], color=ctx.author.color)
                    embed.add_field(name=text[1], value=f'{from_lang}', inline=True)
                    embed.add_field(name=text[2], value=f'{to_lang}', inline=True)
                    embed.add_field(name=text[3], value=f'```{message}```', inline=False)
                    embed.add_field(name=text[4], value=f'```{translation}```')
                    await ctx.send(embed=embed)    

    @cog_ext.cog_slash(name = 'we', description = 'Send detailed weather information in that place', guild_ids = [], options = we)
    async def we(self, ctx: SlashContext, city=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if city == None:
                if lang == 'es':
                    text = es.we(1)
                    await ctx.send(text)
                elif lang == 'en':
                    text = en.we(1)
                    await ctx.send(text)
            else:
                if lang == 'es':
                    r =  requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&')
                elif lang == 'en':
                    r =  requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&')
                if r.status_code == 200:
                    we = json.loads(r.content)
                    coor_lon = we["coord"]["lon"]
                    coor_lat = we["coord"]["lat"]
                    tiempo = we["weather"][0]["main"]
                    desc_tie = we["weather"][0]["description"]
                    temp = we["main"]["temp"]
                    sen = we["main"]["feels_like"]
                    mini = we["main"]["temp_min"]
                    maxi = we["main"]["temp_max"]
                    hum = we["main"]["humidity"]
                    wind = we["wind"]["speed"]
                    tzone = we["timezone"]
                    if lang == 'es':
                        text = es.we(2)
                    elif lang == 'en':
                        text = en.we(2)
                    embed = discord.Embed(title=f'{text[0]} {city}', color=ctx.author.color)
                    embed.set_thumbnail(url=f'{ctx.author.avatar_url}')
                    embed.add_field(name=f'{text[1]}', value=f'{text[2]} {coor_lon}º\n{text[3]} {coor_lat}º')
                    embed.add_field(name=f'{text[4]} {tiempo}', value=f'{text[5]} \n{desc_tie}')
                    embed.add_field(name=f'{text[6]}', value=f'{text[7]} {temp} {text[8]} {sen} {text[9]} {mini} {text[10]} {maxi} ºC')
                    embed.add_field(name=f'{text[11]}', value=f'{hum}%')
                    embed.add_field(name=f'{text[12]}', value=f'{wind}km/h')
                    embed.add_field(name=f'{text[13]}', value=f'{tzone}')
                    embed.set_footer(text=f'By openweathermap.org')
                    await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'bugrep', description = 'If you have a problem or have found a bug in Mitsuri send it to us', guild_ids = [], options = bug)
    async def bugrep(self, ctx: SlashContext, bug=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if bug == None:
                if lang == 'es':
                    text = es.bugrep(1)
                    await ctx.send(text)
                elif lang == 'en':
                    text = en.bugrep(1)
                    await ctx.send(text)
            else:
                if lang == 'es':
                    text = es.bugrep(2)
                elif lang == 'en':
                    text = en.bugrep(2)
                channel = client.get_channel(777666498927263795)
                user = str(client.get_user(ctx.author.id))
                embed = discord.Embed(color=ctx.author.color)
                embed.set_author(name=f'Reportó {ctx.author.display_name}')
                embed.set_thumbnail(url=f'{ctx.author.avatar_url}')
                embed.add_field(name='Nombre y tag:', value=f'{user}', inline=True)
                embed.add_field(name='ID:', value=f'{ctx.author.id}', inline=True)
                embed.add_field(name='mensaje:', value=f'```{bug}```', inline=False)
                command = discord.Embed(color=ctx.author.color)
                command.set_author(name=text[4])
                command.set_thumbnail(url=f'https://64.media.tumblr.com/8fac83ee7351cd6ac1c02587cbcac030/ec237f4a7d01db1a-22/s640x960/6a13f71d4812524d705130aa040dde8dea886d6b.jpg')
                command.add_field(name=text[5], value=text[6], inline=True)
                message = await ctx.send(embed=command)
                await message.add_reaction("✅")
                await message.add_reaction("❌")
                @client.event
                async def on_reaction_add(reaction, user):
                    if reaction.emoji == '✅' and user == ctx.author:
                        await message.delete()
                        if lang == 'es':
                            text = es.bugrep(3)
                        elif lang == 'en':
                            text = en.bugrep(3)
                        command2 = discord.Embed(color=ctx.author.color)
                        command2.set_author(name=text[0])
                        command2.set_thumbnail(url='https://64.media.tumblr.com/d8841e84219ae53081bda00495cddb3d/5be347091e1ad9ec-55/s640x960/6141959d7cda3f3794d19a9bfffce0c088e19ca8.png')
                        command2.add_field(name=text[1], value=text[2], inline=True)
                        await channel.send(embed=embed)
                        await ctx.send(embed=command2)
                    elif reaction.emoji == '❌' and user == ctx.author:
                        await message.delete()
                        if lang == 'es':
                            text = es.bugrep(4)
                        elif lang == 'en':
                            text = en.bugrep(4)
                        command2 = discord.Embed(color=ctx.author.color)
                        command2.set_author(name=text[0])
                        command2.set_thumbnail(url='https://64.media.tumblr.com/d8841e84219ae53081bda00495cddb3d/5be347091e1ad9ec-55/s640x960/6141959d7cda3f3794d19a9bfffce0c088e19ca8.png')
                        command2.add_field(name=text[1], value=text[2], inline=True)
                        command2.add_field(name=text[3], value=text[4], inline=False)
                        await ctx.send(embed=command2)

    

def setup(bot: commands.Bot):
    bot.add_cog(useful_slash_commands(bot))


