import json
import random
import asyncio
import discord
import requests
from discord.ext import commands
import sys

import es
import en
sys.path.append('/Users/santi/Desktop/escritorio/mitsuri-bot/mitsuri_bot_oficial/commands')
import reactions

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

def lang_comprove(guild_id):
    with open("lang.json", "r") as f:
        guilds = json.load(f)
    if str(guild_id) in guilds:
        language = guilds[str(guild_id)]["lang"]
        return language
    else:
        return False

class reacction_commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def hi(self, ctx, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if mention == None:
                if lang == 'es':
                    img = es.hi(1, 0)
                elif lang == 'en':
                    img = en.hi(1, 0)
                data = img[0]
                embed = discord.Embed(title=f'{ctx.author.display_name} {img[1]}', color=ctx.author.color)
                embed.set_image(url=data)
                await ctx.send(embed=embed)
            else:
                user = str(mention)[:-5]
                autor = ctx.author.id
                autor = str(client.get_user(autor))
                if user == "Mitsuri":
                    if lang == 'es':
                        img = es.hi(2, 1)
                    elif lang == 'en':
                        img = en.hi(2, 1)
                    data = img[0]
                    embed = discord.Embed(title=f'{ctx.author.display_name} {img[1]}', color=ctx.author.color)
                    embed.set_image(url=data)
                elif user == autor[0:-5]:
                    if lang == 'es':
                        img = es.hi(2, 2)
                    elif lang == 'en':
                        img = es.hi(2, 2)
                    data = img[0]
                    embed = discord.Embed(title=f'{ctx.author.display_name} {img[1]} {ctx.author.display_name}¿¿??', color=ctx.author.color)
                    embed.set_image(url=data)
                else:
                    if lang == 'es':
                        img = es.hi(2, 3)
                    elif lang == 'en':
                        img = es.hi(2, 3)
                    data = img[0]
                    embed = discord.Embed(title=f'{ctx.author.display_name} {img[1]} {user}', color=ctx.author.color)
                    embed.set_image(url=data)
                await ctx.send(embed=embed)    
    
    @commands.command()
    async def poke(self, ctx, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if mention == None:
                if lang == 'es':
                    text = es.poke(1, 0)
                elif lang == 'en':
                    text = en.poke(1, 0)
                await ctx.send(text)
            else:
                response = requests.get("https://nekos.life/api/v2/img/poke")
                data = json.loads(response.content)
                data = data["url"]
                user = str(mention)[:-5]
                autor = ctx.author.id
                autor = str(client.get_user(autor))
                if user == "Mitsuri":
                    if lang == 'es':
                        text = es.poke(2, 1)
                    elif lang == 'en':
                        text = en.poke(2, 1)
                    embed = discord.Embed(title=f'{text[0]} {ctx.author.display_name} {text[1]}', color=ctx.author.color)
                    embed.set_image(url=data)
                elif user == autor[0:-5]:
                    if lang == 'es':
                        text = es.poke(2, 2)
                    elif lang == 'en':
                        text = en.poke(2, 2)
                    embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{ctx.author.display_name}**¿¿??', color=ctx.author.color)
                    embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
                else:
                    if lang == 'es':
                        text = es.poke(2, 3)
                    elif lang == 'en':
                        text = en.poke(2, 3)
                    embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{user}**', color=ctx.author.color)
                    embed.set_image(url=data)
                await ctx.send(embed=embed)
    
    @commands.command()
    async def kiss(self, ctx, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if mention == None:
                if lang == 'es':
                    text = es.kiss(1, 0)
                elif lang == 'en':
                    text = en.kiss(1, 0)
                await ctx.send(text)
                return
            numeroo = random.randint(1, 10)
            if numeroo <=3:
                response = requests.get("https://nekos.life/api/v2/img/kiss")
                data = json.loads(response.content)
                data = data["url"]
            else:
                r = requests.get(f'https://waifu.pics/api/sfw/kiss')
                if r.status_code == 200:
                    try:
                        img = json.loads(r.content)
                        data = img["url"]
                    except:
                        response = requests.get("https://nekos.life/api/v2/img/kiss")
                        data = json.loads(response.content)
                        data = data["url"]
                else:
                    response = requests.get("https://nekos.life/api/v2/img/kiss")
                    data = json.loads(response.content)
                    data = data["url"]
                    
            user = str(mention)[:-5]
            autor = ctx.author.id
            autor = str(client.get_user(autor))
            
            if user == "Mitsuri":
                if lang == 'es':
                    text = es.kiss(2, 1)
                elif lang == 'en':
                    text = en.kiss(2, 1)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
                embed.set_image(url=data)
            elif user == autor[0:-5]:
                if lang == 'es':
                    text = es.kiss(2, 2)
                elif lang == 'en':
                    text = en.kiss(2, 2)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{ctx.author.display_name}**¿¿??', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
            else:
                if lang == 'es':
                    text = es.kiss(2, 3)
                elif lang == 'en':
                    text = en.kiss(2, 3)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{user}**', color=ctx.author.color)
                embed.set_image(url=data)
            await ctx.send(embed=embed)
            
    @commands.command()
    async def slap(self, ctx, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            
            if mention == None:
                if lang == 'es':
                    text = es.slap(1, 0)
                elif lang == 'en':
                    text = en.slap(1, 0)
                await ctx.send(text)
                return
            response = requests.get("https://nekos.life/api/v2/img/slap")
            data = json.loads(response.content)
            data = data["url"]
            user = str(mention)[:-5]
            autor = ctx.author.id
            autor = str(client.get_user(autor))
            if user == "Mitsuri":
                if lang == 'es':
                    text = es.slap(2, 1)
                elif lang == 'en':
                    text = en.slap(2, 1)
                embed = discord.Embed(title=f'{text[0]} {ctx.author.display_name} {text[1]} {ctx.author.display_name}', color=ctx.author.color)
                embed.set_image(url=data)
            elif user == autor[0:-5]:
                if lang == 'es':
                    text = es.slap(2, 2)
                elif lang == 'en':
                    text = en.slap(2, 2)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{ctx.author.display_name}**¿¿??', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
            else:
                if lang == 'es':
                    text = es.slap(2, 3)
                elif lang == 'en':
                    text = en.slap(2, 3)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{user}**', color=ctx.author.color)
                embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def cuddle(self, ctx, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            
            if mention == None:
                if lang == 'es':
                    text = es.cuddle(1, 0)
                elif lang == 'en':
                    text = en.cuddle(1, 0)
                await ctx.send(text)
                return

            numeroo = random.randint(1, 10)
            if numeroo <=3:
                response = requests.get("https://nekos.life/api/v2/img/cuddle")
                data = json.loads(response.content)
                data = data["url"]
            else:
                r = requests.get(f'https://waifu.pics/api/sfw/cuddle')
                if r.status_code == 200:
                    try:
                        img = json.loads(r.content)
                        data = img["url"]
                    except:
                        response = requests.get("https://nekos.life/api/v2/img/cuddle")
                        data = json.loads(response.content)
                        data = data["url"]
                else:
                    response = requests.get("https://nekos.life/api/v2/img/cuddle")
                    data = json.loads(response.content)
                    data = data["url"]
                
            user = str(mention)[:-5]
            autor = ctx.author.id
            autor = str(client.get_user(autor))

            if user == "Mitsuri":
                if lang == 'es':
                    text = es.cuddle(2, 1)
                elif lang == 'en':
                    text = en.cuddle(2, 1)
                embed = discord.Embed(title=text, color=ctx.author.color)
                embed.set_image(url=data)
            elif user == autor[0:-5]:
                if lang == 'es':
                    text = es.cuddle(2, 2)
                elif lang == 'en':
                    text = en.cuddle(2, 2)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{ctx.author.display_name}**¿¿??', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
            else:
                if lang == 'es':
                    text = es.cuddle(2, 3)
                elif lang == 'en':
                    text = en.cuddle(2, 3)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{user}**', color=ctx.author.color)
                embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def hug(self, ctx, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            
            if mention == None:
                if lang == 'es':
                    text = es.hug(1, 0)
                elif lang == 'en':
                    text = en.hug(1, 0)
                await ctx.send(text)
                return
            numeroo = random.randint(1, 10)
            if numeroo <=3:
                response = requests.get("https://nekos.life/api/v2/img/hug")
                data = json.loads(response.content)
                data = data["url"]
            else:
                r = requests.get(f'https://waifu.pics/api/sfw/hug')
                if r.status_code == 200:
                    try:
                        img = json.loads(r.content)
                        data = img["url"]
                    except:
                        response = requests.get("https://nekos.life/api/v2/img/hug")
                        data = json.loads(response.content)
                        data = data["url"]
                else:
                    response = requests.get("https://nekos.life/api/v2/img/hug")
                    data = json.loads(response.content)
                    data = data["url"]
        
            user = str(mention)[:-5]
            autor = ctx.author.id
            autor = str(client.get_user(autor))
            if user == "Mitsuri":
                if lang == 'es':
                    text = es.hug(2, 1)
                elif lang == 'en':
                    text = en.hug(2, 1)
                embed = discord.Embed(title=f'{text[0]} {user} {text[1]} {ctx.author.display_name}', color=ctx.author.color)
                embed.set_image(url=data)
            elif user == autor[0:-5]:
                if lang == 'es':
                    text = es.hug(2, 2)
                elif lang == 'en':
                    text = en.hug(2, 2)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{ctx.author.display_name}**¿¿??', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
            else:
                if lang == 'es':
                    text = es.hug(2, 3)
                elif lang == 'en':
                    text = en.hug(2, 3)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{user}**', color=ctx.author.color)
                embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if mention == None:
                if lang == 'es':
                    text = es.pat(1, 0)
                elif lang == 'en':
                    text = en.pat(1, 0)
                await ctx.send(text)
                return
            response = requests.get("https://nekos.life/api/v2/img/pat")
            data = json.loads(response.content)
            data = data["url"]
            user = str(mention)[:-5]
            autor = ctx.author.id
            autor = str(client.get_user(autor))
            if user == "Mitsuri":
                if lang == 'es':
                    text = es.pat(2, 1)
                elif lang == 'en':
                    text = en.pat(2, 1)
                embed = discord.Embed(title=text, color=ctx.author.color)
                embed.set_image(url=data)
            elif user == autor[0:-5]:
                if lang == 'es':
                    text = es.pat(2, 2)
                elif lang == 'en':
                    text = en.pat(2, 2)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{ctx.author.display_name}**¿¿??', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
            else:
                if lang == 'es':
                    text = es.pat(2, 3)
                elif lang == 'en':
                    text = en.pat(2, 3)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{user}**', color=ctx.author.color)
                embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def baka(self, ctx, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            
            if mention == None:
                if lang == 'es':
                    text = es.baka(1, 0)
                elif lang == 'en':
                    text = en.baka(1, 0)
                await ctx.send(text)
                return
            response = requests.get("https://nekos.life/api/v2/img/baka")
            data = json.loads(response.content)
            data = data["url"]
            user = str(mention)[:-5]
            autor = ctx.author.id
            autor = str(client.get_user(autor))
            if user == "Mitsuri":
                if lang == 'es':
                    text = es.baka(2, 1)
                elif lang == 'en':
                    text = en.baka(2, 1)
                embed = discord.Embed(description=f'{text} **{ctx.author.display_name}**', color=ctx.author.color)
                embed.set_image(url=data)
            elif user == autor[0:-5]:
                if lang == 'es':
                    text = es.baka(2, 2)
                elif lang == 'en':
                    text = en.baka(2, 2)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
            else:
                if lang == 'es':
                    text = es.baka(2, 3)
                elif lang == 'en':
                    text = en.baka(2, 3)
                embed = discord.Embed(title=f'{user} {text}', color=ctx.author.color)
                embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def feed(self, ctx, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if mention == None:
                if lang == 'es':
                    text = es.feed(1, 0)
                if lang == 'en':
                    text = en.feed(1, 0)
                await ctx.send(text)
                return
            response = requests.get("https://nekos.life/api/v2/img/feed")
            data = json.loads(response.content)
            data = data["url"]
            user = str(mention)[:-5]
            autor = ctx.author.id
            autor = str(client.get_user(autor))
            if user == "Mitsuri":
                if lang == 'es':
                    text = es.feed(2, 1)
                if lang == 'en':
                    text = en.feed(2, 1)
                embed = discord.Embed(title=f'{text[0]} {ctx.author.display_name} {text[1]}', color=ctx.author.color)
                embed.set_image(url=data)
            elif user == autor[0:-5]:
                if lang == 'es':
                    text = es.feed(2, 2)
                if lang == 'en':
                    text = en.feed(2, 2)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{ctx.author.display_name}**¿¿??', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
            else:
                if lang == 'es':
                    text = es.feed(2, 3)
                if lang == 'en':
                    text = en.feed(2, 3)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{user}**', color=ctx.author.color)
                embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def tickle(self, ctx, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            
            if mention == None:
                if lang == 'es':
                    text = es.tickle(1, 0)
                elif lang == 'en':
                    text = en.tickle(1, 0)
                await ctx.send(text)
                return
            response = requests.get("https://nekos.life/api/v2/img/tickle")
            data = json.loads(response.content)
            data = data["url"]
            user = str(mention)[:-5]
            autor = ctx.author.id
            autor = str(client.get_user(autor))
            if user == "Mitsuri":
                if lang == 'es':
                    text = es.tickle(2, 1)
                elif lang == 'en':
                    text = en.tickle(2, 1)
                embed = discord.Embed(title=f'{text[0]} {ctx.author.display_name} {text[1]} {ctx.author.display_name}', color=ctx.author.color)
                embed.set_image(url=data)
            elif user == autor[0:-5]:
                if lang == 'es':
                    text = es.tickle(2, 2)
                elif lang == 'en':
                    text = en.tickle(2, 2)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{ctx.author.display_name}**¿¿??', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
            else:
                if lang == 'es':
                    text = es.tickle(2, 3)
                elif lang == 'en':
                    text = en.tickle(2, 3)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{user}**', color=ctx.author.color)
                embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def smug(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                text = es.smug()
            elif lang == 'en':
                text = en.smug()
            response = requests.get("https://nekos.life/api/v2/img/smug")
            data = json.loads(response.content)
            data = data["url"]
            embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
            embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def run(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                text = es.run()
            elif lang == 'en':
                text = en.run()
            data = reactions.runn()
            embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
            embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def dance(self, ctx, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            
            numeroo = random.randint(1, 10)
            if numeroo <= 4:
                data = reactions.dancee()
            else:
                r = requests.get(f'https://waifu.pics/api/sfw/dance')
                if r.status_code == 200:
                    try:
                        img = json.loads(r.content)
                        data = img["url"]
                    except:
                        data = reactions.dancee()
                else:
                    data = reactions.dancee()
            if mention == None:
                if lang == 'es':
                    text = es.dance(1, 0)
                elif lang == 'en':
                    text = en.dance(1, 0)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
                embed.set_image(url=data)
                await ctx.send(embed=embed)
            else:
                user = str(mention)[:-5]
                autor = ctx.author.id
                autor = str(client.get_user(autor))
                if user == "Mitsuri":
                    if lang == 'es':
                        text = es.dance(2, 1)
                    elif lang == 'en':
                        text = en.dance(2, 1)
                    embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
                    embed.set_image(url=data)
                elif user == autor[0:-5]:
                    if lang == 'es':
                        text = es.dance(2, 2)
                    elif lang == 'en':
                        text = en.dance(2, 2)
                    embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{ctx.author.display_name}**¿¿??', color=ctx.author.color)
                    embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
                else:
                    if lang == 'es':
                        text = es.dance(2, 3)
                    elif lang == 'en':
                        text = en.dance(2, 3)
                    embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{user}**', color=ctx.author.color)
                    embed.set_image(url=data)
                await ctx.send(embed=embed)

    @commands.command()
    async def angry(self, ctx, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            data = reactions.angryy()
            if mention == None:
                if lang == 'es':
                    text = es.angry(1, 0)
                elif lang == 'en':
                    text = en.angry(1, 0)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
                embed.set_image(url=data)
                await ctx.send(embed=embed)
            else:
                user = str(mention)[:-5]
                autor = ctx.author.id
                autor = str(client.get_user(autor))
                if user == "Mitsuri":
                    if lang == 'es':
                        text = es.angry(2, 1)
                    elif lang == 'en':
                        text = en.angry(2, 1)
                    embed = discord.Embed(description=f'{text} **{ctx.author.display_name}**', color=ctx.author.color)
                    embed.set_image(url=data)
                elif user == autor[0:-5]:
                    if lang == 'es':
                        text = es.angry(2, 2)
                    elif lang == 'en':
                        text = en.angry(2, 2)
                    embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{ctx.author.display_name}**¿¿??', color=ctx.author.color)
                    embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
                else:
                    if lang == 'es':
                        text = es.angry(2, 3)
                    elif lang == 'en':
                        text = en.angry(2, 3)
                    embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{user}**', color=ctx.author.color)
                    embed.set_image(url=data)
                await ctx.send(embed=embed)

    @commands.command()
    async def revive(self, ctx, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            
            if mention == None:
                if lang == 'es':
                    text = es.revive(1, 0)
                elif lang == 'en':
                    text = en.revive(1, 0)
                await ctx.send(text)
                return
            data = reactions.revivee()
            user = str(mention)[:-5]
            autor = ctx.author.id
            autor = str(client.get_user(autor))
            if user == "Mitsuri":
                if lang == 'es':
                    text = es.revive(2, 1)
                elif lang == 'en':
                    text = en.revive(2, 1)
                embed = discord.Embed(title=f'¿Qué? donde estoy, me han revividoo :D', color=ctx.author.color)
                embed.set_image(url=data)
            elif user == autor[0:-5]:
                if lang == 'es':
                    text = es.revive(2, 2)
                elif lang == 'en':
                    text = en.revive(2, 2)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{ctx.author.display_name}**¿¿??', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
            else:
                if lang == 'es':
                    text = es.revive(2, 3)
                elif lang == 'en':
                    text = es.revive(2, 3)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{user}**', color=ctx.author.color)
                embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def kill(self, ctx, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if mention == None:
                if lang == 'es':
                    text = es.kill(1, 0)
                elif lang == 'en':
                    text = en.kill(1, 0)
                await ctx.send(text)
                return
            data = reactions.killl()
            user = str(mention)[:-5]
            autor = ctx.author.id
            autor = str(client.get_user(autor))
            if user == "Mitsuri":
                if lang == 'es':
                    text = es.kill(2, 1)
                elif lang == 'en':
                    text = en.kill(2, 1)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
                embed.set_image(url=data)
            elif user == autor[0:-5]:
                if lang == 'es':
                    text = es.kill(2, 2)
                elif lang == 'en':
                    text = en.kill(2, 2)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{ctx.author.display_name}**¿¿??', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
            else:
                if lang == 'es':
                    text = es.kill(2, 3)
                elif lang == 'en':
                    text = en.kill(2, 3)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{user}**', color=ctx.author.color)
                embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def blush(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                text = es.blush()
            elif lang == 'en':
                text = en.blush()
            data = reactions.blushh()
            embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
            embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def happy(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                text = es.happy()
            elif lang == 'en':
                text = en.happy()
            data = reactions.happyy()
            embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
            embed.set_image(url=data)
            await ctx.send(embed=embed)            

    @commands.command()
    async def sad(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                text = es.sad()
            elif lang == 'en':
                text = en.sad()
            data = reactions.sadd()
            embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
            embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def laugh(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                text = es.laugh()
            elif lang == 'en':
                text = en.laugh()
            data = reactions.laughh()
            embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
            embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def cry(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            
            numeroo = random.randint(1, 10)
            if numeroo <=3:
                data = reactions.cryy()
            else:
                r = requests.get(f'https://waifu.pics/api/sfw/cry')
                if r.status_code == 200:
                    try:
                        img = json.loads(r.content)
                        data = img["url"]
                    except:
                        data = reactions.cryy()
                else:
                    data = reactions.cryy()
            if lang == 'es':
                text = es.cry()
            elif lang == 'en':
                text = en.cry()
            embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
            embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def confused(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                text = es.confused()
            elif lang == 'en':   
                text = en.confused() 
            data = reactions.confusedd()
            embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
            embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def bored(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                text = es.bored()
            elif lang == 'en':   
                text = en.bored()
            data = reactions.boredd()
            embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
            embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def fbi(self, ctx):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            data = reactions.fbii()
            embed = discord.Embed(title=f'FBIIII OPEN UP!!!', color=ctx.author.color)
            embed.set_image(url=data)
            await ctx.send(embed=embed)

    @commands.command()
    async def sleep(self, ctx, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            data = reactions.sleepp()
            if mention == None:
                if lang == 'es':
                    text = es.sleep(1, 0)
                elif lang == 'en':
                    text = en.sleep(1, 0)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
                embed.set_image(url=data)
                await ctx.send(embed=embed)
            else:
                user = str(mention)[:-5]
                autor = ctx.author.id
                autor = str(client.get_user(autor))
                if user == "Mitsuri":
                    if lang == 'es':
                        text = es.sleep(2, 1)
                    elif lang == 'en':
                        text = en.sleep(2, 1)
                    embed = discord.Embed(description=f'{text} **{ctx.author.display_name}**', color=ctx.author.color)
                    embed.set_image(url=data)
                elif user == autor[0:-5]:
                    if lang == 'es':
                        text = es.sleep(2, 2)
                    elif lang == 'en':
                        text = en.sleep(2, 2)
                    embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{ctx.author.display_name}**¿¿??', color=ctx.author.color)
                    embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
                else:
                    if lang == 'es':
                        text = es.sleep(2, 3)
                    elif lang == 'en':
                        text = en.sleep(2, 3)
                    embed = discord.Embed(description=f'**{ctx.author.display_name}** {text} **{user}**', color=ctx.author.color)
                    embed.set_image(url=data)
                await ctx.send(embed=embed) 

def setup(bot: commands.Bot):
    bot.add_cog(reacction_commands(bot))