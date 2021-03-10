init python:
    ArminAmizade2 = 0
    ErenAmizade = 0
    HanjiAmizade3 = 0
    LeviAmizade4 = 0
    AnnieAmizade5 = 0
    ErwinAmizade6 = 0
    pontoAnterior = 0

# Coloca el código de tu juego en este archivo.
#Mouse personalisado
define config.mouse = {"default" : [("cursor_pointer.png", 0, 0)]}

# "Init; aquí se ponen códigos que
#cambian o crean aspectos del juego, por ejemplo aquí podemos crear un código que permita
#al jugador tener un sistema de puntos, o crear un efecto especial.

#Esta sección la llamaremos "declaración", los personajes deben ser declarados antes de poderse usar.
#Declara los personajes usados en el juego como en el ejemplo:

define m = Character("Mikasa")
define s = Character("Sasha", image="sasha")
define l = Character("Levi")
define e = Character("Eren")
define r = Character("Erwin")
define a = Character("Armin")
define k = Character("Mike")
define z = Character("Hange")
define je = Character("Jean")
define an = Character("Annie")
define cr = Character("Crista")
define co = Character("Connie")
define pe = Character("Petra")
define au = Character("Auruo")
define ba = Character("Zackly")
define se = Character("Chofer")
define so = Character("Soldado")
define ni = Character("Niña")
define lo = Character("Niño")
define de = Character("???")
define n = Character("")
define f = Character("Nifa")
define la = Character("Farlan")
define be = Character("Isabel")
define ke = Character("Sra.Ackerman")

image carta = "carta.png"
image Shasha Feliz = "Shasha Feliz.png"
image Shasha Pensando = "Shasha Pensando.png"
image Shasha Contenta = "Shasha Contenta.png"
image Eren enojado s = "Eren enojado s.png"
image Eren normal s = "Eren normal s.png"
image Eren preocupado s = "Eren preocupado s.png"
image Eren sorprendido s = "Eren sorprendido s.png"
image Eren incomodo s = "Eren incomodo s.png"
image Erwin normal c = "Erwin normal c.png"
image Armin disgustado s = "Armin disgustado s.png"
image Armin enojado s = "Armin enojado s.png"
image Armin enojado sce = "Armin enojado sce.png"
image Armin disgustado sce = "Armin disgustado sce.png"
image Errwin normal cba = "Errwin normal cba.png"
image Armin feliz c = "Armin feliz c.png"
image Armin disgustado c = "Armin disgustado c.png"
image Armin alegre c = "Armin alegre c.png"
image Armin soprendido1 s = "Armin soprendido1 s.png"
image Armin enojado sc = "Armin enojado sc.png"
image Eren normal c = "Eren normal c.png"
image Eren enojado2 c = "Eren enojado2 c.png"
image Armin disgustado cce = "Armin disgustado cce.png"
image Eren preocupado c = "Eren preocupado c.png"
image Eren enojado3 c = "Eren enojado3 c.png"
image Eren serio c = "Eren serio c.png"
image Eren enojado c = "Eren enojado c.png"
image Eren alegre c = "Eren alegre c.png"
image Levi normal c = "Levi normal c.png"
image Levi normal2 c = "Levi normal2 c.png"
image Hange alegre s = "Hange alegre s.png"
image Hange feliz s = "Hange feliz s.png"
image Hange gi1 s = "Hange gi1 s.png"
image Hange gi2 s = "Hange gi2 s.png"
image Hange hablando s = "Hange hablando s.png"
image Hange insegura s = "Hange insegura s.png"
image Hange normal s = "Hange normal s.png"
image Hange preocupada s = "Hange preocupada s.png"
image Hange seria s = "Hange seria s.png"
image Hange sorprendida1 s = "Hange sorprendida1 s.png"
image Hange sorprendida2 s = "Hange sorprendida2 s.png"
image Armin enojado cce = "Armin enojado cce.png"
image Errwin normal sba = "Errwin normal sba.png"
image Erwim feliz s = "Erwim feliz s.png"
image Erwin incomodo1 s = "Erwin incomodo1 s.png"
image Erwin incomodo2 s = "Erwin incomodo2 s.png"
image Erwin normal s = "Erwin normal s.png"
image Erwin normal1 s = "Erwin normal1 s.png"
image Levi normal s = "Levi normal s.png"
image Levi enojado s = "Levi enojado s.png"
image Levi enojado sbe = "Levi enojado sbe.png"
image Levi feliz s = "Levi feliz s.png"
image Levi hablando s = "Levi hablando s.png"
image Levi normal2 s = "Levi normal2 s.png"
image Levi sonrojado s = "Levi sonrojado s.png"
image Levi sorpendido s = "Levi sorpendido s.png"
image Levi suave2 s = "Levi suave2 s.png"
image Levi tranquilo s = "Levi tranquilo s.png"
image Armin feliz s = "Armin feliz s.png"
image Eren serio s = "Eren serio s.png"
image Armin hablando s = "Armin hablando s.png"
image Armin serio s = "Armin serio s.png"
image Eren enojado2 s = "Eren enojado2 s.png"
image Eren enojado3 s = "Eren enojado3 s.png"
image Levi preocupado s = "Levi preocupado s.png"
image Hange preocupada c = "Hange preocupada c.png"
image Hange insegura c = "Hange insegura c.png"
image Erwin incomodo2 c = "Erwin incomodo2 c.png"
image Erwin incomodo2 c = "Erwin incomodo2 c.png"
image Mikasa enojada c = "Mikasa enojada c.png"
image Mikasa feliz c = "Mikasa feliz c.png"
image Mikasa normal c = "Mikasa normal c.png"
image Mikasa sonrojada1 c = "Mikasa sonrojada1 c.png"
image Mikasa sonrojada2 c = "Mikasa sonrojada2 c.png"
image Erwim feliz c = "Erwim feliz c.png"
image Levi enojado cbe = "Levi enojado cbe.png"
image Levi hablando c = "Levi hablando c.png"
image Levi enojado c = "Levi enojado c.png"
image Levi preocupado c = "Levi preocupado c.png"
image Armin serio c = "Armin serio c.png"
image Armin tt s = "Armin tt s.png"
image Levi sonrojado c = "Levi sonrojado c.png"
image Armin tt c = "Armin tt c.png"
image Armin hablando c = "Armin hablando c.png"
image Annie triste s = "Annie triste s.png"
image Annie normal s = "Annie normal s.png"
image Annie preocupada s = "Annie preocupada s.png"
image Annie hablando s = "Annie hablando s.png"
image Annie feliz s = "Annie feliz s.png"
image Armin alegre s = "Armin alegre s.png"
image Armin sonrojado s = "Armin sonrojado s.png"
image Shasha hablando s = "Shasha hablando s.png"
image Shasha feliz s = "Shasha feliz s.png"
image Shasha Pensando s = "Shasha Pensando s.png"
image Shasha Contenta s = "Shasha Contenta s.png"
image Shasha sonrojada s = "Shasha sonrojada s.png"
image Annie sorprendida s = "Annie sorprendida s.png"
image Annie sonrojada s = "Annie sonrojada s.png"
image Eren llorando s = "Eren llorando s.png"
image Annie llorando s = "Annie llorando s.png"
image Mikasa enojada s = "Mikasa enojada s.png"
image Mikasa enojada2 s = "Mikasa enojada2 s.png"
image Mikasa enojada3 s = "Mikasa enojada3 s.png"
image Mikasa feliz s = "Mikasa feliz s.png"
image Mikasa hablando s = "Mikasa hablando s.png"
image Mikasa normal s = "Mikasa normal s.png"
image Mikasa sonrojada1 s = "Mikasa sonrojada1 s.png"
image Mikasa sonrojada2 s = "Mikasa sonrojada2 s.png"
image Mikasa triste s = "Mikasa triste s.png"
image Shasha gritando c = "Shasha gritando c.png"
image Hange hablando c = "Hange hablando c.png"
image Hange sorprendida2 c = "Hange sorprendida2 c.png"
image Mikasa hablando c = "Mikasa hablando c.png"
image Hange normal c = "Hange normal c.png"
image Hange gi1 c = "Hange gi1 c.png"
image Hange gi2 s = "Hange gi2 s.png"
image Mikasa triste c = "Mikasa triste c.png"
image Hange gi2 c = "Hange gi2 c.png"

######################################################################
#Sistema de Notify
default beach = False
default available_screens = ["notify1", "notify2", "notify3"]
default delay_done = True
default life = 100
default life_e = 100


# Muestra una imagen de fondo: Aquí se usa un marcador de posición por
# defecto. Es posible añadir un archivo en el directorio 'images' con el
# nombre "bg room.png" or "bg room.jpg" para que se muestre aquí.

define lili = "lili.png"
define taberna = "taberna.jpg"
define tarven = "tarven.jpg"
define pasteur_day = "pasteur_day.jpg"
define legion = "legion.jpg"
define chisme = "chisme.png"
define me = "me.png"
define mordida = "mordida.jpg"
define iluminacion = "iluminacion.jpg"
define ilumi = "ilumi.jpg"
define carruaje = "carruaje.png"
define cielo = "cielo.jpg"
define habita = "habita.jpg"


#carta de Erwin
screen documento:
    add "carta"
    textbutton "Continuar" action Jump("suite"):
        xalign 0.5
        yalign 0.9

# Presenta las líneas del diálogo.
# El juego comienza aquí. (linea amarilla) (NO borrar el label start, si no esta, renpy no puede correr el juego.

label start:
    call screen capitulos

    return

label capitulo1:
    $ contador = 0
    $allocate_screen("{color=#FFFFFF}¡No toques la pantalla!{/color}")
    play music "inicio.mp3"
    show text "{size=+25}{color=#FFFFFF}Capítulo 1{/color}{/size}" at truecenter
    with dissolve
    pause 4
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}Tomar una decisión{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    $allocate_screen("{color=#FFFFFF}¡Sube el volumen para escuchar conversaciones!{/color}")
    show text "{size=+30}{color=#ffc30f}¿Sasha ya ha despertado?{/size}{/color}" at truecenter
    with dissolve
    pause 26
    hide text
    scene img1
    with dissolve
    show text "{size=+30}{color=#000000}Sasha: ¡Ah! ¡Hola!{/size}{/color}" at truecenter:
        xpos 0.5 ypos 900
    with dissolve
    pause 1
    hide text
    with dissolve
    show text "{size=+30}{color=#000000}Sasha: ¿Me buscabas por algo?{/size}{/color}" at truecenter:
        xpos 0.5 ypos 900
    with dissolve
    pause 3
    hide text
    with dissolve
    show text "{size=+30}{color=#000000}Eren: ¡Aquí estás! ¡Por fin!{/size}{/color}" at truecenter:
        xpos 0.5 ypos 900
    pause 1
    with dissolve
    hide text
    with dissolve
    show text "{size=+30}{color=#000000}*Sasha: Ah, bueno... hoy no puede ser.*{/size}{/color}" at truecenter:
        xpos 0.5 ypos 900
    with dissolve
    pause 1
    hide text
    with dissolve
    show text "{size=+30}{color=#000000}Sasha: Tengo que... ¡Sí! Tengo que... ¡Hacer algo! ¡Algo importante!{/size}{/color}" at truecenter:
        xpos 0.5 ypos 900
    with dissolve
    pause 3
    hide text
    with dissolve
    show text "{size=+30}{color=#000000}Eren: ¿Qué te pasa, Sasha? ¿Te duelen los dientes? De repente suenas rara...{/size}{/color}" at truecenter:
        xpos 0.5 ypos 900
    with dissolve
    pause 8
    hide text
    with dissolve
    show text "{size=+30}{color=#000000}Sasha: ¡...! Eh... O sea... ¿Vale? Vamos a bordar este entrenamiento. ¿O no? Y después la hora de comer.{/size}{/color}" at truecenter:
        xpos 0.5 ypos 900
    with dissolve
    pause 15
    hide text
    show taberna
    with dissolve
    show screen quick_menu
    stop music
    m "{cps=24}...{/cps}"
    with fade
    play music "musica normal.mp3" loop
    show Shasha Feliz
    with dissolve
    s "Mikasa... ya has despertado."
    m "Buenos días."
    s "Buenos días."
    show Shasha Contenta
    with dissolve
    s "Hoy habrá carne para el desayuno."
    m "..."
    play sound "pasa.mp3"
    show Shasha Feliz
    with dissolve
    s "... ¿Qué pasa?"
    m "Creí que te preocuparía más el entrenamiento de hoy que la comida."
    n "Me puse en pie para comenzar a vestirme."
    show Shasha Pensando
    with dissolve
    s "¡Sé que el entrenamiento es importante!"
    show Shasha Feliz
    with dissolve
    s "Pero es raro que haya carne como desayuno y que no sea un evento especial."
    m "De cualquier manera tú comes lo que sea, no veo qué te preocupa."
    n "Me puse las botas."
    show Shasha Pensando
    with dissolve
    s "Tan fría como siempre, Mikasa..."
    show tarven
    with dissolve
    play music "murmurando.mp3"
    n "Llegamos al comedor, el cual se encontraba ya lleno."
    n "Parece que el hecho de que haya carne como desayuno..."
    n "animó a todos a levantarse temprano con tal de recibir su porción y no quedarse con las ganas."
    n "Ojeé todo el comedor en busca de una persona, Eren."
    n "Me acerqué a la mesa en la que estaba Eren sentado junto con Armin y Connie."
    $contador = 0
    show Eren normal s
    with dissolve
    play sound "eren.mp3"
    m "¡Eren!"
    m "¿Ya comiste algo?"
    python:
        ErenAmizade += 40
    call chamarBarraMais(ErenAmizade)
    play sound "ah eren.mp3"
    show Eren sorprendido s
    with dissolve
    e "¿¡Ah!?"
    show Eren incomodo s
    with dissolve
    e "Eh, Mikasa..."
    show Eren preocupado s
    with dissolve
    e "¡No eres mi madre para decirme qué hacer!"
    e "Yo decido si quiero comer o no."
    m "Pero Eren... Es importante que comas algo..."
    play sound "de que estas hablando.mp3"
    show Eren incomodo s
    with dissolve
    e "¿De qué estás hablan-"
    m "Ya que el entrenamiento de hoy será muy duro y no podrás aguantarlo."
    show Eren preocupado s
    with dissolve
    e "¿Cuántas veces te lo he dicho? ¡No soy tu hermano pequeño al que tienes que proteger! Así que déjalo ya, ¿vale?"

menu:
    "¿Qué debía responder?"

    "...":
        show Eren normal s
        with dissolve
        show text "{size=+20}{color=#EFC12D}¡Has ganado +10!{/size}{/color}" at truecenter:
            xpos 402 ypos 60
        with dissolve
        python:
            ErenAmizade += 10
        call chamarBarraMais(ErenAmizade)
        with dissolve
        hide text
        with dissolve
        n "Desde hace tiempo Eren comenzó a tratarme de esa forma: me gritaba, me empujaba, me hacía a un lado..."
        jump correc

    "¡Pero yo...!":
        show Eren enojado s
        with dissolve
        show text "{size=+20}{color=#EFC12D}¡Has perdido -10 puntos!{/size}{/color}" at truecenter:
            xpos 402 ypos 60
        with dissolve
        python:
            ErenAmizade -= 10
        call chamarBarraMenos(ErenAmizade)
        play sound "oi.mp3"
        with hpunch
        hide text
        with dissolve
        n "Recalqué colocando mis manos sobre sus hombros, pero él las quitó de inmediato bruscamente."
        n "Me miraba con desprecio y hasta podría decir que con odio."
        play sound "se realista.mp3"
        e "¡Sé realista, Mikasa!"
        play sound "no me importa.mp3"
        e "¡A nadie le importa lo que quieras!"
        play sound "golpe mesa.mp3"
        with hpunch
        n "Gritó golpeando la mesa, provocando que todos nos miraran."
        show Eren preocupado s
        with dissolve
        play sound "sorry.mp3"
        m "Lo siento..."
        hide screen barraAmizade
        show Eren normal s
        with dissolve
        n "Desde hace tiempo Eren comenzó a tratarme de esa forma: me gritaba, me empujaba, me hacía a un lado..."
        jump incorrec

label incorrec:
n "No lo entendía, lo único que quería era protegerlo."
n "Pero a él le molestaba eso. Yo sabía que Eren no era un niño, solo quería cumplir parte de mi promesa con Carla."
n "Proteger a Eren incluso a costa de mi vida, pero últimamente sus acciones me afectaban de cierta manera."
n "Al punto de perder esa personalidad que tanto me caracterizaba estando frente a otras personas."
n "Con él me volvía débil; me sentía frágil y a punto de romperme, como un jarrón que cae al suelo."
n "Sus palabras hirientes sonaban todo el tiempo en mi cabeza."
n "Y me hacían pensar varias veces qué era lo que estaba haciendo mal."
n "Claramente me preocupaba mucho y por eso siempre estaba pendiente de él."
label correc:
n "El silencio era tan incómodo que me daban ganas de salir de ahí corriendo."
n "Ser el centro de atención era una de las sensaciones que más odiaba."
n "Tan solo escuchaba los murmullos de la gente, pero no sabía qué decían. Sentí que explotaría en cualquier momento."
n "Estaba a punto de ponerme de pie cuando el comandante Erwin entró al comedor."
hide Eren normal s
stop music
show Errwin normal cba
with dissolve
r "¡Buenos días, soldados!"
r "El entrenamiento está por comenzar."
r "¡Diríjanse todos al campo para comenzar con las agrupaciones!"
show Erwin normal c
with dissolve
n "Así, todos empezaron a ponerse de pie y a salir del comedor para iniciar el entrenamiento."
n "Agradecí internamente al comandante Erwin por entrar, me había salvado de una situación realmente vergonzosa."
hide Erwin normal c
hide Errwin normal cba
with dissolve
play music "miss the way u played.mp3"
n "No pude ponerme de pie."
n "Aún me sentía avergonzada y no me había dado cuenta de que la mayoría de los cadetes ya habían salido."
n "Me levanté lentamente y comencé a caminar a paso lento para salir de ese lugar."
n "Aún no creía la situación por la que acababa de pasar."
n "Pero algo me sacó de mis pensamientos. Sentí la mano de alguien reposar suavemente sobre mi hombro izquierdo."
n "Volteé para ver de quién se trataba y bajé la mirada al descubrirlo."
$contador = 0
python:
    ArminAmizade2 += 50
call chamarBarraMais2(ArminAmizade2)
with dissolve
a "Mikasa..."
with fade
show Armin disgustado sce
with dissolve
a "¿Estás bien?"
m "Estoy bien, Armin, no te preocupes."
n "Esbocé una pequeña sonrisa forzada para hacerle sentir mejor."
show Armin enojado s
with dissolve
a "¡No me mientas, Mikasa!"
show Armin enojado sce
with dissolve
n "Tenía razón, le había mentido."
n "No pude pronunciar ni una palabra."
n "Armin es muy listo, es un gran amigo para mí y realmente me conoce a la perfección."
n "Realmente conocer a Armin cambió mi vida."
n "Él era la única persona a la que podía acudir cuando todo me salía mal."
n "Aunque muchas veces era él quien intuía las cosas y hablaba conmigo."
n "Esta vez no era la excepción, volteé a verlo y él me miraba con esos azulados ojos fijamente esperando una respuesta."
n "Normalmente con cualquier persona hubiese pasado de largo y me hubiera alejado, pero con Armin era diferente."
n "Tenía que darle una respuesta."
a "¡Te conozco y sé que las palabras de Eren te afectaron!"

show Armin enojado s
with dissolve

menu:
    "¿Qué debía responder?"

    "Sí...":
        show Armin disgustado sce
        with dissolve
        show text "{size=+20}{color=#EFC12D}¡Has obtenido +10 puntos!{/size}{/color}" at truecenter:
            xpos 402 ypos 60
        python:
            ArminAmizade2 += 10
        call chamarBarraMais2(ArminAmizade2)
        with dissolve
        hide text
        with dissolve
        n "Por fin pude decirlo después de dar un largo suspiro."
        jump buena

    "Te equivocas.":
        show Armin enojado sce
        with dissolve
        show text "{size=+20}{color=#EFC12D}¡Has perdido -10 puntos!{/size}{/color}" at truecenter:
            xpos 402 ypos 60
        python:
            ArminAmizade2 -= 10
        call chamarBarraMenos2(ArminAmizade2)
        with dissolve
        hide text
        with dissolve
        show Armin disgustado sce
        with dissolve
        a "¿Eh?"
        m "Con tal de proteger a Eren estoy dispuesta a soportar sus actitudes."
        n "¿De verdad estaba dispuesta?"
        show Armin enojado s
        with dissolve
        a "Eso no está bien, Mikasa... Estás dando todo de ti para protegerlo y él no lo reconoce ni te lo agradece..."
        show Armin disgustado sce
        with dissolve
        a "Al contrario: te lo paga insultándote y menospreciándote frente a los demás..."
        n "Nuevamente tenía razón."
        hide screen barraAmizade2
        with dissolve
        jump media

label buena:
m "Pero no me queda de otra que tragarme sus palabras, Armin."
hide screen barraAmizade2
with dissolve
show Armin enojado s
with dissolve
a "¡Eso no está bien, Mikasa!"
a "¡No tienes que estar aguantando las malas actitudes de Eren, no es la primera vez que te lo hace!"
show Armin enojado sce
with dissolve
n "Armin tenía razón otra vez."
n "Pero no importaba qué me dijera, yo seguiría con mi propósito de proteger a Eren."
show Armin disgustado s
with dissolve
a "Él no te merece..."
show Armin disgustado sce
with dissolve
n "Terminó con un tono leve y triste."
n "Se veía en su mirada y en sus palabras que hablaba en serio."
n "Quizás tenía razón... Armin jamás se equivocaba en lo que decía."
n "Él siempre es honesto y dice las cosas directas aunque lastimen a las personas, tal y como lo hacía conmigo ahora."

label media:
    n "Armin, más que nadie, sabía que mi relación con Eren había cambiado mucho y era el único que se percataba de todo lo que sucedía entre nosotros."
    n "Por ello, sus palabras me hacían reflexionar."
    n "Ciertamente, desde hace tiempo, Christa, Jean, Connie e incluso Sasha me habían dicho que mi relación con Eren no era buena y debía parar."
    n "Dijeron que debía dejar de ser tan cercana y de estar siempre pendiente de él, que debía darle su espacio y comprenderlo mejor."
    n "Yo creía que lo estaba haciendo bien garantizando su seguridad, pero, con tan solo acercarme a él, recibía malas caras, gestos y acciones de su parte."
    n "Pero él era mi única familia y eso me impedía alejarme y dejar de preocuparme por él."
    m "No te preocupes, Armin, no volverá a pasar lo de hoy..."
    m "Es mejor que vayamos al campo o nos pondrán un castigo."
    play sound "puerta.mp3"
    n "Tiré de su brazo para encaminarnos hacia el campo."
    hide Armin disgustado sce
    with dissolve
    hide Armin disgustado sce
    with dissolve
    show lili
    with dissolve
    stop music
    n "Armin no volvió a hablar en el camino, tan solo bajó la mirada. Sabía que no estaba conforme con lo que yo le había dicho."
    n "Y por una parte yo tampoco me sentía conforme conmigo misma."
    n "Pero quería evitar tocar ese tema a toda costa, así que aceleré el paso para llegar al campo justo cuando estaban tomando lista."
    play music "medieval.mp3"
    m "Llegamos a tiempo."
    scene pasteur_day
    with dissolve
    n "Me sentí aliviada al saber que evitaría el castigo."
    k "¡Mikasa Ackerman!"
    play sound "si de mikasa.mp3"
    m "¡Sí! ¡Aquí!"
    n "Di un paso al frente haciendo el saludo militar."
    k "¡Ackerman, harás equipo con Eren Jaeger!"
    m "¿¡Qué!?"
    n "No podía creer las instrucciones que me había dado."

menu:
    k "¿Algún problema, Ackerman?"

    "Me gustaría hacer equipo con otra persona.":
        n "Me maldecía internamente mientras pronunciaba esas palabras."
        k "Bien, entonces harás equipo con Arlert."
        play sound "arleth.mp3"
        k "¡Arlert! ¡¿Estás aquí?!"
        a "... ¡Sí!"
        n "Pensaba que no sería posible hacer el cambio."
        n "Además, le prometí a Armin que no volvería a pasar."
        n "Resignada, me dirigí hacia donde estaba Armin. En cuanto vio que me acerqué a él..."
        with fade
        show Armin disgustado c
        with dissolve
        a "Mikasa... ¿Estás bien? ¿Tienes fiebre?"
        n "Tocó mi frente preocupado."
        m "No te preocupes, estoy bien."
        a "..."
        m "Tus palabras me han hecho reflexionar."
        show Armin feliz c
        with dissolve
        a "Mikasa..."
        m "Esta vez dejaré a Eren tranquilo."
        n "Armin sonrió de oreja a oreja."
        show Armin alegre c
        with dissolve
        a "¡Bien, comencemos con el entrenamiento!"
        n "Adoptó una pose de pelea."
        hide Armin alegre c
        with dissolve
        n "En la primera ronda derroté a Armin, pero en la segunda, Armin logró derribarme."
        n "Cuando ya estábamos a punto de empezar la última..."
        n "La mayoría de nuestros compañeros ya habían terminado sus tres rondas."
        n "Así que se pusieron a observar mi entrenamiento con Armin."
        n "Armin se acercó a mí corriendo y lanzando una serie de patadas y puñetazos dirigidos a diferentes partes de mi cuerpo."
        n "Estaba a punto de esquivar y contraatacar... cuando... escuché una voz familiar."
        e "¡No tienes por qué ser tan ruda!"
        m "¡...!"
        with hpunch
        stop music
        play sound "pobre mikasa.mp3"
        with hpunch
        n "Armin logró asestarme un puñetazo en la cara."
        show Armin soprendido1 s
        with dissolve
        a "¡...!"
        hide Armin soprendido1 s
        with dissolve
        n "¿Qué acababa de escuchar?"
        n "Me hinqué en el suelo mientras me sobaba la mejilla."
        n "Estaba en shock."
        show Armin disgustado c
        with dissolve
        a "¡Mikasa!"
        show Armin disgustado cce
        with dissolve
        n "Armin me tomó de los hombros haciendo que reaccionase."
        show Armin enojado cce
        with dissolve
        a "¿Qué ha pasado?"
        show Armin enojado sc
        with dissolve
        a "¡¿Por qué no lo esquivaste?!"
        n "No le dije nada, solo miré a Eren con recelo, realmente estaba molesta."
        play music "suspenso.mp3"
        show Armin disgustado c
        with dissolve
        m "¡Eren!"
        n "Todas las miradas apuntaban a Eren."
        n "Eren apartó a Armin y se acercó."
        hide Armin disgustado c
        with dissolve
        scene img1
        show me
        m "¿Eren?"
        with fade
        e "Mikasa, te reto. Apuesto a que no me vences."
        n "Todos tenían cara de sorpresa. Sabía que Eren me estaba poniendo a prueba."
        n "Realmente debía demostrarle que, sin mí, él moriría. Adopté una posición defensiva, sabía que me atacaría."
        with dissolve
        scene pasteur_day
        show Armin enojado sc
        with dissolve
        a "¿¡Eren, que te pasa!?"
        hide Armin enojado sc
        with dissolve
        show Eren enojado2 c
        with dissolve
        e "¡No interrumpas, Armin!"
        hide Eren enojado2 c
        with dissolve
        show Armin enojado sc
        with dissolve
        a "¡Pero...!"
        show Armin disgustado cce
        with dissolve
        m "Armin..."
        a "Me quedaré a observaros."
        hide Armin disgustado cce
        with dissolve
        show Eren preocupado c
        with dissolve
        n "Eren soltó un suspiro."
        hide Eren preocupado c
        with dissolve
        with fade
        n "Cuando ya teníamos el campo abierto..."
        show Eren enojado3 c
        with dissolve
        e "No te contengas, ¿quieres?"
        hide Eren enojado3 c
        with dissolve
        jump co

    "No señor, ninguno.":
        n "Bendita mi suerte."
        k "¡Bien! ¡Entonces ve con tu compañero y comienza el entrenamiento!"
        n "Habló rudamente y se alejó para nombrar a las siguientes parejas."
        n "Solté un gran suspiro."
        n "Definitivamente ese no era mi día."
        n "¿Por qué, de entre todos los reclutas, tuvieron que ponerme como pareja a Eren?"
        n "La vida me odiaba."
        n "Resignada, me dirigí hacia donde estaba Eren."
        n "En cuanto vio que me acerqué a él..."
        show Eren preocupado c
        with dissolve
        n "Soltó un bufido molesto y volteó la cara hacia otra dirección."
        n "Su actitud realmente me molestó."
        m "Somos equipo..."
        show Eren normal c
        with dissolve
        m "Espero que cooperes."
        play music "suspenso.mp3"
        n "Hice hincapié en que no aguantaría sus modalidades."
        e "Lo haré solo porque es un entrenamiento."
        show Eren enojado3 c
        with dissolve
        e "No trates de protegerme en un entrenamiento, ¿quieres?"
        show Eren normal c
        with dissolve
        n "No le dije nada, solo lo miré con recelo, recordando lo que me había hecho en la mañana; realmente estaba molesta."
        n "El hecho de que se quejara por ser su compañera me molestaba aún más."
        show Eren serio c
        with dissolve
        n "Realmente debía demostrarle que, sin mí, él moriría. Adopté una posición defensiva sabiendo que me atacaría."
        n "Podía verlo en esos ojos azul verdosos que no me quitaban la mirada de encima."
        n "Hasta parecía que habían perdido su brillo y que se habían opacado de lo molesto que estaba."
        hide Eren serio c
        with dissolve
        jump co

label co:
n "Estaba molesto y se colocó en pose de batalla."
show pelea:
    alpha 1.0
    linear 1.0 alpha 0.0
    pause .5
    linear 1.0 alpha 1.0
    pause .5
    repeat


show screen life_player
show screen life_enemy
scene pelea
with fade

"Prepárate para pelear."
e "¿Lista?"
m "Sí."

label fight:
    scene pasteur_day
    with dissolve

    if life ==0:
        jump lose

    elif life_e ==0:
        jump win

$ enemy_atack = renpy.random.choice (["Ataca", "Defiende"])

if enemy_atack == "Ataca":
    play sound "cuerpo.mp3"
    show pelea:
        alpha 1.0
        linear 1.0 alpha 0.0
        pause .5
        linear 1.0 alpha 1.0
        pause .5
        repeat

    $life = change_stat(life, -10)
    n "¡Ja!"

elif enemy_atack == "Defiende":
    play sound "esquivar.mp3"
    show pelea:
        alpha 1.0
        linear 1.0 alpha 0.0
        pause .5
        linear 1.0 alpha 1.0
        pause .5
        repeat
    $ life_e = change_stat(life_e, +5)
    "¡Detiene el golpe!"

"Mi turno."

menu:
    "Atacar.":
        $ life_e = change_stat(life_e, -10)
        play sound "cuerpo.mp3"
        show pelea:
            alpha 1.0
            linear 1.0 alpha 0.0
            pause .5
            linear 1.0 alpha 1.0
            pause .5
            repeat
        m "¡Ja!"

    "Defenderse.":
        $ life = change_stat (life, +5)
        m "¡Vas a perder, Eren!"

jump fight

label siguiente:
scene img2
n "Sin más, Eren me atacó. Lanzó un puñetazo directo a mi cara que logré esquivar a tiempo."
n "Era más rápida que él. Esbocé una mirada triunfadora, lo cual le molestó."
play sound "cuerpo.mp3"
n "Nuevamente se acercó a mí corriendo y lanzando una serie de patadas y puñetazos dirigidos a diferentes partes de mi cuerpo."
n "Algunos los esquivé fácilmente."
n "Y otros los utilicé para contraatacar, tenía la ventaja en mis manos."
scene pasteur_day
n "Ágilmente, levanté mi cuerpo en el aire y lancé una patada directa al estómago de Eren."
n "Aquello provocó que este cayera al suelo y se quejara de dolor."
show Eren enojado2 c
with dissolve
e "¡Es solo un entrenamiento, Mikasa!"
show Eren preocupado c
with dissolve
n "Se quejó totalmente molesto mientras se sobaba su estómago."
n "Terminó de enojarme."
n "Me había estado aguantando, pero ya había rebasado mi límite."
m "¿¡Pero qué tonterías estás diciendo!?"
show Eren serio c
with dissolve
m "¿¡Dices que yo soy la ruda cuando tú empezaste a lanzar tus ataques directos a mi cara sin piedad!?"
m "Eres bueno para quejarte porque yo sí logré darte un golpe..."
m "¡Pero tú no lo lograste!"
hide screen life_enemy
with dissolve
$contador = 35
python:
    ErenAmizade -= 20
call chamarBarraMenos(ErenAmizade)
show Eren enojado c
with dissolve
n "Me miró con odio, lo sabía, le había dado justo en su orgullo."
n "Pero eso no me importaba en ese momento."
n "Odiaba que no reconociese las cosas."
hide screen barraAmizade
with dissolve
show Eren serio c
with dissolve
n "Se levantó sin dejar de mirarme, se colocó nuevamente en pose de pelea y comenzó a correr hacia mí."
m "¡Sigues insistiendo, Eren... pero no vas a lograrlo!"
n "Él se acercaba cada vez más."
m "¡Vas a perder, Eren!"
n "Grité de manera victoriosa mientras me colocaba en pose de defensa."
show Eren enojado2 c
with dissolve
e "¡La que va a perder eres tú, Mikasa!"
show Eren serio c
with dissolve
n "Gritó lleno en cólera mientras corría hacia mí."
n "Estaba lista para recibir el impacto, defenderme y contraatacar."
n "Pero, de repente, Eren paró en seco a un palmo de mí y me lanzó una mirada victoriosa."
show Eren alegre c
with dissolve
e "¿¡Quién es la que va a perder, Mikasa!?"
hide Eren alegre c
with dissolve
n "Mordió su mano y un terrible humo apareció en la zona."
play audio "punch.mp3"
with hpunch
m "¿¡Pero qué...!?"
n "No terminé de hablar ya que había salido disparada por el impacto de la transformación de Eren."
hide screen life_player
with dissolve
show lili
with fade
play sound "corazon.mp3"
n "Todo pasó muy rápido."
with pixellate
n "En cuanto recuperé el equilibrio, logré divisar la forma titán de Eren emergiendo del vapor que salía del lugar."
with dissolve
show titan
with fade
n "Comencé a ponerme de pie mientras intentaba reaccionar a lo que estaba pasando."
with pixellate
n "¿Por qué Eren se había transformado en titán?"
n "El rugido de aquel titán me sacó de mis pensamientos."
n "Tenía su mirada fija en mí."
n "Era igual que la de Eren, llena de odio."
n "Tomé mi posición de defensa."
n "Pero esta vez tenía miedo, no tenía mi equipo tridimensional conmigo."
n "Se suponía que este era un entrenamiento físico y no necesitábamos nuestros equipos."
n "El titán comenzó a correr en mi dirección."
play sound "corazon.mp3"
n "Mi corazón palpitaba rápidamente, sentí cómo mi cuerpo me pedía que me moviera."
n "Me pedía alejarme de ahí. Estaba en desventaja, pelear con un titán sin el equipo era una muerte segura."
n "Cada vez estaba más cerca, tenía que hacer algo."
m "¡Eren, basta!"
m "¡No puedes convertirte en titán solo para derrotarme!"
n "Eren ignoró mis palabras."
k "¡Ackerman! ¡Aléjese de Jaeger! ¡Ahora!"
n "Gritó con desesperación al ver que Eren no se detenía."
play sound "corriendo.mp3"
n "Comencé a correr."
n "Ágilmente logré subirme a una edificación cercana y fijé mi mirada en Eren."
with dissolve
n "Mi cuerpo comenzó a temblar, logré divisar sus ojos verdes."
m "Ha perdido la razón..."
m "Eren..."
m "¡No otra vez!"
n "Recordé el día en que Eren no pudo controlar su poder de titán y me atacó."
m "¡No puede estar pasando otra vez! ¡Eren!"
e "..."
m "¡Eren! ¡Reaccio...!"
play audio "punch.mp3"
with hpunch
a "¡Mikasa!"
with hpunch
with dissolve
n "Al escuchar el grito de Armin solo sentí que mi cuerpo volaba por los cielos."
n "Abrí los ojos aún quejándome de un dolor insoportable en todo mi cuerpo."
n "Intenté ver a mi alrededor y me di cuenta de que había salido volando tras el ataque del titán de Eren."
n "Comencé a caer en picada, sentí como mi corazón se aceleraba y mi respiración estaba inquieta."
n "Veía el suelo cada vez más cercano a mí."
n "Sería mi fin. Cerré los ojos, efecto de la caída y del dolor, y caí."
with dissolve
scene lili
a "¡Mikasa!"
n "Escuché la voz de Armin retumbar en mi cabeza."
with fade
n "Comencé a abrir lentamente mis ojos."
define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
with flashbulb
n "La luz del sol me impedía abrirlos del todo, sentía mi cuerpo completamente adormecido, pero también lo sentía apretado."
n "Soltaba quejidos por el insoportable dolor que sentía."
n "Mi respiración aún era agitada. Quise tocar mi cabeza, pero al intentar mover mis manos me di cuenta de que alguien las estaba tomando."
with fade
scene img2b
play sound "oi levi.mp3"
l "Eh, mocosa... ¿Estás bien?"
n "Conocía perfectamente esa voz."
n "Aún quejándome de dolor, comencé a abrir más los ojos."
n "Me asombré por la persona que tenía tan cerca de mí."
show img2b:
    xanchor 0 yanchor 0
    xpos 0 ypos -700
    linear 2.0 xpos -0 ypos -0
m "Capitán... ¿Levi?"
l "Parece que te encuentras bien, Mikasa."
n "¿Me llamó por mi nombre?"
l "Te llevaré con Hange para que te revise completamente."
m "¡No lo hagas!"
n "Estaba totalmente avergonzada."
m "No es necesario... Estoy bien..."
n "Me volví a quejar de dolor."
play sound "mf.mp3"
l "¡No desobedezcas, Ackerman!"
l "¡Te llevaré con Hange y punto!"
n "Frunció el ceño molesto."
show legion
with dissolve
l "Mike..."
l "Quiero que te encargues del resto."
n "Habló indiferente mientras entraba al edificio de la legión."
show Levi normal c
with dissolve
l "Espero que hayas aprendido la lección, Mikasa..."
n "Me miraba fíjamente mientras me hablaba."
n "Realmente sus ojos eran lindos."
show Levi normal2 c
with dissolve
with pixellate
n "Parecían negros a simple vista, pero viéndolos más de cerca eran de un color azulado oscuro."
n "Además, logré ver cómo suavizaban su rostro, podría decir que me miraba con cierta ternura y preocupación."
with pixellate
m "Sí, capitán..."
m "Ya tomé una decisión..."
with pixellate
n "Hablé pausadamente y segura de lo que estaría a punto de decir."
m "Ya no me preocuparé más por una persona que intentó matarme..."
n "Sentía que en cualquier momento iba a perder el conocimiento."
with pixellate
hide Levi normal2 c
with dissolve
show lili
with pixellate
l "Ya era hora de que te dieras cuenta, Ackerman..."
m "Lo siento, capitán..."
n "Instintivamente sonreí."
m "Gracias..."
with pixellate
n "Susurré mientras caía dormida."
show text "{size=+25}{color=#FFFFFF}Capítulo 1{/color}{/size}" at truecenter
with dissolve
pause 1
hide text
with dissolve
show text "{size=+25}{color=#FFFFFF}FIN{/color}{/size}" at truecenter
with dissolve
pause 0
hide text
with dissolve
$persistent.cap2 = True
return


label capitulo2:
    play music "sonido relajante.mp3"
    show text "{size=+25}{color=#FFFFFF}Capítulo 2{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}Una terrible noticia{/color}{/size}" at truecenter
    with dissolve
    pause 8
    hide text
    show screen quick_menu
    with dissolve
    show lili
    with fade
    play sound "Hange bajo.mp3"
    z "En fin... parece ser que estábamos... bajo... equivocada..."
    n "..."
    play sound "Levi lilo.mp3"
    l "Tch... ya ni siquiera... puedo..."
    n "..."
    n "Escuché dos voces lejanas, pero no entendí lo que decían."
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    with flashbulb
    n "Comencé a abrir torpemente mis ojos, la luz no me permitía abrirlos completamente."
    n "Con la poca visibilidad que tenía, analicé el lugar donde estaba."
    show iluminacion
    with fade
    scene lili
    with pixellate
    z "No presenta heridas graves, solo debe estar en observación."
    l "Bien... entonces te la encargo."
    show ilumi
    with fade
    n "Logré abrir por completo mis ojos e intenté levantarme de la cama."
    n "Pero sentí un dolor insoportable cerca de mi abdomen, lo que provocó que cayera de nuevo sobre la cama."
    m "¡Ay!"
    n "Coloqué mis manos sobre la zona que me causaba dolor."
    play sound "puerta.mp3"
    n "De repente escuché un crujido, levanté la mirada hacia de donde el ruido y vi cómo se abría la puerta, dejando ver quién entraba a la habitación."
    with fade
    show Hange sorprendida1 s
    with dissolve
    z "¡Ah, Mikasa!"
    $contador = 0
    python:
        HanjiAmizade3 += 60
    call chamarBarraMais3(HanjiAmizade3)
    with dissolve
    z "¡Estás herida, no intentes levantarte!"
    show Hange preocupada s
    with dissolve
    n "Pasó sus manos suavemente sobre mis hombros y se recostó sobre la cama."
    n "Me quejé del dolor y me acomodé para no lastimarme más, después volteé a verla."
    m "¿Qué fue lo que sucedió Hange?"
    z "¿No lo recuerdas, Mikasa?"
    m "Sí..."
    m "¿Cuánto tiempo llevo dormida?"
    show Hange insegura s
    with dissolve
    z "Unas dos horas, pero no importa."
    show Hange hablando s
    with dissolve
    z "¡Tus heridas no son graves, solo necesitas reposar un día más!"
    n "Se sentó en la silla con una expresión alegre."
    show Hange alegre s
    with dissolve
    z "Vaya, Mikasa... ¡Qué susto nos diste!"
    show Hange feliz s
    with dissolve
    n "Tan solo la miré extrañada. No entendía por qué se reía o a qué se refería con que solo fue un susto."
    n "Bajé la mirada hacia mi abdomen, el cual estaba envuelto en vendas y me dolía si lo apretaba."

    menu:
        n "Regresé mi mirada a Hange, tenía muchas cosas que preguntarle."

        "No entiendo a qué te refieres":
            show text "{size=+10}{color=#010104}¡Has obtenido +10 puntos!{/size}{/color}" at truecenter:
                xpos 440 ypos 190
            python:
                HanjiAmizade3 += 10
            call chamarBarraMais3(HanjiAmizade3)
            show Hange normal s
            with dissolve
            hide text
            with dissolve
            z "Me refiero a que no te pasó nada grave."
            z "El hecho de que Eren, transformado en titán, te atacase sin tu equipo y salieses viva es algo digno de admirar."
            hide screen barraAmizade3
            with dissolve
            n "Me miraba sintiéndose orgullosa."
            show Hange alegre s
            with dissolve
            z "Además, Levi llegó a tiempo para evitar que cayeras."
            n "Me sonrió y yo agaché la cabeza."
            show Hange normal s
            with dissolve
            n "Aquello último provocó que me avergonzara. Gracias a él no caí al suelo y seguía viva."
            n "Pero me avergonzaba que un hombre me hubiese cargado."
            n "Realmente era fuerte, no le oí quejarse de cargarme a pesar de su baja estatura..."
            n "Recordé sus ojos, aquellos ojos de un tono azul oscuro mirándome fijamente. Y su rostro..."
            n "Uno que mostraba en cierta forma preocupación y alivio."
            n "Jamás había visto al capitán mostrar ese tipo de expresiones antes."
            n "¿O es que era la primera vez que las hacía? No lo creo."
            n "Ciertamente lo odiaba."
            n "¿La razón? Por cómo golpeó a Eren durante el juicio."
            n "Jamás se me borrarían esas ganas de regresarle cada uno de esos golpes que le dio a Eren."
            n "¿En serio? ¿Jamás lo perdonaría?"
            show Hange hablando s
            with dissolve
            z "¡Mikasa!"
            show Hange seria s
            with dissolve
            with hpunch
            m "¿Eh?"
            n "Levanté la mirada al escuchar a Hange gritar mi nombre."
            m "¿Qué... qué sucede?"
            show Hange insegura s
            with dissolve
            z "¡Te pregunté que si ya te sentías mejor!"
            m "Ah, sí... No te preocupes, estoy bien."
            jump kike

        "¿Cómo que solo fue un susto?":
            show text "{size=+10}{color=#010104}¡Has perdido -5 puntos!{/size}{/color}" at truecenter:
                xpos 440 ypos 190
            python:
                HanjiAmizade3 -= 5
            call chamarBarraMenos3(HanjiAmizade3)
            show Hange alegre s
            with dissolve
            z "Jajajajaja."
            n "Fruncí el ceño."
            show Hange normal s
            with dissolve
            z "Me refiero a que no te pasó nada grave."
            hide screen barraAmizade3
            with dissolve
            hide text
            with dissolve
            z "El hecho de que Eren, transformado en titán, te atacase sin tu equipo y salieses viva es algo digno de admirar."
            n "Me miraba sintiéndose orgullosa."
            jump kike

label kike:
    play music "musica sadhappy.mp3"
    play sound "toc toc.mp3"
    show Hange normal s
    with dissolve
    n "De repente oímos cómo alguien llamaba a la puerta."
    n "Hange se levantó y se dirigió a la puerta para abrirla."
    hide Hange normal s
    play sound "puerta.mp3"
    show Hange alegre s
    with dissolve
    z "Ya era hora de que llegaras... Erwin."
    hide Hange alegre s
    with dissolve
    show Erwin incomodo1 s
    with dissolve
    r "Lo siento."
    n "Erwin se rascó la nuca nervioso."
    r "¿Está todo bien?"
    hide Erwin incomodo1 s
    with dissolve
    show Hange normal s
    with dissolve
    n "Hange asintió con la cabeza."
    n "Ambos voltearon a verme. Erwin se sentó en la silla mientras que Hange se quedó de pie a su lado."
    hide Hange normal s
    with dissolve
    m "Comandante..."
    show Erwim feliz s
    with dissolve
    r "Ackerman, había venido a ver cómo estabas... Pero veo que estás bien."
    n "El comandante me sonrió."
    m "Sí, estoy bien, comandante... Gracias."
    n "Bajé la mirada y comencé a jugar con mis dedos."
    show Erwin incomodo1 s
    with dissolve
    r "Ackerman..."
    show Erwin incomodo2 s
    with dissolve
    n "Volteé a verlo."
    r "Hay algo importante que debo decirle..."
    n "Su mirada se tornó seria."
    r "Eren Jaeger se encuentra en vigilancia y podría ser juzgado nuevamente por convertirse en titán y atacar a un compañero."
    n "Estaba sorprendida."
    r "Si eso ocurre, el juzgado pedirá que declares lo sucedido..."
    n "Dio un largo suspiro y continuó."
    r "Si lo encuentran culpable..."
    show Erwin incomodo1 s
    with dissolve
    r "¡Lo matarán!"
    show Erwin incomodo2 s
    with dissolve
    n "No supe qué decir, tan solo bajé la mirada sin poder creer lo que había escuchado."
    n "Las palabras del comandante retumbaban en mi cabeza."
    n "Recordé el pasado."
    n "Eren iba a ser asesinado por la policía militar cuando se enteraron de que era un titán."
    n "Se le permitió vivir gracias a la intervención de la Legión de Reconocimiento..."
    n "Selló la puerta en el muro de Trost..."
    n "Aunque esto no definía si él seguiría vivo o no."
    n "Dependía del simple hecho de que no se trasformase en titán a menos que fuera necesario."
    n "Y que no perdiera el control y no atacará a sus subordinados."
    n "Lo cual, esta vez, Eren no cumplió."
    n "Tenía la mirada perdida, no podía creer que Eren podría ser asesinado por mi culpa."
    n "Se suponía que yo debía protegerlo y cuidarlo, pero era yo quien lo estaba llevando a su muerte."
    r "Ackerman, esto no es su culpa."
    n "Interrumpió mis pensamietos al ver que no respondía."
    r "Jaeger actuó por impulso y no pudo controlar su poder."
    show Erwin incomodo1 s
    with dissolve
    r "Su transformación llamó la atención de la policía militar y se dieron cuenta de lo sucedido..."
    r "No había forma de poder ocultarlo."
    show Erwin incomodo2 s
    with dissolve
    n "Bajó la mirada en señal de culpa."
    r "No nos queda de otra que aceptar el juicio, tener la posibilidad de perder la custodia de Jaeger, y que sea asesinado."
    n "Terminó de hablar mirándome fijamente."
    hide Erwin incomodo2 s
    hide Erwim feliz s
    with dissolve
    m "Todo es mi culpa... Eren se transformó por mi culpa..."
    m "¡Matarán a Eren por mi culpa!"
    n "Grité desesperada soltando algunas lágrimas."
    m "¡Si yo no lo hubiera provocado, esto no estaría pasando!"
    play sound "llorando mikasa 1.mp3"
    n "Apreté mis puños con fuerza."
    show Hange insegura s
    with dissolve
    z "Mikasa... esto no es tu culpa... Eren decidió transformarse en titán sin saber si perdería el control de nuevo o no."
    show Hange preocupada s
    with dissolve
    n "Hange colocó su mano sobre mi hombro izquierdo."
    play sound "llorando mikasa 2.mp3"
    show Hange insegura s
    with dissolve
    z "Debes tranquilizarte o te pondrás mal... Por favor..."
    play sound "puerta.mp3"
    n "De repente se escuchó un crujido, alguien había abierto la puerta de la habitación nuevamente."
    hide Hange insegura s
    with dissolve
    show Levi normal s
    with dissolve
    l "Erwin, el comandante Pixis te espera en su oficina."
    hide Levi normal s
    with dissolve
    show Erwin incomodo1 s
    with dissolve
    r "¿Tan pronto...?"
    n "Dio un suspiro y se puso de pie."
    show Errwin normal sba
    with dissolve
    r "Hange, necesito que te encargues del papeleo de mi oficina."
    hide Errwin normal sba
    hide Erwin incomodo1 s
    with dissolve
    show Hange sorprendida1 s
    with dissolve
    z "¿¡Qué!? ¡No es justo, Erwin!"
    show Hange preocupada s
    with dissolve
    z "¿Y quién cuidará de Mikasa?"
    hide Hange preocupada s
    with dissolve
    show Erwim feliz s
    with dissolve
    r "¡Levi lo hará!"
    n "Me sorprendí por sus palabras y alcé la vista al comandante."
    r "No hay problema... ¿Cierto, Ackerman?"
    m "N-no..."
    n "Tartamudeé intentando esconder mi rostro bajando la mirada."
    hide Erwim feliz s
    with dissolve
    show Levi enojado sbe
    with dissolve
    l "Erwin, yo no estoy para cuidar mocosas... Yo sol..."
    hide Levi enojado sbe
    with dissolve
    show Erwim feliz s
    with dissolve
    r "¡Si no hay problema, entonces nos vamos!"
    n "Interrumpió a Levi con un tono muy alegre."
    hide Erwim feliz s
    with dissolve
    show Hange gi1 s
    with dissolve
    z "Te la encargo, Levi."
    show Hange gi2 s
    with dissolve
    n "Hange guiñó el ojo a Levi y salió de la habitación junto a Erwin."
    hide Hange gi2 s
    with dissolve
    show Levi enojado sbe
    with dissolve
    l "Maldita seas, cuatro ojos..."
    hide Levi enojado sbe
    with dissolve
    show Erwim feliz s
    with dissolve
    play sound "puerta.mp3"
    hide Erwim feliz s
    with dissolve
    show Levi enojado s
    with dissolve
    l "Ya me las pagarás, Erwin..."
    n "Murmuraba molesto por lo que le habían encargado."
    hide Levi enojado s
    with dissolve
    with fade
    show Levi tranquilo s
    with dissolve
    play music "WYS - Snowman.mp3"
    n "El ambiente se puso tenso, por un momento olvidé la noticia."
    n "Era realmente incómodo: jamás me había sentido en un ambiente así, me sentía avergonzada."
    n "No quería levantar la mirada, no entendía qué era lo que me pasaba."
    n "Mi corazón comenzó a acelerarse, sentí mi cara caliente y mis manos estaban temblando."
    n "No podía decir nada, tampoco podía levantar la vista."
    show Levi hablando s
    with dissolve
    play sound "oi mocosa.mp3"
    l "Eh, mocosa..."
    hide Levi hablando s
    with fade
    scene img3
    show tempe
    n "Levi tocó mi frente."
    l "¿Estás bien? Estás caliente..."
    m "Estoy bien."
    m "No es nada..."
    n "Intenté calmarme."
    l "¿Estás segura? Si te pasa algo, Hange va a molestarme y no toleraré eso..."
    n "Se quejó dando un suspiro."
    m "Estoy bien..."
    n "Respiré hondo intentando tranquilizarme."
    l "Si tú lo dices..."
    show ilumi
    with fade
    show Levi normal s
    with dissolve
    n "Se sentó en la silla cruzado de brazos."
    n "Comencé a tranquilizarme. El color rojo de mi cara ya había desaparecido y mis manos ya habían dejado de temblar."
    n "Respiré profundo dando largos suspiros."
    show Levi tranquilo s
    with dissolve
    n "Me acomodé nuevamente en la cama, colocando mi espalda en el respaldo, y volteé a verlo."
    n "Estaba sentado en aquella silla de brazos cruzados y con la cabeza hacia atrás, daba largos suspiros y tenía cerrados los ojos."
    n "Miré su rostro con detenimiento. Se veía relajado, pero serio, como siempre solía estar."
    n "Con su típica cara amargada, me preguntaba si no tenía otra expresión que mostrar aparte de esa."
    n "Su piel era clara y suave, se notaba que era un tipo loco de la limpieza que hasta su cuerpo lo representaba."
    n "No estaba mal del todo, sonreí inconscientemente."
    play sound "gracias de mikasa con levi.mp3"
    m "Gracias..."
    n "No dejaba de mirarlo."
    l "¿Por qué?"
    m "Por..."
    show Levi normal s
    with dissolve
    n "Fruncí el ceño, odiaba agradecer a la gente y que no mostraran interés alguno."
    m "salvarme..."
    n "Solté un suspiro. Me dije que sería la última vez que le agradecería algo a alguien."
    show Levi feliz s
    with dissolve
    l "No tienes que perder tu orgullo por agradecerme."
    n "Enderezó su cabeza y me miró fijamente con una sonrisa burlona."
    n "Me sobresaltó su comentario y lo miré enojada. Realmente lo odiaba, me había hecho enojar con su comentario."
    n "Si no hubiera sido por mi herida, ya me habría levantado y le habría dado un buen golpe por burlarse de mí de esa manera."
    n "Opté por fijar mi mirada en otro punto cruzándome de brazos."
    n "Se suponía que debía estar enojada, pero aquella sonrisa me había provocado otra cosa, me había hecho sonrojar."
    m "Idiota..."
    show Levi hablando s
    with dissolve
    l "¿Yo soy idiota?"
    show Levi normal s
    with dissolve
    n "Su tono era sarcástico."
    show Levi tranquilo s
    with dissolve
    n "Volví a sobresaltarme."
    n "Volteé a verlo nuevamente y seguía con la misma posición de antes."
    m "¿Tienes algún problema conmigo?"
    m "Tan solo te agradecí por salvarme..."
    show Levi suave2 s
    with dissolve
    l "Yo solo te dije que no te avergonzaras tú sola."
    l "Eres tú la que actúa raro."
    show Levi hablando s
    with dissolve
    l "Además, no iba a dejar que ningún cadete fuera lastimado por ese mocoso de Jaeger..."
    show Levi tranquilo s
    with dissolve
    l "Así que no tienes nada que agradecer, Ackerman..."
    show Levi normal s
    with dissolve
    n "Esbocé una sonrisa."
    m "Pero yo no soy un cadete..."
    show Levi sorpendido s
    with dissolve
    n "Levantó la mirada sorprendido."
    m "Yo soy alguien de la élite."
    m "Valgo por cien soldados."
    n "Lo miré sonriendo con orgullo."
    show Levi feliz s
    with dissolve
    l "Si tú lo dices, Ackerman..."
    n "Dibujó en su rostro una sonrisa de medio lado."
    $contador = 0
    python:
        LeviAmizade4 += 50
    call chamarBarraMais4(LeviAmizade4)
    with dissolve
    n "Aquella sonrisa me causó placer."
    n "Él conocía cuál era mi potencial y no dudaba de mis palabras."
    n "Me alegraba saber que alguien reconocía lo que valía, cuál era mi poder y qué era capaz de hacer."
    n "Inconscientemente sonreí."
    n "Él era igual a mí, tenía su orgullo. Se quejaba de todo aquello que le molestaba mostrando una actitud indiferente."
    n "Odiaba estar rodeado de gente y prefería estar solo, igual que yo."
    n "Tenía grandes habilidades y era realmente fuerte y ágil, no por nada era llamado «el hombre más fuerte de la humanidad»."
    show Levi normal s
    with dissolve
    l "Eh, Ackerman..."
    n "Llamó mi atención sacándome de mis pensamientos."
    show Levi hablando s
    with dissolve
    n "Me estaba mirando fijamente."
    show Levi normal s
    with dissolve

    menu:
        l "¿Qué piensas hacer con lo de Jaeger?"

        "No lo sé...":
            show text "{size=+10}{color=#010104}¡Has obtenido +5 puntos!{/size}{/color}" at truecenter:
                xpos 440 ypos 190
            python:
                LeviAmizade4 += 5
            call chamarBarraMais4(LeviAmizade4)
            with dissolve
            hide text
            with dissolve
            n "Instintivamente tomé la bufanda de mi cuello y oculté parte de mi rostro en ella, podía percibir el olor de Eren en ella."
            n "Mis mejillas se sonrojaron y lágrimas comenzaron a resbalar por mi rostro."
            show Levi normal s
            with dissolve
            l "Ya veo."
            n "Él solo volteó la mirada a otra dirección."
            m "Capitán Levi... necesito su ayuda."
            n "Lo miré con preocupación."
            show Levi sorpendido s
            with dissolve
            l "¿Eh?"
            n "Esta vez me miraba extrañado."
            l "¿Por qué tendría yo que ayudarte?"
            m "Me obligarán a decir la verdad en el juicio..."
            n "Limpié mis lágrimas."
            show Levi tranquilo s
            with dissolve
            m "Pero si usted interrumpe, ¡podría salvarlo! Tal y como lo hizo aquella vez."
            show Levi sorpendido s
            with dissolve
            m "Se lo suplico..."
            m "Será lo único que le pediré en mi vida."
            n "Me miró sorprendido y bajó la mirada."
            show Levi suave2 s
            with dissolve
            n "Ambos alzamos los ojos al mismo tiempo, centrándonos en la mirada del otro."
            n "Sus oscuros ojos azules me miraban atentamente."
            n "Sus ojos decían más que mil palabras."
            n "Con su mirada podía entender cómo era él, cómo era el capitán Levi."
            n "Todos esos sentimientos escondidos bajo aquella aburrida y continua mirada seria y actitud amargada..."
            show Levi normal s
            with dissolve
            l "De acuerdo."
            l "Pero no quiero que te retractes de la decisión que ya tomaste."
            m "Lo prometo, capitán."
            show Levi sonrojado s
            with dissolve
            n "Di un suspiro de alivio y solté una pequeña sonrisa."
            n "Él solo volteó la mirada a otra dirección."
            n "¿Estaba avergonzado? Estaba igual que yo cuando entró a la habitación."
            n "No entendía qué era lo que me provocaba cuando lo veía."
            n "Sentía mis manos temblar y me daba vergüenza mirarle a los ojos."
            n "Aunque... mirarle a los ojos me provocaba seguridad, pero también querer conocerlo más..."
            n "Conocer su pasado..."
            n "Conocer por qué siempre actuaba así, por qué era indiferente a las cosas."
            n "Cómo es que se había vuelto tan fuerte y cómo podía demostrar tener un corazón inquebrantable."
            n "Daría lo que fuera por conocerlo más, pero debe poner de su parte también para que pueda hacerlo."
            show Levi normal s
            with dissolve
            l "Ya es tarde..."
            n "Se levantó de la silla y se dirigió a la puerta."
            l "Será mejor que descanses... Mañana podría ser el juicio..."
            l "Espero que estés lista..."
            play sound "puerta.mp3"
            show Levi feliz s
            with dissolve
            l "Descansa, Ackerman..."
            n "Me dio una pequeña sonrisa para finalmente salir de la habitación."
            hide Levi feliz s
            with dissolve
            m "Hasta mañana..."
            n "Me acomodé en la cama."
            m "Levi..."
            n "Susurré su nombre con mis mejillas ruborizadas."
            show lili
            with pixellate
            show text "{size=+25}{color=#FFFFFF}Capítulo 2{/color}{/size}" at truecenter
            with dissolve
            pause 1
            hide text
            with dissolve
            show text "{size=+25}{color=#FFFFFF}FIN{/color}{/size}" at truecenter
            with dissolve
            pause 0
            hide text
            with dissolve
            $persistent.cap3 = True
            return

        "No quiero que lo maten...":
            show text "{size=+10}{color=#010104}¡Has obtenido +10 puntos!{/size}{/color}" at truecenter:
                xpos 440 ypos 190
            python:
                LeviAmizade4 += 10
            call chamarBarraMais4(LeviAmizade4)
            with dissolve
            hide text
            with dissolve
            n "Agaché mi cabeza."
            play sound "mi unica familia.mp3"
            m "Es mi única familia."
            m "Gracias a él volví a vivir en este mundo cruel..."
            n "Mi voz se quebró."
            n "Ciertamente Eren había cambiado su forma de ser conmigo."
            n "Al punto de incluso poder matarme en forma de titán, pero, tal y como se lo había dicho a Armin..."
            n "Eren era mi única familia y siempre le estaría agradecida por haberme salvado de aquellos secuestradores y darme una segunda oportunidad de vivir."
            n "Instintivamente tomé la bufanda de mi cuello y oculté parte de mi rostro en ella, podía percibir el olor de Eren en ella."
            play sound "llorando mikasa 1.mp3"
            n "Mis mejillas se sonrojaron y lágrimas comenzaron a resbalar por mi rostro."
            show Levi normal2 s
            with dissolve
            l "Es estúpido que llores por ese mocoso."
            play sound "llorando mikasa 2.mp3"
            n "Parecía no interesarle lo que decía."
            show Levi suave2 s
            with dissolve
            l "Él no te merece, Ackerman... Además... tomaste una decisión."
            n "Frunció el ceño dirigiendo su mirada a otro lado."
            n "¿Acaso le molestaba eso? ¿Por qué se comportaba de esa manera?"
            show Levi normal2 s
            with dissolve
            m "Lo sé."
            n "Limpié mis lágrimas."
            m "Pero prometí que lo protegería incluso con mi vida..."
            n "Paré un momento para recordar por qué decía eso y proseguí."
            m "Se lo prometí a Carla..."
            l "¿Carla?"
            m "Ese era el nombre de la madre de Eren, la mujer que me adoptó después de perder a mis padres..."
            n "Sentí que la nostalgia llegaba a mis ojos haciéndome llorar."
            m "Me hizo prometerle que siempre cuidaría de Eren..."
            show Levi tranquilo s
            with dissolve
            l "Ya veo..."
            show Levi normal2 s
            with dissolve
            m "Capitán Levi... necesito su ayuda."
            n "Lo miré con preocupación."
            show Levi sorpendido s
            with dissolve
            l "¿Eh?"
            n "Esta vez me miró extrañado."
            l "¿Por qué tendría yo que ayudarte?"
            m "Me obligarán a decir la verdad en el juicio..."
            show Levi normal2 s
            with dissolve
            n "Bajé la mirada."
            hide Levi normal2 s
            with dissolve
            scene img3b
            show manon
            with fade
            m "Pero si usted interrumpe, ¡podría salvarlo! Tal y como lo hizo aquella vez."
            m "Se lo suplico..."
            n "Tomé una de sus manos."
            m "Será lo único que le pediré en mi vida."
            n "Me miró sorprendido y bajó la mirada para ver cómo una de mis manos tomaba la suya."
            n "Apretó con fuerza mi mano y volteé a verlo sorprendida."
            n "Ambos alzamos los ojos al mismo tiempo, centrándonos en la mirada del otro."
            n "Sus oscuros ojos azules me miraban atentamente."
            n "Podía verlos fijamente y con detenimiento."
            n "Estos tenían un brillo especial, un brillo único que jamás había visto en ninguna otra persona. Sus ojos decían más que mil palabras."
            n "Era como nadar en un enorme lago a la luz de la luna por la noche."
            n "Con su mirada podía entender cómo era él, cómo era el capitán Levi."
            n "Sus ojos reflejaban dolor, soledad, fortaleza."
            n "Todos esos sentimientos escondidos bajo aquella aburrida y continua mirada seria y su actitud amargada."
            l "De acuerdo."
            l "Pero no quiero que te retractes de la decisión que ya tomaste."
            n "Se soltó del agarre de nuestras manos."
            m "Lo prometo, capitán."
            with fade
            show ilumi
            show Levi sonrojado s
            with dissolve
            n "Suspiré aliviada y solté una pequeña sonrisa."
            n "Él solo volteó la mirada a otra dirección."
            n "¿Estaba avergonzado? Estaba igual que yo cuando entró a la habitación."
            n "No entendía qué era lo que me provocaba cuando lo veía."
            n "Sentía un hormigueo en mi estómago, sentía mi cara caliente y mis mejillas ruborizadas."
            n "Sentía mis manos temblar y me daba vergüenza mirarle a los ojos."
            n "Además, mirarle a los ojos me provocaba seguridad, pero también querer conocerlo más..."
            n "Conocer su pasado."
            n "Conocer por qué siempre actuaba así, por qué era indiferente a las cosas."
            n "Cómo es que se había vuelto tan fuerte y cómo podía demostrar tener un corazón inquebrantable."
            n "Daría lo que fuera por conocerlo más, pero debe poner de su parte también para que pueda hacerlo."
            show Levi normal2 s
            with dissolve
            l "Ya es tarde..."
            n "Se levantó de la silla y se dirigió a la puerta."
            l "Será mejor que descanses... Mañana podría ser el juicio..."
            l "Espero que estés lista..."
            play sound "puerta.mp3"
            n "Abrió la puerta."
            show Levi feliz s
            with dissolve
            l "Descansa, Ackerman..."
            n "Me dio una pequeña sonrisa antes de salir de la habitación."
            hide Levi feliz s
            with dissolve
            m "Hasta mañana..."
            n "Me acomodé en la cama."
            m "Levi..."
            n "Susurré su nombre con mis mejillas ruborizadas."
            show lili
            with pixellate
            show text "{size=+25}{color=#FFFFFF}Capítulo 2{/color}{/size}" at truecenter
            with dissolve
            pause 1
            hide text
            with dissolve
            show text "{size=+25}{color=#FFFFFF}FIN{/color}{/size}" at truecenter
            with dissolve
            pause 0
            hide text
            with dissolve
            $persistent.cap3 = True
            return


label capitulo3:
    play music "tranquiz.mp3"
    show text "{size=+25}{color=#FFFFFF}Capítulo 3{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}El juicio{/color}{/size}" at truecenter
    with dissolve
    pause 8
    hide text
    show screen quick_menu
    scene carruaje
    with fade
    with hpunch
    n "El día había llegado."
    n "Respiraba hondo y exhalaba con tranquilidad."
    n "Mis ojos se posaron en la ventana del carruaje en el que iba viendo el hermoso paisaje de las afueras de la cuidad."
    with hpunch
    n "Árboles frondosos con diferentes tonalidades de verde, los hacían lucir espectaculares y más cuando el viento soplaba y movían sus frondosas hojas."
    n "Dejando caer algunas hojas que eran llevadas por el viento soltando el aroma a hierba fresca."
    with hpunch
    show lili
    with fade
    n "Cerré mis ojos para respirar aquel fresco olor mientras el aire jugaba con mis cabellos."
    scene cielo
    with dissolve
    n "Abrí mis ojos para ver el cielo, un color azul realmente claro y el sol brillante que daba indicios de un caluroso día."
    n "Nos dirigíamos a la sala donde se llevaría a cabo el juicio."
    scene carruaje
    with dissolve
    n "Estarían presentes las 3 legiones y el que se haría cargo del juicio y de la decisión final, el comandante Zackley."
    n "Igual que aquella vez."
    n "Me encontraba en un carruaje de aquellos que utilizaban los altos mandos para transportarse de un lugar a otro."
    n "Cabe decir que era de aquellos grandes carruajes donde cabían 4 personas en el."
    with hpunch
    n "El comandante Erwin y el capitán Levi iban sentados en frente de mí, mientras que Hange me acompañaba sentada a mi lado."
    n "Por insistencia de Hange acepté ir a aquél lugar en el carruaje por ser una parte importante del juicio."
    n "Y aunque al principio me quejé ahora lo disfrutaba."
    n "Íbamos en un camino que jamás había visto, por lo que estaba maravillada con cada cosa nueva que veía."
    with hpunch
    n "Así como de los hermosos paisajes que se reflejaban en mis ojos."
    n "Era una de las cosas que más me fascinaba, la naturaleza en su máximo esplendor."
    show Hange sorprendida1 s
    with dissolve
    z "Erwin ¿Realmente es necesario que toda la legión de reconocimiento éste presente en el juicio?"
    show Hange seria s
    with dissolve
    n "-Escuché a Hange preguntar algo dudosa, yo no despegué mi vista de la ventana-"
    hide Hange seria s
    with dissolve
    show Erwin incomodo2 s
    with dissolve
    r "En realidad no tiene caso...pero Zackley lo ha pedido y no puedo negarme."
    with hpunch
    n "-Respondió soltando un suspiro molesto-"
    hide Erwin incomodo2 s
    with dissolve
    show Hange seria s
    with dissolve
    z "Me pregunto por qué querría a toda la legión presente."
    hide Hange seria s
    with dissolve
    show Levi normal s
    with dissolve
    l "Para saber si Mikasa dice la verdad o no."
    m "¿Acaso no basta con el hecho de que tenga que contar lo que pasó?"
    hide Levi normal s
    with dissolve
    show Erwin normal s
    with dissolve
    r "El hecho es que Zackley sabe que eres cercana a Jaeger, por ello ha decidido tomar medidas."
    with hpunch
    n "-Cuestionó el comandante tomando con sus dedos su mentón para analizar-"
    show Erwin incomodo1 s
    with dissolve
    r "Supongo que se dió cuenta de ello la vez anterior."
    show Erwin incomodo2 s
    with dissolve
    n "-Suspiré con fastidio-"
    hide Erwin incomodo2 s
    with dissolve
    n "-Volteé a ver nuevamente la ventana-"
    hide carruaje
    show cielo
    with dissolve
    n "El comandante Erwin tenía razón."
    n "La vez anterior, uno de los soldados de la policía militar mencionó que Eren y yo éramos hermanos ya que su familia me había adoptado."
    with hpunch
    n "Además del hecho del que mencionó que Eren y yo asesinamos a 3 secuestradores que intentaron venderme en el Mercado."
    n "Eren intentó hacerles ver a los demás que yo no era un monstruo solo por defenderme de esa gente, a diferencia de él, que podía transformarse en un titán."
    n "-Bajé la mirada tras recordar aquello-"
    n "La situación era totalmente lo contrario, está vez sería juzgado por intentar matar a su propia familia convertido en titán."
    n "Era absurdo y algo irónico."
    with hpunch
    n "Comenzaba a imaginarme lo que la tonta policía militar daría esta vez como argumentos."
    n "Tal vez un *se los dije* o era de esperarse de alguien que puede convertirse en titán."
    show carruaje
    with fade
    show Erwin normal s
    with dissolve
    stop music
    se"Hemos llegado comandante."
    n "El comandante sólo abrió la puerta dando un largo suspiro y comenzando a descender por las pequeñas escaleras."
    show Erwin normal1 s
    with dissolve
    n "Ayudó a Hange a bajar y posteriormente a mí tendiéndome su mano para bajar brindándome una pequeña sonrisa."
    show Erwim feliz s
    with dissolve
    n " Imité su sonrisa en forma de agradecimiento."
    hide Erwim feliz s
    with dissolve
    show pasillo real
    with fade
    n "Caminamos por largos pasillos en silencio, era la primera vez que ponía atención a la estructura de aquel edificio."
    play sound "pasos juntos.mp3"
    n "Sus paredes eran totalmente blancas y muy altas con una que otra pintura o escultura colgada sobre ella."
    n "Tenía grandes ventanas por todo el pasillo, dejando entrar la luz completamente."
    n "Admiré todo el edificio hasta que llegamos al lugar."
    with fade
    play sound "puerta grande.mp3"
    show Erwin normal s
    with dissolve
    n "El comandante Erwin abrió la puerta y caballerosamente me dejó pasar asombrándome por el hecho de que ya casi toda la sala estaba llena."
    play music "Restoring Hope.mp3"
    hide Erwin normal s
    with dissolve
    show juicio
    with dissolve
    n "Caminé al lado de Hange y nos posicionamos frente a la mesa principal, tan solo nosotros 4 estaríamos ahí."
    n "Decidí mirar a mí alrededor, el resto de las legiones ya se encontraban ahí."
    n "Posicionada a nuestro lado derecho se encontraba la legión de reconocimiento."
    show Armin feliz s
    with dissolve
    n "Fijé mi mirada en cierto rubio que al sentir mi mirada volteó a verme levantando un poco su mano a la altura de su pecho para saludarme brindándome una cálida sonrisa."
    play sound "pelea hanji y levi.mp3"
    n "Correspondí el saludo de la misma manera, me alegraba de ver a Armin, me hacía sentir más tranquila."
    n "Nos habían citado a las 9 para comenzar con el juicio media hora después."
    hide Armin feliz s
    with fade
    n "Todo parecía estar tranquilo."
    n "Hange y el capitán Levi estaban discutiendo mientras que el comandante Erwin se reía de ambos."
    n "Las otras legiones conversaban entre los miembros de dichas sedes."
    n "Yo tan solo miraba a mí alrededor algo ansiosa."
    n "Dentro de poco..."
    n "Me convertiría en el centro de atención de todos y sentiría la mirada de todos en mi persona para escuchar mi historia, era una de las cosas que más odiaba."
    n "Además, sería a través de mi historia, que se decidiría que hacer con Eren."
    n "Yo ya había tomado una decisión y no estaba dispuesta a cambiarla, pero el hecho de romper una promesa también me frustraba."
    n "Cerré mis puños intentando tranquilizarme..."
    with fade
    scene img4
    with dissolve
    show mhyt
    n "Sentí la mirada de alguien y dirigí la mía hacía esa mirada chocando con los ojos del capitán Levi que me miraban fijamente."
    n "Lo miré sorprendida, aquellos ojos siempre me atrapaban y me llevaban a otro mundo, un mundo donde era capaz de ver el interior del capitán."
    n "-Involuntariamente me sonrojé-"
    n "Entendí el porque me miraba, de una u otra forma quería tranquilizarme y decirme que todo estaría bien, podía leerlo en sus ojos, en su mirada, y lo había conseguido."
    n "Tan solo esbocé media sonrisa en señal de agradecimiento la cual no pasó desapercibida para el capitán, ya que imitó mi gesto..."
    show juicio
    with dissolve
    n "Y cambió su vista a Hange que seguía molestándolo."
    n "Lo seguí mirando un rato, haciéndome pensar cómo era que con solo mirarme me hacía sentir tranquila, que con solo vernos a los ojos podíamos decirnos mil cosas."
    n "Y como con pequeñas medias sonrisas nos agradecíamos todo."
    n "Tanto el capitán como yo, odiábamos demostrar nuestras debilidades, odiábamos mostrar muestras de afecto y odiábamos ser el centro de atención."
    n "Por ello siempre teníamos esa actitud amargada e indiferente a las cosas."
    n "Siempre nos quejábamos de todo y teníamos la costumbre de hablar seria y fríamente con los demás cuando era necesario."
    n "En pocas palabras, SOMOS IGUALES. Solté una pequeña risita al llegar a mi conclusión."
    n "No necesitaba conocer al capitán para saber que era igual que yo de cierta forma."
    n "Pero realmente quería conocerlo."
    n "Quería saber si él también tenía personas por las que verdaderamente se preocupaba, tal como yo lo hacía con Eren y Armin."
    n "Quería saber si él también había tenido un pasado tormentoso que lo perseguía todo el tiempo."
    n "Quería saber si tras de él se ocultaban miles de desveladas por aquellos recuerdos abrumadores y tormentosos."
    n "Quería saber si él también poseía un poder extraño que lo hacía más fuerte por momentos por defender o proteger algo importante."
    n "Quería saber si le gustaban las comidas dulces o saladas."
    n "Quería saber si le gustaba admirar los paisajes y admirar su belleza tal y como a mí me gustaba."
    n "Quería saber más sobre él, quería conocerlo con más profundidad."
    n "Pero, ¿Desde cuándo comencé a tomarle interés?"
    n "Mi corazón se aceleraba cada que pensaba en ello, mis mejillas se ponían calientes y un extraño hormigueo se presentaba en mi estómago."
    n "Simplemente pasaba cada vez que lo veía a los ojos, aquellos que me atrapaban y no me cansaba de verlos."
    n "Realmente eran preciosos."
    play music "Dark Tension.mp3"
    play sound "Tres enormes golpes.mp3"
    with fade
    ba"Bien...Bien...Bien..."
    n "-Dijo entrando el comandante Zackley poniendo orden en la sala-"
    ba"Comenzaremos una vez que entre el acusado."
    n "-Dijo tomando asiento en el escritorio principal debajo de los 4 escudos de las incorporaciones-"
    n "Todos los demás tomamos nuestras posiciones."
    n "Me senté en el 3 lugar, a mi derecha estaba el comandante Erwin y a mi izquierda Hange seguido del capitán Levi."
    n "El resto de las legiones solo guardaron silencio y se pusieron en posición de firmes."
    play sound "puerta grande.mp3"
    n "Se escuchó como la puerta principal se abrió, esperamos en silencio, sin movernos de nuestra posición."
    scene img4b
    with fade
    n "Hasta que vimos a Eren esposado y siendo sentado a un lado del escritorio del comandante Zackley viéndonos de frente."
    n "Trague saliva al ver que su mirada iba dirigida hacía mí."
    n "Con la misma mirada de siempre, odio y recelo."
    show juicio
    with dissolve
    play sound "Tres enormes golpes.mp3"
    n "Solté un largo suspiro para relajarme y fijé mi mirada en el comandante Zackley que daba golpes en la mesa llamando la atención de todos."
    ba"Muy buenos días, sean todos bienvenidos a este evento especial."
    n "-Dijo posando su mirada en toda la sala-"
    n "¿Evento Especial? ¿Qué tenía de Especial? Tan solo era un juicio."
    ba"Sin más preámbulos daremos inicio al juicio."
    with dissolve
    show Erwin normal s at right with ease
    with dissolve
    call screen documento
    with dissolve
    label suite:
        n "-Dijo tomando en sus manos una carta y comenzó a leer-"
        hide Erwin normal s
        with dissolve
        ba"En está ocasión se realizará un juicio en contra del joven, Eren Jaeger."
        ba"Acusado de atacar a la soldado Mikasa Ackerman durante un entrenamiento dentro de la legión de reconocimiento convertido en su forma titán."
        n "Finalizó y dirigió su mirada hacía la mesa en la que me encontraba sentada."
        n "Los soldados de las otras legiones comenzaron a hablar en voz baja, discutían sobre lo que acaba de decir el comandante."
        n "Aunque no podía escuchar que decían, era realmente incómodo."
        ba"Mikasa Ackerman."
        n "-Mencionó mi nombre buscándome con la mirada-"
        ba"¿Podría contar su versión de lo sucedido aquel día por favor?"
        n "-Dijo mirándome fijamente poniendo su barbilla sobre sus brazos recargados en el escritorio-"
        play sound "si de mikasa.mp3"
        m "¡Sí!"

    menu:
        n "-Dije poniéndome de pie y respirando profundo-"

        "Contar lo sucedido desde lo que había ocurrido en el campo de batalla.":
            n "Comencé a contar lo sucedido."
            n "Hasta cuando caí al suelo y fuí rescatada por el capitán Levi."
            n "-Sentía mi cuerpo temblar pero no perdí mi postura al hablar-"
            n "Sin despegar mi mirada del comandante, quien tenía cerrados los ojos escuchándome atentamente."
            n "Me quedé en mi posición esperando alguna pregunta o instrucción de él, sin embargo no decía nada."
            n "Él ambiente comenzaba a ponerse tenso y comenzaba a ponerme ansiosa, realmente odiaba cuando pasaba eso y no podía salir del lugar."
            n "Sentía la mirada de todos en mi persona, incluyendo la de Eren que era de completo odio. Me mordí el labio inferior para no descontrolarme."
            n "Apreté mis puños un poco pero no cambié mi posición."
            ba"No es exactamente lo que a escrito en el reporte."
            n "-Dijo posando sus ojos sobre unos papeles que al parecer tenían mi versión escrita-"
            n "Mierda"
            n "Mis manos comenzaron a temblar a causa de la mirada terrorifica que emanaba de Eren"
            n "No me e explicado bien..."
            scene gamne oooo with fade
            pause 3
            with dissolve
            "No pude salvar a Eren"

            return

        "Contar lo sucedido desde lo que había ocurrido en el comedor":

            m "Todo empezó..."
            n "-Comencé a contar lo sucedido-"
            n "Desde lo que había ocurrido en el comedor, hasta cuando caí al suelo y fuí rescatada por el capitán Levi."
            n "Conté todo viendo al comandante a los ojos, sintiendo la mirada penetrante de Eren mientras hablaba, y la de todos los presentes en la sala."
            n "Sentía mi cuerpo temblar pero no perdí mi postura al hablar."
            m "Cuando desperté me encontraba en la habitación de la comandante Hange que se encargó de curar mis heridas."
            n "-Terminé soltando todo el aire que me había aguantado por sacar-"
            n "Sin despegar mi mirada del comandante, quien tenía cerrados los ojos escuchándome atentamente."
            n "Me mordí el labio inferior para no descontrolarme, apreté mis puños un poco pero no cambié mi posición."
            ba"Es exactamente lo mismo escrito en el reporte."
            n "-Dijo posando sus ojos sobre unos papeles que al parecer tenían mi versión escrita-"
            jump dd

label dd:
    play music "suspenso.mp3"
    ba"Cabe decir que ¿Entonces perdió el conocimiento después de que el capitán Levi la rescatará?"
    n "-Preguntó dejando a un lado los papeles y fijando su mirada en mí nuevamente-"
    play sound "si de mikasa.mp3"
    m "¡Así es!"
    m "Tan solo reconocí la cara del capitán Levi y perdí el conocimiento, cuando desperté me encontraba en la oficina de la comandante Hange."
    n "-Recalqué segura de mí misma, aunque sabía que lo que había dicho no era del todo cierto-"
    ba"Bien."
    n "-Asintió con la cabeza-"
    ba"Comandante Hange y Capitán Levi ¿Hay algo que quisieran agregar o cambiar a lo que dijo la soldado Ackerman?"
    n "-Preguntó mirando a los ya mencionados-"
    show Levi normal s
    with dissolve
    l "Solo una cosa señoría."
    n "-Pronunció Levi poniéndose de pie-"
    l "Fuí el encargado de llevar a la soldado Ackerman hasta la habitación de la comandante Hange."
    n "-Dijo seriamente, podía ver en sus ojos que odiaba hablar con tanta formalidad-"
    ba"De acuerdo."
    ba"¿Y usted comandante Hange Zoe?"
    hide Levi normal s
    with dissolve
    show Hange seria s
    with dissolve
    n "-Fijó su mirada en ella-"
    z "Tan solo decir que recibió una pequeña herida en la parte de su abdomen."
    z "Pero logré curarla sin problemas su señoría."
    n "-Pronunció formalmente-"
    ba"Si ese es el caso..."
    n "-Dijo apuntando algo en las hojas de papel-"
    ba"Ahora me gustaría dirigirme al acusado."
    hide Hange seria s
    with dissolve
    show Eren normal s
    with dissolve
    n "-Fijó su mirada en Eren-"
    ba"Eren Jaeger...podría decirme ¿Cuál fue su motivo para transformarse en titán y atacar a la soldado Ackerman?"
    show Eren incomodo s
    with dissolve
    e "Quería vencerla en el entrenamiento señor."
    show Eren preocupado s
    with dissolve
    n "-Dijo sin mentir y de manera directa, sorprendiéndome su respuesta-"
    e "Admito que fue exagerado transformarme."
    show Eren serio s
    with dissolve
    e "Pero quería enseñarle que no soy débil como ella cree."
    n "-Dijo frunciendo el ceño-"
    show Eren preocupado s
    with dissolve
    e "Aunque no medí las consecuencias y perdí el control de mí mismo."
    show Eren serio s
    with dissolve
    n "-Término por fin mirando al comandante-"
    n "El comandante solo soltó un suspiro, la sala comenzó a llenarse de nuevo de susurros de los soldados."
    n "Bajé mi mirada analizando cada una de las palabras de Eren, sentía que me herían como navajas apuñalándome la espalda."
    hide Eren serio s
    with dissolve
    show Hange feliz s
    with dissolve
    n "Sentí la mano de Hange sobre una de las mías y levanté mi vista para verla, me brindó una cálida sonrisa y me relajé un poco."
    hide Hange feliz s
    with dissolve
    show Levi suave2 s
    with dissolve
    n "Sentí de nuevo la mirada del capitán Levi, que me miraba preocupado y nuevamente logró tranquilizarme con la mirada."
    hide Levi suave2 s
    with fade
    play sound "Tres enormes golpes.mp3"
    ba "Bueno."
    n "-El comandante habló de pronto provocando el silencio en toda la sala-"
    ba"De acuerdo a lo acordado para la custodia del joven Jaeger y evitar su muerte en manos de la policía militar..."
    n "-Trague saliva-"
    ba"Se acordó que la legión de reconocimiento, bajo el mando de el comandante Erwin Smith y la supervisión del Capitán Rivaille."
    ba"Vigilarían a Eren Jaeger las 24 horas todos los días."
    ba"Para evitar su transformación de titán a menos que fuera necesaria en alguna expedición o experimento para conocer más sobre los titanes..."
    n "-Mencionó leyendo un papel-"
    ba"Y para ello tendrían que presentar informes donde se explicaría el uso del titán de Jaeger."
    n "-Término mirando nuestra mesa-"
    show Erwin normal s
    with dissolve
    ba"Comandante Smith ¿Tiene algo que decir al respecto?"
    n "-Lo miró fijamente-"
    n "-El comandante se puso de pie-"
    show Errwin normal sba
    with dissolve
    r "¡Ciertamente ese fue el acuerdo para tener la custodia de Jaeger!"
    r "Tanto mis subordinados como yo, estuvimos siempre al pendiente del soldado Jaeger para evitar que sucediera un accidente."
    show Erwin normal s
    with dissolve
    n "-Hablo con la verdad y continuó-"
    show Erwin normal1 s
    with dissolve
    r "Para ello no quise tener siempre vigilado a Jaeger."
    r "Y me conformé con el hecho de que él estaría tranquilo y controlado si estaba la joven Mikasa Ackerman a su lado..."
    show Erwin normal s
    with dissolve
    n "-Aquella declaración me sorprendió, realmente no lo sabía-"
    n "Pero tampoco quise evidenciar mi asombro así que conservé mi postura"
    play sound "esta bien de Erwin.mp3"
    r "Pero lo que he visto es prometedor..."
    hide Erwin normal s
    with fade
    scene img5b
    show scrti:
        alpha 1.0
        linear 1.0 alpha 0.0
        pause .5
        linear 1.0 alpha 1.0
        pause .5
        repeat
    r "Estuve observando la relación que tenían, sabía que era un gran método para no sobre explotar al joven Jaeger de estarlo observando."
    n "-Término mirando fijamente a Eren quien estaba sorprendido-"
    ba"Entiendo la razón de sus decisiones comandante..."
    ba"Pero si utilizó un método diferente al acordado ¿No creé que debió de haberlo escrito y mandado para que todos estuvieran enterados?"
    r "Si lo hacía público mi plan no funcionaría señor."
    n "-Respondió el comandante sin inmutarse ante la pregunta-"
    r "Tomé mis propios riesgos."
    so"¡Señoría!"
    n "-Gritó un soldado de la policía militar-"
    so"Sí me lo permite..."
    n "-Dijo pidiéndole una reverencia para poder hablar-"
    ba"Adelante."
    with fade
    scene img5
    so"El comandante de la legión de reconocimiento, Erwin Smith, suele tomar decisiones adelantadas sin pedir la aprobación de ninguna incorporación."
    so"Además, suele poner a las personas en riesgo ante sus inmutables decisiones que parece ser que solo él sabe lo que hace."
    so"Y no muestra interés ante las opiniones de los demás."
    n "-Hablaba de un modo muy golpeado-"
    so"Me parece que está vez tomó una decisión apresurada sin el consentimiento del resto de las legiones participantes en este juicio."
    n "-Finalizó creando un ambiente de susurros sobre lo anterior dicho-"
    n "Miré de reojo al comandante quien se encontraba de pie a la espera de respuestas del comandante Zackley."
    n "Sin cambiar su postura ni la facción de su rostro."
    n "Escuché como la gente hablaba mal del comandante Erwin, diciendo que lo que el jefe de policía militar había dicho era cierto."
    n "Que no servía para ser capitán, que debían de tomar la decisión de si también juzgarlo o no por sus acciones."
    n "Comencé a molestarme por sus palabras."
    n "Sabía que debía de mantener la calma y esperar pero de verdad odiaba que hablarán mal de las personas sin conocerlas."
    show juicio
    with dissolve
    show Levi hablando s
    with dissolve
    l "¡Señoría!"
    show Levi normal s
    with dissolve
    n "-Giré mi vista hacia la persona que había pedido la palabra-"
    l "¿Me permite hablar?"
    n "-Preguntó levantando la mano mientras todo el mundo volvía a guardar silencio-"
    ba"Adelante capitán."
    l "Quiero decir ante todos los aquí presentes..."
    l "Qué quién dió la idea de que la soldado Ackerman cuidará y protegiera a Jaeger... ¡Fuí yo!"
    hide Levi normal s
    with dissolve
    show scrti:
        alpha 1.0
        linear 1.0 alpha 0.0
        pause .5
        linear 1.0 alpha 1.0
        pause .5
        repeat
    show Levi suave2 s
    with dissolve
    n "-Dijo Levi mirando fijamente al comandante quien lo miró sorprendido al igual que el resto de los presentes-"
    l "La razón es simple"
    n "-Continuó después de que el ambiente se pusiera tenso-"
    l "La relación entre ambos soldados era cercana a una familiar..."
    l "Durante los entrenamientos notaba como la soldado Ackerman siempre estaba al pendiente del joven Jaeger."
    l "Al igual que en cada ocasión que le pedíamos a Jaeger transformarse para probar o experimentar algo, siendo la única en lograr controlarlo..."
    n "-Estaba asombrada ante sus palabras-"
    show Levi hablando s
    with dissolve
    l "Yo estoy consciente de que había tomado el cargo de cuidar de él."
    l "Pero creo que si alguien más cercano a él lo cuidaba sería un trabajo más fácil y menos tedioso y riesgoso."
    show Levi suave2 s
    with dissolve
    n "La sala quedó en completo silencio."
    n "Todos se quedaron analizando lo que el capitán Levi acababa de decir."
    n "Comencé a oír las voces de los demás:"
    n "Tiene razón* *Siempre están juntos* *Tiene sentido*"
    n "*De seguro por eso Mikasa siempre estaba atrás de él* *Como Eren no lo sabía de seguro por eso la atacó*."
    show juicio
    hide Levi suave2 s
    with fade
    hide scrti
    play sound "Tres enormes golpes.mp3"
    n "El comandante dió golpes en la mesa pidiendo orden en la sala."
    ba"Tienen sentido las razones que lo llevó a tomar esa decisión capitán."
    n "-Mencionó dándole el punto bueno-"
    ba"Aunque la razón por la que Jaeger se transformó y atacó a su hermana aún no me quedan claras."
    n "-Hizo hincapié en lo que más dudas causaba-"
    with fade
    n "La sala volvió a quedar en silencio."
    n "No sabía sí tenía que hablar, y si debía hacerlo ¿Qué era lo que tenía que decir?"
    n "Me encontraba confundida ante lo que el comandante Erwin como el capitán Levi habían dicho."
    n "Nada de lo que decían era cierto, y aunque lo fuera, ¿Porque no me lo había dicho?"
    show Armin enojado s
    with dissolve
    a "¡Señoría!"
    show Armin serio s
    with dissolve
    n "-Escuché una aguda voz pidiendo permiso para hablar-"
    show Armin hablando s
    with dissolve
    a "¿Me permite?"
    show Armin serio s
    with dissolve
    ba"Adelante."
    n "-Escuché decir al hombre por tercera vez-"
    show Armin hablando s
    with dissolve
    a "La razón por la que Eren Jaeger se transformó y atacó a la soldado Mikasa Ackerman..."
    a "Fue porque Eren no estaba enterado de la misión asignada a Mikasa."
    a "Ella siempre estuvo sobre él para evitar que él llegase a transformarse en titán."
    n "-Mencionó seguro de sí mismo-"
    a "Los conozco a ambos y sé que a Eren le molesta el hecho de que estén sobre él."
    a "Por ello, tomó una actitud fría hacia Mikasa para intentar alejarla y tener su espacio personal."
    a "Pero Mikasa no podía alejarse puesto que su misión era observar y proteger a Eren."
    show Armin serio s
    with dissolve
    n "-Tanto Eren como yo estábamos atónitos ante las palabras de Armin-"
    n "El comandante quedo sorprendido ante las palabras de aquel rubio de ojos azules."
    n "Sin duda Armin era muy listo y analizaba rápido las situaciones para ponerlas a nuestro favor."
    n "El resto de la sala se quedó en silencio igualmente analizando las palabras de Armin."
    n "Ahora lo entendía todo."
    n "Está era la ayuda que le había pedido al capitán Levi cuando estábamos juntos en la habitación de Hange."
    n "Este era el favor que le había pedido, y no solo eso, si no que le había dicho todo al comandante Erwin y Armin lo intuyó."
    n "Y con astucia siguió el plan."
    hide Armin serio s
    with fade
    show juicio
    with dissolve
    show Levi feliz s
    with dissolve
    n "Volteé a ver al capitán Levi quien me mostró una pequeña sonrisa dibujada en su suave rostro, había acertado."
    hide Levi feliz s
    with fade
    play music "medieval.mp3"
    ba"Si ese es el caso..."
    ba"Entonces declaró libre a Eren Jaeger, quién permanecerá en la legión de reconocimiento bajó constante vigilancia."
    ba"Se mantendrá vigente el acuerdo pasado ¡No declaró culpables!"
    n "-Dijo levantando la voz-"
    ba"Con esto doy por finalizado este juicio."
    play sound "Tres enormes golpes.mp3"
    n "-Dijo golpeando 3 veces seguidos el escritorio dando por terminado el juicio-"
    n "El comandante Zackley se dirigió a nuestra mesa para darnos un saludo rápido para después retirarse del lugar."
    n "El resto de las legiones comenzaron a abandonar el lugar."
    n "El comandante Erwin se dirigió a donde estaba Eren y lo soltó para después decirle:"
    show Erwin normal s
    with dissolve
    r "-Nos debes una-"
    hide Erwin normal s
    with dissolve
    show Eren preocupado s
    with dissolve
    n "-Dijo mirando al chico con mirada penetrante, a lo cual Eren solo dijo *Gracias* cabizbajo."
    hide Eren preocupado s
    with dissolve
    show Levi enojado sbe
    with dissolve
    l "Ya hice mi parte..."
    show Levi normal s
    with dissolve
    n "-Escuché a alguien detrás de mí mencionar con fastidio-"
    n "Sonreí ante el comentario y dándome vuelta para ver a la persona."
    m "Y yo cumpliré la mía capitán...gracias."
    show Levi feliz s
    with dissolve
    n "-Me mostró media sonrisa y se alejó del lugar-"
    play sound "puerta grande.mp3"
    show pasillo real
    with fade
    n "Estaba segura de que ya estaba harto de estar rodeado de gente."
    m "Aguantamos mucho capitán."
    n "-Reí ante mi comentario y salí detrás de él-"
    hide Levi feliz s
    with dissolve
    n "A lo lejos estaba el mismo carruaje esperándonos para llevarnos devuelta a la base de la legión."
    show carruaje
    with fade
    n "Aunque esta vez solo subimos Hange, el Capitán Levi y yo, porque el comandante Erwin se quedó viendo todo lo relacionado con Eren."
    n "Durante el camino elegí mi nuevo propósito de estar en la legión de reconocimiento."
    n "Estaría ahí por Armin, porque realmente quería proteger a mi amigo."
    n "Protegería a Eren por mi promesa con Carla, brindaría mis servicios al comandante Erwin."
    n "Y comenzaría a tratar con nuevas personas como Hange y Sasha."
    n "Además de acercarme más a la persona capaz de hundirme en sus ojos y llevarme a otro mundo."
    n "-Sonreí al tener mis nuevos propósitos-"
    show Hange normal s
    with dissolve
    z "¿Porque sonríes Mikasa?"
    m "Porque voy a iniciar de nuevo."
    n "-Respondí mirándola segura de mí misma-"
    m "Será mi última oportunidad."
    n "-Dije orgullosa de mi misma-"
    n "Aunque Hange al parecer no lo había entendido votó por solo mostrarme una sonrisa."
    hide Hange normal s
    with dissolve
    show Levi feliz s
    with dissolve
    n "En cambio, Levi sonrió de medio lado."
    n "Sabía a qué me refería y ese era mi intención."
    n "Hacerle saber que volvería a vivir porque...Aunque el mundo puede llegar a ser cruel...también puede ser muy hermoso."
    hide Levi feliz s
    with dissolve
    show lili
    show text "{size=+25}{color=#FFFFFF}Capitulo 3{/color}{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}FIN{/color}{/size}" at truecenter
    with dissolve
    pause 0
    hide text
    with dissolve
    $persistent.cap4 = True
    return

label capitulo4:
    play music "medieval.mp3"
    with dissolve
    show text "{size=+25}{color=#FFFFFF}Capítulo 4{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}La bufanda{/color}{/size}" at truecenter
    with dissolve
    pause 8
    hide text
    show screen quick_menu
    with dissolve
    show tarven
    with fade
    n "Habían pasado varios días desde el juicio."
    n "Eren había sido colocado en el escuadrón del capitán Levi."
    n "El escuadrón de operaciones especiales, personas de élite y de alto rango con un expediente sorprendente lo conformaban."
    n "Con ello sabía que ya no tendría que enfocarme en proteger a Eren porque me había hecho una promesa."
    n "Además, él se encontraba en un buen lugar y ellos podrían protegerlo."
    n "Hoy era nuestro día libre."
    n "Un día en el que podíamos descansar de toda actividad y podíamos olvidarnos de que éramos soldados."
    n "Aunque teníamos que vestir el uniforme en caso de emergencia, era el único día que podíamos disfrutar para nosotros mismos."
    show establo
    with dissolve
    n "Después del desayuno me dirigí al establo, me acerqué a mi caballo y le acaricié su hocico."
    n "Le encantaban las caricias y disfrutaba de mi presencia. Tomé una de las riendas y comencé a sacarlo tranquilamente."
    show pasteur_day
    with dissolve
    n "Al ser día libre, podía usar mi caballo libremente, salimos del establo y a lo lejos vi al escuadrón de operaciones especiales."
    au"No estoy de acuerdo en cuidar de un mocoso."
    n "-Exclamó uno de aquellos integrantes-"
    pe"No vamos a cuidar de él, Auro."
    n "-Pronunció la única mujer de ese escuadrón-"
    pe"Solo debemos vigilarlo y protegerlo cuando sea necesario, él no es un niño."
    n "-Dijo tranquilamente aquella chica de ojos miel y cabello rojizo claro-"
    au"Tú siempre tan buena persona, Petra."
    n "-Dijo aquel chico de afro café-"
    n "Mientras ellos discutían, los otros dos miembros solo se reían."
    n "Auro y Petra, nombres de dos de los miembros de ese escuadrón."
    $contador = 0
    with fade
    python:
        ErenAmizade += 25
    call chamarBarraMais(ErenAmizade)
    with dissolve
    show Eren sorprendido s
    with dissolve
    e"¿Qué haces aquí, Mikasa?"
    n "-Escuché mi nombre y volteé a ver quién era, fruncí el ceño al ver de quien se trataba-"
    show Eren normal s
    with dissolve
    e "¿Acaso vienes a espiarme?"
    n "-Dijo con el tono más golpeador y grosero del mundo-"
    m "No."
    n "-Dije secamente sin cambiar mi mirada-"
    m "Solo vine por mi caballo."
    n "-Tiré de una de las riendas de mi caballo y comencé a caminar-"
    with hpunch
    show Eren incomodo s
    with dissolve
    play music "Most Beautiful.mp3"

    menu:
        e "¿Y se puede saber a dónde vas?"

        "Eso no te importa":
            show Eren serio s
            with dissolve
            centered "{size=+25}{color=#f00}-10p{/color}{/size}"
            python:
                ErenAmizade -= 10
            call chamarBarraMenos(ErenAmizade)
            n "-Exclamé mientras seguía caminando-"
            with hpunch
            hide screen barraAmizade
            with dissolve
            n "Ya, una vez más alejada, solté un suspiro. Estaba a punto de subir a mi caballo cuando sentí un tirón."
            n "Eren me había agarrado del brazo bruscamente haciéndome mirarlo de frente."
            with hpunch
            m "¡Suéltame!"
            n "-Grité molesta viéndolo con odio-"
            m "¡Te dije que me sueltes!"
            with hpunch
            n "-Volví a decir intentando zafarme de su agarre-"
            show Eren incomodo s
            with dissolve
            e "¡Solo quiero saber a dónde vas!"
            n "-Gritó apretando mi muñeca, solté un quejido del dolor-"
            show Eren enojado3 s
            with dissolve
            play sound "se realista.mp3"
            e "¿¡Por qué te comportas así, Mikasa!?"
            e "¡Eres tan infantil!"
            with hpunch
            show Eren serio s
            with dissolve
            n "-Exclamó zarandeando con brusquedad mi cuerpo-"
            with hpunch
            m "¿Yo soy la infantil? ¿Acaso yo me convertí en titán para ganarle a mi hermano porque no aceptaba perder?"
            with hpunch
            n "-Grité enfurecida zafándome de su agarre-"
            m "¡Eso sí es ser infantil, Eren!"
            n "-Recalqué mirándolo con odio-"
            n "Se quedó callado mientras me miraba con odio y desprecio, sabía que tenía la razón y él no lo aceptaba."
            n "Lo miré de la misma manera, odiaba que me hiciera sus reproches, yo era mejor que él en todo."
            n "Yo siempre tenía la razón en las cosas, no podía ganarme."
            show Eren sc Creido
            show Eren enojado2 s
            with dissolve
            e "¿Hermana?"
            e "¿Aún te consideras mi hermana después de meterme en un juicio?"
            show Eren serio s
            with dissolve
            n "-Me quedé impactada ante lo que acababa de decir-"
            show Eren enojado3 s
            with dissolve
            e "¡Yo no necesito una hermana así!"
            show Eren enojado s
            with dissolve
            e "¡Olvídate de que somos hermanos! ¡Tú y yo no somos FAMILIA!"
            show Eren serio s
            with dissolve
            with hpunch
            n "-Gritó jalando mis brazos y tirándome al suelo-"
            n "Aunque lo que había dicho me había dolido..."
            n "Debía demostrarle que no me importaba en lo más mínimo."
            jump nor

        "¡Déjame en paz!":
            centered "{size=+25}{color=#f00}¡-5p!{/size}{/color}"
            python:
                ErenAmizade -= 5
            call chamarBarraMenos(ErenAmizade)
            show Eren enojado s
            with dissolve
            n "-Exclamé mientras seguía caminando-"
            hide screen barraAmizade
            with dissolve
            with hpunch
            show Eren incomodo s
            with dissolve
            e "¡Solo quiero saber a dónde vas!"
            show Eren enojado3 s
            with dissolve
            play sound "se realista.mp3"
            e "¿¡Por qué te comportas así, Mikasa!?"
            e "¡Eres tan infantil!"
            m "¿Yo soy la infantil? ¿Acaso yo me convertí en titán para ganarle a mi hermano porque no aceptaba perder?"
            show Eren serio s
            with dissolve
            m "¡Eso si es ser infantil, Eren!"
            n "-Recalqué mirándolo con odio-"
            n "Se quedó callado mientras me miraba con odio y desprecio, sabía que tenía la razón y él no lo aceptaba."
            n "Lo miré de la misma manera, odiaba que me hiciera sus reproches, yo era mejor que él en todo."
            n "Yo siempre tenía la razón en las cosas, no podía ganarme."
            show Eren enojado2 s
            with dissolve
            e "¿Hermana?"
            n "-Dijo por fin en tono sarcástico-"
            e "¿Aún te consideras mi hermana después de meterme en un juicio?"
            show Eren serio s
            with dissolve
            n "-Me quedé impactada ante lo que acababa de decir-"
            show Eren enojado3 s
            with dissolve
            e "¡Yo no necesito una hermana así!"
            show Eren enojado2 s
            with dissolve
            e "¡Olvídate de que somos hermanos! ¡Tú y yo no somos FAMILIA!"
            show Eren serio s
            with dissolve
            n "Aunque lo que había dicho me había dolido..."
            n "Debía demostrarle que no me importaba en lo más mínimo."
            jump nor

label nor:
        n "-Con todo el odio y asco del mundo me quité la bufanda roja que tenía en mi cuello-"
        m "¡Bien!"
        m "¡Entonces ya no necesito esta porquería!"
        hide Eren serio s
        with dissolve
        hide Eren serio s
        scene img6
        show bufanda
        with fade
        with hpunch
        n "-Grité lanzándole la bufanda-"
        n "-Él me miró sorprendido-"
        e "..."
        m "..."
        n "-Sus ojos perdieron el color al escuchar mis palabras. Sentía mi garganta seca y mi boca temblorosa-"
        m "¡No quiero nada tuyo!"
        e "..."
        m "¡Jamás!"
        with fade
        scene bosque1
        with dissolve
        n "-Grité mientras me subía a mi caballo y me dirigía al bosque más cercano-"
        play music "huyendo4.mp3"
        with hpunch
        n "El aire golpeaba mi rostro bruscamente debido a la velocidad con la que cabalgaba, estaba furiosa."
        n "Creía que después del juicio él no se tomaría la molestia de volver a dirigirme la palabra."
        n "Y cada vez que lo hacía era para reclamarme las cosas."
        n "¿Por qué?"
        n "¿Qué ganaba con eso?"
        n "Pues ganaba hacerme enojar y con ello... yo me alejaría, como si no pudiera contra él."
        n "Apreté mis dientes al darme cuenta de mis errores, aceleré el paso golpeando a mi caballo para que corriera más rápido."
        n "Necesitaba alejarme."
        n "Necesitaba un lugar tranquilo para pensar algunas cosas y olvidar otras. Necesitaba un espacio solo para mí. Necesitaba ir a mí lugar favorito."
        play music "bosque.mp3"
        n "-Una vez que divisé la entrada del bosque bajé la velocidad-"
        n "Sentía el aire fresco en mi cara, el olor a hierba y vegetación inundaba el lugar."
        n "El canto de algunos pájaros era perceptible. Una vez más cerca, me bajé de mi caballo y lo acaricié de nuevo."
        with hpunch
        play sound "sorry.mp3"
        m "Lo siento..."
        n "-Le dije mientras le acariciaba su lomo y le miraba a los ojos-"
        m "Tú no tienes la culpa..."
        n "-Él volteó a verme con aquellos profundos ojos negros mientras aceptaba mis caricias-"
        m "Vamos a un lugar más tranquilo."
        n "-Le dije mientras nos adentrábamos en el bosque-"
        scene bosque2
        with fade
        n "El lugar era realmente extenso y hermoso, árboles de diferentes tamaños y tonalidades de verde hacían este un lugar muy bello."
        n "La suave brisa que llegaba de entre los árboles era cálida y fresca."
        n "La poca luz que entraba entre las frondosas copas de los árboles hacía del lugar el paisaje perfecto para descansar."
        n "Caminaba con mí caballo al lado, estaba tan acostumbrado a mi presencia que me seguía sin la necesidad de tirar de la rienda."
        n "Ambos disfrutábamos del lugar a nuestra manera, caminando lentamente admirando el paisaje que de vez en cuando podía visitar."
        scene bosque5
        with dissolve
        n "Llegué a mi lugar favorito, un pequeño lago con aguas cristalinas y vegetación por doquier."
        n "Me senté en la orilla de este mientras admiraba su inigualable belleza."
        n "El ambiente tan tranquilo había hecho que mi furia y enojo de antes se fulminara por completo."
        n "Respiré hondo y disfruté del lugar. Era de las pocas veces que me sentía diferente, me sentía en otro mundo."
        n "Me sentía libre y sin preocupaciones, me sentía feliz y recordaba mi niñez con mis padres."
        n "Bajé la mirada para recordar aquellos momentos que compartí con mis padres en un bosque parecido a este."
        n "Solíamos jugar en el agua de un pequeño lago, mi padre me había enseñado a pescar en él."
        n "Y en el bosque me había enseñado a cazar."
        n "Aunque yo prefería la cosecha de frutas y verduras con mi madre."
        n "De vez en cuando salíamos a jugar al extenso bosque por horas y descansábamos sobre el suave césped tomados de las manos mirando al cielo."
        n "Veíamos las nubes y a veces las estrellas."
        n "Eran momentos únicos que jamás borraría de mi mente."
        play sound "relinchar.mp3"
        n "El sonido de galopes de un caballo me sacó de mis recuerdos y me hicieron mirar a mí alrededor."
        n "Divisé mi caballo tomando agua del lago y, cerca de él, otro caballo con alguien desmontándolo."
        n "Me puse de pie y me dirigí hacia allá cuando identifiqué al dueño del otro caballo."
        $contador = 0
        python:
            LeviAmizade4 += 55
        call chamarBarraMais4(LeviAmizade4)
        with dissolve
        show Levi normal s
        with dissolve
        l "Ackerman..."
        n "-Pronunció mi nombre con un tono algo sorprendido-"
        l "¿Qué haces aquí?"
        show Levi suave2 s
        with dissolve
menu:
    n "-Preguntó cambiando la expresión de su rostro en una de indiferencia-"

    "Suelo venir aquí en mis días libres, capitán":
        centered "{size=+25}{color=#f00}¡+15p!{/size}{/color}"
        python:
            LeviAmizade4 += 15
        call chamarBarraMais4(LeviAmizade4)
        show Levi normal s
        with dissolve
        n "-Dije algo avergonzada-"
        m "Este es mi lugar favorito."
        hide screen barraAmizade4
        with dissolve
        l "Oh."
        n "-Mencionó mientras se sentaba cerca del lago-"
        show Levi hablando s
        with dissolve
        l "¿Entonces no importa si le hago compañía?"
        show Levi normal s
        with dissolve
        jump mm

    "¿Y usted qué hace aquí?":
        centered "{size=+25}{color=#f00}¡-10p!{/size}{/color}"
        python:
            LeviAmizade4 -= 10
        call chamarBarraMenos4(LeviAmizade4)
        n "-Pregunté con algo de curiosidad mientras mi corazón comenzaba a acelerarse-"
        show Levi enojado s
        with dissolve
        l "Eso no es de tu incumbencia, mocosa."
        n "-Dijo secamente sin despegar la mirada del lago-"
        jump cv

    "Suelo venir aquí... porque me gusta estar tranquila.":
        centered "{size=+25}{color=#f00}¡+8p!{/size}{/color}"
        python:
            LeviAmizade4 += 8
        call chamarBarraMais4(LeviAmizade4)
        show Levi tranquilo s
        with dissolve
        l "Oh."
        n "-Mencionó mientras se sentaba cerca del lago-"
        show Levi feliz s
        with dissolve
        n "Giré mi vista al lago igual que él, esbozando una pequeña sonrisa."
        n "Aunque él no me haya contestado, sabía que estaba ahí porque le gustaba el lugar."
        n "También le gustaban los lugares tranquilos donde no había gente ni ruidos, era igual que yo."
        jump cv

label mm:
    n "-Preguntó esperando mi respuesta-"
    menu:
        "No capitán, no hay problema.":
            centered "{size=+25}{color=#f00}¡+5p!{/size}{/color}"
            python:
                LeviAmizade4 += 5
            call chamarBarraMais4(LeviAmizade4)
            n "-Le dije sentándome a su lado-"
            m "¿Y usted qué hace aquí?"
            n "-Pregunté con algo de curiosidad mientras mi corazón comenzaba a acelerarse-"
            l "Eso no es de tu incumbencia, mocosa."
            n "-Dijo secamente sin despegar la mirada del lago-"
            n "Giré mi vista al lago igual que él, esbozando una pequeña sonrisa."
            n "Aunque él no me haya contestado sabía que estaba ahí porque le gustaba el lugar."
            n "También le gustaban los lugares tranquilos donde no había gente ni ruidos, era igual que yo."
            jump cv

        "... No.":
            centered "{size=+25}{color=#f00}¡+3p!{/size}{/color}"
            python:
                LeviAmizade4 += 3
            call chamarBarraMais4(LeviAmizade4)
            jump cv


label cv:
    show Levi enojado s
    with dissolve
    hide screen barraAmizade4
    with dissolve
    l "Mi escuadrón la vió pelearse con Jaeger de nuevo."
    n "-Dijo molesto-"
    l "¿No prometió algo, Ackerman?"
    n "-Preguntó algo molesto, pero sin cambiar su semblante-"
    m "Así que nos vieron..."
    show Levi suave2 s
    with dissolve
    n "-Dije dando un suspiro fastidiada-"
    m "Yo no quería hablar con él, pero sus actitudes me hacen enojar y siempre le contesto."
    n "-Fruncí el ceño al recordar lo que había pasado-"
    hide Levi suave2 s
    with dissolve
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    scene bufanda
    with flashbulb
    scene bosque5
    with dissolve
    show Levi normal s
    with dissolve
    m "Siempre quiere hacerme ver como si yo fuera la mala, como si por mi culpa él fuera débil..."
    n "-Acerqué mis piernas a mi pecho y las abracé-"
    m "Nunca acepta las cosas, odia perder y por eso se vuelve tan egoísta y molesto."
    l "Antes no pensabas así de él, Ackerman."
    n "-Mencionó sorprendiéndome su comentario-"
    m "Tiene razón."
    n "-Contesté con sinceridad regresando a mi posición-"
    m "Estaba tan cegada con el hecho de no perderlo que no me importaban sus malas actitudes y su pésima personalidad..."
    m "Era lo último que me quedaba de familia en este mundo..."
    show Levi hablando s
    with dissolve
    l "No todo se compone de lazos familiares, hay otros que pueden ser de amistad o de trabajo."
    show Levi suave2 s
    with dissolve
    n "-Dijo con una voz más tranquila-"
    l "A veces son ese tipo de lazos lo que te impulsan a seguir peleando."
    n "-Mencionó mientras acariciaba el pasto-"
    m "¿Lazos de amistad o de trabajo?"
    n "-Pregunté asombrada-"
    show Levi normal s
    with dissolve
    l "Tú debes de tener muchos de esos lazos."
    play sound "deverdad.mp3"
    l "¿No?"
    n "-Preguntó mirándome fijamente-"
    n "Comencé a pensar en quiénes podían formar parte de esos lazos de los que hablaba el capitán."
    n "A decir verdad, creo que no tenía ninguno. Estaba todo el tiempo con Eren, que no socializaba con nadie."
    n "Y mucho menos a mis autoridades, hasta que recordé a alguien."
    m "Armin..."
    n "-Dije con una pequeña sonrisa al recordar a mi amigo rubio de ojos azules-"
    m "Es la persona más cercana que tengo ahora."
    show Levi hablando s
    with dissolve
    l "Ese lazo es más que suficiente para motivarte a seguir..."
    l "¿No quieres la felicidad y seguridad de tu amigo?"
    show Levi suave2 s
    with dissolve
    n "-Hizo hincapié en lo que yo siempre me proponía-"
    m "¡Por supuesto que sí!"
    n "-Dije volteándome a mirarlo-"
    m "Haría todo lo que estuviese en mis manos para cumplir su sueño y protegerlo de este cruel mundo."
    n "-Le dije mientras pasaba por mi mente la imagen de Armin con una enorme sonrisa-"
    m "Haría todo por él..."
    n "-Dije en voz tenue con una pequeña lágrima en mis ojos-"
    show Levi hablando s
    with dissolve
    l "Entonces no te eches para atrás, cuida de ese mocoso y valora su presencia."
    l "En este mundo nunca sabes por cuánto tiempo una persona podrá estar a tu lado..."
    play sound "levide.mp3"
    l "Al fin y al cabo, todos nos enfrentamos a la posibilidad de perder a alguien..."
    hide Levi hablando s
    with dissolve
    scene img6b
    with fade
    n "-Dijo recostándose sobre el pasto mirando al cielo con un semblante triste-"
    l "Las personas tardan en llegar pero se van muy rápido..."
    n "-Mencionó algo melancólico-"
    n "Al ver su rostro sabía que había tenido una mala experiencia."
    n "Sus ojos mirando al cielo decían muchas cosas: tristeza, arrepentimiento, culpa..."
    n "Su rostro melancólico mostraba el recuerdo de alguien que se había ido."
    n "Podía ver que aquella persona había sido muy cercana a él y que le dolía, pero no quería demostrarlo."
    n "Nuevamente, con ver su rostro, podía leer lo que pensaba sin que dijera nada, él era así."
    n "Ocultaba, tras ese semblante serio y arrogante, a una persona débil y con sentimientos."
    n "Prefería mostrar ese lado duro e indiferente ante los demás y se guardaba las cosas para sí mismo."
    n "Era igual que yo, me preguntaba cuántas veces ya lo había dicho."
    n "El hecho de que prefiriéramos un ambiente de tranquilidad y soledad al bullicio de la legión nos hacía iguales."
    n "Y ahora mismo lo estábamos compartiendo juntos."
    n "Su presencia no me molestaba, al contrario, me sentía cómoda."
    n "Pero verlo ahí, recostado con sus brazos detrás de su nuca y una pierna encima de la otra cruzada mientras miraba al cielo..."
    n "Hacía que mi corazón se acelerase, palpitarse con rapidez y mis mejillas se calentaran y tomaran ese color rojo intenso."
    n "Seguí admirando su belleza, porque debía de admitir que realmente era guapo, aquellos cabellos negros con aquel corte lo hacía lucir atractivo..."
    n "El color azul oscuro de sus ojos lo hacían tentador, la fisionomía de su cuerpo lo hacía sexy, y la suavidad de su piel y esos labios lo hacían perfecto."
    n "Comencé a sentir un revoloteo en mi estómago, el color de mis mejillas había aumentado y comenzaba a temblar."
    with hpunch
    n "(¿Qué me está pasando?)"
    n "(En qué estoy pensando?)"
    show bosque5
    with fade
    show Levi normal s
    with dissolve
    l "Ackerman... ¿Se encuentra bien?"
    n "-Preguntó mientras se colocaba encima de mí y ponía una de sus cálidas manos en mi frente-"
    m "Ah... estoy bien."
    n "-Le dije con dificultad-"
    n "-Estaba totalmente avergonzada-"
    l "Si tú lo dices..."
    n "-Dijo separándose de mí-"
    show Levi enojado sbe
    with dissolve
    l "Actúas muy raro."
    n "-Mencionó molesto-"
    show Levi normal s
    with dissolve
    play sound "disculpe.mp3"
    m "Lo siento..."
    n "-Dije mientras me tapaba el rostro con mis piernas-"
    hide Levi normal s
    show lili
    with dissolve
    play sound "noes.mp3"
    l "No es necesario que te disculpes..."
    m "Capitán..."
    m "Para usted..."
    m "¿Quiénes forman esos lazos de amistad y trabajo de los que habla?"
    l "..."
    n "Se hizo un silencio incómodo."
    n "No me atrevía a levantar la vista porque aún seguía avergonzada."
    n "Quería ver su expresión, quería ver su rostro."
    n "Pero no podía hacerlo porque cada vez que lo hacía pasaba lo mismo. Me estaba volviendo loca."
    n "No sabía qué era lo que me pasaba, y lo más seguro es que a él le molestase cada vez que me ponía así."
    l "No lo sé..."
    l "No suelo hablar con la gente, es aburrido y molesto."
    n "(Lo sabía, igual que yo)"
    m "Pero debe de haber alguien, aunque solo sea una persona."
    n "-Quería que me respondiera de una u otra manera-"
    l "¿Por qué tendría que decírtelo, mocosa?"

    menu:
        l "¡Mi vida no te importa!"

        "¡Claro que me importa! Yo...":
            scene bosque5
            with dissolve
            python:
                LeviAmizade4 += 12
            call chamarBarraMais4(LeviAmizade4)
            n "-Recalqué mirándolo fijamente-"
            show Levi sorpendido s
            with dissolve
            l "¡...!"
            m "Quiero conocerlo..."
            hide screen barraAmizade4
            with dissolve
            n "-Lo miré avergonzada y él me miraba sorprendido-"
            m "Si algún día me necesitas... habláme."
            show Levi tranquilo s
            with dissolve
            m "Yo... lo sé..."
            show Levi suave2 s
            with dissolve
            m "Es loco ver cómo la vida nos une con personas que nunca imaginábamos..."
            m "Y nos separa de personas que pensábamos que siempre iban a estar ahí."
            m "No importa todo lo que haya pasado..."
            m "Yo voy a estar."
            n "Muy tarde... Me di cuenta muy tarde de lo que había dicho."
            n "Ese era mi pensamiento. Lo dije en voz alta y él lo había escuchado."
            n "Sus ojos mostraban un brillo especial que solo alguien tan cerca de él podría verlo."
            n "Una brillo que jamás había visto."
            n "El silencio incómodo volvió a hacerse presente."
            play sound "sonidocaballo.mp3"
            n "Tan solo se oía la brisa que chocaba con las hojas de los árboles."
            n "Se oían las tranquilas aguas de aquel lago, así como el relincho de nuestros caballos."
            jump jaja


        "¡Quiero conocerlo!":
            scene bosque5
            with dissolve
            show Levi sorpendido s
            with dissolve
            python:
                LeviAmizade4 += 14
            call chamarBarraMais4(LeviAmizade4)
            n "-Solté de golpe-"
            n "Muy tarde... Me di cuenta muy tarde de lo que había dicho."
            n "Ese era mi pensamiento. Lo dije en voz alta y él lo había escuchado."
            hide screen barraAmizade4
            with dissolve
            n "-Lo miré avergonzada y él me miraba sorprendido-"
            show Levi tranquilo s
            with dissolve
            n "El silencio incómodo volvió a hacerse presente."
            play sound "sonidocaballo.mp3"
            n "Tan solo se oía la brisa que chocaba con las hojas de los árboles."
            n "Se oían tranquilas aguas de aquel lago, así como el relincho de nuestros caballos."
            jump jaja

label jaja:
    show Levi sonrojado s
    with dissolve
    n "Ese silencio incómodo... provocado por mi culpa..."
    n "Por decir mis pensamientos en voz alta, por querer mostrar mi interés hacia él."
    n "Me estaba matando lentamente."
    n "Sabía que no era buena en estas cosas; de hecho, no sabía ni qué estaba haciendo y por qué llegué a pensar eso."
    n "Pero era la verdad: quería conocerlo, quería saber sobre él, quería pasar más tiempo con él."
    n "Volteé a verlo una vez más. Sus mejillas se encontraban sonrojadas, igual que las mías."
    n "No había cambiado su semblante, pero me miraba fijamente."
    n "Su mirada entró en la mía y el revoloteo regresó a mi estómago."
    show Levi feliz s
    with dissolve
    n "Mantuvimos nuestras miradas pegadas por mucho tiempo hasta que él mostró una pequeña sonrisa."
    show Levi sonrojado s
    with dissolve
    n "No sabía el por qué... pero me gustaba ver sus sonrisas, por muy pequeñas que fueran me provocaban un sentimiento de felicidad inexplicable."
    l "Erwin quizás..."
    show Levi tranquilo s
    with dissolve
    n "-Rompió por fin el silencio, pero aún avergonzado-"
    l "La cuatro ojos también es una buena persona."
    n "-Mencionó, aunque rompiendo su orgullo-"
    play sound "si2.mp3"
    m "Y-ya veo."
    n "-Dije feliz al obtener mis respuestas-"
    m "La señorita Hange y el comandante Erwin son grandes personas, realmente los admiro."
    show Levi suave2 s
    with dissolve
    n "-Acepté para mí misma-"
    l "Han estado conmigo desde el principio."
    n "-Mencionó algo nostálgico-"
    show Levi feliz s
    with dissolve
    l "Aunque yo no soy muy abierto con nadie, con ellos he llegado a serlo."
    n "-Mencionó mostrando de nuevo aquella sonrisa-"
    show Levi normal s
    with dissolve
    m "¿Darías tu vida por ellos?"
    m "Porque estoy segura de que ellos lo harían por ti."
    show Levi tranquilo s
    with dissolve
    l "Preferiría que no lo hicieran..."
    n "-Dijo cambiando su semblante a uno triste-"
    l "Este mundo los necesita, no pueden irse por salvar a una basura como yo."
    show Levi normal s
    with dissolve
    play sound "loentiendes.mp3"
    l "¿Lo entiendes?"
    n "Me impresionó la manera en que se describía a sí mismo. Ciertamente vivir en este mundo te hacía sentir inferior ante los titanes."
    n "Pero sabía que él no se refería a eso, se refería a su pasado, igual que yo..."
    n "Algo que nos dijera que nos teníamos que ir ya, pero por más que lo intentáramos seguíamos luchando y al final seguíamos aquí."
    m "No creo que ellos piensen eso. Para ellos tú eres alguien importante, un amigo, un hermano, un compañero."
    n "-Mencioné intentando hacerlo sentir mejor-"
    m "Si tanto te preocupa, entonces sé fuerte, más fuerte que ellos; demuéstrales que no necesitas que te protejan porque tú puedes solo."
    n "-Le dije dándole una sonrisa-"
    n "Me miró sorprendido ya que le di las misma palabras que él me había dicho."
    show Levi feliz s
    with dissolve
    play sound "solke.mp3"
    l "Tienes razón."
    n "-Sonrió con orgullo pero sincero-"
    show Levi suave2 s
    with dissolve
    n "Nuestras miradas volvieron a cruzarse pero esta vez en forma de agradecimiento."
    with dissolve
    play music "Nature.mp3"
    hide Levi suave2 s
    with fade
    show lili
    n "El silencio incómodo ya no estaba. Solo estábamos él y yo solos intentando conocernos, intentando saber más del otro."
    with fade
    scene img7
    n "Mirábamos nuestras facciones todo el tiempo, sentíamos esas molestias todo el rato, pero no nos desagradaban."
    n "Estábamos cerca el uno del otro, no nos habíamos percatado del momento en que habíamos quedado así..."
    n "Pero ninguno se movió, era cómodo, tranquilo, seguro, perfecto."
    n "Podíamos sentir lejanamente la respiración del otro, el viento jugando con nuestros cabellos mientras seguíamos mirándonos a los ojos."
    n "Comencé a mirar su boca, aquella en donde estaban presentes esos suaves labios de un color rosa pálido..."
    play sound "corazon.mp3"
    n "Mi corazón comenzó a acelerarse, no podía dejar de mirarlos."
    n "Levantaba mi vista y él miraba mis ojos. Después se volteaba con la misma expresión que yo, pensaba lo mismo que yo."
    n "¿Pero quién lo haría primero?"
    n "Era vergonzoso pensar en eso, pero no parábamos de hacer ese ciclo de miradas."
    n "Comenzaba a excitarme el hecho de tocar esos labios, sentirlos, los deseaba sobre los míos, pero la vergüenza me lo impedía."
    n "Además, jamás me había pasado algo así, tampoco sabía cómo hacerlo."
    n "La cercanía con él era mínima; sentía su respiración intranquila, igual que la mía."
    n "Su aliento llegaba a mi rostro, un aroma dulce, digno de alguien loco por la limpieza, y sus ojos chocaban con los míos sin poder dejar de admirarlos."
    m "Capitán..."
    n "-Pronuncié con miedo y vergüenza-"
    m "Yo..."
    with dissolve
    scene img7b
    show beso
    with fade
    n "Pegué mis labios con los suyos de manera suave y delicada."
    n "Al momento del contacto mi cuerpo se erizó por la nueva sensación."
    n "Torpemente comenzamos con el roce de nuestros labios, eran cálidos y suaves tal y como los imaginaba."
    n "Comenzamos a profundizarlo más, cerrando nuestros ojos y pegando más nuestros cuerpos."
    n "El beso comenzó a ser más pasional cuando tomábamos la experiencia, tomamos nuestras manos mientras disfrutábamos del momento."
    show bosque5
    with fade
    show Levi feliz s
    with dissolve
    n "Por falta de aire nos separamos y nos miramos a los ojos, una pequeña sonrisa salió de nuestras bocas al mismo tiempo mientras nuestras manos seguían pegadas."
    with dissolve
    with hpunch
    show Levi sorpendido s
    with dissolve
    play music "medieval.mp3"
    hide Levi sorpendido s
    with fade
    show Hange sorprendida2 s
    with dissolve
    z "¡Guau! ¡No puedo creerlo!"
    n "-Los gritos de una persona nos sacaron de ese momento de paz-"
    z "¡Los soldados más fuertes de la humanidad son pareja!"
    play sound "hanjiaAAA.mp3"
    z "¡No puedo creerlo!"
    n "-Gritó emocionada dando brincos de felicidad y mirándonos de manera curiosa-"
    hide Hange sorprendida2 s
    with dissolve
    play sound "cuatrojos.mp3"
    show Levi enojado sbe
    with dissolve
    l "¿Qué haces aquí, cuatro ojos de mierda?"
    show Levi sonrojado s
    with dissolve
    n "-Preguntó Levi totalmente avergonzado-"
    hide Levi sonrojado s
    with dissolve
    show Hange alegre s
    with dissolve
    n "Hange solo se reía, nos volteaba a ver y volvía a reír."
    n "Era la situación más incómoda de mi vida. No podía ocultar lo avergonzada que estaba en ese momento."
    m "¿Desde cuándo has estado ahí escondida?"
    n "-Pregunté con miedo a la respuesta sin atreverme a mirarla a los ojos-"
    show Hange feliz s
    with dissolve
    z "¡Eso no importa!"
    n "-Gritó con felicidad-"
    show Hange gi1 s
    with dissolve
    z "¡Solo sé que has hecho una buena elección, Mikasa!"
    show Hange normal s
    with dissolve
    n "-Me dijo tomando mis manos y mirando a Levi, quien estaba avergonzado-"
    with hpunch
    m "¡No es lo que parece!"
    n "-Intenté decir con los nervios de punta-"
    show Hange alegre s
    with dissolve
    z "¡No te preocupes, Mikasa, todos lo entenderán!"
    show Hange feliz s
    with dissolve
    n "-Dijo corriendo a su caballo-"
    show Hange gi2 s
    with dissolve
    z "¡Todos van a celebrar su relación!"
    n "-Dijo montándose en el caballo y saliendo del lugar-"
    hide Hange gi2 s
    with dissolve
    n "Me quedé anonadada ante lo que acababa de pasar."
    n "Hange nos había visto y estaba dispuesta a contárselo a todo el mundo. Mi vergüenza estaba al límite."
    show Levi enojado sbe
    with dissolve
    l "¡Hay que intentar alcanzarla!"
    show Levi enojado s
    with dissolve
    n "-Acercó mi caballo y me subí a él-"
    l "¡Me las va a pagar!"
    n "-Gritó enojado comenzando a cabalgar fuera del bosque. Yo corrí detrás de él-"
    hide Levi enojado s
    with fade
    scene bosque2
    with dissolve
    n "El trayecto se volvió algo incómodo, no nos dirigimos palabra alguna en ningún momento."
    n "Aún estaba avergonzada por lo que acaba de pasar."
    scene establo
    with dissolve
    n "Con tiempo, llegamos al cuartel, dejamos los caballos en el establo y entramos al comedor a buscarla."
    play music "murmurando.mp3"
    scene tarven
    with dissolve
    n "MALA IDEA."
    n "Todos los presentes voltearon a vernos sorprendidos, algunos susurraban y otros solo sonreían. Caminamos entre las mesas y las miradas nos seguían."
    n "(Perfecto)"
    n "-Me dije-"
    n "(Lo que más odio)"
    n "-Pensé al ver todas las miradas sobre mí-"
    n "Parecía que Hange no estaba ahí, demasiado tarde de nuevo."
    n "Hange les había dicho a todos lo que había visto y por eso todos nos miraban con sorpresa y admiración."
    n "Mordí mi labio inferior por la incomodidad y terminamos saliendo al pasillo."
    stop music
    scene pasillo2
    with fade
    show Levi enojado sbe
    with dissolve
    l "Iré a buscarla."
    show Levi enojado s
    with dissolve
    n "-Mencionó molesto-"
    show Levi hablando s
    l "¡Vete a tu cuarto!"
    show Levi preocupado s
    with dissolve
    n "-Me miró algo preocupado-"
    n "Solo asentí con la cabeza sin protestar."
    hide Levi preocupado s
    with dissolve
    scene taberna
    with fade
    n "Caminé por el pasillo hasta llegar a mi cuarto. Me hubiera encantado encerrarme pero no podía porque compartía cuarto con Sasha."
    n "Así que decidí dormirme antes de que ella llegara y empezase a preguntarme qué había pasado."
    n "Me volteé dándole la espalda a la puerta y, antes de dormir, toqué mis labios esbozando una pequeña sonrisa."
    with fade
    show lili
    show screen modal_example
    n "= LEVI ="
    show screen style_prefix_screen
    scene habita
    with dissolve
    play sound "musica normal.mp3"
    n "El día había comenzado de la peor manera."
    call screen style_prefix_screen
    with dissolve
    n "Me encontraba en la oficina de Erwin con la peor de mis miradas dirigidas a una persona en específico."
    show Errwin normal cba
    with dissolve
    r "¡Estamos listos para la exploración!"
    show Erwim feliz c
    with dissolve
    n "-Mencionó Erwin con una sonrisa-"
    show Erwin normal c
    with dissolve
    r "¡Díganles a los cadetes que se preparen!"
    n "-Nos dijo mirándonos con seriedad-"
    hide Erwin normal c
    hide Erwim feliz c
    hide Errwin normal cba
    with dissolve
    show Hange preocupada c
    with dissolve
    z "¡No lo haré hasta que Levi dejé de verme así!"
    n "-Gritó haciendo un puchero enfrente de Erwin-"
    hide Hange preocupada c
    with dissolve
    show Erwin incomodo2 c
    with dissolve
    r "¿Podrían dejar de pelear?"
    show Erwin normal c
    with dissolve
    r "¡La exploración es más importante!"
    n "-Dio un gran suspiro mientras esperaba respuestas-"
    hide Erwin normal c
    with dissolve
    show Hange insegura c
    with dissolve
    z "¡Ya, enano, perdóname!"
    show Hange preocupada c
    with dissolve
    n "-Me sacó de mis casillas-"
    l "¿Tenías que decírselo a todo el mundo?"
    n "-Grité molesto con la peor de mis miradas-"
    l "¡Ni siquiera sabías qué pasó entre nosotros!"
    n "-Gruñí molesto y algo incómodo-"
    hide Hange preocupada c
    with dissolve
    show Errwin normal cba
    with dissolve
    r "¡Arreglen sus problemas después!"
    r "¡Hange tendrás que solucionarlo!"
    play sound "puerta.mp3"
    show Erwin normal c
    with dissolve
    n "-Ordenó poniéndose en pie y saliendo de la oficina. Yo salí detrás de él realmente molesto-"
    hide Erwin normal c
    with dissolve
    scene establo
    with fade
    play music "musica sadhappy.mp3"
    n "Caminé en dirección al establo para sacar mi caballo, teníamos una nueva expedición que era realmente molesta pero necesaria para la humanidad."
    n "Dentro del establo divisé a esa persona especial que me volvía loco."
    show Mikasa sonrojada1 c
    with dissolve
    n "-Me acerqué a ella-"
    n "Ella, al verme, tomó las mismas características de siempre."
    n "Ese típico color rojo en sus mejillas que la hacía ver hermosa, más de lo que ya era, y su mirada baja por la vergüenza."
    m "Buenos días, capitán."
    n "-Su voz era realmente dulce y provocadora-"
    l "Sí..."
    n "-Dije sin más, no sabía cómo lidiar con estas cosas-"
    show Mikasa normal c
    with dissolve
    m "Lamento lo de ayer."
    n "-Dijo borrando la linda expresión de su rostro, cambiándolo a un semblante triste y apagado-"
    l "¿Por qué se disculpa?"
    n "-Mencioné algo preocupado por la respuesta-"
    n "Se quedó callada con la misma mirada, di un suspiro, no me gustaba ese rostro..."
    n "Solo aquel en donde sus ojos grises brillaban si estabas cerca, donde se posaba una hermosa sonrisa, donde sus mejillas resplandecían."
    n "Todo ello me provocaba sensaciones raras en todo mi cuerpo, me excitaba. Me hacía perderme en sus ojos y admirar el brillo que desprendía de ellos."
    n "Además de conocerla con la mirada, saber cómo se sentía y qué pensaba, era un rasgo único que entre nosotros dos era idéntico."
    n "Su sonrisa era hermosa, sus labios color durazno eran suaves y cálidos, sus manos eran delicadas y suaves, el cabello azabache brillante era sedoso y suave."
    n "Aquella chica me volvía loco, sin darme cuenta no podía dejar de pensar en ella."
    n "Era cómodo estar a su lado, era como estar con otro yo, éramos idénticos en muchas cosas."
    n "Ella era hermosa, fuerte, valiente y una gran persona; solo bastaba con conocerla para decir que ella era perfecta."
    n "El hecho de que ella me dijese que quería conocerme me excitaba y me provocaba miles de sensaciones."
    n "Por más que quería, no podía alejarla porque me gustaba estar con ella. Su presencia me tranquilizaba, su olor me hacía sentirme seguro y con paz."
    n "Di un largo suspiro, me bajé del caballo y me dirigí a ella con un objeto en mi mano."
    l "Ten."
    n "-Le dije acercando el objeto-"
    l "Esto es tuyo, lo encontré ayer en el establo."
    n "-Me miró mientras tomaba el objeto en sus manos-"
    m "Gracias."
    show Mikasa enojada c
    with dissolve
    m "Pero no la quiero de vuelta."
    n "-Mencionó molesta-"
    show Mikasa normal c
    with dissolve
    l "La he lavado, acéptala por eso."
    n "-Mencioné molesto-"
    l "El olor de Jaeger ya no está..."
    show Mikasa feliz c
    with dissolve
    l "Así que puedes usarla sin problemas."
    n "-Me molestaba el hecho de que Jaeger complicar las cosas-"
    hide Mikasa feliz c
    with dissolve
    scene img8
    show bht
    with dissolve
    with fade
    n "Apareció en su rostro una sonrisa de aquellas que me provocaban cosas en el estómago y me sonrojé."
    n "Me miró y se acercó a mí para enrollarme la bufanda en mi cuello."
    l "¿Qué haces?"
    n "-Pregunté extrañado por su acción y algo avergonzado-"
    m "Quiero que su olor quede impregnado en mi bufanda"
    n "-Mencionó suavemente excitándome con su voz y su deseo-"
    m "Solo así usaré la bufanda."
    l "Tch..."
    n "-Dije fingiendo estar molesto cuando en realidad era todo lo contrario-"
    with fade
    show establo
    show Mikasa feliz c
    with dissolve
    n "Quitó la bufanda con cuidado y se la enrolló en su cuello como solía usarla."
    n "Escondió su boca y nariz en ella para olfatear el nuevo olor, esa escena me excitaba y me alegraba."
    n "Sabía que debía mostrar desinterés, pero voté para sonreír, de lo cual ella se dio cuenta e imitó mi gesto."
    show Mikasa sonrojada2 c
    with dissolve
    m "¡Gracias, capitán!"
    n "-Dijo dulcemente mostrando una de sus más bellas sonrisas-"
    n "Sonreí de lado, no era bueno con las palabras pero esperaba que con ello se conformara por ahora."
    l "Vamos a la formación."
    show lili
    with fade
    n "-Le dije comenzando a cabalgar con ella a mi lado-"
    n "Una vez en la formación nos tuvimos que separar, puesto que yo era el comandante del escuadrón de operaciones especiales."
    n "Ella se quedó a mi lado derecho, a mucha distancia, pero aun así podía verla y escuchar lo que pasaba cerca de ella."
    scene pueblo
    with fade
    play music "Gente gritando.mp3"
    show Mikasa normal c
    with dissolve
    n "Al caminar entre la multitud que nos despedía entre gritos dos pequeños niños se acercaron a ella."
    show Mikasa feliz c
    with dissolve
    ni"¡Cuando sea grande quiero ser como usted!"
    n "-Mencionó una pequeña niña de coletas con una sonrisa tierna y brillantes ojos-"
    lo"¡Yo quiero unirme a la Legión de Reconocimiento para tener las alas de la libertad!"
    n "-Gritó un niño de emoción alzando sus manos-"
    m "Tienes que trabajar muy duro..."
    n "-Le dijo a la pequeña niña con su dulce voz mientras acariciaba su cabeza-"
    m "Y tú tienes que cuidar de tu hermana para que puedas entrar en la legión..."
    n "-Le dijo brindándole una hermosa sonrisa-"
    lo"¡Si, lo prometo!"
    n "-Dijo el pequeño haciendo torpemente el saludo militar-"
    n "-Mikasa solo rió y volvió a fijar su mirada en su puesto-"
    n "Realmente era hermosa y una buena persona, solo bastaba con conocerla para saber que era perfecta."
    n "El recuerdo de lo que había dicho regresó tras haver presenciado esa tierna escena."
    n "(Sería una gran madre)"
    n "-Pensé con una sonrisa boba-"
    show Mikasa normal c
    with dissolve
    r "¡Todos saben sus posiciones!"
    hide Mikasa normal c
    with dissolve
    show Errwin normal cba
    with dissolve
    r "¡Hagamos de esta exploración una victoria más!"
    r "¡No olviden entregar sus corazones!"
    show Erwin normal c
    n "-Los gritos de Erwin me pusieron de vuelta en mi puesto atento-"
    show Errwin normal cba
    r "¡Adelante!"
    hide Errwin normal cba
    with dissolve
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    n "-Gritó mientras avanzaba con su caballo y los demás comenzamos a seguirle en dirección a la puerta-"
    stop music
    with flashbulb
    scene exterior
    with dissolve
    n "Salimos de los muros y un nuevo mundo se abría ante nosotros."
    n "Siempre era sorprendente ver ese paisaje nuevo. Rápidamente todos tomamos nuestras posiciones."
    show Mikasa feliz c
    with dissolve
    n "Di una mirada rápida a la chica que me dio una sonrisa antes de alejarse de mi posición y ponerse en la suya."
    n "Regresé mi vista a mi puesto, confiaba en ella y sabía que no le pasaría nada. Era la primera vez que me preocupaba por alguien externo en una misión."
    n "(Realmente me traes loco, Ackerman, ya hay otra persona que forme parte de mis lazos más importantes)"
    show screen style_prefix_screen2
    n "-Pensé esbozando una sonrisa-"
    hide Mikasa feliz c
    with dissolve
    show lili
    call screen style_prefix_screen2
    l "..."
    call screen modal_example
    show text "{size=+25}{color=#FFFFFF}Capítulo 4{/color}{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}FIN{/color}{/size}" at truecenter
    with dissolve
    pause 0
    hide text
    with dissolve
    $persistent.cap5 = True
    return

label capitulo5:
    play music "suspenso.mp3"
    show text "{size=+25}{color=#FFFFFF}Capítulo 5{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}Especie no identificada{/color}{/size}" at truecenter
    with dissolve
    pause 8
    hide text
    show screen quick_menu
    with dissolve
    show lili
    with fade
    show bosque6
    with dissolve
    n "El ambiente era tenso, estábamos rodeados de áreas verdes y pocos árboles de diferentes tamaños."
    n "El aire era pesado y provocaba escalofríos en todo el cuerpo, nos encontrábamos en territorio de titanes..."
    n "... los mayores enemigos y asesinos de la humanidad."
    n "A pesar de que ya habíamos estado fuera de las murallas, el miedo jamás se iba y la desesperación siempre regresaba."
    n "Nuestro objetivo era *Recolectar materiales y materia prima en el bosque de los árboles gigantes*."
    n "Aquello era debido a la cantidad de pérdidas generadas por la invasión de los titanes dentro de los muros."
    n "Miraba con total atención mi alrededor, en busca de un posible titán cerca o de alguna señal de humo."
    n "Apretaba con fuerza las riendas de mi caballo mientras cabalgaba. Mi respiración era agitada."
    n "Mordí mi labio inferior para intentar calmar la angustia que tenía."
    n "Me encontraba sola, ubicada en el flanco derecho centro del grupo principal."
    n "Ahí se encontraban el comandante Erwin, Hange y el escuadrón de Levi."
    n "Mi misión consistía en proteger al grupo principal avisando de algún indicio de avistamiento de titán lanzando una señal."
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    show bht2
    with flashbulb
    with dissolve
    n "Agradecía encontrarme cerca del grupo principal para estar cerca de una persona."
    n "Sonreí de medio lado y acaricié mi bufanda, el olor se desprendió al momento de tocarla."
    n "Respiré con tranquilidad aquel olor tan peculiar y único que lograba acelerar mi corazón y sonrojarme."
    n "El recuerdo de su última sonrisa antes de separarnos provocaba un revoloteo en mi estómago."
    n "El sentimiento de estar cerca de él, de estar cabalgando a su lado, se hacía cada vez más intenso; mi corazón palpitaba rápidamente al imaginarme la escena."
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    with flashbulb
    show bosquebl
    with hpunch
    with fade
    so"¡Excéntrico!"
    n "El grito de un soldado me sacó de mis pensamientos y volteé rápidamente en dirección al titán."
    n "Un titán de aproximadamente 10 metros corría veloz en mi dirección."
    n "Sin dudarlo, me puse de pie sobre el lomo de mi caballo manteniendo el equilibrio mientras sacaba mis cuchillas."
    show bosque1
    with dissolve
    n "Una vez más cerca, dirigí uno de mis cables al cuerpo del titán, clavándolo en él. Con agilidad volé en dirección al titán dando vueltas y piruetas en el aire."
    show acciti
    with pushleft
    n "Llegué a la zona de la nuca y la corté con profundidad."
    play sound "stuijm.mp3"
    scene bosquebl
    with pushright
    n "El titán cayó de golpe al suelo y regresé a mi caballo para tomar de nuevo mi posición."
    scene bosque1
    with pushdown
    so"¡Muy bien hecho, Ackerman!"
    n "-Exclamó aquel soldado mientras disparaba la bengala verde en el aire.-"
    so"¡Sus movimientos son únicos!"
    n "-Me alagó mientras cabalgaba a mi lado-"
    m "Gracias."
    n "-No me gustaba ser alagada porque no sabía cómo reaccionar-"
    n "Poco a poco el cielo se teñía de color verde a causa de las bengalas que indicaban que la dirección al bosque era segura."
    show bosu
    with dissolve
    n "Así que comenzamos a entrar al enorme bosque de árboles gigantes y tremenda vegetación."
    n "El olor a hierba era muy perceptible, así como la oscuridad provocada por la poca entrada de luz en el bosque."
    n "Dentro del bosque nos unimos en grupos para evitar perdernos y para cuidarnos la espalda sin dejar a un lado el objetivo principal."
    n "El camino comenzaba a ser denso y la probabilidad de ganar aumentaba."
    n "Teníamos las enormes ramas de los árboles para usar el equipo de maniobras sin problemas."
    show Levi enojado cbe
    with dissolve
    l "¡No olviden el objetivo principal!"
    show Levi normal c
    with dissolve
    n "-Exclamó nuestro capitán-"
    show Levi hablando c
    with dissolve
    l "¡Estén alertas!"
    show Levi normal c
    with dissolve
    n "-Gritó mientras se posicionaba enfrente de todos-"
    hide Levi normal c
    with dissolve
    show Erwin normal c
    with dissolve
    so"¡Comandante!"
    n "-Gritó un soldado que había salido de otro lugar-"
    show Erwin incomodo2 c
    with dissolve
    so"¡El flanco izquierdo sur ha sido eliminado por completo!"
    n "-Un sudor frío corrió por mi cuerpo-"
    so"¡El flanco izquierdo centro está teniendo problemas!"
    n "-Exclamó aterrado mientras cabalgaba cerca del comandante-"
    n "No escuché lo que el comandante decía, por mí cabeza solo retumbaban las palabras de ese hombre."
    hide Erwin incomodo2 c
    with dissolve
    show lili
    with dissolve
    show text "{size=+25}{color=#FFFFFF}*El flanco izquierdo sur ha sido eliminado por completo*{/color}{/size}" at truecenter
    with dissolve
    pause 4
    hide text
    show bosu
    with dissolve
    n "Intenté recordar si alguien de mis compañeros estaba en esa ubicación..."
    n "Solté un suspiro de alivio al recordar que no había nadie ahí, hasta que la segunda parte retumbó."
    show lili
    with dissolve
    show text "{size=+25}{color=#FFFFFF}*El flanco izquierdo centro está teniendo problemas*{/color}{/size}" at truecenter
    with dissolve
    pause 4
    hide text
    scene bosu
    with dissolve
    with hpunch
    m "¡Armin!"
    n "-Grité al recordar que mi amigo estaba en esa zona, tomé las riendas de mi caballo con desesperación y cambié mi ruta-"
    r "¡Ackerman, ¿a dónde va?!"
    n "-Gritó el comandante mientras me seguía por detrás-"
    r "¡No puede ir sola y mucho menos romper la formación!"
    m "¡Armin está ahí y no voy a dejar que muera!"
    n "-Grité cabalgando más rápido, dejando atrás mi posición-"
    show bosdespe
    with fade
    play sound "corazon.mp3"
    n "Mi corazón palpitaba demasiado rápido, así como mi respiración era agitada."
    n "Mis manos sudaban mientras apretaban con fuerza las riendas. Sabía que estaba rompiendo las reglas y que posiblemente recibiría un castigo por eso."
    n "Pero me aterrorizaba saber que Armin estaba en esa zona y que podría pasarle algo."
    n "Decidida, mordiendo mis labios, avancé lo más rápido que pude a la zona."
    n "En el camino encontraba los restos de algunos compañeros y charcos de sangre que bañaban el pasto verde de alrededor."
    n "La desesperación comenzó a crecer en mi ser y rezaba por que Armin estuviera bien."
    show despeb
    with fade
    n "A unos cuantos metros logré divisar a Armin con Jean inconsciente a su espalda mientras intentaba alejarse del titán en su caballo."
    n "Se trataba de un excéntrico, uno de unos 8 metros, pero era diferente a los otros."
    n "Algo me hacía pensar que ese titán era extraño, más de lo que ya podían ser."
    show Armin soprendido1 s
    with dissolve
    with hpunch
    m "¡Armin!"
    n "-Grité su nombre acelerando el paso-"
    m "¡Cuidado!"
    n "-Le grité al ver cómo el titán se abalanzaba sobré él-"
    n "Armin volteó rápidamente y, tomando a Jean con rapidez, se tiró del caballo logrando esquivar al titán."
    hide Armin soprendido1 s
    with dissolve
    n "Paré un momento y saqué el aire de alivio contenido en mis pulmones al ver que Armin estaba bien."
    n "Armin realmente era listo, pensaba y actuaba rápido sin preámbulos."
    n "Con dificultad se colocó de espaldas a un árbol con Jean en los brazos."
    n "Con una mano sujetaba su cuchilla apuntando al titán que se acercaba con sed de sangre hacia él."
    n "El recuerdo de las palabras del capitán entró en mi cabeza y retumbaron fuertemente."
    show lili
    with dissolve
    show text "{size=+25}{color=#FFFFFF}*¿No quieres la felicidad y seguridad de tu amigo?...*{/color}{/size}" at truecenter
    with dissolve
    pause 4
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}*...Entonces no te eches para atrás, cuida de ese mocoso y valora su presencia...*{/color}{/size}" at truecenter
    with dissolve
    pause 4
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}*En este mundo nunca sabes por cuánto tiempo una persona podrá estar a tu lado...*{/color}{/size}" at truecenter
    with dissolve
    pause 4
    hide text
    show despeb
    with dissolve
    m "Desperté del impacto de sus palabras y con determinación me dirigí directo al titán."
    play sound "huyendo4.mp3"
    n "Dejando atrás mi caballo, sin dudar ni un segundo. Tenía razón, debía proteger lo más importante para mí para no perderlo."
    show bosque1
    with fade
    show bosque1
    with dissolve
    n "Clavé los ganchos en el cuerpo del titán mientras me impulsaba con ayuda de los árboles para llegar a él."
    show dosti
    with pushleft
    play sound "stuijm.mp3"
    n "Este, al sentir los cables, volteó rápidamente a verme dispuesto a atacar. Con rapidez y agilidad esquivé su mano y aterricé en una rama."
    scene dosna
    with pushright
    n "El titán cayó de golpe al suelo y regresé a mi caballo para tomar de nuevo mi posición."
    scene bosque1
    with pushdown
    n "Realmente el titán era excéntrico, pero era diferente a los otros; se movía muy rápido y hacía movimientos impredecibles por lo que era difícil acercarse a él."
    a "¡Mikasa!"
    n "El gritó de Armin me sacó de mis pensamientos."
    with hpunch
    n "Reaccionando a destiempo caí de la rama en un intento por esquivar el manotazo del titán que había saltado hasta la rama que estaba."
    n "Rápidamente me incorporé y, lanzando los cables, logré tomar equilibrio en el aire para después llegar al suelo. Estaba realmente agitada y sorprendida."
    n "No podía creer que me costará tanto matar a un titán cuando yo era experta en eso."
    show dosti
    with pushleft
    n "El titán volvió a abalanzarse sobre mí y solté los ganchos clavándolos en los árboles más cercanos a este."
    n "Con impulso me levanté en el aire mirándolo desde mucha altura. Tenía que matarlo."
    n "No solo para proteger a mis amigos, sino porque ese titán era extraño y un peligro para la humanidad."
    scene dosna
    with pushright
    n "Caí en picada en dirección al titán."
    n "Dando vueltas para llegar más rápido me dirigí a la nuca, estaba a punto de cortarla cuando este lo esquivó en el último segundo."
    scene bosque1
    with pushdown
    with hpunch
    m "¡¿Qué?!"
    n "-Exclamé levantándome del suelo por la caída-"
    m "¡¿Pero... cómo?!"
    n "-No podía creerlo, mis movimientos eran realmente rápidos, ningún titán podía escapar de ellos-"
    show dosna
    with dissolve
    n "Miré con miedo y enojo al titán al mismo tiempo, este solo mostraba una horrorosa sonrisa."
    n "Sus ojos penetrantes, fijados en mí, me causaban escalofríos. Parecía regenerarse rápido ya que no mostraba herida alguna."
    n "Ni siquiera podía tocarle ni acercarme a él, comenzaba a desesperarme, jamás había tardado en matar a uno."
    n "Pero mis sospechas comenzaban a ser ciertas, ese titán era raro, anormal, no podía ser un excéntrico, debía ser una especie no identificada."
    show despeb
    with dissolve
    play sound "oi levi.mp3"
    show Levi enojado cbe
    with dissolve
    l "¡Ackerman! ¡Arlert!"
    show Levi normal c
    with dissolve
    n "-Escuché que alguien nos llamaba pero no aparté mi mirada del titán-"
    show Levi enojado cbe
    with dissolve
    l "¿Qué diablos hacen aquí?"
    show Levi enojado c
    with dissolve
    n "-Exclamó molesto. Sabía quién era-"
    hide Levi enojado c
    with dissolve
    show Armin enojado sc
    with dissolve
    a "¡Capitán Levi... un titán excéntrico atacó al flanco izquierdo centro y sur!"
    a "¡Solo Jean y yo estamos vivos!"
    show Armin disgustado cce
    with dissolve
    n "-Gritó con desesperación-"
    show Armin disgustado c
    with dissolve
    a "¡Mikasa me ha salvado la vida!"
    show Armin disgustado cce
    with dissolve
    n "-Exclamó con ganas de llorar-"
    hide Armin disgustado cce
    with dissolve
    show Eren preocupado c
    with dissolve
    e "Armin, tranquilízate... ese titán no es la gran cosa."
    n "-Mencionó fastidiado de las acciones del rubio-"
    show Eren enojado3 c
    with dissolve
    e "Que no puedas matar un titán es diferente..."
    show Eren normal c
    with dissolve
    n "Volteé con odio hacia Eren por lo que le había dicho a Armin."
    n "Sabía que no era el momento de pelear, pero hablaba como si él fuera el mejor matando titanes cuando nunca lo había hecho."
    hide Eren normal c
    with dissolve
    show Armin disgustado cce
    with dissolve
    n "Ver a Armin cabizbajo solo me causaban ganas de golpear a Eren y regresarle sus palabras."
    hide Armin disgustado cce
    with dissolve
    with hpunch
    n "Pero el enorme estruendo de los pasos del titán me hicieron tomar pose de ataque y no dejar de ver a mi enemigo."
    n "El miedo me invadía, los escalofríos en mi cuerpo se hacían presentes, mi respiración se agitaba..."
    n "El sudor de mis manos y la ira tomaban posesión de mi cuerpo, provocándome fiereza y hartazgo de todo."
    show dosti
    with pushleft
    play sound "stuijm.mp3"
    n "Salí disparada directa a la cabeza del titán, cortando uno de sus ojos y varios dedos de la mano que había levantado para agarrarme."
    scene dosna
    with pushright
    n "Tomé impulso en un árbol y volé directa a una de sus piernas para cortarla, logrando que este cayera."
    show dosti
    with pushleft
    play sound "stuijm.mp3"
    n "Con agilidad subí corriendo por su espalda y corté con agresividad su hombro, lastimando el músculo de su brazo para que no pudiera levantarlo."
    n "El titán gritó con desesperación mientras intentaba ponerse de pie y levantar la otra mano."
    show dosti
    with pushleft
    play sound "stuijm.mp3"
    n "Volé en dirección a la otra mano y la corté antes de que terminara de regenerarse."
    show despeb
    with dissolve
    n "Sentí la mirada de las 3 personas que se encontraban debajo de mí."
    show Eren normal c
    with dissolve
    e "..."
    hide Eren normal c
    with dissolve
    show Armin enojado cce
    with dissolve
    a "¡...!"
    hide Armin enojado cce
    with dissolve
    show Levi preocupado c
    with dissolve
    l "..."
    hide Levi preocupado c
    with dissolve
    n "Di una vista rápida, me miraban con asombro y preocupación, como si nunca me hubieran visto luchar contra un titán."
    show dosti
    with pushleft
    scene dosna
    with pushright
    play sound "stuijm.mp3"
    n "Regresé mi mirada furiosa al titán y, realizando mis típicos giros en el aire, di por fin en la nuca del titán, cortándolo profundamente y acabando con todo."
    show despeb
    with dissolve
    n "Quedé parada en el frondoso pasto con el titán comenzando a evaporarse frente a mí. Mi respiración agitada comenzaba a disminuir."
    n "La tensión de mis músculos también, al igual que la ira que me apresaba en ese momento, empezaban a desvanecerse."
    play music "Dream.mp3"
    show Armin soprendido1 s
    with dissolve
    a "¡Mikasa!"
    show Armin disgustado cce
    with dissolve
    n "-Giré para ver a mi amigo-"
    a "¿Estás bien?"
    a "¿No éstas herida?"
    n "-Preguntó tomando una de mis manos e inspeccionándola muy preocupado-"
    show Armin feliz c
    with dissolve
    m "Estoy bien, Armin, tranquilo."
    n "-Le dije mostrando una sonrisa ante su preocupación-"
    m "¿Tú estás bien?"
    n "-Pregunté mirándolo preocupada-"
    a "Estoy bien gracias a ti."
    show Armin disgustado cce
    with dissolve
    n "-Mencionó cabizbajo-"
    show Armin disgustado c
    with dissolve
    a "Jean se lastimó por intentar defenderme, pero no tiene heridas graves."
    show Armin disgustado cce
    with dissolve
    n "-Mencionó mirando de reojo a Jean siendo tratado por Levi-"
    show Armin disgustado c
    with dissolve
    a "Tanto tú como él me salvaron la vida y yo no pude hacer nada..."
    show Armin disgustado cce
    with dissolve
    n "-Apretó sus labios y puños en señal de que se sentía culpable mientras se aguantaba las ganas de llorar-"
    scene img8b
    show abrazo
    with dissolve
    m "Armin..."
    n "-Pronuncié su nombre con ternura mientras lo abrazaba-"
    m "Sabes que daría mi vida por protegerte, eres muy importante para mí y también para Jean."
    n "-Le brindé una cálida sonrisa-"
    n "Optó solo por devolverme la sonrisa mientras correspondía mi abrazo."
    n "Saber que estaba bien lograba que mi corazón se calmase y la tranquilidad regresará a mí."
    n "Acaricié su cabeza mientras lo abrazaba. Realmente era un niño, mi mejor amigo, alguien realmente lindo y muy inteligente."
    n "Me preguntaba cuál había sido la última vez que lo había abrazado, la última vez que habíamos pasado un momento así."
    n "Se sentía una infinita paz y tranquilidad estando a su lado. Saber que tenía a una persona así de importante en mi vida me hacía sentir feliz y agradecida."
    n "Durante el abrazo sentí la mirada penetrante de Eren."
    n "Volteé a verlo de reojo sin separarme de Armin."
    n "Su cara mostraba las expresiones de siempre: enojo y fastidio. Con delicadeza me separé de Armin."
    show despeb
    with dissolve
    n "Le brindé una cálida sonrisa y, tomándolo de la mano, nos dirigimos hacia donde estaba el capitán Levi con Jean, pasando de largo a Eren."
    show Armin soprendido1 s
    with dissolve
    a "Jean... ¿Estás bien?"
    show Armin disgustado cce
    with dissolve
    n "-Preguntó algo apenado sin mirarle a los ojos y sin soltar mi mano-"
    je"Estoy bien, perdón por ser tan débil Armin."
    n "-Dijo de la misma manera: apenado y cabizbajo-"
    je"Quería protegerte pero al final fuí un estorbo y terminamos ambos siendo salvados por Mikasa."
    n "-Comentó apretando los labios-"
    m "Gracias, Jean..."
    n "-Le dije suavemente-"
    show Armin serio c
    with dissolve
    m "Por proteger a Armin y permitir que llegase a tiempo para ayudaros."
    n "-Se giró y me miró sorprendido para después darme una sonrisa a mí y a Armin-"
    hide Armin serio c
    with dissolve
    n "Dejé a Armin con Jean para que hablaran y terminara de curar sus heridas."
    show Levi normal c
    with dissolve
    n "Yo fuí directo con el capitán, quien miraba atentamente los restos del titán que se evaporaban con el tiempo."
    m "No era un titán excéntrico, ese era diferente..."
    n "-Mencioné yendo al grano-"
    m "Es una especie no identificada."
    n "-Recalqué mirándolo esperando su aprobación-"
    show Levi hablando c
    with dissolve
    play sound "solke.mp3"
    l "Tienes razón, Ackerman..."
    show Levi normal c
    with dissolve
    n "-Mencionó mirándome fijamente-"
    show Levi normal2 c
    with dissolve
    l "Para que hayas tenido problemas derrotándolo, significa que es otra especie."
    n "-Me alegraba saber que reconocía mi fuerza y que estaba de acuerdo con mi teoría-"
    show Levi hablando c
    with dissolve
    l "Lo mejor será irnos de aquí, no sabemos si puede haber más. Regresemos con Hange y Erwin."
    show Levi normal c
    with dissolve
    n "-Regresó a donde estaba su caballo y todos hicimos lo mismo siguiendo sus pasos-"
    hide Levi normal c
    with dissolve
    play music "Most Beautiful.mp3"
    show bosdespe
    with fade
    show Eren normal s
    with dissolve
    n "Durante el camino Eren no paraba de observarme con sus ojos penetrantes."
    n "Comenzaban a molestarme más sus actitudes infantiles y que fingiera que no pasaba nada."
    n "Soltaba bufidos de molestia, cosa que el capitán no pasaba desapercibido ya que cada que podía volteaba a verme intentando descifrar qué me molestaba."
    n "Ese acto por su parte me hacía feliz."
    n "Estábamos a punto de llegar a donde se suponía que era el encuentro..."
    play music "Dark Tension.mp3"
    with hpunch
    show titih
    with fade
    n "Y de la nada salieron dos de aquellos titanes, los mismos que el anterior, uno de frente y otro por detrás de nosotros, tomándonos por sorpresa."
    show bosdespe
    with dissolve
    show Levi enojado cbe
    with dissolve
    l "¡Ackerman, protege a Jaeger y a Arlert!"
    hide Levi enojado cbe
    with dissolve
    n "-Me ordenó dirigiéndose de frente a por el otro titán-"
    n "Di la vuelta en mi caballo y me dirigí al que venía por atrás con gran velocidad."
    n "Solté los cables y clavé los ganchos en dos árboles para volar sobre el Titán."
    show bosdespe
    with pushleft
    n "Este paró en seco y siguió mi movimiento olvidándose de los otros; era mi oportunidad."
    scene wetimi
    with pushright
    play sound "stuijm.mp3"
    n "Tomé impulso en un árbol y volé directa a una de sus piernas para cortarla, logrando que este cayera."
    n "Después me dirigí a la cabeza esquivando la cantidad de manotazos que me lanzaba en el camino. Ya estaba cerca de la cara."
    with hpunch
    n "Cambié mi maniobra y volé por detrás de su cabeza hasta llegar a la cara."
    play sound "stuijm.mp3"
    n "Lancé mis cuchillas a sus ojos para dejarlo ciego unos segundos, funcionó."
    show bosdespe
    with pushleft
    with hpunch
    play sound "stuijm.mp3"
    n "Terminé por rematar sus brazos y manos cortando sus dedos. Soltó un grito desgarrador..."
    with hpunch
    n "Giré rápidamente en dirección a la nuca dando un corte perfecto y mortal para él."
    n "Al parecer, haber peleado con el otro titán me había enseñado el método para acabar con este."
    n "Fue entonces que recordé que eran dos y yo había acabado con uno."
    show ppletitan
    with dissolve
    n "Giré mi vista hacia Levi y mis pupilas se dilataron ante la imagen que acaba de ver."
    show bosdespe
    with fade
    n "Levi había sido lanzado a un árbol por un manotazo del titán."
    with hpunch
    play music "The Power of Mind.mp3"
    m "¡Levi!"
    show bosque1
    with dissolve
    n "-Grité su nombre mientras volaba entre las ramas para llegar a él-"
    show bosu
    play sound "salva1.mp3"
    with fade
    scene img9
    show herido
    with dissolve
    m "¡Espera, no deberías moverte!"
    n "-Me incliné a donde estaba y lo levanté despacio y con cuidado-"
    m "¿Estás bien?"
    l "Protege a..."
    n "-Tosió escupiendo sangre y quejándose del dolor-"
    n "Lo miré un momento, su espalda estaba cubierta de sangre y sus ropas estaban totalmente rasgadas."
    n "Mi cuerpo se estremeció al verlo."
    n "Mi respiración estaba agitada por no creer lo que estaba viendo, mi corazón latía desaceleradamente y sin control lleno de pánico."
    n "Levi tomó una de mis manos intentando resistir el dolor mientras cerraba sus ojos y apretaba mi mano con fuerza."
    n "Jadeaba por el cansancio y su cuerpo estaba tenso, estaba perdiendo mucha sangre y por ello sus fuerzas también se iban."
    n "Con determinación y total cuidado lo cargué mientras se quejaba del dolor y lo llevé con Jean y Armin para que lo tratarán."
    show bosdespe
    with fade
    show Armin soprendido1 s
    with dissolve
    a "¿Mikasa?"
    show Armin serio c
    with dissolve
    n "-Escuché a Armin, quien me veía con preocupación-"
    show Armin enojado sc
    with dissolve
    a "¡No vayas!"
    play music "The Path of Silence.mp3"
    show Armin disgustado cce
    with dissolve
    n "-Me pidió con miedo tomando mi mano-"
    show Armin soprendido1 s
    with dissolve
    play sound "Mikasalimit.mp3"
    with hpunch
    scene img9b
    show asesina
    with dissolve
    m "¡Voy a matarlo!"
    n "-Grité zafándome de su agarre dirigiéndome de nuevo al titán-"
    n "No me encontraba en mis cabales, el deseo y objetivo de matar a ese titán recorría mi mente y se transmitía a todo mi cuerpo."
    n "Las ansias de despedazarlo y cortarlo en pedazos con mis cuchillas me hacían explotar y correr más rápido, quería matarlo con mis propias manos."
    n "Quería verlo gritar y evaporarse, quería hacerle pagar por lo que había hecho."
    n "Estaba furiosa, sentía mis venas arder y mi garganta quemarse. Mis ojos lo fulminaban con la mirada mortal que le mostraba."
    n "Mis manos sostenían con fuerza las cuchillas listas para rebanar carne. Apretaba mis dientes provocando crujidos."
    show bosquebl
    with fade
    n "La velocidad con la que iba hacía crujir, romper y levantar pedazos de los árboles con cada pisada."
    n "Las hojas crujían cuando pasaba cerca y algunas caían del impacto del aire. Volaba con ayuda del gas y los cables."
    scene img10
    show titanassei
    with fade
    play sound "Mikasalimit.mp3"
    play sound "stuijm.mp3"
    with hpunch
    n "Una vez cerca del titán, la furia volvió a dominar mi cuerpo y, sin pensarlo dos veces, lo ataqué de la misma forma que los otros dos."
    play sound "stuijm.mp3"
    n "Pero fue diferente: con cada corte gritaba de desesperación y enojo, los cortes los hacía con agresividad y violencia."
    n "Eran cortes tan profundos que llegaba a los huesos, tajaban todo su cuerpo."
    n "Los gritos del titán me provocaban más ganas de herirle y hacerle pagar por lo que había hecho."
    play sound "stuijm.mp3"
    with hpunch
    n "Traté de calmar toda mi ira cortando su cabeza y cuello, seguido de una fuente de sangre que manchaba toda mi ropa y rostro."
    n "Aterricé, dejándome caer de rodillas sobre el pasto. La tensión en mis músculos me impedía moverme."
    n "La agitación de todo mi cuerpo me impedía respirar bien, el cansancio de mi cuerpo y mi mente estaban al límite."
    with pixellate
    show evaop
    with fade
    n "En cualquier momento caería rendida, pero lo había conseguido. Con dificultad levanté la mirada para ver al titán evaporándose frente a mí."
    with pixellate
    show lili
    with fade
    n "Solté una risilla maliciosa y victoriosa, veía al titán con la mirada más fulminadora y dominante de todas."
    play music "WYS - Snowman.mp3"
    a "¡Mikasa!"
    n "-Sentí que mi cuerpo era levantado cuidadosamente-"
    a "¿Estás bien?"
    n "-Preguntó mi amigo mientras colocaba uno de mis brazos detrás de su cabeza y sostenía mi cadera como apoyo para empezar a caminar-"
    m "Sí..."
    n "-Solté dando un suspiro y recobrando el aliento-"
    n "-Al llegar vi que Levi era tratado por Jean, no dejaba de hacer muecas de dolor y su espalda no dejaba de sangrar-"
    n "Mis ojos se clavaron en él, la desesperación y miedo volvió a apoderarse de mi cuerpo, que ya había recuperado los cinco sentidos."
    with pixellate
    show bosu
    with dissolve
    show Armin serio c
    with dissolve
    m "¡Armin, debes buscar al comandante Erwin, rápido!"
    n "-Le dije sin despegar mi mirada de Levi-"
    show Armin disgustado c
    with dissolve
    a "Pero Mikasa... yo no puedo hacerlo."
    show Armin disgustado cce
    with dissolve
    n "-Lo miré preocupada-"
    show Armin serio c
    with dissolve
    je"¡Yo iré a buscarlos!"
    n "-Dijo Jean poniéndose de pie y entregándome los materiales de curación-"
    je"¡Pero tú cuida y trata al capitán, Mikasa!"
    n "-Me dijo subiendo a su caballo y partiendo-"
    n "Tan solo asentí y me dirigí a Levi."
    scene img10b
    show herido2
    with dissolve
    n "Tomé una de sus manos para que me mirara; lo hizo mirándome con dolor y sufrimiento. Sin esperar comencé a tratarlo con cuidado."
    n "Limpiando su herida y quitando parte de su ropa dañada, se quejaba del dolor y apretaba mi mano con fuerza cerrando sus ojos."
    n "Le acariciaba su rostro con delicadeza pidiéndole que me mirase."
    n "Quité la parte de arriba de sus ropas dejando el torso desnudo, la parte de enfrente también estaba herida."
    n "Con el pañuelo comencé a limpiar sus heridas mientras nos mirábamos a los ojos."
    n "Sus ojos mostraban dolor y sufrimiento, estaban hundidos. Su mirada era diferente a las otras, era una mirada abierta."
    n "Era una mirada fácil de entender, pero al mismo tiempo, de agradecimiento, asombro y amor."
    n "Sus ojos penetraban en los míos y un choque de sentimientos crecían en mí de nuevo."
    l "También estás sucia."
    n "-Pronunció sin dejar de mirarme-"
    m "No es igual a usted, capitán."
    n "-Contesté con preocupación mientras seguía limpiando sus heridas-"
    show lili
    with fade
    play music "miss the way u played.mp3"
    show screen modal_example2
    n "=EREN="
    show screen style_prefix_screen1
    scene bosque6
    with dissolve
    n "..."
    n "El día había comenzado de la peor manera."
    call screen style_prefix_screen1
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    with flashbulb
    show herido2
    n "Esa escena me molestaba, me quemaba por dentro; no soportaba ver a Mikasa tan gentil y cercana al capitán."
    n "Sus acciones me molestaban y lo que estaba haciendo era incoherente."
    scene bosque6
    with fade
    show Armin serio c
    with fade
    n "Solté bufidos de molestia y cambié mi vista y dirección a mi amigo rubio, quien vigilaba el lugar asustado."
    e "Si tienes miedo no puedes pelear."
    n "-Le dije directamente con fastidio-"
    n "Solo volteó a verme frunciendo el ceño, cosa que me extrañó mucho ya que él no era así conmigo."
    e "¿Qué? ¿Acaso te molesta que te diga la verdad, Armin?"
    n "-Le pregunté de golpe, odiaba que la gente me viera como el malo del cuento-"
    a "No."
    n "-Contestó secamente-"
    e "¿Entonces?"
    n "-Le dije molesto al ver que no me había contestado nada y tampoco me miraba-"
    show Armin enojado sc
    with dissolve
    a "Me molesta tu actitud, la forma en que te diriges a una persona y la juzgas sin saber por lo que ha pasado."
    show Armin enojado cce
    with dissolve
    n "-Mencionó mirándome con odio y regresando su vista al camino-"
    e "¿Estás diciendo que yo juzgo antes de conocer?"
    n "-Su comentario me había molestado-"
    show Armin hablando c
    with dissolve
    a "¡Sí! De todo te quejas, Eren. Si no salen las cosas como quieres, pones excusas tontas."
    a "No quieres ser protegido, pero tampoco eres fuerte. Juzgas a débiles pero no sabes por qué lo somos."
    show Armin serio c
    with dissolve
    n "-Se puso de pie y se dirigió a mí colocándose de frente-"
    show Armin enojado sc
    with dissolve
    a "¡Dices que no te importan ciertas personas, pero solo estás sobre ellas!"
    show Armin enojado cce
    with dissolve
    n "-Mencionó molesto, mirándome con odio-"
    n "Armin jamás había sido así conmigo, él siempre me brindaba consejos y cuando me equivocaba me corregía con tranquilidad y paciencia."
    n "Pero esta vez me regañaba hablando de forma directa e hiriente."
    n "Suponía que lo hacía por la tensión del momento y porque le molestaba que le dijera que era débil aun cuando él ya lo sabía."
    show Armin enojado sc
    with dissolve
    a "¡Deja de ser tan arrogante e infantil, Eren!"
    show Armin enojado cce
    n "-Términó con la peor palabra de todas-"
    e "¡¿Tú también dices que soy infantil?!"
    n "-Exclamé con ira-"
    e "¡Pensé que solo era Mikasa, pero veo que hasta mi amigo piensa eso!"
    n "-Me dolían de cierta forma sus palabras, pero no quería demostrarlo, ellos no podían decidir sobre mi vida, no más."
    show Armin enojado sc
    with dissolve
    a "¡Mikasa siempre se ha preocupado por ti porque te considera su hermano."
    show Armin enojado cce
    with dissolve
    a "Eres lo único que le queda en este mundo y tú la tratas como si fuera la peor persona!"
    show Armin serio c
    with dissolve
    n "-Dijo en un tono serio y molesto evitando mi mirada-"
    e "¡Ella no es mi hermana, solo la adoptamos para que no viviera sola."
    e "Además, es hartante tenerla siempre a tu lado, ¡no te sientes libre ni tienes espacio personal!"
    n "-Exclamé molesto porque nadie sabía cómo me sentía-"
    show Armin enojado sc
    with dissolve
    a "¡Mikasa lo hacía para protegerte!"
    show Armin enojado cce
    with dissolve
    a "No sabes cuántos sacrificios tuvo que hacer con tal de estar a tu lado y protegerte todo el tiempo."
    show Armin hablando c
    with dissolve
    a "Para ella lo eras todo, Eren, pero tus actitudes..."
    a "... y faltas de respeto la hirieron de una manera que decidió alejarse de ti y solo le quedó confiar en que puedes tú solo."
    show Armin disgustado c
    with dissolve
    n "-Sus palabras bombardeaban mi mente-"
    e "¿Meterme en un juicio es parte de protegerme?"
    e "¿Que siempre esté a mi lado, incluso en la noche, es para protegerme?"
    e "¿Acaso no confía en que puedo hacerlo solo?"
    n "-Grité con desesperación al pensar que yo era el malo y ella la víctima-"
    show Armin enojado sc
    with dissolve
    a "¡Eren!"
    with hpunch
    n "-Me tomó de los brazos con brusquedad-"
    a "¡Mikasa solo está cumpliendo con la promesa que le hizo a tu madre!"
    n "-Quedé boquiabierto con sus palabras-"
    a "Desde el día del juicio Mikasa sabía que tenía que protegerte más por el hecho de que la policía militar te buscaba para matarte."
    a "Quería cerciorarse de que no fueras a cometer una locura convertido en titán."
    a "¡Ella solo quería proteger a la persona que le dio una segunda oportunidad de vivir!"
    a "¡La persona que le enseño a luchar y jamás rendirse, la que sería el único lugar al que podría regresar!"
    show Armin serio c
    with dissolve
    n "-Términó con un nudo en la garganta-"
    n "Me quedé asombrado ante lo que acaba de escuchar."
    n "Armin sabía todo eso mientras que yo no sabía nada."
    n "No creía las palabras de mi amigo al decirme que lo hacía por ser su familia, por una promesa, por mi bienestar."
    show Armin disgustado c
    with dissolve
    a "Pero todo eso se acabó, Eren... la perdiste."
    show Armin disgustado cce
    with dissolve
    n "-Término mirándome a los ojos con recelo y tristeza-"
    n "Tenía razón, la había perdido."
    n "La hermana que tenía ya no estaba, yo le había quitado ese título."
    n "Se había ido de mi lado y comenzó a hacer su vida con nuevas personas, pero no podía soportarlo."
    n "Ella y Armin se habían vuelto más cercanos que antes."
    n "Ella se juntaba con las chicas de su escuadrón y comenzaba a tener acercamiento con el capitán Levi."
    n "Eso sí me molestaba: que mirara al capitán de diferente manera a los otros, lo miraba como antes ella me miraba a mí."
    n "Ella cambiaba estando con él, se notaba que ella daría su vida para protegerlo."
    n "Pero... ¿Por qué?."
    n "¿En qué momento Mikasa se había preocupado por el hombre que me había golpeado en el juicio?"
    n "Mi cuerpo ardía de ira y furia, no soportaba que el capitán la mirara también de esa forma, ella sólo era mía."
    show Armin enojado cce
    with dissolve
    e "¿Por qué siempre está con el capitán?"
    n "-Intenté buscar una respuesta-"
    with hpunch
    show Armin enojado sc
    with dissolve
    a "¡Porque él no la rechaza!"
    n "-Sentí una punzada en el pecho-"
    show Armin hablando c
    with dissolve
    a "Él si la entiende y la apoya."
    a "Le muestra sus fortalezas, corrige sus defectos y los pone a prueba."
    show Armin feliz c
    with dissolve
    a "Él la escucha cuando tiene problemas y la ayuda para volverse fuerte."
    n "-Terminó con aura de alegría por ella-"
    a "Él sí la respeta y reconoce como soldado y persona, él sí sabe que ella es humana."
    n "-Acabó mirándome fijamente a los ojos-"
    show Armin disgustado cce
    with dissolve
    e "No me gusta verlos juntos."
    n "-Solté por fin con mi cuerpo en llamas-"
    a "Pues tú ya no puedes meterte en su vida porque no quieres saber nada de ella."
    n "-Sentí que una flecha atravesaba mi cuerpo-"
    show Armin enojado sc
    with dissolve
    with hpunch
    a "¡La perdiste y todo fue tu culpa!"
    n "-Otra flecha se clavó más profunda-"
    a "Tienes que aceptar tu error y dejar que ella sea feliz."
    show Armin serio c
    with dissolve
    n "-La tercera flecha se clavó en mi corazón-"
    a "Eren..."
    n "-Pronunció mi nombre de forma atroz y terrorífica-"
    show Armin tt c
    with dissolve
    a "¡Ni se te ocurra arruinar la vida de Mikasa por tercera vez!"
    n "-Su voz amenazadora retumbaba en mi cabeza y provocó que me quedara callado sin más que decir-"
    hide Armin tt c
    with dissolve
    n "Armin se alejó de mí para dirigirse al comandante Erwin, quien había llegado gracias a Jean."
    n "Yo me quedé cabizbajo, analizando todo lo que acaba de pasar. Empezaba a darme cuenta de lo que había perdido."
    n "Sentía que Armin tenía razón en lo que había dicho."
    n "Yo era el culpable de todo."
    n "Yo la había alejado de mi vida por puro capricho cuando en realidad la necesitaba a mi lado."
    n "Pero todo eso se había acabado por mi culpa."
    n "Ella ahora tenía nuevos amigos, tenía a un nuevo hermano, tenía a alguien que la miraba de forma especial y yo ya no estaba en su vida."
    show Errwin normal cba
    with dissolve
    r "¡Vámonos Jaeger!"
    r "¡Regresaremos a los muros!"
    show Erwin normal c
    with dissolve
    n "-Me gritó el comandante Erwin-"
    hide Erwin normal c
    hide Errwin normal cba
    with dissolve
    n "Me subí a mi caballo aún con la mente pérdida mientras seguía a mi escuadrón."
    n "Divisé una de las carretas vacías y encontré a Mikasa abrazando al capitán Levi."
    show Mikasa feliz c
    with dissolve
    m "Es mejor que descanses Levi... yo te aviso cuando lleguemos a los muros."
    n "-Le habló con esa hermosa voz tan característica de ella que ya no iba dirigida a mí-"
    hide Mikasa feliz c
    with dissolve
    show Levi sonrojado c
    with dissolve
    l "¡Tch!"
    n "-Oí que se quejó el capitán mientras se acomodaba en los brazos de ella-"
    l "Gracias..."
    hide Levi sonrojado c
    with dissolve
    n "-Pronunció antes de caer dormido-"
    n "Jamás había visto al capitán ser tan abierto con nadie."
    n "Armin tenía razón."
    n "Él y Mikasa tenían muchas cosas en común, y quisiera o tendría que aceptarlo por mucho que me negase."
    n "El camino fue tranquilo y solo algunos titanes se acercaron, pero no hubo bajas."
    show lili
    with dissolve
    show text "{size=+25}{color=#FFFFFF}Cada vez que podía fijaba mi mirada en aquella carreta, mirando a ambas personas dentro de ella, dormidas, tomadas de las manos y abrazadas.{/color}{/size}" at truecenter
    with dissolve
    pause 6
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}El cuerpo me ardía y me daban ganas de llorar y gritar, pero debía resignarme.{/color}{/size}" at truecenter
    with dissolve
    pause 4
    hide text
    stop music
    show pueblo
    with fade
    n "Una vez que llegamos a los muros la gente nos recibió entre gritos y aplausos."
    n "Habíamos conseguido nuestro objetivo aunque hubiésemos perdido gente."
    show legion
    with fade
    n "Nos dirigimos al cuartel y ahí vi por última vez a Mikasa."
    n "Se dirigía a la enfermería. Con ayuda de Hange y el comandante Erwin cargaban a Levi para no lastimarlo."
    n "Fue la última en entrar, pero antes me dirigió una última mirada."
    show Mikasa enojada c
    with dissolve
    show screen style_prefix_screen3
    n "Una mirada llena de rencor y tristeza. Finalmente cerró la puerta y, con ello, el lazo que había entre nosotros."
    hide Mikasa enojada c
    with dissolve
    call screen style_prefix_screen3
    e "..."
    call screen modal_example2
    scene lili
    show text "{size=+25}{color=#FFFFFF}Capitulo 5{/color}{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}FIN{/color}{/size}" at truecenter
    with dissolve
    pause 0
    hide text
    with dissolve
    $persistent.cap6 = True
    return



label capitulo6:
    play music "Most Beautiful.mp3"
    show text "{size=+25}{color=#FFFFFF}Capítulo 6{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}¿Amor?{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    show screen quick_menu
    with dissolve
    show lili
    with fade
    show habile
    with fade
    n "El ambiente era tranquilo después de la desesperación por la que había pasado."
    n "Mi cuerpo y mente se habían calmado y disfrutaba de la tranquilidad que se respiraba en aquella habitación."
    n "Era una de las pocas habitaciones que tenía la enfermería en la Legión."
    show domile
    with fade
    n "Inhalaba tranquilamente ese aire mientras cerraba por momentos mis ojos y relajaba mi cuerpo en aquella silla de madera pegada a la cama."
    n "Después desviaba mi mirada a la persona que descansaba plácidamente en aquella cama."
    n "Con su típico semblante serio pero su cara más relajada y tranquila."
    n "El capitán Levi se encontraba acostado sobre la cama con la parte superior de su cuerpo vendada."
    n "Otra venda más rodeaba su cabeza y tenía un pequeño parche en su pómulo derecho, esto a causa de las heridas que había sufrido en la última expedición."
    n "Su espalda había sido rasgada por completo al chocar con el tronco de un árbol."
    n "Había recibido un fuerte golpe en la cabeza y, por efecto de la caída, se lastimó parte del pecho y su mejilla."
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    show heri
    with flashbulb
    n "Solté un suspiro al recordar la escena."
    n "El sentimiento de pánico que había tenido al verlo herido perdiendo sangre no había desaparecido del todo."
    n "A pesar de que me encontraba tranquila, aún estaba preocupada por él."
    scene img11
    show domile
    with fade
    n "Pero verlo ahí, recostado sobre la cama, respirando tranquila y pausadamente, me hacía recobrar el aliento y preocuparme menos."
    n "Llevaba ya 3 horas en ese lugar y, sin darme cuenta, ya estaba oscureciendo."
    n "Me levanté a encender unas cuántas velas para alumbrar la habitación y mientras las colocaba en el mejor lugar..."
    play sound "quejido.mp3"
    scene habile
    with fade
    n "Escuché a Levi moverse en la cama, escuchando sus quejidos de dolor con su típico tono molesto."
    show Levi enojado s
    with dissolve
    play sound "espmika.mp3"
    m "¡Espera!"
    m "No te levantes, vas a lastimarte."
    n "-Le dije mientras le ayudaba a sentarse en la cama colocando las almohadas detrás de su espalda-"
    play sound "tch.mp3"
    l "¡Tch!"
    $contador = 0
    python:
        LeviAmizade4 += 60
    call chamarBarraMais4(LeviAmizade4)
    with dissolve
    n "-Se quejó mientras se acomodaba-"
    play sound "tch2.mp3"
    l "Qué molesto."
    n "-Mencionó mientras inspeccionaba su cuerpo-"
    show Levi normal2 s
    with dissolve
    m "Su espalda es lo más delicado. Por favor, tenga cuidado, capitán."
    n "-Mencioné mirándolo preocupada-"
    n "Me miró fijamente un momento provocando que un leve escalofrío recorriese mi cuerpo."
    n "Después volvió a desviar su mirada a sus partes vendadas."
    show Levi preocupado s
    with dissolve
    n "Resopló con molestia mientras acariciaba sus heridas aún apretando los dientes y cerrando sus ojos con fuerza por el dolor."
    n "Verlo me parecía tierno. Sin duda llevaba toda la tarde esperando verlo despierto nuevamente aun si así fuera con su típica cara seria y ceño fruncido."
    n "Acerqué un poco más mi silla a la cama, quedando casi frente a él, y volteó a verme sorprendido y extrañado."
    show Levi suave2 s
    with dissolve
    play sound "bien.mp3"
    m "Me alegra mucho saber que está bien..."
    n "-Mencioné con voz temblorosa mientras bajaba la mirada-"
    l "¿Ackerman?"
    n "Sus palabras provocaron en mí otro escalofrío más, levanté mi vista para verlo fijamente analizando lo que quería decirme con solo verme."
    show Levi sonrojado s
    with dissolve
    n "Por impulso tomé sus manos con delicadeza y las entrelacé con las mías."
    n "Agaché mi cabeza nuevamente intentando evitar soltar aquellas lágrimas que rondaban por mis ojos amenazando con salir."
    n "El sentimiento de ese momento era inexplicable, no entendía qué estaba haciendo, pero no quería dejar de hacerlo."
    n "Quería demostrarle mi preocupación por él, quería demostrarle que realmente me importaba todo lo que le pasaba y sufría."
    n "Quería demostrarle que me volvía débil por su culpa, quería demostrarle que era capaz de hacer miles de cosas por él sin ningún motivo."
    show Levi tranquilo s
    with dissolve
    play sound "Mikasadelevi.mp3"
    l "Mikasa..."
    n "-Pronunció mi nombre con una voz suave y tranquila mientras apretaba con fuerza mis manos-"
    show Levi suave2 s
    with dissolve
    l "¿Por qué... te preocupas por mí... de esa manera...?"
    menu:
        n "-Preguntó con un tono de voz que jamás había escuchado, uno de culpa quizás-"

        "No lo sé.":
            python:
                LeviAmizade4 += 5
            call chamarBarraMais4(LeviAmizade4)
            n "-Contesté sin mentir aún con mi mirada baja *no sabía porque lo estaba haciendo*-"
            play sound "disculpe.mp3"
            m "Lo siento..."
            hide screen barraAmizade4
            with dissolve
            n "-Dije soltándome del agarre de sus manos y escondiendo mi rostro en la bufanda-"
            m "No era mi intención."
            n "-Dije con voz apenas audible por la bufanda que cubría casi por completo mi cara-"
            jump gh


        "Quiero demostrarle que...":
            python:
                LeviAmizade4 += 10
            call chamarBarraMais4(LeviAmizade4)
            show Levi normal2 s
            with dissolve
            n "Sentía su mirada fija en mí."
            n "Pero no me atrevía a levantar la vista, me daba vergüenza mirarle a los ojos."
            hide screen barraAmizade4
            with dissolve
            n "No tenía una respuesta clara y mis acciones tampoco eran las mejores, aquellas sensaciones siempre regresaban cuando estaba cerca de él."
            n "Solo él hacía que me sintiera fatal y que me convirtiera en otra persona."
            n "Solo él provocaba que mi respiración se agitara y mi corazón palpitase más rápido de lo normal."
            n "Hacía que mis mejillas se calentaran, que las cosquillas en mi estómago se hicieran presentes y que no pudiera miirarle a los ojos por vergüenza."
            play sound "disculpe.mp3"
            m "Lo siento..."
            n "-Mencioné cortando lo que quería decir-"
            m "..."
            m "Yo..."
            n "-Dije soltándome del agarre de sus manos y escondiendo mi rostro en la bufanda-"
            m "No era mi intención."
            n "-Dije con voz apenas audible por la bufanda que cubría casi por completo mi cara-"
            jump gh


label gh:
    hide Levi suave2 s
    with dissolve
    play music "As the Day Ends.mp3"
    scene img11b
    show alejes1
    with fade
    play sound "Mikasadelevi.mp3"
    l "Mikasa..."
    n "-Pronunció por segunda vez mi nombre mientras volteaba a verme-"
    l "¿Por qué te alejas?"
    n "-Pronunció con una voz temblorosa y los ojos apagados-"
    n "Volteé a verlo sorprendida, levantando la cabeza para chocar con su penetrante mirada."
    n "El tono con el que lo había dicho, así como las palabras que había dicho, me habían asombrado."
    n "(¿De verdad hablaba en serio?)"
    n "(¿De verdad no quería que me alejara?)"
    m "¿No quieres que me aleje?"
    n "-Pregunté con miedo a la respuesta bajando la mirada-"
    with hpunch
    l "¡No!"
    n "-Contestó rápido mientras tomaba de nuevo una de mis manos-"
    with hpunch
    l "¡Quiero que... estés a mi lado...!"
    scene alejes2
    with dissolve
    n "-Mencionó en un tono más triste mientras acariciaba mi mano-"
    n "Con esas últimas palabras hizo que mi corazón palpitase a más no poder."
    n "Sentía que se me saldría del pecho. Mis mejillas de nuevo se calentaban y el nerviosismo se apoderaba de mí nuevamente."
    n "Sus ojos demostraban que hablaba en serio."
    n "Ese brillo especial me hacía pensar que disfrutaba del momento, pero también se sentía avergonzado."
    n "Su penetrante mirada chocaba con la mía en un concurso de ver quién aguantaba más."
    n "La cercanía entre nosotros era cada vez más corta."
    n "Podía percibir el suave aroma de su aliento fresco proveniente de su boca."
    n "El aire que soltaba golpeaba suavemente mi cara, el calor entre ambos se hacía presente."
    n "El choque de nuestros cuerpos nos hizo darnos cuenta de lo cerca que estábamos."
    n "Con suavidad, comenzó a acariciar mi mejilla."
    n "El roce de sus dedos me provocaban escalofríos de placer."
    n "Busqué la mano con la que me acariciaba mientras cerraba mis ojos y la apreté con suavidad."
    n "Me gustaba tomar su mano, era tan suave y cálida..."
    n "Recogió uno de mis mechones de cabello que había cerca de mi cara y lo pasó detrás de mi oreja con suavidad mientras esbozaba una pequeña sonrisa."
    n "Un sentimiento de felicidad inundaba mi cuerpo mientras le devolvía una media sonrisa."
    n "Sus palabras retumbaban fuertemente en mi cabeza."
    n "Una extraña alegría y sensación se apoderaba de mi cuerpo en ese momento."
    n "Una sensación inexplicable tomaba riendas de mi mente y solo me hacía pensar en él."
    n "Quería estar a su lado, quería estar siempre cerca de él."
    play music "musica normal.mp3"
    play sound "puerta.mp3"
    with hpunch
    scene habile
    with dissolve
    n "El ruido de la puerta me hizo retroceder de golpe y algo apenada, soltándome del agarre de sus manos."
    show Erwin normal s
    with dissolve
    n "Dirigí mi mirada a las personas que habían entrado."
    hide Erwin normal
    with dissolve
    show Hange alegre s
    with dissolve
    z "¡Levi!"
    n "-Gritó Hange corriendo y abrazando a Levi mientras se aguantaba las ganas de llorar-"
    z "¡Me alegro de que estés bien!"
    n "-Dijo apretándolo más-"
    hide Hange alegre s
    with dissolve
    show Levi enojado sbe
    with dissolve
    l "¡Cuatro ojos, me lastimas!"
    show Levi enojado s
    with dissolve
    n "-Se quejó mientras hacía muecas de dolor-"
    l "¡Aléjate!"
    hide Levi enojado s
    with dissolve
    show Hange normal s
    with dissolve
    n "-Le ordenó algo incómodo-"
    hide Hange normal s
    with dissolve
    show Erwin incomodo1 s
    with dissolve
    r "¡Nos diste un gran susto, Levi!"
    show Errwin normal sba
    with dissolve
    r "Me alegro de que estés bien..."
    show Erwim feliz s
    with dissolve
    n "-Pronunció el comandante Erwin mirando con alivio a Levi-"
    r "¡Gracias por cuidar de él, Mikasa!"
    n "-Me agradeció con una sincera sonrisa-"
    m "No es nada..."
    n "-Contesté algo apenada y con nerviosismo-"
    hide Erwim feliz s
    hide Erwin incomodo1 s
    hide Errwin normal sba
    with dissolve
    show Hange seria s
    with dissolve
    n "Hange se posicionó a un lado del comandante Erwin, cruzó sus brazos y cambió su semblante a uno más serio."
    n "Aquella expresión de ella me hizo entender que ahora irían a algo más serio."
    n "El comandante soltó un suspiro y comenzó a hablar."
    hide Hange seria s
    with dissolve
    show Errwin normal sba
    with dissolve
    r "La expedición fue un éxito."
    r "Se logró cumplir el objetivo principal y los materiales ya están siendo repartidos entre quienes los necesitan."
    show Erwin normal s
    with dissolve
    n "-Habló seriamente con algo de orgullo por no haber fallado esta vez-"
    show Erwin incomodo1 s
    with dissolve
    r "Sin embargo... perdimos a muchos soldados..."
    r "Y las razones de su muerte son trágicas e inexplicables, lo que hace que sus muertes sean más dolorosas de lo normal."
    show Erwin incomodo2 s
    with dissolve
    n "-Resopló mientras apretaba los puños-"
    hide Erwin incomodo2 s
    hide Erwin incomodo1 s
    hide Erwin normal s
    hide Errwin normal sba
    with dissolve
    show Hange preocupada s
    with dissolve
    z "Erwin..."
    n "-Pronunció con suavidad Hange colocando su mano sobre su hombro y mirándolo con preocupación-"
    hide Hange preocupada s
    with dissolve
    show Erwin incomodo2 s
    with dissolve
    n "Tan solo los miré."
    n "El comandante estaba actuando de la misma forma en que yo lo había hecho cuando me enteré de ello."
    n "Solo que él se estaba conteniendo, después de todo, era humano, debía demostrar lo que sentía."
    n "El sentimiento de culpa y tristeza inundaron la habitación haciendo el ambiente tenso y pesado."
    n "El comandante luchaba internamente ya que debía de mantener esa postura firme y digna de un comandante para no manchar su nombre."
    n "Pero le resultaba difícil. También quería llorar y golpear todo por cada baja que había habido en las expediciones."
    show Erwin normal s
    with dissolve
    m "Comandante..."
    m "Existe una especie que no conocemos de esos monstruos..."
    n "-Le dije mientras formulaba mis argumentos-"
    m "Se trata de una mezcla entre excéntricos e inteligentes ya que son capaces de razonar, actúan con gran habilidad y son muy rápidos y agresivos."
    hide Erwin normal s
    with dissolve
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    scene titih
    with flashbulb
    n "-Mencioné mientras la horrible imagen de aquellos titanes se dibujaba en mi cabeza causándome pánico-"
    show habile
    with fade
    show Hange hablando s
    with dissolve
    play music "As the Day Ends.mp3"
    z "Una especie no identificada..."
    show Hange normal s
    with dissolve
    n "-Término por concluir Hange tomando con sus manos su mentón-"
    m "Así es."
    n "-Confirmé su conclusión dando un suspiro-"
    show Hange hablando s
    with dissolve
    z "Sin embargo solo tú pudiste hacerles frente, ¿no es así?"
    show Hange seria s
    with dissolve
    n "-Me miró fijamente retomando su postura-"
    m "Eso creo... solo actúe por impulso para proteger a mis seres queridos..."
    m "No me había percatado de que solo yo había peleado contra ellos."
    n "-Confesé rascando mi cabeza por la confusión que estaba teniendo-"
    show Hange hablando s
    with dissolve
    z "Según Armin, tuviste muchos problemas para acabar con uno."
    show Hange seria s
    with dissolve
    n "-Habló Hange colocándose de rodillas frente a mí-"
    hide Hange seria s
    with dissolve
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    scene titanassei
    with flashbulb
    z "Sin embargo, el último titán lo venciste de una manera diferente... como más agresiva... ¿Por qué?"
    n "-Preguntó haciéndome sobresaltar por su cuestionamiento-"
    scene habile
    with fade
    show Hange seria s
    with dissolve
    n "La respuesta ni yo la sabía, opté por bajar mi mirada para pensar en algo."
    n "Estaba harta de esas bestias y luché por defender a las personas que quería, no encontraba otra respuesta."
    hide Hange seria s
    with dissolve
    show Erwin normal s
    with dissolve
    r "Arlert mencionó que actuaste así después de ver a Levi herido."
    r "¿Es ese el por qué de tu comportamiento y acciones, Ackerman?"
    n "-Preguntó ahora el comandante sobresaltándome nuevamente por la pregunta-"
    hide Erwin normal s
    with dissolve
    show Hange seria s
    with dissolve
    z "..."
    hide Hange seria s
    with dissolve
    show Levi normal2 s
    with dissolve
    l "..."
    n "Los miré sorprendida y algo asustada tras sentir la mirada de Levi detrás de mí."
    hide Levi normal2 s
    with dissolve
    show Erwin normal s
    with dissolve
    n "Tenía que responder algo, pero mis palabras no salían de mi boca."
    n "Es cierto que había actuado de inmediato tras ver aquello."
    n "Entonces, ¿por qué me daba miedo aceptarlo?"
    menu:


        "Sí...":
            python:
                LeviAmizade4 += 5
            call chamarBarraMais4(LeviAmizade4)
            n "-Contesté en cuanto pude pronunciar palabras-"
            hide screen barraAmizade4
            with dissolve
            hide Erwin normal s
            with dissolve
            n "Tanto Hange como el comandante se miraron un momento y fijaron su mirada en Levi, quien estaba de brazos cruzados con la mirada baja y los ojos cerrados."
            show Hange seria s
            with dissolve
            jump sd



        "Había hecho lo mismo con Armin, ¿cuál era la diferencia?":
            python:
                LeviAmizade4 += 4
            call chamarBarraMais4(LeviAmizade4)
            hide Erwin normal s
            with dissolve
            n "Tanto Hange como el comandante se miraron un momento pensativos."
            show Hange seria s
            with dissolve
            hide screen barraAmizade4
            with dissolve
            jump sd

label sd:
    hide Hange seria s
    with dissolve
    show Erwin normal1 s
    with dissolve
    r "Levi... ¿qué sucedió?"
    n "-Le preguntó el comandante sin cambiar su postura ni tono-"
    hide Erwin normal1 s
    with dissolve
    show Levi hablando s
    with dissolve
    l "El titán era ágil."
    l "Me confíe y por eso salí herido..."
    l "Eso es todo."
    show Levi normal2 s
    with dissolve
    n "-Recalcó abriendo los ojos y mirando al comandante con el ceño fruncido-"
    hide Levi normal2 s
    with dissolve
    show Erwin incomodo2 s
    with dissolve
    n "Él tan solo cerró un momento los ojos soltando un respiro."
    n "Tomó las hojas que llevaba cargando consigo y me las entregó; las recibí y volteé a verlo."
    show Erwin normal s
    with dissolve
    r "Necesito que me haga su reporte."
    r "Todo lo que vio, vivió y las características de esos Titanes."
    r "La información que nos dé nos será de gran importancia para la siguiente expedición dentro de 2 semanas, Ackerman."
    n "-Mencionó con un semblante serio y tenso-"
    r "Lo quiero mañana en mi oficia."
    n "-Exigió abriendo la puerta de la habitación-"
    play sound "puerta.mp3"
    r "Se lo encargo..."
    hide Erwin normal s
    hide Erwin incomodo2 s
    with dissolve
    show Hange normal s
    with dissolve
    n "-Terminó saliendo de la habitación seguido de Hange, quien nos miró un momento con una sonrisa pequeña antes de salir de la habitación-"
    hide Hange normal s
    with dissolve
    n "Tan solo solté un bufido."
    n "Ciertamente todos debíamos escribir nuestros reportes sobre cada expedición."
    n "Pero ahora tenía el doble de trabajo y no era muy paciente para escribir reportes."
    n "-Resoplé molesta colocando las hojas en una pequeña mesa-"
    show Levi tranquilo s
    with dissolve
    l "Parece que tienes mucho trabajo."
    n "-Mencionó en tono burlón-"
    m "¡Cállate!"
    n "-Le dije lanzándole una mirada fulminadora-"
    show Levi normal s
    with dissolve
    l "¿Faltándole el respeto a su capitán, Ackerman?"
    n "-Mencionó en tono sarcástico-"
    n "Fruncí el ceño de nuevo por su comentario, me molestaba."
    n "Solo estaba burlándose de mí, me hacía perder mi orgullo si le contestaba."
    n "Por lo que solo voté para cerrar mis ojos y cruzarme de brazos fijando mi mirada en el suelo mientras soltaba bufidos."
    show Levi suave2 s
    with dissolve
    l "Gracias..."
    n "-Le escuché decir apenas en voz audible-"
    n "Tan solo me asombré por sus palabras, pero no cambié mi postura."
    n "(¿Por qué ahora me estaba agradeciendo y antes se estaba burlando de mí?)"
    n "Él era raro, pero el tono de su voz demostraba que perdía su orgullo con lo que decía."
    m "¿Por qué?"
    n "-Pregunté sin cambiar mi postura, la duda me carcomía por dentro-"
    show Levi tranquilo s
    with dissolve
    l "Ya deberías de saber por qué..."
    n "-Mencionó algo molesto y apenado-"
    show Levi normal s
    with dissolve
    m "Un cadete no debería salvar a su capitán."
    n "-Le reproché dándole una sonrisa burlona-"
    m "Ni mucho menos hacerle perder su orgullo."
    n "-Mencioné sarcásticamente-"
    show Levi suave2 s
    with dissolve
    n "Volteó a verme con recelo, le había dado justo en su punto débil."
    n "Tan solo me reía por sus expresiones, esta vez había ganado y se la había regresado."
    show Levi sonrojado s
    with dissolve
    n "Sentí su mano tocar la mía, me sobresalté. Lo miré a los ojos, pero se encontraba demasiado cerca y el ritmo de mi corazón comenzó a acelerarse."
    m "¿Ca... capitán?"
    n "-Lo llamé con los nervios en punta avergonzada-"
    l "No..."
    n "-Mencionó acariciando de nuevo mi mejilla provocándome leves escalofríos-"
    l "Levi... quiero que me llames por mi nombre cuando estemos solos..."
    n "-Dijo acercándome más a su cuerpo-"
    m "Levi...."
    n "-Pronuncié su nombre con algo de vergüenza mientras sentía el roce de sus labios sobre los míos-"
    m "Yo..."
    hide Levi sonrojado s
    with dissolve
    scene img12
    show beso2
    with dissolve
    n "-Fui callada por el choque de nuestros labios y el sentimiento de pasión que comenzaba a surgir-"
    n "Sus labios suaves rozaban los míos con delicadeza y pasión."
    n "Las sensaciones en mi estómago despertaron de golpe, el mágico momento me hacía olvidarme de todo."
    n "Disfrutaba de sus manos acariciando mis mejillas, que me provocaban escalofríos de placer. Su brazo me acercaba más a él para sentir su calor."
    n "Su cuerpo pegado al mío era una de las mejores sensaciones que había sentido."
    n "Levanté mis brazos y los coloqué detrás de su nuca para acercarlo más a mi cara y aumentar la pasión del momento."
    scene habile
    with dissolve
    show Levi sonrojado s
    with dissolve
    n "La falta de aire nos hizo separarnos levemente pegando nuestras frentes con el otro, mirándonos a los ojos mientras recuperábamos el aliento."
    n "Nuestras respiraciones eran agitadas por la falta de aire, pero eso no importaba. El cruce de nuestras miradas penetrantes me provocaba felicidad."
    n "El brillo de sus ojos me decían infinidad de cosas, así como yo lo hacía con él."
    show Levi feliz s
    with dissolve
    n "Una pequeña risilla se escapó de nuestros labios mientras tomábamos de nuevo cierta distancia aún con nuestras manos unidas."
    m "Deberías descansar."
    n "-Le dije poniéndome de pie tomando las hojas de la mesa-"
    m "Descansa..."
    n "-Lo miré nuevamente brindándole una sonrisa-"
    l "¿Vendrás mañana?"
    n "-Preguntó mirándome con cierta ternura-"
    m "Tal vez."
    show Levi tranquilo s
    with dissolve
    n "-Le dije acercándome a él y depositando un beso en su plana frente, sintiendo cómo se estremecía con mis labios sobre su piel-"
    show Levi sonrojado s
    with dissolve
    m "Hasta mañana, Levi..."
    play sound "puerta.mp3"
    n "-Susurré mientras caminaba hacia la salida para finalmente cerrar la puerta-"
    scene pasillo3
    with fade
    n "Me quedé recargada sobre la puerta y con una de mis manos me tapé la cara."
    n "Estaba avergonzada al límite, los latidos de mi corazón estaban muy acelerados y el calor de mis mejillas era alto."
    n "Podía asegurar que el color rojo también sería visible para cualquiera."
    n "(¿Qué acababa de hacer?)"
    n "Aquella pregunta rondaba por mi cabeza sin poder creer lo que había hecho. Comencé a caminar por el pasillo en dirección a mi habitación."
    m "Lo mejor será escribir el reporte de una vez."
    n "-Me dije a mi misma-"
    m "Servirá también para calmarme."
    n "-Me dije dando un suspiro y acelerando el paso-"
    scene pasillo2
    with fade
    play music "Most Beautiful.mp3"
    n "Caminaba con rapidez por el pasillo para evitar tener contacto con la gente."
    n "Al ser la hora de cenar, todos deberían de encontrarse en el comedor."
    with hpunch
    n "O eso creía hasta que choqué con alguien y caí al piso de culada tirando todas las hojas al suelo."
    show Annie normal s
    with dissolve
    $contador = 0
    python:
        AnnieAmizade5 += 33
    call chamarBarraMais5(AnnieAmizade5)
    with dissolve
    an"¿Mikasa?"
    n "-La voz de alguien reconocible me hizo alzar la mirada mientras sobaba mi cabeza-"
    an"¡Lo siento!"
    n "-Mencionó recogiendo los papeles tirados para después darme su mano-"
    n "Tomé su mano con molestia y la miré con el ceño fruncido."
    n "Me entregó las hojas y las acepté de mala gana sin despegar mi mirada de ella, quien se encontraba cabizbaja."
    m "¿Se puede saber qué haces aquí, Annie?"
    n "-Le pregunté aprovechando el percance que habíamos tenido-"
    an"Tengo que hablar con el comandante de la Legión."
    n "-Contestó mirándome fijamente-"
    show Annie triste s
    with dissolve
    an"No era mi intención chocar contigo, Mikasa..."
    n "-Dijo con un tono diferente al que siempre usaba-"
    n "La miré extrañada, estaba diferente, su actitud era distinta a la que yo conocía."
    n "Se veía vulnerable y débil. No era propio de ella disculparse, ni mucho menos ser amable con los demás y mucho menos conmigo."
    n "Solté un suspiro y me acerqué a ella. Aunque nos llevábamos mal... podría llegar a entenderla."
    n "En cierta manera creía que tanto ella como yo teníamos similitudes y nos parecíamos en varias cosas."
    show Annie normal s
    with dissolve
    m "¿Qué te sucede?"
    n "-Le pregunté de golpe mirándola fijamente-"
    m "Actúas extraño."
    n "-Mencioné mientras ella me miraba sorprendida-"
    an"¿Por qué te preocupa?"
    n "-Contestó de la misma forma que antes-"
    m "No lo sé."
    n "-Acepté sintiendo cómo mi orgullo desaparecía de nuevo-"
    menu:

        "¿Quiero saber por qué actúas así?":
            python:
                AnnieAmizade5 += 5
            call chamarBarraMais5(AnnieAmizade5)
            an"He decidido salir de las tropas reales para unirme a la Legión de Reconocimiento."
            hide screen barraAmizade5
            with dissolve
            n "-Mencionó mirándome a los ojos-"
            jump ss

        "Siento que nos parecemos mucho en eso...":
            python:
                AnnieAmizade5 += 7
            call chamarBarraMais5(AnnieAmizade5)
            n "-Le dije bajando la mirada-"
            an"Ya veo."
            hide screen barraAmizade5
            with dissolve
            n "-Mencionó ella aún con la mirada baja-"
            an"En cierta forma tienes razón."
            n "-Volteé a verla sorprendida-"
            m "¿Entonces?"
            n "-Volví a preguntar al ver que ya había más confianza y el ambiente ya no era tenso-"
            an"He decidido salir de las tropas reales para unirme a la Legión de Reconocimiento."
            n "-Mencionó mirándome a los ojos-"
            jump ss

label ss:
    m "¿Por qué?"
    n "-Pregunté asombrada ante lo que acababa de decir-"
    m "¡Creí que querías una vida tranquila y no volver a ver titanes!"
    n "-Exclamé aún sin poder creerlo-"
    show Annie preocupada s
    with dissolve
    an"Sí... pero desde ese día tengo remordimientos que me impiden seguir adelante."
    show Annie triste s
    with dissolve
    n "-Comenzó a hablar con algo de tristeza-"
    an"Gritos de gente pidiéndome ayuda para que los salvará de los titanes..."
    an"El sonido de los huesos rompiéndose al ser mordidos por esas bestias, los cuerpos partidos de mis compañeros...."
    n "-Tomó aire con algo de inquietud-"
    show Annie preocupada s
    with dissolve
    an"Todo eso aparece en mis sueños."
    an"¡No puedo vivir con ese remordimiento!"
    n "-Exclamó agitada con cara de culpa-"
    m "Annie..."
    n "-Pronuncié su nombre acercándome a ella y acariciando su espalda-"
    m "Entiendo ese sentimiento, pero ¿de verdad crees que entrando a la Legión de Reconocimiento podrás vivir tranquila?"
    n "-No entendía bien cuál era su objetivo-"
    show Annie hablando s
    with dissolve
    an"Quizás..."
    show Annie normal s
    with dissolve
    n "-Contestó recuperando su postura-"
    show Annie hablando s
    with dissolve
    an"Por lo menos podré estar presente y ayudaré a mis compañeros a diferencia de solo verlos de lejos y no poder hacer nada."
    an"Me equivoqué en elegir una vida tranquila, en este mundo nunca hay tranquilidad."
    show Annie normal s
    with dissolve
    m "Tienes razón."
    m "Esperó que la decisión que tomes te ayude a estar más tranquila."
    n "-Acepté. Odiaba ver así a la gente, me veía a mí misma en ella-"
    show Annie feliz s
    with dissolve
    an"Gracias, Mikasa."
    $contador = 0
    python:
        AnnieAmizade5 += 36
    call chamarBarraMais5(AnnieAmizade5)
    n "-Me brindó una pequeña sonrisa-"
    an"Espero que ya no peleemos más, eres una gran persona."
    n "-Dijo mientras caminaba por el pasillo en dirección a la oficina del comandante-"
    hide screen barraAmizade5
    with dissolve
    n "La miré irse de lejos a paso lento."
    hide Annie feliz s
    with dissolve
    n "Hablar con ella no había sido tan incómodo, de hecho, era la primera vez que hablaba con ella de esa forma."
    n "Y aun siendo la primera vez, fue directa y abierta conmigo. Al igual que ella, yo también había cambiado."
    n "En parte era agradable conocer gente nueva y hablar con esas personas para conocerlas mejor."
    n "El sonido del reloj llamó mi atención y volteé a verlo por curiosidad para ver la hora."
    with hpunch
    stop music
    m "¡Las nueve!"
    n "-Grité asustada al ver que ya era tarde-"
    m "¡Y aún no escribo el maldito reporte!"
    n "-Me maldije a mí misma y comencé a caminar más rápido en dirección a mi habitación-"
    n "El tiempo no estaba de mi lado, sin duda."
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    scene beso2
    with flashbulb
    n "Aunque había sido un buen día, el recuerdo del beso con Levi provocó que me sonrojara."
    show pasillo5
    with fade
    n "También fue agradable hablar con Annie, con quien creía que nunca formaría algún tipo de lazo."
    n "Caminaba rápidamente."
    n "Recordaba que tenía doble trabajo por hacer."
    n "Tan solo me faltaba bajar las escaleras del último piso en el que estaba cuando vi a Armin sentado en una de las pilas de las torres mirando al cielo."
    scene torre
    with fade
    n "Me sorprendió verlo ahí, así que me acerqué a él."
    show Armin serio s
    with dissolve
    play music "Alone with Dream.mp3"
    m "¿Armin?"
    n "-Lo llamé acercándome un poco-"
    m "¿Qué haces aquí?"
    show Armin feliz s
    with dissolve
    a "¡Mikasa!"
    n "-Se sonrió al verme-"
    a "Nada en especial, solo quería estar solo."
    n "-Dijo volteando a ver el cielo nuevamente-"
    m "Entiendo... entonces te dejo."
    n "-Le dije dándole la espalda-"
    show Armin hablando s
    with dissolve
    with hpunch
    a "¡Espera!"
    show Armin serio s
    with dissolve
    n "-Me dijo tomando mi mano-"
    show Armin hablando s
    with dissolve
    a "Puedes quedarte si quieres."
    a "Me gustaría tener tu compañía."
    show Armin feliz s
    with dissolve
    n "-Confesó soltándome la mano-"
    $contador = 0
    python:
        ArminAmizade2 += 53
    call chamarBarraMais2(ArminAmizade2)
    with dissolve
    m "Está bien."
    n "-Dije soltando un suspiro y sentándome a su lado-"
    m "¡Este lugar es increíble, puedes ver todo lo que rodea a la Legión desde aquí!"
    n "-Dije asombrada ya que era la primera vez que estaba ahí-"
    show Armin alegre s
    with dissolve
    a "¡Sí! Así como el cielo."
    n "-Dijo sonriéndole al cielo inocentemente-"
    show Armin feliz s
    with dissolve
    show Armin serio s
    with dissolve
    n "Ver a Armin así, tranquilo, disfrutando de las pequeñas cosas y sonriendo como solo él sabía hacerlo..."
    n "Me hacía sentir tranquila y alegre por él, porque a pesar de cómo era nuestro mundo..."
    n "Armin podía llegar a ser un pequeño niño. Cuando él quería, se olvidaba de los problemas y lo hacía a su manera."
    n "Tan solo sonreía al verlo así, era de las pocas veces en que me recordaba al pequeño Armin que conocí cuando era una niña."
    n "Veía en él ese niño alegre que sólo hablaba de las maravillas del mundo de afuera, que jamás apagaba su sonrisa y sus juegos eran los más divertidos."
    n "Era alguien que entendía fácilmente las situaciones y te apoyaba en todo lo que pudiera."
    n "Su voz te tranquilizaba, te daba los mejores consejos y te hacía entender muchas cosas."
    n "Y no solo eso, poseía de una inteligencia que cualquiera desearía, ya que muchas veces esta le había ayudado a sobrevivir a él y a toda la Legión."
    n "Porque debía de admitir que él no era alguien fuerte físicamente pero mentalmente era el mejor de todos por mucho."
    n "Y, sobre todo, él era mi mejor amigo."
    n "Él, que me había apoyado en muchas ocasiones y que jamás tendría cómo pagárselo."
    n "Lo cuidaba con todo mi ser. Deseaba su protección, su felicidad, deseaba verlo cumplir sus sueños."
    n "Y, sobre todo, deseaba que jamás perdiera su sonrisa, esa que lo hacía único entre todos, una sonrisa que te tranquilizaba el alma."
    n "Pero esta vez él no sonreía, estaba serio viendo el cielo."
    n "Ni siquiera el brillo de sus ojos estaba presente. Noté que su cuerpo estaba tenso, lo conocía desde hacía mucho, algo le incomodaba."
    n "Algo lo alteraba, algo lo hacía sentir menos, y quería saber qué era."
    m "¿Armin?"
    n "-Lo llamé haciendo que volteara a verme-"
    menu:

        "¿Qué sucede?":
            python:
                ArminAmizade2 += 10
            call chamarBarraMais2(ArminAmizade2)
            with dissolve
            n "-Pregunté a mi amigo, quien no cambiaba su semblante. Mi corazón comenzó a acelerarse de preocupación-"
            show Armin disgustado s
            with dissolve
            a "Acabo de hablar con Annie."
            hide screen barraAmizade2
            with dissolve
            show Armin disgustado sce
            with dissolve
            n "-Comenzó a decir cabizbajo-"
            a "Me dijo que quiere entrar a la Legión para quitarse toda la culpa que lleva en su pecho."
            n "-Sus ojos, sin vida, miraban al suelo mientras su voz se quebraba poco a poco-"
            show Armin enojado s
            with dissolve
            a "¡No quiero que entre!"
            show Armin disgustado sce
            with dissolve
            n "-Lo dijo en forma de súplica levantando la voz-"
            show Armin hablando s
            with dissolve
            a "¡Yo quiero que se quede en las tropas de la realeza!"
            a "Quiero su seguridad...."
            show Armin disgustado sce
            with dissolve
            n "-No pudo terminar. Se le quebró la voz por completo y acurrucó sus piernas-"
            m "Armin..."
            n "-Pronuncié su nombre acercándome a él y abrazándolo por la espalda-"
            m "Annie ha tomado esa decisión, ella sabe por qué lo está haciendo. Conoce las consecuencias y aun así está dispuesta a enfrentarlo."
            n "-Lo miré a los ojos para intentar tranquilizarlo, no me gustaba verlo así-"
            show Armin tt s
            with dissolve
            a "Pero yo no quiero."
            a "Cuando me lo dijo, ella quería llorar y yo no supe qué hacer."
            show Armin disgustado sce
            with dissolve
            n "-Se acurrucó entre sus piernas y cerró los ojos intentando no llorar-"
            n "Jamás dudaría de las palabras de Armin."
            n "Él siempre era honesto y llegaba a descifrar con facilidad lo que sentía cada persona."
            n "Así que la actitud de Annie cuando chocamos debió ser porque acababa de hablar con Armin..."
            n "Estaba tan vulnerable que por eso había actuado así conmigo."
            n "Porque con Armin cualquiera sacaría todo de sí y se lo contaría con la verdad."
            m "¿Por qué te preocupas tanto por ella?"
            n "-Le pregunté tranquilamente al ver que realmente le angustiaba-"
            show Armin disgustado s
            with dissolve
            a "Ella me dijo que yo servía para la Legión."
            a "Fue la primera en decirme que, a pesar de ser débil, tenia potencial y podía sobrevivir mientras siguiera mis sueños."
            n "-Comenzó a hablar aguantando las lágrimas-"
            a "Era de las pocas personas con las que hablaba cuando nos hicimos reclutas..."
            show Armin hablando s
            with dissolve
            n "-Contaba mientras sonreía suavemente-"
            a "Y sin darme cuenta se volvió alguien importante para mí, aunque ella no lo supiera."
            a "Al grado de sentirme aliviado de saber que estaría bien por no volver a ver titanes en su vida..."
            show Armin disgustado sce
            with dissolve
            n "-Concluyó bajando la cabeza y mordiéndose el labio inferior-"
            n "Estaba realmente sorprendida, jamás había visto a Armin conversar con Annie."
            n "Pero era obvio que jamás los vi por estar tan pegada a Eren."
            n "De cierta manera dejaba muchas veces atrás a Armin por estar con Eren. Últimamente me maldecía por todo eso que hacía antes."
            m "Entiendo..."
            n "-Le dije comprendiendo lo que sentía-"
            m "¿Armin... qué sientes por ella?"
            n "-Le pregunté sin saber qué me respondería-"
            show Armin hablando s
            with dissolve
            a "No lo sé... la veía como una gran amiga para mí."
            show Armin sonrojado s
            with dissolve
            a "Pero últimamente, cada vez que la veía, sentía sensaciones raras que jamás había sentido."
            a "Me ponía nervioso hablar con ella, me sonrojaba cuando la veía y muchas veces no podía sacarla de mi cabeza."
            n "-Mencionó algo apenado mientras un leve sonrojo pintaba sus suaves mejillas-"
            hide Armin sonrojado s
            with dissolve
            define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
            scene miri
            with flashbulb
            n "(Levi)"
            n "-Pensé-"
            scene torre
            with dissolve
            show Armin sonrojado s
            with dissolve
            n "Me pasaba exactamente lo mismo cada vez que lo veía, cada vez que estaba cerca de él."
            n "En cada momento, el recuerdo de sus pequeñas sonrisas no desaparecían por noches, era realmente confuso pero ahora entendía que no solo yo vivía con esos síntomas."
            a "Es algo que le llaman amor."
            n "-Mencionó algo apenado mirándome a los ojos-"
            m "¿Amor?"
            n "-Pregunté inocentemente-"
            show Armin feliz s
            with dissolve
            a "¡Sí!"
            a "Hay diferente tipos de amor."
            a "El que sientes por tu familia, por tus amigos más cercanos, por tus compañeros de trabajo."
            show Armin sonrojado s
            with dissolve
            a "Y... el que sientes por otra persona, normalmente del género opuesto, una atracción y el deseo de estar a su lado y pensar que es la persona perfecta..."
            show Armin alegre s
            with dissolve
            n "-Rió algo nervioso-"
            a "... o eso decía el libro."
            show Armin serio s
            with dissolve
            n "-Dijo rascándose la cabeza nervioso-"
            m "¿Y qué amor es el que sientes por Annie?"
            n "-Pregunté con curiosidad aún asombrada del dato que me había dado-"
            show Armin sonrojado s
            with dissolve
            a "Supongo que el último."
            n "-Contestó con la mirada baja totalmente sonrojado-"
            show Armin disgustado s
            with dissolve
            a "Pero yo no sé nada del tema, así que no podría acercarme a ella como quiero para protegerla."
            show Armin disgustado sce
            with dissolve
            n "-Mencionó ahora triste-"
            m "No pienses eso, Armin,. Si realmente quieres estar con ella entonces lucha por ella."
            show Armin feliz s
            with dissolve
            m "Annie es una buena persona y creo que sería lindo que estuvieran juntos."
            n "-Le sonreí mientras tomaba una de sus manos-"
            m "¿No es así?"
            n "-Le pregunté esperando su respuesta-"
            a "¡Tienes razón Mikasa!"
            n "-Comenzó a ponerse en pie sin soltar mi mano-"
            show Armin alegre s
            with dissolve
            a "Gracias..."
            n "-Me dijo dándome una de esas sonrisas características de él-"
            show Armin feliz s
            with dissolve
            a "Necesitaba hablar con alguien, gracias por escucharme."
            n "-Mencionó con alegría viéndome de reojo-"
            m "Era lo mínimo que podía hacer después de todo lo que has hecho por mí."
            n "-Confesé imitando su sonrisa-"
            n "Nos soltamos la mano y nos seguimos mirando con tiernas sonrisas, el Armin que conocía estaba de vuelta."
            show Armin serio s
            with dissolve
            a "Eh, ¿Mikasa?"
            n "-Volteé a verlo extrañada-"
            a "¿Qué hacen esas hojas ahí?"
            n "-Señaló las hojas que estaban en el suelo-"
            with hpunch
            m "¡El reporte!"
            n "-Grité corriendo a recoger las hojas-"
            m "El comandante me pidió el informe de lo que sucedió en la expedición y otras cosas."
            n "-Le dije exaltada poniéndome de pie-"
            m "¡Te veo después o no acabaré!"
            show Armin disgustado sce
            with dissolve
            n "-Salí corriendo del lugar, no sin antes escuchar el *cuídate Mikasa* de Armin que me miraba nervioso y preocupado-"
            hide Armin disgustado sce
            with dissolve
            scene afuera
            with fade
            scene tabernanoche
            with fade
            n "Bajé rápido las escaleras y entré rápidamente a mi habitación, tan estrepitosamente que pensé que había despertado a Sasha."
            n "Pero ella ni siquiera se levantó, realmente tenia el sueño pesado."
            n "Agitada, coloqué las hojas en el escritorio y encendí una vela para alumbrar el lugar."
            n "Me senté sin hacer mucho ruido y comencé a con mi reporte."
            n "Anoté lo más prevalente de ese día, poniendo énfasis en las características de esas horribles bestias, su forma de actuar y mi opinión."
            n "Anoté también el por qué de mis acciones y quiénes eran importantes para mí."
            n "Mientras escribía me dolía la mano, jamás había escrito tanto en un informe y por ello me cansaba con facilidad."
            n "Una vez que terminé volví a releerlo una y otra vez para cerciorarme de que todo estaba bien."
            n "Pero estaba tan cansada que me recosté en el escritorio y me quedé dormida cerrando lentamente mis ojos."
            jump des


        "¿Por qué estabas aquí solo?":
            python:
                ArminAmizade2 += 5
            call chamarBarraMais2(ArminAmizade2)
            with dissolve
            a "Simplemente quería estarlo..."
            n "-Estaba insatisfecha con la respuesta-"
            m "Pero..."
            a "Eh, ¿Mikasa?"
            n "-Fui interrumpida y volteé a verlo extrañada-"
            a "¿Qué hacen esas hojas ahí?"
            n "-Señaló las hojas que estaban en el suelo-"
            with hpunch
            m "¡El reporte!"
            n "-Grité corriendo a recoger las hojas-"
            m "El comandante me pidió el informe de lo que sucedió en la expedición y otras cosas."
            n "-Le dije exaltada poniéndome de pie-"
            show Armin disgustado sce
            with dissolve
            m "¡Te veo después o no acabaré!"
            hide Armin disgustado sce
            with dissolve
            n "-Salí corriendo del lugar, no sin antes escuchar el *cuídate Mikasa* de Armin que me miraba nervioso y preocupado-"
            scene afuera
            with fade
            scene tabernanoche
            with fade
            n "Bajé rápido las escaleras y entré rápidamente a mi habitación, tan estrepitosamente que pensé en que había despertado a Sasha."
            n "Pero ella ni siquiera se levantó, realmente tenia el sueño pesado."
            n "Agitada, coloqué las hojas en el escritorio y encendí una vela para alumbrar el lugar."
            n "Me senté sin hacer mucho ruido y comencé a con mi reporte."
            n "Anoté lo más prevalente de ese día, poniendo énfasis en las características de esas horribles bestias, su forma de actuar y mi opinión."
            n "Anoté también el por qué de mis acciones y quiénes eran importantes para mí."
            n "Mientras escribía me dolía la mano, jamás había escrito tanto en un informe y por ello me cansaba con facilidad."
            n "Una vez que terminé volví a releerlo una y otra vez para cerciorarme de que todo estaba bien."
            n "Pero estaba tan cansada que me recosté en el escritorio y me quede dormida cerrando lentamente mis ojos."
            jump des


label des:
    play music "musica normal.mp3"
    scene taberna
    with fade
    show Shasha Contenta
    with dissolve
    s "Mikasa... Mikasa... ¡Oye, Mikasa!"
    n "-Escuchaba a lo lejos la voz de Sasha pronunciando mi nombre mientras sentía que me movía con brusquedad-"
    m "¿Qué quieres, Sasha?"
    n "-Le pregunté molesta por despertarme-"
    show Shasha Pensando
    with dissolve
    s "Mikasa..."
    s "¡Son las once de la mañana y aún sigues dormida!"
    with hpunch
    m "¿¡Qué!?"
    n "-Grité abriendo los ojos por completo y poniéndome de pie torpemente-"
    m "¡Sasha, dime que es mentira!"
    n "-Coloqué mis manos en sus hombros con algo de brusquedad mientras la miraba a los ojos angustiada-"
    show Shasha Feliz
    with dissolve
    s "Es verdad, Mikasa... Es más, te traje tu ración de comida ya que ayer tampoco bajaste a cenar."
    n "-Me extendió un pedazo de pan y un poco de leche-"
    m "Sasha..."
    n "-Logré pronunciar apenas conmocionada-"
    m "Pero te van a regañar."
    n "-Le dije mirándola con algo de culpa-"
    show Shasha Contenta
    with dissolve
    s "¡Eso no importa!"
    s "¡Es más importante que comas!"
    n "-Dijo brindándome una sonrisa antes de disponerse a salir del cuarto-"
    show Shasha Pensando
    with dissolve
    s "¡No vuelvas a dejar la vela encendida!"
    s "¿Qué tal si ocasionas un incendio?"
    n "-Me reprochó inflando sus cachetes-"
    show Shasha Feliz
    with dissolve
    m "Lo siento... No volverá a pasar."
    n "-Le dije algo apenada por lo que había hecho por mí y por ser tan descuidada-"
    show Shasha Contenta
    with dissolve
    s "Está bien."
    n "-Contestó con una brillante sonrisa para salir de la habitación-"
    hide Shasha Contenta
    with dissolve
    n "Debía darme prisa."
    scene oficina
    with fade
    n "Disfruté mi desayuno. Tomé los papeles y fuí directa a la oficina del comandante. Al llegar toqué la puerta y, con su permiso, entré."
    m "Con su permiso, comandante."
    n "-Pronuncié haciendo el singular saludo de soldado-"
    show Erwin normal1 s
    with dissolve
    r "¡Ackerman!"
    n "-Exclamó sorprendido al verme-"
    show Erwin incomodo2 s
    with dissolve
    r "No creí que lo harías tan pronto, debí darte más tiempo."
    n "-Confesó nervioso mientras se rascaba la nuca-"
    show Erwin incomodo2 s
    m "No hay problema."
    n "-Dije fingiendo ya que sí me había molestado-"
    m "Aquí tiene."
    n "-Le extendí los papeles y, saludando nuevamente, comencé a retirarme de su oficina-"
    r "¿Ackerman, podría pedirle un favor?"
    n "-Tan solo asentí con la cabeza-"
    show Erwin incomodo1 s
    with dissolve
    r "¿Podría cuidar a Levi un día más?"
    r "Hange está realmente ocupada y yo necesito organizar papeles."
    show Erwim feliz s
    with dissolve
    r "¿Hay algún inconveniente?"
    n "-Preguntó en un tono de burla-"
    m "Ninguno, señor."
    n "-Contesté mientras mi cuerpo se estremecía por dentro y salía de la habitación sonrojada-"
    hide Erwim feliz s
    hide Erwin incomodo1 s
    hide Erwin normal1 s
    hide Erwin incomodo2 s
    with dissolve
    scene habile
    with fade
    play music "musica sadhappy.mp3"
    play sound "puerta.mp3"
    n "Ya, un poco más calmanda, entré a la habitación de Levi."
    show Levi tranquilo s
    with dissolve
    n "Lo vi sentado en la silla afuera de la ventana, me acerqué y me senté en la orilla de la cama."
    m "¿Ya estás mejor?"
    n "-Le pregunté suavemente mientras revisaba con la mirada sus heridas de la espalda-"
    show Levi suave2 s
    with dissolve
    l "Sabía que vendrías..."
    n "-Dijo volteando a verme-"
    show Levi feliz s
    with dissolve
    l "No te negarías a venir, ¿cierto?"
    n "-Sonrió sarcásticamente-"
    m "Solo quiero pagarte por la vez que me rescataste, es todo."
    n "-Contesté molesta cruzándome de brazos y dirigiendo mi mirada a otro lado-"
    show Levi normal s
    with dissolve
    l "No creo que sea solo eso..."
    n "-Recalcó sobresaltándome con sus palabras-"
    n "Tenía razón, yo no venía solo a eso. Venía a verlo, a ver cómo estaba, ver su cara, quería estar con él."
    n "Quería sentir su presencia cerca de mí, quería que él despertara todas esas extrañas y hermosas sensaciones que solo él me provocaba."
    n "Quería sentir su aroma natural, no impregnado en mi bufanda."
    n "Quería besarlo, sentir el roce de sus labios con los míos."
    n "Quería que su mirada penetrara la mía, que me llevara a otro mundo con sus ojos, que nuestros cuerpos se pegarán y el calor se hiciera presente."
    n "Fue entonces que recordé que a eso se le llamaba *AMOR*."
    n "-Sonreí mientras él me miraba extrañado-"
    show Levi sorpendido s
    with dissolve
    m "Tienes razón."
    m "Vengo a verte."
    n "-Finalmente lo había dicho con un nudo en la garganta y con la vergüenza al límite, pero volteé a verlo-"
    n "Estaba sorprendido, asombrado e impactado por mis palabras sin poder creerlas."
    show Levi sonrojado s
    with dissolve
    n "El brillo de sus ojos era muy notorio, así como su respiración agitada y el leve sonrojo en sus mejillas."
    n "-Se volteó un momento y, soltando todo el aire acumulado, respondió-"
    l "No digas esas cosas, mocosa..."
    n "-Comentó molesto pero sonrojado, sabía que mentía-"
    show Levi normal s
    with dissolve
    n "Tan solo sonreí y me puse de pie para salir de la habitación."
    l "¿A dónde vas?"
    n "-Preguntó sin voltear a verme-"
    m "A traerte algo de comer, no has comido nada."
    n "-Le respondí saliendo de la habitación-"
    hide Levi normal s
    with dissolve
    scene pasillo2
    with fade
    n "Me dirigí a la cocina y por el camino encontré a Armin y Eren hablar en el pasillo."
    n "Pasé desapercibida por ambos y entré a la cocina."
    scene cocina
    with fade
    n "Mientras preparaba algunos alimentos, alcancé a escuchar levemente la conversación que ambos tenían."
    e "Lo siento, Armin."
    e "Tenías razón con todo lo que me dijiste, ahora lo he pensado y me he dado cuenta de que soy yo el culpable de todo."
    n "-Le escuche reprocharse a sí mismo-"
    e "Por ello te pido que me perdones, te he tratado tan mal últimamente cuando tú solo querías protegerme."
    e "Siempre has estado a mi lado y no me gustaría perder a mi mejor amigo por mi culpa."
    n "-Habló en un tono de total honestidad y triste-"
    a "Como tu amigo siempre te apoyaré Eren."
    a "Admito que me hiciste sentir mal y solo muchas veces, pero creo que no soy yo con quien deberías disculparte."
    n "-Sabía que se refería a mí-"
    a "Yo solo quise abrirte los ojos. Quería demostrarte que estabas dejando atrás a todos y que estabas haciendo las cosas mal."
    a "Y ahora que ya lo comprendiste me gustaría que regresases a ser el que eras antes."
    a "El Eren que conocí cuando éramos niños, ese es el Eren que todos queremos."
    n "-Le comentó seguro de sí mismo-"
    e "Lo tendrás pronto, Armin, pero necesito que me ayudes a ser el que era antes. Necesitó tu apoyo ahora más que nunca."
    n "-Le suplicó-"
    n "Sus voces dejaron de oírse."
    scene pasillo2
    with fade
    n "Una vez que tuve la bandeja lista, salí de la cocina y me cerciné de que no hubiera nadie."
    n "Ambos se habían ido. Caminando a paso lento recordaba un poco de las palabras de Eren."
    n "Me alegraba saber que regresaría a ser el de siempre y que sería Armin quien lo apoyaría, pero yo ya había hecho una promesa."
    n "El amor que sentía por Eren no iba más allá de su seguridad y protección."
    n "Aquel amor desesperado que sentía por él había desaparecido hacía mucho. Ahora esos sentimientos le pertenecían a otra persona."
    n "La persona que descontrolaba mis 5 sentidos, la que me mostraba mis debilidades y fortalezas y me comprendía con tan solo mirarme."
    show lili
    with fade
    show text "{size=+25}{color=#FFFFFF}La persona que tiene muchos parentescos conmigo, solo esa persona era dueña de mi corazón, de mis desveladas, de mis pensamientos, de mi cuerpo...{/color}{/size}" at truecenter
    with dissolve
    pause 8
    show text "{size=+25}{color=#FFFFFF}Solo él...{/color}{/size}" at truecenter
    with dissolve
    pause 3
    show text "{size=+25}{color=#FFFFFF}El capitán Levi era dueño de mi frío corazón que comenzaba a calentarse con algo llamado...*Amor*...{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}Capitulo 6{/color}{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}FIN{/color}{/size}" at truecenter
    with dissolve
    pause 0
    hide text
    with dissolve
    $persistent.cap7 = True
    return

label capitulo7:
    play music "medieval.mp3"
    show text "{size=+25}{color=#FFFFFF}Capítulo 7{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}No es un rumor{/color}{/size}" at truecenter
    with dissolve
    pause 6
    hide text
    show screen quick_menu
    with dissolve
    show lili
    with fade
    show cielo2
    with dissolve
    n "La luz del sol anunciaba un nuevo día."
    n "Los penetrantes rayos solares se asomaban por la ventana de mi habitación dándome la señal de que debía levantarme pronto."
    show taberna
    with fade
    n "Con pereza, me levanté de la cama y comencé a vestirme con el uniforme militar."
    n "Anoche había llegado muy tarde a mi cuarto y había tardado en conciliar el sueño."
    n "¿La razón?"
    n "Me había quedado hasta tarde con Levi."
    n "Había revisado sus heridas y otras las había tratado, en pocos días podría estar totalmente recuperado."
    n "Me había quedado con él llevándole sus alimentos, hasta que llegó Hange, así que pude regresar a mi cuarto."
    n "Pero el recuerdo de su voz, sus sonrisas, las sensaciones de sus manos tocando mi piel..."
    n "El roce de sus labios con los míos, sus ojos con aquel brillo especial y su mirada penetrante..."
    n "Eran las causantes de mi actual insomnio, eran las causantes de que pasara horas sin dormir recordando cada uno de sus finos detalles."
    n "Su perfecta figura, de su misterioso pasado..."
    n "Eran cada vez más las veces que dormía menos, y aun así, despertaba con las mayores energías para el entrenamiento diario."
    show Shasha Contenta s
    with dissolve
    s "¡Mikasa!"
    s "¡Vámonos al comedor!"
    n "-Exclamó mi compañera de cuarto con una tremenda sonrisa-"
    m "Termina de ponerte las botas e iremos."
    n "-Le contesté mientras ella soltaba una risita-"
    m "No te dejarán entrar descalza."
    n "-Le dije mientras soltaba una pequeña risilla por su poca atención-"
    show Shasha feliz s
    with dissolve
    s "Sí, sí, sí."
    n "-Renegó sentándose en el suelo y poniéndose sus botas-"
    show Shasha hablando s
    with dissolve
    s "Por cierto, Mikasa..."
    n "-Volteé a verla-"
    s "¿A qué hora llegaste ayer?"
    show Shasha feliz s
    with dissolve
    n "-Preguntó mientras se ponía su segunda bota con dificultad-"
    m "Muy tarde."
    n "-Le contesté sin darle importancia-"
    m "¿Por qué?"
    n "-Le pregunté mirándola con curiosidad-"
    show Shasha hablando s
    with dissolve
    s "Pues me sorprende que siempre tengas energías."
    n "-Contestó riendo y dirigiéndose a la puerta-"
    show Shasha Contenta s
    with dissolve
    s "¡Vamos!"
    n "-Exclamó abriendo la puerta y saliendo del cuarto-"
    play sound "puerta.mp3"
    hide Shasha Contenta s
    with dissolve
    n "Solté un suspiro, su pregunta me había incomodado un poco."
    n "Pero me alegraba que no supiera por qué llegaba tarde."
    n "Salí de la habitación y comencé a seguirla."
    show pasillo2
    with fade
    show Shasha sonrojada s
    with dissolve
    n "En medio del pasillo Sasha volteó a verme y con una sonrisa pícara y ojos penetrantes me dijo:"
    s "Espero que el rumor que contó la señorita Hange el otro día haya sido mentira."
    m "¿De qué hablas?"
    n "-Pregunté con algo de nerviosismo sintiendo mis latidos cada vez más rápidos-"
    show Shasha hablando s
    with dissolve
    s "Ya sabes..."
    n "-Comentó en tono divertido-"
    show Shasha sonrojada s
    with dissolve
    s "Que tú y el capitán Levi se ven a escondidas para andarse besando."
    show Shasha Contenta s
    with dissolve
    n "-Dijo entre carcajadas divertidas y pícaras-"
    show Shasha feliz s
    with dissolve
    n "Sentí que una piedra enorme caía sobre mí."
    n "Tragué saliva e intenté calmar mis impulsos de salir corriendo de ahí avergonzada."
    n "(Así que ese fue el rumor que inventó Hange el día que nos vio en el bosque)"
    n "-Pensé con una cara totalmente avergonzada-"
    m "Eso es mentira."
    n "-Contesté con mi voz temblando y sin mirarla a los ojos-"
    show Shasha hablando s
    with dissolve
    s "¡Ya lo sé, Mikasa!"
    n "-Colocó sus manos sobre mis hombros brindándome una gran sonrisa-"
    play sound "imagi.mp3"
    s "¡Solo fue un chisme que todos se creyeron!"
    show Shasha Contenta s
    with dissolve
    n "-Rió mientras miraba mi cara con detenimiento-"
    show Shasha hablando s
    with dissolve
    s "¡No te lo tomes tan en serio, Mikasa. Ya sé que tú no harías eso!"
    show Shasha feliz s
    with dissolve
    n "-Me reprochó al ver que no hacía otra expresión más que de asombro-"
    m "Eh... sí..."
    n "-Le dije fingiendo una sonrisa divertida-"
    show Shasha Contenta s
    with dissolve
    s "Bueno..."
    s "¡Vayamos al comedor, que me estoy muriendo de hambre!"
    n "-Exclamó mientras caminaba con mayor rapidez por el pasillo-"
    hide Shasha Contenta s
    with dissolve
    show tarven
    with dissolve
    play music "murmurando.mp3"
    n "El comedor se encontraba lleno."
    n "El aroma a hierbas frescas y pan recién horneado inundaba el lugar."
    n "El bullicioso murmullo de los soldados sentados en grupos hablando de sus experiencias del día pasado era intenso."
    n "Se oía el sonido de platos y vasos chocando entre sí."
    n "Y las incontables carcajadas y risas de ciertos grupos de amigos hacían del lugar y el tiempo..."
    n "el único momento donde podíamos liberar toda presión que cargásemos al pertenecer a la Legión de Reconocimiento."
    n "Una vez que recibí mi porción de comida me dirigí a la mesa en donde se encontraban Armin, Crista, Connie y Sasha sentados."
    n "Últimamente me sentaba con ellos en cada comida."
    cr"¡Hola, Mikasa!"
    n "-Me saludó alegremente la rubia de ojos azules con esa hermosa sonrisa-"
    play sound "comoestas.mp3"
    cr"¿Cómo estás?"
    n "-Me preguntó sin dejar de sonreír-"
    m "Bien, Crista. Gracias."
    n "-Contesté brindándole una cálida sonrisa-"
    co"¡Hoy tardaron mucho en llegar!"
    show Shasha feliz s
    with dissolve
    n "-Comentó Connie dirigiendo su mirada a Sasha y posteriormente a mí-"
    show Shasha Pensando s
    with dissolve
    s "¡Mikasa aún no despertaba!"
    n "-Contestó Sasha con medio pan en la boca-"
    m "¡Pero si a ti te faltaba ponerte las botas!"
    n "-Le dije frunciendo el ceño molesta-"
    show Shasha Contenta s
    with dissolve
    n "Sasha tan solo rió mientras terminaba de comerse el pan."
    show Shasha feliz s
    with dissolve
    n "El ambiente era tranquilo en aquella mesa, aunque la mayoría de las veces Sasha era la que causaba el desorden."
    hide Shasha feliz s
    with dissolve
    n "Me gustaba el lugar."
    n "Desde hacía poco había comenzado a relacionarme más con mis compañeros de escuadrón."
    n "Mi relación con Sasha había mejorado bastante, sin mencionar mi amistad con Armin, que era la más cercana y confiable que tenía."
    n "Desde el día del juicio me había propuesto varias cosas, entre ellas..."
    n "Relacionarme más con las personas y, aunque en un principio me fue difícil..."
    n "Tanto para mí como para ellos, hubo varios que lograron ayudarme brindándome su confianza desde el inicio."
    n "Y ellos eran los que estaban sentados conmigo, riéndose y disfrutando de ese momento."
    k "¡Buenos días soldados!"
    stop music
    n "-La voz grave del comandante Mike resonó en todo el comedor provocando que todos guardaran silencio-"
    k "¡Es hora de empezar el entrenamiento!"
    n "-Automáticamente todos comenzaron a ponerse de pie y a salir del comedor para dirigirse al campo de entrenamiento-"
    show Armin feliz s
    with dissolve
    a "¡Vamos, Mikasa!"
    n "-Exclamó mi amigo estirando su mano para que la tomara-"
    n "Tomé su mano amablemente y salimos del comedor."
    hide Armin feliz s
    with dissolve
    play music "medieval.mp3"
    show pasteur_day
    with dissolve
    n "Buscamos nuestra línea de formación habitual para escuchar las instrucciones de ese día."
    k "¡Antes de comenzar con el entrenamiento hay dos anuncios importantes que debo decirles por orden directa del comandante Erwin!"
    n "Su voz fuerte resonaba por todo el campo. Todos manteníamos posición de descanso."
    k "La primera es que... ¡La siguiente expedición será la siguiente semana!"
    n "-Exclamó mientras varios soldados se miraban entre sí asustados-"
    k "La segunda es que... ¡Tendremos a una nueva integrante en las tropas!"
    k "¡Pasa, por favor!"
    n "-Exclamó realizando un gesto para que cierta persona entrase en escena-"
    n "Los murmullos no tardaron en aparecer."
    n "Algunos se preguntaban qué tipo de persona entraría a la Legión."
    n "Otros estaban asustados por la siguiente expedición."
    n "Y otros permanecían callados e inquietos en su posición, como Armin y yo."
    n "Los murmullos se dejaron de escuchar de repente."
    n "Clavé mis ojos en la persona delante de todos, ella estaba al lado del comandante realizando el saludo militar."
    k "Por favor, preséntese soldado."
    n "-Ordenó el comandante en posición firme y con voz autoritaria-"
    show Annie hablando s
    with dissolve
    an"¡Annie Leonhart!"
    show Annie normal s
    with dissolve
    n "-Respondió ella con voz seria-"
    k "A partir de hoy la soldado Leonhart formará parte de la Legión de Reconocimiento."
    k "¡Espero que apoyen a su nueva compañera!"
    n "-Exclamó autoritariamente mirándonos a todos-"
    hide Annie normal s
    with dissolve
    n "*¡Sí!* Contestamos al unísono todos los soldados realizando el saludo militar-"
    k "¡Tomen posiciones y divídanse en grupos de 4!"
    k "¡Después regresen a formación para darles las indicaciones!"
    show Armin disgustado sce
    with dissolve
    n "Volteé a ver a Armin, quien solo observaba con angustia a Annie."
    n "Podía ver en su mirada que tenía miedo y preocupación por ella, desde hacía días se encontraba en ese estado."
    show Armin sonrojado s
    with dissolve
    n "Tomé una de sus manos para que me mirase, me sonrió nervioso y al mismo tiempo sonrojado."
    n "Sabía qué era lo que quería."
    n "Le brindé una cálida sonrisa y con seguridad me dirigí a cierta persona seguida de Armin, quien iba apenado."
    hide  Armin sonrojado s
    with dissolve
    show Annie sorprendida s
    with dissolve
    play sound "annie.mp3"
    m "Annie..."
    n "-La llamé. Ella se giró sorprendida-"
    m "Veo que terminaste entrando a la legión."
    n "-Confesé mirándola algo preocupada. Me había pegado la preocupación ese día-"
    play sound "io.mp3"
    an"Sí..."
    n "-Apenas contestó-"
    hide Annie sorprendida s
    with dissolve
    show Armin sonrojado s
    with dissolve
    a "Annie..."
    n "-La voz temblorosa de Armin se escuchó detrás de mí-"
    a "¿Te gustaría... hacer equipo con nosotros?"
    n "-Le preguntó mirándola con esos ojos azules brillantes-"
    hide Armin sonrojado s
    with dissolve
    show Annie sorprendida s
    with dissolve
    n "-Se quedó callada con la cabeza agachada-"
    n "Realmente había cambiado mucho, ya no era aquella chica fría y dura."
    n "Ahora demostraba más emociones y sentimientos con cualquiera."
    hide Annie sorprendida s
    with dissolve
    show Armin feliz s
    with dissolve
    play sound "na.mp3"
    je"¡Oye, Armin!"
    n "-Escuché a alguien gritar a lo lejos-"
    play sound "jen.mp3"
    je"¿Puedo hacer equipo contigo?"
    n "-Preguntó Jean, ya más cerca de nosotros-"
    a "Claro... ¿No hay problema, Mikasa?"
    n "-Me preguntó colocándose al lado de Jean-"
    play sound "sibi.mp3"
    m "Claro, me parece bien."
    m "¿Y tú, Annie?"
    n "-Le volví a preguntar mirándola fijamente-"
    hide Armin feliz s
    with dissolve
    show Annie feliz s
    with dissolve
    play sound "io.mp3"
    an"Está bien..."
    n "-Contestó ella mirándome algo apenada-"
    hide Annie feliz s
    with dissolve
    show Armin hablando s
    with dissolve
    a "¡Entonces vayamos a la línea de formación!"
    show Armin serio s
    with dissolve
    n "Armin había vuelto a ser el de antes. Él se preocupaba mucho por Annie incluso en un entrenamiento."
    n "Su comportamiento me daba mucho que pensar."
    n "¿Por qué actuaba así? ¿Por qué se ponía de esa manera? ¿Por qué le preocupaba lo más mínimo?"
    hide Armin serio s
    with dissolve
    n "Regresamos a la línea todos los soldados ya con nuestros equipos formados."
    n "Parecía ser que el entrenamiento sería diferente está vez."
    k "¡El entrenamiento consistirá en ver qué tan hábiles son manejando un caballo ajeno mientras se enfrentan a diversos obstáculos!"
    scene lili
    with dissolve
    show text "{size=+25}{color=#FFFFFF}-Inició la explicación del ejercicio-{/color}{/size}" at truecenter
    pause 3
    hide text
    with dissolve
    show pasteur_day
    with fade
    k "Empezarán ideando la mejor estrategia para que todos los integrantes del equipo sobrevivan."
    k "Si uno falla, significaría su muerte en una expedición..."
    n "-Escalofríos recorrieron el cuerpo de algunos soldados-"
    k "¡Si todos los integrantes sobreviven, significaría la victoria!"
    n "-Otros soldados se miraron con orgullo-"
    k "¡Tomen el entrenamiento enserio, ya que se utilizará esta técnica para la siguiente expedición!"
    n "-Recalcó mirándonos fijamente-"
    k "¡El primer equipo será el de Leonhart!"
    n "-Anunció tomando una lista-"
    n "El murmullo del resto de los soldados no se hizo esperar, todos querían ver las habilidades de la nueva integrante de la Legión."
    play music "suspenso.mp3"
    scene entre
    with fade
    n "Caminamos hasta el bosque asignado y nos subimos a los caballos tomando las posiciones que hace unos minutos habíamos planeado con la mirada."
    n "El comandante lanzó la señal y comenzamos con el entrenamiento."
    n "Armin iba al frente, Annie y yo íbamos a los costados y Jean detrás."
    n "El plan consistía en que Annie y yo nos encargaríamos de matar a los titanes."
    n "Armin nos avisaría del avistamiento de algún titán u obstáculo y nos daría órdenes."
    n "Jean nos cuidaría la espalda y serviría de cebo en caso de que se necesitase."
    n "Durante el trayecto se presentaron obstáculos sencillos que tenían como objetivo el poder manejar a nuestro caballo."
    show Armin enojado s
    with dissolve
    a "¡Titán!"
    a "¡Por ambos lados!"
    hide Armin enojado s
    with dissolve
    n "Annie y yo volteamos a vernos y, asintiendo sin decir nada, saltamos sobre el lomo del caballo."
    n "Sacamos las cuchillas y, tomando la mejor postura, clavamos los ganchos en los troncos más cercanos"
    show bosq
    with pushright
    n "Nos impulsamos con el gas hasta llegar a la máquina que representaba un titán."
    play sound "stuijm2.mp3"
    with hpunch
    n "Cortamos la zona donde debería estar la nuca."
    scene entre
    with pushleft
    n "Regresamos a nuestras posiciones y volvimos a tomar el control de los caballos."
    je"¡Dos titanes excéntricos por atrás!"
    n "-Gritó Jean al ver las figuras mecánicas que representaban a los excéntricos-"
    show Armin enojado s
    with dissolve
    a "¡Sigamos!"
    n "-Ordenó Armin cambiando de dirección. Todos le seguimos-"
    a "¡Si nos movemos nos alcanzará!-"
    n "Acertó."
    hide Armin enojado s
    with dissolve
    n "Las figuras se quedaron atrás y, con ello y esquivando los últimos obstáculos, derrotamos a los últimos titanes."
    n "Salimos del bosque terminando nuestra sesión."
    play music "WYS - Snowman.mp3"
    show pasteur_day
    with dissolve
    n "Recibimos los aplausos y halagos de algunos compañeros que nos miraban asombrados; entre ellos, el comandante."
    k "¡Bien hecho!"
    n "-Nos felicitó brindándonos una sonrisa-"
    k "¡Pueden ir a descansar!"
    n "Realizamos el saludo militar y, sin decir nada, nos retiramos al campo abierto"
    n "Jean se quedó a ver al resto de los equipos."
    show Armin feliz s
    with dissolve
    a "¡Lo conseguimos!"
    n "-Se alegró Armin sonriéndole al cielo y acostándose en el suelo-"
    m "¡Todo gracias a ti, Armin!"
    n "-Contesté sentándome a su lado-"
    show Armin disgustado sce
    with dissolve
    a "No es cierto."
    a "Si tanto tú como Annie no lucharan contra los titanes, mi plan no funcionaría."
    a "En realidad yo solo aviso, no tengo que enfrentarme a esas bestias."
    n "-Mencionó algo triste, pero seguro de sí mismo-"
    hide Armin disgustado sce
    with dissolve
    show Annie hablando s
    with dissolve
    an"Creo que sin la cabeza no hay acción."
    n "-Habló Annie mientras miraba a Armin-"
    show Annie feliz s
    with dissolve
    an "Si tú no nos dirigieras ni avisaras, sería demasiado tarde y no podríamos actuar."
    hide Annie feliz s
    with dissolve
    show Armin sonrojado s
    with dissolve
    n "-Mencionó brindándole una cálida sonrisa a lo que Armin se sonrojó y bajó la mirada-"
    n "Armin se veía realmente tierno sonrojado y apenado, parecía un niño pequeño."
    scene img12b
    show love
    with fade
    n "Sus ojos azules brillaban más de lo normal, se veían inquietos y solo miraban con determinación a una persona."
    n "Annie se acababa de sentar en el pasto. Levantó su rostro mientras abría los ojos para ver el cielo."
    n "El viento que soplaba en esos momentos jugaba con su cabello."
    n "Los ojos de Armin estaban posados en ella, con aquel brillo único y esos ojos inquietos."
    n "*... Amor es el que sientes por otra persona, normalmente del género opuesto, una atracción y el deseo de estar a su lado y pensar que es la persona perfecta...*"
    n "La voz de Armin retumbó en mi cabeza."
    n "El recuerdo de aquellas palabras me hizo darme cuenta de que Armin presentaba ese amor del que hablaba."
    n "Armin sentía atracción por Annie, podía verlo en su mirada, en sus mejillas, en sus palabras, en sus acciones, podía verlo en todos lados."
    show pasteur_day
    with fade
    n "Me levanté despacio del pasto y, respirando por última vez la tranquilidad de ese lugar, comencé a caminar en dirección al edificio de la Legión."
    show Armin hablando s
    with dissolve
    a "¿Mikasa, a dónde vas?"
    hide Armin hablando s
    with dissolve
    show Annie normal s
    with dissolve
    n "-Me preguntó Armin mirándome extrañado al igual que Annie-"
    hide Annie normal s
    with dissolve
    show Armin serio s
    with dissolve
    m "No he dormido bien estos días..."
    n "-Fingí estar cansada-"
    show Armin sonrojado s
    with dissolve
    m "Ya que terminó todo, quiero ir a descansar, así que pueden quedarse aquí los dos."
    hide Armin sonrojado s
    with dissolve
    show Annie sonrojada s
    with dissolve
    n "-Respondí brindándoles una sonrisa. Ambos se sonrojaron-"
    m "¡Nos vemos!"
    n "-Me marché del lugar no sin antes volver a mirar a ambos, avergonzados mirando al suelo-"
    hide Annie sonrojada s
    with dissolve
    show Armin sonrojado s
    with dissolve
    hide Armin sonrojado s
    with dissolve
    play music "As the Day Ends.mp3"
    show pasillo3dia
    with fade
    n "Caminé por los pasillos del cuartel, estos se encontraban en completo silencio ya que la mayoría aún realizaban su entrenamiento."
    n "La tenue luz que los alumbraba me resultaba gratificante de cierta manera."
    n "Caminaba por cada pasillo sin un lugar en concreto a donde ir. Sin darme cuenta terminé en la habitación donde estaba Levi."
    play sound "corazon.mp3"
    n "Mi corazón comenzó a acelerarse en cuanto reconocí la puerta."
    n "El nerviosismo se apoderó de mi cuerpo."
    n "(¿Por qué de todos los lugares tenía que llegar justamente ahí?)"
    n "Era el destino."
    n "Harta de aquellas sensaciones, me dispuse a entrar; prefería tener esas sensaciones estando con él."
    play sound "toc toc.mp3"
    n "Así que toqué la puerta con suaves golpes esperando una respuesta, pero nunca llegó."
    n "Lo intenté una vez más y tampoco funcioó. La curiosidad me hizo entrar en silencio y con cuidado."
    show habile
    with fade
    n "Cerré la puerta con cuidado y visualicé rápidamente la habitación."
    n "No había nada diferente al día anterior, me acerqué a la cama y lo vi."
    show domile2
    with fade
    n "Estaba dormido con un semblante diferente, estaba tenso, asustado, nervioso."
    n "Podía observar que estaba sudando, su respiración era algo agitada, pero no se movía. Sabía que significaba: estaba teniendo una pesadilla."
    scene habile
    with fade
    show screen modal_example
    n "= LEVI ="
    show screen style_prefix_screen
    play music "Dark Piano.mp3"
    scene lili
    with fade
    call screen style_prefix_screen
    show text "{size=+25}{color=#FFFFFF}*¿Por qué? ¿Por qué tenía que ver esa escena?*{/color}{/size}" at truecenter
    with dissolve
    pause 5
    with flashbulb
    show text "{size=+25}{color=#FFFFFF}*¿Por qué a mí?*{/color}{/size}" at truecenter
    with dissolve
    pause 4
    hide text
    with dissolve
    play sound "impac.mp3"
    scene so1
    with flashbulb
    n "Me cuestionaba mientras me encontraba tirado en el suelo mirando aquellos ojos sin vida de quien yo consideraba mi hermana."
    n "Sentía el cuerpo tenso y no podía formular palabra alguna."
    n "Me atragantaba con mi propia saliva y el aire que respiraba era mínimo, había dejado de funcionar."
    n "Había olvidado cómo respirar, había olvidado hasta mi nombre."
    n "Lo había olvidado todo con solo ver esos ojos muertos y apagados, sin ese brillo característico que me brindaba felicidad y paz."
    n "Se habían ido. Ella se había ido. Mi alma se había ido."
    scene somn
    with flashbulb
    n "Frente a mí tenía al culpable, que tenía en su horrorosa boca al que era mi hermano, metido entre sus dientes arrojándolo al suelo como si de basura se tratase."
    play sound "impac.mp3"
    scene so2
    with flashbulb
    n "El aire ya no entraba a mis pulmones, mi corazón amenazaba con detenerse por cada segundo que veía salir la sangre del cuerpo de mi hermano."
    n "Mis ojos estaban clavados en la terrible escena mientras la tensión de mis músculos me impedía moverme."
    scene lili
    with fade
    show text "{size=+25}{color=#FFFFFF}*Nos abandonaste Levi*{/color}{/size}" at truecenter
    with dissolve
    pause 4
    show text "{size=+25}{color=#FFFFFF}*¿Por qué nos dejaste morir, hermano?*{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    scene cementerio
    with flashbulb
    n "Aquellas voces familiares me trasladaron a un lugar diferente."
    n "Estaba en un cementerio con una piedra gigante que tenía grabada el nombre de mis amigos, de mis hermanos."
    play sound "(Susurros).mp3"
    scene lili
    with fade
    show text "{size=+25}{color=#FFFFFF}*¿Por qué nos dejaste morir, Levi?*{/color}{/size}" at truecenter
    with dissolve
    pause 4
    hide text
    with dissolve
    scene cementerio
    with dissolve
    n "-Volteé a ver mí alrededor buscando a la persona que hablaba-"
    scene lili
    with fade
    show text "{size=+25}{color=#FFFFFF}*Nos abandonaste, hermano...*{/color}{/size}" at truecenter
    with dissolve
    pause 4
    hide text
    with dissolve
    scene cementerio
    with dissolve
    l "¡No!"
    n "-Grité desesperadamente al reconocer aquella voz femenina-"
    scene lili
    with fade
    show text "{size=+25}{color=#FFFFFF}*¿Por qué no llegaste a tiempo?*{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    scene cementerio
    with dissolve
    n "El eco de aquella voz resonaba en todo el lugar. Resonaba dentro de mí causándome dolor de cabeza."
    scene lili
    with fade
    show text "{size=+25}{color=#FFFFFF}*¿Por qué tú no moriste?*{/color}{/size}" at truecenter
    with dissolve
    pause 4
    hide text
    with dissolve
    scene cementerio
    with dissolve
    play sound "corazon.mp3"
    l "¡Lo siento!"
    n "-Grité al aire-"
    l "¡Fue mi culpa!"
    n "-Grité asustado y desesperado-"
    play sound "corriendo.mp3"
    l "¡Yo me equivoqué!"
    n "-Grité corriendo por todo el cementerio con la respiración agitada-"
    play sound "(Susurros).mp3"
    scene lili
    with fade
    show text "{size=+25}{color=#FFFFFF}*Es demasiado tarde, hermano...*{/color}{/size}" at truecenter
    with dissolve
    pause 4
    hide text
    with dissolve
    scene cementerio
    with dissolve
    l "¡No!"
    n "-Grité intentando encontrar a la persona-"
    l "¡Haré lo que sea!"
    l "¡Lo juro!"
    n "-Comenzaba a entrar en crisis-"
    l "¡Por favor!"
    scene dosombras
    with flashbulb
    n "-Grité al visualizar a ambas personas con cuchillos en las manos-"
    scene lili
    with fade
    show text "{size=+25}{color=#FFFFFF}*Es demasiado tarde, Levi...*{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    scene cuchillo
    with fade
    n "-Habló oscuramente mi hermano sosteniendo fuertemente el cuchillo acercándose a mí-"
    l "¡No!"
    l "¡Espera!"
    n "-Le rogaba desesperado mientras me echaba hacia atrás-"
    n "-Mientras levantaba el cuchillo frente a mi cara-"
    play sound "Mikasalimit.mp3"
    scene lili
    with fade
    show text "{size=+25}{color=#FFFFFF}*Adiós, hermano...*{/color}{/size}" at truecenter
    with dissolve
    pause 3
    hide text
    with dissolve
    with flashbulb
    with hpunch
    scene habileb
    with fade
    play music "Sad Piano.mp3"
    n "Me levanté de golpe de la cama, mí respiración era agitada."
    n "Mi cuerpo temblaba, mis ojos miraban a la nada."
    n "Toqué mi pecho con dificultad, cerciorándome de que no tenía clavado nada. El miedo recorría mi cuerpo."
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    scene cuchillo
    with flashbulb
    n "La desesperación se apoderaba de mi respiración, la angustia de mi mente, el recuerdo de lo que acababa de ocurrir me atormentaba."
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    scene somn
    with flashbulb
    n "Necesitaba ayuda, mi medicina, mi calmante, necesitaba alejarme de ese miedo, olvidar ese sueño."
    scene ho
    with fade
    n "Sentí como alguien me tomaba de las manos y las apretaba."
    n "Con dificultad giré mi vista hacia esa persona, ella, me miraba con un rostro totalmente pálido y muy preocupado."
    scene img13
    show mkasa
    with dissolve
    m "Levi..."
    n "-Su dulce voz entró en mi cabeza mientras la miraba a los ojos-"
    m "Tranquilo..."
    m "¡Estoy contigo, no éstas solo, aquí estoy yo!"
    n "-Me decía mientras apretaba mis manos con fuerzas-"
    n "No podía pronunciar palabras, estaba petrificado del miedo, de la desesperación, de la angustia."
    n "Tan sólo la miré a los ojos, odiaba verla así, verla con otra cara que no fuera la suya."
    n "Estaba pálida y sus expresiones me demostraban que estaba sufriendo por mi culpa."
    n "Apreté sus manos con desesperación mientras me mordía los labios, mi respiración agitada comenzaba a bajar pero lo recuerdos y palabras no desaparecían."
    n "Me encontraba en un estado en donde no sabía que pensar ni que hacer."
    scene ho
    with dissolve
    n "Me sentía débil e inútil. Me sentía una presa sencilla que podía ser cazada por cualquiera. Me sentía la persona más frágil del mundo."
    n "La parte contraria de lo que aparentaba ser estaba rota y la persona que no quería que lo viera, veía la peor parte de mí."
    n "Me odiaba a mí mismo en ese momento. Solté sus manos y agarré mi pecho."
    n "Me dolía, me dolía todo. Aquellas sensaciones de culpa que tanto ocultaba salían a la luz en forma de lágrimas."
    scene lili
    with fade
    n "Mi cuerpo temblaba sin que pudiera parar. Cerré los ojos mientras sentía que mis fuerzas se iban."
    scene img13b
    show abrazo2
    with fade
    n "De pronto, una calidez extraordinaria se hizo presente."
    n "Una luz en medio de la oscuridad alumbraba el camino que debía seguir, su voz me llamaba y me pedía que regresara con ella."
    m "¡Levi!"
    n "-Escuché gritar mi nombre-"
    n "Abrí tan solo un poco los ojos. La tensión de mi cuerpo se había ido."
    n "Sentía una extraña calidez sobre mi cuerpo y mi respiración agitada se calmaba con el pasar de los segundos."
    n "Los latidos de mi corazón se sincronizaban con otro, comenzaba a dejarme llevar por esa cálida sensación de paz."
    n "Fue entonces que lo comprendí: ella, aquella chica, me estaba abrazando con fuerza."
    n "Me pegaba con desesperación a su cuerpo y me rodeaba con sus brazos."
    n "La cercanía de nuestros cuerpos hacía que mi corazón imitará el latido del suyo. Mi respiración se tranquilizaba al respirar su aroma, su fragancia."
    n "Sentía como me apretaba con fuerza mientras sentía como su cuerpo temblaba; lloraba, sentía como sus lágrimas caían en mi hombro desnudo."
    n "Aún no estaba en mis cinco sentidos, pero debía de admitir que la sensación era relajante."
    n "Tenerla a mi lado me había calmado sin necesidad de aplicar la medicina, esa era la respuesta, esa era la razón, ella, solo ella, era mí medicina."
    l "Lo... siento..."
    n "-Pronuncié una vez que pude recobrar las palabras-"
    m "Idiota..."
    n "-Me contestó mientras me abrazaba con más fuerza soltando más lágrimas-"
    n "No recuerdo cuánto tiempo fue que nos quedamos de esa manera, pero realmente le estaba agradecido."
    n "Jamás tendría cómo pagárselo. Nunca pensé que alguien más llegaría a verme en mis peores momentos."
    n "Me culpaba a mí mismo por meterla en algo que no le correspondía, además..."
    n "(¿Por qué estaba llorando?)"
    n "(¿Por qué me estaba ayudando?)"
    n "(¿Por qué ella estaba ahí cuando todo esto sucedió?)"
    scene habile
    with dissolve
    play sound "puerta.mp3"
    n "El sonido de la puerta abriéndose de golpe me hizo girar a ver quién era; no quería que nadie interrumpiera nuestro momento, quería estar a solas con ella."
    play sound "haleviu.mp3"
    show Hange alegre s
    with dissolve
    z "¡Levi!"
    n "-Escuché a mi amiga loca gritar-"
    show Hange sorprendida2 s
    with dissolve
    z "¿Pero qué diablos pasó?"
    n "-Su cara cambió a una pálida al verme tan débil y vulnerable-"
    l "Hange..."
    n "-Pronuncié su nombre con dificultad, era de las pocas veces que la llamaba así-"
    show Hange preocupada s
    with dissolve
    n "Pareció entender, ya que su rostro cambió por completo a uno de terror y preocupación."
    z "Tranquilo... Ahora mismo procedo con la medicina."
    n "-Le escuché decir mientras la metía en una jeringa-"
    show Hange seria s
    with dissolve
    z "Todo va a estar bien, Levi."
    n "-Decía nerviosa mientras se acercaba a mí con la jeringa en mano-"
    hide Hange seria s
    with dissolve
    scene lili
    with fade
    n "Cerré los ojos."
    n "Quería evitar ver el momento en el que introduciría la aguja en mi brazo y soltaría el líquido. Solo recordar la sensación ya me causaba escalofríos."
    m "¡No!"
    m "¡No lo hagas!"
    m "¡Lo vas a lastimar!"
    n "-Escuché sus gritos cuando ya estaba acostado en la cama-"
    m "¡Por favor, Hange!"
    m "¡Déjalo tranquilo!"
    n "-Gritaba mientras se ponía casi encima de mí-"
    n "(¿Por qué te preocupas tanto por mí?)"
    n "(¿Por qué lloras y gritas por defenderme?)"
    z "Mikasa... Levi necesita su medicina... Si no se la doy se pondrá peor... Por favor..."
    n "-Ahora la que imploraba era Hange aguantándose las ganas de llorar-"
    n "(¿Por qué ambas lloraban por mí culpa)"
    n "Yo no valía nada en este mundo, yo no significaba nada para nadie, no entendía por qué luchaban por mí."
    scene habileb
    with dissolve
    m "¿Me lo prometes?"
    n "-Le preguntó comenzando a limpiar sus lágrimas de su bello rostro-"
    z "Te lo prometo."
    n "-Contestó mi amiga acercándose a mí y levantando mi brazo-"
    z "¡Tranquilo, Levi, estarás mejor con esto!"
    n "-Me dijo mientras inyectaba la medicina-"
    scene lili
    with fade
    n "El mareo comenzó inmediatamente, mi cuerpo se desvanecía por completo."
    n "Mi mente comenzaba a cerrarse, comenzaba a desparecer de este mundo, al final solo las vi a ambas llorando."
    n "Hange era alguien realmente loca y obsesionada con titanes, pero alguien muy confiable."
    n "Fue de las únicas personas que se quedó a mi lado a pesar de ser un asco de persona, podría considerarla mi amiga."
    n "Era alguien que me dolería mucho perder, alguien en quien realmente podía confiar y acudir en casos como este en donde yo no podía solo."
    n "Mikasa era aquella chica que me tenía loco, que realmente admiraba su valentía y poder como soldado."
    n "Amaba todo de ella: su cuerpo, sus ideas, sus metas, sus caricias y sus ganas de nunca rendirse."
    n "Aquella chica de cabello azabache y ojos grises brillosos me había cambiado."
    n "Me había demostrado que no le importaba que tan patán, malo, seco, serio, agresivo e indiferente llegará a ser."
    n "Ella sacaba mi lado más oculto, más tierno, más compasivo..."
    n "Ella sabía cómo lidiar conmigo, cómo tratarme, cómo hacerme sentir mejor, cómo molestarme, cómo excitarme, cómo enamorarme..."
    n "Sí... si las tontas historias que me había contado mi madre eran ciertas..."
    n "Entonces, yo estaba enamorado, enamorado de ella; lo que significaba que para mí ella lo era todo y yo desearía su bien por encima del mío."
    n "Yo buscaría su felicidad a cualquier precio, porque para mí era la mujer perfecta."
    play sound "ne.mp3"
    z "Tendrás que decirle la verdad."
    n "-Escuché apenas audible la voz de Hange susurrando en mi oído-"
    n "(Lo haré)"
    show screen style_prefix_screen2
    n "-Le contesté en mis pensamientos antes de caer rendido por efecto de la medicina."
    call screen style_prefix_screen2
    l "..."
    call screen modal_example
    show pasillo3dia
    with fade
    n "Salí de aquella habitación por órdenes de Hange."
    n "Ella me prometió que él estaría bien."
    n "Confiaba en ella, después de todo, ella lo conocía y por eso había sabido cómo actuar."
    n "(Si tan sólo hubiera sabido que se administraba medicina)"
    n "-Me reproché a mí misma mientras salía del edificio y me iba al campo-"
    show campo
    with dissolve
    play music "As the Day Ends.mp3"
    n "Estando afuera intenté calmarme y olvidarme de lo que había pasado."
    n "Yo solo había ido para calmar mis sensaciones, para verlo otra vez, pero no estaba en mis planes tener que calmarlo de una pesadilla."
    n "El aire frío anunciaba que ya se acercaba el otoño."
    n "Tomé la bufanda y me tapé parte del rostro para cubrirme del frío y para percibir el dulce aroma de Levi impregnado en ella."
    n "Levanté la vista al cielo, despejado, de un color azul pastel."
    $contador = 0
    python:
        ErenAmizade += 27
    call chamarBarraMais(ErenAmizade)
    with dissolve
    show Eren normal s
    with dissolve
    e "Mikasa..."
    n "-Escuché una voz pronunciar mi nombre-"
    e "¿Podemos hablar?"
    m "Dime..."
    n "-Contesté sabiendo de quién se trataba-"
    show Eren preocupado s
    with dissolve
    e "Lo siento."
    e "No era mi intención herirte de esa manera. Mi pésima actitud me hizo alejar a varias personas importantes para mí, tú incluida."
    n "-Comenzó a hablar sin miedo, directo a lo que iba, yo solo lo escuchaba-"
    show Eren incomodo s
    with dissolve
    e "Yo siempre me quejé de que me molestaba que estuvieras a mi lado..."
    e "Me molestaba que me cuidaras tanto y no me dejarás solo, pero ahora entiendo porque lo hacías..."
    n "-Eren hablaba cabizbajo mientras jugaba con sus dedos-"
    show Eren preocupado s
    with dissolve
    e "¡Lo más importante para mí en este mundo sois Armin y tú!"
    n "-Gritó llamando mi atención volteándolo a ver-"
    show Eren llorando s
    with dissolve
    e "¡Por eso no puedo darme por vencido!"
    e "¡Los salvaré a todos de este infierno e iremos los 3 juntos a conocer el mar!"
    n "-Gritó con lágrimas en los ojos-"
    play sound "eren.mp3"
    m "Eren..."
    n "-Pronuncié su nombre asombrada por sus revelaciones-"
    e "Mikasa... sé que todo lo que te hice estuvo mal."
    e "Y estás en todo tu derecho de odiarme y apartarme de tu vida..."
    e "También tienes derecho a meter a quien quieras en ella y tienes derecho a volver a vivir..."
    n "-Hablaba en serio mientras se destruía por dentro-"
    e "Pero quiero decirte que conozco los sentimientos que tienes por mí..."
    n "-Quedé petrificada-"
    show Eren incomodo s
    with dissolve
    e "Y yo solo...."
    menu:
        "¡No!":
            show Eren preocupado s
            with dissolve
            python:
                ErenAmizade -= 8
            call chamarBarraMenos(ErenAmizade)
            n "-Exclamé callándolo-"
            m "¡No lo digas!"
            n "-Le pedí agachando mi cabeza-"
            show Eren incomodo s
            with dissolve
            m "¡Sí, te perdono!"
            m "¡Pero no acepto tus sentimientos!"
            hide screen barraAmizade
            e "¡¿Qué?!"
            n "-Exclamó sorprendido sin dejar de mirarme-"
            show Eren serio s
            with dissolve
            m "No más..."
            n "-Respondí sintiendo una punzada en el pecho-"
            jump fg

        "¡Basta, Eren!":
            show Eren preocupado s
            with dissolve
            python:
                ErenAmizade -= 10
            call chamarBarraMenos(ErenAmizade)
            show Eren incomodo s
            with dissolve
            e "Pero es la verdad... yo quiero corresponder esos sentimientos... por eso yo..."
            n "-Grité harta de escucharlo-"
            m "¡Estás equivocado!"
            hide screen barraAmizade
            n "-Exclamé dando pasos hacia atrás-"
            m "Te perdono..."
            e "¡¿Qué?!"
            n "-Exclamó sorprendido sin dejar de mirarme-"
            m "¡Sí, te perdono!"
            n "-Le recalqué aún a cierta distancia-"
            show Eren preocupado s
            with dissolve
            m "¡Pero no acepto tus sentimientos!"
            m "No más..."
            n "-Respondí sintiendo una punzada en el pecho-"
            show Eren enojado2 s
            with dissolve
            e "¿Pero qué te pasa?"
            e "¿No quisiste esto siempre?"
            e "¡¿Que yo llegará y te diera el sí?!"
            n "-Reclamó cambiando su actitud-"
            show Eren preocupado s
            with dissolve
            m "¡Sí, eso es lo que quería hace mucho!"
            n "-Le contesté de la misma manera-"
            m "¡Pero ya no más. Te olvidé Eren, te dejé de amar hace mucho...!"
            n "-Grité de golpe-"
            jump fg

label fg:
    show Eren enojado3 s
    with dissolve
    e "¿¡Acaso hay alguien más!?"
    e "¿Acaso los rumores de Hange eran ciertos?"
    n "-Preguntó recordando lo que me había dicho Sasha por la mañana-"
    show Eren enojado2 s
    with dissolve
    e "¡Contéstame, Mikasa!"
    e "¿Es cierto?"
    n "-Volvió a preguntar a punto de explotar-"
    show Eren incomodo s
    with dissolve
    m "¡Sí!"
    m "¡Hay otra persona!"
    m "¡No quiero que lo arruines!"
    n "-Grité harta y con ganas de llorar-"
    m "¡Es mi tercera oportunidad de nacer y comenzar de cero!"
    n "-Lo miré con odio apretando los dientes-"
    show Eren preocupado s
    with dissolve
    e "No puedo creerlo..."
    n "-Pronunció después del shock-"
    show Eren incomodo s
    with dissolve
    e "Mikasa, tú..."
    show Eren serio s
    with dissolve
    m "Solo me di cuenta de mis errores, Eren."
    m "Estando a tu lado me perdí en este mundo y es ahora que puedo verlo por completo."
    n "-Le mencioné siendo honesta-"
    m "¡Y la tercera vida me mostró a las personas con las que puedo contar, a las que realmente me valoran a su lado y las que yo elegí para cuidarlas!"
    show Eren normal s
    with dissolve
    m "Quiero regresar a nuestra amistad de hermanos..."
    m "aquella en la que te estoy totalmente agradecida por haberme salvado..."
    m "pero que cada quien comience sus vidas por diferentes lados y con las personas que quiera."
    m "¿Está bien?"
    n "-Le pregunté mirándolo con indiferencia-"
    show Eren preocupado s
    with dissolve
    e "Está bien..."
    n "-Contestó dando un suspiro de resignación-"
    show Eren normal s
    with dissolve
    e "Nos vemos, Mikasa..."
    hide Eren normal s
    with dissolve
    n "-Terminó regresando al cuartel a paso lento-"
    n "Me quedé un rato más analizando todo lo que acaba de pasar en el día."
    n "Sin duda había sido un día donde muchas cosas habían ocurrido por algo."
    n "Primero el entrenamiento."
    n "Tras revisar el comandante Erwin mi informe, supuso que la mejor idea era esquivar a esos titanes y evitar la lucha contra ellos."
    n "Era un gran punto a favor, pero nada aseguraba que eso nos protegería de esos monstruos."
    n "Segundo."
    n "Las palabras sinceras y honestas de Eren me habían calado hasta los huesos."
    n "Realmente su arrepentimiento era extremo y debía de admitir que ya no aguantaba mucho tiempo sin hablarle a la persona que me había salvado la vida."
    n "Lo había perdonado de corazón a pesar de cómo me había tratado porque realmente lo quería y apreciaba mucho."
    n "Me alegraba infinitamente saber que nuestra amistad regresaría a ser la de siempre."
    n "Tercero."
    n "Jamás había visto así a Levi: solo, triste, desesperado, agonizando, con miedo y terror en su máxima expresión."
    n "Sabía que no había hecho nada por él, tan solo lo había abrazado por impulso."
    n "Sentí que algo me había movido para hacerlo, el recuerdo de mis padres se reflejaron en sus ojos apagados y negros."
    n "Había perdido su identidad en ese momento, había dejado de ser él."
    n "Me di cuenta de que quería estar a su lado, quería saber el motivo de sus caídas y golpes duros como este."
    n "Quería saber que lo atormentaba por las noches."
    n "Quería saber el por qué de su enfermedad."
    n "Quería saber las razones y motivos por los que aparentaba ser una persona dura cuando no lo era."
    n "Algo dentro de mí se encendió y me quemaba: el recuerdo fugaz de su figura muerta me causó escalofríos. Temía perderle tal y como aquél día."
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    show titanassei
    with flashbulb
    r "... Arlert mencionó que actuaste así después de ver a Levi herido."
    r "¿Es ese el po rqué de tu comportamiento y acciones, Ackerman?"
    scene campo
    with fade
    n "Las palabras del comandante regresaron a mi cabeza mientras la imagen de aquel día también se dibujaba en mi mente."
    n "Yo había salvado a Levi de diferente manera a la que lo había hecho con Armin."
    n "Un ardiente odio al titán que lo había lastimado había tomado posesión de mí y lo había matado de la peor manera posible."
    n "¿Por qué?"
    n "Por miedo a perderle, por miedo a perder a una persona importante en mi vida."
    show lili
    with dissolve
    show text "{size=+25}{color=#FFFFFF}¡¿Acaso hay alguien más?!{/color}{/size}" at truecenter
    with dissolve
    pause 4
    hide text
    with dissolve
    scene campo
    with dissolve
    n "Ahora las palabras de Eren retumbaban en mi cabeza"
    n "Sí, lo que le había dicho era cierto."
    n "Yo ya no sentía nada por él, tan solo un enorme agradecimiento por haberme salvado aquel día."
    n "Pero nada más, aquel sentimiento se había ido y aquellas extrañas sensaciones que sentía por él, ahora las sentía por alguien más."
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    scene miri
    with flashbulb
    a "...Amor: el que sientes por otra persona, normalmente del genero opuesto..."
    a "Una atracción y el deseo de estar a su lado y pensar que es la persona perfecta..."
    scene campo
    with dissolve
    n "Las palabras de Armin rebotaron ahora en mi cabeza."
    n "Revolvía mis ideas. Ese amor del que hablaba por otra persona podría asegurar que era el que sentía hace mucho por Eren."
    n "Pero ya no más, ahora todas esas sensaciones las sentía con alguien más."
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    show beso
    with flashbulb
    s "Espero que el rumor del que habló la señorita Hange él otro día haya sido mentira..."
    s "Ya sabes... que tú y el capitán Levi se ven a escondidas para andarse besando..."
    scene campo
    with dissolve
    n "Las palabras de Sasha también entraron en mi cabeza reordenando mis ideas."
    n "No era mentira, no del todo."
    n "Debía admitir que mi relación con Levi era extraña porque no sabíamos cómo actuar, nos daba miedo y vergüenza."
    n "Pero era cierto que siempre que estábamos solos sentíamos que vivíamos en otro mundo."
    n "El choque de nuestros labios era mágico y especial, nos hacía sentir libres y que estábamos destinados a ser uno solo."
    n "Volteé a ver al cielo con determinación mientras el viento jugaba con mis cabellos y la bufanda desprendía su olor."
    n "Había llegado a una conclusión: las cosas pasaban por algo."
    n "El entrenamiento y las palabras de Eren no habían sido casualidad, estaban predestinadas a suceder de una manera u otra."
    n "Esbocé una sonrisa mientras miraba al cielo."
    n "Lo admitía, aquellos chismes de los soldados y los rumores de Hange no eran rumores."
    n "¡Eran ciertos! Mi relación con Levi no era mentira. ¡Era real!"
    m "Qué molesto..."
    n "-Dije al aire sin borrar la pequeña sonrisa que se asomaba en mis labios-"
    m "Estoy enamorada de ti, Levi..."
    n "-Me dije a mi misma perdiendo todo mi orgullo."
    n "Acababa de aceptar que mi destino siempre fue estar a su lado."
    n "De alguna u otra manera nos encontraríamos y crearíamos nuestro propio destino."
    show lili
    with dissolve
    show text "{size=+25}{color=#FFFFFF}Capitulo 7{/color}{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}FIN{/color}{/size}" at truecenter
    with dissolve
    pause 0
    hide text
    with dissolve
    $persistent.cap8 = True
    return

label capitulo8:
    play music "The Lie.mp3"
    show text "{size=+25}{color=#FFFFFF}Capítulo 8{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}Nuevos sentimientos{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    show screen quick_menu
    with dissolve
    show lili
    with fade
    show tarven
    with fade
    n "Después de ir al comedor a tomar mis alimentos de la mañana, me dirigí al cuarto de Levi."
    show pasillo2
    with dissolve
    n "Él se encontraba casi totalmente recuperado y pronto podría salir de ese cuarto."
    n "Caminaba lento, el único ruido que resonaba era el rechinar de mis botas con cada paso que daba."
    n "-Llevaba mis manos detrás de mi espalda mientras tarareaba una canción-"
    n "La canción que mi madre solía cantarme cuando las cosas parecían ir mal, aquella triste canción donde me pedía no rendirme..."
    n "ya que yo era una pequeña flor en pleno crecimiento."
    $ variable = _("{i}Solo el brote de la flor que conoce el dolor{/i}")
    n "[variable!t]..."
    $ variable = _("{i}Colorea los bordes de la esperanza{/i}")
    n "[variable!t]..."
    $ variable = _("{i}Flor, que floreció con lágrimas{/i}")
    n "[variable!t]..."
    $ variable = _("{i}¿No eres tan hermosa?{/i}")
    n "[variable!t]..."
    n "Aquella canción solo podía ser entendida si se hablaba el idioma oriental de mi madre y yo la aprendí gracias a ella."
    n "Entendía a la perfección el significado de aquella canción y cuando la cantaba, la presencia de mi madre renacía dentro de mí."
    show pasillo3dia
    with fade
    play sound "corazon.mp3"
    n "Sin darme cuenta había llegado a la puerta, la miré un momento mientras intentaba calmar las típicas sensaciones que se hacían presentes en mí."
    n "-Solté un suspiro para relajarme y tomé la perilla para después parar en seco al oír voces provenientes dentro del cuarto-"
    pe "¡Por favor coma todos sus alimentos capitán!"
    n "-La voz de una chica me hizo acercarme a la puerta para escuchar mejor-"
    l "No necesito que me lo digas Petra."
    l "No tenías que venir aquí por mí..."
    pe "¿Tiene algo de malo que su subordinada esté preocupada por usted capitán?"
    n "-La escuché preguntar algo triste-"
    l "No, gracias."
    n "-Habló con honestidad, sentí una punzada en el pecho-"
    pe "Levi...podría..."
    n "Un infinito silencio se hizo presente."
    n "Aquel silencio me carcomía por dentro, las risillas de aquella chica de cabello rojizo me estaban provocando las ganas de tirar la puerta."
    n "No aguanté más, y con la mayor delicadeza abrí la puerta"
    scene img14
    with fade
    n "Quedé con la boca abierta, Petra se encontraba recostada sobre el pecho de Levi con una brillante sonrisa."
    n "Sentí algo dentro de mi romperse para después quemarse en un ardiente fuego."
    n "Aquella escena me destrozaba por dentro."
    n "La sensaciones que tenía en un principio desaparecían."
    n "La emoción que tenía se desvanecía al ver la inocente y brillante sonrisa de Petra en los brazos del hombre que me había cargado, abrazado y besado."
    show ohno
    with dissolve
    pe "¿Mikasa?"
    n "-La escuché pronunciar mi nombre extrañada y sonrojada-"
    pe "¿Qué haces aquí?"
    show habile
    with fade
    n "-Preguntó separándose de Levi mientras agachaba la cabeza-"
    m "Nada..."
    n "-Respondí apenas recuperé la voz-"
    show Levi normal2 s
    with dissolve
    play sound "Mikasadelevi.mp3"
    l "Mikasa"
    n "-La voz de él me causó escalofríos en todo el cuerpo haciéndome reaccionar-"
    show Levi preocupado s
    with dissolve
    l "¿Estás bien?"
    n "-Me preguntó mirándome algo extrañado-"
    m "Si...lamento interrumpir..."
    n "-Hablé mientras cerraba con fuerza mis puños y mordía mis labios-"
    m "¡Con permiso!"
    hide Levi preocupado s
    with dissolve
    show pasillo3dia
    with dissolve
    n "-Exclamé tomando con brusquedad la perilla para salir de aquella habitación azotando la puerta detrás de mí-"
    n "Sentía un terrible ardor correr por todo mi cuerpo, unas infinitas ganas de golpear lo primero que se me cruzará en el camino."
    show pasillo6
    with fade
    play music "Dream.mp3"
    n "-Paré en seco mirando el fondo del pasillo-"
    n "-Bajé la mirada rendida mientras aguantaba con todas mis fuerzas las ganas de llorar-"
    n "Comencé a relajarme, miré el piso desconcertada mientras divagaba en otro lugar en mi mente."
    n "¿Qué me estaba pasando?"
    n "¿Por qué había actuado de esa manera?"
    n "¿Qué fue lo que realmente me había provocado aquellos impulsos de ira?"
    show Annie llorando s
    with fade
    n "Un pequeño sollozo me sacó de mis pensamientos provocando que levantará la vista en uno de los balcones de las torres del edificio."
    play sound "annie.mp3"
    m "¿Annie?"
    n "¿Estás bien?"
    n "-Le pregunté acercándome a su lado-"
    n "-Bajó la mirada al piso mientras mordía sus labios-"
    play sound "consuelo.mp3"
    m "Si hay algo que pueda hacer...dímelo, ¿Vale?"
    scene img14b
    show madre
    with fade
    n "Sus manos temblaban, una de ellas sostenía una carta arrugada y maltratada."
    n "-Se hizo un silencio incómodo y triste-"
    n "Annie realmente ha cambiado mucho, era una chica fría, arrogante y siempre permanecía distante."
    n "En ese aspecto se parecía a mí de cierta manera."
    n "Pero, se ha convertido en una chica débil, frágil y sentimental, todo lo contrario a lo que solía ser."
    n "Era la primera vez que alguien lloraba en mi pecho."
    n "Recuerdo que cuando era niña, solía llorar en los brazos calidos de mi madre hasta quedarme dormida."
    n "Una pequeña sonrisa se asomó en mi boca, ahora era yo la que interpretaba el rol de madre."
    n "-Acaricié su suave cabellera rubia-"
    n "Siempre he odiado ver a las personas débiles. En este mundo se nos enseñaba a ser fuertes de una u otra manera."
    n "Pero yo no era la indicada para decir tal cosa."
    n "Hace unos minutos, acabé en un estado de ira, sin saber exactamente la razón de mi comportamiento y también había tenido ganas de desahogarme."
    show pasillo6
    with fade
    show Armin hablando s
    with dissolve
    a "¡Mikasa!"
    n "-La voz jadeante de Armin me hizo levantar la vista-"
    a "¡Qué bueno que te encuentro!"
    show Armin serio s
    with dissolve
    m "¿Qué sucede Armin?"
    n "Armin se quedó un momento en silencio, fijaba su suave mirada en Annie y ella en él."
    n "Su choque de miradas les hizo entenderse mutuamente que se hablarían pronto, me alegraba saber que Annie también contará como apoyo a Armin."
    show Armin hablando s
    with dissolve
    a "¡El comandante Erwin quiere verte!"
    a "¡Es sobre la siguiente expedición!"
    show Armin disgustado sce
    with dissolve
    n "-Recalcó mostrando un semblante de preocupación-"
    m "¡Voy enseguida!"
    hide Armin disgustado sce
    with dissolve
    show Annie feliz s
    with dissolve
    $contador = 0
    python:
        AnnieAmizade5 += 65
    call chamarBarraMais5(AnnieAmizade5)
    with dissolve
    n "-Le respondí mirando de reojo a Annie, quien solo me brindó una tierna sonrisa-"
    m "cuídala..."
    hide Annie feliz s
    with dissolve
    n "-Le pedí a Armin antes de bajar por las escaleras-"
    show pasillo3dia
    with dissolve
    n "Caminé a paso veloz por los pasillos hasta llegar a la oficina del comandante Erwin."
    play music "Psycho.mp3"
    play sound "toc toc.mp3"
    n "-Tomando un poco de aire toqué la puerta anunciado mi presencia-"
    play sound "puerta.mp3"
    r "¡Adelante!"
    show oficina
    with fade
    show Hange alegre s
    with dissolve
    z "¡Mikasa!"
    z "¡Qué bueno que llegas...te hemos estado buscando!"
    show Hange seria s
    with dissolve
    n "-Se colocó aún lado del comandante con un semblante más serio-"
    m "¿Qué sucede?"
    hide Hange seria s
    with dissolve
    show Errwin normal sba
    with dissolve
    r "La siguiente expedición será dentro de 2 días."
    play sound "misi.mp3"
    r "Pero, antes de contestarme, creo que deberías comprender mejor lo que implican nuestras misiones."
    r "Los entrenamientos que tuvieron hace semanas, se basaron en una táctica de escape en caso de encontrarnos con esos titanes nuevamente."
    play sound "vencer.mp3"
    r "Si podemos aumentar la efectividad de los entrenamientos de todo el Cuerpo, lo normal sería que la tasa de mortalidad disminuyese sola."
    show Erwin normal1 s
    with dissolve
    n "-Colocó sus manos cruzadas sosteniendo su mentón-"
    show Erwin incomodo1 s
    with dissolve
    r "Sin embargo si esos titanes llegan a emboscarnos..."
    r "¡Nos matarán a todos!"
    show Erwin incomodo2 s
    with dissolve
    n "-Término en un tono frío y tenebroso a la vez-"
    hide Erwin incomodo2 s
    hide Erwin normal1 s
    hide Erwin incomodo1 s
    hide Errwin normal sba
    with dissolve
    show Hange seria s
    with dissolve
    z "De acuerdo a tu informe nos dimos cuenta que la mejor opción es evitar luchar contra ellos."
    z "Sin embargo, al poseer cierta inteligencia, es seguro que nos persigan."
    play sound "evit.mp3"
    z "¿Acaso hay otra manera de evitarlos?"
    n "-Preguntó al aire golpeando con sus puños el escritorio-"
    n "Guardé silencio bajando mi mirada, intente buscar alguna alternativa, ninguna, no había forma de salir con vida de aquellos monstruos."
    hide Hange seria s
    with dissolve
    show Erwin normal1 s
    with dissolve
    r "La situación es simple..."
    n "-El comandante volvió a hablar haciéndome levantar la vista-"
    r "Esta expedición no fue encomendada personalmente por mí."
    m "¿Qué?"
    m "Quiere decir..."
    m "¿Qué usted no organizó esta expedición?"
    show Erwin incomodo1 s
    with dissolve
    r "Así es, fue Zackley y la realeza. Se nos pidió que saliéramos y descubriéramos más de aquellos titanes, quieren recibir nueva información."
    show Erwin incomodo2 s
    with dissolve
    n "-Resopló molesto-"
    $contador = 0
    python:
        HanjiAmizade3 += 53
    call chamarBarraMais3(HanjiAmizade3)
    with dissolve
    m "¡Eso es un suicidio!"
    m "¿¡Acaso está bien salir de los muros y que muera gente con tal de traer nueva información!?"
    play sound "esperanza.mp3"
    show Erwin normal s
    with dissolve
    r "Como seguro ya sabes, el cuerpo de exploración es la unica esperanza de la humanidad."
    show Erwin incomodo2 s
    with dissolve
    r "Es por el bien de la humanidad."
    n "-Contestó secamente bajando la mirada-"
    hide Erwin incomodo2 s
    hide Erwin normal s
    hide Erwin incomodo1 s
    with dissolve
    n "Bufé molesta ya que no podía faltarle el respeto, no me quedaba de otra que aceptar sus órdenes pero no podía aceptar lo inhumano que era el objetivo."
    show Hange insegura s
    with dissolve
    z "Mikasa, necesitáremos tu ayuda."
    z "Ya que pudiste enfrentarte a ellos, serás capaz de proteger al pequeño grupo del que estarás a cargo."
    n "-Mencionó con una sonrisa forzada-"

    menu:

        "¿Por qué?":
            python:
                HanjiAmizade3 += 14
            call chamarBarraMenos3(HanjiAmizade3)
            show Hange seria s
            with dissolve
            n "-Pregunté aún molesta-"
            z "Tu equipo será el de observación..."
            n "-Dijo sacando unos papeles-"
            hide screen barraAmizade3
            with dissolve
            z "Estará conformado por 10 personas incluyéndote."
            n "-Volteó a verme fugazmente para regresar a ver los papeles nuevamente-"
            show Hange preocupada s
            with dissolve
            z "Entre ellos Armin y Sasha."
            n "-Mordí mi labio inferior y cerré con fuerza mis puños-"
            jump tru


        "...":
            python:
                HanjiAmizade3 -= 8
            call chamarBarraMenos3(HanjiAmizade3)
            hide Hange insegura s
            with dissolve
            show Erwin normal1 s
            with dissolve
            r "Sé que es algo difícil Ackerman."
            hide screen barraAmizade3
            with dissolve
            n "-Mencionó el comandante al no ver respuesta de mi parte-"
            hide Erwin normal1 s
            with dissolve
            show Hange seria s
            with dissolve
            z "Tu equipo será el de observación..."
            n "-Dijo sacando unos papeles-"
            z "Estará conformado por 10 personas incluyéndote."
            show Hange preocupada s
            with dissolve
            z "Entre ellos Armin y Sasha."
            n "-Cerré con fuerza mis puños-"
            n "Me frustraba la idea de perderlos."
            n "No quiero volver a vivir ese dolor de perderlo todo."
            jump tru

label tru:
    n "Un leve escalofrío recorrió mi cuerpo, la imagen de mis dos amigos aparecieron en mi mente."
    n "Ambos estarían conmigo en una experiencia suicida que nadie sabría cuál podría ser el resultado."
    n "Imaginarme lo peor sería perderlos frente a mis ojos."
    n "Mí misión es protegerlos, tal y como lo había dicho Hange."
    n "Pero si fracasaba en mi misión, mis amigos desaparecerían de mi vida."
    n "Con solo imaginarme sus caras pálidas y sus ojos sin vida me erizaba la piel."
    hide Hange preocupada s
    with dissolve
    show Errwin normal sba
    with dissolve
    play music "Most Beautiful.mp3"
    r "Ackerman, al igual que usted, me encuentro frustrado de no saber los resultados ni las consecuencias."
    r "Espero contar con su apoyo por más difícil que sea la situación..."
    show Erwin normal1 s
    with dissolve
    n "-Término colocándose de pie y viendo fuera desde la ventana-"
    n "Lo miré un momento y aprecié como él también estaba angustiado."
    n "El comandante también sabía que esa expedición podría ser la última para los que íbamos a ir."
    n "Pero él siempre mantenía la compostura de un líder, y eso era una de las cosas que más admiraba de él."
    m "¡Cuente conmigo!"
    m "Aunque sea mí última expedición seguiré sus órdenes."
    n "-Confesé realizando el saludo militar y comencé a retirarme-"
    $contador = 0
    python:
        ErwinAmizade6 += 50
    call chamarBarraMais6(ErwinAmizade6)
    with dissolve
    play sound "oir.mp3"
    show Erwim feliz s
    with dissolve
    r "Me alegra oírte decir eso."
    hide Erwin normal1 s
    hide Erwim feliz s
    hide Errwin normal sba
    with dissolve
    show Hange feliz s
    with dissolve
    n "-Esbozó una pequeña sonrisa, Hange hizo lo mismo pero me dirigió unas últimas palabras-"
    show Hange gi1 s
    with dissolve
    z "Levi quiere hablar contigo."
    show Hange alegre s
    with dissolve
    n "-Dió una risita burlona antes de que cerrará la puerta y saliera de la oficina-"
    hide Hange alegre s
    with dissolve
    play sound "puerta.mp3"
    scene pasillo3dia
    with dissolve
    n "Había terminado por hacerme sentir peor mentalmente."
    n "Mi mente intentaba acomodar todas las sensaciones nuevas que había sentido hasta ahora."
    n "Ira, pero no cualquiera, un enojo específico a aquella escena."
    n "Tristeza, al abrazar a Annie y miedo de perderlo todo de nuevo."
    n "Angustia, por no sentirme capaz de cumplir mi misión."
    n "Pérdida en mis pensamientos regresé de nuevo a aquella puerta en la cual, dentro de ese cuarto, había pasado un momento que jamás olvidaría."
    play sound "puerta.mp3"
    scene habileb
    with dissolve
    n "-Tomé con fuerza la perilla y me adentré en el oscuro cuarto-"
    n "Sentí la mirada penetrante de Levi y con desgano me senté en la silla que había a su lado, recordando que ahí había estado Petra."
    n "-Crucé mis brazos y fruncí el ceño mirando a otro lado-"
    m "¿Qué quieres hablar conmigo?"
    n "-Pregunté en el tono más seco y tosco que tenía-"
    show lili
    with fade
    show screen modal_example
    n "=LEVI="
    show screen style_prefix_screen
    play music "Moonlight Forever.mp3"
    scene habileb
    with fade
    play sound "puerta.mp3"
    n "-El ruido de la puerta abrirse provocó que volteará a ver quién entraba-"
    call screen style_prefix_screen
    show Mikasa normal s
    with dissolve
    n "Me emocioné en cuanto la vi."
    n "En cuanto logré divisar su figura y su hermoso rostro, sentí miles de sensaciones extrañas en todo el cuerpo."
    show Mikasa enojada2 s
    with dissolve
    n "Pero..."
    n "Desde la mañana cuando había entrado, había actuado diferente. Se veía molesta y enojada."
    n "La conocía a la perfección y sabía qué hacía los mismos gestos que yo, estaba molesta por algo."
    show Mikasa enojada3 s
    with dissolve
    m "¿Qué quieres hablar conmigo?"
    show Mikasa enojada s
    with dissolve
    n "-Preguntó de la manera más seca y apagada que jamás había escuchado de ella-"
    n "-La miré un momento para ver su rostro fruncido-"
    n "Sus brazos cruzados y su mirada puesta en otro lado significaba que no quería verme."
    n "Quería evitarme y sin embargo había venido a verme y se encontraba sentada al lado de mi cama."
    l "¿Estás molesta?"
    n "-Le pregunté en mi típico tono serio e indiferente-"
    show Mikasa enojada3 s
    with dissolve
    m "¿Por qué razón habría de estar molesta?"
    show Mikasa enojada s
    with dissolve
    n "-Preguntó en el mismo tono mordiendo uno de sus labios-"
    l "Tu carácter lo dice todo."
    n "-Le contesté mirándola fijamente-"
    show Mikasa enojada2 s
    with dissolve
    m "Yo siempre he sido así capitán."
    n "-Contestó amargamente-"
    l "¿No te dije que me llamaras por mi nombre cuando estuviéramos solos?"
    n "-Reafirmé molesto ante sus actitudes–"
    show Mikasa enojada3 s
    with dissolve
    m "¿Acaso soy la única que te dice por tu nombre?"
    m "¿O hay otra persona que también pueda decirlo?"
    show Mikasa enojada s
    with dissolve
    n "-Subió el tono de su voz apretando los dientes mirándome con recelo-"
    l "¿De qué diablos estás hablando?"
    n "-Pregunté sin entender a qué se refería comenzando a fastidiarme-"
    m "Creo que sabe a qué me refiero."
    n "-Contestó sin inmutarse en la misma postura con el mismo tono-"
    l "¡Tus actitudes son tan infantiles Mikasa!"
    n "-Le dije con la mirada más fría de todas-"
    l "¿Qué diablos te pasa?"
    l "¿Qué tanto te molesta?"
    n "-Pregunté elevando el tono de mi voz mientras me acercaba a ella-"
    show Mikasa enojada3 s
    with dissolve
    m "¡Yo no soy infantil!"
    show Mikasa enojada s
    with dissolve
    n "-Se quejó defendiéndose a sí misma regresándome la mirada-"
    show Mikasa enojada3 s
    with dissolve
    m "¡Si tenías visitas en la mañana me hubieras avisado y no habría interrumpido su momento juntos!"
    show Mikasa enojada2 s
    with dissolve
    n "-Gritó molesta girando su vista a otro lado mientras apretaba sus puños y dientes-"
    n "Me quedé sorprendido ante su respuesta, ¿así que esa era la razón por la que estaba molesta?"
    n "Su rostro mostraba una parte sonrojada mientras mantenía el ceño fruncido y los brazos cruzados."
    n "Mordía sus labios por incomodidad y miraba hacia la nada, solté un suspiro."
    hide Mikasa enojada2 s
    with dissolve
    scene img15
    show celosa
    with dissolve
    l "¿Estás celosa?"
    n "-Le pregunté en un tono burlón pero sin cambiar mi facción del rostro-"
    m "¿Ah?"
    n "-Contestó sorprendida y nerviosa cambiando todas sus facciones totalmente-"
    n "Se veía realmente tierna, nerviosa y totalmente sonrojada."
    n "Sus ojos nuevamente brillaban con el reflejo de la luz, el color rosa de sus labios volvía, aquellos gestos que siempre tomaba regresaban de nuevo."
    m "¡No estoy celosa!"
    n "-Contestó torpemente intentando ocultar lo avergonzada que estaba-"
    m "¿Por qué habría de estarlo?"
    n "-Preguntó nerviosa bajando la mirada-"
    l "Porque te molestó que Petra estuviera aquí..."
    n "-Tomé su mentón con cuidado para que volteará a verme-"
    l "¿No es así?"
    n "-La miré a los ojos mientras nuestras miradas chocaban-"
    m "No..."
    n "-Contestó mientras intenta ocultar su rostro sonrojado-"
    n "*Realmente adorable*"
    n "-Pensé mientras la seguía mirando-"
    scene habile
    with dissolve
    show Mikasa sonrojada1 s
    with dissolve
    l "Solo vino a traerme el desayuno."
    l "Me tiene un gran respeto por haberla rescatado hace tiempo, eso es todo."
    show Mikasa triste s
    with dissolve
    n "-Terminé sin rodeos mientras la miraba-"
    n "Bajó su mirada cambiando a un semblante triste."
    n "Sus mejillas aún tenían ese color rojo claro, sus ojos comenzaban a apagar ese brillo único mientras su rostro se entristecía, odiaba verla de esa manera."
    m "Me siento...estúpida por eso."
    n "-Dijo sin cambiar su postura-"
    show Mikasa sonrojada2 s
    with dissolve
    l "No pienses de esa manera..."
    n "-Acaricié suavemente su mejilla-"
    n "Aceptó mi gesto con gratitud tomando con su mano la mía sin despegarla de su mejilla."
    show Mikasa triste s
    with dissolve
    n "Había logrado que se calmara, quería borrar ese triste rostro de ella y cambiarlo por el original."
    n "El de ella, el que me volvía loco y me hacía pensar cuán bella era."
    m "Lo siento, actúe de una forma tan estúpida que y..."
    scene img15b
    show beso3
    with dissolve
    n "-La callé de un beso en los labios-"
    n "No necesitaba disculparse, entendía su preocupación y me enloquecía saber que se preocupaba por mí de esa manera."
    n "La pegué más a mi cuerpo para después acariciar su rostro con suavidad."
    n "Amaba la sensación de placer que solo ella lograba despertar en mí, su aroma me enloquecía."
    n "Nos separamos por falta de aire, esta vez tomamos distancia."
    scene habile
    with fade
    show Mikasa sonrojada2 s
    with dissolve
    n "Le brindé una media sonrisa, ya que había conseguido lo que quería, ella bajó la mirada sonrojada, estaba avergonzada pero de cierta forma le había gustado."
    l "¿Aún sigues molesta?"
    n "-Le pregunté sarcásticamente sin borrar mi sonrisa-"
    show Mikasa sonrojada1 s
    with dissolve
    m "Cállate..."
    n "-Respondió avergonzada ocultando su rostro en la bufanda-"
    n "Levanté la vista y me puse de pie en dirección a la ventana."
    show Mikasa normal s
    with dissolve
    n "Sus ojos voltearon a verme, miraba con indiferencia el paisaje exterior, solté algunos suspiros mientras me cruzaba de brazos."
    m "¿Te sientes mejor?"
    n "-Le escuché preguntar preocupada-"
    l "Iré a la expedición dentro de dos días."
    n "-Contesté sin rodeos, sin cambiar mi vista-"
    show Mikasa triste s
    with dissolve
    play music "Sad Piano.mp3"
    m "Ojalá hubiera sido otra respuesta..."
    n "-Respondió dando un suspiro recostando su cabeza en la cama-"
    n "Volteé a verla extrañado por su respuesta, bajé mis brazos y me acerqué a ella sentándome en el borde de la mesa, tomé una de sus manos con delicadeza."
    m "No podré protegerlos..."
    n "-Su tono disminuyó notablemente, la angustia y el terror en su rostro se hacían presente a mayor escala-"
    m "Armin, Sasha y mi grupo...si no lo hago, ellos..."
    n "-Apretó con fuerza las sábanas de la cama-"
    n "Acaricié su cabeza suavemente mientras la veía con tristeza."
    n "No era más que una soldado novata con excelentes habilidades y poder, pero también era humana."
    n "Mis dedos se enredaban con su suave y sedoso cabello azabache, el olor se desprendía cuando jugaba con el."
    n "-Levantó la vista suavemente para verme sin inmutarse-"
    show Mikasa normal s
    with dissolve
    m "¿Cómo le hace?"
    m "¿Cómo logra ser tan buen capitán?"
    l "No hay un método para serlo."
    n "-Le contesté recargándome sobre mis brazos hacia atrás-"
    l "Yo tampoco me considero un capitán honorable."
    n "-Confesé mirándola a los ojos-"
    show Mikasa hablando s
    with dissolve
    m "¡Pero todo el mundo lo respeta, es fuerte y sabe tomar las mejores decisiones en el momento!"
    l "Tuvo que haber algo detrás para que lograra hacer eso..."
    hide Mikasa hablando s
    with dissolve
    scene habileb
    with dissolve
    n "-Me arrepentí de haber tocado el tema, un dolor inmenso comenzó a crecer en mi pecho mientras mi respiración se agitaba-"
    m "¡Levi!"
    n "-Se sentó a mi lado tomando mi mano-"
    m "¿Qué sucede?"
    n "-Preguntó atónita mientras le veía con preocupación-"
    l "La medicina..."
    n "-Hablé con dificultad mientras apretaba con fuerza la parte de mi pecho-"
    n "Se levantó de golpe y corrió a la pequeña mesa tomando consigo una botella de cristal pequeña."
    n "Se volvió a acercar y sacó dos pastillas extendiéndomelas mientras me arrimaba un vaso con agua."
    n "Tomé las pastillas y dando un largo suspiro me recargué en el respaldo de la cama, mientras intentaba recuperar mis sentidos y fuerzas."
    show Mikasa triste s
    with dissolve
    l "Lo siento..."
    n "No contestó, bajó la mirada mientras apretaba sus manos, no podía ver su cara, la cubría con su cabello."
    n "Su sonrisa había desaparecido y el sonrojo también."
    n "Estaba cabizbaja mientras intentaba calmarse, recuerdo haberla visto de la misma manera aquél día que también presenció mi ataque de nerviosismo."
    l "Es la segunda vez que me ves de esta manera..."
    n "-Intenté explicar, pero mi voz se quebraba con cada palabra-"
    l "Lo siento..."
    n "-Volví a decir bajando mi rostro, maldiciéndome por lo que había sucedido-"
    n "-Sentí como tomó una de mis manos con delicadeza mientras se inclinaba aún cabizbaja-"
    play sound "sorry.mp3"
    m "Lo siento..."
    n "-Dijo apretando mis manos con fuerza y levantando su rostro-"
    m "Quiero saber qué es eso que te atormenta..."
    n "Agradecía su preocupación, un calor interno se hizo presente dentro de mí mientras la miraba."
    n "Realmente le preocupaba, la hacía llorar y preocuparse, me cuidaba y me protegía sin que se lo pidiera."
    n "Hablaba conmigo sin juzgarme y prefería pasar sus días libres a mi lado."
    n "Yo no merecía tener a una mujer así de perfecta a mi lado, alguien podría llegar a ser el afortunado, pero definitivamente no sería yo."
    l "¿Por qué te preocupas tanto por mí?"
    n "-Respondí temiendo la respuesta-"
    n "Todo dependería de su respuesta, todo dependería de ella, yo no la merecía."
    n "Sin embargo ella siempre estaba a mi lado, si ella decidía quedarse la amaría para toda la vida, porque eso era lo que sentía por ella."
    n "Una obsesiva atracción por una mujer tan perfecta como ella, pero si ella se iba..."
    n "Me resignaría a saber que no era más que un alma sin vida viviendo entre los vivos."
    hide Mikasa triste s
    with dissolve
    scene img16
    show te amo
    with dissolve
    m "¡Quiero conocerte, saber más de ti, estar a tu lado!"
    n "-Exclamó mientras lágrimas se plasmaban en su fino rostro-"
    play sound "llorando mikasa 2.mp3"
    m "Levi..."
    n "-Volteé a verla sorprendido-"
    m "yo..."
    n "-Se quedó callada mientras un leve sonrojo se hacía presente en su rostro-"
    play sound "llorando mikasa 1.mp3"
    n "No había porque temer ni porque dudar."
    n "Aquella mujer me pedía a gritos que me quedará a su lado, que conviviéramos más para conocernos más a fondo."
    n "Que nos quedáramos juntos para compartir cada una de esas caricias y esos besos."
    n "Aquella hermosa chica me aceptaba aún sin conocerme del todo y quería intentarlo, quería ir lejos."
    scene habileb
    with fade
    n "Y yo también quería intentarlo."
    n "La necesitaba, aquellas sensaciones desbordaban al límite de mi ser cada que la veía."
    n "Sabía que aquello no era normal, pero me gustaba sentirlo y más cuando veía su delicado rostro."
    n "Aquella brillante y única sonrisa y aquellos ojos relucientes que solo me miraban a mí y a nadie más."
    n "Nos miramos a los ojos avergonzados por nuestra atrevida confirmación de que necesitábamos estar juntos para vivir."
    n "Porque no era una casualidad o un hecho a propósito, ella y yo nos habíamos conocido por algo."
    n "Ella y yo debíamos conocernos más por algo, ella y yo debíamos estar juntos por algo."
    n "-Nos abrazamos-"
    n "La cálida sensación de la unión de nuestros cuerpos era gratificante, era un momento solo para nosotros."
    n "Solo podíamos sentirnos libres en esos momentos, podíamos sentir como si solo estuviéramos nosotros solos en este mundo cruel."
    show screen style_prefix_screen2
    n "Porque las cosas no pasaban de casualidad, siempre había una razón por la que las cosas debían pasar, y eso era llamado DESTINO."
    call screen style_prefix_screen2
    l "..."
    call screen modal_example
    play music "As the Day Ends.mp3"
    show establo
    with fade
    n "Finalmente el día de la expedición había llegado."
    n "En los establos estábamos todos los que formaríamos parte de aquella misión, el ambiente era tenso y causaba escalofríos."
    n "Todos mostraban una expresión de miedo, angustia y preocupación."
    show Shasha Contenta
    with dissolve
    s "¡Estaremos bien Mikasa!"
    s "¡Hemos entrenado muy duro!"
    n "-Las exclamaciones de Sasha me hacían sentir segura y por una parte tranquila-"
    hide Shasha Contenta
    with dissolve
    show Armin feliz c
    with dissolve
    a "Haremos todo lo que nos órdenes Mikasa."
    n "-La voz suave y temerosa de Armin me hicieron brindarle una cálida sonrisa-"
    a "¡Así que no te preocupes por nosotros!"
    hide Armin feliz c
    with dissolve
    n "Ambos se movieron a la posición que nos tocaba mientras hablaban montados en los caballos."
    n "La preocupación no se quitaba de mí ser, pero sabía que debía confiar en ellos y en mí misma para que nada malo pasará."
    show Levi normal c
    with dissolve
    l "¿Estás lista?"
    n "-Su voz me causó un leve escalofrío-"
    m "Eso creo..."
    n "-Contesté volteándolo a ver, ya que se había acomodado a mi lado montado en su caballo-"
    show Levi hablando c
    with dissolve
    l "Tranquila..."
    l "Te prometo que nada malo les pasara, confía en tus habilidades."
    show Levi normal2 c
    with dissolve
    n "-Sonrió mientras acariciaba a su caballo-"
    m "Levi, prométeme que estarás bien y que no te pasará nada..."
    show Levi preocupado c
    with dissolve
    l "Solo sí tú me prometes lo mismo."
    n "-Volteó a verme con cierta mirada preocupada-"
    show Levi normal c
    with dissolve
    l "Aún nos queda una visita a la ciudad pendiente."
    n "-Recordó mientras una pequeña sonrisa se dibujaba en su rostro-"
    m "Lo prometo."
    m "Aún tenemos un pendiente que hacer."
    n "-sonreí-"
    hide Levi normal c
    with dissolve
    show pueblo
    with dissolve
    n "Sin decir nada más, nos fuimos a la formación en nuestros caballos, su presencia me hacía sentir tranquila."
    n "Su aroma impregnado en mi bufanda me calmaba y hacía que me sonrojara."
    n "Hace dos días nos habíamos declarado mutuamente que nos amábamos, que necesitamos la presencia del otro para sentirnos libres, completos, en armonía."
    show Erwin normal c
    with dissolve
    r "¡No olviden la importancia de esta misión!"
    r "¡Entreguemos nuestros corazones para la salvación de la humanidad!"
    n "-Los gritos del comandante Erwin rebotaban en todo el lugar-"
    hide Erwin normal c
    with dissolve
    n "-¡Sí!- respondieron los soldados tomando las riendas de sus caballos-"
    show Levi normal c
    with dissolve
    l "Lo siento comandante, pero yo ya le entregué mi corazón a alguien más."
    n "-Volteé a verlo de reojo-"
    show Levi hablando c
    with dissolve
    l "¡Haré todo lo que esté en mis manos para salvar a la humanidad y proteger a la persona que tiene mi corazón!"
    l "¡Adelante!"
    hide Levi hablando c
    with dissolve
    n "-Gritó mientras avanzábamos directo a la puerta que dividía este mundo con el otro-"
    show Errwin normal cba
    with dissolve
    r "¡Tomen sus posiciones!"
    hide Errwin normal cba
    with dissolve
    n "-Ordenó una vez que salimos de los muros-"
    show exterior
    with fade
    n "Rápidamente mis compañeros se acercaron y se acomodaron de acuerdo al plan del comandante."
    n "Armin iría a mi lado para formular estrategias, Sasha y los demás formarían un rectángulo para proteger y vigilar en todos los puntos."
    n "La verdadera misión comenzaba ahora."
    n "Nuestros instintos debían de estar alerta totalmente nuestros ojos y oídos atentos a cualquier señal u sonido."
    n "Debía de guardar mi energía en caso de que la necesitase, una vez dentro del territorio enemigo ya no había vuelta atrás."
    show Levi normal c
    with dissolve
    l "*Cuídate, Mikasa*"
    m "*Cuídate, Levi*"
    hide Levi normal c
    with dissolve
    n "-Pensamos los dos mientras nos enfocábamos por completo a la misión-"
    show lili
    with dissolve
    show text "{size=+25}{color=#FFFFFF}Capitulo 8{/color}{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}FIN{/color}{/size}" at truecenter
    with dissolve
    pause 0
    hide text
    with dissolve
    $persistent.cap9 = True
    return

label capitulo9:
    play music "Dark Tension.mp3"
    show lili
    with fade
    show text "{size=+25}{color=#FFFFFF}Capítulo 9{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}La muerte{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    show screen quick_menu
    show exor
    with fade
    n "Mi escuadrón estaba en el flanco derecho del equipo principal en el que estaba Levi."
    n "En aquel tétrico lugar respirar se hacía costoso y todo cuanto escuchábamos era el galope de los caballos."
    n "Esta vez yo lideraba y todo el peso de la responsabilidad me mantenía con miedo, pero no lo demostraba."
    n "Armin estaba a mi lado, debía mantener mi postura para no asustarlo más de lo que ya estaba."
    n "Mi misión, además de liderar al grupo, era protegerlo de posibles ataques."
    n "Un extraño presentimiento comenzó a formarse dentro de mí."
    n "Desde que habíamos salido de los muros tenía la horrible sensación de que algo malo iba a ocurrir."
    n "Fallar la misión, que la expedición tuviese otro propósito, que la misión fuese una farsa..."
    n "La preocupación comenzó a crecer considerablemente, al punto de no poder ocultarlo."
    n "Mordí mis labios con fuerza y apreté con miedo las riendas de mi caballo."
    n "¿Acaso era eso con lo que Levi siempre cargaba?"
    n "El color de una bengala amarilla proveniente del otro extremo se dibujó en el cielo."
    n "Ese era el color que usábamos para..."
    s "¡Especie no identificada!"
    m "¡Sigan avanzando! ¡Debemos estar alertas!"
    n "Traté de calmar mi miedo mientras daba la orden."
    show Shasha gritando c
    with dissolve
    s "¡Mikasa!"
    hide Shasha gritando c
    with dissolve
    n "Casi sin aliento, me giré a ver a Sasha, quien estaba totalmente aterrada. Detrás de ella y tres soldados más venía un titán."
    m "¡Armin, lanza la bengala!"
    m "¡Muevanse de ahí!"
    show exoro
    with dissolve
    n "Tarde."
    with hpunch
    n "Un titán atacó a uno de los soldados aplastándolo con su mano y haciendo que su sangre salpicase a todos a su alrededor."
    play sound "grito.mp3"
    n "Quedaron perplejos. Sus gritos retumbaban en mi cabeza y comenzaban a desesperarme."
    n "Armin, habiendo caído presa del miedo, lanzó la bengala torpemente."
    n "Los soldados, pálidos, siguieron mis instrucciones."
    n "Tuve razón al pensar que la misión fracasaría."
    n "No fui capaz de proteger al grupo. Había perdido a un soldado a mi mando y mi cuerpo temblaba de miedo, desesperación y angustia."
    play sound "gritos.mp3"
    n "Los gritos se volvieron a hacer presentes, esta vez más fuertes y atroces."
    n "Me giré y ahí lo vi: otro titán se acercaba a nosotros a gran velocidad."
    show exor
    with dissolve
    m "¡Avancen!"
    n "Aceleré el trote de mi caballo y los demás me siguieron."
    n "Ambos titanes nos seguían a paso veloz."
    n "El grito de una mujer pidiendo ayuda llamó la atención de los demás, que quedaron perplejos al ver cómo el titán la hacía trizas."
    n "Contemplaba los rostros atemorizados, que me impedían pensar con claridad."
    n "Ya había perdido a cuatro bajo mi mando; me sentía culpable y tenía miedo."
    n "Si seguíamos así acabaríamos muertos uno tras otro."
    n "Me dirigí en Armin y Sasha, quienes estaban también aterrados, con intención de contarles un nuevo plan."
    m "Voy a ir a por los titanes. ¡Armin, tú hazte cargo del grupo!"
    show Armin soprendido1 s
    with dissolve
    a "¿Qué? Pero yo no..."
    m "¡Es una orden! Volved a los muros mientras los distraigo."
    a "Mika..."
    show Armin disgustado cce
    with dissolve
    m "Yo doy las órdenes y tú debes obedecer."
    n "Los titanes seguían acercándose con aquellas sonrisas tétricas y sedientas de sangre."
    m "¡Idos ahora! ¡Ya!"
    show Armin enojado sc
    with dissolve
    a "¡Seguidme!"
    show Armin enojado cce
    with dissolve
    n "Agradecí la obediencia de Armin y deseé que se salvasen mientras se alejaban."
    hide Armin enojado cce
    with dissolve
    show paisaje1
    with fade
    n "Cambié de rumbo para tomar un camino distinto al escuadrón y lancé una bengala para llamar la atención de aquellos titanes."
    n "Pedí a mi caballo que me ayudase a salir con vida de esa mientras lo arreaba."
    n "No quería girarme. Escuchaba los pasos de los titanes detrás de mí."
    play sound "viento.mp3"
    with hpunch
    n "Una fuerte ráfaga de viento me azotó. Un titán debía haber intentado darme un manotazo y estuvo cerca."
    show bosque7
    with fade
    play music "Dark Magic.mp3"
    n "Llegué al bosque. Una vez allí, haciendo uso de mi equipo de maniobras, subí a una de las ramas más altas del árbol."
    n "Los titanes comenzaron a trepar y yo saqué las cuchillas preparándome para atacar."
    show movert
    with pushright
    n "Salté sobre la cabeza del titán que más se hubo acercado y me propulsé hasta otra rama."
    n "Estando juntos no podía matarlos, corría el riesgo de que alguno me pillase desprevenida mientras iba a por otro."
    with hpunch
    n "Uno de ellos saltó a la rama donde estaba y esta se partió, haciéndolo caer."
    show movur
    with pushleft
    n "Era mi oportunidad para enfrentarme al otro que me miraba con una sonrisa."
    with hpunch
    n "Me lancé hacia su nuca mientras giraba en el aire."
    m "¡Te tengo! ¡Muere!"
    play sound "stuijm.mp3"
    with hpunch
    scene movert
    with pushright
    n "Corté su nuca con agresividad y empezó a caer mientras se evaporaba."
    show evaop
    with fade
    n "Busque con la mirada al titán que había caído. Estaba mirando al de su especie evaporarse con cara totalmente inexpresiva."
    n "Parecía estar sintiendo algo por su compañero caído."
    n "Estaba inmóvil emitiendo unos sonidos que parecían gritos. Era mi oportunidad para matarlo, pero algo me lo impedía."
    show nile
    with fade
    n "El titán reaccionó. Me miró y se colocó en una posición en que dejaba su nuca desprotegida."
    n "Parecía estar pidiéndome que lo matase. Me lancé a su nuca con cuidado de que no se tratase de una trampa."
    scene movert
    with fade
    play sound "stuijm.mp3"
    n "Lo corté con suavidad y comenzó a evaporarse."
    n "No tenía palabras con las que expresar lo sucedido."
    scene suelo
    with dissolve
    n "Estaba exhausta y mi cuerpo cayó sobre la hierba mientras el dolor de cabeza regresaba."
    scene movert
    with dissolve
    n "Cuando me recuperé me puse en pie y silbé al caballo para que regresase, y así lo hizo."
    show exor
    with fade
    n "De nuevo volvieron a escucharse unos gritos desgarradores provenientes de las profundidades del bosque, a donde me dirigí"
    with hpunch
    scene bosque8
    with fade
    n "De repente el caballo se tropezó y caí al suelo."
    show petead
    with fade
    play music "The Path of Silence.mp3"
    n "Ante mí pude ver una escena que me dejó sin aliento"
    n "La hierba estaba teñida de rojo, y frente a mí estaba aquella soldado de cabello bermejo mirando a la nada con sus ojos color miel ya sin vida."
    n "Aquella sonrisa que un día me había puesto celosa ya no estaba."
    n "El lugar se había vuelto un escenario tétrico y melancólico."
    n "Volví a ver otra escena que me dejó nuevamente la sangre helada."
    scene petea
    with dissolve
    n "Otro de los soldados colgaba de una rama con el cuello roto y la mirada perdida."
    n "En el suelo yacían otros dos soldados cortados por la mitad sobre un enorme charco de sangre."
    n "No podía creerlo: el escuadrón de Levi había sido aniquilado."
    n "Todos esos soldados de élite ahora estaban muertos."
    n "Me acerqué al cuerpo de Petra, me hinqué a su lado y bajé sus párpados mientras recordaba la actitud que había tomado con ella unos días atrás."
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    scene meu
    with flashbulb
    play sound "disculpe.mp3"
    m "Lo siento."
    m "No era mi intención haberte tratado de esa forma..."
    m "De verdad, lo siento."
    show exor
    with fade
    play sound "corazon.mp3"
    n "Levi cruzó por mi mente y mi estómago se revolvió. Los latidos de mi corazón se aceleraron pensando en lo peor."
    n "-Un grito desgarrador hizo que fijara la mirada en un punto-"
    show tit
    with fade
    play sound "Mikasalimit.mp3"
    n "Levi estaba rodeado por titanes a punto de abalanzarse sobre él."
    n "Toda suerte de sentimientos negativos se reunían en mí y paralizaron mi cuerpo."

    menu:

        "¡Levi! ¡No me dejes sola!":
            n "Lágrimas brotaron de mis ojos al gritar."
            jump ps


        "¡Levi!":
            n "Agarré la bufanda con fuerza."
            jump ps

        "¡No te vayas!":
            n "-Escucho mi voz-"
            n "Pero se distrajo, uno de los titanes aprovecho en tomarlo de los pies"
            n "-Volvió a soltar un grito lleno de ira y dolor-"
            m "¡Levi!"
            scene gamne oooo with fade
            pause 3
            with dissolve
            "Levi perdió los pies por mi culpa."
            return


label ps:
    n "-Volvió a soltar un grito lleno de ira y dolor-"
    n "El cabello le tapaba los ojos y no podía ver su mirada."
    n "Estaba volando frente a los titanes sujetando las cuchillas con fuerza."
    scene img16b
    show titanessei
    with fade
    n "Giraba y maniobraba en el aire acabando con los titanes uno a uno con cortes perfectos."
    n "Quedé sorprendida por la habilidad y velocidad con las que se movía, así como por su forma de acabar con los enemigos."
    n "Parecía actuar con odio e ira."
    n "Sus gritos parecían reflejar cierta culpabilidad..."
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    scene img17
    show recuerdo
    with flashbulb
    l "Debo pedirte un favor."
    m "¿Qué sucede?"
    l "Si llego a perder el control..."
    l "¡Detenme!"
    m "¿A qué te refieres?"
    l "Tan solo prométemelo, Mikasa."
    m "Está bien, lo prometo."
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    show titanessei
    with flashbulb
    n "Ahora entendía a qué se refería."
    n "Estaba disfrutando matarlos, eso es algo que el Levi del que me enamoré odiaría."
    n "Estaba actuando sin pensar, algo le había hecho perder la razón."
    play music "Isolation.mp3"
    show lili
    with dissolve
    play sound "pobre mikasa.mp3"
    n "-Me abalancé sobre él y ambos caímos al suelo-"
    show te amo
    with fade
    play sound "llorando mikasa 1.mp3"
    n "Entre sollozos le grité desesperada."
    m "¡Levi, reacciona!"
    play sound "llorando mikasa 2.mp3"
    m "¡Estoy aquí!"
    m "¡Te amo!"
    m "¡Te necesito a mi lado!"
    play sound "llorando mikasa 1.mp3"
    m "¡Por favor!"
    m "¡Levi!"
    scene lili
    with fade
    show screen modal_example
    n "=LEVI="
    show screen style_prefix_screen
    n "Mi cuerpo se sentía pesado y tenía dificultad para respirar."
    call screen style_prefix_screen
    n "Estaba rodeado de vapor y sangre fresca."
    scene img17b
    show notevayas
    with dissolve
    n "-Agaché la cabeza y la vi-"
    l "Mikasa..."
    m "Levi...¿has regresado a ser tú?"
    l "Yo...lo siento."
    n "Negó con la cabeza mientras me abrazaba fuertemente de nuevo."
    m "¡Levi, de verdad que lo siento mucho!"
    m "Lo siento."
    n "Su voz se quebraba al hablar. Ocultó su rostro con la bufanda y se acurrucó sobre mi pecho."
    n "Sabía que lloraba por mi culpa."
    n "Me había tenido que detener al perder el control. Al perder al escuadrón me había vuelto a pasar como cuando perdí a mis hermanos."
    n "Acaricié su cabeza entrelazando mis dedos con su cabello sintiendo no poder hacer más en esa situación."
    n "Hange me comentó que en los momentos de fuertes impactos despertaba en mí algo que hacía que doblase mi fuerza y perdía la razón."
    n "Por eso me había preparado aquella medicina que me ayudaba a calmar esas extrañas reacciones."
    n "Por desgracia no siempre funcionaba."
    n "Cada vez que dormía soñaba con dolorosos recuerdos que me atormentaban."
    n "Miré al cielo aguantándome las ganas de llorar, no quería hacerlo frente a Mikasa."
    n "Sus lamentos y lágrimas me llegaban hasta el alma."
    n "Sé que era fuerte y, sin embargo, ahí estaba llorando en mis brazos."
    n "Un nudo en la garganta me impedía decirle que ya estaba todo bien."
    m "Levi..."
    m "No vuelvas a hacer eso."
    l "Mikasa..."
    m "¡No quiero volver a quedarme sola! ¿No te lo había dicho?"
    n "Apretó con fuerza mi camisa y cerró nuevamente sus ojos aún llorosos. Acaricié su cabeza y respondí lo único que puede."
    l "Lo siento."
    n "Era mi culpa. Actué sin tenerla en cuenta."
    scene bosque8
    with fade
    show Hange sorprendida2 c
    play music "As the Day Ends.mp3"
    with dissolve
    z "¡Levi! ¡Mikasa! ¿Estáis bien?"
    hide Hange sorprendida2 c
    with dissolve
    show Mikasa normal c
    with dissolve
    m "Estoy bien."
    n "-Mikasa se puso en pie mientras se frotaba la cara intentando disimular las lágrimas-"
    m "¿Dónde están los demás?"
    hide Mikasa normal c
    with dissolve
    show Hange hablando c
    with dissolve
    z "Los supervivientes están con Erwin, están regresando a los muros."
    z "¿Y tu escuadrón, Mikasa?"
    hide Hange hablando c
    with dissolve
    show Mikasa hablando c
    with dissolve
    m "Ordené que volvieran a los muros. Si han logrado escapar, ya deben haber llegado."
    hide Mikasa hablando c
    with dissolve
    show Hange normal c
    with dissolve
    z "Está bien, será mejor que nos vayamos nosotros también."
    n "-Ambos asentimos mientras ella hostigó al caballo partiendo antes que nosotros-"
    hide Hange normal c
    with dissolve
    show Mikasa normal c
    with dissolve
    m "Levi."
    n "-Volteé a verla. Me estaba mirando fijamente a los ojos-"
    show Mikasa hablando c
    with dissolve
    m "Cuando regresemos, ¿visitaremos la ciudad?"
    show Mikasa normal c
    with dissolve
    l "¿Sigues queriendo salir conmigo después de todo?"
    show Mikasa sonrojada2 c
    with dissolve
    m "Sí. Prometí que te detendría y lo hice. ¡Pero tú también me hiciste una promesa!"
    n "Entrelazó nuestros dedos. Seguía sonriendo después de todos los disgustos que le causaba."
    l "¿Por qué sigues a mi lado? No puedo entender tus razones."
    m "Porque te amo, no necesito otro motivo."
    n "-Me besó tras pronunciar esas palabras-"
    n "Cuando nuestros labios se separaron limpió las lágrimas que resbalaban por mi rostro con sus suaves manos."
    show Mikasa feliz c
    with dissolve
    m "¿Necesito otro motivo?"
    n "Para mí ella era realmente perfecta."
    n "Sin importar qué tan mala fuera la situación, ella sabía cómo calmarme."
    n "Una chica tan perfecta como ella no podía estar al lado de un hombre como yo."
    show Mikasa triste c
    with dissolve
    m "Es la primera vez que te veo llorar."
    show Mikasa hablando c
    with dissolve
    m "No lo ocultes. Si quieres llorar, hazlo."
    m "Si no quieres que alguien te vea puedo cubrirte, pero no te aguantes las ganas."
    hide Mikasa hablando c
    with dissolve
    scene img18
    show sad
    with dissolve
    n "Me abrazó y apretó mi cabeza contra su pecho."
    n "Lloré todo lo que me había guardado por mucho tiempo."
    n "Dejé que saliera toda la culpa que había cargado conmigo y me aferré a Mikasa como un niño que busca la protección de su madre."
    n "Su mano acariciando mi cabeza y espalda, era tranquilizante."
    n "No sé cuánto tiempo debió haber pasado, pero en algún momento me volví a sentir libre de toda carga y las lágrimas cesaron."
    scene bosque8
    with fade
    show Mikasa feliz c
    with dissolve
    m "¿Nos vamos?"
    show Mikasa sonrojada1 c
    with dissolve
    n "Asentí y agarré su mano. Se sorprendió de que lo hiciese y yo sonreí."
    hide Mikasa sonrojada1 c
    with dissolve
    scene exor
    with dissolve
    n "Alcanzamos a Hange. En la carreta llevaba algunos cuerpos que había logrado rescatar."
    scene exterior
    with dissolve
    n "Fuimos en completo silencio durante el camino de vuelta. La misión había fracasado y muchas vidas se habían perdido."
    show Mikasa enojada c
    with dissolve
    n "Mikasa sujetaba con fuerza las riendas de su caballo. Sus ojos mostraban preocupación y se mordía fuertemente los labios."
    so "¡Muros al frente!"
    n "-Mikasa alzó la cabeza y, mirando al frente, aceleró el paso-"
    hide Mikasa enojada c
    with dissolve
    n "Se la notaba preocupada por sus compañeros."
    n "Las puertas comenzaron a abrirse a medida que nos acercábamos."
    scene pueblo
    with fade
    de "¡Mikasa!"
    show Shasha Contenta
    with dissolve
    n "Dos voces, aún lejanas, gritaron el nombre de Mikasa y a esta se le dibujó una gran expresión de alivio."
    hide Shasha Contenta
    with dissolve
    show Armin feliz c
    with dissolve
    m "¡Armin! ¡Sasha!"
    n "Me alegra que estéis bien."
    show Armin hablando c
    with dissolve
    a "Eso deberíamos decirlo nosotros, nos tenías preocupados."
    hide Armin hablando c
    with dissolve
    show Shasha Pensando
    with dissolve
    s "¡Tonta!"
    show Shasha gritando c
    with dissolve
    s "Ni se te ocurra volver a hacer una locura como esa por nosotros."
    hide Shasha gritando c
    with dissolve
    show Hange normal c
    with dissolve
    z "Mira todo lo que ha soportado. Es una chica muy fuerte, ¿verdad?"
    n "-Hange me estaba mirando con una sonrisa pícara-"
    show Hange gi1 c
    with dissolve
    z "Qué afortunado de tener a una chica así."
    show Hange insegura c
    with dissolve
    l "¿¡De qué hablas!?"
    show Hange gi2 c
    with dissolve
    z "Cuídala, Levi."
    show Hange normal c
    with dissolve
    n "Me conocía demasiado bien cómo para ocultar lo que sentía. Le devolví una sonrisa tímida y respondí a su encargo."
    l "Prometo que lo haré."
    hide Hange normal c
    with dissolve
    show Mikasa normal c
    with dissolve
    n "Mikasa se me acercó tranquilamente y, antes de que dijese nada, contesté a la petición que me había hecho en el bosque."
    show Mikasa feliz c
    with dissolve
    l "Te veo mañana a las once en el campo de entrenamiento."
    n "Asintió con una sonrisa."
    hide Mikasa feliz c
    with dissolve
    scene sede
    with fade
    n "Partimos a la sede a discutir todo lo que había sucedido."
    n "No paraba de pensar en que Mikasa y yo íbamos a pasar el próximo día paseando por la ciudad, solos y sin interrupciones."
    n "A pesar del fracaso que había sido la misión, aún podía quedarme con eso como algo bueno."
    n "Algo me decía que nuestra relación estaba por cambiar."
    show lili
    with fade
    show text "{size=+25}{color=#FFFFFF}Capitulo 9{/color}{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}FIN{/color}{/size}" at truecenter
    with dissolve
    pause 0
    hide text
    with dissolve
    $persistent.cap10 = True
    return

label capitulo10:
    play music "The Lie.mp3"
    show lili
    with fade
    show text "{size=+25}{color=#FFFFFF}Capítulo 10{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}Nuestro pasado{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    show screen quick_menu
    with dissolve
    show oficina2
    with fade
    n "Armin, Levi, Hange, el comandante y yo estábamos dando la cara por la legión."
    n "Una tenue luz iluminaba la oficina."
    n "Estábamos sentados frente a la realeza, guardando silencio y escuchando quejas estúpidas."
    show Erwin incomodo2 s
    with dissolve
    so "¡Vuestra misión solo era observar a los titanes, y aun así llegáis con una lista de muertos! ¿A qué se debe, Erwin?"
    with hpunch
    n "El soldado agarró de la camisa a Erwin en un tomo amenazante."
    show Erwin incomodo1 s
    with dissolve
    r "Nadie sabía cómo actuarían esas bestias."
    show Erwin incomodo2 s
    with dissolve
    n "Levi agarró con fuerza el brazo de aquel soldado que sostenía la camisa del comandante. Tenía la mirada de una fiera."
    hide Erwin incomodo2 s
    hide Erwin incomodo1 s
    with dissolve
    show Levi enojado sbe
    with dissolve
    l "¡Suéltalo!"
    show Levi enojado s
    with dissolve
    n "El soldado, intimidado, obedeció."
    hide Levi enojado s
    with dissolve
    so "¡No hay justificación para haber tenido tantas bajas!"
    so "¡Desde que es comandante de la Legión de Reconocimiento solo vuelve con listas de muertos, pero ningún descubrimiento!"
    n "El soldado mostró su molestia aventando unas hojas que había sobre la mesa."
    with hpunch
    n "Me harté. Di un golpe en la mesa al levantarme y llamé la atención de todos. La mirada de odio a los soldados era recíproca."
    m "¡No tenéis ningún derecho a reclamar nada!"
    m "¡No habéis salido de estas murallas y habláis sin saber cómo se siente estar ahí afuera!"
    m "¡No tenéis ni idea de lo que sentimos los que tenemos que ver a nuestros compañeros morir delante de nuestros ojos!"
    show Erwin normal s
    with dissolve
    r "Es suficiente, Mikasa."
    n "El comandante apoyó su mano sobre mi hombro mientras pronunciaba aquellas palabras."
    n "Me callé, pero dejé ir un bufido. Volví a sentarme y me crucé de brazos."
    so "Mañana hablaremos con usted más detenidamente, comandante Smith."
    n "Erwin asintió."
    hide Erwin normal s
    with dissolve
    n "-La oficina comenzó a vaciarse-"
    show taberna
    with fade
    n "Yo me fui a mi cuarto, necesitaba descansar y prepararme para el próximo día."
    play music ".mp3"
    scene lili
    with pixellate
    ke "Mikasa, recuerda lo importante que es mantener oculta esta marca en tu brazo."
    m "¿Por qué tengo que esconderla?"
    ke "No a muchos les gusta esta marca que representa a nuestro linaje. Por eso es mejor ocultarla, ¿sí?"
    m "¡Sí, mami!"
    show sue
    with fade
    ke "Hoy es un día especial para papá. ¿Te acuerdas?"
    m "¡Sí! ¡Hoy es su cumpleaños!"
    ke "Shhhh...podría escucharnos."
    ke "¿Me ayudas?"
    m "Claro. ¿Puedo hacer su postre favorito?"
    ke "Por supuesto. Seguro que le encantará."
    scene lili
    with dissolve
    s "Mikasa..."
    s "Mikasa..."
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    stop music
    show taberna
    with flashbulb
    n "Abrí los ojos, aunque con torpeza a causa de la luz que entraba por la ventana."
    show Shasha hablando s
    with fade
    play music "murmurando.mp3"
    s "¡Mikasa!"
    show Shasha Shasha Pensando s
    with dissolve
    m "¿Sasha?"
    n "Aún estaba adormilada y me costaba abrir los ojos, apenas lograba ver su silueta."
    show Shasha hablando s
    with dissolve
    s "Mikasa, ¿estás bien?"
    m "Sí, ¿por qué?"
    s "Estás llorando."
    m "¿Eh?"
    n "Me llevé las manos a los ojos. Estaban mojados. Un reguero recorría mi cara, perdiéndose en mis mejillas y acabando sobre las cobijas."
    s "¿Estabas soñando con algo malo? ¿Tal vez alguna pesadilla?"
    show Shasha feliz s
    with dissolve
    n "Me sequé las lágrimas con el brazo."
    m "No, soñaba con un recuerdo de mis padres."
    show Shasha Contenta s
    with dissolve
    s "Debe ser por eso. Pero no te preocupes, con comida las preocupaciones se van. ¡Ya verás!"
    n "Era increíble cómo siempre lograba levantarme el ánimo. Le sonreí y me puse el uniforme."
    n "Después de cambiarme, salimos al pasillo."
    hide Shasha Contenta s
    with dissolve
    scene tarven
    with fade
    n "El dulce aroma a frutas y miel era presente en todo el comedor."
    n "Los soldados estaban allí sentados en grupos con sus bandejas ya sobre la mesa."
    n "Me senté lo más alejada posible del bullicio de ciertas mesas."
    show Armin feliz s
    with dissolve
    a "Buenos días, Mikasa."
    m "¡Armin!"
    a "¿Puedo acompañarte?"
    m "Eso no tienes ni que preguntarlo."
    n "Hice espacio para que se sentase cómodamente y se sentó a mi lado con una sonrisa."
    show Armin hablando s
    with dissolve
    a "Ayer fue muy agotador. ¿Has podido descansar?"
    show Armin disgustado sce
    with dissolve
    n "Al acabar la frase bostezó."
    m "Parece que tú no has podido descansar. ¿No has dormido?"
    a "No he podido."
    show Armin hablando s
    with dissolve
    a "¿Qué vas a hacer hoy?"
    show Armin serio s
    with dissolve
    m "Lo mismo de siempre, ¿por qué?"
    show Armin disgustado s
    with dissolve
    a "Pensaba que harías algo diferente en tu día libre."
    show Armin serio s
    with dissolve
    m "¿Cómo que día libre?"
    a "El comandante nos dio el día libre para descansar después de aquella expedición. ¿No lo escuchaste?"
    a "Lo dijo ayer antes de salir de la oficina ayer."
    m "No lo recuerdo."
    n "Recordé que me fui antes que nadie por el enfado. Estoy convencida de que ni siquiera llegué a escucharlo por mi vergonzosa actitud."
    n "«Te veo mañana en el campo de entrenamiento a las once.»"
    n "Me sobresalté al acordarme de aquellas palabras."
    m "Armin, ¿qué hora es?"
    show Armin hablando s
    with dissolve
    a "Debe ser cerca de las doce, ¿pero por qué estás tan nerviosa de repente?"
    show Armin serio s
    with dissolve
    m "¡Maldición! ¡Te veo después!"
    hide Armin serio s
    with dissolve
    n "Me levanté y salí corriendo."
    play music "miss the way u played.mp3"
    scene pasteur_day
    with fade
    n "Llegué al lugar donde quedamos en poco tiempo."
    n "Ojeé los alrededores buscando a Levi."
    n "Lo encontré sentado en un tronco mirando el paisaje con su caballo al lado."
    n "El simple hecho de verlo ya me llenaba de felicidad."
    n "Me acerqué con miedo a que me regañase."
    show Levi normal s
    with dissolve
    l "Llegas tarde."
    show Levi tranquilo s
    with dissolve
    l "Pero me alegro de que hayas venido."
    play sound "disculpe.mp3"
    show Levi normal2 s
    with dissolve
    m "Lo siento."
    n "Estaba totalmente avergonzada y no sabía cómo responder a la sonrisa que me había dedicado."
    n "Miré al suelo un poco triste. Me había estado esperando y yo había olvidado que habíamos quedado."
    n "Su mano tocó mi mentón. Me sobresalté."
    n "Alcé la vista y le miré a los ojos. Eran preciosos. Él también me miraba fijamente a los ojos."
    n "Ese cruce de miradas me tranquilizaba y hacía que me enamorase más y más de él."
    show Levi tranquilo s
    with dissolve
    l "¿Nos vamos?"
    m "Vale."
    hide Levi tranquilo s
    with dissolve
    n "Él se subió a su caballo y me ofreció su mano ofreciéndome subir con él."
    n "Me dio vergüenza pensar que alguien pudiese vernos yendo en el mismo caballo."
    n "Levi notó que me había sonrojado y me sonrió. Parecía estarse divirtiendo."
    show Levi feliz s
    with dissolve
    l "No te preocupes, solo seremos tú y yo. Lo prometo."
    hide Levi feliz s
    with dissolve
    n "Acepté su ayuda y me senté detrás de él. Podía sentir su calor y oler su aroma."
    n "Lo abracé por la cintura, encerrando con mis brazos su perfecta figura."
    n "Lo abracé con fuerza. Me recosté sobre su espalda, podía sentir sus latidos."
    scene erat
    with fade
    play music "Isolation.mp3"
    n "Estaba tan absorta en mis pensamientos, abrazada a la persona que amaba, que no me di cuenta de que habíamos llegado."
    n "Levanté la mirada y me encontré con un lugar de impresionante belleza."
    n "Casas blancas con tejados color café en filas, pequeñas áreas con vegetación, un canal con aguas cristalinas..."
    show Levi normal s
    with dissolve
    l "Esto es solo la entrada. Te encantarán las cosas que hay en el centro."
    hide Levi normal s
    with dissolve
    n "Estaba emocionada por saber qué más vería."
    n "Siguió avanzando por las calles de losas y piedras."
    scene olh
    with fade
    n "Había niños jugando y corriendo allá donde mirase, madres cargando a sus hijos comprando en el mercado, los padres trabajaban en sus talleres..."
    n "Era un paisaje idéntico al lugar donde solía vivir."
    n "Bajamos del caballo y comenzamos a caminar. Miraba impresionada cada detalle de la ciudad."
    n "Una enorme fuente en medio de una extensa área verde hacía del centro un lugar hermoso."
    show Levi feliz s
    with dissolve
    l "¿Te gusta?"
    n "Me tomó de la mano mientras miraba ensimismada la fuente."
    menu:
        "Sí, gracias por traerme.":
            python:
                LeviAmizade4 += 15
            call chamarBarraMenos4(leviAmizade4)
            l "No hay de qué, prometí que lo haría."
            n "Tomó mi mano y comenzamos a caminar por el lugar."
            hide screen barraAmizade4
            with dissolve
            jump flly

        "Me da un sentimiento de melancolía.":
            python:
                LeviAmizade4 -= 15
            call chamarBarraMenos4(leviAmizade4)
            hide screen barraAmizade4
            with dissolve
            jump flly

label flly:
    n "La melancolía se apoderaba de mí al vagar por esas calles tan familiares."
    n "Aun así, solo me importaba hacer buenos recuerdos con Levi, sin dejar que el pasado me afectase."
    n "La escena de una niña siendo abrazada por sus padres llamó mi atención."
    n "Recuerdos de mi infancia invadieron mis pensamientos."
    n "Antes de que me diese cuenta, lágrimas empezaron a brotar de mis ojos"
    n "De repente sentí calor."
    n "Unos brazos rodeaban mi cuerpo con delicadeza."
    n "Levi me estaba abrazando. Me apretaba contra su cuerpo mientras acariciaba mi cabeza."
    l "No llores. No me gusta verte llorar."
    m "Lo siento, no era mi intención. Es solo que recordé a mis padres."
    l "¿Qué les ocurrió?"
    n "Guardé silencio. No hablaba con nadie de mi pasado, me dolía. Nunca hablaba de aquella noche en la que lo perdí todo."
    l "Lo siento, no debía haber preguntado."
    m "Fueron asesinados..."
    l "Entiendo, debe ser duro."
    m "No es justo."
    m "¿Por qué mis padres? Solo queríamos ser felices."
    l "Mikasa..."
    l "No sigas."
    n "Limpió mis lágrimas con sus manos."
    n "Me aferré a él con desesperación y dolor. Me había prometido muchas veces no llorar, pero no soportaba el dolor."
    n "Me maldecía por no haber sido yo la que abrió la puerta. Me culpaba por no haber podido hacer nada para salvarlos."
    n "Permanecí un rato en silencio abrazada a él."
    l "¿Estás mejor?"
    m "Levi..."
    m "¿Está bien conocer nuestro pasado?"
    l "¿A qué te refieres?"
    m "Te dije que quería conocerte más. ¿No deberíamos conocer el pasado del otro?"
    n "Estaba cabizbaja y él se quedó en silencio."
    n "Suponía que su pasado también debía ser doloroso, pero quería saber más de él."
    m "Solía vivir en una pequeña cabaña en el bosque."
    m "La razón era porque ciertos grupos de vendedores y secuestradores nos estaban buscando."
    l "¿Vendedores y secuestradores?"
    m "Al parecer tenían cierto interés en mi madre y en mí. Por eso decidieron vivir ocultos en el bosque."
    m "El único que nos visitaba era el padre de Eren, Grisha Jaeger."
    l "¿Entonces ya conocías desde antes al mocoso de Eren?"
    m "No, jamás lo había visto."
    m "A pesar de estar alejados del resto, aprendía cosas básicas como la pesca, la agricultura y la caza."
    m "Ganábamos dinero vendiendo en el mercado nuestras cosechas y bordados que mi madre me enseñó a hacer."
    m "Para mí no había nada más importante que mis padres. Pero ese día todo cambió."
    l "¿Te refieres al día en que se fueron?"
    m "Ese día ayudaba a mi madre con sus bordados. Me decía que esa costumbre se la pasase algún día a mis hijos."
    m "Inocentemente pregunté de dónde venían los hijos, me dijo que preguntase a mi padre."
    m "Él me dijo que le preguntase al doctor cuando fuese a visitarnos."
    m "Recordándolo ahora me hace cierta gracia."
    l "Sí que eras inocente."
    m "¡Cállate!"
    n "Me dio vergüenza haber contado eso."
    m "En ese momento alguien llamó a la puerta."
    m "Mi madre fue a abrir y un hombre desconocido la apuñaló, aunque no murió al momento."
    m "Ella tomó unas tijeras y se abalanzó contra uno de los sujetos que entraron mientras me gritaba que huyese."
    m "Antes de que me pudiese dar cuenta, mi padre ya estaba muerto."
    n "Cerré los ojos, como si tuviese la escena delante y no quisiera verla. Tuve que hacer una pausa."
    m "Aquel hombre remató a mi madre golpeándola con un hacha en la cabeza."
    l "No puede ser… ¿Qué pasó contigo?"
    m "Me golpeó y me desmayé."
    m "Desperté en otro lugar. Los hombres estaban hablando de venderme en el mercado para hacer dinero conmigo."
    m "Tenía las manos amarradas, no podía hacer nada."
    m "Entonces Eren llegó a salvarme. Mató a dos de aquellos hombres y me salvó."
    m "Pero el tercer hombre atrapó a Eren y lo intentó estrangular. Ante aquella situación desperté algún tipo de poder en mí."
    m "Perdí el miedo y maté a aquel hombre con un cuchillo."
    l "¿Qué es ese tipo de poder que despertaste?"
    m "No sé explicarlo muy bien."
    m "Armin dijo que cuando estoy furiosa o preocupada por perder a alguien, actúo de una forma muy salvaje."
    l "Ya veo..."
    m "Eren y el doctor Grisha me aceptaron en su casa y empecé a vivir con ellos; acabé viéndolos como mi segunda familia."
    m "También conocí a Armin, que se volvió mi mejor amigo, y Carla fue como mi madre."
    m "Cuando la perdí mi alma volvió a romperse. He estado cuidando de Eren para no perderlo a él también."
    m "Ahora hay más personas por las que me preocupo y quiero proteger."
    m "Por ejemplo, tú."
    n "Levi entrelazó sus dedos con los míos. Estaba sonrojado."
    m "Ya te conté mi historia. Ahora es tu turno."
    l "Está bien, pero no lo haré aquí."
    n "Levi se dirigió al caballo y yo lo seguí de la mano."
    m "¿A dónde vamos?"
    l "Es un secreto que tienes que prometerme que guardarás."
    m "Lo prometo."
    show screen modal_example
    n "=LEVI="
    show screen style_prefix_screen
    n "Me aterraba lo que ella podría llegar a pensar sobre ese lugar."
    call screen style_prefix_screen
    n "Me asustaba la idea de que me odiara y no quisiera volver a saber de mí."
    n "Comenzaba a dudar sí debía de ir a ese lugar o no."
    n "-Paré en seco justo en la entrada-"
    m "¿Qué es este lugar Levi?"
    l "Mí antiguo hogar."
    m "¿Aquí vivías?"
    n "-Preguntó sorprendida tomando mi mano-"
    l "¿Horroroso verdad?"
    m "Levi."
    m "Mírate quién eres ahora, eso es lo importante."
    n "-Dijo con una sonrisa-"
    n "La preocupación que sentía de que ella se fuera desapareció al mostrarme esa sonrisa."
    n "Sus muestras de cariño me hacían quererla y desearla más a mi lado."
    n "Bajamos con cuidado por la enorme escalera, la tomaba de la mano para guiarla por el camino."
    n "Una vez que bajamos, ella miraba sorprendida el lugar."
    n "-Seguimos caminando-"
    n "Finalmente llegamos a una pequeña casa a la que subías con una escalera, paré en seco."
    m "¿Era este tu hogar?"
    l "Si."
    n "-Sentí una horrible nostalgia-"
    n "Cuando me di cuenta Mikasa ya estaba subiendo las escaleras con cuidado, una vez llegó a la puerta volteó a verme y la miré sorprendida."
    n "Esbozó una sonrisa para después abrir la puerta y entrar, subí para alcanzarla."
    n "-Mí cuerpo se tensó y caí al piso-"
    m "¿Levi qué sucede?"
    n "-Preguntó corriendo a mí lado-"
    m "Lo siento, actúe precipitadamente y sé qué esto no es fácil para ti."
    n "-Bajé la mirada sin poder decir nada-"
    n "Ahora entendía lo difícil que había sido para ella contarme su pasado, ella sí era valiente."
    m "No es necesario que me lo cuentes aquí, es más, sí no quieres hacerlo, no lo hagas."
    n "-Dijo hincándose a mí lado tomando mis manos-"
    m "Es más difícil contarlo en el lugar qué viviste..."
    m "así qué podemos dejarlo para después."
    l "Mikasa, yo..."
    n "No Levi, por favor no te lastimes de esa manera..."
    n "-Suplicó acariciando mi rostro suavemente-"
    n "Lo había olvidado, Mikasa me había visto en mi peor forma por falta de la medicina."
    n "Me había visto llorar y al final consolado"
    n "Creía que sólo alguien como Hange podría ser la única que viviría eso conmigo y guardaría el secreto."
    n "Pero, Mikasa también estuvo siempre ahí, desde el pequeño momento en que comenzamos a tratarnos."
    n "*No la merecía*"
    n "Mikasa no podía ser mía por lo que más deseara en el mundo."
    #"Cuídala Levi"
    n "Lo admito, estoy loco por ella."
    n "No puedo dormir por pensar en ella, me molesta verla con otros hombres."
    n "Adoro cada una de sus expresiones y me encanta el roce de sus labios sobre los míos."
    n "Admiro su belleza y sus habilidades, simplemente me encanta todo de ella, la amo."
    l "Aquí viví con dos amigos que llegué a considerar mis hermanos."
    n "-Comencé a relatar después de mi reflexión, Mikasa me miró sorprendida-"
    l "En esta casa los bautice como mis hermanos sin que sé los dijera."
    n "-Miré con nostalgia el lugar tomando su mano y entramos a la casa-"
    m "¿Jamás se los dijiste?"
    n "-Preguntó sentándose en un sillón-"
    l "Supongo que llegaron a intuirlo, ya qué hicimos muchas cosas juntos"
    n "-Respondí sentándome a su lado, esbocé una pequeña sonrisa al recordarlos-"
    l "Mi hermano era Farlan y mi pequeña hermana era Isabel."
    l "Nos conocimos porque querían aprender a usar el equipo de maniobras y sentirse libres estando en este pobre lugar."
    #"-Miré el techo recordando nuestros deseos-"
    m "¿Sentir qué volaban como las aves?"
    l "¿Cómo lo sabes?"
    n "-Pregunté sorprendido ya que había adivinado nuestro mayor sueño-"
    m "Intuición."
    m "Cuando era niña, quería volar como las aves y alcanzar a mis padres en el cielo, ese era mi mayor deseo."
    l "Ya veo, tu sueño era muy cercano al de Isabel."
    n "-Le dije con una sonrisa melancólica-"
    l "Supongo que la mayoría sueña en volar y sentirse libre-"
    m "Tú también llegaste a soñarlo ¿o no?"
    m "¡Compartías el mismo sueño que tus hermanos!"
    l "Supongo que sí."
    l "A Farlan lo conocí después de una pelea callejera, habían asesinado a su pequeño hermano y querían matarlo."
    l "Lo salvé y como agradecimiento decidió seguirme, se convirtió en mi amigo y mi hermano mayor"
    n "-Relaté con nostalgia mirando toda la habitación-"
    m "Ya veo."
    l "A Isabel la conocí cuando era perseguida por las patrullas que cuidaban la escalera y multaban a todo aquél que se atrevía a subirlas sin permiso."
    l "Farlan y yo la protegimos, quiso quedarse con nosotros para aprender a usar el equipos de maniobras, se convirtió en nuestra hermana menor."
    l "No me quejaba de la vida, después de que aquél sujeto me dejará solo..."
    n "-Me molestó recordarlo-"
    m "¿Quién?"
    l "Kenny."
    n "-Pronuncié su nombre con cierto rencor-"
    l "Fue el hombre que me crió después de que mi madre muriera a causa de una enfermedad, me enseñó movimientos de defensa y ataque."
    l "Un día, me dejó solo, a mi suerte, tuve que llevar acabo sus tácticas y enseñanzas. Gracias a eso logré sobrevivir aquí."
    m "¡Entonces ha de ser alguien hábil para que te enseñara todos sus movimientos!"
    l "Lo es, pero no sé nada de él desde entonces."
    n "-Confesé con cierta culpa, le quería agradecer todo-"
    l "Cuando comencé a vivir con mis hermanos me sentía vivo de nuevo, hasta que recibimos una misión secreta..."
    m "¿Una misión secreta?"
    l "El hombre que manejaba la escalera de este lugar, nos ofreció un lugar en la superficie."
    l "Con la condición de que matáramos al comandante de la legión de reconocimiento."
    m "¿¡El comandante Erwin?!"
    n "-Asentí-"
    l "Aceptamos el trato y nos dejamos atrapar para entrar a la legión, utilizaríamos nuestra primera expedición para matarlo."
    n "-Solté un suspiro y continúe-"
    l "Fuí yo quien decidió matarlo, dejando a mis hermanos atrás, el peor error que pude cometer."
    l "Ese día estaba lloviendo, un titán excéntrico los había atacado y devorado cuando yo llegué al lugar."
    n "-Me apretó la mano mientras me veía preocupada-"
    l "Tuve la misma sensación que tú..."
    l "Actúe de la misma forma salvaje que en el bosque."
    l "Me dejé llevar por la ira y la culpa por la muerte de mis hermanos mientras despedazaba a aquel titán para finalmente llorar."
    m "Levi..."
    l "En pocas palabras fue lo mismo que con mí escuadrón..."
    m "¡...!"
    l "Erwin me dió unas palabras de aliento y decidí seguirlo sin importar."
    l "Entonces conocí a Hange y a Mike que se volverían mis amigos cercanos, igual que Erwin."
    l "Erwin me colocó como capitán de tropa formando mi propio escuadrón...nunca he podido hacer nada bien solo."
    l "Necesito la ayuda de los demás para salir adelante, y eso te incluye a ti."
    n "-La miré con tristeza y culpa-"
    m "¡No Levi, nadie sabía lo que podría pasar allá afuera, estoy segura de que ellos no se arrepintieron en ningún momento!"
    m "¡Sé qué ellos están bien y te piden que no te des por vencido!"
    l "Tienes razón."
    l "¡Ahora tengo el deber de proteger lo más importante para mí!"
    n "-Tomé sus manos y la besé en los labios suavemente, se sobresaltó-"
    l "Y esa persona eres tú."
    n "-Le confesé en forma de susurro volviendola a besar con suavidad y pasión-"
    m "Levi..."
    n "-Pronunció mi nombre entre el roce de nuestros labios-"
    m "Yo..."
    n "-La callaba entre besos apasionados pegándola más a mí cuerpo-"
    n "Sé rindió y me correspondió el beso de la misma forma, mordía mis labios mientras se pegaba más y enrollaba con sus brazos mi cuello."
    n "El exquisito aroma de su cabello penetraba en mi nariz."
    n "En vez de alejarla comencé a empujarla al respaldo de aquél sucio sillón quedando encima de ella mientras la seguía besando."
    m "Levi..."
    n "-Soltaba bocanadas por falta de aire-"
    m "Espe..."
    n "-Volví a callarla con más besos apasionados, el sabor de sus labios era dulce-"
    m "Levi..."
    n "-Volvió a llamarme con un tono que adoraba escuchar-"
    m "Espera..."
    n "-Me pidió colocando sus manos en mi pecho-"
    m "¡Levi!"
    n "-Me separé de ella para mirarla-"
    n "Su rostro estaba totalmente sonrojado, respiraba con dificultad, adoraba cada una de sus expresiones."
    n "Tomé sus manos que estaban en mi pecho, abrió los ojos para verme, sus ojos brillaban ante la pasión del momento."
    n "Estiré sus brazos arriba de su cabeza y me acerqué para besarla nuevamente, la besaba con suavidad y pasión sintiendo como su cuerpo se estremecía."
    n "Sus manos intentaban zafarse de mi agarre, con cada separación exhalaba el aire con fuerza, parecía no tener experiencia y le costaba mantener el aire en sus pulmones."
    n "Esbocé una sonrisa al reconocer que aún era inocente, pero quería dar un paso más con ella."
    n "Quería saciar mis impulsos y deseos con ella de una manera suave y delicada, de manera que ella también los disfrutará."
    n "Me miraba con cierto temor y confusión, intentaba zafarse de mi agarre mientras intentaba regular su respiración y ocultar su rostro sonrojado."
    l "Mikasa...mírame"
    n "-Pronuncié su nombre con delicadeza-"
    n "Se negó ocultando su rostro entre nuestros brazos."
    n "Me acerqué a ella aprovechado qué había girado su cabeza y comencé a besarle el cuello con delicadeza, se estremeció al instante y volvió a girar su rostro."
    n "Cerré los ojos para profundizar el beso mientras volvía a recargarla en el respaldo del sillón con fuerza, su cuerpo temblaba y se estremecía con cada choque de lengua."
    n "Soltaba pequeñas bocanadas de aire acompañadas de gemidos de placer y desesperación."
    m "Levi..."
    n "-Pronunciaba mi nombre entre gemidos de placer-"
    m "Deten..."
    n "-Volví a callarla profundizando el beso, cerró sus ojos con fuerza mientras me pegaba más a su cuerpo-"
    n "Coloqué una de mis piernas entre las suyas y apretaba con fuerza sus manos."
    n "Mi cuerpo y mente me pedían más a gritos, paré un momento al sentir mis mejillas húmedas."
    n "Me separé dejando el camino de saliva salir de nuestras bocas, nos miramos un momento y nos sorprendimos al ver que ambos llorábamos."
    n "Mikasa lloraba con su rostro sonrojado y yo con mi respiración intranquila."
    n "Tomamos el impulso de abrazarnos sintiendo el calor del otro, nuestros latidos se sincronizaron al igual que nuestra respiración."
    n "Limpiábamos mutuamente nuestras lágrimas."
    l "Lo siento, no debí forzarte de esa manera."
    m "No Levi, perdóname por sentir miedo."
    l "Exageré y me dejé llevar."
    n "-Confesé tomándola del mentón para que me mirará-"
    l "Discúlpame."
    n "Me brindó una cálida sonrisa mientras me tomaba de las manos y depositaba un beso en mi frente, imité su gesto y le ayudé a ponerse de pie."
    l "Deberíamos regresar, se ha hecho muy tarde."
    n "-Le dije tomándola de la mano saliendo de mi antiguo hogar-"
    m "¡Es realmente hermoso!"
    m "¡Es más hermoso con los colores del atardecer!"
    l "Después vendremos en la noche."
    n "Jalé las riendas del caballo y comenzamos a subir directo a la base de la legión."
    n "Aquél día quedaría recordado como nuestro primer día juntos."
    n "El día en qué decidimos contar nuestro pasado y en que habíamos decidido dar mayor cercanía entre nosotros."
    n "Me sentía libre y feliz conmigo mismo, el sueño de compartir un día entero con ella se había cumplido, me alegraba tenerla a mi lado y saber que sólo yo estaba dentro de su corazón."
    n "Dejamos el caballo en el establo y entramos a la base, siendo encontrados por Hange con un rostro de preocupación."
    z "¿Dónde han estado?"
    m "Sólo salimos a dar un paseo a la ciudad."
    n "Hange no protestó, conociéndola, nos estaría molestando desde el primer instante en qué nos viera, pero no fue así."
    n "No decía nada vergonzoso pero tampoco hablaba, sus expresiones mostraban qué estaba nerviosa y preocupada."
    l "Hange ¿Qué sucede?"
    z "Erwin está herido..."
    z "¡Los de la realeza lo han golpeado por no responder lo que querían saber!"
    n "-Contestó en un estado de crisis, Mikasa la miró sorprendida, yo me acerqué con cierta preocupación–"
    m "¿Qué información quieren?"
    z "Algo sobre esos titanes, lo que sea, algo nuevo fuera del reporte que escribiste."
    m "¡Bien!"
    n "-Respondió apretando los puños-"
    m "¡Les daré esa maldita información que tanto quieren!"
    m "¡Iré a hablar con ellos ahora!"
    z "¡Espera, Mikasa!"
    n "-Le gritó mientras íbamos detrás de ella-"
    n "El día había comenzado bien y había terminado de la peor manera con aquella noticia."
    n "¿Qué tipo de información tenía Mikasa?, una extraña preocupación comenzó a crecer."
    n "Después de todo, ahora la conocía más, conocía su dolor y la razón del porque era así su personalidad."
    n "La seguí en todo momento depositando mí confianza en ella, deseaba con todo mí ser algún día reanudar lo que habíamos dejado pendiente."
    n "La miraba por detrás con seriedad, ella era fuerte pero en algún momento fue débil, lo que define a una persona es su pasado y ella y yo lo entendíamos."
    show screen style_prefix_screen2
    n "Sabíamos qué estábamos destinados a estar juntos por nuestro pasado."
    call screen style_prefix_screen2
    l "..."
    call screen modal_example
    show lili
    with fade
    show text "{size=+25}{color=#FFFFFF}Capitulo 10{/color}{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}FIN{/color}{/size}" at truecenter
    with dissolve
    pause 0
    hide text
    with dissolve
    $persistent.cap11 = True
    return

label capitulo11:
    show lili
    with fade
    show text "{size=+25}{color=#FFFFFF}Capítulo 11{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}Ser fuerte{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    show screen quick_menu
    with dissolve
    show screen modal_example
    n "=LEVI="
    show screen style_prefix_screen
    n "Llegamos al lugar donde Erwin descansaba."
    call screen style_prefix_screen
    n "-Se sorprendió de vernos-"
    n "No tenía heridas importantes, tenía pequeñas vendas cubriéndole las heridas y moretes en la piel."
    n "-Sonrió levemente, con esa calma que siempre lo caracterizaba en cuanto entramos-"
    m "Comandante, ¿se encuentra bien?"
    n "-Erwin asintió con calma–"
    z "Lamentamos llegar tarde."
    n "–Erwin negó sin decir nada–"
    n "Conformes con la respuesta, Mikasa y Hange se alejaron un momento, pareciendo hablar del tema sobre el estado de Erwin."
    n "Así como de la supuesta golpiza de los altos mandos en busca de información."
    n "Que Mikasa, muy segura de sí misma, estaba dispuesta a ofrecer a base de reclamos y quejas."
    r "Levi, no seas como yo."
    n "-Dijo rompiendo el silencio, volteé a verlo sorprendido-"
    l "¿De qué diablos hablas?"
    n "-Pregunté viéndolo confundido hasta seguir su mirada en la figura angustiada de alguien-"
    l "¿Hablas de Hange?"
    r "No puedo tener a una gran mujer como ella a mi lado."
    n "-Soltó con un sonrisa llena de dolor-"
    n "-Levantó su vista para verme-"
    r "Alguien que sacrifica a sus soldados, y carga con el peso de la humanidad, simplemente no puede..."
    n "-Le dolió aceptarlo, pero era la verdad-"
    n "-Soltó un suspiro mientras la veía nuevamente-"
    n "Parecía costarle aceptar una realidad que él mismo se había impuesto por su cargo en la milicia, y podía comprenderlo."
    n "Erwin miraba a Hange a su manera, deseando protegerla siempre en forma de escondidas, y eso parecía bastarle."
    r "Tú eres diferente Levi, ¡no puedes dejar ir a alguien como ella!"
    n "-Dijo mientras lo veía sorprendido-"
    r "¿Creíste qué no lo había notado?"
    n "-Cuestionó con cierto tono de burla-"
    r "Mikasa, esa cadete ¿la amas cierto?"
    n "-Preguntó al ver a la mujer mencionada y desviaba su mirar acusador a mi persona nuevamente-"
    l "¡Cállate!"
    n "-Alcancé a decir en voz baja aún escondido-"
    r "¡Cuídala Levi!"
    r "Mikasa tiene un gran potencial y es capaz de defenderse sola, pero cualquier mujer necesita ser protegida por un hombre en algún momento..."
    n "-Lo miré sorprendido expectante de su frase a completar-"
    r "Sí Levi, tú eres ese hombre, él que la va a proteger cuando ella no pueda pelear-"
    n "-Lo miré atónito-"
    l "No sé si podría hacerlo..."
    n "-Hablé apretando los puños-"
    r "Debes dejar tu pasado atrás Levi..."
    n "-Me dijo con escepticismo, lo entendía-"
    l "¿Cómo podría dejarlo?"
    l "¡Toda mi vida no he sido más que un ser insensible, un bandido que mataba con tal de sobrevivir!"
    n "-Me expresé mirándolo con molestia-"
    l "¡¿Cómo podría protegerla de este horrible mundo sí ni siquiera yo puedo lidiar con el!?"
    n "-Reclamé preocupado con los miedos lejanos y ocultos-"
    n "Erwin me conocía perfecto, y sabía que por mucho que reclamara y exigiera opciones..."
    n "siempre podría lidiar con los problemas y apañármelas para salvarla y protegerla."
    n "El azul de sus ojos decía miles de cosas en un juicio de desaprobación de mis palabras falsas como mentiras, y la realidad de mis miedos al descubierto."
    n "Sus ojos, fáciles de leer para mí, con el pasar del tiempo, descifré su mensaje: “Tienes razón, pero no del todo”."
    l "La amo como no tienes idea, tenerla cerca me hace sentir vivo."
    n "-Hablé con sinceridad comenzando a romperme-"
    l "¡No me perdonaría si le pasara algo y yo no pudiera protegerla!"
    n "-Hablé apretando sus dientes-"
    r "¿Quieres que la mujer que se preocupa por ti, que vela, cuida y piensa en ti, se valla de tu lado?"
    r "¿Acaso quieres perderla?"
    n "-Me preguntó con cierta presión-"
    l "¡No!"
    l "¡No quiero perderla!"
    n "-Grité aturdido-"
    r "¡Entonces se fuerte!"
    r "¡Si realmente la amas serás el hombre más fuerte con tal de protegerla!"
    n "-Me dijo con seguridad y optimismo-"
    r "¡Tienes alguien a quien proteger y cuidar!"
    n "-Me recordó mientras bajaba mi mirada-"
    l "¿Y si sucede lo mismo?"
    n "-Pregunté aferrado a sus ropas en una agonía-"
    l "¿Y si ella pasa por lo mismo que pasaron mis hermanos o mi escuadrón?"
    n "-Pregunté con temor-"
    l "¿Qué sería de mí?"
    n "-Cuestioné con los ojos llorosos-"
    n "Me estaba aguantando el dolor."
    n "*El hombre más fuerte de la humanidad* también era humano, también cometía errores y sufría."
    n "Está era de las pocas veces que reconocía miedo y dolor, quería gritar y llorar."
    n "Sin pensarlo, oculto de ojos de los demás, Erwin me abrazó."
    n "Ignoró mis intentos bruscos de apartarme buscando salida al dolor, pero no desistió, se aferró a mi cuerpo encerrándome por completo."
    n "Compartiendo el sentimiento de comprensión y confianza que quería transmitir."
    n "Quería dejarme en claro que no estaba mal quebrarme ni rogarla al mundo protegerla, que sentía miedo de perder una vez más."
    n "Me dejé abrazar rendido, con el cuerpo temblando a la agonía reprimida, no hubo gritos."
    n "Pero me desahogaba a la falsa manera de ocultarlo en silencio por segundos antes de recuperar mi compostura."
    n "¿Qué sucedió aquí?"
    n "-Una voz se escuchó al entrar al silencioso el lugar-"
    n "-Hange y Mikasa regresaron a la escena tras la entrada del nuevo invitado-"
    n "Todos volteamos hacia la puerta al observar al comandante Zackley totalmente serio."
    ba "Quiero saber que ha sucedido."
    n "-Preguntó mirando a Erwin-"
    ba "¿Podrían explicarme qué ha sucedido?"
    m "¡Unos hombres golpearon al comandante Erwin por no recibir la información que querían!"
    n "-Comenzó a decir en un tono agresivo-"
    n "Soltó un suspiro resignado, levantó su mano en señal de disculpa hacia Erwin."
    n "Quien contestó con la mano levantado sin importarle tanto, la habitación permaneció en silencio hasta que Mikasa habló nuevamente."
    m "¡Hablaré con usted y le diré todo lo que se!"
    n "-Zackley la vió asombrado–"
    z "¡Mikasa!"
    n "-Gritó tomándola de los hombros-"
    m "¡Hablo enserio!"
    ba "Si es así, entonces acompáñame."
    n "-Le pidió Zackley saliendo del lugar con ella detrás–"
    r "¡Hange, Levi!"
    n "-Ambos volteamos a verlo-"
    r "¡Están a cargo de la legión!"
    show screen style_prefix_screen2
    n "-Nos dijo como si no hubiera otra alternativa, porque realmente no la había-"
    show lili
    call screen style_prefix_screen2
    l "..."
    call screen modal_example
    with dissolve
    n "Caminaba a zancadas por los pasillos."
    n "El comandante seguía su camino, caminaba rápido ignorando todo, quería acabar con todo de una vez."
    n "Debí haberlo hecho hace tiempo y me arrepentía, no quería causar más problemas por las que tendría que pagar y lo aceptaba."
    n "Me resigné a soltar un enorme bufido de molestia y seguir caminando por los estrechos pasillos hasta llegar a la oficina del comandante."
    ba "Por favor, siéntese"
    n "-Me pidió señalando la silla, lo hice con desgano-"
    ba "¿Me dará toda la información qué le pida?"
    n "-Preguntó mirándome fijamente con curiosidad, fruncí el ceño-"
    m "¿Qué quiere saber?"
    n "-Pregunté sin cambiar de semblante-"
    ba "¿Sabía del objetivo de la última expedición?"
    n "-Preguntó cruzando sus brazos-"

menu:

    "Si, si así pudiera llamarlo...":
        n "-Pronuncié con repudio, sin medir el veneno de mis palabras a su gesto de molestia-"
        n "¡Un suicidio, muchos soldados murieron por ese estúpido objetivo!"
        n "-Reclamé golpeando la mesa mirándolo con la peor de mis miradas-"
        ba "..."
        jump con

    "¡Sí, muchos soldados muríeron por ese objetivo!":
        n "-Reclamé mirándolo con odio-"
        ba "..."
        m "¡La expedición fué un suicidio!"
        jump con

label con:
    n "-Cerró los ojos recargándose en el respaldo de la silla sin inmutarse-"
    n "Me enfurecía que actuara con tanta tranquilidad sabiendo que le decía la verdad."
    n "Apretaba con fuerza los puños a causa de la molestia de su silencio indiferente."
    n "Soltó un suspiro en la misma posición, lo miré con odio al no recibir respuestas de su parte."
    n "El ruido de la puerta abrirse de golpe nos hizo voltear a ver al soldado que entraba en pánico a la oficina."
    so "¡Señor, malas noticias!"
    n "-Habló con la respiración agitada-"
    so "¡Avistamiento de esos titanes en las murallas!"
    n "-Gritó mientras ambos lo miramos sorprendidos-"
    so "¡Los soldados que vigilaban las murallas han sido eliminados!"
    n "-Exclamó aterrorizado-"
    ba "¡Ackerman!"
    n "-Volteé a verlo-"
    ba "¡Vaya al muro de inmediato y acabe a esos titanes!"
    n "-Me ordenó con una mirada desafiante-"
    m "¿Qué?"
    m "¿Yo?"
    n "-Cuestioné incrédula-"
    ba "¡Es una orden!"
    ba "¿Le quedó claro?"
    n "-Comentó de manera agresiva-"
    ba "¡Vaya a los depósitos, tome un equipo y diríjase a los muros!"
    n "-Lo miré sorprendida-"
    ba "¡Ahora!"
    n "-Corrí por el pasillo hasta llegar al depósito-"
    n "-Me coloqué el equipo sin entender aún que pasaba, seguí a los soldados hasta llegar al establo y tomar un caballo partiendo en dirección a los muros."
    n "Mi corazón palpitaba con rapidez, mi respiración era agitada, un terrible miedo y terror se apoderó de mí dándome nerviosismo."
    n "Llegamos a la ciudad dónde los gritos de la gente eran estremecedores, daban escalofríos."
    n "Veía por todos lados a la gente correr con miedo en su rostros, gritando y empujándose entre ellos con tal de salvarse."
    so "¡Ackerman suba por los techos!"
    n "-Me ordenó un soldado desesperado-"
    so "¡Llegará más rápido a los muros!-"
    n "-Seguí sus órdenes sin protestar-"
    n "Subí a los techos de las casas impulsándome con el equipo en dirección a las murallas."
    n "Volando entre los techos, ví a unos padres correr con sus hijos en brazos, con miedo y llorando."
    n "Era el mismo sentimiento, el recuerdo de hace años, cuando perdí Carla."
    n "El sentimiento de miedo y angustia por sobrevivir; mi cuerpo temblaba a pesar de moverse con seguridad,"
    n "Miraba al frente con determinación y miedo a la vez,"
    n "Por tercera vez tendría que despedazar a esos monstruos y proteger a la gente que corría para sobrevivir."
    de "¡Ayuda!"
    de "¡Alguien, ayúdeme!"
    n "-Una voz chillona me hizo parar-"
    ni "¡Por favor ayúdeme!"
    n "-Suplicó una pequeña niña atrapada entre los restos de una casa destrozada."
    n "Bajé para ayudarla, quitando los restos de madera sobre ella, la jalé con cuidado ayudándola a ponerse de pie-"
    m "¿Dónde están tus padres?"
    n "-Le pregunté hincándome a su altura-"
    ni "Un titán..."
    n "–Trató de decir mientras sollozaba-"
    ni "ellos me protegieron."
    n "-Balbuceaba mientras se limpiaba con sus sucias manos sus ojos llorosos-"
    n "La miré con tristeza al recordar mi pasado."
    n "-La tomé de la mano poniéndome de pie mientras me veía con tristeza-"
    n "-Apreté fuerte su mano-"
    m "No te sueltes de mi ¿de acuerdo?"
    n "-Le dije con suavidad, ella apretó mi mano y asintió con la cabeza-"
    n "Debía llevarla con los demás para que saliera de ahí."
    n "Pero un titán se asomó por detrás de las casas, con la misma expresión sedienta de muerte."
    n "La niña comenzó a llorar escondiéndose detrás de mí, mordí los labios al ver como comenzaba a acercarse."
    m "¡Maldita sea!"
    n "-Grité dándome vuelta cargando a la niña y volando en dirección contraria-"
    m "¡No veas!"
    n "-La niña se escondió en mi regazo mientras temblaba de miedo-"
    n "El titán estaba cada vez más cerca, no podía sacar las cuchillas al cargar a la niña."
    m "Tampoco podía acercarme a la zona de evacuación, el titán casi nos alcanzaba, no tenía opción, tenía que luchar y acabar con él."
    n "Cambié de dirección rápidamente confundiéndolo lo suficiente para dejar a la niña escondida en una casa mientras sacaba las cuchillas."
    n "La pequeña estiró sus brazos balbuceando en mi dirección asustada."
    m "¡Tranquila, confía en mí!"
    n "-Le pedí acariciando su cabeza-"
    n "Me lancé con ayuda del gas por su espalda cortándolo con las cuchillas, se quejó lanzando manotazos al aire."
    n "Utilicé una de sus manos para correr por ella y cortarle los dedos y parte de su brazo, volvió a quejarse soltando gritos desgarradores."
    n "Aproveché y clavé los ganchos sobre una de sus piernas para arrastrarme por el suelo y cortar sus piernas haciéndolo caer."
    n "Volé dando piruetas para finalmente cortar su nuca."
    n "El humo comenzó a aparecer, me paré agitada mientras la sangre del titán también desaparecía de mis ropas y de mi cara."
    ni "¡Cuidado!"
    n "-El grito de la niña me hizo voltear hacia atrás y ver a otro de esos titanes-"
    n "Lanzó un manotazo haciéndome volar y estrellarme en la pared de una casa."
    n "Levanté la vista quejándome del dolor visualizando a 4 de ellos corriendo en mi dirección."
    n "Abrí los ojos de golpe y me puse de pie esquivando a 3."
    n "El último alcanzó a golpearme y volví a estrellarme contra el suelo dando vueltas."
    n "La sangre comenzaba a salir de mis heridas, apreté los dientes y me puse de pie nuevamente."
    n "Volvió a repetirse lo mismo, el ciclo era infinito."
    n "Lograba esquivar a 3 con dificultad y el último alcanzaba a golpearme en las paredes y techos de las casas."
    n "Un fugaz pensamiento cruzó mi mente."
    n "*¿Y la niña?*"
    n "Me puse de pie mirando a la niña a lo lejos, los titanes sólo se fijaban en mí."
    m "¡Corre!"
    n "-Grité desesperada-"
    m "¡Vete de aquí!"
    n "-Le grité al ver que los titanes se acercaban a mí nuevamente-"
    m "¡Rápido!"
    n "-Ella salió de su escondite huyendo del lugar-"
    n "Apreté con fuerza las cuchillas y me abalancé sobre ellos, esquivando y dando cortadas, volvía al techo y repetía el mismo proceso."
    n "Pero no acaba, las heridas no eran profundas y se curaban con rapidez."
    n "Traté de repetir el paso, pero me alcanzaron lanzándome al techo de una vivienda."
    n "Me paré con dificultad, estaba débil, las últimas cuchillas se rompieron, sentía todo el cuerpo adolorido y la sangre escurriendo por mi rostro."
    n "Miré al cielo borrosamente, no faltaba mucho para que perdiera el conocimiento y me mataran, solté un suspiro de dolor y tristeza."
    n "Por lo menos había salvado a la niña que me recordaba a mí, el recuerdo de mis padres pasó por mi mente soltando lágrimas."
    m "Mamá, papá, pronto estaré con ustedes...."
    n "-Dije al aire deseando que me contestaran-"
    n "El manotazo de un titán sobre el techo provocó que saliera volando, no tenía fuerzas para responder."
    n "-Sentí un jalón-"
    n "El dolor fue tal que escupí sangre y sentí estrellarme en el piso pero no dolió."
    n "Sentía el cuerpo adolorido y siendo apretado,"
    n "Comenzaba a ver más borroso, el latido de mi corazón bajaba su ritmo, mí respiración se iba, mi cuerpo comenzaba a perder fuerzas."
    n "Percibí un aroma y recordé de quien era."
    n "Me sentí aliviada por un momento, quería abrazarlo y besarlo, agradecerle, pero mi cuerpo no me lo permitía."
    n "Poco a poco comenzaba a cerrar mis ojos perdiendo la visión, mi cuerpo ya no respondía."
    l "No te vayas..."
    n "-Habló una voz suave y quebrada-"
    l "por favor..."
    n "-Mi cuerpo era apretado contra el suyo-"
    l "No me dejes solo."
    n "-Imploraba con la voz rota-"
    l "Lo siento..."
    l "¡Es mi culpa!"
    n "-Exclamó entre gritos apretando mi cuerpo-"
    l "¡Debí quedarme a tú lado!"
    n "-Gritó con desesperación-"
    m "N-no es...t-tu culpa Levi..."
    l "¡No me dejes solo!"
    l "¡Te necesito a mi lado!"
    n "-Sentí su mano en mi rostro-"
    l "Por favor..."
    n "-Balbuceó entre llantos mientras acariciaba mi rostro-"
    m "Lo si-iento Levi..."
    l "¡Eres lo último que me queda en este cruel mundo!"
    n "-Gritaba mientras me abrazaba-"
    l "Eres mi motivo de seguir vivo..."
    n "-Susurraba mientras sus lágrimas caían en mi rostro-"
    m "Levi...ya no sigas...por favor..."
    l "¡Te amo Mikasa!"
    l "¡No me dejes!"
    n "-Se acercó a mi rostro para besar mis labios con suavidad-"
    m "Le-ev-i..."
    n "-Pronuncié su nombre con dificultad abriendo un poco mis ojos soportando el dolor, me miró sorprendido-"
    n "Estamos destinados...a estar juntos..."
    n "-Hablaba con dificultad aguantando el dolor-"
    l "¡No me dejes!"
    n "-Me abrazó con desesperación-"
    m "N-no lo ha-aré, lo...pro..-meto"
    n "-Dije con sinceridad, volvió a besarme con suavidad."
    n "Limpié las lágrimas que salían de su rostro dándole una sonrisa mientras él la imitaba con dolor."
    m "Sé fuerte Levi, hazlo por mí..."
    n "-Rogué acariciando su mano-"
    m "N-cesito tu ayuda..."
    n "-Volví a mirarlo con ternura-"
    l "¡Acabaré con ellos y te protegeré!"
    n "-Tomó mis manos apretándolas contra su pecho-"
    l "¡Es una promesa!"
    m "Es una promesa...Levi..."
    n "-Esbocé una pequeña sonrisa y lo miré con ternura para después cerrar mis ojos."
    show lili
    with fade
    show text "{size=+25}{color=#FFFFFF}Capitulo 11{/color}{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}FIN{/color}{/size}" at truecenter
    with dissolve
    pause 0
    hide text
    with dissolve
    $persistent.cap12 = True
    return

label capitulo12:
    play music "The Power of Mind.mp3"
    show lili
    with fade
    show text "{size=+25}{color=#FFFFFF}Capítulo 12{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}Mi destino{/color}{/size}" at truecenter
    with dissolve
    pause 5
    hide text
    show screen quick_menu
    with dissolve
    show lili
    with fade
    show screen modal_example
    n "=LEVI="
    show screen style_prefix_screen
    n "Recargué su cuerpo sobre el piso con delicadeza colocando su bufanda como soporte para su cabeza."
    n "La miré de nuevo, mantenía un semblante de dolor pese a perder el conocimiento."
    n "Su rostro estaba pálido, verla herida me hacía sentir la peor persona del mundo."
    n "El piso temblaba con brusquedad, los gritos de aquellos monstruos retumbaban por todo el lugar."
    n "Giré mí vista tras sentir una fuerte oleada de aire sobre mi cara, miré con odio a las bestias que corrían a mí con sus sonrisas sádicas."
    n "-Apreté con fuerza las cuchillas y solté los ganchos para volar en su dirección con la mayor rapidez y agilidad posible-"
    l "Ustedes..."
    n "-Decía mientras volaba sobre ellos-"
    l "¿¡Cómo se atreven a lastimar a la persona que amo?!"
    n "-Grité lleno de furia volando en su dirección dando piruetas en el aire, rasgando y cortando su piel sin piedad-"
    n "¡Más!"
    n "-Grité dando giros a gran velocidad cortando profundamente varias de sus extremidades, gritaban del dolor, sus sonrisas desaparecieron-"
    n "Solo peleaba por venganza, una sonrisa triunfadora se dibujó en mi rostro inconscientemente."
    n "Comenzaron a ponerse de pie aun tardando en curar sus heridas, sus miradas cambiaron."
    n "-Volaba dando giros y piruetas, corriendo por los techos logrando confundirlos-"
    n "Clavé mis ganchos sobre uno de ellos, y esquivando sus ataques, corté su nuca."
    n "Repetí el mismo proceso con 2 de aquellas bestias, cortando con profundidad sus cuerpos, torturándolos mientras sonreía satisfecho con cada grito."
    n "No paraba de cortar el cuerpo aún con el titán evaporándose."
    m "¡Levi reacciona!"
    m "¡Por favor regresa!"
    n "-Abrí los ojos de golpe sintiendo una ráfaga de viento golpear mi rostro-"
    n "Apretaba con desesperación las cuchillas, miré confundido mis manos, quería soltarlas pero no podía, mi cuerpo no respondía."
    l "¿Qué?"
    n "-Dije confundido al mirar al titán que corría en mi dirección-"
    n "-Salí volando tras el choque del titán y mis cuchillas tratando de protegerme-"
    n "Paré sobre una terraza mirando desconcertado al titán, tragué saliva."
    n "Sus palabras retumbaron dentro de mi cabeza como una campana."
    m "Por favor...no te quiero perder..."
    n "Abrí los ojos de golpe recordé a Mikasa llorar rogándome no volver a perder el control y lo había hecho de nuevo."
    n "Salté del techo esquivando el manotazo, cubrí con mis manos mi rostro de ser golpeado por alguna piedra que saliera volando del impacto anterior."
    n "El titán paró en seco pareciendo sentarse sin despegar su vista del cielo, parecía balbucear palabras que no lograba entender."
    n "-Lo miré sorprendido acercándome a él, éste volteó a verme-"
    n "Lo miré inseguro mostrándole mis cuchillas para amenazarlo pero pareció no inmutarse."
    n "Giró su rostro mostrándome solamente su nuca, se acercaba arrastrándose sin cambiar su posición."
    n "-Tragué saliva y clavé mis cuchillas sobre su nuca y la corté con determinación, el humo comenzó a salir-"
    n "El silencio se hizo presente y la venganza sé había acabado, me tiré al suelo exhausto, mirando confundido los restos del titán que se evaporaba."
    n "Un escalofrío recorrió mi cuerpo haciéndome levantar la vista hacía la terraza donde estaba Mikasa."
    n "Con las pocas fuerzas que me quedaban, me arrodillé a su lado y la acurruqué en mi pecho, un sentimiento de culpa se apoderaba de mi mente y no podía pensar en otra cosa."
    z "¡Levi!"
    z "¿Estás bien?"
    n "-Hange hizo presencia hincándose a mi lado inspeccionando con sus manos mi rostro-"
    l "Estoy bien."
    n "-Dije alejándome y bajando la mirada-"
    l "Pero ella..."
    z "Tranquilo, ayúdame a levantarla."
    n "-Acepté sin decir nada-"
    z "¡Por favor encárgate de ella Nifa!"
    n "-Le dijo a una soldado que asintió alejándose con otros soldados cargando la camilla-"
    n "Miré como se alejaban del lugar, rogaba porque estuviera bien."
    n "Miré a Hange un momento, mantenía una expresión diferente a la de siempre, su rostro no reflejaba otro más que seriedad."
    n "La miré extrañado por el cambio de su rostro al que siempre suele tener, y quizás la respuesta era Zackley mirándonos desde la lejanía."
    z "Lo siento Levi, vamos con Mikasa."
    n "-Exclamó cambiando a su semblante de siempre-"
    l "¡No, espera!"
    n "-Pedí bajando la mirada-"
    l "¡Explícame ¿qué hizo ése hombre!?"
    n "-Pregunté desesperado-"
    z "Mandó a Mikasa a luchar sola contra esos titanes, su plan era observar como luchaba contra ellos..."
    n "-Fruncí el ceño entendiendo porque Hange se había molestado–"
    z "¡Hablaremos de eso después, vayamos con los heridos!"
    n "-Sugirió jalándome del brazo-"
    n "No me resistí, dejé que me llevara, quería verla, saber sí no corría peligro, sí se recuperaría pronto, sí seguiría a mí lado como lo había prometido."
    n "Llegamos al campamento montado para la atención de heridos."
    n "Hange me guiaba por ese lugar hasta encontrar la carpa correcta, mi corazón latía sin frenos."
    z "¿Cuál es su estado Nifa?"
    n "-Oí a Hange preguntarle a su subordinada-"
    f "Hay heridas profundas."
    n "-Sentí que el corazón se me paraba-"
    f "He logrado curar las más superficiales pero tardará en recuperarse..."
    n "-Sentí un flechazo en el pecho-"
    f "No sé con exactitud cuánto tiempo tardará en despertar."
    n "-Finalizó con un tono preocupado-"
    z "Entiendo..."
    n "-Respondió sentándose en una silla ocultando con sus manos su rostro."
    z "Nifa, sal a tratar a otros heridos, yo me haré cargo del resto."
    n "Miré a Hange preocupado, actuaba diferente a como siempre era."
    n "La Hange que yo conocía no estaba ahí, había desaparecido, soltaba suspiros y se alborotaba el cabello desesperada esta frustrada, enojada, triste y desesperada."
    z "¿Cómo aguanta toda esta presión Erwin?"
    n "-Comenzó a decir soltando un suspiro-"
    z "¿Cómo soporta la muerte de sus soldados?"
    n "-Preguntó viéndome con tristeza-"
    l "Solo Erwin sabe cómo hacerlo, no hay reglamento a seguir para ser comandante..."
    n "-Respondí sentándome en una silla cercana a ella-"
    z "Y sin embargo nos dejó a cargo."
    l "Tienes las aptitudes, capacidades y el corazón para hacerlo."
    n "-Le demostré mientras me veía sorprendida-"
    z "Supongo..."
    n "-respondió apenada-"
    z "¡Gracias Levi!"
    n "-Me agradeció entre risillas-"
    n "Normalmente hubiera soltado un bufido o la hubiera ignorado, pero prefería verla de esa manera alegre y viva como suele ser."
    n "Le dirigí una pequeña sonrisa a lo cual ella rió, regresó a ser la misma."
    z "¡Ya recibí el empujón que necesitaba!"
    z "Te dejo para qué estés con ella."
    n "-Dijo guiñándome el ojo saliendo de la carpa, le recriminé en mi mente avergonzado-"
    n "Acerqué la silla a la cama, fijé mi vista en Mikasa, vendada de los brazos, el cuello y parte de la cabeza."
    n "Su cuerpo seguía frío, sus labios estaban secos, sus ropas rasgadas eran cubiertas por cobijas."
    l "Mikasa."
    n "-La llamé tomando con delicadeza su mano-"
    n "No me salían más palabras para describir la alegría de saber que seguía viva, a mi lado, besé su mano para después encerrarla entre mis manos."
    l "Si tan solo me hubiera quedado contigo."
    n "-Me reclamé mientras acariciaba sus manos-"
    l "Si no me hubiera alejado, no estarías herida."
    n "Deseaba que me contestara y me dijera que tenía razón, que era mi culpa, necesitaba escuchar su voz, la necesitaba solo a ella."
    l "Isabel, Farlan..."
    n "-Los nombré después de mucho tiempo-"
    l "¡Encontré lo que jamás creí tener, es la razón de mi vida por tercera vez!"
    n "-Apreté con mi puño el pecho aguantando las ganas de llorar-"
    l "¡Por favor, no dejen que se vaya de mí lado!"
    n "-Les rogué mientras me recostaba sobre la cama sin soltar su mano-"
    play music "Psycho.mp3"
    show text "{size=+25}{color=#FFFFFF}Estamos contigo Hermano...{/color}{/size}" at truecenter
    show text "{size=+25}{color=#FFFFFF}Ella no se irá de tu lado Levi...{/color}{/size}" at truecenter
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    scene lili
    with flashbulb
    n "El aroma a humedad era el único aroma perceptible en aquél sucio lugar."
    n "El silencio fúnebre y la oscuridad presente lo hacía el lugar más tétrico y horrible para vivir, sólo la gente fuerte lograría sobrevivir."
    scene
    #Levi y farlan escondidos
    la "¿Estás seguro de hacer esto Levi?"
    n "-Lo escuché preguntarme algo nervioso-"
    la "¿Y sí llega la policía?"
    l "Esos tipos son lentos, tranquilízate"
    ##
    n "-Dije indiferente preparando mí equipo para volar-"
    n "Salté a los tejados impulsado por el gas del equipo, tumbé las cajas de aquella carreta sorprendiendo a los vendedores."
    n "Fruncí el ceño y volví a tirar el resto de cajas tirando su contenido, varios hombres nos siguieron."
    n "-Saqué mi cuchillo y comencé a pelear-"
    n "Mientras Farlan llevaba a la gente de regreso a sus casas."
    #señor apuntando
    de "¡Da un paso más y te mato!"
    n "-Me amenazó cargando el gatillo de una pistola viéndome con odio-"
    n "-Farlan trató de acercarse-"
    de "-¡No te muevas o disparo!"
    n "-Lo amenazó apuntándolo con la pistola-"
    l "¡Tú problema es conmigo no con él!"
    n "-Fruncí el ceño molesto apretando mis puños-"
    #Farlan con cuchillo
    la "¡Levi!"
    n "-Gritó Farlan asustado comenzando a correr en mí dirección sacando un cuchillo-"
    l "¡No te metas!"
    n "-Le grité molesto, él paró-"
    l "¡Déjame solo, vete de aquí!"
    n "-Le pedí mientras el hombre se acercaba más-"
    la "¡No te dejaré aquí solo! Déjame..."
    l "¡Que te largues de aquí!"
    n "-Le grité harto mirándolo con odio-"
    l "¿Qué esperas Farlan?-"
    n "Volví a gritarle, él solo me vió y se alejó con ayuda del equipo-"
    ##Señor apuntando
    de "¡¿Así tratas a tú familia!?"
    n "-Dijo con risas burlonas-"
    ##
    n "Fruncí el ceño harto de sus opiniones y le lancé el cuchillo con agilidad clavándoselo en el pecho mientras se desangraba rápidamente-"
    n "Regresé a mi hogar dejando el equipo tirado en el sucio sillón y entré a la habitación que compartía con ellos."
    #Isabela acostada en la cama
    be "¡Hermano! ¡Volviste!"
    n "-Me saludó la chica pelirroja acostada sobre las sucias cobijas del lugar-"
    be "¿Estás bien?"
    n "-Preguntó intentando levantarse-"
    l "¡No te levantes!"
    n "-Le regañé mientras ella reía-"
    l "¿Dónde está Farlan?"
    n "-Le pregunté sentándome a su lado-"
    be "Salió a buscar mi medicina, no tardará-"
    n "-Respondió tapándose con las cobijas-"
    l "¿Estás mejor?"
    n "-Le pregunté tocando su frente caliente-"
    l "Tienes mucha fiebre..."
    be "-¡Con la medicina estaré bien hermano!"
    n "-Me dijo brindándome una sonrisa, suspiré aliviado-"
    n "Isabel se puso mal debido a las bajas temperaturas"
    be "Hermano gracias por cuidarme."
    n "-Sonrió dibujando un color rojo en sus mejillas-"
    be "Perdón por preocuparte."
    n "-Confesó ocultándose con las cobijas el rostro apenada-"
    l "Tonta."
    n "-Acaricié su cabeza-"
    l "Recupérate pronto. "
    n "-Ella asintió con su cabeza con una sonrisa-"
    #farlan con medicina en las manos
    la "¡Isabel traje tú medicina!"
    n "-Anunció entrando con un vaso de agua-"
    la "¡Ah Levi!"
    l "Dale su medicina primero."
    la "Toma, con esto estarás mejor."
    n "-Le dijo con ternura acercándole el vaso, ella lo aceptó y tomó el líquido-"
    #Isabela feliz
    be "Gracias hermano, por cuidar de mí"
    n "-Farlan sonrió, yo crucé los brazos-"
    be "¿Si me recupero pronto, podremos ir a ver las estrellas como siempre lo hacemos?"
    #farla feliz
    la "¡Claro!"
    n "-Contestó dándole una sonrisa-"
    la "¡Es una costumbre que tenemos después de todo!"
    n "-Afirmó tapándola con las cobijas-"
    la "Descansa."
    n "-Ella asintió cerrando sus ojos-"
    ##
    n "Salí de la habitación sentándome en el sillón, Farlan se sentó a mí lado y me estiró una bolsa, la tomé confundido."
    #Levi y Farlan sentados hablando
    la "Las conseguimos en el asalto de hoy, son suficientes reservas."
    n "-Dijo mirando con desdén una de esas bolsas."
    la "Nos durarán para varios días."
    l "Entonces usémoslas adecuadamente."
    n "-Lancé la bolsa al costal donde había más de ellas-"
    la "¡No vuelvas a hacer una tontería como esa Levi!"
    la "¿Sabes lo que pudo pasar sí no manejabas la situación?"
    n "-Me recriminó poniéndose de pie-"
    l "No sucedió."
    l "¡Puedo acabar con cualquiera!"
    n "-Dije con orgullo mirándolo a los ojos-"
    la "¡No importa que seas fuerte, ellos también pueden matarte!"
    l "No importa."
    n "-Solté con desgano recostándome sobre el sillón-"
    la "¡Claro qué importa!"
    la "¡A Isabel y a mí nos importa!"
    n "-Levantó la voz viéndome fijamente-"
    la "¡No actúes solo, recuerda que sólo nos tenemos nosotros tres!"
    n "-Me recordó sorprendiéndome-"
    la "¡Siempre nos protegeremos y ayudaremos entre nosotros, no lo olvides!"
    n "-Dijo agachando su cabeza-"
    l "Lo siento..."
    n "Tenía razón, ellos eran mi única familia ahora."
    n "A quiénes debía cuidar, proteger y asegurarles un futuro de supervivencia dentro de éste mundo cruel lleno de muerte."
    #Farlan viendo el techo feliz
    la "¿Iremos a ver las estrellas?"
    n "-Preguntó viendo el techo con esperanza-"
    la "Después de todo es nuestra costumbre..."
    l "Lo haremos."
    n "-Dije mirando el techo imaginando las estrellas-"
    la "Deseo que siempre estemos juntos."
    n "*Yo también lo deseo*"
    n "-Pensé mirando con determinación el techo-"
    #=Fin del flashback de Levi =
    de "Levi..."
    n "Abrí los ojos con dificultad al sentir que movían mi cuerpo."
    n "Levanté la cabeza viendo a Mikasa aún acostada sobre la cama dormida, mis manos se entrelazaban con las suyas."
    n "-Giré la vista a la persona que me despertó-"
    z "¡¿Por fin despertaste dormilón!?"
    n "-Preguntó con risas acercándome una taza de té, la tomé con dificultad-"
    z "¡Hace tiempo que no te veo así Levi!"
    n "-Confesó sonriéndome divertida sentándose a mí lado-"
    l "¿Cuánto tiempo llevo dormido?"
    n "-Pregunté aún somnoliento-"
    z "Desde que te dejé, hasta medio día..."
    n "-Contestó entre risas, la miré sorprendido-"
    z "Parece que estabas muy cansado, solo con ella caes dormido ¿eh?"
    n "-Insinuó divertida, me alejé de ella avergonzado-"
    l "Hange, ¿Mikasa...?"
    n "-Pregunté preocupado-"
    z "No ha despertado..."
    n "-Confirmó cabizbaja-"
    n "Verla recostada sobre la cama me recordaba a Isabel."
    so "¡Comandante Hange!"
    so "¡Capitán Levi!"
    n "-La voz áspera retumbó llamando nuestra atención-"
    so "¡Ya es hora!"
    n "-Exclamó solicitando que saliéramos del lugar y partir a otro lado-"
    l "¿Hora de qué?"
    n "-Pregunté confundido mirando a Hange-"
    z "¡Sólo iré yo, Levi se hará cargo de Erwin!"
    n "-Exclamó poniéndose de pie comenzando a caminar a la entrada-"
    l "¿Hange, qué diablos pasa?"
    n "-Pregunté confundido poniéndome de pie-"
    z "Sigue mis instrucciones, después te contaré qué sucede."
    n "-Me miró con inseguridad-"
    z "¡No olvides ir con Erwin!"
    n "-Bufé molesto-"
    n "Hange me ocultaba cosas, miré por última vez a Mikasa y salí de la carpa."
    n "Entré donde estaba Erwin, volteó a verme sorprendido cuando me senté a su lado, no lo miré, mi mente pensaba en otras cosas."
    l "Hange me lo pidió."
    l "¡No, más bien me lo ordenó!"
    n "-Fruncí el ceño cruzándome de brazos-"
    r "Entonces está haciendo bien su trabajo."
    n "-Respondió con una sonrisa, volteé a verlo-"
    l "¡¿No crees qué es mucho para ella!?"
    l "Está sufriendo por eso ¿sabes?"
    n "Le dije esperando una respuesta al porqué de dejarla a cargo de todo y poner ese peso en sus hombros."
    r "..."
    n "-Esquivó la pregunta como era de esperarse-"
    l "Eso no responde nada..."
    n "-Contesté fijando la mirada en el suelo-"
    r "¿Cómo está Mikasa?"
    n "-Preguntó sacándome de mis pensamientos-"
    l "No se sabe cuándo despertará..."
    n "-Comencé a decir apretando los puños-"
    l "Todo por mí culpa, sí yo la hubiera detenido..."
    n "-Me recriminé de nuevo, golpeando con mí puño mí pierna con fuerza-"
    r "No es tu culpa, ella fue quién quiso hablar con Zackley, nadie sabía lo que iba a pasar..."
    n "-Dijo con tranquilidad mientras me miraba preocupado-"
    l "¡Ese imbécil la uso para sus propios beneficios poniendo su vida en peligro!"
    n "-Erwin suspiró fijando su vista en la ventana, lo miré intentando descifrar que pensaba al respecto, nada, ninguna idea de lo que pensaba–"
    r "Arlet y Jaeguer fueron a verla."
    n "-Me sobresalté-"
    r "Hange les dió la noticia y corrieron a buscarla, en cuánto vieron que estabas con ella, no sé preocuparon más y decidieron regresar después."
    n "-Volteó a verme mientras lo veía sorprendido y apenado-"
    r "Sigue cuidando de ella Levi, despertará pronto."
    n "-Sentí brotar un pequeño rayo de esperanza en mí ser-"
    l "Eso espero Erwin, es lo que más deseo."
    show screen style_prefix_screen2
    n "-Miré la ventana imaginando lo que le diría cuando despertara-"
    call screen style_prefix_screen2
    l "..."
    call screen modal_example
    show text "{size=+25}{color=#FFFFFF}=Recuerdo de Mikasa={/color}{/size}" at truecenter
    #Mikasa y su madre preparando comida
    m "Mami, ¿dónde está papá?"
    n "-Le pregunté después de buscar por toda la casa–"
    ke "Tu padre salió a cazar, no tardará en llegar."
    n "-Respondió mientras seguía preparando la comida-"
    ke "¡Sabes que a papá se le da muy bien la caza!"
    n "-Dijo sonriendo-"
    m "Siempre hablas así de papá, se nota que lo quieres mucho."
    n "-Acepté viéndola con curiosidad, ella sonrió apenada-"
    m "¿Cómo conociste a papá?"
    #madre de mikasa sonrojada
    ke "Es una historia muy larga."
    n "-Habló apenada y divertida-"
    ke "Pero, puedo decirte que era nuestro destino conocernos y quedarnos juntos."
    n "-Respondió ruborizada con una hermosa sonrisa-"
    m "¿Destino?"
    n "-Pregunté sin entender ese término-"
    ke "La leyenda del hilo rojo del destino."
    ke "¿La recuerdas?"
    n "-Me preguntó sentándose a mi lado-"
    m "¡Papá me la contó una vez!"
    n "-Recordé sus palabras-"
    #Dos hilos del amor
    m "Un hilo rojo invisible está atado al dedo meñique de cada persona."
    m "Al final de éste, está atado al de la persona que es tu alma gemela, con la que estás destinada a pasar el resto de tu vida."
    n "-Contaba mientras veía a mí madre a los ojos brillantes con una sonrisa-"
    #Madre de mikasa sonriendo
    ke "Así es, pero dentro de nuestro clan..."
    n "-Tomó mi brazo señalando la marca debajo de la venda-"
    ke "Dice que ese destino está forjado desde que naces, y no habrá persona que pueda meterse antes de conocer a tu alma gemela..."
    n "-Contó mirándome con ternura acariciando mí cabeza-"
    m "¿No conociste a nadie más que a papá?"
    n "-Pregunté sorprendida-"
    ke "¡Papá fue el primero y el único en robarse mí corazón y formar parte importante de mi vida!"
    #madre de mikasa sonrojada
    n "-Confesó ruborizada con una sonrisa alegre-"
    ke "¡Tu padre era mí destino desde que nací!"
    n "-Sonrió, la miré con alegría–"
    m "¿Yo también tendré algo así?"
    n "-Mi madre me vió con ternura-"
    #Dedo meñique de mikasa
    ke "¡Cuando llegué el momento te darás cuenta de quién está al otro lado de tu hilo rojo del destino!"
    n "-Exclamó levantando mi mano, miré con curiosidad mi dedo meñique, imaginando cuán largo sería y cuánto tardaría en encontrar a la persona atada del otro lado-"
    show text "{size=+25}{color=#FFFFFF}*¿Quién es mí destino?*{/color}{/size}" at truecenter
    define flashbulb = Fade(0.2, 0.0, 0.8, color='#fff')
    with flashbulb
    n "Un terrible dolor sentía en todo el cuerpo."
    n "Me quejaba mientras abría los ojos lentamente y con dificultad."
    n "Comencé a ver borroso y escuchar ruidos, la luz que entraba al lugar me dificultaba abrir los ojos."
    n "Mi cuerpo estaba tenso, no podía moverlo a mi voluntad, intentarlo dolía."
    n "La calidez en mi mano me sobresaltó ya que sentía el resto del cuerpo frío."
    l "¡Mikasa!"
    n "-El grito de alguien llamándome me hizo abrir por completo los ojos."
    n "-Giré mi cabeza en dirección a la persona parada a un lado de mí cama, esperé hasta enfocarla–"
    m "Le-vi..."
    n "-Intenté pronunciar su nombre con dificultad, sintiendo mi garganta rasparse por el esfuerzo-"
    l "¡Por fin despertaste!"
    n "-Exclamó con alegría mientras acariciaba con ternura mi cabeza-"
    l "¡No sabes cuánto te he esperado!"
    n "-Dijo dándome una sonrisa derramando una lágrima-"
    l "¡Tengo que llamar a Hange!"
    n "-Exclamó saliendo del lugar-"
    n "-Miré el lugar en el que estaba-"
    n "Estaba recostada con cobijas, mi cuello y brazos vendados."
    n "-Intenté levantarme, pero no pude-"
    n "El dolor llegó a ser insoportable al momento de tan sólo moverme, me encontraba en la misma situación de hace tiempo, no, era diferente, ésta vez ni siquiera podía moverme."
    z "¡Ah, Mikasa!"
    n "-Exclamó entrando al lugar con alegría-"
    z "¡Me alegra saber qué has despertado!"
    n "-Exclamó sentándose en una silla al lado de mí-"
    z "¡4 días para que despertarás y te recuperarás favorablemente!"
    n "-Dijo con una sonrisa-"

    menu:
         "¿4...dí-as?":
             n "-Pregunté con esfuerzo y dolor-"
             z "No te sobresfuerces tu estado no es bueno..."
             z "¿De acuerdo?!"
             n "-Cuestionó con preocupación en su rostro, asentí levemente con dolor-"
             jump ba

         "¡¿Q-ué?!":
             z "¡Lo importante es qué ya despertaste!"
             n "-Dijo preocupada sobresaltándome-"
             z "¡Hablaremos después de todo lo sucedido, por ahora solo dedícate en cooperar para tu pronta recuperación."
             jump ba

label ba:
    n "¿Qué había sucedido durante 4 días?"
    n "¿Qué me había pasado?"
    n "¿Por qué no podía moverme ni hablar?"
    n "Todas esas preguntas retumbaban en mí cabeza confundiéndome, quería preguntar y tener respuestas, levantarme y saber qué me había pasado."
    n "Quería saber qué había sucedido, quería saber dónde estaba."
    z "Me encargaré de revisar tus heridas, te contaré todo lo que pasó, pero no pongas resistencia."
    n "-Volví a asentir con dificultad-"
    n "Con ayuda de Levi, Hange logró sentarme."
    n "Miré a Levi preocupada y confundida, él me miró con tristeza, me alegraba de verlo de nuevo, el recuerdo de la leyenda de mi madre se hizo presente en mi mente."
    n "Con sólo verlo, recordaba aquél sueño, bajé la vista para ver mi mano, levantando un poco el dedo meñique."
    n "-Dibujé una sonrisa para después voltearlo a ver-"
    n "-Se acercó a mí lado tomando con delicadeza mi mano, entrelazando nuestros dedos, en especial, los meñiques-"
    l "Gracias por quedarte a mi lado."
    n "-Dijo besando mi mano-"
    l "Te amo."
    n "-Confesó con una sonrisa a lo cual me sonrojé-"
    n "Solté una lágrima, su mano cálida rozó mi mejilla limpiándola, me brindó otra sonrisa."
    n "Y sin lastimarme, me abrazó, a lo que terminé llorando al recordar una parte de lo que había sucedido."
    n "Sentir de nuevo su calor, oler su aroma, sentir su presencia de nuevo conmigo me recordaba que estaba viva."
    n "Después de todo le había hecho aquella promesa de quedarme a su lado por un sólo motivo."
    show lili
    with dissolve
    show text "{size=+25}{color=#FFFFFF}*Eres mi destino Levi, la persona del otro lado de mí hilo rojo del destino*{/color}{/size}" at truecenter
    with dissolve
    pause 6
    show text "{size=+25}{color=#FFFFFF}Capitulo 12{/color}{/size}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve
    show text "{size=+25}{color=#FFFFFF}FIN{/color}{/size}" at truecenter
    with dissolve
    pause 0
    hide text
    with dissolve
    $persistent.cap13 = True
    return



return
