## Pantalla de menú rápido #####################################################
##
## El menú rápido es presentado en el juego para ofrecer fácil acceso a los
## menus externos al juego.

screen quick_menu():

    ## Asegura que esto aparezca en la parte superior de otras pantallas.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

###basado en imagebutton
#screen de mi menupeque:

    imagebutton idle "inv_idle" xpos 1800 ypos 25 hover "inv_hover" focus_mask True action [Show ("flor"), Hide ("quick_menu")]


screen flor:
    modal True

    imagebutton idle "inv_idle" hover "inv_hover" xpos 1800 ypos 25 focus_mask True action [ Hide ("flor"), Show ("quick_menu")]

#############################################################################################################################

    imagebutton idle "auto" hover "auto_hover" xpos 1700 ypos 25 focus_mask None action Preference("auto-forward", "toggle")

    imagebutton idle "historial" hover "historial_hover" xpos 1400 ypos 25 focus_mask None action ShowMenu('history')

    imagebutton idle "guardar" hover "guardar_hover" xpos 1500 ypos 25 focus_mask None action ShowMenu('save')

    imagebutton idle "opciones" hover "opciones_hover" xpos 1300 ypos 25 focus_mask None action ShowMenu("preferences")

    imagebutton idle "salir" hover "salir_hover" xpos 1200 ypos 25 focus_mask None action Quit(confirm=not main_menu)

    imagebutton idle "saltar" hover "saltar_hover" xpos 1600 ypos 25 focus_mask None action Skip() alternate Skip(fast=True, confirm=True)


## Este código asegura que la pantalla 'quick_menu' se muestra en el juego,
## mientras el jugador no haya escondido explícitamente la interfaz.
#init python:
    #config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
