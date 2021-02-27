#Barra de Eren
screen barraAmizade(amizade):
    frame:
        xalign 0.01  ypos 300
        hbox:
            spacing 20
            vbox:
                spacing 10
                text "{color=#F7FCF8}Eren{/color}"

                $ ui.vbar(100, amizade, xmaximum=5, ymaximum=200, top_bar=Frame("images/top.png", 25, 25), bottom_bar=Frame("images/bottom.png", 25, 25), xalign=0.5, yalign=0.5)

label chamarBarraMais(valorBarra):
    $pontoAnterior = valorBarra
    while contador < valorBarra:
        $contador += 3
        show screen barraAmizade(contador)
        pause 0.001
    $renpy.pause(2)
    hide screen barraAmizade
    return


label chamarBarraMenos(valorBarra):
    if valorBarra > 100:
        $valorBarra = 100
    if(valorBarra < pontoAnterior):
        $contador = pontoAnterior
        while contador > valorBarra:
            $contador -= 2
            show screen barraAmizade(contador)
            pause 0.001
        $renpy.pause(1)
        hide screen barraPontos

    elif(valorBarra > pontoAnterior):
        $contador = pontoAnterior
        while contador < valorBarra:
            $contador += 1
            show screen barraAmizade(contador)
            pause 0.001
        $renpy.pause(2)
        hide screen barraPontos
    return

#Barra de Armin
screen barraAmizade2(amizade):
    frame:
        xalign 0.01 ypos 300
        hbox:
            spacing 20
            vbox:
                spacing 10
                text "{color=#F7FCF8}Armin{/color}"

                $ ui.vbar(100, amizade, xmaximum=5, ymaximum=200, top_bar=Frame("images/top.png", 25, 25), bottom_bar=Frame("images/bottom.png", 25, 25), xalign=0.5, yalign=0.5)

label chamarBarraMais2(valorBarra):
    $pontoAnterior = valorBarra
    while contador < valorBarra:
        $contador += 3
        show screen barraAmizade2(contador)
        pause 0.001
    $renpy.pause(2)
    hide screen barraAmizade2
    return


label chamarBarraMenos2(valorBarra):
    if valorBarra > 100:
        $valorBarra = 100
    if(valorBarra < pontoAnterior):
        $contador = pontoAnterior
        while contador > valorBarra:
            $contador -= 2
            show screen barraAmizade2(contador)
            pause 0.001
        $renpy.pause(1)
        hide screen barraPontos

    elif(valorBarra > pontoAnterior):
        $contador = pontoAnterior
        while contador < valorBarra:
            $contador += 1
            show screen barraAmizade2(contador)
            pause 0.001
        $renpy.pause(2)
        hide screen barraPontos
    return

#Barra Hanji
screen barraAmizade3(amizade):
    frame:
        xalign 0.01 ypos 300
        hbox:
            spacing 20
            vbox:
                spacing 10
                text "{color=#F7FCF8}Hange{/color}"

                $ ui.vbar(100, amizade, xmaximum=5, ymaximum=200, top_bar=Frame("images/top.png", 25, 25), bottom_bar=Frame("images/bottom.png", 25, 25), xalign=0.5, yalign=0.5)

label chamarBarraMais3(valorBarra):
    $pontoAnterior = valorBarra
    while contador < valorBarra:
        $contador += 3
        show screen barraAmizade3(contador)
        pause 0.001
    $renpy.pause(2)
    hide screen barraAmizade3
    return


label chamarBarraMenos3(valorBarra):
    if valorBarra > 100:
        $valorBarra = 100
    if(valorBarra < pontoAnterior):
        $contador = pontoAnterior
        while contador > valorBarra:
            $contador -= 2
            show screen barraAmizade3(contador)
            pause 0.001
        $renpy.pause(1)
        hide screen barraPontos

    elif(valorBarra > pontoAnterior):
        $contador = pontoAnterior
        while contador < valorBarra:
            $contador += 1
            show screen barraAmizade3(contador)
            pause 0.001
        $renpy.pause(2)
        hide screen barraPontos
    return

#barra de LEVI
screen barraAmizade4(amizade):
    frame:
        xalign 0.01 ypos 300
        hbox:
            spacing 20
            vbox:
                spacing 10
                text "{color=#F7FCF8}Levi{/color}"

                $ ui.vbar(100, amizade, xmaximum=5, ymaximum=200, top_bar=Frame("images/top.png", 25, 25), bottom_bar=Frame("images/bottom.png", 25, 25), xalign=0.5, yalign=0.5)

label chamarBarraMais4(valorBarra):
    $pontoAnterior = valorBarra
    while contador < valorBarra:
        $contador += 3
        show screen barraAmizade4(contador)
        pause 0.001
    $renpy.pause(2)
    hide screen barraAmizade4
    return


label chamarBarraMenos4(valorBarra):
    if valorBarra > 100:
        $valorBarra = 100
    if(valorBarra < pontoAnterior):
        $contador = pontoAnterior
        while contador > valorBarra:
            $contador -= 2
            show screen barraAmizade4(contador)
            pause 0.001
        $renpy.pause(1)
        hide screen barraPontos

    elif(valorBarra > pontoAnterior):
        $contador = pontoAnterior
        while contador < valorBarra:
            $contador += 1
            show screen barraAmizade4(contador)
            pause 0.001
        $renpy.pause(2)
        hide screen barraPontos
    return

#Barra de Annie
screen barraAmizade5(amizade):
    frame:
        xalign 0.01  ypos 300
        hbox:
            spacing 20
            vbox:
                spacing 10
                text "{color=#F7FCF8}Annie{/color}"

                $ ui.vbar(100, amizade, xmaximum=5, ymaximum=200, top_bar=Frame("images/top.png", 25, 25), bottom_bar=Frame("images/bottom.png", 25, 25), xalign=0.5, yalign=0.5)

label chamarBarraMais5(valorBarra):
    $pontoAnterior = valorBarra
    while contador < valorBarra:
        $contador += 3
        show screen barraAmizade5(contador)
        pause 0.001
    $renpy.pause(2)
    hide screen barraAmizade5
    return


label chamarBarraMenos5(valorBarra):
    if valorBarra > 100:
        $valorBarra = 100
    if(valorBarra < pontoAnterior):
        $contador = pontoAnterior
        while contador > valorBarra:
            $contador -= 2
            show screen barraAmizade5(contador)
            pause 0.001
        $renpy.pause(1)
        hide screen barraPontos

    elif(valorBarra > pontoAnterior):
        $contador = pontoAnterior
        while contador < valorBarra:
            $contador += 1
            show screen barraAmizade5(contador)
            pause 0.001
        $renpy.pause(2)
        hide screen barraPontos
    return


#Barra de Erwin
screen barraAmizade6(amizade):
    frame:
        xalign 0.01 ypos 300
        hbox:
            spacing 20
            vbox:
                spacing 10
                text "{color=#F7FCF8}Erwin{/color}"

                $ ui.vbar(100, amizade, xmaximum=5, ymaximum=200, top_bar=Frame("images/top.png", 25, 25), bottom_bar=Frame("images/bottom.png", 25, 25), xalign=0.5, yalign=0.5)

label chamarBarraMais6(valorBarra):
    $pontoAnterior = valorBarra
    while contador < valorBarra:
        $contador += 3
        show screen barraAmizade6(contador)
        pause 0.001
    $renpy.pause(2)
    hide screen barraAmizade6
    return


label chamarBarraMenos6(valorBarra):
    if valorBarra > 100:
        $valorBarra = 100
    if(valorBarra < pontoAnterior):
        $contador = pontoAnterior
        while contador > valorBarra:
            $contador -= 2
            show screen barraAmizade6(contador)
            pause 0.001
        $renpy.pause(1)
        hide screen barraPontos

    elif(valorBarra > pontoAnterior):
        $contador = pontoAnterior
        while contador < valorBarra:
            $contador += 1
            show screen barraAmizade6(contador)
            pause 0.001
        $renpy.pause(2)
        hide screen barraPontos
    return
