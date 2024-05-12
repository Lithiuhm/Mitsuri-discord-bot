import praw
import json
import random
import asyncio
import discord
import requests
from discord.ext import commands
import sys
from discord_slash import SlashCommand, SlashCommandOptionType, SlashContext, cog_ext
from discord_slash.utils.manage_commands import create_option, create_choice

import es
import en


def ran_walll():
    size_x = 0
    size_y = 0
    cont = 0
    si = 0
    r = requests.get(f'https://wall.alphacoders.com/api2.0/get.php?=random')
    while size_x < 1920 and size_y < 1080 or si != 1 or cont == 29:
        if r.status_code == 200:
            wall = json.loads(r.content)
            size_x = int(wall["wallpapers"][cont]["width"])
            size_y = int(wall["wallpapers"][cont]["height"])
            if size_x < 1920 and size_y < 1080:
                cont += 1
            else:
                data = wall["wallpapers"][cont]["url_image"]
                idd = wall["wallpapers"][cont]["id"]
                si = 1
    return (data,idd)
# ================================================================================================================
def get_gif(search_term):
    '''Esta funcion se usa para obtener un gif de la api de TENOR con un tag de búsqueda introducido por el
    usuario de discord o dado por nosotros, se comprueban las medidas del gif para ofrecer mejor calidad del gif
    y que no salga un gif enano'''
    size_x = 0
    size_y = 0
    while size_x <= 240 and size_y <= 210:
        r = requests.get(f'https://api.tenor.com/v1/random?q={search_term}&')
        if r.status_code == 200:
            top_8gifs = json.loads(r.content)

            #regular expresion inventada por santi para poder encontrar los gif sin usar json(json es más eficiente)     
            #regular = '\'gif\': {\'url\': \'https:\/\/media\.tenor\.com\/images\/[a0-z9]*\/tenor\.gif\''
            #x = re.findall(regular, str(top_8gifs))

            size_x = int(top_8gifs["results"][0]["media"][0]["gif"]["dims"][0])
            size_y = int(top_8gifs["results"][0]["media"][0]["gif"]["dims"][1])
            data = top_8gifs["results"][0]["media"][0]["gif"]["url"]
        else:
            top_8gifs = None
    return data

def lang_comprove(guild_id):
    with open("lang.json", "r") as f:
        guilds = json.load(f)
    if str(guild_id) in guilds:
        language = guilds[str(guild_id)]["lang"]
        return language
    else:
        return False

wallpaper = [
        create_option(
        name = "search",
        description = "What do you want to look for?",
        required = True,
        option_type = 3,
        )
]

wallpaper2 = [
        create_option(
        name = "search",
        description = "What do you want to look for?",
        required = True,
        option_type = 3,
        )
]

tenor = [
        create_option(
        name = "search",
        description = "What do you want to look for?",
        required = True,
        option_type = 3,
        )
]

ch = [
        create_option(
        name = "search",
        description = "Who are you looking for?",
        required = True,
        option_type = 3,
        )
]

class media_slash_commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @cog_ext.cog_slash(name = 'wallpaper', description = 'Sends the number of pages the doujin has entered', guild_ids = [], options = wallpaper)
    async def wallpaper(self, ctx: SlashContext,search=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if search == None:
                if lang == 'es':
                    text = es.wallpaper(1, 0)
                elif lang == 'en':
                    text = en.wallpaper(1, 0)
                await ctx.send(text)
            else:
                response = requests.get("https://wallhaven.cc/api/v1/search?q=" + search + "&categories=110&purity=100&sorting=random&order=desc%22")
                data = response.json()
                try: 
                    send = data['data'][0]['path']
                    if lang == 'es':
                        text = es.wallpaper(2, 1)
                    elif lang == 'en':
                        text = en.wallpaper(2, 1)
                    embed = discord.Embed(color=ctx.author.color)
                    embed.add_field(name=text[0], value=f'{text[1]} {search}')
                    embed.set_image(url=send)
                    embed.set_footer(text=text[2])
                    await ctx.send(embed=embed)
                except:
                    if lang == 'es':
                        text = es.wallpaper(2, 2)
                    elif lang == 'en':
                        text = en.wallpaper(2, 2)
                    await ctx.send(text)

    @cog_ext.cog_slash(name = 'dogo', description = 'Send a puppy', guild_ids = [], options = [])
    async def dogo(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            r = requests.get('https://shibe.online/api/shibes?count=1')
            y = r.json()
            if lang == 'es':
                text = es.dogo()
            elif lang == 'en':
                text = en.dogo()
            embed= discord.Embed(title=f'{text} {ctx.author.display_name}.',color=0xff80ff)
            embed.set_image(url=f'{y[0]}')
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'neko', description = 'Send a kitten', guild_ids = [], options = [])
    async def neko(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            r = requests.get('https://shibe.online/api/cats?count=1')
            y = r.json()
            if lang == 'es':
                text = es.neko()
            elif lang == 'en':
                text = en.neko()
            embed = discord.Embed(title=f'{text} {ctx.author.display_name}.',color=0xff80ff)
            embed.set_image(url=f'{y[0]}')
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'bird', description = 'Send a little bird', guild_ids = [], options = [])
    async def pajaro(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            r = requests.get('https://shibe.online/api/birds?count=1')
            y = r.json()
            if lang == 'es':
                text = es.bird()
            elif lang == 'en':
                text = en.bird()
            embed= discord.Embed(title=f'{text} {ctx.author.display_name}.',color=0xff80ff)
            embed.set_author(name=f'{ctx.author.display_name}',icon_url=f'{ctx.author.avatar_url}')
            embed.set_image(url=f'{y[0]}')
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'tenor', description = 'Send a random tenor gif of what you want to search', guild_ids = [], options = tenor)
    async def tenor(self, ctx: SlashContext,search=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if search == None:
                if lang == 'es':
                    text = es.tenor(1)
                    await ctx.send(text)
                elif lang == 'en':
                    text = en.tenor(1)
                    await ctx.send(text)
            else:
                data = get_gif(search)
                if lang == 'es':
                    text = es.tenor(2)
                elif lang == 'en':
                    text = en.tenor(2)
                embed = discord.Embed(color=ctx.author.color)
                embed.add_field(name=text[0], value=f'{text[1]} {search}')
                embed.set_image(url=data)
                embed.set_footer(text=text[2])
                await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'ran_wall', description = 'Send a random wallpaper', guild_ids = [], options = [])
    async def ran_wall(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            data = ran_walll()
            if lang == 'es':
                text = es.ran_wall()
            elif lang == 'en':
                text = en.ran_wall()
            embed = discord.Embed(color=ctx.author.color)
            embed.add_field(name=text[0], value=f'{text[1]} {data[1]}')
            embed.set_image(url=data[0])
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'en_meme', description = 'Send a meme in English from reddit', guild_ids = [], options = [])
    async def en_meme(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            r = requests.get('https://meme-api.herokuapp.com/gimme/1')
            if r.status_code == 200:
                meme = json.loads(r.content)
                data = meme["memes"][0]["url"]
                author = meme["memes"][0]["author"]
                title = meme["memes"][0]["title"]
                if lang == 'es':
                    text = es.en_meme()
                elif lang == 'en':
                    text = en.en_meme()
                embed = discord.Embed(color=ctx.author.color)
                embed.add_field(name=text[0], value=f'{text[1]}\n {title}')
                embed.set_image(url=data)
                embed.set_footer(text=f'{text[2]} {author}')
                await ctx.send(embed=embed)        

    @cog_ext.cog_slash(name = 'es_meme', description = 'Send a meme in Spanish from reddit', guild_ids = [], options = [])
    async def es_meme(self, ctx: SlashContext):
        reddit = praw.Reddit(client_id='rtbtnYDZFchysA', client_secret='DKFkPRRXABlJ9p0333oAvnaOx_yFeA', user_agent='Mozilla/5.0 (X11; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0')
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            se = ["SpanishMeme", "Divertido", "DankHispano", "MemesESP", "Memes_humor_video_ESP", "retrasadosporelmundo"]
            el = random.randint(0, len(se)-1)
            cosa = se[el]
            memes_submissions = reddit.subreddit(f'{cosa}').hot()
            post_to_pick = random.randint(1, 24)
            for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
            if lang == 'es':
                text = es.es_meme()
            elif lang == 'en':
                text = en.es_meme()
            embed = discord.Embed(color=ctx.author.color)
            embed.add_field(name=text[0], value=text[1])
            embed.set_image(url=submission.url)
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'wallpaper2', description = 'This command is set in case you cannot find a photo with mi!wallpaper command', guild_ids = [], options = wallpaper2)
    async def wallpaper2(self, ctx: SlashContext, search=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if search == None:
                if lang == 'es':
                    text = es.wallpaper2(1)
                    await ctx.send(text)
                elif lang == 'en':
                    text = en.wallpaper2(1)
                    await ctx.send(text)
            else:
                r =  requests.get(f'https://wall.alphacoders.com/api2.0/get.php?=search&term={search}')
                if r.status_code == 200:
                    wall = json.loads(r.content)
                    si = 0
                    response = str(wall)
                    if not "{'success': True, 'total_match': '0'}" in response:
                        while si == 0:
                            num = random.randint(0, 49)
                            try:
                                img = wall["wallpapers"][num]["url_image"]
                                si = 1
                            except:
                                si= 0
                    if lang == 'es':
                        text = es.wallpaper2(2)
                    elif lang == 'en':
                        text = en.wallpaper2(2)
                    try:
                        embed = discord.Embed(color=ctx.author.color)
                        embed.add_field(name=text[0], value=f'{text[1]} {search}')
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)
                    except:
                        if lang == 'es':
                            text = es.wallpaper2(3)
                            await ctx.send(text)
                        elif lang == 'en':
                            text = en.wallpaper2(3)
                            await ctx.send(text)
                else:
                    if lang == 'es':
                        text = es.wallpaper2(3)
                        await ctx.send(text)
                    elif lang == 'en':
                        text = en.wallpaper2(3)
                        await ctx.send(text)

    @cog_ext.cog_slash(name = 'ranwaifu', description = 'Send a random waifu', guild_ids = [], options = [])
    async def ranwaifu(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            r = requests.get(f'https://waifu.pics/api/sfw/waifu')
            if r.status_code == 200:
                data = json.loads(r.content)
                img = data["url"]
                if lang == 'es':
                    text = es.ranwaifu()
                elif lang == 'en':
                    text = en.ranwaifu()
                embed = discord.Embed(title=text,color=ctx.author.color)
                embed.set_author(name=f'{ctx.author.display_name}', icon_url=f'{ctx.author.avatar_url}')
                embed.set_image(url=img)
                await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'megumin', description = 'megumin', guild_ids = [], options = [])
    async def megumin(self, ctx: SlashContext):
        r = requests.get(f'https://waifu.pics/api/sfw/megumin')
        if r.status_code == 200:
            data = json.loads(r.content)
            img = data["url"]
            embed = discord.Embed(title='Megumiin >~<',color=ctx.author.color)
            embed.set_author(name=f'{ctx.author.display_name}', icon_url=f'{ctx.author.avatar_url}')
            embed.set_image(url=img)
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'ranneko', description = 'Send a random kawaii neko', guild_ids = [], options = [])
    async def ranneko(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            
            r = requests.get(f'https://waifu.pics/api/sfw/neko')
            if r.status_code == 200:
                data = json.loads(r.content)
                img = data["url"]
                if lang == 'es':
                    text = es.ranneko()
                elif lang == 'en':
                    text = en.ranneko()
                embed = discord.Embed(title=text,color=ctx.author.color)
                embed.set_author(name=f'{ctx.author.display_name}', icon_url=f'{ctx.author.avatar_url}')
                embed.set_image(url=img)
                await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'character', description = 'Send a photo of the character you chose!', guild_ids = [], options = ch)
    async def character(self, ctx: SlashContext,search=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                if search == None:
                    await ctx.send("Debes escribir el nombre del personaje que quieras buscar")
                    return
                else:
                    r = requests.get(f'https://api.jikan.moe/v3/search/character?q={search}')
                    if r.status_code == 200:
                        data = json.loads(r.content)
                        img = data["results"][0]["image_url"]
                        em = discord.Embed(title=f'Buscado {search}')
                        em.set_image(url=img)
                        await ctx.send(embed=em)
                    else:
                        await ctx.send("No se ha encontrado el personaje que buscas, revisa el nombre")
            elif lang == 'en':
                if search == None:
                    await ctx.send("You must write the name of the character you want to find")
                    return
                else:
                    r = requests.get(f'https://api.jikan.moe/v3/search/character?q={search}')
                    if r.status_code == 200:
                        data = json.loads(r.content)
                        img = data["results"][0]["image_url"]
                        em = discord.Embed(title=f'Searching {search}')
                        em.set_image(url=img)
                        await ctx.send(embed=em)
                    else:
                        await ctx.send("The character you are looking for has not been found, check the name")

def setup(bot: commands.Bot):
    bot.add_cog(media_slash_commands(bot))


