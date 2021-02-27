init python:
    if(persistent.cap1 == None):
        persistent.cap1 = True
    if(persistent.cap2 == None):
        persistent.cap2 = False
    if(persistent.cap3 == None):
        persistent.cap3 = False
    if(persistent.cap4 == None):
        persistent.cap4 = False
    if(persistent.cap5 == None):
        persistent.cap5 = False
    if(persistent.cap6 == None):
        persistent.cap6 = False
    if(persistent.cap7 == None):
        persistent.cap7 = False
    if(persistent.cap8 == None):
        persistent.cap8 = False
    if(persistent.cap9 == None):
        persistent.cap9 = False
    if(persistent.cap10 == None):
        persistent.cap10 = False
    if(persistent.cap11 == None):
        persistent.cap11 = False
    if(persistent.cap12 == None):
        persistent.cap12 = False


screen capitulos:
    add "images/background.png"
    imagemap:
        ground "images/capitulos idle.png"
        hover "images/capitulos hover.png"

        hotspot(199,133,203,171) action Jump("capitulo1")
        if(persistent.cap2 == True):
            hotspot(538,136,199,170) action Jump("capitulo2")
        if(persistent.cap3 == True):
            hotspot(877,141,201,164) action Jump("capitulo3")
        if(persistent.cap4 == True):
            hotspot(1196,133,203,173) action Jump("capitulo4")
        if(persistent.cap5 == True):
            hotspot(1544,142,208,163) action Jump("capitulo5")
        if(persistent.cap6 == True):
            hotspot(203,432,200,164) action Jump("capitulo6")
        if(persistent.cap7 == True):
            hotspot(548,432,199,170) action Jump("capitulo7")
        if(persistent.cap8 == True):
            hotspot(886,428,204,171) action Jump("capitulo8")
        if(persistent.cap9 == True):
            hotspot(1199,426,211,171) action Jump("capitulo9")
        if(persistent.cap10 == True):
            hotspot(1552,430,213,164) action Jump("capitulo10")
        if(persistent.cap11 == True):
            hotspot(551,749,212,175) action Jump("capitulo11")
        if(persistent.cap12 == True):
            hotspot(895,750,209,165) action Jump("capitulo12")
