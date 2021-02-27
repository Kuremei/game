init python:

    def MaxScale(img, minwidth=config.screen_width, minheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(minwidth) / currwidth
        yscale = float(minheight) / currheight

        if xscale > yscale:
            maxscale = xscale
        else:
            maxscale = yscale

        return im.FactorScale(img, maxscale, maxscale)

    def MinScale(img, maxwidth=config.screen_width, maxheight=config.screen_height):
        currwidth, currheight = renpy.image_size(img)
        xscale = float(maxwidth) / currwidth
        yscale = float(maxheight) / currheight

        if xscale < yscale:
            minscale = xscale
        else:
            minscale = yscale

        return im.FactorScale(img, minscale, minscale)

    maxnumx = 2
    maxnumy = 2
    maxthumbx = config.screen_width / (maxnumx + 1)
    maxthumby = config.screen_height / (maxnumy + 1)
    maxperpage = maxnumx * maxnumy
    gallery_page = 0
    closeup_page = 0


    class GalleryItem:
        def __init__(self, name, images, thumb, locked="lockedthumb"):
            self.name = name
            self.images = images
            self.thumb = thumb
            self.locked = locked
            self.refresh_lock()

        def num_images(self):
            return len(self.images)

        def refresh_lock(self):
            self.num_unlocked = 0
            lockme = False
            for img in self.images:
                if not renpy.seen_image(img):
                    lockme = True
                else:
                    self.num_unlocked += 1
            self.is_locked = lockme

    gallery_items = []
    gallery_items.append(GalleryItem("{color=#FFFFFF}Cap 1{/color}", ["img1", "img1b", "img2", "img2b" ], "thumb1"))
    gallery_items.append(GalleryItem("{color=#FFFFFF}Cap 2{/color}", ["img3", "img3b" ], "thumb2"))
    gallery_items.append(GalleryItem("{color=#FFFFFF}Cap 3{/color}", ["img4", "img4b", "img5", "img5b" ], "thumb3"))
    gallery_items.append(GalleryItem("{color=#FFFFFF}Cap 4{/color}", ["img6", "img6b", "img7", "img7b", "img8" ], "thumb4"))
    gallery_items.append(GalleryItem("{color=#FFFFFF}Cap 5{/color}", ["img8b", "img9", "img9b", "img10", "img10b" ], "thumb5"))
    gallery_items.append(GalleryItem("{color=#FFFFFF}Cap 6{/color}", ["img11", "img11b", "img12" ], "thumb6"))
    gallery_items.append(GalleryItem("{color=#FFFFFF}Cap 7{/color}", ["img12b", "img13", "img13b" ], "thumb7"))
    gallery_items.append(GalleryItem("{color=#FFFFFF}Cap 8{/color}", ["img14", "img14b", "img15", "img15b", "img16" ], "thumb8"))
    gallery_items.append(GalleryItem("{color=#FFFFFF}Cap 9{/color}", ["img16b", "img17", "img17b", "img18"  ], "thumb9"))
