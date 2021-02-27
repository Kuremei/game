label lose:
    hide mikasa with hpunch
    scene pele with fade
    pause 3
    show gi:
        linear 0.1 xpos 0 ypos 0
        linear 1 xpos 100 ypos 100
        linear 1 xpos 0 ypos 0
        linear 1 xpos -100 ypos -100
        linear 1 xpos 0 ypos 0
        repeat


    with dissolve
    "HAS PERDIDO LA BATALLA"
    return





label win:
    hide eren with dissolve
    pause 1

    "VICTORIA!!!"
    jump siguiente
