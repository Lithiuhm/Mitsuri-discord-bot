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

class game_slash_commands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @cog_ext.cog_slash(name = 'coin', description = 'flip a coin', guild_ids = [], options = [])
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
    
    @cog_ext.cog_slash(name = '8ball', description = 'Ask Mitsuri a question', guild_ids = [], options = _8ball)
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

    @cog_ext.cog_slash(name = 'yon', description = 'Ask Mitsuri a question', guild_ids = [], options = yon)
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

    @cog_ext.cog_slash(name = 'dice', description = 'You roll a 6-sided dice', guild_ids = [], options = [])
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

    @cog_ext.cog_slash(name = 'connect4', description = 'Ask Mitsuri a question', guild_ids = [], options = obligatory)
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

def setup(bot: commands.Bot):
    bot.add_cog(game_slash_commands(bot))





























































































































































































































































































































































































                    