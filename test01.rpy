init python:
    def change_stat(stat, amount):
        stat += amount
        if stat > 100:
            stat = 100
        elif stat < 0:
            stat = 0
        return stat









screen life_player:
    bar:
        value life
        left_bar Frame ("gui/bar/bar2.png")
        right_bar Frame ("gui/bar/bar.png")
        thumb "#a7a400"
        range 100
        xalign 0.1
        xysize (200, 25)
    text "{color=#FFFFFF}Mikasa [life]{/color}":
        xalign 0.1


screen life_enemy:
    bar:
        value life_e
        left_bar Frame ("#00b034")
        right_bar Frame ("#6c000a")
        thumb "#a7a400"
        range 100
        xalign 0.3
        xysize (200, 25)
    text "{color=#FFFFFF}Eren [life_e]{/color}":
        xalign 0.3
