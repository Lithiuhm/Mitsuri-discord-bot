import json
import random
import asyncio
import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import sys
import re
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

def lang_comprove(guild_id):
    with open("lang.json", "r") as f:
        guilds = json.load(f)
    if str(guild_id) in guilds:
        language = guilds[str(guild_id)]["lang"]
        return language
    else:
        return False

def nhent_get(num, page):
    final_list = []
    html = requests.get("https://nhentai.net/g/" + str(num) + "/1/").text
    tags = ["lolicon", "bondage", "guro", "vore", "pig", "bestiality", "necrophilia", "scat", "loli", "shotacon", "ffm-threesome", "inchore", "hakuyagen"]
    if "lolicon" in html or "bondage" in html or "guro" in html or  "vore" in html or "pig" in html or "bestiality" in html or "necrophilia" in html or "scat" in html or "loli" in html or "shotacon" in html or "ffm-threesome" in html or "inchore" in html or "hakuyagen" in html:
        return False

    parsed_html = BeautifulSoup(html, 'html.parser')
    num_pages = parsed_html.body.find('span', attrs={'class':'num-pages'}).text
    
    if page == "num":
        return(num_pages)
    
    if page == "all":
        temp_html = requests.get("https://nhentai.net/g/" + str(num) + "/" + str(1) + "/").text
        temp_parsed_html = BeautifulSoup(temp_html, 'html.parser')
        temp_link = temp_parsed_html.find_all(src=re.compile("i.nhentai"))
        
        for image_url in temp_link:
            final_list.append(image_url.get('src'))
        img = final_list[0][:-5]
        typ = final_list[0][len(final_list[0])-4:]
        final = []
        for x in range(1, int(num_pages)+1):
            final += [img + str(x) + typ]
        return (final)
        
    else:
        for x in range(1, 2):
            temp_html = requests.get("https://nhentai.net/g/" + str(num) + "/" + str(page) + "/").text
            temp_parsed_html = BeautifulSoup(temp_html, 'html.parser')
            temp_link = temp_parsed_html.find_all(src=re.compile("i.nhentai"))
            #temp_img_list = str(temp_parsed_html.find('img', attrs={'height':'1823'}))
            #return re.findall('https://i.nhentai.net/galleries/[0-9]+/[0-9]+.[a-z]+', temp_img_list)
            for image_url in temp_link:
                final_list.append(image_url.get('src'))
        if final_list == []:
            return("[]")
        else:
            return(final_list)    
# ================================================================================================================
def nhent_how_many():
    '''Esta funcion se utiliza para saber cuantos doujins existen en total en la página de
    Nhentai'''
    #Gets the html in text
    html = requests.get("https://nhentai.net/").text

    #Parses html with the selected parser (it can also be lxml)
    parsed_html = BeautifulSoup(html, 'html.parser')
    
    #Gets the id from the last uploaded comic
    last_comic = parsed_html.body.find('div', attrs={'class':'container index-container'}).find('div', attrs={'class':'gallery'}).a.get('href')
    
    return last_comic[3:-1]

pages = [
        create_option(
        name = "code",
        description = "Enter a doujinshi number",
        required = True,
        option_type = 4,
        )
]

nhent_read = [
        create_option(
        name = "code",
        description = "Enter a doujinshi number",
        required = True,
        option_type = 4,
        ),
        create_option(
        name='page',
        description = 'number of the H you want to read',
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

obligatory = [
        create_option(
        name = "mention",
        description = "Mention a friend",
        required = True,
        option_type = 6,
        )
]

class nsfw_slash_commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @cog_ext.cog_slash(name = 'pages_of', description = 'Enter a doujinshi number', guild_ids = [], options = pages)
    async def pages_of(self, ctx: SlashContext, code : int=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if ctx.channel.is_nsfw():
                límite = int(nhent_how_many())
                if code == None:
                    if lang == "es":
                        text = es.pages_of(0)
                    elif lang == "en":
                        text = en.pages_of(0)
                    await ctx.send(text)
                elif code > límite:
                    if lang == "es":
                        text = es.pages_of(1)
                    elif lang == "en":
                        text = en.pages_of(1)
                    await ctx.send(f'{text[0]} {code} {text[1]} {límite} {text[2]}')
                else:
                    if lang == "es":
                        text = es.pages_of(2)
                    elif lang == "en":
                        text = en.pages_of(2)
                    page="num"
                    nhent_list = nhent_get(code, page)
                    await ctx.send(f'{text[0]} {code} {text[1]} {nhent_list} {text[2]}')
            else:
                if lang == "es":
                    text = es.pages_of(3)
                elif lang == "en":
                    text = en.pages_of(3)
                embed = discord.Embed(title=f'{text[0]} {ctx.author.display_name}... {text[1]}', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/8ad8fbfbc529f5a3f40b9d444608dd41/tenor.gif?itemid=14108808')
                await ctx.send(embed=embed, delete_after=10.0)

    @cog_ext.cog_slash(name = 'sauce_cont', description = 'Send the number of doujins that exist', guild_ids = [], options = [])
    async def sauce_cont(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if ctx.channel.is_nsfw():
                if lang == "es":
                    text = es.sauce_cont(1)
                elif lang == "en":
                    text = en.sauce_cont(1)
                await ctx.send(text[0] + nhent_how_many() + text[1])
            else:
                if lang == "es":
                    text = es.sauce_cont(2)
                elif lang == "en":
                    text = en.sauce_cont(2)
                embed = discord.Embed(title=f'{text[0]} {ctx.author.display_name}... {text[1]}', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/8ad8fbfbc529f5a3f40b9d444608dd41/tenor.gif?itemid=14108808')
                await ctx.send(embed=embed, delete_after=10.0)

    @cog_ext.cog_slash(name = 'nhentai_read', description = 'You can read the doujin you want, as long as it is in accordance with Discord\'s terms of service', guild_ids = [], options = nhent_read)
    async def nhentai_read(self, ctx: SlashContext, code : int=None, page=None): 
        page_num = 1
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if ctx.channel.is_nsfw():           
                if code == None:
                    if lang == "es":
                        text = es.nhentai_read(2)
                    elif lang == "en":
                        text = en.nhentai_read(2)
                    await ctx.send(text)
                elif page == None:
                    if lang == "es":
                        text = es.nhentai_read(1)
                    elif lang == "en":
                        text = en.nhentai_read(1)
                    await ctx.send(text)
                else:
                    límite = int(nhent_how_many())
                    if code > límite:
                        if lang == "es":
                            text = es.nhentai_read(3)
                        elif lang == "en":
                            text = en.nhentai_read(3)
                        await ctx.send(f'{text[0]} {code} {text[1]} {límite} {text[2]}')
                        return
                    if page == None and page != "all":
                        if lang == "es":
                            text = es.nhentai_read(4)
                        elif lang == "en":
                            text = en.nhentai_read(4)
                        await ctx.send(text)
                    else:
                        num = code
                        nhent_pages = nhent_get(num, page="num")
                        if nhent_pages == False:
                            if lang == "es":
                                text = es.nhentai_read(5)
                            elif lang == "en":
                                text = en.nhentai_read(5)
                            await ctx.send(text)
                            return
                        if page == "all":
                            if lang == "es":
                                text = es.nhentai_read(6)
                            elif lang == "en":
                                text = en.nhentai_read(6)
                            nhent_list = nhent_get(num, page="all")
                            embed = discord.Embed(title=f'{text[0]} {num}', description=f'{text[1]} {nhent_pages} {text[2]}', colour=discord.Color.purple())
                            embed.set_author(name=text[3])
                            embed.set_thumbnail(url=nhent_list[0])
                            embed.set_image(url=nhent_list[0])
                            mensage = await ctx.send(embed=embed)
                            message_id = mensage.id
                            if message_id == mensage.id:
                                await mensage.add_reaction("⏮")
                                await mensage.add_reaction("⬅️")
                                await mensage.add_reaction("➡️")
                                await mensage.add_reaction("⏭")
                                await mensage.add_reaction("❌")
                            message_id = mensage.id
                            def check(reaction, user):
                                return int(user.id) != 761359894791192596 and str(reaction.emoji) in ['⏮', '⬅️','➡️','⏭','❌']
                            try:
                                nhent_pages = nhent_get(num, page="num")
                                
                                while True:
                                    reaction, user = await self.bot.wait_for('reaction_add', timeout=180.0, check=check)                                
                                    message_idtemp = mensage.id
                                    if reaction.emoji == '⏭':
                                        if user.id != 761359894791192596: 
                                            if lang == "es":
                                                text = es.nhentai_read(7)
                                            elif lang == "en":
                                                text = en.nhentai_read(7)
                                        
                                            channel = reaction.message.channel
                                            if message_id == message_idtemp:
                                                
                                                page_num = int(nhent_pages)
                                                
                                                await mensage.remove_reaction("⏭", user)
                                                embed_temp = discord.Embed(title=f'{text[0]} {num}', description=f'{text[1]} {nhent_pages} {text[2]} {nhent_pages}', colour=discord.Color.purple())
                                                embed_temp.set_author(name=text[3])
                                                embed_temp.set_thumbnail(url=nhent_list[0])
                                                embed_temp.set_image(url=nhent_list[len(nhent_list)-1])
                                                await mensage.edit(embed=embed_temp)
                                            
                                    if reaction.emoji == '⏮':
                                        if user.id != 761359894791192596:
                                            channel = reaction.message.channel
                                            if message_id == message_idtemp:
                                                lista_react = 1
                                                page_num = 1
                                                if lang == "es":
                                                    text = es.nhentai_read(7)
                                                elif lang == "en":
                                                    text = en.nhentai_read(7)
                                                    
                                                await mensage.remove_reaction("⏮", user)
                                                embed_temp = discord.Embed(title=f'{text[0]} {num}', description=f'{text[1]} {nhent_pages} {text[2]} {lista_react}', colour=discord.Color.purple())
                                                embed_temp.set_author(name=text[3])
                                                embed_temp.set_thumbnail(url=nhent_list[0])
                                                embed_temp.set_image(url=nhent_list[0])
                                                await mensage.edit(embed=embed_temp)
                                            
                                    if reaction.emoji == '➡️':
                                        if user.id != 761359894791192596:
                                            channel = reaction.message.channel
                                            if message_id == message_idtemp:
                                                if page_num == int(nhent_pages):
                                                    page_num = int(nhent_pages)
                                                else:
                                                    page_num += 1
                                                if lang == "es":
                                                    text = es.nhentai_read(7)
                                                elif lang == "en":
                                                    text = en.nhentai_read(7)
                                                await mensage.remove_reaction("➡️", user)
                                                embed_temp = discord.Embed(title=f'{text[0]} {num}', description=f'{text[1]} {nhent_pages} {text[2]} {page_num}', colour=discord.Color.purple())
                                                embed_temp.set_author(name=text[3])
                                                embed_temp.set_thumbnail(url=nhent_list[0])
                                                embed_temp.set_image(url=nhent_list[page_num-1])
                                                
                                                await mensage.edit(embed=embed_temp)
                                        
                                            
                                    
                                    if reaction.emoji == '⬅️':
                                        if user.id != 761359894791192596:
                                            nhent_pages = nhent_get(num, page="num")
                                            
                                            channel = reaction.message.channel
                                            if message_id == message_idtemp:
                                                if page_num == 1:
                                                    page_num = 1
                                                else:
                                                    page_num -= 1
                                                if lang == "es":
                                                    text = es.nhentai_read(7)
                                                elif lang == "en":
                                                    text = en.nhentai_read(7)
                                                await mensage.remove_reaction("⬅️", user)
                                                embed_temp = discord.Embed(title=f'{text[0]} {num}', description=f'{text[1]} {nhent_pages} {text[2]} {page_num}', colour=discord.Color.purple())
                                                embed_temp.set_author(name=text[3])
                                                embed_temp.set_thumbnail(url=nhent_list[0])
                                                embed_temp.set_image(url=nhent_list[page_num-1])
                                                
                                                await mensage.edit(embed=embed_temp)
                                    
                                    if reaction.emoji == '❌':
                                        if user.id != 761359894791192596:
                                            channel = reaction.message.channel
                                            if message_id == message_idtemp:
                                                page_num = 1
                                                await mensage.remove_reaction("❌", user)
                                                await mensage.delete()
                            except asyncio.TimeoutError:
                                try: 
                                    await mensage.delete()
                                except:
                                    pass    
                            page_num = 0
                            await asyncio.sleep(600.0)
                            await mensage.delete()
                            
                        else:
                            nhent_list = nhent_get(code, page)
                            if nhent_list == "[]":
                                if lang == "es":
                                    text = es.nhentai_read(8)
                                elif lang == "en":
                                    text = en.nhentai_read(8)
                                pagina="num"
                                nhent_list = nhent_get(code, pagina)
                                await ctx.send(f'{text[0]} {page} {text[1]} {code}{text[2]} {nhent_list} {text[3]}')
                            else:
                                if lang == "es":
                                    text = es.nhentai_read(9)
                                elif lang == "en":
                                    text = en.nhentai_read(9)
                                num = code
                                embed = discord.Embed(title=f'{text[0]} {num}', description=f'{text[1]} {nhent_pages} {text[2]} {page}', colour=discord.Color.red())
                                embed.set_image(url=nhent_list[0])
                                mensage = await ctx.send(embed=embed)
            else:
                if lang == "es":
                    text = es.nhentai_read(10)
                elif lang == "en":
                    text = en.nhentai_read(10)
                embed = discord.Embed(title=f'{text[0]} {ctx.author.display_name}{text[1]}', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/8ad8fbfbc529f5a3f40b9d444608dd41/tenor.gif?itemid=14108808')
                await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'cum', description = 'You come in a person or alone', guild_ids = [], options = optional)
    async def cum(self, ctx: SlashContext, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if ctx.channel.is_nsfw():
                response = requests.get("https://nekos.life/api/v2/img/cum")
                data = json.loads(response.content)
                data = data["url"]
                user = str(mention)[:-5]
                autor = ctx.author.id
                autor = str(client.get_user(autor))
                if mention == None:   
                    if lang == 'es':
                        text = es.cum(1, 0)
                    elif lang == 'en':
                        text = en.cum(1, 0)
                    embed = discord.Embed(title=f'{ctx.author.display_name} {text}', color=ctx.author.color)
                    embed.set_image(url=data)
                elif user == "Mitsuri":
                    if lang == 'es':
                        text = es.cum(2, 1)
                    elif lang == 'en':
                        text = en.cum(2, 1)
                    embed = discord.Embed(title=f'{ctx.author.display_name} {text}', color=ctx.author.color)
                    embed.set_image(url='https://media1.tenor.com/images/9e72adcc75f042880c9d95af86ce69de/tenor.gif?itemid=18050703')
                elif user == autor[0:-5]:
                    if lang == 'es':
                        text = es.cum(2, 2)
                    elif lang == 'en':
                        text = en.cum(2, 2)
                    embed = discord.Embed(title=f'{ctx.author.display_name} {text} {ctx.author.display_name}¿¿??', color=ctx.author.color)
                    embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
                else:
                    if lang == 'es':
                        text = es.cum(2, 3)
                    elif lang == 'en':
                        text = en.cum(2, 3)
                    embed = discord.Embed(title=f'{ctx.author.display_name} {text} {user}', color=ctx.author.color)
                    embed.set_image(url=data)
                await ctx.send(embed=embed)
            else:
                if lang == "es":
                    text = es.nhentai_read(10)
                elif lang == "en":
                    text = en.nhentai_read(10)
                embed = discord.Embed(title=f'{text[0]} {ctx.author.display_name}{text[1]}', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/8ad8fbfbc529f5a3f40b9d444608dd41/tenor.gif?itemid=14108808')
                await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'kuni', description = 'lick your friend\'s member', guild_ids = [], options = obligatory)
    async def kuni(self, ctx: SlashContext, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if ctx.channel.is_nsfw():
                response = requests.get("https://nekos.life/api/v2/img/kuni")
                data = json.loads(response.content)
                data = data["url"]
                user = str(mention)[:-5]
                autor = ctx.author.id
                autor = str(client.get_user(autor))
                if mention == None:   
                    if lang == 'es':
                        text = es.kuni(1, 0)
                    elif lang == 'en':
                        text = en.kuni(1, 0)
                    await ctx.send(text)
                    return
                elif user == "Mitsuri":
                    if lang == 'es':
                        text = es.kuni(2, 1)
                    elif lang == 'en':
                        text = en.kuni(2, 1)
                    embed = discord.Embed(description=f'{ctx.author.display_name} {text}', color=ctx.author.color)
                    embed.set_image(url='https://media1.tenor.com/images/9e72adcc75f042880c9d95af86ce69de/tenor.gif?itemid=18050703')
                elif user == autor[0:-5]:
                    if lang == 'es':
                        text = es.kuni(2, 2)
                    elif lang == 'en':
                        text = en.kuni(2, 2)
                    embed = discord.Embed(title=f'{ctx.author.display_name} {text} {ctx.author.display_name}¿¿??', color=ctx.author.color)
                    embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
                else:
                    if lang == 'es':
                        text = es.kuni(2, 3)
                    elif lang == 'en':
                        text = en.kuni(2, 3)
                    embed = discord.Embed(title=f'{ctx.author.display_name} {text} {user}', color=ctx.author.color)
                    embed.set_image(url=data)
                await ctx.send(embed=embed)
            else:
                if lang == "es":
                    text = es.nhentai_read(10)
                elif lang == "en":
                    text = en.nhentai_read(10)
                embed = discord.Embed(title=f'{text[0]} {ctx.author.display_name}{text[1]}', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/8ad8fbfbc529f5a3f40b9d444608dd41/tenor.gif?itemid=14108808')
                await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'suck', description = 'lick your friend\'s member', guild_ids = [], options = obligatory)      
    async def suck(self, ctx: SlashContext, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if ctx.channel.is_nsfw():
                cosas = ["https://nekos.life/api/v2/img/bj", "https://nekos.life/api/v2/img/blowjob"]
                link = random.choice(cosas)
                response = requests.get(link)
                data = json.loads(response.content)
                data = data["url"]
                user = str(mention)[:-5]
                autor = ctx.author.id
                autor = str(client.get_user(autor))
                if mention == None:   
                    if lang == 'es':
                        text = es.suck(1, 0)
                    elif lang == 'en':
                        text = en.suck(1, 0)
                    await ctx.send(text)
                    return
                elif user == "Mitsuri":
                    if lang == 'es':
                        text = es.suck(2, 1)
                    elif lang == 'en':
                        text = en.suck(2, 1)
                    embed = discord.Embed(description=f'{ctx.author.display_name} {text}', color=ctx.author.color)
                    embed.set_image(url='https://media1.tenor.com/images/9e72adcc75f042880c9d95af86ce69de/tenor.gif?itemid=18050703')
                elif user == autor[0:-5]:
                    if lang == 'es':
                        text = es.suck(2, 2)
                    elif lang == 'en':
                        text = en.suck(2, 2)
                    embed = discord.Embed(title=f'{ctx.author.display_name} {text} {ctx.author.display_name}¿¿??', color=ctx.author.color)
                    embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
                else:
                    if lang == 'es':
                        text = es.suck(2, 3)
                    elif lang == 'en':
                        text = en.suck(2, 3)
                    embed = discord.Embed(title=f'{ctx.author.display_name} {text} {user}', color=ctx.author.color)
                    embed.set_image(url=data)
                await ctx.send(embed=embed)
            else:
                if lang == "es":
                    text = es.nhentai_read(10)
                elif lang == "en":
                    text = en.nhentai_read(10)
                embed = discord.Embed(title=f'{text[0]} {ctx.author.display_name}{text[1]}', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/8ad8fbfbc529f5a3f40b9d444608dd41/tenor.gif?itemid=14108808')
                await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'anal', description = 'give your friend an anal', guild_ids = [], options = obligatory)      
    async def anal(self, ctx: SlashContext, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if ctx.channel.is_nsfw():
                response = requests.get("https://nekos.life/api/v2/img/anal")
                data = json.loads(response.content)
                data = data["url"]
                user = str(mention)[:-5]
                autor = ctx.author.id
                autor = str(client.get_user(autor))
                if mention == None:   
                    if lang == 'es':
                        text = es.anal(1, 0)
                    elif lang == 'en':
                        text = en.anal(1, 0)
                    await ctx.send(text)
                    return
                elif user == "Mitsuri":
                    if lang == 'es':
                        text = es.anal(2, 1)
                    elif lang == 'en':
                        text = en.anal(2, 1)
                    embed = discord.Embed(description=f'{ctx.author.display_name} {text}', color=ctx.author.color)
                    embed.set_image(url='https://media1.tenor.com/images/9e72adcc75f042880c9d95af86ce69de/tenor.gif?itemid=18050703')
                elif user == autor[0:-5]:
                    if lang == 'es':
                        text = es.anal(2, 2)
                    elif lang == 'en':
                        text = en.anal(2, 2)
                    embed = discord.Embed(title=f'{ctx.author.display_name} {text} {ctx.author.display_name}¿¿??', color=ctx.author.color)
                    embed.set_image(url='https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411')
                else:
                    if lang == 'es':
                        text = es.anal(2, 3)
                    elif lang == 'en':
                        text = en.anal(2, 3)
                    embed = discord.Embed(title=f'{ctx.author.display_name} {text} {user}', color=ctx.author.color)
                    embed.set_image(url=data)
                await ctx.send(embed=embed)
            else:
                if lang == "es":
                    text = es.nhentai_read(10)
                elif lang == "en":
                    text = en.nhentai_read(10)
                embed = discord.Embed(title=f'{text[0]} {ctx.author.display_name}{text[1]}', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/8ad8fbfbc529f5a3f40b9d444608dd41/tenor.gif?itemid=14108808')
                await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'masturb', description = 'masturbate all you want', guild_ids = [], options = [])
    async def masturb(self, ctx: SlashContext, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if ctx.channel.is_nsfw():
                response = requests.get("https://nekos.life/api/v2/img/pwankg")
                data = json.loads(response.content)
                data = data["url"]
                user = str(mention)[:-5]
                autor = ctx.author.id
                autor = str(client.get_user(autor))
                if lang == 'es':
                    text = es.masturb(1, 0)
                elif lang == 'en':
                    text = en.masturb(1, 0)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
                embed.set_image(url=data)
                await ctx.send(embed=embed)
            else:
                if lang == "es":
                    text = es.nhentai_read(10)
                elif lang == "en":
                    text = en.nhentai_read(10)
                embed = discord.Embed(title=f'{text[0]} {ctx.author.display_name}{text[1]}', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/8ad8fbfbc529f5a3f40b9d444608dd41/tenor.gif?itemid=14108808')
                await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'feets', description = 'enjoy a good pair of feet', guild_ids = [], options = [])
    async def feets(self, ctx: SlashContext, mention : discord.Member=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if ctx.channel.is_nsfw():
                response = requests.get("https://nekos.life/api/v2/img/erofeet")
                data = json.loads(response.content)
                data = data["url"]
                user = str(mention)[:-5]
                autor = ctx.author.id
                autor = str(client.get_user(autor))
                if lang == 'es':
                    text = es.feets(1, 0)
                elif lang == 'en':
                    text = en.feets(1, 0)
                embed = discord.Embed(description=f'**{ctx.author.display_name}** {text}', color=ctx.author.color)
                embed.set_image(url=data)
                await ctx.send(embed=embed)
            else:
                if lang == "es":
                    text = es.nhentai_read(10)
                elif lang == "en":
                    text = en.nhentai_read(10)
                embed = discord.Embed(title=f'{text[0]} {ctx.author.display_name}{text[1]}', color=ctx.author.color)
                embed.set_image(url='https://media1.tenor.com/images/8ad8fbfbc529f5a3f40b9d444608dd41/tenor.gif?itemid=14108808')
                await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(nsfw_slash_commands(bot))