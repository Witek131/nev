from PIL import Image, ImageDraw


def gradient(color):
    new_image = Image.new("RGB", (512, 200), (0, 0, 0))  
    draw = ImageDraw.Draw(new_image)
    r = 0
    g = 0
    b = 0
    if color == 'R' or color == 'r':
        r = 255
    elif color == 'G' or color == 'g':
        g = 255
    else:
        b = 255
    x = 512
    for i in range(256):
        for i in range(2):
            print(i)
            draw.line((x - i, 0, x - i, 200), fill=(r, g, b), width=1)
        x -= 2
        if r > 0:
            r -= 1
        elif g > 0:
            g -= 1
        else:
            b -= 1
    new_image.save('res.png', "PNG")
    
gradient('G')
