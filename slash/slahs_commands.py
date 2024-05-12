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
import time
import praw
import requests
from bs4 import BeautifulSoup
import re
import reactions
from translate import Translator

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
        option_type = 4,
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
        required = False,
        option_type = 6,
        )
]

bug = [
        create_option(
        name = "bug",
        description = "what error have you found?",
        required = False,
        option_type = 6,
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

wallpaper = [
        create_option(
        name = "search",
        description = "What do you want to look for?",
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

help_ = [
        create_option(
        name = "help_",
        description = "Show bot commands",
        required = True,
        option_type = 3,
        choices=[
            create_choice(
                name = "Main information",
                value = "main"
            ),
            create_choice(
                name = "information commands",
                value = "info"
            ),
            create_choice(
                name = "nsfw commands",
                value = "nsfw"
            ),
            create_choice(
                name = "useful commands",
                value = "useful"
            ),
            create_choice(
                name = "read commands",
                value = "read"
            ),
            create_choice(
                name = "games commands",
                value = "games"
            ),
            create_choice(
                name = "music commands",
                value = "music"
            ),
            create_choice(
                name = "media commands",
                value = "media"
            ),
            create_choice(
                name = "reactions commands",
                value = "reacts"
            ),
            create_choice(
                name = "moderation commands",
                value = "moder"
            ),
            create_choice(
                name = "traslate languages",
                value = "traslate"
            )
        
        ]
        )
]

comandos = [
        create_option(
        name = "commands",
        description = "Show all bot commands",
        required = True,
        option_type = 3,
        choices=[
            create_choice(
                name = "send to DM",
                value = "dm"
            ),
            create_choice(
                name = "send to current channel",
                value = "channel"
            )
        ]
        )
]


_8ball = [
        create_option(
        name = "question",
        description = "Ask Mitsuri a question",
        required = True,
        option_type = 3,
        )
]

yon = [
        create_option(
        name = "question",
        description = "Ask Mitsuri a question",
        required = True,
        option_type = 3,
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

class slash_slash_commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @cog_ext.cog_slash(name = 'coin', description = 'flip a coin', guild_ids = [696831427882254346])
    async def moneda(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            side = random.randint(1,100)
            if side == 50 or side > 50:
                coin = 1
            if side < 50:
                coin = 2
            if coin == 1:
                if lang == 'es':
                    respuesta = es.moneda(1)
                    em = discord.Embed(title=f'{ctx.author.display_name} \n{respuesta[0]}', description=respuesta[1], color=random.randint(0, 16777215))
                    await ctx.send(embed=em)
                elif lang == 'en':
                    respuesta = en.moneda(1)
                    em = discord.Embed(title=f'{ctx.author.display_name} \n{respuesta[0]}', description=respuesta[1], color=random.randint(0, 16777215))
                    await ctx.send(embed=em)
            elif coin == 2:
                if lang == 'es':
                    respuesta = es.moneda(2)
                    em = discord.Embed(title=f'{ctx.author.display_name} \n{respuesta[0]}', description=respuesta[1], color=random.randint(0, 16777215))
                    await ctx.send(embed=em)
                elif lang == 'en':
                    respuesta = en.moneda(2)
                    em = discord.Embed(title=f'{ctx.author.display_name} \n{respuesta[0]}', description=respuesta[1], color=random.randint(0, 16777215))
                    await ctx.send(embed=em)
    
    @cog_ext.cog_slash(name = '8ball', description = 'Ask Mitsuri a question', guild_ids = [696831427882254346], options = _8ball)
    async def _8ball(self, ctx: SlashContext, question = None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                if question == None:
                    respuesta = es._8ball(1, "a")
                    await ctx.send(respuesta)
                else:
                    respuesta = es._8ball(2, question)
                    await ctx.send(respuesta)
            elif lang == 'en':
                if question == None:
                    respuesta = en._8ball(1, "a")
                    await ctx.send(respuesta)
                else:
                    respuesta = en._8ball(2, question)
                    await ctx.send(respuesta)

    @cog_ext.cog_slash(name = 'yon', description = 'Ask Mitsuri a question', guild_ids = [696831427882254346], options = yon)
    async def yon(self, ctx: SlashContext, question=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                if question == None:
                    text = es.yon(1, "a")
                    await ctx.send(text)
                else:
                    respuesta = es.yon(2, question)
                    await ctx.send(respuesta)
            elif lang == 'en':
                if question == None:
                    text = en.yon(1, "a")
                    await ctx.send(text)
                else:
                    respuesta = en.yon(2, question)
                    await ctx.send(respuesta)

    @cog_ext.cog_slash(name = 'dice', description = 'You roll a 6-sided dice', guild_ids = [696831427882254346])
    async def dado(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                respuesta = es.dado()
                await ctx.send(respuesta)
            elif lang == 'en':
                respuesta = en.dado()
                await ctx.send(respuesta)

    @cog_ext.cog_slash(name = 'connect4', description = 'Ask Mitsuri a question', guild_ids = [696831427882254346], options = obligatory)
    async def connect4(self, ctx: SlashContext, mention : discord.User=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if lang == 'es':
                respuesta = es.connect4()
            elif lang == 'en':
                respuesta = en.connect4()
        client.red = '🔴'
        client.yellow = ':yellow_circle:'
        client.white = '⚪'

        client.grille = [[client.white,client.white,client.white,client.white,client.white,client.white,client.white],
                        [client.white,client.white,client.white,client.white,client.white,client.white,client.white],
                        [client.white,client.white,client.white,client.white,client.white,client.white,client.white],
                        [client.white,client.white,client.white,client.white,client.white,client.white,client.white],
                        [client.white,client.white,client.white,client.white,client.white,client.white,client.white],
                        [client.white,client.white,client.white,client.white,client.white,client.white,client.white]]

        tab0 = "".join(client.grille[0])
        tab1 = "".join(client.grille[1])
        tab2 = "".join(client.grille[2])
        tab3 = "".join(client.grille[3])
        tab4 = "".join(client.grille[4])
        tab5 = "".join(client.grille[5])

        tabcomplet = tab0 + "\n" + tab1 + "\n" + tab2 + "\n" + tab3 + "\n" + tab4 + "\n" + tab5

        jaune = ctx.message.author
        
        if mention is None :
            embedsolo = discord.Embed(description = respuesta[0], 
                                    colour = discord.Colour.dark_orange())

            jeusolo = await ctx.message.channel.send(embed = embedsolo)

            await asyncio.sleep(5)

            await ctx.message.delete()
            await jeusolo.delete()

        
        else:

            embedstartgame = discord.Embed(description = f"<@{mention.id}> \n<@{jaune.id}> {respuesta[1]}", 
                                            colour = discord.Colour.blurple())

            rep = await ctx.message.channel.send(embed = embedstartgame)
            await rep.add_reaction('✅')
        
        def check(reaction, user):
            return user == mention and str(reaction.emoji) == '✅'

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=30.0, check=check)

        except asyncio.TimeoutError:

            embedrefused = discord.Embed(description = respuesta[2], 
                                        colour = discord.Colour.dark_blue())

            await ctx.message.delete()
            await rep.edit(embed = embedrefused)
            await rep.clear_reactions()

            await asyncio.sleep(5)

            await rep.delete()
            return

        else:
            embedjeu = discord.Embed(description = f"{respuesta[3]} <@{jaune.id}>\n<@{jaune.id}> {respuesta[4]}",
                                    colour = 0x050087)

            embedjoueurs = discord.Embed(description = f"{client.yellow} <@{jaune.id}>\n{client.red} <@{mention.id}>", 
                                    colour =0x050087)

            await ctx.message.delete()
            await rep.edit(embed = embedjeu)
            await rep.clear_reactions()
            tab = await ctx.message.channel.send(respuesta[5])

            await asyncio.sleep(5)

            await rep.edit(embed = embedjoueurs)
            await tab.edit(content = f"{tabcomplet}")

            for t in range (42):

                if t %2 == 0:

                    embedjeujaune = discord.Embed(description = f"{client.yellow} {respuesta[6]} <@{jaune.id}>\n{client.red} {respuesta[7]} <@{mention.id}>", 
                                                colour =0xFFFF00)

                    await rep.edit(embed = embedjeujaune)

                    if (client.grille[0][0]) == client.white:
                        await tab.add_reaction('1⃣')
                    if (client.grille[0][1]) == client.white:
                        await tab.add_reaction('2⃣')
                    if (client.grille[0][2]) == client.white:
                        await tab.add_reaction('3⃣')
                    if (client.grille[0][3]) == client.white:
                        await tab.add_reaction('4⃣')
                    if (client.grille[0][4]) == client.white:
                        await tab.add_reaction('5⃣')
                    if (client.grille[0][5]) == client.white:
                        await tab.add_reaction('6⃣')
                    if (client.grille[0][6]) == client.white:
                        await tab.add_reaction('7⃣')

                    def checkjaune1(reaction, user):
                        return user == jaune and ((str(reaction.emoji) == '1⃣') or (str(reaction.emoji) == '2⃣') or (str(reaction.emoji) == '3⃣') or (str(reaction.emoji) == '4⃣') or (str(reaction.emoji) == '5⃣') or (str(reaction.emoji) == '6⃣') or (str(reaction.emoji) == '7⃣'))

                    reaction, user = await self.bot.wait_for('reaction_add', check=checkjaune1)
                    if user.id != 761359894791192596:
                        if (str(reaction.emoji) == '1⃣'):

                            if (client.grille[5][0]) == client.white:
                                client.grille[5][0] = client.yellow
                                tableau0 = "".join(client.grille[0])
                                tableau1 = "".join(client.grille[1])
                                tableau2 = "".join(client.grille[2])
                                tableau3 = "".join(client.grille[3])
                                tableau4 = "".join(client.grille[4])
                                tableau5 = "".join(client.grille[5])
                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                await tab.edit(content = f"{tableaucomplet}")
                            
                            else:
                                if (client.grille[4][0]) == client.white:
                                    client.grille[4][0] = client.yellow
                                    tableau0 = "".join(client.grille[0])
                                    tableau1 = "".join(client.grille[1])
                                    tableau2 = "".join(client.grille[2])
                                    tableau3 = "".join(client.grille[3])
                                    tableau4 = "".join(client.grille[4])
                                    tableau5 = "".join(client.grille[5])
                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                    await tab.edit(content = f"{tableaucomplet}")
                                
                                else:
                                    if (client.grille[3][0]) == client.white:
                                        client.grille[3][0] = client.yellow
                                        tableau0 = "".join(client.grille[0])
                                        tableau1 = "".join(client.grille[1])
                                        tableau2 = "".join(client.grille[2])
                                        tableau3 = "".join(client.grille[3])
                                        tableau4 = "".join(client.grille[4])
                                        tableau5 = "".join(client.grille[5])
                                        tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                        await tab.edit(content = f"{tableaucomplet}")

                                    else:
                                        if (client.grille[2][0]) == client.white:
                                            client.grille[2][0] = client.yellow
                                            tableau0 = "".join(client.grille[0])
                                            tableau1 = "".join(client.grille[1])
                                            tableau2 = "".join(client.grille[2])
                                            tableau3 = "".join(client.grille[3])
                                            tableau4 = "".join(client.grille[4])
                                            tableau5 = "".join(client.grille[5])
                                            tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                            await tab.edit(content = f"{tableaucomplet}")
                                        
                                        else:
                                            if (client.grille[1][0]) == client.white:
                                                client.grille[1][0] = client.yellow
                                                tableau0 = "".join(client.grille[0])
                                                tableau1 = "".join(client.grille[1])
                                                tableau2 = "".join(client.grille[2])
                                                tableau3 = "".join(client.grille[3])
                                                tableau4 = "".join(client.grille[4])
                                                tableau5 = "".join(client.grille[5])
                                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                await tab.edit(content = f"{tableaucomplet}")
                                            
                                            else:
                                                if (client.grille[0][0]) == client.white:
                                                    client.grille[0][0] = client.yellow
                                                    tableau0 = "".join(client.grille[0])
                                                    tableau1 = "".join(client.grille[1])
                                                    tableau2 = "".join(client.grille[2])
                                                    tableau3 = "".join(client.grille[3])
                                                    tableau4 = "".join(client.grille[4])
                                                    tableau5 = "".join(client.grille[5])
                                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                    await tab.edit(content = f"{tableaucomplet}")

                        elif (str(reaction.emoji) == '2⃣'):

                            if (client.grille[5][1]) == client.white:
                                client.grille[5][1] = client.yellow
                                tableau0 = "".join(client.grille[0])
                                tableau1 = "".join(client.grille[1])
                                tableau2 = "".join(client.grille[2])
                                tableau3 = "".join(client.grille[3])
                                tableau4 = "".join(client.grille[4])
                                tableau5 = "".join(client.grille[5])
                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                await tab.edit(content = f"{tableaucomplet}")
                            
                            else:
                                if (client.grille[4][1]) == client.white:
                                    client.grille[4][1] = client.yellow
                                    tableau0 = "".join(client.grille[0])
                                    tableau1 = "".join(client.grille[1])
                                    tableau2 = "".join(client.grille[2])
                                    tableau3 = "".join(client.grille[3])
                                    tableau4 = "".join(client.grille[4])
                                    tableau5 = "".join(client.grille[5])
                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                    await tab.edit(content = f"{tableaucomplet}")
                                
                                else:
                                    if (client.grille[3][1]) == client.white:
                                        client.grille[3][1] = client.yellow
                                        tableau0 = "".join(client.grille[0])
                                        tableau1 = "".join(client.grille[1])
                                        tableau2 = "".join(client.grille[2])
                                        tableau3 = "".join(client.grille[3])
                                        tableau4 = "".join(client.grille[4])
                                        tableau5 = "".join(client.grille[5])
                                        tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                        await tab.edit(content = f"{tableaucomplet}")

                                    else:
                                        if (client.grille[2][1]) == client.white:
                                            client.grille[2][1] = client.yellow
                                            tableau0 = "".join(client.grille[0])
                                            tableau1 = "".join(client.grille[1])
                                            tableau2 = "".join(client.grille[2])
                                            tableau3 = "".join(client.grille[3])
                                            tableau4 = "".join(client.grille[4])
                                            tableau5 = "".join(client.grille[5])
                                            tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                            await tab.edit(content = f"{tableaucomplet}")
                                        
                                        else:
                                            if (client.grille[1][1]) == client.white:
                                                client.grille[1][1] = client.yellow
                                                tableau0 = "".join(client.grille[0])
                                                tableau1 = "".join(client.grille[1])
                                                tableau2 = "".join(client.grille[2])
                                                tableau3 = "".join(client.grille[3])
                                                tableau4 = "".join(client.grille[4])
                                                tableau5 = "".join(client.grille[5])
                                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                await tab.edit(content = f"{tableaucomplet}")
                                            
                                            else:
                                                if (client.grille[0][1]) == client.white:
                                                    client.grille[0][1] = client.yellow
                                                    tableau0 = "".join(client.grille[0])
                                                    tableau1 = "".join(client.grille[1])
                                                    tableau2 = "".join(client.grille[2])
                                                    tableau3 = "".join(client.grille[3])
                                                    tableau4 = "".join(client.grille[4])
                                                    tableau5 = "".join(client.grille[5])
                                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                    await tab.edit(content = f"{tableaucomplet}")
                                        
                        elif (str(reaction.emoji) == '3⃣'):

                            if (client.grille[5][2]) == client.white:
                                client.grille[5][2] = client.yellow
                                tableau0 = "".join(client.grille[0])
                                tableau1 = "".join(client.grille[1])
                                tableau2 = "".join(client.grille[2])
                                tableau3 = "".join(client.grille[3])
                                tableau4 = "".join(client.grille[4])
                                tableau5 = "".join(client.grille[5])
                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                await tab.edit(content = f"{tableaucomplet}")
                            
                            else:
                                if (client.grille[4][2]) == client.white:
                                    client.grille[4][2] = client.yellow
                                    tableau0 = "".join(client.grille[0])
                                    tableau1 = "".join(client.grille[1])
                                    tableau2 = "".join(client.grille[2])
                                    tableau3 = "".join(client.grille[3])
                                    tableau4 = "".join(client.grille[4])
                                    tableau5 = "".join(client.grille[5])
                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                    await tab.edit(content = f"{tableaucomplet}")
                                
                                else:
                                    if (client.grille[3][2]) == client.white:
                                        client.grille[3][2] = client.yellow
                                        tableau0 = "".join(client.grille[0])
                                        tableau1 = "".join(client.grille[1])
                                        tableau2 = "".join(client.grille[2])
                                        tableau3 = "".join(client.grille[3])
                                        tableau4 = "".join(client.grille[4])
                                        tableau5 = "".join(client.grille[5])
                                        tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                        await tab.edit(content = f"{tableaucomplet}")

                                    else:
                                        if (client.grille[2][2]) == client.white:
                                            client.grille[2][2] = client.yellow
                                            tableau0 = "".join(client.grille[0])
                                            tableau1 = "".join(client.grille[1])
                                            tableau2 = "".join(client.grille[2])
                                            tableau3 = "".join(client.grille[3])
                                            tableau4 = "".join(client.grille[4])
                                            tableau5 = "".join(client.grille[5])
                                            tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                            await tab.edit(content = f"{tableaucomplet}")
                                        
                                        else:
                                            if (client.grille[1][2]) == client.white:
                                                client.grille[1][2] = client.yellow
                                                tableau0 = "".join(client.grille[0])
                                                tableau1 = "".join(client.grille[1])
                                                tableau2 = "".join(client.grille[2])
                                                tableau3 = "".join(client.grille[3])
                                                tableau4 = "".join(client.grille[4])
                                                tableau5 = "".join(client.grille[5])
                                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                await tab.edit(content = f"{tableaucomplet}")
                                            
                                            else:
                                                if (client.grille[0][2]) == client.white:
                                                    client.grille[0][2] = client.yellow
                                                    tableau0 = "".join(client.grille[0])
                                                    tableau1 = "".join(client.grille[1])
                                                    tableau2 = "".join(client.grille[2])
                                                    tableau3 = "".join(client.grille[3])
                                                    tableau4 = "".join(client.grille[4])
                                                    tableau5 = "".join(client.grille[5])
                                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                    await tab.edit(content = f"{tableaucomplet}")
                        
                        elif (str(reaction.emoji) == '4⃣'):

                            if (client.grille[5][3]) == client.white:
                                client.grille[5][3] = client.yellow
                                tableau0 = "".join(client.grille[0])
                                tableau1 = "".join(client.grille[1])
                                tableau2 = "".join(client.grille[2])
                                tableau3 = "".join(client.grille[3])
                                tableau4 = "".join(client.grille[4])
                                tableau5 = "".join(client.grille[5])
                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                await tab.edit(content = f"{tableaucomplet}")
                            
                            else:
                                if (client.grille[4][3]) == client.white:
                                    client.grille[4][3] = client.yellow
                                    tableau0 = "".join(client.grille[0])
                                    tableau1 = "".join(client.grille[1])
                                    tableau2 = "".join(client.grille[2])
                                    tableau3 = "".join(client.grille[3])
                                    tableau4 = "".join(client.grille[4])
                                    tableau5 = "".join(client.grille[5])
                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                    await tab.edit(content = f"{tableaucomplet}")
                                
                                else:
                                    if (client.grille[3][3]) == client.white:
                                        client.grille[3][3] = client.yellow
                                        tableau0 = "".join(client.grille[0])
                                        tableau1 = "".join(client.grille[1])
                                        tableau2 = "".join(client.grille[2])
                                        tableau3 = "".join(client.grille[3])
                                        tableau4 = "".join(client.grille[4])
                                        tableau5 = "".join(client.grille[5])
                                        tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                        await tab.edit(content = f"{tableaucomplet}")

                                    else:
                                        if (client.grille[2][3]) == client.white:
                                            client.grille[2][3] = client.yellow
                                            tableau0 = "".join(client.grille[0])
                                            tableau1 = "".join(client.grille[1])
                                            tableau2 = "".join(client.grille[2])
                                            tableau3 = "".join(client.grille[3])
                                            tableau4 = "".join(client.grille[4])
                                            tableau5 = "".join(client.grille[5])
                                            tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                            await tab.edit(content = f"{tableaucomplet}")
                                        
                                        else:
                                            if (client.grille[1][3]) == client.white:
                                                client.grille[1][3] = client.yellow
                                                tableau0 = "".join(client.grille[0])
                                                tableau1 = "".join(client.grille[1])
                                                tableau2 = "".join(client.grille[2])
                                                tableau3 = "".join(client.grille[3])
                                                tableau4 = "".join(client.grille[4])
                                                tableau5 = "".join(client.grille[5])
                                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                await tab.edit(content = f"{tableaucomplet}")
                                            
                                            else:
                                                if (client.grille[0][3]) == client.white:
                                                    client.grille[0][3] = client.yellow
                                                    tableau0 = "".join(client.grille[0])
                                                    tableau1 = "".join(client.grille[1])
                                                    tableau2 = "".join(client.grille[2])
                                                    tableau3 = "".join(client.grille[3])
                                                    tableau4 = "".join(client.grille[4])
                                                    tableau5 = "".join(client.grille[5])
                                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                    await tab.edit(content = f"{tableaucomplet}")
                        
                        elif (str(reaction.emoji) == '5⃣'):

                            if (client.grille[5][4]) == client.white:
                                client.grille[5][4] = client.yellow
                                tableau0 = "".join(client.grille[0])
                                tableau1 = "".join(client.grille[1])
                                tableau2 = "".join(client.grille[2])
                                tableau3 = "".join(client.grille[3])
                                tableau4 = "".join(client.grille[4])
                                tableau5 = "".join(client.grille[5])
                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                await tab.edit(content = f"{tableaucomplet}")
                            
                            else:
                                if (client.grille[4][4]) == client.white:
                                    client.grille[4][4] = client.yellow
                                    tableau0 = "".join(client.grille[0])
                                    tableau1 = "".join(client.grille[1])
                                    tableau2 = "".join(client.grille[2])
                                    tableau3 = "".join(client.grille[3])
                                    tableau4 = "".join(client.grille[4])
                                    tableau5 = "".join(client.grille[5])
                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                    await tab.edit(content = f"{tableaucomplet}")
                                
                                else:
                                    if (client.grille[3][4]) == client.white:
                                        client.grille[3][4] = client.yellow
                                        tableau0 = "".join(client.grille[0])
                                        tableau1 = "".join(client.grille[1])
                                        tableau2 = "".join(client.grille[2])
                                        tableau3 = "".join(client.grille[3])
                                        tableau4 = "".join(client.grille[4])
                                        tableau5 = "".join(client.grille[5])
                                        tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                        await tab.edit(content = f"{tableaucomplet}")

                                    else:
                                        if (client.grille[2][4]) == client.white:
                                            client.grille[2][4] = client.yellow
                                            tableau0 = "".join(client.grille[0])
                                            tableau1 = "".join(client.grille[1])
                                            tableau2 = "".join(client.grille[2])
                                            tableau3 = "".join(client.grille[3])
                                            tableau4 = "".join(client.grille[4])
                                            tableau5 = "".join(client.grille[5])
                                            tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                            await tab.edit(content = f"{tableaucomplet}")
                                        
                                        else:
                                            if (client.grille[1][4]) == client.white:
                                                client.grille[1][4] = client.yellow
                                                tableau0 = "".join(client.grille[0])
                                                tableau1 = "".join(client.grille[1])
                                                tableau2 = "".join(client.grille[2])
                                                tableau3 = "".join(client.grille[3])
                                                tableau4 = "".join(client.grille[4])
                                                tableau5 = "".join(client.grille[5])
                                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                await tab.edit(content = f"{tableaucomplet}")
                                            
                                            else:
                                                if (client.grille[0][4]) == client.white:
                                                    client.grille[0][4] = client.yellow
                                                    tableau0 = "".join(client.grille[0])
                                                    tableau1 = "".join(client.grille[1])
                                                    tableau2 = "".join(client.grille[2])
                                                    tableau3 = "".join(client.grille[3])
                                                    tableau4 = "".join(client.grille[4])
                                                    tableau5 = "".join(client.grille[5])
                                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                    await tab.edit(content = f"{tableaucomplet}")

                        elif (str(reaction.emoji) == '6⃣'):

                            if (client.grille[5][5]) == client.white:
                                client.grille[5][5] = client.yellow
                                tableau0 = "".join(client.grille[0])
                                tableau1 = "".join(client.grille[1])
                                tableau2 = "".join(client.grille[2])
                                tableau3 = "".join(client.grille[3])
                                tableau4 = "".join(client.grille[4])
                                tableau5 = "".join(client.grille[5])
                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                await tab.edit(content = f"{tableaucomplet}")
                            
                            else:
                                if (client.grille[4][5]) == client.white:
                                    client.grille[4][5] = client.yellow
                                    tableau0 = "".join(client.grille[0])
                                    tableau1 = "".join(client.grille[1])
                                    tableau2 = "".join(client.grille[2])
                                    tableau3 = "".join(client.grille[3])
                                    tableau4 = "".join(client.grille[4])
                                    tableau5 = "".join(client.grille[5])
                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                    await tab.edit(content = f"{tableaucomplet}")
                                
                                else:
                                    if (client.grille[3][5]) == client.white:
                                        client.grille[3][5] = client.yellow
                                        tableau0 = "".join(client.grille[0])
                                        tableau1 = "".join(client.grille[1])
                                        tableau2 = "".join(client.grille[2])
                                        tableau3 = "".join(client.grille[3])
                                        tableau4 = "".join(client.grille[4])
                                        tableau5 = "".join(client.grille[5])
                                        tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                        await tab.edit(content = f"{tableaucomplet}")

                                    else:
                                        if (client.grille[2][5]) == client.white:
                                            client.grille[2][5] = client.yellow
                                            tableau0 = "".join(client.grille[0])
                                            tableau1 = "".join(client.grille[1])
                                            tableau2 = "".join(client.grille[2])
                                            tableau3 = "".join(client.grille[3])
                                            tableau4 = "".join(client.grille[4])
                                            tableau5 = "".join(client.grille[5])
                                            tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                            await tab.edit(content = f"{tableaucomplet}")
                                        
                                        else:
                                            if (client.grille[1][5]) == client.white:
                                                client.grille[1][5] = client.yellow
                                                tableau0 = "".join(client.grille[0])
                                                tableau1 = "".join(client.grille[1])
                                                tableau2 = "".join(client.grille[2])
                                                tableau3 = "".join(client.grille[3])
                                                tableau4 = "".join(client.grille[4])
                                                tableau5 = "".join(client.grille[5])
                                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                await tab.edit(content = f"{tableaucomplet}")
                                            
                                            else:
                                                if (client.grille[0][5]) == client.white:
                                                    client.grille[0][5] = client.yellow
                                                    tableau0 = "".join(client.grille[0])
                                                    tableau1 = "".join(client.grille[1])
                                                    tableau2 = "".join(client.grille[2])
                                                    tableau3 = "".join(client.grille[3])
                                                    tableau4 = "".join(client.grille[4])
                                                    tableau5 = "".join(client.grille[5])
                                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                    await tab.edit(content = f"{tableaucomplet}")

                        elif (str(reaction.emoji) == '7⃣'):

                            if (client.grille[5][6]) == client.white:
                                client.grille[5][6] = client.yellow
                                tableau0 = "".join(client.grille[0])
                                tableau1 = "".join(client.grille[1])
                                tableau2 = "".join(client.grille[2])
                                tableau3 = "".join(client.grille[3])
                                tableau4 = "".join(client.grille[4])
                                tableau5 = "".join(client.grille[5])
                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                await tab.edit(content = f"{tableaucomplet}")
                            
                            else:
                                if (client.grille[4][6]) == client.white:
                                    client.grille[4][6] = client.yellow
                                    tableau0 = "".join(client.grille[0])
                                    tableau1 = "".join(client.grille[1])
                                    tableau2 = "".join(client.grille[2])
                                    tableau3 = "".join(client.grille[3])
                                    tableau4 = "".join(client.grille[4])
                                    tableau5 = "".join(client.grille[5])
                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                    await tab.edit(content = f"{tableaucomplet}")
                                
                                else:
                                    if (client.grille[3][6]) == client.white:
                                        client.grille[3][6] = client.yellow
                                        tableau0 = "".join(client.grille[0])
                                        tableau1 = "".join(client.grille[1])
                                        tableau2 = "".join(client.grille[2])
                                        tableau3 = "".join(client.grille[3])
                                        tableau4 = "".join(client.grille[4])
                                        tableau5 = "".join(client.grille[5])
                                        tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                        await tab.edit(content = f"{tableaucomplet}")

                                    else:
                                        if (client.grille[2][6]) == client.white:
                                            client.grille[2][6] = client.yellow
                                            tableau0 = "".join(client.grille[0])
                                            tableau1 = "".join(client.grille[1])
                                            tableau2 = "".join(client.grille[2])
                                            tableau3 = "".join(client.grille[3])
                                            tableau4 = "".join(client.grille[4])
                                            tableau5 = "".join(client.grille[5])
                                            tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                            await tab.edit(content = f"{tableaucomplet}")
                                        
                                        else:
                                            if (client.grille[1][6]) == client.white:
                                                client.grille[1][6] = client.yellow
                                                tableau0 = "".join(client.grille[0])
                                                tableau1 = "".join(client.grille[1])
                                                tableau2 = "".join(client.grille[2])
                                                tableau3 = "".join(client.grille[3])
                                                tableau4 = "".join(client.grille[4])
                                                tableau5 = "".join(client.grille[5])
                                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                await tab.edit(content = f"{tableaucomplet}")
                                            
                                            else:
                                                if (client.grille[0][6]) == client.white:
                                                    client.grille[0][6] = client.yellow
                                                    tableau0 = "".join(client.grille[0])
                                                    tableau1 = "".join(client.grille[1])
                                                    tableau2 = "".join(client.grille[2])
                                                    tableau3 = "".join(client.grille[3])
                                                    tableau4 = "".join(client.grille[4])
                                                    tableau5 = "".join(client.grille[5])
                                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                    await tab.edit(content = f"{tableaucomplet}")

                    await tab.clear_reactions()

                else:

                    embedjeumention = discord.Embed(description = f"{client.red} {respuesta[6]} <@{mention.id}>\n{client.yellow} {respuesta[7]} <@{jaune.id}>", 
                                                colour =0xFF0000)

                    await rep.edit(embed = embedjeumention)

                    if (client.grille[0][0]) == client.white:
                        await tab.add_reaction('1⃣')
                    if (client.grille[0][1]) == client.white:
                        await tab.add_reaction('2⃣')
                    if (client.grille[0][2]) == client.white:
                        await tab.add_reaction('3⃣')
                    if (client.grille[0][3]) == client.white:
                        await tab.add_reaction('4⃣')
                    if (client.grille[0][4]) == client.white:
                        await tab.add_reaction('5⃣')
                    if (client.grille[0][5]) == client.white:
                        await tab.add_reaction('6⃣')
                    if (client.grille[0][6]) == client.white:
                        await tab.add_reaction('7⃣')

                    def checkmention1(reaction, user):
                        return user == mention and ((str(reaction.emoji) == '1⃣') or (str(reaction.emoji) == '2⃣') or (str(reaction.emoji) == '3⃣') or (str(reaction.emoji) == '4⃣') or (str(reaction.emoji) == '5⃣') or (str(reaction.emoji) == '6⃣') or (str(reaction.emoji) == '7⃣'))

                    reaction, user = await self.bot.wait_for('reaction_add', check=checkmention1)
                    if user.id != 761359894791192596:
                        if (str(reaction.emoji) == '1⃣'):

                            if (client.grille[5][0]) == client.white:
                                client.grille[5][0] = client.red
                                tableau0 = "".join(client.grille[0])
                                tableau1 = "".join(client.grille[1])
                                tableau2 = "".join(client.grille[2])
                                tableau3 = "".join(client.grille[3])
                                tableau4 = "".join(client.grille[4])
                                tableau5 = "".join(client.grille[5])
                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                await tab.edit(content = f"{tableaucomplet}")
                            
                            else:
                                if (client.grille[4][0]) == client.white:
                                    client.grille[4][0] = client.red
                                    tableau0 = "".join(client.grille[0])
                                    tableau1 = "".join(client.grille[1])
                                    tableau2 = "".join(client.grille[2])
                                    tableau3 = "".join(client.grille[3])
                                    tableau4 = "".join(client.grille[4])
                                    tableau5 = "".join(client.grille[5])
                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                    await tab.edit(content = f"{tableaucomplet}")
                                
                                else:
                                    if (client.grille[3][0]) == client.white:
                                        client.grille[3][0] = client.red
                                        tableau0 = "".join(client.grille[0])
                                        tableau1 = "".join(client.grille[1])
                                        tableau2 = "".join(client.grille[2])
                                        tableau3 = "".join(client.grille[3])
                                        tableau4 = "".join(client.grille[4])
                                        tableau5 = "".join(client.grille[5])
                                        tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                        await tab.edit(content = f"{tableaucomplet}")

                                    else:
                                        if (client.grille[2][0]) == client.white:
                                            client.grille[2][0] = client.red
                                            tableau0 = "".join(client.grille[0])
                                            tableau1 = "".join(client.grille[1])
                                            tableau2 = "".join(client.grille[2])
                                            tableau3 = "".join(client.grille[3])
                                            tableau4 = "".join(client.grille[4])
                                            tableau5 = "".join(client.grille[5])
                                            tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                            await tab.edit(content = f"{tableaucomplet}")
                                        
                                        else:
                                            if (client.grille[1][0]) == client.white:
                                                client.grille[1][0] = client.red
                                                tableau0 = "".join(client.grille[0])
                                                tableau1 = "".join(client.grille[1])
                                                tableau2 = "".join(client.grille[2])
                                                tableau3 = "".join(client.grille[3])
                                                tableau4 = "".join(client.grille[4])
                                                tableau5 = "".join(client.grille[5])
                                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                await tab.edit(content = f"{tableaucomplet}")
                                            
                                            else:
                                                if (client.grille[0][0]) == client.white:
                                                    client.grille[0][0] = client.red
                                                    tableau0 = "".join(client.grille[0])
                                                    tableau1 = "".join(client.grille[1])
                                                    tableau2 = "".join(client.grille[2])
                                                    tableau3 = "".join(client.grille[3])
                                                    tableau4 = "".join(client.grille[4])
                                                    tableau5 = "".join(client.grille[5])
                                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                    await tab.edit(content = f"{tableaucomplet}")
                                                
                                                else:
                                                    if (client.grille[0][0]) != client.white:
                                                        await tab.clear_reaction("1⃣")

                        elif (str(reaction.emoji) == '2⃣'):

                            if (client.grille[5][1]) == client.white:
                                client.grille[5][1] = client.red
                                tableau0 = "".join(client.grille[0])
                                tableau1 = "".join(client.grille[1])
                                tableau2 = "".join(client.grille[2])
                                tableau3 = "".join(client.grille[3])
                                tableau4 = "".join(client.grille[4])
                                tableau5 = "".join(client.grille[5])
                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                await tab.edit(content = f"{tableaucomplet}")
                            
                            else:
                                if (client.grille[4][1]) == client.white:
                                    client.grille[4][1] = client.red
                                    tableau0 = "".join(client.grille[0])
                                    tableau1 = "".join(client.grille[1])
                                    tableau2 = "".join(client.grille[2])
                                    tableau3 = "".join(client.grille[3])
                                    tableau4 = "".join(client.grille[4])
                                    tableau5 = "".join(client.grille[5])
                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                    await tab.edit(content = f"{tableaucomplet}")
                                
                                else:
                                    if (client.grille[3][1]) == client.white:
                                        client.grille[3][1] = client.red
                                        tableau0 = "".join(client.grille[0])
                                        tableau1 = "".join(client.grille[1])
                                        tableau2 = "".join(client.grille[2])
                                        tableau3 = "".join(client.grille[3])
                                        tableau4 = "".join(client.grille[4])
                                        tableau5 = "".join(client.grille[5])
                                        tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                        await tab.edit(content = f"{tableaucomplet}")

                                    else:
                                        if (client.grille[2][1]) == client.white:
                                            client.grille[2][1] = client.red
                                            tableau0 = "".join(client.grille[0])
                                            tableau1 = "".join(client.grille[1])
                                            tableau2 = "".join(client.grille[2])
                                            tableau3 = "".join(client.grille[3])
                                            tableau4 = "".join(client.grille[4])
                                            tableau5 = "".join(client.grille[5])
                                            tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                            await tab.edit(content = f"{tableaucomplet}")
                                        
                                        else:
                                            if (client.grille[1][1]) == client.white:
                                                client.grille[1][1] = client.red
                                                tableau0 = "".join(client.grille[0])
                                                tableau1 = "".join(client.grille[1])
                                                tableau2 = "".join(client.grille[2])
                                                tableau3 = "".join(client.grille[3])
                                                tableau4 = "".join(client.grille[4])
                                                tableau5 = "".join(client.grille[5])
                                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                await tab.edit(content = f"{tableaucomplet}")
                                            
                                            else:
                                                if (client.grille[0][1]) == client.white:
                                                    client.grille[0][1] = client.red
                                                    tableau0 = "".join(client.grille[0])
                                                    tableau1 = "".join(client.grille[1])
                                                    tableau2 = "".join(client.grille[2])
                                                    tableau3 = "".join(client.grille[3])
                                                    tableau4 = "".join(client.grille[4])
                                                    tableau5 = "".join(client.grille[5])
                                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                    await tab.edit(content = f"{tableaucomplet}")
                                        
                        elif (str(reaction.emoji) == '3⃣'):

                            if (client.grille[5][2]) == client.white:
                                client.grille[5][2] = client.red
                                tableau0 = "".join(client.grille[0])
                                tableau1 = "".join(client.grille[1])
                                tableau2 = "".join(client.grille[2])
                                tableau3 = "".join(client.grille[3])
                                tableau4 = "".join(client.grille[4])
                                tableau5 = "".join(client.grille[5])
                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                await tab.edit(content = f"{tableaucomplet}")
                            
                            else:
                                if (client.grille[4][2]) == client.white:
                                    client.grille[4][2] = client.red
                                    tableau0 = "".join(client.grille[0])
                                    tableau1 = "".join(client.grille[1])
                                    tableau2 = "".join(client.grille[2])
                                    tableau3 = "".join(client.grille[3])
                                    tableau4 = "".join(client.grille[4])
                                    tableau5 = "".join(client.grille[5])
                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                    await tab.edit(content = f"{tableaucomplet}")
                                
                                else:
                                    if (client.grille[3][2]) == client.white:
                                        client.grille[3][2] = client.red
                                        tableau0 = "".join(client.grille[0])
                                        tableau1 = "".join(client.grille[1])
                                        tableau2 = "".join(client.grille[2])
                                        tableau3 = "".join(client.grille[3])
                                        tableau4 = "".join(client.grille[4])
                                        tableau5 = "".join(client.grille[5])
                                        tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                        await tab.edit(content = f"{tableaucomplet}")

                                    else:
                                        if (client.grille[2][2]) == client.white:
                                            client.grille[2][2] = client.red
                                            tableau0 = "".join(client.grille[0])
                                            tableau1 = "".join(client.grille[1])
                                            tableau2 = "".join(client.grille[2])
                                            tableau3 = "".join(client.grille[3])
                                            tableau4 = "".join(client.grille[4])
                                            tableau5 = "".join(client.grille[5])
                                            tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                            await tab.edit(content = f"{tableaucomplet}")
                                        
                                        else:
                                            if (client.grille[1][2]) == client.white:
                                                client.grille[1][2] = client.red
                                                tableau0 = "".join(client.grille[0])
                                                tableau1 = "".join(client.grille[1])
                                                tableau2 = "".join(client.grille[2])
                                                tableau3 = "".join(client.grille[3])
                                                tableau4 = "".join(client.grille[4])
                                                tableau5 = "".join(client.grille[5])
                                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                await tab.edit(content = f"{tableaucomplet}")
                                            
                                            else:
                                                if (client.grille[0][2]) == client.white:
                                                    client.grille[0][2] = client.red
                                                    tableau0 = "".join(client.grille[0])
                                                    tableau1 = "".join(client.grille[1])
                                                    tableau2 = "".join(client.grille[2])
                                                    tableau3 = "".join(client.grille[3])
                                                    tableau4 = "".join(client.grille[4])
                                                    tableau5 = "".join(client.grille[5])
                                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                    await tab.edit(content = f"{tableaucomplet}")
                        
                        elif (str(reaction.emoji) == '4⃣'):

                            if (client.grille[5][3]) == client.white:
                                client.grille[5][3] = client.red
                                tableau0 = "".join(client.grille[0])
                                tableau1 = "".join(client.grille[1])
                                tableau2 = "".join(client.grille[2])
                                tableau3 = "".join(client.grille[3])
                                tableau4 = "".join(client.grille[4])
                                tableau5 = "".join(client.grille[5])
                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                await tab.edit(content = f"{tableaucomplet}")
                            
                            else:
                                if (client.grille[4][3]) == client.white:
                                    client.grille[4][3] = client.red
                                    tableau0 = "".join(client.grille[0])
                                    tableau1 = "".join(client.grille[1])
                                    tableau2 = "".join(client.grille[2])
                                    tableau3 = "".join(client.grille[3])
                                    tableau4 = "".join(client.grille[4])
                                    tableau5 = "".join(client.grille[5])
                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                    await tab.edit(content = f"{tableaucomplet}")
                                
                                else:
                                    if (client.grille[3][3]) == client.white:
                                        client.grille[3][3] = client.red
                                        tableau0 = "".join(client.grille[0])
                                        tableau1 = "".join(client.grille[1])
                                        tableau2 = "".join(client.grille[2])
                                        tableau3 = "".join(client.grille[3])
                                        tableau4 = "".join(client.grille[4])
                                        tableau5 = "".join(client.grille[5])
                                        tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                        await tab.edit(content = f"{tableaucomplet}")

                                    else:
                                        if (client.grille[2][3]) == client.white:
                                            client.grille[2][3] = client.red
                                            tableau0 = "".join(client.grille[0])
                                            tableau1 = "".join(client.grille[1])
                                            tableau2 = "".join(client.grille[2])
                                            tableau3 = "".join(client.grille[3])
                                            tableau4 = "".join(client.grille[4])
                                            tableau5 = "".join(client.grille[5])
                                            tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                            await tab.edit(content = f"{tableaucomplet}")
                                        
                                        else:
                                            if (client.grille[1][3]) == client.white:
                                                client.grille[1][3] = client.red
                                                tableau0 = "".join(client.grille[0])
                                                tableau1 = "".join(client.grille[1])
                                                tableau2 = "".join(client.grille[2])
                                                tableau3 = "".join(client.grille[3])
                                                tableau4 = "".join(client.grille[4])
                                                tableau5 = "".join(client.grille[5])
                                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                await tab.edit(content = f"{tableaucomplet}")
                                            
                                            else:
                                                if (client.grille[0][3]) == client.white:
                                                    client.grille[0][3] = client.red
                                                    tableau0 = "".join(client.grille[0])
                                                    tableau1 = "".join(client.grille[1])
                                                    tableau2 = "".join(client.grille[2])
                                                    tableau3 = "".join(client.grille[3])
                                                    tableau4 = "".join(client.grille[4])
                                                    tableau5 = "".join(client.grille[5])
                                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                    await tab.edit(content = f"{tableaucomplet}")
                        
                        elif (str(reaction.emoji) == '5⃣'):

                            if (client.grille[5][4]) == client.white:
                                client.grille[5][4] = client.red
                                tableau0 = "".join(client.grille[0])
                                tableau1 = "".join(client.grille[1])
                                tableau2 = "".join(client.grille[2])
                                tableau3 = "".join(client.grille[3])
                                tableau4 = "".join(client.grille[4])
                                tableau5 = "".join(client.grille[5])
                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                await tab.edit(content = f"{tableaucomplet}")
                            
                            else:
                                if (client.grille[4][4]) == client.white:
                                    client.grille[4][4] = client.red
                                    tableau0 = "".join(client.grille[0])
                                    tableau1 = "".join(client.grille[1])
                                    tableau2 = "".join(client.grille[2])
                                    tableau3 = "".join(client.grille[3])
                                    tableau4 = "".join(client.grille[4])
                                    tableau5 = "".join(client.grille[5])
                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                    await tab.edit(content = f"{tableaucomplet}")
                                
                                else:
                                    if (client.grille[3][4]) == client.white:
                                        client.grille[3][4] = client.red
                                        tableau0 = "".join(client.grille[0])
                                        tableau1 = "".join(client.grille[1])
                                        tableau2 = "".join(client.grille[2])
                                        tableau3 = "".join(client.grille[3])
                                        tableau4 = "".join(client.grille[4])
                                        tableau5 = "".join(client.grille[5])
                                        tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                        await tab.edit(content = f"{tableaucomplet}")

                                    else:
                                        if (client.grille[2][4]) == client.white:
                                            client.grille[2][4] = client.red
                                            tableau0 = "".join(client.grille[0])
                                            tableau1 = "".join(client.grille[1])
                                            tableau2 = "".join(client.grille[2])
                                            tableau3 = "".join(client.grille[3])
                                            tableau4 = "".join(client.grille[4])
                                            tableau5 = "".join(client.grille[5])
                                            tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                            await tab.edit(content = f"{tableaucomplet}")
                                        
                                        else:
                                            if (client.grille[1][4]) == client.white:
                                                client.grille[1][4] = client.red
                                                tableau0 = "".join(client.grille[0])
                                                tableau1 = "".join(client.grille[1])
                                                tableau2 = "".join(client.grille[2])
                                                tableau3 = "".join(client.grille[3])
                                                tableau4 = "".join(client.grille[4])
                                                tableau5 = "".join(client.grille[5])
                                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                await tab.edit(content = f"{tableaucomplet}")
                                            
                                            else:
                                                if (client.grille[0][4]) == client.white:
                                                    client.grille[0][4] = client.red
                                                    tableau0 = "".join(client.grille[0])
                                                    tableau1 = "".join(client.grille[1])
                                                    tableau2 = "".join(client.grille[2])
                                                    tableau3 = "".join(client.grille[3])
                                                    tableau4 = "".join(client.grille[4])
                                                    tableau5 = "".join(client.grille[5])
                                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                    await tab.edit(content = f"{tableaucomplet}")

                        elif (str(reaction.emoji) == '6⃣'):

                            if (client.grille[5][5]) == client.white:
                                client.grille[5][5] = client.red
                                tableau0 = "".join(client.grille[0])
                                tableau1 = "".join(client.grille[1])
                                tableau2 = "".join(client.grille[2])
                                tableau3 = "".join(client.grille[3])
                                tableau4 = "".join(client.grille[4])
                                tableau5 = "".join(client.grille[5])
                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                await tab.edit(content = f"{tableaucomplet}")
                            
                            else:
                                if (client.grille[4][5]) == client.white:
                                    client.grille[4][5] = client.red
                                    tableau0 = "".join(client.grille[0])
                                    tableau1 = "".join(client.grille[1])
                                    tableau2 = "".join(client.grille[2])
                                    tableau3 = "".join(client.grille[3])
                                    tableau4 = "".join(client.grille[4])
                                    tableau5 = "".join(client.grille[5])
                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                    await tab.edit(content = f"{tableaucomplet}")
                                
                                else:
                                    if (client.grille[3][5]) == client.white:
                                        client.grille[3][5] = client.red
                                        tableau0 = "".join(client.grille[0])
                                        tableau1 = "".join(client.grille[1])
                                        tableau2 = "".join(client.grille[2])
                                        tableau3 = "".join(client.grille[3])
                                        tableau4 = "".join(client.grille[4])
                                        tableau5 = "".join(client.grille[5])
                                        tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                        await tab.edit(content = f"{tableaucomplet}")

                                    else:
                                        if (client.grille[2][5]) == client.white:
                                            client.grille[2][5] = client.red
                                            tableau0 = "".join(client.grille[0])
                                            tableau1 = "".join(client.grille[1])
                                            tableau2 = "".join(client.grille[2])
                                            tableau3 = "".join(client.grille[3])
                                            tableau4 = "".join(client.grille[4])
                                            tableau5 = "".join(client.grille[5])
                                            tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                            await tab.edit(content = f"{tableaucomplet}")
                                        
                                        else:
                                            if (client.grille[1][5]) == client.white:
                                                client.grille[1][5] = client.red
                                                tableau0 = "".join(client.grille[0])
                                                tableau1 = "".join(client.grille[1])
                                                tableau2 = "".join(client.grille[2])
                                                tableau3 = "".join(client.grille[3])
                                                tableau4 = "".join(client.grille[4])
                                                tableau5 = "".join(client.grille[5])
                                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                await tab.edit(content = f"{tableaucomplet}")
                                            
                                            else:
                                                if (client.grille[0][5]) == client.white:
                                                    client.grille[0][5] = client.red
                                                    tableau0 = "".join(client.grille[0])
                                                    tableau1 = "".join(client.grille[1])
                                                    tableau2 = "".join(client.grille[2])
                                                    tableau3 = "".join(client.grille[3])
                                                    tableau4 = "".join(client.grille[4])
                                                    tableau5 = "".join(client.grille[5])
                                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                    await tab.edit(content = f"{tableaucomplet}")

                        elif (str(reaction.emoji) == '7⃣'):

                            if (client.grille[5][6]) == client.white:
                                client.grille[5][6] = client.red
                                tableau0 = "".join(client.grille[0])
                                tableau1 = "".join(client.grille[1])
                                tableau2 = "".join(client.grille[2])
                                tableau3 = "".join(client.grille[3])
                                tableau4 = "".join(client.grille[4])
                                tableau5 = "".join(client.grille[5])
                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                await tab.edit(content = f"{tableaucomplet}")
                            
                            else:
                                if (client.grille[4][6]) == client.white:
                                    client.grille[4][6] = client.red
                                    tableau0 = "".join(client.grille[0])
                                    tableau1 = "".join(client.grille[1])
                                    tableau2 = "".join(client.grille[2])
                                    tableau3 = "".join(client.grille[3])
                                    tableau4 = "".join(client.grille[4])
                                    tableau5 = "".join(client.grille[5])
                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                    await tab.edit(content = f"{tableaucomplet}")
                                
                                else:
                                    if (client.grille[3][6]) == client.white:
                                        client.grille[3][6] = client.red
                                        tableau0 = "".join(client.grille[0])
                                        tableau1 = "".join(client.grille[1])
                                        tableau2 = "".join(client.grille[2])
                                        tableau3 = "".join(client.grille[3])
                                        tableau4 = "".join(client.grille[4])
                                        tableau5 = "".join(client.grille[5])
                                        tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                        await tab.edit(content = f"{tableaucomplet}")

                                    else:
                                        if (client.grille[2][6]) == client.white:
                                            client.grille[2][6] = client.red
                                            tableau0 = "".join(client.grille[0])
                                            tableau1 = "".join(client.grille[1])
                                            tableau2 = "".join(client.grille[2])
                                            tableau3 = "".join(client.grille[3])
                                            tableau4 = "".join(client.grille[4])
                                            tableau5 = "".join(client.grille[5])
                                            tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                            await tab.edit(content = f"{tableaucomplet}")
                                        
                                        else:
                                            if (client.grille[1][6]) == client.white:
                                                client.grille[1][6] = client.red
                                                tableau0 = "".join(client.grille[0])
                                                tableau1 = "".join(client.grille[1])
                                                tableau2 = "".join(client.grille[2])
                                                tableau3 = "".join(client.grille[3])
                                                tableau4 = "".join(client.grille[4])
                                                tableau5 = "".join(client.grille[5])
                                                tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                await tab.edit(content = f"{tableaucomplet}")
                                            
                                            else:
                                                if (client.grille[0][6]) == client.white:
                                                    client.grille[0][6] = client.red
                                                    tableau0 = "".join(client.grille[0])
                                                    tableau1 = "".join(client.grille[1])
                                                    tableau2 = "".join(client.grille[2])
                                                    tableau3 = "".join(client.grille[3])
                                                    tableau4 = "".join(client.grille[4])
                                                    tableau5 = "".join(client.grille[5])
                                                    tableaucomplet = tableau0 + "\n" + tableau1 + "\n" + tableau2 + "\n" + tableau3 + "\n" + tableau4 + "\n" + tableau5
                                                    await tab.edit(content = f"{tableaucomplet}")

                    await tab.clear_reactions()

                embedfinjeujaune = discord.Embed(description = f"<@{jaune.id}> {respuesta[8]} <@{jaune.id}> {respuesta[10]} <@{mention.id}>\n{respuesta[9]}",
                                                colour =0xFFFF00)

                embedfinjeumention = discord.Embed(description = f"<@{mention.id}> {respuesta[8]} <@{mention.id}> {respuesta[10]} <@{jaune.id}>\n{respuesta[9]}",
                                                colour =0xFF0000)

                for x in range(len(client.grille)):
                    for y in range(len(client.grille[x])-3):
                        if client.grille[x][y] == client.yellow and client.grille[x][y+1] == client.yellow and client.grille[x][y+2] == client.yellow and client.grille[x][y+3] == client.yellow:
                            
                            await rep.edit(embed = embedfinjeujaune)
                            return
                        elif client.grille[x][y] == client.red and client.grille[x][y+1] == client.red and client.grille[x][y+2] == client.red and client.grille[x][y+3] == client.red:
                            
                            await rep.edit(embed = embedfinjeumention)
                            return

                for x in range(len(client.grille)-3):
                    for y in range(len(client.grille[x])):
                        if client.grille[x][y] == client.yellow and client.grille[x+1][y] == client.yellow and client.grille[x+2][y] == client.yellow and client.grille[x+3][y] == client.yellow:
                            
                            await rep.edit(embed = embedfinjeujaune)
                            return
                        elif client.grille[x][y] == client.red and client.grille[x+1][y] == client.red and client.grille[x+2][y] == client.red and client.grille[x+3][y] == client.red:
                            
                            await rep.edit(embed = embedfinjeumention)
                            return

                for x in range(len(client.grille)-3):
                    for y in range(len(client.grille[x])-3):
                        if client.grille[x][y] == client.yellow and client.grille[x+1][y+1] == client.yellow and client.grille[x+2][y+2] == client.yellow and client.grille[x+3][y+3] == client.yellow:
                            
                            await rep.edit(embed = embedfinjeujaune)
                            return
                        elif client.grille[x][y] == client.red and client.grille[x+1][y+1] == client.red and client.grille[x+2][y+2] == client.red and client.grille[x+3][y+3] == client.red:
                            
                            await rep.edit(embed = embedfinjeumention)
                            return

                for x in range(len(client.grille)-3):
                    for y in range(3, len(client.grille[x])):
                        if client.grille[x][y] == client.yellow and client.grille[x+1][y-1] == client.yellow and client.grille[x+2][y-2] == client.yellow and client.grille[x+3][y-3] == client.yellow:
                            
                            await rep.edit(embed = embedfinjeujaune)
                            return
                        elif client.grille[x][y] == client.red and client.grille[x+1][y-1] == client.red and client.grille[x+2][y-2] == client.red and client.grille[x+3][y-3] == client.red:
                            
                            await rep.edit(embed = embedfinjeumention)
                            return

    @cog_ext.cog_slash(name = 'help', description = 'Show bot commands', guild_ids = [696831427882254346], options = help_)
    async def help(self, ctx: SlashContext, help_=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if help_ == "main" or help_ == None:
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
            elif help_ == "nsfw":
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
            elif help_ == "read":
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
            elif help_ == "info":        
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
            elif help_ == "media": 
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
            elif help_ == "games": 
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
            elif help_ == "music": 
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
            elif help_ == "moder":
                if lang == 'es':
                    respuesta = es.help_moder()
                    commands = discord.Embed(title=respuesta[0], color=ctx.author.color) #,color=Hex code
                    commands.set_author(name=f'{ctx.author.display_name} {respuesta[1]}', icon_url=f'{ctx.author.avatar_url}')
                    commands.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                    commands.add_field(name=respuesta[2], value=respuesta[3], inline=False)
                    commands.set_footer(text=respuesta[4],icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                elif lang == 'en':
                    commands = discord.Embed(title=":heartpulse: Here is a list of moder commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------", color=ctx.author.color) #,color=Hex code
                    commands.set_author(name=f'{ctx.author.display_name} \n ❤️ We thank you for using Mitsuri  ❤️  ', icon_url=f'{ctx.author.avatar_url}')
                    commands.set_thumbnail(url='https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                    commands.add_field(name=f':hammer: Moder :hammer:', value=f'```Moderation Commands \n Comming soon```')
                    commands.set_footer(text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181",icon_url=f'https://static.wikia.nocookie.net/bd949a92-0ecb-49b3-ab23-01320b401bff')
                await ctx.send(embed=commands)
            elif help_ == "reacts":
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
            elif help_ == "useful":
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
            elif help_ == "traslate":
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

    @cog_ext.cog_slash(name = 'commands', description = 'Show all bot commands', guild_ids = [696831427882254346], options = comandos)
    @client.command()
    async def commandss(self, ctx: SlashContext, commands=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            if commands == "dm" or commands == None:
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
            elif commands == "channel":
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

    @cog_ext.cog_slash(name = 'servericon', description = 'Sends the number of pages the doujin has entered', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'serverinfo', description = 'Send a detailed description of the current server', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'profile', description = 'Send a detailed description to a person from the server or yours if you do not specify person', guild_ids = [696831427882254346], options = optional)
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
                embed.set_thumbnail(url=f'{user3.avatar_url}')
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

    @cog_ext.cog_slash(name = 'ping', description = 'Shows ping between message and message, and Mitsuri ping', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'vote', description = 'Send the link to Mitsuri!\'S top.gg page to vote!', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'feedback', description = 'Send a github link to report any bugs or suggestions', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'bughunter', description = 'Send a list of our helpers who have contributed ideas and found bugs to improve the bot', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'partners', description = 'servers that have supported me from the beginning', guild_ids = [696831427882254346])
    async def partners(self, ctx: SlashContext):
        embed = discord.Embed(color=ctx.author.color)
        embed.set_thumbnail(url='https://64.media.tumblr.com/d8841e84219ae53081bda00495cddb3d/5be347091e1ad9ec-55/s640x960/6141959d7cda3f3794d19a9bfffce0c088e19ca8.png')
        embed.add_field(name=f':handshake: :gift_heart:  ¿Quienes son mis partners? :gift_heart: :handshake: ', value='\nTengo 2 servidores donde empecé a dar mis primeros pasos, ellos me ayudaron a crecer y a corregir mis errores y poco a poco fui mejorando y llegar a ser lo que soy ahora mismo')
        embed.add_field(name=f'\n-----Tenemos como primer Partner a: Valpo | Role & Game-----', value=f'Descripción: \n\n┌────────────────────────┐\n✦ ──────𝒱𝒶𝓁𝓅𝑜  𝓇𝑜𝓁𝑒  𝒶𝓃𝒹  𝒢𝒶𝓂𝑒───── ✦\n└────────────────────────┘\n\nSpanish server for gamers and role community\nServer en Español para la comunidad de gamers y role\n\n༄Roles por Nivel \n༄Roles de Colores \n༄Sorteos \n༄Eventos\n༄Apuestas\n༄Múltiples canales de chat\n༄Ciudad de Role\n༄Confesiones\n༄Juegos\n༄Familias\n༄Clubs\n༄Un bot 24/7 en cada canal de música\n⋘▬▬▬▬▬▬▬▬▬༺★༻▬▬▬▬▬▬▬▬▬▬⋙\n ✦ Invite Link: [Invitación al servidor de Valpo | Role & Game](https://discord.gg/JCR9Zjz)', inline=False)
        embed.add_field(name=f'\n------------Tenemos como segundo Partner a: WABI-SABI-----------', value=f'Descripción: \n\n┌────── ∘°❉°∘ ──────┐\n•---------- WABI-SABI---------•\n└────── °∘❉∘° ──────┘\n¿Quienes somos?\n\n✎﹏﹏﹏﹏﹏﹏﹏\n:sparkles:    Somos una comunidad que nace de la idea de tres amigos de tener un lugar agradable para charlar , opinar, compartir cositas sobre temática anime, videojuegos, arte,  y mucho más!\n﹏﹏﹏﹏\n¿Qué ofrecemos?\n\n➤ En Wabi-Sabi  puedes encontrar\n꒰:rice_ball:꒱↝ Comunidad activa\n꒰:dancer_tone1:꒱↝ Ambiente no tóxico\n꒰:slot_machine:꒱↝ Actividades y concursos\n꒰:game_die: ꒱↝ Autoroles \n꒰:crown:꒱↝ Premio especial a usuario del mes\n꒰:gift:꒱↝ Tienda con artículos especiales (Juegos, camisetas, skins, vales amazon, netflix, llaveros...)\n꒰:moneybag:꒱↝ Banco con tus puntos acumulados\n꒰:video_camera: ꒱↝ Streamings de todo tipo\n꒰:performing_arts: ꒱↝ Variedad de bots\n꒰:trophy: ꒱↝ Wabis!\n△▽△▽△▽△▽△▽△▽△▽△▽\n¿Qué esperas para unirte?\n➤ ¡Te estamos esperando! \n ✦ Invite Link: [Invitación al servidor de WABI-SABI](https://discord.gg/n3dAgSt)', inline=True)
        #embed.add_field(name=f'\n---------Tenemos como tercer Partner a: Otakus Shin Sekai--------', value='Descripción: \n\n┌────────────────────────┐\nঔৣ͜͡ঔৣ═════OTAKUS SHIN SEKAI ═════ঔৣ͜͡ঔৣ\n└────────────────────────┘\n\n𝚀𝚞𝚎 𝚝𝚎𝚗𝚎𝚖𝚘𝚜 𝚎𝚗 𝚎𝚜𝚝𝚎 𝚛𝚎𝚒𝚗𝚘?. 𝙼𝚞𝚌𝚑𝚒𝚜𝚒𝚖𝚊𝚜 𝚌𝚘𝚜𝚊𝚜!\n▬▬▬▬▬▬▬▬▬▬▬▬⌘⋆⋆⌘▬▬▬▬▬▬▬▬▬▬▬▬▬\n:pinching_hand: ␥ ⩩ 𝚁𝚎𝚐𝚕𝚊𝚜 𝚜𝚎𝚗𝚌𝚒𝚕𝚕𝚊𝚜\n:dizzy:  ␥ ⩩ 𝙰𝚕𝚒𝚊𝚗𝚣𝚊𝚜 𝚌𝚘𝚗 𝚌𝚞𝚊𝚕𝚚𝚞𝚒𝚎𝚛 𝚝𝚒𝚙𝚘 𝚍𝚎 𝚜𝚎𝚛𝚟𝚎𝚛𝚜.\n:muscle:  ␥ ⩩ 𝙾𝚠𝚗𝚎𝚛𝚎𝚜 𝚊𝚌𝚝𝚒𝚟𝚘𝚜, 𝚊𝚍𝚖𝚒𝚗𝚜 𝚊𝚌𝚝𝚒𝚟𝚘𝚜 𝚢 𝚜𝚎 𝚋𝚞𝚜𝚌𝚊 𝚎𝚗𝚌𝚊𝚛𝚐𝚊𝚍𝚘 𝚍𝚎 𝚊𝚕𝚒𝚊𝚗𝚣𝚊 𝚢 𝚙𝚊𝚛𝚊 𝚖𝚘𝚍𝚎𝚛𝚊𝚛 𝚎𝚕 𝚜𝚎𝚛𝚟𝚒𝚍𝚘𝚛\n:envelope:  ␥ ⩩ 𝙲𝚑𝚊𝚝 𝚊𝚌𝚝𝚒𝚟𝚘 𝚍𝚘𝚗𝚍𝚎 𝚙𝚘𝚍𝚛𝚊𝚜 𝚌𝚘𝚗𝚘𝚌𝚎𝚛 𝚐𝚎𝚗𝚝𝚎 𝚖𝚞𝚢 𝚍𝚒𝚟𝚎𝚛𝚝𝚒𝚍𝚊, 𝚌𝚑𝚊𝚛𝚕𝚊𝚛 𝚢 𝚓𝚞𝚐𝚊𝚛 𝚌𝚘𝚗 𝚎𝚕𝚕𝚘𝚜\n:robot: ␥ ⩩ 𝙱𝚘𝚝𝚜 𝚙𝚊𝚛𝚊 𝚍𝚒𝚟𝚎𝚛𝚝𝚒𝚛𝚜𝚎 𝚊 𝚖𝚘𝚗𝚝𝚘𝚗\n:boom:  ␥ ⩩ 𝙰𝚞𝚝𝚘-𝚛𝚘𝚕𝚎𝚜 𝚍𝚎: 𝚍𝚊𝚝𝚘𝚜 𝚗𝚘 𝚝𝚊𝚗 𝚙𝚎𝚛𝚜𝚘𝚗𝚊𝚕𝚎𝚜, 𝚌𝚘𝚕𝚘𝚛𝚎𝚜, 𝚓𝚞𝚎𝚐𝚘𝚜 𝚏𝚊𝚟𝚘𝚛𝚒𝚝𝚘𝚜, 𝙽𝚂𝙵𝚆, 𝚑𝚘𝚋𝚋𝚒𝚎𝚜, 𝚛𝚎𝚐𝚒ó𝚗, 𝚎𝚝𝚌.\n:projector:  ␥ ⩩ 𝙷𝚊𝚢 𝚙𝚎𝚕í𝚌𝚞𝚕𝚊 𝟷 𝚟𝚎𝚜 𝚊 𝚕𝚊 𝚜𝚎𝚖𝚊𝚗𝚊!.\n:hotsprings:  ␥ ⩩ 𝙷𝚊𝚌𝚎𝚖𝚘𝚜 𝚜𝚘𝚛𝚝𝚎𝚘𝚜 𝚌𝚊𝚍𝚊 𝟹 𝚖𝚎𝚜𝚎𝚜!.\n:rocket:  ␥ ⩩ Canales de sugerencia!, soporte técnico y reportes(por si alguien molesta)\n▬▬▬▬▬▬▬▬▬▬▬▬⌘⋆⋆⌘▬▬▬▬▬▬▬▬▬▬▬▬▬\n▬▬▬▬▬▬▬▬▬▬▬▬⌘⋆⋆⌘▬▬▬▬▬▬▬▬▬▬▬▬▬\n✦ Invite Link: [Invitación al servidor de Otakus Shin Sekai](https://discord.gg/tcdr429)', inline=False)
        embed.set_footer(text=f'¡Informacion de partners pedida por: {ctx.author.display_name}, Gracias!')
        await ctx.send(embed=embed, delete_after=120.0)

    @cog_ext.cog_slash(name = 'wallpaper', description = 'Sends the number of pages the doujin has entered', guild_ids = [696831427882254346], options = wallpaper)
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

    @cog_ext.cog_slash(name = 'dogo', description = 'Send a puppy', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'neko', description = 'Send a kitten', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'bird', description = 'Send a little bird', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'tenor', description = 'Send a random tenor gif of what you want to search', guild_ids = [696831427882254346], options = wallpaper)
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
                    await ctx.send("You must write after mi!tenor what you want to search")
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

    @cog_ext.cog_slash(name = 'ran_wall', description = 'Send a random wallpaper', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'en_meme', description = 'Send a meme in English from reddit', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'es_meme', description = 'Send a meme in Spanish from reddit', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'wallpaper2', description = 'This command is set in case you cannot find a photo with mi!wallpaper command', guild_ids = [696831427882254346], options = wallpaper)
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

    @cog_ext.cog_slash(name = 'ranwaifu', description = 'Send a random waifu', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'megumin', description = 'megumin', guild_ids = [696831427882254346])
    async def megumin(self, ctx: SlashContext):
        r = requests.get(f'https://waifu.pics/api/sfw/megumin')
        if r.status_code == 200:
            data = json.loads(r.content)
            img = data["url"]
            embed = discord.Embed(title='Megumiin >~<',color=ctx.author.color)
            embed.set_author(name=f'{ctx.author.display_name}', icon_url=f'{ctx.author.avatar_url}')
            embed.set_image(url=img)
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'ranneko', description = 'Send a random kawaii neko', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'character', description = 'Send a photo of the character you chose!', guild_ids = [696831427882254346], options = wallpaper)
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

    @cog_ext.cog_slash(name = 'pages_of', description = 'Enter a doujinshi number', guild_ids = [696831427882254346], options = pages)
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

    @cog_ext.cog_slash(name = 'sauce_cont', description = 'Send the number of doujins that exist', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'nhentai_read', description = 'You can read the doujin you want, as long as it is in accordance with Discord\'s terms of service', guild_ids = [696831427882254346], options = nhent_read)
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

    @cog_ext.cog_slash(name = 'cum', description = 'You come in a person or alone', guild_ids = [696831427882254346], options = optional)
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

    @cog_ext.cog_slash(name = 'kuni', description = 'lick your friend\'s member', guild_ids = [696831427882254346], options = obligatory)
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

    @cog_ext.cog_slash(name = 'suck', description = 'lick your friend\'s member', guild_ids = [696831427882254346], options = obligatory)      
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

    @cog_ext.cog_slash(name = 'anal', description = 'give your friend an anal', guild_ids = [696831427882254346], options = obligatory)      
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

    @cog_ext.cog_slash(name = 'masturb', description = 'masturbate all you want', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'feets', description = 'enjoy a good pair of feet', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'hi', description = 'hi to a friend or say hi to all users', guild_ids = [696831427882254346], options = optional)
    async def hi(self, ctx: SlashContext, mention : discord.Member=None):
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

    @cog_ext.cog_slash(name = 'poke', description = 'Give some lovely pokes to your friend', guild_ids = [696831427882254346], options = obligatory)
    async def poke(self, ctx: SlashContext, mention : discord.Member=None):
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
            
    @cog_ext.cog_slash(name = 'kiss', description = 'Give some kisses to your friend', guild_ids = [696831427882254346], options = obligatory)
    async def kiss(self, ctx: SlashContext, mention : discord.Member=None):
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

    @cog_ext.cog_slash(name = 'slap', description = 'Slaps the tagged user', guild_ids = [696831427882254346], options = obligatory)
    async def slap(self, ctx: SlashContext, mention : discord.Member=None):
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

    @cog_ext.cog_slash(name = 'cuddle', description = 'snuggle up with your friend', guild_ids = [696831427882254346], options = obligatory)
    async def cuddle(self, ctx: SlashContext, mention : discord.Member=None):
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

    @cog_ext.cog_slash(name = 'hug', description = 'Give a hug to your friend', guild_ids = [696831427882254346], options = obligatory)
    async def hug(self, ctx: SlashContext, mention : discord.Member=None):
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

    @cog_ext.cog_slash(name = 'pat', description = 'Give some pats to your friend', guild_ids = [696831427882254346], options = obligatory)
    async def pat(self, ctx: SlashContext, mention : discord.Member=None):
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

    @cog_ext.cog_slash(name = 'baka', description = 'Call idiot (baka in Japanese) to the tagged user', guild_ids = [696831427882254346], options = obligatory)
    async def baka(self, ctx: SlashContext, mention : discord.Member=None):
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
                    text = es.baka(2, 2)
                elif lang == 'en':
                    text = en.baka(2, 3)
                embed = discord.Embed(title=f'{user} {text}', color=ctx.author.color)
                embed.set_image(url=data)
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'feed', description = 'If someone is hungry feed them', guild_ids = [696831427882254346], options = obligatory)
    async def feed(self, ctx: SlashContext, mention : discord.Member=None):
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

    @cog_ext.cog_slash(name = 'tickle', description = 'A friend is sad Well, a good tickle will help him!', guild_ids = [696831427882254346], options = obligatory)
    async def tickle(self, ctx: SlashContext, mention : discord.Member=None):
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

    @cog_ext.cog_slash(name = 'smug', description = 'show who you are... yeeahh!', guild_ids = [696831427882254346])
    async def smug(self, ctx: SlashContext):
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

    @cog_ext.cog_slash(name = 'run', description = 'Run run they catch you!!', guild_ids = [696831427882254346])
    async def run(self, ctx: SlashContext):
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

    @cog_ext.cog_slash(name = 'dance', description = 'To dance! alone or with your friend', guild_ids = [696831427882254346], options = optional)
    async def dance(self, ctx: SlashContext, mention : discord.Member=None):
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

    @cog_ext.cog_slash(name = 'angry', description = 'Show your vilest anger', guild_ids = [696831427882254346], options = optional)
    async def angry(self, ctx: SlashContext, mention : discord.Member=None):
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

    @cog_ext.cog_slash(name = 'revive', description = 'revive your friend', guild_ids = [696831427882254346], options = obligatory)
    async def revive(self, ctx: SlashContext, mention : discord.Member=None):
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
                embed = discord.Embed(title=text, color=ctx.author.color)
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

    @cog_ext.cog_slash(name = 'kill', description = 'kill your enemy', guild_ids = [696831427882254346], options = obligatory)
    async def kill(self, ctx: SlashContext, mention : discord.Member=None):
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

    @cog_ext.cog_slash(name = 'blush', description = 'If they bring out the colors with beautiful words, blush at ease', guild_ids = [696831427882254346])
    async def blush(self, ctx: SlashContext):
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

    @cog_ext.cog_slash(name = 'happy', description = 'Explode with happiness', guild_ids = [696831427882254346])
    async def happy(self, ctx: SlashContext):
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

    @cog_ext.cog_slash(name = 'sad', description = 'Are you sad?, show your emotions', guild_ids = [696831427882254346])
    async def sad(self, ctx: SlashContext):
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

    @cog_ext.cog_slash(name = 'laugh', description = 'Laugh as much as you want or can!', guild_ids = [696831427882254346])
    async def laugh(self, ctx: SlashContext):
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

    @cog_ext.cog_slash(name = 'cry', description = 'They have broken your heart... cry as much as you want', guild_ids = [696831427882254346])
    async def cry(self, ctx: SlashContext):
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

    @cog_ext.cog_slash(name = 'confused', description = 'Are you confused…? you don\'t understand…', guild_ids = [696831427882254346])
    async def confused(self, ctx: SlashContext):
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

    @cog_ext.cog_slash(name = 'bored', description = 'You don\'t know what to do, you feel bored', guild_ids = [696831427882254346])
    async def bored(self, ctx: SlashContext):
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

    @cog_ext.cog_slash(name = 'fbi', description = 'FBI OPEN UP!', guild_ids = [696831427882254346])
    async def fbi(self, ctx: SlashContext):
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

    @cog_ext.cog_slash(name = 'sleep', description = 'Did you fall asleep or… sleep with your friend', guild_ids = [696831427882254346], options = optional)
    async def sleep(self, ctx: SlashContext, mention : discord.Member=None):
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
    
    @cog_ext.cog_slash(name = 'invite', description = 'If you want to invite the bot to your server use this command', guild_ids = [696831427882254346])
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

    @cog_ext.cog_slash(name = 'ran_music', description = 'wants to listen to music!!', guild_ids = [696831427882254346], options = [])
    async def ran_music(self, ctx: SlashContext):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            musica = ran_musica()
            if lang == 'es':
                text = es.ran_music()
            elif lang == 'en':
                text = en.ran_music()
            embed = discord.Embed(color=0xea7938)
            embed.add_field(name=text[0], value=f'{musica}')
            embed.set_footer(text=f'{ctx.author.display_name} {text[1]}')
            await ctx.send(embed=embed)

    @cog_ext.cog_slash(name = 'createinvite', description = 'Create an invite from the current channel and send it on the same channel', guild_ids = [696831427882254346], options = invite)
    async def createinvite(self, ctx: SlashContext, time=None, uses=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            try:
                tiempo = int(time)
                usos = int(uses)
                invitelink = await ctx.channel.create_invite(max_age = tiempo, max_uses = usos)
                icon_url = str(ctx.guild.icon_url)
                if tiempo != 0:
                    hora = tiempo // 3600
                    minutos = (tiempo % 3600) // 60
                    segundos = (tiempo % 60)
                    horaa = (hora, minutos, segundos)
                else:
                    if lang == 'es':
                        text = es.createinvite(1)
                    elif lang == 'en':
                        text = en.createinvite(1)
                    horaa = (text[0], text[1], text[2])
                if usos == 0:
                    if lang == 'es':
                        text = es.createinvite(2)
                    elif lang == 'en':
                        text = en.createinvite(2)
                    usos = text
                else:
                    usos = usos
                if lang == 'es':
                    text = es.createinvite(3)
                elif lang == 'en':
                    text = en.createinvite(3)
                if "https" in icon_url:
                    embed = discord.Embed(color=ctx.author.color)
                    embed.set_thumbnail(url=icon_url)
                    embed.add_field(name=text[0], value=f'{text[1]} {horaa[0]}\n{text[2]} {horaa[1]}\n{text[3]} {horaa[2]}\n{text[4]} {usos}\n```{invitelink}```')
                    embed.set_footer(text=f'{text[5]} {ctx.author.display_name}<-')
                    await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(color=ctx.author.color)
                    embed.add_field(name=text[0], value=f'{text[1]} {horaa[0]}\n{text[2]} {horaa[1]}\n{text[3]} {horaa[2]}\n{text[4]} {usos}\n```{invitelink}```')
                    embed.set_footer(text=f'{text[5]} {ctx.author.display_name}<-')
                    await ctx.send(embed=embed)
            except:
                if lang == 'es':
                    text = es.createinvite(4)
                    await ctx.send(text)
                elif lang == 'en':
                    text = en.createinvite(4)
                    await ctx.send(text) 

    @cog_ext.cog_slash(name = 'createinvitedm', description = 'Create an invite from the current channel and send it to the DM', guild_ids = [696831427882254346], options = invite)
    async def createinvitedm(self, ctx: SlashContext, tiempo=None, usos=None):
        guild_id = ctx.author.guild.id
        lang = lang_comprove(guild_id)
        if lang == False:
            text = es.lang_comprove()
            em = discord.Embed(title=text[0], description=text[1], color=random.randint(0, 16777215))
            await ctx.send(embed=em)
        else:
            try:
                tiempo = int(tiempo)
                usos = int(usos)
                
                invitelink = await ctx.channel.create_invite(max_age = tiempo, max_uses = usos)
                icon_url = str(ctx.guild.icon_url)
                if tiempo != 0:
                    hora = tiempo // 3600
                    minutos = (tiempo % 3600) // 60
                    segundos = (tiempo % 60)
                    horaa = (hora, minutos, segundos)
                else:
                    if lang == 'es':
                        text = es.createinvitedm(1)
                    elif lang == 'en':
                        text = en.createinvitedm(1)
                    horaa = ("Infinito", "Infinito", "Infinito")
                if usos == 0:
                    if lang == 'es':
                        text = es.createinvitedm(2)
                    elif lang == 'en':
                        text = en.createinvitedm(2)
                    usos = "infinito"
                else:
                    usos = usos
                if lang == 'es':
                    text = es.createinvitedm(3)
                elif lang == 'en':
                    text = en.createinvitedm(3)
                if "https" in icon_url:
                    embed = discord.Embed(color=ctx.author.color)
                    embed.set_thumbnail(url=icon_url)
                    embed.add_field(name=text[0], value=f'{text[1]} {horaa[0]}\n{text[2]} {horaa[1]}\n{text[3]} {horaa[2]}\n{text[4]} {usos}\n```{invitelink}```')
                    embed.set_footer(text=f'{text[5]} {ctx.author.display_name}<-')
                    await ctx.author.send(embed=embed)
                    mensage = await ctx.send(f'{ctx.author.display_name} {text[6]}')
                    await mensage.add_reaction("📩")
                else:
                    embed = discord.Embed(color=ctx.author.color)
                    embed.add_field(name=text[0], value=f'{text[1]} {horaa[0]}\n{text[2]} {horaa[1]}\n{text[3]} {horaa[2]}\n{text[4]} {usos}\n```{invitelink}```')
                    embed.set_footer(text=f'{text[5]} {ctx.author.display_name}<-')
                    await ctx.author.send(embed=embed)
                    mensage = await ctx.send(f'{ctx.author.display_name} {text[6]}')
                    await mensage.add_reaction("📩")
            except:
                if lang == 'es':
                    text = es.createinvitedm(4)
                    await ctx.send(text)
                elif lang == 'en':
                    text = en.createinvitedm(4)
                    await ctx.send(text)

    @cog_ext.cog_slash(name = 'avatar', description = 'Send the avatar of the tagged person or your avatar if you don\'t tag anyone', guild_ids = [696831427882254346], options = optional)
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

    @cog_ext.cog_slash(name = 'tr', description = 'Translate a text from one language to another', guild_ids = [696831427882254346], options = tr)
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

    @cog_ext.cog_slash(name = 'we', description = 'Send detailed weather information in that place', guild_ids = [696831427882254346], options = we)
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

    @cog_ext.cog_slash(name = 'bugrep', description = 'If you have a problem or have found a bug in Mitsuri send it to us', guild_ids = [696831427882254346], options = bug)
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

    @cog_ext.cog_slash(name = 'supser', description = 'Send a description about the official Mitsuri support server, the invitation link and the link to the Mitsuri top.gg page', guild_ids = [696831427882254346], options = [])
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

def setup(bot: commands.Bot):
    bot.add_cog(slash_slash_commands(bot))
    