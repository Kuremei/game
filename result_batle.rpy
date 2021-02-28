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
    "¡Derrota!"
    return





label win:
    hide eren with dissolve
    pause 1

    "¡Victoria!"
    jump siguiente
