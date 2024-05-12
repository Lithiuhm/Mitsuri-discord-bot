import random
prefijo = "mi!"

def lang(num1, num2, num3, lang):
    
    if num1 == 1:
        #lang == None
        #field
        name=f'Language selection'
        value='**ES:**\nDebes introducir el lenguaje que quieres que hable\nPor ahora solo puedo hablar Inglés, Español y Francés\n\n**EN:**\nYou must enter the language you want me to speak\nI can only speak English, Spanish and French\n\n**FR:**\nVous devez entrer la langue que vous voulez que je parle\nPour l\'instant, je ne parle que l\'anglais, l\'espagnol et le français'
        return (name, value)
    elif num1 == 2:
        #if not lang in langu:
        name=f'You have entered an invalid language'
        value='**ES:**\nInglés: mi!lang en\nEspañol: mi!lang es\nFrancés: mi!lang fr\n\n**EN:**\nEnglish: mi!lang en\nSpanish: mi!lang es\nFrench: mi!lang fr\n\n**FR:**\nAnglais: mi!lang en\nEspagnol: mi!lang es\nFrançais: mi!lang fr'
        return (name, value)
    elif num1 == 3:
        if num2 == 1:
            #if lines[guild+1] == "es":
            name=f'El lenguaje anterior en este servidor era: '
            value=f'Ha sido cambiado a '
            if num3 == 0:
                return (name, value)
            elif num3 == 1:
                name=f'Selección de Idioma'
                value=f'Ahora hablaré `Español` en este servidor'
                return (name, value)
            elif num3 == 2:
                name=f'Language selection'
                value='Now I will speak `English` on this server'
                return (name, value)
            elif num3 == 3:
                name=f'Sélection de la langue'
                value='Maintenant je vais parler espagnol sur ce serveur'
                return (name, value)
        
        elif num2 == 2:       
            name=f'The last language on this server was '
            value=f'Has been changed to '
            if num3 == 0:
                return (name, value)
            elif num3 == 1:
                name=f'Selección de Idioma'
                value=f'Ahora hablaré `Español` en este servidor'
                return (name, value)
            elif num3 == 2:
                name=f'Language selection'
                value='Now I will speak `English` on this server'
                return (name, value)
            elif num3 == 3:
                name=f'Sélection de la langue'
                value='Maintenant je vais parler espagnol sur ce serveur'
                return (name, value)

        elif num2 == 3:
            name=f'La dernière langue sur ce serveur était '
            value=f'Il a été changé en '
            if num3 == 0:
                return (name, value)
            elif num3 == 1:
                name=f'Selección de Idioma'
                value=f'Ahora hablaré `Español` en este servidor'
                return (name, value)
            elif num3 == 2:
                name=f'Language selection'
                value='Now I will speak `English` on this server'
                return (name, value)
            elif num3 == 3:
                name=f'Sélection de la langue'
                value='Maintenant je vais parler espagnol sur ce serveur'
                return (name, value)

    elif num1 == 4:
        name=f'Language selection'
        value=f'**ES:**\nNo tienes idioma seleccionado con Mitsuri en este servidor\nSe cambiará a: `{lang}`\n\n**EN:**You have no language selected with Mitsuri on this server \nIt will be changed to: `{lang}`\n\n**FR:** Vous n\'avez pas de langue sélectionnée avec Mitsuri sur ce serveur\nça change en: `{lang}`'
        if num2 == 0:
            return (name, value)
        elif num2 == 1:
            name=f'Selección de Idioma'
            value=f'Ahora hablaré `Español` en este servidor'
            return (name, value)
        elif num2 == 2:
            name=f'Language selection'
            value='Now I will speak `English` on this server'
            return (name, value)
        elif num2 == 3:
            name=f'Sélection de la langue'
            value='Maintenant je vais parler espagnol sur ce serveur'
            return (name, value)

    elif  num1 == 5:
        name=f'❌ | Language could not be changed | ❌'
        value='**ES:**\nEste comando solo puede ser usado por un administrador del servidor actual, pídele a un administrador que lo cambie\n\n**EN:**\nThis command can only be used by a current server administrator, ask an admin to change it\n\n**FR:**\nCette commande ne peut être utilisée que par un administrateur du serveur actuel, demandez à un administrateur de la modifier'
        return (name, value)

def prefix(num1):
    if num1 == 1:
        name=f'To select a new prefix'
        value=f'Use: `{prefijo}prefix <new prefix>'
        return (name, value)
    elif num1 == 2:
        description='<a:yes:798310222942044201> Prefix changed to:'
        return description
    elif num1 == 3:
        text = "<a:no:798309997934673950> You do not have permission to use this command"
        return text

def help(num1, num2):
    #Segunda fila
    title=":heartpulse: Here you have a list of all my commands :heartpulse:\n -----------------> :beginner: Enjoy it :beginner: <-----------------"
    
    #primera fila
    name=f'\n ❤️ We thank you for using Mitsuri  ❤️ '
    
    #tercera fila
    value=f'<a:yes:798310222942044201>If you want the commands through private chat use: `{prefijo}commands`\n\n<a:yes:798310222942044201>To see the commands on the current channel use: `{prefijo}nodmcommands`\n\n<a:gearz:798310116977672243>To change the language use `mi!lang`\n\n<a:yes:798310222942044201>To change the prefix use:\n`{prefijo}prefix`\n\n<a:right:798310109507485736>You can also react in the reactions below to turn the page\n and see the commands by category <a:left:798310022308036608>\n----------------------- ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ -----------------------‏‏ ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎  ‏‏‎ --------------------'

    #cuarta fila
    #primera columna
    name1=f'📑 Information 📑\n<a:loading:798310144344719370>`{prefijo}help_info`\n\n🔞 NSFW 🔞\n<a:loading:798310144344719370>`{prefijo}help_nsfw`\n\n:books: Useful :books:\n<a:loading:798310144344719370>`{prefijo}help_useful`'
    value1=f'---------------------'
    
    #quinta fila
    #segunda columna
    name2=f':book:Read Doujins:book:\n<a:loading:798310144344719370>`{prefijo}help_read` \n\n:game_die:Entertainment:game_die:\n<a:loading:798310144344719370>`{prefijo}help_games`\n\n :notes: Music :notes:\n<a:loading:798310144344719370>`{prefijo}help_music`'
    value2=f'-----------------------'
    
    #sexta fila
    #tercera columna
    name3=f'📸 Media 📸\n<a:loading:798310144344719370>`{prefijo}help_media` \n\n💞 Reactions 💞\n<a:loading:798310144344719370>`{prefijo}help_reacts`\n\n:hammer: moder :hammer:\n<a:loading:798310144344719370>`{prefijo}help_moder`'
    value3=f'------------------------'
    
    #septima fila
    name4=':incoming_envelope: ----------INVITE---------- :incoming_envelope: `/` :sos: :point_right: ------HELP------ :point_left: :sos:'
    value4='<a:url:798310137327779890>[--------->INVITE<---------](https://ya.co.ve/Uej)<a:url:798310137327779890> `/` <a:url:798310137327779890>[--------->HELP<---------](https://discord.gg/dYMhtbq7Jr)<a:url:798310137327779890>'
    
    #ocatava fila
    name5='💰------->DONATIONS<------💰 `/` 🏆-------->VOTE<--------🏆'
    value5='<a:url:798310137327779890>[------>DONATIONS<------](https://www.paypal.com/paypalme/Mitsuribot)<a:url:798310137327779890>  `/` <a:url:798310137327779890>[-------->VOTE<---------](https://top.gg/bot/761359894791192596)<a:url:798310137327779890>'

    #novena fila
    text="Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    if num2 == 0:
        return (title, name, value, name1, value1, name2, value2, name3, value3, name4, value4, name5, value5, text)

    elif num2 == 2:
        
        #segunda fila
        title=":heartpulse: Here you have a list of information commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"
        
        #primera fila
        name=f'\n ❤️ We thank you for using Mitsuri  ❤️ '

        #tercera fila
        name2=f':bookmark_tabs: Information :bookmark_tabs:'
        value=f'```Information commands \n{prefijo}servericon\n{prefijo}serverinfo\n{prefijo}profile (Tag someone)\n{prefijo}ping\n{prefijo}vote\n{prefijo}feedback\n{prefijo}partners\n{prefijo}bughunter```'

        #footer
        text="Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

        return (title, name, name2, value, text)

    elif num2 == 3:

        #segunda fila
        title=":heartpulse: Here you have a list of NSFW commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"

        #primera fila
        name=f'\n ❤️ We thank you for using Mitsuri  ❤️ '

        #tercera fila
        name1=f'IMPORTANT INFORMATION'
        value1=f'```WE ARE IMPLEMENTING ALL OF THESE NSFW COMMANDS, IN THE FOLLOWING VERSIONS OF MITSURI THEY WILL BE AVAILABLE FOR YOUR USE```'

        #cuarta fila
        name2=f':underage: NSFW :underage:'
        value2=f'```NSFW commands that work\n{prefijo}cum (Tag someone)\n{prefijo}kuni [tag someone]\n{prefijo}suck [tag someone]\n{prefijo}anal [tag someone]\n{prefijo}masturb\n{prefijo}feets```'

        #quinta fila
        name3=f'Upcoming commands'
        value3=f'```\n{prefijo}erotic, {prefijo}nsfwneko, {prefijo}yuri, {prefijo}boobs, {prefijo}pussy, {prefijo}avatar, {prefijo}nsfwavatar, {prefijo}foxgirl, {prefijo}trap, {prefijo}ahegao, {prefijo}hentai```'

        #footer
        text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

        return (title, name, name1, value1, name2, value2, name3, value3, text)

    elif num2 == 4:
        
        #segunda fila
        title=":heartpulse: Here you have a list of useful commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"
        
        #primera fila
        name=f'\n ❤️ We thank you for using Mitsuri  ❤️ '

        #tercera fila
        name1=f':books: Useful :books:'
        value=f'```Useful commands \n{prefijo}invite\n{prefijo}createinvite [time] [uses]\n{prefijo}createinvitedm [time] [uses]\n{prefijo}avatar (Tag someone)\n{prefijo}tr [Source language] [Final language] [Message]\n{prefijo}bugrep [Error message or suggestion]\n{prefijo}supser\n{prefijo}we [City/Country]```'

        #footer
        text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"


        return (title, name, name1, value, text)

    elif num2 == 5:
        
        #segunda fila
        title=":heartpulse: Here you have a list of commands to read Doujins :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"
        
        #primera fila
        name=f'\n ❤️ We thank you for using Mitsuri  ❤️ '

        #tercera fila
        name1=f':book: Read Doujinshis :book:'
        value=f'```Read Doujinshis commands\n{prefijo}nhentai_read [Doujinshi number] [Page (It can be a number to read a specific page or "all" if you want to read all pages of a doujinshi)]\n{prefijo}pages_of [Doujinshi number]\n{prefijo}sauce_cont [Doujinshi number]```'

        #footer
        text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"


        return (title, name, name1, value, text)

    elif num2 == 6:

        #segunda fila
        title=":heartpulse: Here you have a list of game commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"

        #primera fila
        name=f'\n ❤️ We thank you for using Mitsuri  ❤️ '

        #tercera fila
        name1=f':game_die: Entertainment :game_die:'
        value=f'```Game commands \n{prefijo}coin\n{prefijo}8ball [Question]\n{prefijo}yon [Question]\n{prefijo}dado\n{prefijo}connect4 [Tag someone]```'

        #footer
        text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"


        return (title, name, name1, value, text)

    elif num2 == 7:

        #segunda fila  
        title=":heartpulse: Here you have a list of music commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"

        #primera fila
        name=f'\n ❤️ We thank you for using Mitsuri  ❤️'

        #cuarta fila
        name2=f':notes: Music :notes:'
        value2=f'```Music commands \n{prefijo}p or {prefijo}play [What do you want to listen?(Youtube links also work)]\n{prefijo}pa or {prefijo}pause\n{prefijo}r or {prefijo}res\n{prefijo}s or {prefijo}stop```'

        #footer
        text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

        return (title, name, name2, value2, text)
    
    elif num2 == 8:

        #segunda fila
        title=":heartpulse: Here you have a list of media commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"

        #primera fila
        name=f'\n ❤️ We thank you for using Mitsuri  ❤️'

        #tercera fila
        name1=f':camera_with_flash: Media :camera_with_flash:'
        value=f'```Media commands \n{prefijo}wallpaper [What do you want to look for?]\n{prefijo}wallpaper2 [What do you want to look for?]\n{prefijo}dogo\n{prefijo}neko\n{prefijo}bird\n{prefijo}tenor [What do you want to look for?]\n{prefijo}en_meme\n{prefijo}es_meme\n{prefijo}ran_wall\n{prefijo}ranwaifu\n{prefijo}megumin\n{prefijo}character [Who are you looking for?]\n{prefijo}ranneko```'

        #footer
        text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

        return (title, name, name1, value, text)


    elif num2 == 9:

        #segunda fila
        title=":heartpulse: Here you have a list of reaction commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"

        #primera fila
        name=f'\n ❤️ We thank you for using Mitsuri  ❤️'

        #tercera fila
        name1=f':revolving_hearts: Reaction :revolving_hearts:'
        value=f'```Reaction commands \n\nTag required:\n{prefijo}poke [Tag someone]\n{prefijo}kiss [Tag someone]\n{prefijo}slap [Tag someone]\n{prefijo}cuddle [Tag someone]\n{prefijo}hug [Tag someone]\n{prefijo}pat [Tag someone]\n{prefijo}baka [Tag someone]\n{prefijo}feed [Tag someone]\n{prefijo}tickle [Tag someone]\n{prefijo}punch [Tag someone]\n{prefijo}think [Tag someone]\n\nTag optional:\n{prefijo}hi (Tag someone)\n{prefijo}dance (Tag someone)\n{prefijo}angry (Tag someone)\n{prefijo}sleep (Tag someone)\n\nWithout tag:\n{prefijo}smug\n{prefijo}run\n{prefijo}blush\n{prefijo}happy\n{prefijo}sad\n{prefijo}laugh\n{prefijo}cry\n{prefijo}confused\n{prefijo}bored\n{prefijo}fbi```'

        #footer
        text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

        return (title, name, name1, value, text)

    elif num2 == 10:    

        #segunda fila
        title=":heartpulse: Here you have a list of moder commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"

        #primera fila
        name=f'\n ❤️ We thank you for using Mitsuri  ❤️'

        #tercera fila
        name1=f':hammer: Moderation :hammer:'
        value=f'```Moderation commands \nComing soon```'

        #footer
        text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

        return (title, name, name1, value, text)

    elif num2 == 11:
        text = "The bot's help message will be removed in 5 seconds"
        return text
        
def command():

    #segunda fila
    title=":heartpulse: Here you have a list of all my commands :heartpulse:\n -----------------> :beginner: Enjoy it :beginner: <-----------------"

    #primera fila
    name=f'\n ❤️ We thank you for using Mitsuri  ❤️'

    #tercera fila
    name1=f':star_struck: Helps :star_struck: '
    value1=f'```Hepls commands\n{prefijo}help_info\n{prefijo}help_nsfw\n{prefijo}help_useful\n{prefijo}help_read\n{prefijo}help_games\n{prefijo}help_music\n{prefijo}help_media\n{prefijo}help_reacts\n{prefijo}help_moder```'
    
    #cuarta fila
    name2=f':bookmark_tabs: Information :bookmark_tabs:'
    value2=f'```Information commands \n{prefijo}servericon\n{prefijo}serverinfo\n{prefijo}profile (Tag someone)\n{prefijo}ping\n{prefijo}vote\n{prefijo}feedback\n{prefijo}partners\n{prefijo}bughunter```'
    
    #quinta fila
    name3=f':book: Read Doujinshis :book:'
    value3=f'```Read Doujinshis commands\n{prefijo}nhentai_read [Doujinshi number] [Page (It can be a number to read a specific page or "all" if you want to read all pages of a doujinshi)]\n{prefijo}pages_of [Doujinshi number]\n{prefijo}sauce_cont [Doujinshi number]```'
    
    #sexta fila
    name4=f':game_die: Entertainment :game_die:'
    value4=f'```Game commands \n{prefijo}coin\n{prefijo}8ball [Question]\n{prefijo}yon [Question]\n{prefijo}dado\n{prefijo}connect4 [Tag someone]```'
    
    #octava fila
    name6=f':notes: Music :notes:'
    value6=f'```Music commands \n{prefijo}p or {prefijo}play [What do you want to listen?(Youtube links also work)]\n{prefijo}pa or {prefijo}pause\n{prefijo}r or {prefijo}res\n{prefijo}s or {prefijo}stop```'
    
    #Novena fila
    name7=f':camera_with_flash: Media :camera_with_flash:'
    value7=f'```Media commands \n{prefijo}wallpaper [What do you want to look for?]\n{prefijo}wallpaper2 [What do you want to look for?]\n{prefijo}dogo\n{prefijo}neko\n{prefijo}bird\n{prefijo}tenor [What do you want to look for?]\n{prefijo}en_meme\n{prefijo}es_meme\n{prefijo}ran_wall\n{prefijo}ranwaifu\n{prefijo}megumin\n{prefijo}character [Who are you looking for?]\n{prefijo}ranneko```'
    
    #decima fila
    name8=f':revolving_hearts: Reaction :revolving_hearts:'
    value8=f'```Reaction commands \n\nTag required:\n{prefijo}poke [Tag someone]\n{prefijo}kiss [Tag someone]\n{prefijo}slap [Tag someone]\n{prefijo}cuddle [Tag someone]\n{prefijo}hug [Tag someone]\n{prefijo}pat [Tag someone]\n{prefijo}baka [Tag someone]\n{prefijo}feed [Tag someone]\n{prefijo}tickle [Tag someone]\n{prefijo}punch [Tag someone]\n{prefijo}think [Tag someone]\n\nTag optional:\n{prefijo}hi (Tag someone)\n{prefijo}dance (Tag someone)\n{prefijo}angry (Tag someone)\n{prefijo}sleep (Tag someone)\n\nWithout tag:\n{prefijo}smug\n{prefijo}run\n{prefijo}blush\n{prefijo}happy\n{prefijo}sad\n{prefijo}laugh\n{prefijo}cry\n{prefijo}confused\n{prefijo}bored\n{prefijo}fbi```'
    
    #undécima fila
    name9=f':hammer: Moderation :hammer:'
    value9=f'```Moderation commands \nComing soon```'
    
    #dodecima fila
    name10=f'IMPORTANT INFORMATION'
    value10=f'```WE ARE IMPLEMENTING ALL OF THESE NSFW COMMANDS, IN THE FOLLOWING VERSIONS OF MITSURI THEY WILL BE AVAILABLE FOR YOUR USE```'
    
    #tridecima fila
    name11=f':underage: NSFW :underage:'
    value11=f'```NSFW commands that work\n{prefijo}cum (Tag someone)\n{prefijo}kuni [tag someone]\n{prefijo}suck [tag someone]\n{prefijo}anal [tag someone]\n{prefijo}masturb\n{prefijo}feets```'
    
    #cuatridécima fila
    name12=f'Upcoming commands'
    value12=f'```\n{prefijo}erotic, {prefijo}nsfwneko, {prefijo}yuri, {prefijo}boobs, {prefijo}pussy, {prefijo}avatar, {prefijo}nsfwavatar, {prefijo}foxgirl, {prefijo}trap, {prefijo}ahegao, {prefijo}hentai```'

    #quitidécima fila
    name13=f':incoming_envelope: ---------------Invite me to your discord server--------------- :incoming_envelope:'
    value13=f'[------------------------>Here is the invitation<-----------------------](https://discord.com/api/oauth2/authorize?client_id=761359894791192596&permissions=261993005047&scope=bot)'
    
    #sextigésima fila
    name14=f':trophy:  ---------------------->Vote me pleasee<----------------------- :trophy: '
    value14=f'[------------------>Come in and vote for me please<-----------------](https://top.gg/bot/761359894791192596)'

    #septigésima fila
    name15=f':no_entry_sign: :infinity:If you have any comments or problems with the bot:infinity: :no_entry_sign: '
    value15=f'[----------------------->Come in and put it here<----------------------](https://github.com/Skynext280/mitsuri-issues/issues)'

    #octagésima fila
    name16=f':sos: :point_right: ----------------Join our discord server---------------- :point_left: :sos:'
    value16=f'[-------------------------->Click here to join<--------------------------](https://discord.gg/dYMhtbq7Jr)'

    #nonadécima fila
    name17=f':moneybag: --------------------If you want to support us------------------ :moneybag:'
    value17=f'[---------------------->You can donate by paypal<--------------------](https://www.paypal.com/paypalme/Mitsuribot)'

    #footer
    text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    #dm
    msg = "I have sent you all the commands to your DM"
    
    return (title, name, name1, value1, name2, value2, name3, value3, name4, value4, name6, value6, name7, value7, name8, value8, name9, value9, name10, value10, name11, value11, name12, value12, name13, value13, name14, value14, name15, value15, name16, value16, name17, value17, msg, text)

def help_nsfw():

    #segunda fila
    title=":heartpulse: Here you have a list of NSFW commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ We thank you for using Mitsuri  ❤️ '

    #tercera fila
    name1=f'IMPORTANT INFORMATION'
    value1=f'```WE ARE IMPLEMENTING ALL OF THESE NSFW COMMANDS, IN THE FOLLOWING VERSIONS OF MITSURI THEY WILL BE AVAILABLE FOR YOUR USE```'

    #cuarta fila
    name2=f':underage: NSFW :underage:'
    value2=f'```NSFW commands that work\n {prefijo}r34 (What do you want to look for?)\n Send a gif / image of rule 34 of what you want to search or random if you don\'t specify what you want to search\n\n{prefijo}ran_coin\n Flip a coin and send a gif / img of rule34 as the coin falls\n\n{prefijo}furro_coin\n Flip a coin and send a gif / img of rule 34 of a furro as the coin falls\n\n{prefijo}cum (Tag someone)\n You come in a person or alone\n\n{prefijo}kuni [tag someone]\n lick your friend\'s member\n\n{prefijo}suck [tag someone]\n suck your friend\'s member\n\n{prefijo}anal [tag someone]\n give your friend an anal\n\n{prefijo}masturb \n masturbate all you want\n\n{prefijo}feets \n enjoy a good pair of feet```'

    #quinta fila
    name3=f'Upcoming commands'
    value3=f'```\n{prefijo}erotic, {prefijo}nsfwneko, {prefijo}yuri, {prefijo}boobs, {prefijo}pussy, {prefijo}avatar, {prefijo}nsfwavatar, {prefijo}foxgirl, {prefijo}trap, {prefijo}ahegao, {prefijo}hentai```'

    #footer
    text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, name2, value2, name3, value3, text)


def help_read():

    #segunda fila
    title=":heartpulse: Here you have a list of commands to read Doujins :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"
        
    #primera fila
    name=f'\n ❤️ We thank you for using Mitsuri  ❤️ '


    #tercera fila
    name1=f':book: Read Doujinshis :book:'
    value1=f'```Read Doujinshis commands\n{prefijo}nhentai_read [Doujinshi number] [Page (It can be a number to read a specific page or "all" if you want to read all pages of a doujinshi)]\n You can read the doujin you want, as long as it is in accordance with Discord\'s terms of service\n\n{prefijo}pages_of [Doujinshi number]\n Sends the number of pages the doujin has entered\n\n{prefijo}sauce_cont [Doujinshi number]\n Send the number of doujins that exist```'

    #footer
    text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, text)


def help_info():

    #segunda fila
    title=":heartpulse: Here you have a list of information commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ We thank you for using Mitsuri  ❤️ '

    #tercera fila
    name1=f':bookmark_tabs: Information :bookmark_tabs:'
    value1=f'```Information commands \n{prefijo}servericon\n Sends the current server icon\n\n{prefijo}serverinfo\n Send a detailed description of the current server\n\n{prefijo}profile\n Send a detailed description to a person from the server or yours if you do not specify person\n\n{prefijo}ping\n Shows ping between message and message, and Mitsuri ping\n\n{prefijo}vote\n Send the link to Mitsuri!\'S top.gg page to vote!\n\n{prefijo}feedback\n Send a github link to report any bugs or suggestions\n\n{prefijo}partners\n Send a description of all our partners\n\n{prefijo}bughunter\n Send a list of our helpers who have contributed ideas and found bugs to improve the bot```'

    #footer
    text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, text)

def help_media():

    #segunda fila
    title=":heartpulse: Here you have a list of media commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ We thank you for using Mitsuri  ❤️'
    
    #tercera fila
    name1=f':camera_with_flash: Media :camera_with_flash:'
    value1=f'```Media commands \n{prefijo}wallpaper [What do you want to look for?]\n Send a wallpaper of what you want to search\n\n{prefijo}wallpaper2 [What do you want to look for?]\n This command is set in case you cannot find a photo with {prefijo}wallpaper command\n\n{prefijo}dogo\n Send a puppy\n\n{prefijo}neko\n Send a kitten\n\n{prefijo}bird\n Send a little bird\n\n{prefijo}tenor [What do you want to look for?]\n Send a random tenor gif of what you want to search\n\n{prefijo}en_meme\n Send a meme in English from reddit\n\n{prefijo}es_meme\n Send a meme in Spanish from reddit\n\n{prefijo}ran_wall\n Send a random wallpaper\n\n{prefijo}ranwaifu\n Send a random waifu\n\n{prefijo}megumin\n Megumin >~<\n\n{prefijo}character [Who are you looking for?]\n Send a photo of the character you chose!\n\n{prefijo}ranneko\n Send a random kawaii neko```'

    #footer
    text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, text)

def help_games():

    #segunda fila
    title=":heartpulse: Here you have a list of game commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ We thank you for using Mitsuri  ❤️ '

    #tercera fila
    name1=f':game_die: Entertainment :game_die:'
    value1=f'```Game commands \n{prefijo}coin \n You flip a coin and it may land heads or tails\n\n{prefijo}_8ball [question]\n Ask Mitsuri a question, she will answer it! \n\n{prefijo}yon [question]\n Ask Mitsuri a question, she will answer you with a yes or no\n\n{prefijo}dice\n You roll a 6-sided dice\n\n{prefijo} connect4 [tag someone]\n A simple game of connecting 4 tiles of the same color```'

    #footer
    text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, text)

def help_music():

    #segunda fila  
    title=":heartpulse: Here you have a list of music commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ We thank you for using Mitsuri  ❤️'

    #cuarta fila
    name2=f':notes: Music :notes:'
    value2=f'```Music commands \n{prefijo}p or {prefijo}play [What do you want to listen?(Youtube links also work)]\n Play music on a channel\n\n{prefijo}pa ó {prefijo}pause\n Pause the song that is playing\n\n{prefijo}r ó {prefijo}res\n Resume the song that was playing\n\n{prefijo}s ó {prefijo}stop\n Stop the song that is playing```'

    #footer
    text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name2, value2, text)


def help_moder():
    
    #segunda fila
    title=":heartpulse: Here you have a list of moder commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ We thank you for using Mitsuri  ❤️'

    #tercera fila
    name1=f':hammer: Moderation :hammer:'
    value1=f'```Moderation commands \nComing soon```'

    #footer
    text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, text)


def help_reacts():

    #segunda fila
    title=":heartpulse: Aquí tienes una lista de comandos de reactions :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

    #tercera fila
    name1=f':revolving_hearts: Reactions :revolving_hearts:\n**-------------------------------Tag required-------------------------------**'
    value1=f'```{prefijo}poke [Tag someone]\n Give some lovely pokes to someone \n\n{prefijo}kiss [Tag someone]\n Kisses the tagged user\n\n{prefijo}slap [Tag someone] \n Slaps the tagged user \n\n{prefijo}cuddle [Tag someone] \n snuggle up with the tagged user \n\n{prefijo}hug [Tag someone] \n Give the tagged user a hug \n\n{prefijo}pat [Tag someone] \n Give the tagged user some pats \n\n{prefijo}baka [Tag someone] \n Call idiot (baka in Japanese) to the tagged user \n\n{prefijo}feed [Tag someone] \n If someone is hungry feed them with this command \n\n{prefijo}tickle [Tag someone] \n A friend is sad Well, a good tickle will help him! \n\n{prefijo}punch [Tag someone] \n You hit the tagged user```'
    
    #cuarta fila
    name2=f'**-------------------------------Tag optional-------------------------------**'
    value2=f'```{prefijo}hi (Tag someone)\n Say hi to a friend or say hi to all users\n\n{prefijo}dance (Tag someone)\n To dance! alone or accompanied if you tag a user\n\n{prefijo}angry (Tag someone)\n Show your vilest anger by mentioning a user or get angry about something without mentioning\n\n{prefijo}sleep (Tag someone) \n Did you fall asleep or… sleep with the tagged user```'

    #quinta fila
    name3=f'**-------------------------------Without tag-------------------------------**'
    value3=f'```{prefijo}smug \n show who you are... yeeahh! \n\n{prefijo}run \n Run run they catch you!!\n\n{prefijo}blush \n If they bring out the colors with beautiful words, blush at ease \n\n{prefijo}happy \n Explode with happiness \n\n{prefijo}sad \n Are you sad?, show your emotions it with this command \n\n{prefijo}laugh \n Laugh as much as you want or can! \n\n{prefijo}cry \n They have broken your heart... cry as much as you want \n\n{prefijo}confused \n Are you confused…? you don\'t understand… \n\n{prefijo}bored \n You don\'t know what to do, you feel bored, this is your command \n\n{prefijo}fbi \n FBI OPEN UP!```'

    #footer
    text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, name2, value2, name3, value3,text)

def help_useful():

    #segunda fila
    title=":heartpulse: Here you have a list of useful commands :heartpulse:\n ---------------------> :beginner: Enjoy it :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ We thank you for using Mitsuri  ❤️ '

    #tercera fila
    name1=f':books: Useful :books:'
    value1=f'```Useful commands \n{prefijo}invite \n If you want to invite the bot to your server use this command\n\n{prefijo}createinvite [time] [uses]\n Create an invite from the current channel and send it on the same channel\n\n{prefijo}createinvitedm [time] [uses]\n Create an invite from the current channel and send it to the DM\n\n{prefijo}avatar (Tag someone)\n Send the avatar of the tagged person or your avatar if you don\'t tag anyone\n\n{prefijo}tr [Source language] [Final language] [Message]\n Translate a text from one language to another\n\n{prefijo}bugrep [Error message or suggestion]\n If you have a problem or have found a bug in Mitsuri send it to us\n\n{prefijo}supser\n Send a description about the official Mitsuri support server, the invitation link and the link to the Mitsuri top.gg page \n\n{prefijo}we [City/Country] \n Send detailed weather information in that place```'

    #footer
    text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, text)

def help_lang():

    #segunda fila
    title=":heartpulse: Here is a list of translator languages :heartpulse:\n --------------------> :beginner: Enjoy it :beginner: <--------------------"

    #primera fila
    name=f'\n ❤️ We thank you for using Mitsuri  ❤️ '

    #tercera fila
    name1=f':books: Translator :books:'
    value1=f'Languages'

    #footer
    text=f"Creator \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, text)


def moneda(num1):
    
    if num1 == 1:
        name = '¡¡Has flipped the coin!!'
        value = 'Has fallen face'
    elif num1 == 2:
        name = '¡¡Has flipped the coin!!'
        value = 'Has fallen tails'
    return (name, value)

def _8ball(num1 ,question):
    
    if num1 ==1:
        text = "you must to ask me a question"
        return text
    elif num1 == 2:

        responses = ['yes, in my opinion',
                    'It is true',
                    'It is decidedly so',
                    'Probably',
                    'Good prognosis',
                    'Everything points to yes',
                    'Definitely',
                    'Yes',
                    'Yes, definitely',
                    'You must trust it',
                    'Vague answer, try again',
                    'Ask another time',
                    'I better not tell you now',
                    'I can not predict it now',
                    'Focus and ask again',
                    'Can be',
                    'Do not count on it',
                    'My answer is no',
                    'My sources tell me no',
                    'The prospects are not good',
                    'Very doubtful',
                ]

        respuesta = random.choices(responses)
        respuesta = respuesta[0]

        a = f'Question: {question}\nAnswer: {respuesta}'

        return a


def yon(num1, question):

    if num1 == 1:
        text = "you must to ask me a question"
        return text
    elif num1 == 2:
        responses = ["Yes", "No"]
        respuesta = random.choices(responses)
        respuesta = respuesta[0]

        a = f'Question: {question}\nAnswer: {respuesta}'
        
        return a

def dado():

    ent = random.randint(1, 6)

    a = f'The dice has fallen and the number has been rolled: {ent}'

    return a


def connect4():

    uno = "You can not play alone"
    dos = "wants to play a match 4 game. You have 30 seconds to accept the game!"
    tres = "Time has passed, try again"
    cuatro = "Lets play! \nThe first player is:"
    cinco = "Your color is yellow!"
    seis = "The game will start soon"
    siete = "**__turn of__**"
    ocho = "**Next**"
    nueve = ", You have won this game!!\nVery well played"
    diez = "Has been interesting"
    once = "and"

    return (uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez, once)


def hi(num1, num2):
    
    gifs = [
        "https://media1.tenor.com/images/fcc3854ad5ee2c22eb0189998be4c8f8/tenor.gif?itemid=14835859",
        "https://media1.tenor.com/images/056c584d9335fcabf080ca43e583e3c4/tenor.gif?itemid=8994845",
        "https://media1.tenor.com/images/2b121b915c9f3411eeba5092cd3c80bb/tenor.gif?itemid=13783216",
        "https://media1.tenor.com/images/72c9b849aa10b222371ebb99a6b1896a/tenor.gif?itemid=8807701",
        "https://media1.tenor.com/images/c2e21a9d8e17c1d335166dbcbe0bd1bf/tenor.gif?itemid=5459102",
        "https://media1.tenor.com/images/9ea72ef078139ced289852e8a4ea0c5c/tenor.gif?itemid=7537923",
        "https://media1.tenor.com/images/b82e6a78b221f7dc2e41605b6aa2cbcc/tenor.gif?itemid=11503720",
        "https://media1.tenor.com/images/79f33c2f524cbfed4ef6896b39e67663/tenor.gif?itemid=9416181",
        "https://media1.tenor.com/images/1bc74d686385dabe1e2076d5ace587fd/tenor.gif?itemid=13649735",
        "https://media1.tenor.com/images/d10c3d213be6893235d97ae768db8c07/tenor.gif?itemid=4608178",
        "https://media1.tenor.com/images/972424767943ed34a19f6ff2a9cbe976/tenor.gif?itemid=14192312",
        "https://media1.tenor.com/images/2ef78ab2f3e2acbf077388e26d3bc2da/tenor.gif?itemid=14815980",
        "https://media1.tenor.com/images/72d407300428e6f2ef3e469511d5f8ec/tenor.gif?itemid=5463317",
        "https://media1.tenor.com/images/f5cd33863e8319ea72990eefc8e697a8/tenor.gif?itemid=5417197",
        "https://media1.tenor.com/images/31a0eeab85c9a5cd27493607c2af4e89/tenor.gif?itemid=16402835",
        "https://media1.tenor.com/images/c30a364589dc6572b85135b1072e8247/tenor.gif?itemid=17060152",
        "https://media1.tenor.com/images/3cde3e1fe79e02abdc287395f57d8578/tenor.gif?itemid=16679443",
        "https://media1.tenor.com/images/e9e94cee9b2629f3feb499eff777547c/tenor.gif?itemid=17246368",
        "https://media1.tenor.com/images/5ff1438afccf129c7f22176e065b12aa/tenor.gif?itemid=12276833",
        "https://media1.tenor.com/images/6c910c695f97aff22ce82da1b3ccd050/tenor.gif?itemid=15089173",
        "https://media1.tenor.com/images/7df1f7c8107f7c4e2aa31fe20a7005a0/tenor.gif?itemid=18429940",
        "https://media1.tenor.com/images/a35527737a7cea9a682257eab848ef9a/tenor.gif?itemid=5118522",
        "https://media1.tenor.com/images/5d3cdb79cecb701cf5b54a34dc47d63a/tenor.gif?itemid=13510572",
        "https://media1.tenor.com/images/58707124f314cebc98639478e295ea66/tenor.gif?itemid=8644350",
        "https://media1.tenor.com/images/bd0220fc03b4ef9d88cb3843b0ab653d/tenor.gif?itemid=18129621",
        "https://media1.tenor.com/images/b8c554012161b234f7c3e28a630c8fc2/tenor.gif?itemid=18077996",
        "https://media1.tenor.com/images/900e502f7534a3756106655170ff6397/tenor.gif?itemid=12421971",
        "https://media1.tenor.com/images/a251caa1a2f4ca8db9da1ec9dfd95c2b/tenor.gif?itemid=13358680",
        "https://media1.tenor.com/images/399dfdd7e3dbbb1e8aafcc3bd5dbf4cd/tenor.gif?itemid=18429980",
        "https://media1.tenor.com/images/56976dab54f0f14b5d9b87d100091858/tenor.gif?itemid=17441907",
        "https://media1.tenor.com/images/cf0088a98ce0493052dcd9bb12d5e61c/tenor.gif?itemid=5473280",
        "https://media1.tenor.com/images/76402488ccf1f4daac62608add05467a/tenor.gif?itemid=13451206",
        "https://media1.tenor.com/images/bb3c7292d3c2e75ba4b51ec15bb9bf3b/tenor.gif?itemid=17227125",
        "https://thumbs.gfycat.com/HauntingNeighboringBarracuda-max-1mb.gif",
        "https://d.wattpad.com/story_parts/578941493/images/15316e3fc0408a2a31271600003.gif",
        "https://media1.tenor.com/images/33fdd8dc7564b56d5905428484f5aee4/tenor.gif?itemid=5604313",
        "https://media1.tenor.com/images/86a81a4a4e63afc759800f452b396787/tenor.gif?itemid=15151699",
        "https://media1.tenor.com/images/31f8ab4eab53b09da67b0216c4f8835e/tenor.gif?itemid=17120141",
        "https://media1.tenor.com/images/b0ee305bfadeb98752d7410688a7fcab/tenor.gif?itemid=12719749",
        "https://media1.tenor.com/images/49b1aa90b1a0b63ee3a89a651efdcd01/tenor.gif?itemid=14596996",
        "https://media1.tenor.com/images/8b00c464465b4ad9ead8db11ccdbdba2/tenor.gif?itemid=9905373",
        "https://media1.tenor.com/images/a5644e4f73314edf63146f3b0771fe01/tenor.gif?itemid=16325037",
        "https://media1.tenor.com/images/d6a2910107681d5d2deabf0b4d872906/tenor.gif?itemid=10548215",
        "https://media1.tenor.com/images/0f6922ce0e6bee7ddf0ecbab7cb4a053/tenor.gif?itemid=9214454",
        "https://media1.tenor.com/images/4306bcc66751c78d1ddbc659aae2ee97/tenor.gif?itemid=12434345",
        "https://media1.tenor.com/images/a856bb9811fa7b142a14d077b18b6fd7/tenor.gif?itemid=10410855",
        "https://media1.tenor.com/images/ed2fc3d868f4fe9e98cabe06647d8f96/tenor.gif?itemid=15834552",
        "https://media1.tenor.com/images/7ace4898fc03fa22b29cc512220d9d31/tenor.gif?itemid=17433381",
        "https://media1.tenor.com/images/6a9fe457a9bbadccc1a851a573923ee2/tenor.gif?itemid=8654074",
        
        ]
    gifff = random.randint(0,len(gifs)-1)
    img = gifs[gifff]
    
    if num1 == 1:
        frases_todos = [
            "has come to greet everyone",
            "wants to say hello to everyone",
            "sends you greetings!",
            "has greeted you !, return the greeting",
            "is happy to see you",
            "greets you!",
        ]
        
        sal2 = random.randint(0,len(frases_todos)-1)
        saludo2 = frases_todos[sal2]
        return (img, saludo2)
    
    elif num1 == 2:
        if num2 == 1:
            saludo = 'greeted me!!! Hello!! UwU'
            return (img, saludo)
        elif num2 == 2:
            saludo = 'say hi to'
            img = 'https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411'
            return (img, saludo)
        elif num2 == 3:
            frases_uno = [
                "greets you",
                "says hi to",
                "says hi to",
                "is very happy to see you",
                "has greeted you, return the greeting",
                "gives you a nice welcome",
                "is happy that you are back",
                "comes running to greet you",
                "greets you with affection",
                "is delighted to see you",
                "greets you happily",

            ]
            
            sal = random.randint(0,len(frases_uno)-1)
            saludo = frases_uno[sal]
            return (img, saludo)

def poke(num1, num2):

    if num1 == 1:
        text = 'You must tag someone'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'heeeey'
            text1 = 'dont poke meee \n（︶^︶）'
            return (text, text1)
        elif num2 == 2:
            text = 'pokes'
            return text
        elif num2 == 3:
            text = 'pokes'
            return text
        
def kiss(num1, num2):
    
    if num1 == 1:
        text = 'You must tag someone'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'h... ha.... has kissed me >~~<'
            return text
        elif num2 == 2:
            text = 'gives a kiss to'
            return text
        elif num2 == 3:
            text = 'gives a kiss to'
            return text

def slap(num1, num2):

    if num1 == 1:
        text = 'You must tag someone'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'Heey'
            text1 = 'What are you doing?\n Mitsuri slaps'
            return (text, text1)
        elif num2 == 2:
            text = 'slaps'
            return text
        elif num2 == 3:
            text = 'slaps'
            return text

def cuddle(num1, num2):
    
    if num1 == 1:
        text = 'You must tag someone'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = '>~~<'
            return text
        elif num2 == 2:
            text = 'cluddle with'
            return text
        elif num2 == 3:
            text = 'cluddle with'
            return text

def hug(num1, num2):

    if num1 == 1:
        text = 'You must tag someone'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'huuuug,'
            text1 = 'gives a hug to'
            return (text, text1)
        elif num2 == 2:
            text = 'gives a hug to'
            return text
        elif num2 == 3:
            text = 'gives a hug to'
            return text

def pat(num1, num2):

    if num1 == 1:
        text = 'You must tag someone'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = '>~~<'
            return text
        elif num2 == 2:
            text = 'gives some pats to'
            return text
        elif num2 == 3:
            text = 'gives some pats to'
            return text

def baka(num1, num2):

    if num1 == 1:
        text = 'You must tag someone'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'Youuuuu are BAKAA'
            return text
        elif num2 == 2:
            text = 'BAKAA¿¿??'
            return text
        elif num2 == 3:
            text = 'BAKAA'
            return text

def feed(num1, num2):

    if num1 == 1:
        text = 'You must tag someone'
        return text
    elif num1 == 2:
        if num2 == 1:   
            text = 'Yaai!!'
            text1 = 'has fed me!'
            return (text, text1)
        elif num2 == 2:
            text = 'has fed me!'
            return text
        elif num2 == 3:
            text = 'has fed me!'
            return text

def tickle(num1, num2):

    if num1 == 1:
        text = 'You must tag someone'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'Heeeyyy!!'
            text1 = 'do not tickle meeeee\n Mitsuri tickles'
            return (text, text1)
        elif num2 == 2:
            text = 'tickles'
            return text
        elif num2 == 3:
            text = 'le hace cosquillas a'
            return text

def smug():

    text = 'is showing off'
    return text

def run():

    text = 'ruuuunnn'
    return text

def dance(num1, num2):

    if num1 == 1:
        text = 'has started dancing!!'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'invited me to dance\nLets dance!! :3'
            return text
        elif num2 == 2:
            text = 'is dancing with'
            return text
        elif num2 == 3:
            text = 'is dancing with'
            return text


def angry(num1, num2):

    if num1 == 1:
        text = 'got angry >:('
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'What did I do now to make you angry with me?'
            return text
        elif num2 == 2:
            text = 'has been angry with'
            return text
        elif num2 == 3:
            text = 'has been angry with'
            return text

def revive(num1, num2):

    if num1 == 1:
        text = 'You must tag someone'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'What? where I am?, they have revived me :D'
            return text
        elif num2 == 2:
            text = 'has revived'
            return text
        elif num2 == 3:
            text = 'has revived'
            return text

def kill(num1, num2):

    if num1 == 1:
        text = 'You must tag someone'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'W... Wwh... What have you done... \n***dies***'
            return text
        elif num2 == 2:
            text = 'has killed'
            return text
        elif num2 == 3:
            text = 'has killed'
            return text

def sleep(num1, num2):
    
    if num1 == 1:
        text = 'has fallen asleep'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'yaaaii!! sleep with you'
            return text
        elif num2 == 2:
            text = 'goes to sleep with'
            return text
        elif num2 == 3:
            text = 'goes to sleep with'
            return text

def blush():

    text = 'has blushed >~~<'
    return text

def happy():

    text = 'is happy!!!'
    return text

def sad():

    text = 'is sad D:'
    return text

def laugh():

    text = 'is laughing a lot'
    return text

def cry():

    text = '... is crying T-T, What have they done to him?'
    return text

def confused():

    text = '... is confused??, do not understand... D:'
    return text

def bored():

    text = 'is bored... :('
    return text

def wallpaper(num1, num2):

    if num1 == 1:
        text = "You must write after mi!Wallpaper what you want to search"
        return text
    elif num1 == 2:
        if num2 == 1:
            name=f'Search wallpaper'
            value=f'Searching:'
            text=f'Wallpaper from wallhaven.cc'
            return (name, value, text)
        if num2 == 2:
            text = "No image related to the word found"
            return text


def dogo():

    text = 'Have a puppy'
    return text


def neko():

    text = 'Take a neko'
    return text


def bird():

    text = 'Have a biiird'
    return text

def tenor(num1):

    if num1 == 1:
        text = "You must write after mi!tenor what you want to search"
        return text
    elif num1 == 2:
        name=f'GIf from tenor'
        value=f'Searching:'
        text=f'Gif from tenor.com'

        return (name, value, text)

def ran_wall():

    name=f'Random wallpaper'
    value=f'Wallpaper id:'
    text=f'Wallpaper from wall.alphacoders.com\nIf wallpaper does not load, you can open this link'
    
    return (name, value, text)


def en_meme():

    name=f'English meme from Reddit'
    value=f'title:'
    text=f'Autor:'
    
    return (name, value, text)


def es_meme():

    name=f'Spanish meme'
    value=f'Reddit meme'
    
    return (name, value)


def wallpaper2(num1):

    if num1 == 1:
        text = "You must write after mi!wallpaper2 what you want to search"
        return text
    elif num1 == 2:
        name=f'Search wallpaper'
        value=f'Searching:'
        text=f'Wallpaper from wall.alphacoders.com\nIf wallpaper does not load, you can open this link'
        return (name, value, text)
    elif num1 == 3:
        text = "No image related to the word found"
        return text


def ranwaifu():

    text = 'Here you have your Random waifu >~<'
    return text

def ranneko():

    text = 'Here you have your Random Neko kawai >~<'
    return text

def invite():

    name=f':partying_face: :partying_face:  ¡Invite me to your Discord server! :partying_face: :partying_face:'
    value='\n----->¡We thank you for using Mitsuri!<-----\n----------->Here you have the invitation<------------\n------------>[¡invite me to your server!](https://discord.com/api/oauth2/authorize?client_id=761359894791192596&permissions=261993005047&scope=bot)<------------'
    text=f'¡La invitación pedida por:'
    text1='Thanks!'

    return (name, value, text, text1)


def ran_music():

    name='The type of music you should listen to is:'
    text = 'wants to listen to music!!'

    return (name, text)


def createinvite(num1):

    if num1 == 1:
        text = ("Infinite", "Infinite", "Infinite")
        return text
    elif num1 == 2:
        text = "Infinite"
        return text
    elif num1 == 3:
        name='¡Here is your invitation!'
        value=f'This invitation will be active for:\n\nHours:'
        value1 ='Minutes:'
        value2 = 'Seconds:'
        value3 = 'Uses:'
        text=f'->invitation created by:'
        return (name, value, value1, value2, value3, text)
    elif num1 == 4:
        text = "You have entered an invalid data in the command"
        return text

def createinvitedm(num1):

    if num1 == 1:
        text = ("Infinite", "Infinite", "Infinite")
        return text
    elif num1 == 2:
        text = "Infinite"
        return text
    elif num1 == 3:
        name='¡Here is your invitation!'
        value=f'This invitation will be active for:\n\nHours:'
        value1 ='Minutes:'
        value2 = 'Seconds:'
        value3 = 'Uses:'
        text=f'->invitation created by:'
        text1= 'I have sent you the invitation you asked for to the private chat'
        return (name, value, value1, value2, value3, text, text1)
    elif num1 == 4:
        text = "You have entered an invalid data in the command"
        return text


def avatar(num1):

    if num1 == 1:
        text = "Showing the avatar of:"
        return text
    elif num1 == 2:
        text = "Showing my avaaataarr!!"
        return text
    elif num1 == 3:
        text = "Showing the avatar of:"
        return text


def tr(num1):

    if num1 == 1:
        text = "You must put the language in which the message to be translated is written"
        return text
    elif num1 == 2:
        text = "You must put the language to which you want to translate the message"
        return text
    elif num1 == 3:
        text = "You must put the message you want to translate"
        return text
    elif num1 == 4:
        text = "You must put the message you want to translate"
        return text
    elif num1 == 5:
        title ='Translating:'
        name=f'Source language:'
        name1=f'Final language:'
        name2='Source message:'
        name3=f'Final message'
        return (title, name, name1, name2, name3)


def we(num1):

    if num1 == 1:
        text = "You must enter a country or city"
        return text
    elif num1 == 2:
        title=f'Weather in'

        name=f'Coordinates:'
        value=f'Length:'
        value1='Latitude:'

        name1=f'Weather:'
        value2=f'Description:'

        name2=f'Temperature:'
        value3=f'Actual temperature:'
        value4 = 'ºC\nThermal sensation:'
        value5 = 'ºC\nMinimum temperature:'
        value6 = 'ºC\nMaximum temperature:'

        name3=f'Humidity:'

        name4=f'Wind speed:'

        name5=f'Time zone:'

        return (title, name, value, value1, name1, value2, name2, value3, value4, value5, value6, name3, name4, name5)

def bugrep(num1):

    if num1 == 1:
        text = "The message about the bug is obligatory"
        return text
    elif num1 == 2:

        name=f'Reportó'

        name2='Nombre y tag:'

        name3='ID:'

        name4='mensaje:'

        name5=f'❌ | Bug report | ❌'

        name6=f'⚠ IMPORTANT ⚠'

        value1=f'When making this report we will take your name, your tag and your user id\nThese data will only be for the staff (The creator and the Mitsuri server staf)\nDo you want to continue?\n\n✅ : Yes\n❌ : No'

        return (name, name2, name3, name4, name5, name6, value1)

    elif num1 == 3:

        name=f'❌ | Bug report | ❌'

        name1='✅ | Message sent succesfully | ✅'

        value=f'I have sent the message to the Staff, they will contact you as soon as possible,♥ Thank you very much for using Mitsuri ♥'

        return (name, name1, value)

    elif num1 == 4:

        name=f'❌ | Bug report | ❌'

        name1='❌ | No message has been sent | ❌'

        value=f'We agree with your decision, you can join our server to make it more private and talk to a Staff\n♥ Thank you very much for using Mitsuri ♥'

        name2='Invitation to support server'

        value1=f'Here is the invitation to our support server to report the bug in person\n[Discord server support Mitsuri](https://discord.gg/GaXZgPbdQC)'

        return (name, name1, value, name2, value1)


def supser():

    name='Servidor oficial de soporte de Mitsuri'
    value=f'Aquí te introduzco mi servidor de soporte\n ¿Qué hay dentro del servidor de soporte?\n\n------------->:heartpulse: Mitsuri Bot Oficial :heartpulse: <-------------\n-----------------------------------------------------------\nʚ∙Soporte en Español e Ingles\nʚ∙Anuncios\nʚ∙Ticket Directos o Privados\nʚ∙Reportes de Bugs\nʚ∙Prueba de Comandos\n-----------------------------------------------------------\n:incoming_envelope: Invitación/Inivte :incoming_envelope:\n[Invitación al servidor de soporte](https://discord.gg/dYMhtbq7Jr)\n\n:white_check_mark: ---->Votar/Vote<---- :white_check_mark:\n[Página de top.gg para votar por Mitsuri](https://top.gg/bot/761359894791192596)\n-----------------------------------------------------------'

    return (name, value)


def servericon(num1):

    if num1 == 1:
        name = "This server has no icon"
        return name
    elif num1 == 2:
        title='¡¡Here is the server icon!!'
        text='->The icon has been requested by:'

        return (title, text)

def serverinfo(num1):
    if num1 == 1:
        name='Server name:'

        name2='Server ID:'

        name3='Region:'

        name4='Server owner:'

        name5='Verification level:'

        name6='Actual state:'

        name7='Members:'

        name8='Channels, categories:'

        name9='Text channels:'

        name10='Voice channels:'

        name11='Roles:'

        name12='Highest role:'

        name13='Number of emojis:'

        name14='Created:'

        name15='server icon:'

        text=f'Information requested by'

        name16='Online'

        return (name, name2, name3, name4, name5, name6, name7, name8, name9, name10, name11, name12, name13, name14, name15, text, name16)

    elif num1 == 2:

        name='Server name:'

        name2='Server ID:'

        name3='Region:'

        name4='Server owner:'

        name5='Verification level:'

        name6='Actual state:'

        name7='Members:'

        name8='Channels, categories:'

        name9='Text channels:'

        name10='Voice channels:'

        name11='Roles:'

        name12='Highest role:'

        name13='Number of emojis:'

        name14='Created:'

        name15='server icon:'

        text=f'Information requested by'

        name16='Online'

        name17= 'No icon'

        return (name, name2, name3, name4, name5, name6, name7, name8, name9, name10, name11, name12, name13, name14, name15, text, name16, name17)


def profile():

    name=f'Profile of'

    name1='Name and tag:'

    name2='ID:'

    name3='Nickname:'

    name4='Highest role:'

    name5='Account created on:'

    name6='On the server since:'

    name7='Roles:'

    text=f'Information requested by'

    return (name, name1, name2, name3, name4, name5, name6, name7, text)
    
def ping():

    title="Latecia"

    name=f"Message:"
    value='ms between message and message'

    name1=f"Mitsuri:"
    value1='ms between discord and mitsuri'

    text=f'Latency requested by:'

    return (title, name, value, name1, value1, text)

def vote():

    name=f':star_struck:  thank you very much for your support :star_struck:'
    value='\nㅤㅤㅤㅤㅤㅤㅤ>¡Yaaaaaaiiiii!<ㅤㅤㅤㅤㅤㅤㅤㅤㅤ\nㅤㅤㅤㅤㅤㅤ>Here you have the link<ㅤㅤㅤㅤㅤㅤㅤ\nㅤㅤㅤㅤㅤㅤ>[MITSURI TOP.GG](https://top.gg/bot/761359894791192596/vote)<ㅤㅤㅤㅤㅤㅤㅤ'
    text=f'Vote requested by:'
    text1='Thanks!'

    return (name, value, text, text1)

def feedback():

    name=f':inbox_tray: ¿Do you have any suggestion? :inbox_tray:'
    value='\nㅤㅤㅤㅤㅤㅤㅤㅤ>¡Thanks a lot<ㅤㅤㅤㅤㅤㅤㅤㅤㅤ\nㅤㅤ>Here is the link to suggest things<ㅤㅤ\nㅤㅤㅤㅤㅤㅤㅤㅤ>[MITSURI GITHUB](https://github.com/Skynext280/mitsuri-issues/issues)<ㅤㅤㅤㅤㅤㅤㅤㅤㅤ'
    text=f'Link requested by:'
    text1='Thanks!'

    return (name, value, text, text1)

def pages_of(num1):
    if  num1 == 0:
        name = 'you must enter a doujinshi number'
        return name
    if num1 == 1:
        name = 'calm bro the number'
        name2 = 'not published yet, but you have'
        name3 = 'Doujins to enjoy :smirk: :smirk:'
        return (name, name2, name3)
    elif num1 == 2:
        name = 'The H:'
        name2 = 'has'
        name3 = 'pages'
        return (name, name2, name3)
    elif num1 == 3:
        name = 'What are you trying to do...'
        name2 = '\n\ntry to put the command on a channel tagged as NSFW'
        return (name, name2)

def sauce_cont(num1):
    if num1 == 1:
        name = "Exist "
        name2 = " sauces(Doujins to read!!)"
        return (name, name2)
    elif num1 == 2:
        name = 'What are you trying to do...'
        name2 = '\n\ntry to put the command on a channel tagged as NSFW'
        return (name, name2)

def nhentai_read(num1):
    if num1 == 1:
        text = "You must enter a valid page"
        return text
    elif num1 == 2:
        text = "You must enter the number of the H you want to read"
        return text
    elif num1 == 3:
        name ='calm beast the number'
        name2 = 'not published yet, but you have'
        name3 = 'Doujins to enjoy :smirk: :smirk:'
        return (name, name2, name3)
    elif num1 == 4:
        text = "You must enter the page number of the H"
        return text
    elif num1 == 5:
        text = "That doujinshi has disallowed tags, violates discord terms and conditions, i can't show it"
        return text
    elif num1 == 6:
        name = 'You are reading the H:'
        name2 = 'This Doujin has'
        name3 = f'pages\n You are reading the page---> {1}'
        name4 = 'Nhentai reading mode'
        return (name, name2, name3, name4)
    elif num1 == 7:
        name = 'You are reading the H:' 
        name2 = 'This Doujin has'
        name3 = f'pages\n You are reading the page--->'
        name4 = 'Nhentai reading mode'
        return (name, name2, name3, name4)
    elif num1 == 8:
        name = 'Page does not exist'
        name2 = 'in the H:'
        name3 = ', this Doujin has'
        name4 = 'pages'
        return (name, name2, name3, name4)
    elif num1 == 9:
        name = 'You are reading the H:'
        name2 = 'This Doujin has'
        name3 = 'pages\n You are reading the page--->'
        return (name, name2, name3)
    elif num1 == 10:
        name = 'What are you trying to do...'
        name2 = '... \n\ntry to put the command on a channel tagged as NSFW'
        return (name, name2)

def cum(num1, num2):
    if num1 == 1:
        text = 'came'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'I don\'t think you should do that'
            return text
        elif num2 == 2:
            text = 'has come in'
            return text
        elif num2 == 3:
            text = 'has come in'
            return text

def kuni(num1, num2):
    if num1 == 1:
        text = 'You must tag someone'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'I don\'t think you should do that'
            return text
        elif num2 == 2:
            text = 'licks/sucks the member of'
            return text
        elif num2 == 3:
            text = 'licks/sucks the member of'
            return text

def suck(num1, num2):
    if num1 == 1:
        text = 'You must tag someone'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'I don\'t think you should do that'
            return text
        elif num2 == 2:
            text = 'licks/sucks the member of'
            return text
        elif num2 == 3:
            text = 'licks/sucks the member of'
            return text

def anal(num1, num2):
    if num1 == 1:
        text = 'You must tag someone'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'I don\'t think you should do that'
            return text
        elif num2 == 2:
            text = 'does an anal to'
            return text
        elif num2 == 3:
            text = 'does an anal to'
            return text        

def masturb(num1, num2):
    if num1 == 1:
        text = 'is masturbating'
        return text

def feets(num1, num2):
    if num1 == 1:
        text = 'Enjoy them'
        return text



