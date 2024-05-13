
# Mitsuri un bot multifuncional para Discord

Mitsuri nació de la idea de dos amigos exactamente el 1 de octubre de 2020, creando un máximo de 10 comandos para aquel entonces, lo que significaba todo un éxito para nosotros. Al no tener mucha idea y teniendo que investigar, la base de Mitsuri fue programada ¡en menos de una semana! Mitsuri está programada en Python 3 en su totalidad, además de una base de datos implementada con MySQL. 

Hoy en día Mitsuri es un bot más avanzado de lo que solía ser, con funcionalidades extremadamente útiles y potentes, desde mostrar tu perfil hasta ofrecerte fondos de pantalla ¡de lo que desees! 



## Infraestructura 

La infraestructura de Mitsuri se puede dividir en 4 partes distintas e igualmente importantes:

### Discord

La rama principal de Mitsuri, Discord. Completamente escrito en Python 3 siendo la su prioridad es sacar el máximo  rendimiento y fiabilidad.

### Mitsuri API

API específica y personalizada para Mitsuri, configurada para permitir que todos los servicios de Mitsuri se comuniquen con tiempos de procesamiento extremadamente rápidos.


### APIs Externas

Escogiendo minusiosamente cada una de las APIs externas que usa Mitsuri para brindar el mejor servicio garantizando fiabilidad y disponibilidad.

### Página Web

El comienzo y el fin de todo. Toda la información sobre los comandos, módulos de eventos y soporte de Mitsuri resumida en un solo lugar para facilitar el acceso.



## Desempeño & Agradecimientos

Mitsuri en su conjunto, incluidas todas sus instancias, desarrolladores y ayudantes, se desempeña increíblemente bien. La mayor parte del tiempo de respuesta promedio está ocupada esperando datos de APIs de terceros para continuar.

El hardware dedicado con seguridad garantiza el máximo tiempo de actividad de todos los servicios. En situaciones de emergencia, Mitsuri está diseñada para apagar los servicios menos prioritarios con el fin de funcionar con los recursos disponibles a su máximo potencial.

Me gustaría finalizar agradeciendo a Kyshi  por su apoyo e inspiración ayudando a mejorar el código en los comienzos de Mitsuri. También a Bazelpon por contribución en la página de Top.gg. 

Además me gustaría dar las gracias a JappyDilema por la ayuda y apoyo proporcionado dibujos, arte e ideas creativas, lo que permite a Mitsuri lucir hermosa. Gracias a Lucy quien me ha dado muchas ideas de comandos para mejorar el bot y hacerlo más útil.

Este proyecto no estaría donde está ahora sin ustedes.


# Comandos

## Comandos de información

`/servericon`
Envía el icono del servidor actual

`/serverinfo`
Envía una descripción detallada del servidor actual

`/profile`
Envía una descripción detallada una persona del servidor o tuya si no especificas persona

`/ping`
Muestra el ping entre mensaje y mensaje, y el ping de Mitsuri

`/vote`
Envía el link de la página de top.gg de Mitsuri!, a votarle!

`/feedback`
Envía un link de github para reportar cualquier error o sugerencia

`/partners`
Envía una descripción de todos nuestros partners

`/bughunter`
Envía una lista con nuestros ayudantes que han aportado ideas y encontrado bugs para mejorar el bot


## Comandos de útiles

`/invite`
Envía un mensaje por si quieres invitarme a tu servidor de discord

`/createinvite [tiempo] [usos]`
Crea una invitación del canal actual y lo envía en el mismo canal 

`/createinvitedm [tiempo] [usos]`
Crea una invitación del canal actual y te lo envía por privado

`/ vatar (menciona a alguien)`
Envía el avatar de la persona etiquetada o el tuyo si no etiquetas a nadie

`/tr [Lenguaje origen] [Lenguaje final] [Mensaje]`
Traduce un texto de un idioma a otro

`/bugrep [Mensaje del bug]`
Traduce un texto de un idioma a otro

`/supser`
Envía una descripción sobre el servidor oficial de soporte de Mitsuri, el link de invitación y el link de la página de top.gg de Mitsuri

`/we [Ciudad/País]`
Envía información detallada del tiempo en ese lugar

## Comandos de juegos

`/coin`
Tiras una moneda y puede caer cara o cruz

`/8ball [pregunta]`
Send a detailed description of the current server

`/yon [pregunta]`
Hazle una pregunta a Mitsuri, te responderá con un sí o un no

`/dice`
Tiras un dado de 6 caras

`/connect4 [menciona a alguien]`
Un simple juego de conectar 4 fichas del mismo color

## Comandos de música 

`/play [¿Qué quieres escuchar?]`
Reproduce música en un canal

`/pause`
Pausa la canción que esté sonando

`/res`
Reanuda la canción que estaba sonando

`/stop`
Detiene la canción que esté sonando

## Comandos de media

`/wallpaper [¿Qué quieres buscar?]`
Envía un wallpaper de lo que quieras buscar

`/wallpaper2 [¿Qué quieres buscar?]`
Este comando está puesto por si no encuentra foto con el comando /wallpaper

`/dogo`
Envía un perritooo

`/neko`
Envía un gatiitoo

`/bird`
Envía un pajaritoo

`/tenor [¿Qué quieres buscar?]`
Envía un gif random de tenor de lo que quieras buscar

`/en_meme`
Envía un meme en inglés de reddit

`/es_meme`
Envía un meme en español de reddit

`/ran_wall`
Envía un wallpaper random

`/ranwaifu`
Envía una waifu random

`/megumin`
Megumin >~<

`/character [¿A quién estás buscando?]`
Envía una foto del personaje que elegiste!

`/ranneko`
Envía una neko kawaii random

## Comandos de reacciones

### Mención obligatória

`/poke [mencionar a alguien]`
Pincha o chincha al usuario mencionado 

`/kiss [mencionar a alguien]`
Le das un beso al usuario mencionado

`/slap [mencionar a alguien]`
Le das una bofetada al usuario mencionado

`/cuddle [mencionar a alguien]`
Dale un achuchon o acurruca teal en el usuario mencionado 

`/​hug [mencionar a alguien]`
Dale un abrazo al usuario mencionado

`/​​​pat [mencionar a alguien]`
Dale unas caricias al usuario mencionado

`/​baka [mencionar a alguien]`
Llama idiota (baka en japones) al usuario mencionado

`/​​​feed [mencionar a alguien]`
Un usuario pasa hambre? dale de comer con este comando

`/tickle [mencionar a alguien]`
Un amigo está triste? ¡¡Pues unas bueanas cosquillas le ayudaran!!

`/punch [mencionar a alguien]`
Le das un golpe a alguien

### Mención opcional

`/hi (Mencionar a alguien)`
Saluda a un amigo o saluda a todos los usuarios

`/​​​dance (mencionar a alguien)`
Echate unos bailes solo o acompañado si mencionas a un usuario

`/angry (mencionar a alguien)`
Muestra tu enfado mas vil mencionando a un usuario o enfádate por algo sin mencionar

`/​sleep (mencionar a alguien)`
Te quedaste dormido o… duerme con el usuario mencionado >~<

### Sin mención

`/​​smug`
Presume de quien eres yeaaah!

`/​run`
Corre corre que te pillan

`/​​blush`
Si te sacan los colores con palabras bonitas sonrojate a gusto 

`/​​happy`
Explota de felicidad

`/​​sad`
Todos tenemos dias en el que nos puede la melancolia (triste)

`/​​laugh`
Ríete tanto como quieras o puedas con este comando

`/​​cry` 
Te han roto el corazón… Pues llora tanto como quieras

`/​confused` 
estas confundido…? No entiendes…?  

`/​bored`  
No sabes que hacer?, te sientes aburrido?, este es tu comando

`/​​fbi` 
FBI OPEN UP! 



## Preguntas Frecuentes

#### ¿Puedo Invitar a Mitsuri a mi servidor de Discord?

Por supuesto, Mitsuri está disponible las 24 horas del día los 365 días del año para repartir felicidad y entretenimiento a todos los servidores que la necesiten.

Pincha [Aquí](https://discord.com/oauth2/authorize?client_id=761359894791192596&permissions=261993005047&scope=bot) para invitar a Mitsuri a tu servidor.

#### ¿Existe algún servidor de soporte?

Si, aquí puedes unirte, encontrarás las últimas actulizaciones, el estado, los planes a futuro, soporte especializado, y poder hablar con todo el equipo y colaboradores.

Pincha [Aquí](https://discord.com/invite/dYMhtbq7Jr) para unirte al servidor de soporte.

### ¿Qué es Top.gg y que tiene que ver con Mitsuri?

Top.gg comenzó como una lista única enfocada en los mejores Discord Bots. Ahora, casi 5 años después, se han convertido en la capa de descubrimiento para las comunidades e integraciones de Discord.

Mitsuri ha sido testeada en su totalidad por top.gg, lo que le da un punto más de fiablidad y seguridad.

También puede votar en Top.gg por Mitsuri pinchando [Aquí](https://top.gg/bot/761359894791192596).

### ¿El bot está verificado por Discord?

Si, una vez un bot de discord llega a los 100 servidores, no puede entrar en más servidores hasta haber pasado la revisión de los desarrolladores de Discord. Mitsuri está en más de 1000 servidores, lo que significa que Mitsuri pasó (hace mucho mucho tiempo) la revisión de discord lo que añade otro punto de fiabilidad y seguridad.

### ¡He encontrado un BUG! ¿Cómo puedo notificarlo?

Primero que todo muchas gracias por usar el bot y mejorar la experiencia de uso. Puedes notificar el problema haciendo uso del comando `/bugrep [Error o sugerencia]` o unirte al servidor oficial de soporte para notificarlo, obtendrás el rol especial de Bug Hunter!

### ¿Cómo puedo apoyar a Mitsuri?

Puedes apoyar a Mitsuri invitando al bot a todos los servidores que quieras y compartiéndolo con tus amigos, así el bot crecerá y más personas podrán hacer uso de el.

También puede votar en Top.gg por Mitsuri pinchando [Aquí](https://top.gg/bot/761359894791192596).

Además puedes donar la cantidad de dinero que tu desees pinchando [Aquí](https://www.paypal.com/paypalme/skynext280).
## Nuestro equipo

[Lithiuhm](https://github.com/Lithiuhm)
Creador Desarrollador

JappyDilema
Diseñadora Desarrolladora

[Lucy](https://github.com/Lucitlaly)
Contribuidora Desarrolladora

Kyshi
Contribuidor Desarrollador

[San1190](https://github.com/San1190)
Contribuidor

Rigel
Contribuidor Desarrollador



## License

[MIT](https://choosealicense.com/licenses/mit/)

