default i = 0
default hovering = False

screen my_screen:
    add "#000"
    hbox:
        spacing 5
        text "[i]"
        text "[hovering]"
        textbutton "Toca":
            action SetVariable("i", i + 1)
            hovered SetVariable("hovering", True)
            unhovered SetVariable("hovering", False)

screen modal_example():
    modal True

    frame:
        xalign 0.5 ypos 50
        textbutton _("Activar modo de juego con Levi"):
            action Return("modal_example")

screen style_prefix_screen():
    style_prefix "red"

    frame:
        xalign 0.5 ypos 50
        text _("Has cambio de personaje.")

style red_frame:
    background "#440000d9"

style red_text:
    color "#ffc0c0"

screen style_prefix_screen2():
    style_prefix "red"

    frame:
        xalign 0.5 ypos 50
        text _("Modo Levi desactivado.")

style red_frame:
    background "#440000d9"

style red_text:
    color "#ffc0c0"






screen modal_example2():
    modal True

    frame:
        xalign 0.5 ypos 50
        textbutton _("Activar modo de juego con Eren"):
            action Return("modal_example")

screen style_prefix_screen1():
    style_prefix "red"

    frame:
        xalign 0.5 ypos 50
        text _("Has cambio de personaje.")

style red_frame:
    background "#440000d9"

style red_text:
    color "#ffc0c0"

screen style_prefix_screen3():
    style_prefix "red"

    frame:
        xalign 0.5 ypos 50
        text _("Modo Eren desactivado.")

style red_frame:
    background "#440000d9"

style red_text:
    color "#ffc0c0"


screen textstyle():
    frame:
        textbutton _("Estas en una Pesadilla"):
            text_color "#c04040"
            text_hover_color "#ff0000"
            action Return(True)

        at examplepos
