import random

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
bright_red = (200, 0, 0)
bright_green = (0, 200, 0)
bright_blue = (0, 0, 200)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (211,211,211)
diff_grey = (190, 190, 190)


def rand_color():
    r = random.randrange(0, 255)
    g = random.randrange(0, 255)
    b = random.randrange(0, 255)
    color = (r, g, b)

    return color
