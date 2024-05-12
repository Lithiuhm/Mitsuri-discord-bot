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

def lang_comprove():
    name=f'🌟 | Important | 🌟'
    value=f'**ES:**\nNo tienes idioma seleccionado con Mitsuri en este servidor\n**USA:** `mi!lang [es]`\n\n**EN:**\nYou have no language selected with Mitsuri on this server\n**USE:** `mi!lang [en]`\n\n**FR:**\nVous n\'avez pas de langue sélectionnée avec Mitsuri sur ce serveur\n**UTILISE:** `mi!lang [fr]`'
    return (name, value)

def help(num1, num2):
    #Segunda fila
    title=":heartpulse: Aquí tienes una lista de todos mis comandos :heartpulse:\n -----------------> :beginner: Disfrutalo :beginner: <-----------------"
    
    #primera fila
    name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️'
    
    #tercera fila
    value=f'Si quieres los comandos por privado escribe `{prefijo}commands`\n Ó también puedes usar el comando `{prefijo}nodmcommands` para \nmostrar los comandos en el canal actual\n\nPara cambiar el idioma usa `mi!lang`\n\nTambién puedes reaccionar en las reacciones de abajo para pasar\nde página y ver los comandos por categoría 💕\n'
    
    #cuarta fila
    #primera columna
    name1=f':bookmark_tabs:  Info! :bookmark_tabs: \n `{prefijo}help_info` \n\n:underage: NSFW :underage:\n`{prefijo}help_nsfw` \n\n :books: Útiles :books:\n`{prefijo}help_useful`'
    value1=f'---------------------'
    
    #quinta fila
    #segunda columna
    name2=f':book: Leer Doujinshi :book:\n `{prefijo}help_read` \n\n:game_die:Entretenimiento:game_die: \n`{prefijo}help_games`\n\n :notes: Música :notes:\n`{prefijo}help_music`'
    value2=f'-------------------------'
    
    #sexta fila
    #tercera columna
    name3=f':camera_with_flash: Media :camera_with_flash:\n`{prefijo}help_media` \n\n:revolving_hearts: Reacciones :revolving_hearts: \n`{prefijo}help_reacts`\n\n:hammer: moder :hammer:\n`{prefijo}help_moder`'
    value3=f'------------------------'
    
    #septima fila
    name4=':incoming_envelope: Invitación :incoming_envelope: `/` :sos: :point_right: Ayuda :point_left: :sos:'
    value4='[--->Invitación<---](https://discord.com/api/oauth2/authorize?client_id=761359894791192596&permissions=2051014001&scope=bot) `/` [------>Ayuda<------](https://discord.gg/dYMhtbq7Jr)'
    
    #ocatava fila
    name5='>Donaciones< `/` ---->Votar<----'
    value5='[>Donaciones<](https://www.paypal.com/paypalme/skynext280)  `/` [---->Votar<----](https://top.gg/bot/761359894791192596)'

    #novena fila
    text="Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    if num2 == 0:
        return (title, name, value, name1, value1, name2, value2, name3, value3, name4, value4, name5, value5, text)

    elif num2 == 2:
        
        #segunda fila
        title=":heartpulse:Aquí tienes una lista de comandos de información:heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"
        
        #primera fila
        name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

        #tercera fila
        name2=f':bookmark_tabs: Información :bookmark_tabs:'
        value=f'```Comandos de información \n{prefijo}servicon\n{prefijo}serverinfo\n{prefijo}profile (Mencionar a alguien)\n{prefijo}ping\n{prefijo}vote\n{prefijo}feedback\n{prefijo}partners\n{prefijo}bughunter```'

        #footer
        text="Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

        return (title, name, name2, value, text)

    elif num2 == 3:

        #segunda fila
        title=":heartpulse:Aquí tienes una lista de comandos de NSFW:heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"

        #primera fila
        name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

        #tercera fila
        name1=f'INFORMACIÓN IMPORTANTE'
        value1=f'```TODOS ESTOS COMANDOS DE NSFW LOS ESTAMOS IMPLEMENTADO, EN LAS SIGUIENTES VERSIONES ESTÁN DISPONIBLES PARA SU USO```'

        #cuarta fila
        name2=f':underage: NSFW :underage:'
        value2=f'```Comandos NSFW que funcionan\n{prefijo}cum (Mencionar a alguien)```'

        #quinta fila
        name3=f'Próximos comandos'
        value3=f'```\n{prefijo}r34, ,{prefijo}r34gif, {prefijo}ran_coin, {prefijo}furro_coin, {prefijo}kuni, {prefijo}kunir, {prefijo}bj, {prefijo}bjr, {prefijo}anal, {prefijo}analr, {prefijo}masturb, {prefijo}rh, {prefijo}feets, {prefijo}erotic, {prefijo}nsfwneko, {prefijo}yuri, {prefijo}boobs, {prefijo}pussy, {prefijo}avatar, {prefijo}nsfwavatar, {prefijo}foxgirl, {prefijo}trap, {prefijo}ahegao, {prefijo}hentai```'

        #footer
        text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

        return (title, name, name1, value1, name2, value2, name3, value3, text)

    elif num2 == 4:
        
        #segunda fila
        title=":heartpulse: Aquí tienes una lista de comandos Útiles :heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"
        
        #primera fila
        name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

        #tercera fila
        name1=f':books: Útiles :books:'
        value=f'```Comandos útiles \n{prefijo}invite\n{prefijo}createinvite [tiempo] [usos]\n{prefijo}createinvitedm [tiempo] [usos]\n{prefijo}avatar (Mencionar a alguien)\n{prefijo}tr [Lenguaje origen] [Lenguaje final] [Mensaje]\n{prefijo}bugrep [Mensaje del error o sugerencia]\n{prefijo}supser\n{prefijo}we [Ciudad/País]```'

        #footer
        text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"


        return (title, name, name1, value, text)

    elif num2 == 5:
        
        #segunda fila
        title=":heartpulse:Aquí tienes una lista de comandos para leer Doujins:heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"
        
        #primera fila
        name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

        #tercera fila
        name1=f':book: Leer Doujinshis :book:'
        value=f'```Comandos Leer doujinshis\n{prefijo}nhentai_read [Número del doujinshi] [página (puede ser un número para leer una página en concreto o "all" si quieres leerlo todo)]\n{prefijo}pages_of [Número del doujinshi]\n{prefijo}sauce_cont [Número del doujinshi]```'

        #footer
        text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"


        return (title, name, name1, value, text)

    elif num2 == 6:

        #segunda fila
        title=":heartpulse: Aquí tienes una lista de comandos de juegos :heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"

        #primera fila
        name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

        #tercera fila
        name1=f':game_die: Entretenimiento :game_die:'
        value=f'```Comandos de juegos \n{prefijo}coin\n{prefijo}8ball [Pregunta]\n{prefijo}yon [Pregunta]\n{prefijo}dado\n{prefijo}connect4 [Mencionar a alguien]```'

        #footer
        text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"


        return (title, name, name1, value, text)

    elif num2 == 7:

        #segunda fila  
        title=":heartpulse: Aquí tienes una lista de comandos de música :heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"

        #primera fila
        name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

        #cuarta fila
        name2=f':notes: Música :notes:'
        value2=f'```Comandos de música \n{prefijo}p ó {prefijo}play [¿Qué quieres escuchar?(funcionan también links de youtube)]\n{prefijo}pa ó {prefijo}pause\n{prefijo}r ó {prefijo}res\n{prefijo}s ó {prefijo}stop```'

        #footer
        text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

        return (title, name, name2, value2, text)

    elif num2 == 8:

        #segunda fila
        title=":heartpulse: Aquí tienes una lista de comandos de media :heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"

        #primera fila
        name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

        #tercera fila
        name1=f':camera_with_flash: Media :camera_with_flash:'
        value=f'```Comandos de media \n{prefijo}wallpaper [¿Qué quieres buscar?]\n{prefijo}wallpaper2 [¿Qué quieres buscar?]\n{prefijo}dogo\n{prefijo}neko\n{prefijo}bird\n{prefijo}tenor [¿Qué quieres buscar?]\n{prefijo}en_meme\n{prefijo}es_meme\n{prefijo}ran_wall\n{prefijo}ranwaifu\n{prefijo}megumin\n{prefijo}character [¿A quién estás buscando?]\n{prefijo}ranneko```'

        #footer
        text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

        return (title, name, name1, value, text)


    elif num2 == 9:

        #segunda fila
        title=":heartpulse: Aquí tienes una lista de comandos de reacciones :heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"

        #primera fila
        name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

        #tercera fila
        name1=f':revolving_hearts: Reacciones :revolving_hearts:'
        value=f'```Comandos de reacciones \n\nMención obligatória:\n{prefijo}poke [mencionar a alguien]\n{prefijo}kiss [mencionar a alguien]\n{prefijo}slap [mencionar a alguien]\n{prefijo}cuddle [mencionar a alguien]\n{prefijo}hug [mencionar a alguien]\n{prefijo}pat [mencionar a alguien]\n{prefijo}baka [mencionar a alguien]\n{prefijo}feed [mencionar a alguien]\n{prefijo}tickle [mencionar a alguien]\n{prefijo}punch [mencionar a alguien]\n{prefijo}think [mencionar a alguien]\n\nMención opcinal:\n{prefijo}hi (Mencionar a alguien)\n{prefijo}dance (mencionar a alguien)\n{prefijo}angry (mencionar a alguien)\n{prefijo}sleep (mencionar a alguien)\n\nSin mención:\n{prefijo}smug\n{prefijo}run\n{prefijo}blush\n{prefijo}happy\n{prefijo}sad\n{prefijo}laugh\n{prefijo}cry\n{prefijo}confused\n{prefijo}bored\n{prefijo}fbi```'

        #footer
        text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

        return (title, name, name1, value, text)

    elif num2 == 10:    

        #segunda fila
        title=":heartpulse: Aquí tienes una lista de comandos de moder :heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"

        #primera fila
        name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

        #tercera fila
        name1=f':hammer: Moderación :hammer:'
        value=f'```Comandos de moderación \nDentro de pocoooo```'

        #footer
        text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

        return (title, name, name1, value, text)

def command():

    #segunda fila
    title=":heartpulse: Aquí tienes una lista de todos mis comandos :heartpulse:\n -----------------> :beginner: Disfrutalo :beginner: <-----------------"

    #primera fila
    name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

    #tercera fila
    name1=f':star_struck: Ayudas :star_struck: '
    value1=f'```Comandos de ayuda\n{prefijo}help_info\n{prefijo}help_nsfw\n{prefijo}help_useful\n{prefijo}help_read\n{prefijo}help_games\n{prefijo}help_music\n{prefijo}help_media\n{prefijo}help_reacts\n{prefijo}help_moder```'
    
    #cuarta fila
    name2=f':bookmark_tabs: Información :bookmark_tabs:'
    value2=f'```Comandos de información \n{prefijo}servicon\n{prefijo}serverinfo\n{prefijo}profile (Mencionar a alguien)\n{prefijo}ping\n{prefijo}vote\n{prefijo}feedback\n{prefijo}partners\n{prefijo}bughunter```'
    
    #quinta fila
    name3=f':book: Leer Doujinshis :book:'
    value3=f'```Comandos Leer doujinshis\n{prefijo}nhentai_read [Número del doujinshi] [página (puede ser un número para leer una página en concreto o "all" si quieres leerlo todo)]\n{prefijo}pages_of [Número del doujinshi]\n{prefijo}sauce_cont [Número del doujinshi]```'
    
    #sexta fila
    name4=f':game_die: Entretenimiento :game_die:'
    value4=f'```Comandos de juegos \n{prefijo}coin\n{prefijo}8ball [Pregunta]\n{prefijo}yon [Pregunta]\n{prefijo}dado\n{prefijo}connect4 [Mencionar a alguien]```'
    
    #octava fila
    name6=f':notes: Música :notes:'
    value6=f'```Comandos de música \n{prefijo}p ó {prefijo}play [¿Qué quieres escuchar?(funcionan también links de youtube)]\n{prefijo}pa ó {prefijo}pause\n{prefijo}r ó {prefijo}res\n{prefijo}s ó {prefijo}stop```'
    
    #Novena fila
    name7=f':camera_with_flash: Media :camera_with_flash:'
    value7=f'```Comandos de media \n{prefijo}wallpaper [¿Qué quieres buscar?]\n{prefijo}wallpaper2 [¿Qué quieres buscar?]\n{prefijo}dogo\n{prefijo}neko\n{prefijo}bird\n{prefijo}tenor [¿Qué quieres buscar?]\n{prefijo}en_meme\n{prefijo}es_meme\n{prefijo}ran_wall\n{prefijo}ranwaifu\n{prefijo}megumin\n{prefijo}character [¿A quién estás buscando?]\n{prefijo}ranneko```'
    
    #decima fila
    name8=f':revolving_hearts: Reacciones :revolving_hearts:'
    value8=f'```Comandos de reacciones \n\nMención obligatória:\n{prefijo}poke [mencionar a alguien]\n{prefijo}kiss [mencionar a alguien]\n{prefijo}slap [mencionar a alguien]\n{prefijo}cuddle [mencionar a alguien]\n{prefijo}hug [mencionar a alguien]\n{prefijo}pat [mencionar a alguien]\n{prefijo}baka [mencionar a alguien]\n{prefijo}feed [mencionar a alguien]\n{prefijo}tickle [mencionar a alguien]\n{prefijo}punch [mencionar a alguien]\n{prefijo}think [mencionar a alguien]\n\nMención opcinal:\n{prefijo}hi (Mencionar a alguien)\n{prefijo}dance (mencionar a alguien)\n{prefijo}angry (mencionar a alguien)\n{prefijo}sleep (mencionar a alguien)\n\nSin mención:\n{prefijo}smug\n{prefijo}run\n{prefijo}blush\n{prefijo}happy\n{prefijo}sad\n{prefijo}laugh\n{prefijo}cry\n{prefijo}confused\n{prefijo}bored\n{prefijo}fbi```'
    
    #undécima fila
    name9=f':hammer: Moderación :hammer:'
    value9=f'```Comandos de moderación \nDentro de pocoooo```'
    
    #dodecima fila
    name10=f'INFORMACIÓN IMPORTANTE'
    value10=f'```TODOS ESTOS COMANDOS DE NSFW LOS ESTAMOS IMPLEMENTADO, EN LAS SIGUIENTES VERSIONES ESTÁN DISPONIBLES PARA SU USO```'
    
    #tridecima fila
    name11=f':underage: NSFW :underage:'
    value11=f'```Comandos NSFW que funcionan\n{prefijo}cum (Mencionar a alguien)```'
    
    #cuatridécima fila
    name12=f'Próximos comandos'
    value12=f'```\n{prefijo}r34, ,{prefijo}r34gif, {prefijo}ran_coin, {prefijo}furro_coin, {prefijo}kuni, {prefijo}kunir, {prefijo}bj, {prefijo}bjr, {prefijo}anal, {prefijo}analr, {prefijo}masturb, {prefijo}rh, {prefijo}feets, {prefijo}erotic, {prefijo}nsfwneko, {prefijo}yuri, {prefijo}boobs, {prefijo}pussy, {prefijo}avatar, {prefijo}nsfwavatar, {prefijo}foxgirl, {prefijo}trap, {prefijo}ahegao, {prefijo}hentai```'

    #quitidécima fila
    name13=f':incoming_envelope: --------------Invitame a tu servidor de discord-------------- :incoming_envelope:'
    value13=f'[---------------------->Aquí tienes la invitación<---------------------](https://discord.com/api/oauth2/authorize?client_id=761359894791192596&permissions=2051014001&scope=bot)'
    
    #sextigésima fila
    name14=f':trophy:  ---------------------->Votame porfiiii<----------------------- :trophy: '
    value14=f'[-------------------->Entraaaa y votamee porfiiii<-------------------](https://top.gg/bot/761359894791192596)'

    #septigésima fila
    name15=f':no_entry_sign: :infinity:  Si tienes algún comentario o problema con el bot :infinity:  :no_entry_sign: '
    value15=f'[----------------------->Entra y ponlo por aquí<----------------------](https://github.com/Skynext280/mitsuri-issues/issues)'

    #octagésima fila
    name16=f':sos: :point_right: --------Únete a nuestro servidor de discord-------- :point_left: :sos:'
    value16=f'[----------------------->Píncha aquí para unirte<---------------------](https://discord.gg/dYMhtbq7Jr)'

    #nonadécima fila
    name17=f':moneybag: ----------------------Si quieres apoyarnos-------------------- :moneybag:'
    value17=f'[---------------------->Puedes donar por paypal<--------------------](https://www.paypal.com/paypalme/skynext280)'

    #footer
    text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    #dm
    msg = "te he Envíado todos mis comandos al chat privado"
    
    return (title, name, name1, value1, name2, value2, name3, value3, name4, value4, name6, value6, name7, value7, name8, value8, name9, value9, name10, value10, name11, value11, name12, value12, name13, value13, name14, value14, name15, value15, name16, value16, name17, value17, msg, text)

def help_nsfw():

    #segunda fila
    title=":heartpulse: Aquí tienes una lista de comandos de NSFW :heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

    #tercera fila
    name1=f'INFORMACIÓN IMPORTANTE'
    value1=f'```TODOS ESTOS COMANDOS DE NSFW LOS ESTAMOS IMPLEMENTADO, EN LAS SIGUIENTES VERSIONES DE MITSURI LAS PONDREMOS EN LINEA```'

    #cuarta fila
    name2=f':underage: NSFW :underage:'
    value2=f'```Comandos NSFW que funcionan\n {prefijo}r34 (Lo que quieras buscar)\n Envía un gif/imagen de rule 34 de lo que quieras buscar o random si no especificas que quieres busacar\n\n{prefijo}ran_coin\n Tiras una moneda y Envía un gif/img de rule34 según caiga la moneda\n\n{prefijo}furro_coin\n Tiras una moneda y evía un gif/img de rule 34 de un furro según caiga la moneda\n\n{prefijo}cum (etiquetar a alguien)\n Te vienes en una persona, no es obligatorio etiquetar alguien, te puedes venir sol@```'

    #quinta fila
    name3=f'Próximos comandos'
    value3=f'```\n{prefijo}r34, ,{prefijo}r34gif, {prefijo}ran_coin, {prefijo}furro_coin, {prefijo}kuni, {prefijo}kunir, {prefijo}bj, {prefijo}bjr, {prefijo}anal, {prefijo}analr, {prefijo}masturb, {prefijo}rh, {prefijo}feets, {prefijo}erotic, {prefijo}nsfwneko, {prefijo}yuri, {prefijo}boobs, {prefijo}pussy, {prefijo}avatar, {prefijo}nsfwavatar, {prefijo}foxgirl, {prefijo}trap, {prefijo}ahegao, {prefijo}hentai```'       

    #footer
    text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, name2, value2, name3, value3, text)


def help_read():

    #segunda fila
    title=":heartpulse: Aquí tienes una lista de comandos para leer Doujins :heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

    #tercera fila
    name1=f':book: leer doujins :book:'
    value1=f'```Comandos para Leer Doujins\n{prefijo}nhentai_read [Número del doujinshi] [página (puede ser un número o "all" si quieres leerlo todo)]\n Puedes leer el doujin que quieras, siempre y cuando vaya acorde con los terminos de servicio de Discord\n\n{prefijo}pages_of [número del Doujin]\n Envía el número de páginas que tiene el doujin introducido\n\n{prefijo}sauce_cont [número del Doujin]\n Envía la cantidad de doujins que existen```'

    #footer
    text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, text)


def help_info():

    #segunda fila
    title=":heartpulse: Aquí tienes una lista de comandos de información :heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

    #tercera fila
    name1=f':bookmark_tabs:  Info! :bookmark_tabs:'
    value1=f'```Comandos de información \n{prefijo}servicon\n Envía el icono del servidor actual\n\n{prefijo}serverinfo\n Envía una descripción detallada del servidor actual\n\n{prefijo}profile (mencionar a alguien)\n Envía una descripción detallada una persona del servidor o tuya si no especificas persona\n\n{prefijo}ping\n Muestra el ping entre mensaje y mensaje, y el ping de Mitsuri\n\n{prefijo}vote\n Envía el link de la página de top.gg de Mitsuri!, a votarle!\n\n{prefijo}feedback\n Envía un link de github para reportar cualquier error o sugerencia\n\n{prefijo}partners\n Envía una descripción de todos nuestros partners\n\n{prefijo}bughunter\n Envía una lista con nuestros ayudantes que han aportado ideas y encontrado bugs para mejorar el bot```'

    #footer
    text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, text)

def help_media():

    #segunda fila
    title=":heartpulse: Aquí tienes una lista de comandos de media/imgs :heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '
    
    #tercera fila
    name1=f':camera_with_flash: Media :camera_with_flash:'
    value1=f'```Comandos de media \n{prefijo}wallpaper [¿Qué quieres buscar?]\n Envía un wallpaper de lo que quieras buscar\n\n{prefijo}wallpaper2 [¿Qué quieres buscar?]\n Este comando está puesto por si no encuentra foto con el comando {prefijo}wallpaper\n\n{prefijo}dogo\n Envía un perritooo \n\n{prefijo}neko\n Envía un gatiitoo\n\n{prefijo}bird\n Envía un pajaritoo\n\n{prefijo}tenor [¿Qué quieres buscar?]\n Envía un gif random de tenor de lo que quieras buscar\n\n{prefijo}en_meme\n Envía un meme en inglés de reddit\n\n{prefijo}es_meme\n Envía un meme en español de reddit\n\n{prefijo}ran_wall\n Envía un wallpaper random\n\n{prefijo}ranwaifu\n Envía una waifu random\n\n{prefijo}megumin\n Megumin >~<\n\n{prefijo}character [¿A quién estás buscando?]\n Envía una foto del personaje que elegiste!\n\n{prefijo}ranneko\n Envía una neko kawaii random```'

    #footer
    text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, text)

def help_games():

    #segunda fila
    title=":heartpulse:Aquí tienes una lista de comandos de juegos/game:heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

    #tercera fila
    name1=f':game_die: Entreteiment :game_die:'
    value1=f'```Comandos de juegos \n{prefijo}coin \n Tiras una moneda y puede caer cara o cruz\n\n{prefijo}_8ball [pregunta]\n Hazle una pregunta a Mitsuri, ella te la responderá! \n\n{prefijo}yon [pregunta]\n Hazle una pregunta a Mitsuri, te responderá con un sí o un no\n\n{prefijo}dice\n Tiras un dado de 6 caras\n\n{prefijo}connect4 [menciona a alguien]\n Un simple juego de conectar 4 fichas del mismo color```'

    #footer
    text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, text)

def help_music():

    #segunda fila
    title=":heartpulse: Aquí tienes una lista de comandos de música :heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

    #cuarta fila
    name2=f':notes: Music :notes:'
    value2=f'```Comandos de música \n{prefijo}p ó {prefijo}play [¿Qué quieres escuchar?(Links de youtube funcionanan también)]\n Reproduce música en un canal\n\n{prefijo}pa ó {prefijo}pause\n Pausa la canción que esté sonando\n\n{prefijo}r ó {prefijo}res\n Reanuda la canción que estaba sonando\n\n{prefijo}s ó {prefijo}stop\n Detiene la canción que esté sonando```'

    #footer
    text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name2, value2, text)


def help_moder():
    
    #segunda fila
    title=":heartpulse: Aquí tienes una lista de comandos de moder :heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

    #tercera fila
    name1=f':hammer: moder :hammer:'
    value1=f'```Comandos de moderación \nDentro de pocoooo```'

    #footer
    text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, text)


def help_reacts():

    #segunda fila
    title=":heartpulse: Aquí tienes una lista de comandos de reactions :heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

    #tercera fila
    name1=f':revolving_hearts: Reactions :revolving_hearts:\n**--------------------------Mención obligatória--------------------------**'
    value1=f'```{prefijo}poke [mencionar a alguien] \n Pincha o chincha al usuario mencionado \n\n{prefijo}kiss [mencionar a alguien] \n Le das un beso al usuario mencionado \n\n{prefijo}slap [mencionar a alguien] \n Le das una bofetada al usuario mencionado \n\n{prefijo}cuddle [mencionar a alguien] \n Dale un achuchon o acurruca teal en el usuario mencionado \n\n{prefijo}hug [mencionar a alguien] \n Dale un abrazo al usuario mencionado \n\n{prefijo}pat [mencionar a alguien] \n Dale unas caricias al usuario mencionado \n\n{prefijo}baka [mencionar a alguien] \n Llama idiota (baka en japones) al usuario mencionado \n{prefijo}feed [mencionar a alguien] \n Un usuario pasa hambre? dale de comer con este comando \n\n{prefijo}tickle [mencionar a alguien] \n Un amigo está triste? ¡¡Pues unas bueanas cosquillas le ayudaran¡¡ \n\n{prefijo}punch [mencionar a alguien] \n Le das un golpe a alguien```'

    #cuarta fila
    name2=f'**----------------------------Mención opcinal-----------------------------**'
    value2=f'```\n{prefijo}hi (Mencionar a alguien) \n Saluda a un amigo o saluda a todos los usuarios \n\n{prefijo}dance (mencionar a alguien) \n Echate unos bailes solo o acompañado si mencionas a un usuario \n\n{prefijo}angry (mencionar a alguien) \n Muestra tu enfado mas vil mencionando a un usuario o enfádate por algo sin mencionar \n\n{prefijo}sleep (mencionar a alguien) \n Te quedaste dormido o… duerme con el usuario mencionado >~<```'
    
    #quinta fila
    name3=f'**-------------------------------Sin mención-------------------------------**'
    value3=f'```\n{prefijo}smug \n Presume de quien eres yeaaah! \n\n{prefijo}run \n Corre corre que te pillan \n\n{prefijo}blush \n Si te sacan los colores con palabras bonitas sonrojate a gusto \n\n{prefijo}happy \n Explota de felicidad \n\n{prefijo}sad \n Todos tenemos dias en el que nos puede la melancolia (triste) \n\n{prefijo}laugh \n Ríete tanto como quieras o puedas con este comando \n\n{prefijo}cry \n Te han roto el corazón… Pues llora tanto como quieras \n\n{prefijo}confused \n estas confundido…? No entiendes…? \n\n{prefijo}bored \n No sabes que hacer?, te sientes aburrido?, este es tu comando \n\n{prefijo}fbi \n FBI OPEN UP! \n\n{prefijo}think\n En que piensas?```'

    #footer
    text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, name2, value2, name3, value3,text)

def help_useful():

    #segunda fila
    title=":heartpulse: Aquí tienes una lista de comandos de usefull :heartpulse:\n ---------------------> :beginner: Disfrutalo :beginner: <---------------------"

    #primera fila
    name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

    #tercera fila
    name1=f':books: Usefull :books:'
    value1=f'```Comandos de útiles \n{prefijo}invite \n Envía un mensaje por si quieres invitarme a tu servidor de discord\n\n {prefijo}createinvite [tiempo] [usos]\n Crea una invitación del canal actual y lo envía en el mismo canal\n\n {prefijo}createinvitedm [tiempo] [usos]\n Crea una invitación del canal actual y te lo envía por privado\n\n{prefijo}avatar (menciaona a alguien)\n Envía el avatar de la persona etiquetada o el tuyo si no etiquetas a nadie\n\n{prefijo}tr [Lenguaje origen] [Lenguaje final] [Mensaje]\n Traduce un texto de un idioma a otro\n\n{prefijo}bugrep [Mensaje del bug]\n Si tienes algún problema o has encontrado algún bug en Mitsuri envíanoslo\n\n{prefijo}supser\n Envía una descripción sobre el servidor oficial de soporte de Mitsuri, el link de invitación y el link de la página de top.gg de Mitsuri \n\n{prefijo}we [Ciudad/País] \n Envía información detallada del tiempo en ese lugar```'

    #footer
    text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, text)


def help_lang():

    #segunda fila
    title=":heartpulse: Aquí tienes una lista de idiomas del traductor :heartpulse:\n --------------------> :beginner: Disfrutalo :beginner: <--------------------"

    #primera fila
    name=f'\n ❤️ Te damos gracias por usar Mitsuri  ❤️ '

    #tercera fila
    name1=f':books: Traductor :books:'
    value1=f'Idiomas'

    #footer
    text=f"Creador \n✪ I\'m Sʞʎuǝxʇ (҂⌣̀_⌣́)#7181"

    return (title, name, name1, value1, text)


def moneda(num1):
    
    if num1 == 1:
        coin = 'Ha caído cara'
    elif num1 == 2:
        coin = 'Ha caído cruz'

    return coin

def _8ball(num1 ,question):
    
    if num1 ==1:
        text = "tienes que hacerme una pregunta"
        return text
    elif num1 == 2:

        responses = ['En mi opinión, sí',
            'Es cierto',
            'Es decididamente así',
            'Probablemente',
            'Buen pronóstico',
            'Todo apunta a que sí',
            'Sin duda',
            'Sí',
            'Sí - definitivamente',
            'Debes confiar en ello',
            'Respuesta vaga, vuelve a intentarlo',
            'Pregunta en otro momento',
            'Será mejor que no te lo diga ahora',
            'No puedo predecirlo ahora',
            'Concéntrate y vuelve a preguntar',
            'Puede ser',
            'No cuentes con ello',
            'Mi respuesta es no',
            'Mis fuentes me dicen que no',
            'Las perspectivas no son buenas',
            'Muy dudoso'
            ]

        respuesta = random.choices(responses)
        respuesta = respuesta[0]

        a = f'Pregunta: {question}\nRespuesta: {respuesta}'

        return a


def yon(num1, question):

    if num1 == 1:
        text = "tienes que hacerme una pregunta"
        return text
    elif num1 == 2:
        responses = ["Sí", "No"]
        respuesta = random.choices(responses)
        respuesta = respuesta[0]

        a = f'Pregunta: {question}\nRespuesta: {respuesta}'
        
        return a

def dado():

    ent = random.randint(1, 6)

    a = f'El dado ha caido y ha salido el número: {ent}'

    return a


def connect4():

    uno = "No puedes jugar tu solo"
    dos = "quiere jugar una partida de juntar 4 en raya. Tienes 30 segundos para aceptar la patida!"
    tres = "Se ha pasado el tiempo, vuelve a intentarlo"
    cuatro = "A jugar!\nEl primer jugador es:"
    cinco = "Tu color es el amarillo!"
    seis = "El juego empezará enseguida"
    siete = "**__Turno de__**"
    ocho = "**Siguiente**"
    nueve = "Ha ganado esta partida !!\nMuy bien jugado"
    diez = "Ha estado interesante"
    once = "y"

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
            "ha venido a saludar a todos",
            "quiere darles a todos un saludo",
            "les manda saludos!",
            "les ha saludado!, vamos a devolverle el saludo",
            "está felíz de verles",
            "les saluda!",
            "ha vueltoo!",
            "acaba de llegar!"
        ]
        
        sal2 = random.randint(0,len(frases_todos)-1)
        saludo2 = frases_todos[sal2]
        return (img, saludo2)
    
    elif num1 == 2:
        if num2 == 1:
            saludo = 'me ha saludado!!!, holaa!! UwU'
            return (img, saludo)
        elif num2 == 2:
            saludo = 'saluda a'
            img = 'https://media1.tenor.com/images/474f0313fb10879f146bcfdacc5bdf8f/tenor.gif?itemid=13451411'
            return (img, saludo)
        elif num2 == 3:
            frases_uno = [
                "te saluda",
                "saluda a",
                "ha venido corriendo a saludarte",
                "está muy feliz de verte",
                "te ha saludado, devuelvele el saludo",
                "te da una agradable bienvenida",
                "está feliz de que hayas vuelto",
                "viene corriendo a saludarte",
                "te saluda con cariño",
                "está encantad@ de verte",
                "te saluda felizmente"
            ]
            
            sal = random.randint(0,len(frases_uno)-1)
            saludo = frases_uno[sal]
            return (img, saludo)

def poke(num1, num2):

    if num1 == 1:
        text = 'Debes mencionar a alguien'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'Oyeeeee'
            text1 = 'no me pinchees \n（︶^︶）'
            return (text, text1)
        elif num2 == 2:
            text = 'pincha a'
            return text
        elif num2 == 3:
            text = 'pincha a'
            return text
        
def kiss(num1, num2):
    
    if num1 == 1:
        text = 'Debes mencionar a alguien'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'm... mee.... mee ha besado >~~<'
            return text
        elif num2 == 2:
            text = 'le da un beso a'
            return text
        elif num2 == 3:
            text = 'le da un beso a'
            return text

def slap(num1, num2):

    if num1 == 1:
        text = 'Debes mencionar a alguien'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = '¿Oyeeee'
            text1 = 'que haces?\n Mitsuri le da una bofetada a'
            return (text, text1)
        elif num2 == 2:
            text = 'le da una bofetada a'
            return text
        elif num2 == 3:
            text = 'le da una bofetada a'
            return text

def cuddle(num1, num2):
    
    if num1 == 1:
        text = 'Debes mencionar a alguien'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = '>~~<'
            return text
        elif num2 == 2:
            text = 'se acurruca en'
            return text
        elif num2 == 3:
            text = 'se acurruca en'
            return text

def hug(num1, num2):

    if num1 == 1:
        text = 'Debes mencionar a alguien'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'abrazooooooo,'
            text1 = 'le da un abrazo a'
            return (text, text1)
        elif num2 == 2:
            text = 'le da un abrazo a'
            return text
        elif num2 == 3:
            text = 'le da un abrazo a'
            return text

def pat(num1, num2):

    if num1 == 1:
        text = 'Debes mencionar a alguien'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = '>~~<'
            return text
        elif num2 == 2:
            text = 'le da unas caricias a'
            return text
        elif num2 == 3:
            text = 'le da unas caricias a'
            return text

def baka(num1, num2):

    if num1 == 1:
        text = 'Debes mencionar a alguien'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'BAKAA TUU'
            return text
        elif num2 == 2:
            text = 'BAKAA¿¿??'
            return text
        elif num2 == 3:
            text = 'BAKAA'
            return text

def feed(num1, num2):

    if num1 == 1:
        text = 'Debes mencionar a alguien'
        return text
    elif num1 == 2:
        if num2 == 1:   
            text = 'Yeeiiii!!'
            text1 = 'me ha dado de comeer! :3'
            return (text, text1)
        elif num2 == 2:
            text = 'le da de comer a'
            return text
        elif num2 == 3:
            text = 'le da de comer a'
            return text

def tickle(num1, num2):

    if num1 == 1:
        text = 'Debes mencionar a alguien'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'Oyeee!!'
            text1 = 'no me hagas cosquilaaaaasss\n Mitsuri le hace cosquillas a'
            return (text, text1)
        elif num2 == 2:
            text = 'le hace cosquillas a'
            return text
        elif num2 == 3:
            text = 'le hace cosquillas a'
            return text

def smug():

    text = 'está presumiendo'
    return text

def run():

    text = 'Correeeee'
    return text

def dance(num1, num2):

    if num1 == 1:
        text = 'se ha puesto a bailaaar!!'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'me ha invitado a bailaar\nA bailaar!! :3'
            return text
        elif num2 == 2:
            text = 'está bailando con'
            return text
        elif num2 == 3:
            text = 'está bailando con'
            return text


def angry(num1, num2):

    if num1 == 1:
        text = 'se ha enfadado >:('
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'Que hice yo ahora para que te enfadaras conmigoo??'
            return text
        elif num2 == 2:
            text = 'se ha enfadado con'
            return text
        elif num2 == 3:
            text = 'se ha enfadado con'
            return text

def revive(num1, num2):

    if num1 == 1:
        text = 'Debes mencionar a alguien'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = '¿Qué? donde estoy, me han revividoo :D'
            return text
        elif num2 == 2:
            text = 'ha revivido a'
            return text
        elif num2 == 3:
            text = 'ha revivido a'
            return text

def kill(num1, num2):

    if num1 == 1:
        text = 'Debes mencionar a alguien'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'q... qqu... quee haas hecho... \n***se muere***'
            return text
        elif num2 == 2:
            text = 'ha matado a'
            return text
        elif num2 == 3:
            text = 'ha matado a'
            return text

def sleep(num1, num2):
    
    if num1 == 1:
        text = 'se ha quedado dormi@'
        return text
    elif num1 == 2:
        if num2 == 1:
            text = 'yeeeii!! a dormirr contigoo'
            return text
        elif num2 == 2:
            text = 'se va a dormir con'
            return text
        elif num2 == 3:
            text = 'se va a dormir con'
            return text

def blush():

    text = 'se ha sonrojado >~~<'
    return text

def happy():

    text = 'está feliiiiz!!!'
    return text

def sad():

    text = 'está triiiste D:'
    return text

def laugh():

    text = 'se está muriendo de risa'
    return text

def cry():

    text = '... está llorando T-T, ¿Qué le habrán hecho?'
    return text

def confused():

    text = '... está confundidoo??, no entender... D:'
    return text

def bored():

    text = 'está aburrid@... :('
    return text

def wallpaper(num1, num2):

    if num1 == 1:
        text = "Debes escribir despues de mi!wallpaper lo que quieres buscar"
        return text
    elif num1 == 2:
        if num2 == 1:
            name=f'Búsqueda wallpaper'
            value=f'Buscando:'
            text=f'Wallpaper de wallhaven.cc'
            return (name, value, text)
        if num2 == 2:
            text = "No se ha encontrado imagen relacionada con la palabra"
            return text


def dogo():

    text = 'Toma un dogooo'
    return text


def neko():

    text = 'Tomaa un nekooo'
    return text


def bird():

    text = 'Tomaa un pajaritoooo'
    return text

def tenor(num1):

    if num1 == 1:
        text = "Debes escribir despues de mi!tenor lo que quieres buscar"
        return text
    elif num1 == 2:
        name=f'GIf de tenor'
        value=f'Buscando:'
        text=f'Gif de tenor.com'

        return (name, value, text)

def ran_wall():

    name=f'Wallpaper random'
    value=f'id del wallpaper:'
    text=f'Wallpaper de wall.alphacoders.com\nSi no carga el wallpaper puede abrir este enlace'
    
    return (name, value, text)


def en_meme():

    name=f'Meme de Reddit'
    value=f'título:'
    text=f'Autor:'
    
    return (name, value, text)


def es_meme():

    name=f'Meme en español'
    value=f'Reddit meme'
    
    return (name, value)


def wallpaper2(num1):

    if num1 == 1:
        text = "Debes escribir despues de mi!wallpaper2 lo que quieres buscar"
        return text
    elif num1 == 2:
        name=f'Búsqueda wallpaper'
        value=f'Buscando:'
        text=f'Wallpaper de wall.alphacoders.com\nSi no carga el wallpaper puede abrir este enlace'
        
        return (name, value, text)
    elif num1 == 3:
        text = "No se ha encontrado imagen relacionada con la palabra"
        return text


def ranwaifu():

    text = 'Aquí tienes tu Waifu random >~<'
    return text

def ranneko():

    text = 'Aquí tienes tu Neko kawaii random >~<'
    return text

def invite():

    name=f':partying_face: :partying_face:  ¡Invitame a tu servidor de Discord! :partying_face: :partying_face:'
    value='\n----->¡Te damos gracias por usar Mitsuri!<-----\n----------->Aqui tienes la invitación<------------\n------------>[¡invítame a tu servidor!](https://discord.com/api/oauth2/authorize?client_id=761359894791192596&permissions=2051014001&scope=bot)<------------'
    text=f'¡La invitación pedida por:'
    text1='Gracias!'

    return (name, value, text, text1)


def ran_music():

    name='El genero de música que deberías escuchar es:'
    text = 'quiere escuchar musiicaa!!'

    return (name, text)


def createinvite(num1):

    if num1 == 1:
        text = ("Infinito", "Infinito", "Infinito")
        return text
    elif num1 == 2:
        text = "infinito"
        return text
    elif num1 == 3:
        name='¡Aquí tienes tu invitación!'
        value=f'Esta invitación estará activa durante:\n\nHoras:'
        value1 ='Minutos:'
        value2 = 'Segundos:'
        value3 = 'Usos:'
        text=f'->invitación creada por:'
        return (name, value, value1, value2, value3, text)
    elif num1 == 4:
        text = "Hás introducido un dato inválido en el comando"
        return text

def createinvitedm(num1):

    if num1 == 1:
        text = ("Infinito", "Infinito", "Infinito")
        return text
    elif num1 == 2:
        text = "infinito"
        return text
    elif num1 == 3:
        name='¡Aquí tienes tu invitación!'
        value=f'Esta invitación estará activa durante:\n\nHoras:'
        value1 ='Minutos:'
        value2 = 'Segundos:'
        value3 = 'Usos:'
        text=f'->invitación creada por:'
        text1= 'te he Envíado la invitación que me pediste al chat privado'
        return (name, value, value1, value2, value3, text, text1)
    elif num1 == 4:
        text = "Hás introducido un dato inválido en el comando"
        return text


def avatar(num1):

    if num1 == 1:
        text = "Mostrando el avatar de:"
        return text
    elif num1 == 2:
        text = "Mostrando mi avaaataarr!!"
        return text
    elif num1 == 3:
        text = "Mostrando el avatar de:"
        return text


def tr(num1):

    if num1 == 1:
        text = "Debes poner el lenguaje en el que está escrito el mensaje a traducir"
        return text
    elif num1 == 2:
        text = "Debes poner el lenguaje al que quieres traducir mensaje"
        return text
    elif num1 == 3:
        text = "Debes poner el mensaje que quieres traducir"
        return text
    elif num1 == 4:
        text = "El lenguaje introducido es incorrecto, para saber más idiomas mi!help_lang"
        return text
    elif num1 == 5:
        title ='Traduciendo:'
        name=f'Idioma origen:'
        name1=f'Idioma final:'
        name2='mensaje origen:'
        name3=f'mensaje final'

        return (title, name, name1, name2, name3)


def we(num1):

    if num1 == 1:
        text = "Debes introducir un país o ciudad"
        return text
    elif num1 == 2:
        title=f'El tiempo en'

        name=f'Coordenadas:'
        value=f'Longitud:'
        value1='Latitud:'

        name1=f'Tiempo:'
        value2=f'Descripción:'

        name2=f'Temperatura:'
        value3=f'Temperatura actual:'
        value4 = 'ºC\nSensación térmica:'
        value5 = 'ºC\nTemperatura mínima:'
        value6 = 'ºC\nTemperatúra máxima:'

        name3=f'Humedad:'

        name4=f'Velocidad del viento:'

        name5=f'Zona horaria:'

        return (title, name, value, value1, name1, value2, name2, value3, value4, value5, value6, name3, name4, name5)

def bugrep(num1):

    if num1 == 1:
        text = "Es obligatorio el mensaje acerca del bug"
        return text
    elif num1 == 2:

        name=f'Reportó'

        name2='Nombre y tag:'

        name3='ID:'

        name4='mensaje:'

        name5=f'❌ | Reporte de bug | ❌'

        name6=f'⚠ IMPORTANTE ⚠'

        value1=f'Al hacer este reporte cogeremos tu nombre, tu tag y tu id de usuario\nEstos datos solo serán para el staf (El creador y el staf del servidor de Mitsuri)\n¿Quieres continuar?\n\n✅ : Sí\n❌ : No'

        return (name, name2, name3, name4, name5, name6, value1)

    elif num1 == 3:

        name=f'❌ | Reporte de bug | ❌'

        name1='✅ | Mensaje Envíado con éxito | ✅'

        value=f'He Envíado el mensaje al Staff, se pondrán en contacto contigo lo antes posible,♥ Muchas gracias por usar Mitsuri ♥'

        return (name, name1, value)

    elif num1 == 4:

        name=f'❌ | Reporte de bug | ❌'

        name1='❌ | No se ha Envíado ningún mensaje | ❌'

        value=f'Estamos de acuerdo con tu decision, puedes unirte a nuestro servidor para hacerlo más privado y hablar con un Staff\n♥ Muchas gracias por usar Mitsuri ♥'

        name2='Invitación al servidor de soporte'

        value1=f'Aquí tienes la invitación a nuestro servidor de soporte para reportar el bug en persona\n[Servidor de Discord soporte Mitsuri](https://discord.gg/GaXZgPbdQC)'

        return (name, name1, value, name2, value1)


def supser():

    name='Servidor oficial de soporte de Mitsuri'
    value=f'Aquí te introduzco mi servidor de soporte\n ¿Qué hay dentro del servidor de soporte?\n\n------------->:heartpulse: Mitsuri Bot Oficial :heartpulse: <-------------\n-----------------------------------------------------------\nʚ∙Soporte en Español e Ingles\nʚ∙Anuncios\nʚ∙Ticket Directos o Privados\nʚ∙Reportes de Bugs\nʚ∙Prueba de Comandos\n-----------------------------------------------------------\n:incoming_envelope: Invitación/Inivte :incoming_envelope:\n[Invitación al servidor de soporte](https://discord.gg/dYMhtbq7Jr)\n\n:white_check_mark: ---->Votar/Vote<---- :white_check_mark:\n[Página de top.gg para votar por Mitsuri](https://top.gg/bot/761359894791192596)\n-----------------------------------------------------------'

    return (name, value)


def servicon(num1):

    if num1 == 1:
        name = "Este servidor no tiene icono"
        return name
    elif num1 == 2:
        title='¡¡Aquí tienes el icono del servidor!!'
        text='->El icono ha sido pedido por:'

        return (title, text)

def serverinfo(num1):
    if num1 == 1:
        name='Nombre del servidor:'

        name2='ID del servidor:'

        name3='Región:'

        name4='Dueño del servidor:'

        name5='Nivel de verificación:'

        name6='Estado actual:'

        name7='Miembros:'

        name8='Canales y categorías:'

        name9='Canales texto:'

        name10='Canales voz:'

        name11='Roles:'

        name12='Rol más alto:'

        name13='Número de emojis:'

        name14='Creado el:'

        name15='icono del servidor:'

        text=f'Información pedida por'

        name16='En linea'

        return (name, name2, name3, name4, name5, name6, name7, name8, name9, name10, name11, name12, name13, name14, name15, text, name16)

    elif num1 == 2:

        name='Nombre del servidor:'

        name2='ID del servidor:'

        name3='Región:'

        name4='Dueño del servidor:'

        name5='Nivel de verificación:'

        name6='Estado actual:'

        name7='Miembros:'

        name8='Canales y categorías:'

        name9='Canales texto:'

        name10='Canales voz:'

        name11='Roles:'

        name12='Rol más alto:'

        name13='Número de emojis:'

        name14='Creado el:'

        name15='icono del servidor:'

        text=f'Información pedida por'

        name16='En linea'

        name17= 'Sin icono'

        return (name, name2, name3, name4, name5, name6, name7, name8, name9, name10, name11, name12, name13, name14, name15, text, name16, name17)


def profile():

    name=f'Perfil de'

    name1='Nombre y tag:'

    name2='ID:'

    name3='Apodo:'

    name4='Rol más alto:'

    name5='Cuenta creada el:'

    name6='En el servidor desde:'

    name7='Roles:'

    text=f'Información pedida por'

    return (name, name1, name2, name3, name4, name5, name6, name7, text)

def ping():

    title="Latecia"

    name=f"Mensaje:"
    value='ms entre mensaje y mensaje'

    name1=f"Mitsuri:"
    value1='ms entre discord y Mitsuri'

    text=f'Latencia pedida por:'

    return (title, name, value, name1, value1, text) 

def vote():

    name=f':star_struck:  ¿Enserio vas a votarme en top.gg? :star_struck: '
    value='\n--------------->¡Yeeeeeiiiii!<----------------\n----------->Aqui tienes el link<-------------\n----------->[MITSURI TOP.GG](https://top.gg/bot/761359894791192596/vote)<-------------'
    text=f'¡Votación pedida por:'
    text1='Gracias!'

    return (name, value, text, text1)

def feedback():

    name=f':inbox_tray: ¿Tienes alguna sugerencia? :inbox_tray:'
    value='\n--------------->¡Muchas gracias<----------------\n---->Aqui tienes el link para sugerir cositas<---\n-------------->[MITSURI GITHUB](https://github.com/Skynext280/mitsuri-issues/issues)<----------------'
    text=f'¡Link pedido por:'
    text1='Gracias!'

    return (name, value, text, text1)









































