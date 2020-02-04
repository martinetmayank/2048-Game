black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 152, 0)
deep_orange = (255, 87, 34)
brown = (121, 85, 72)
green = (0, 128, 0)
light_green = (139, 195, 74)
teal = (0, 150, 136)
blue = (33, 150, 136)
purple = (156, 39, 176)
pink = (234, 30, 99)
deep_purple = (103, 58, 183)


color_dict = {
    0: black,
    2: red,
    4: green,
    8: purple,
    16: deep_purple,
    32: deep_orange,
    64: teal,
    128: light_green,
    256: pink,
    512: orange,
    1024: black,
    2048: brown
}


def getColor(tile_number):
    """
    Returns the color for specific number.

    Arguments:\n
        :tileNumber: the tile for which you require color.
    """
    return color_dict[tile_number]
