"""
File: bluescreen.py
--------------------
This program shows an example of "greenscreening" (actually
"bluescreening" in this case).  This is where we replace the
pixels of a certain color intensity in a particular channel
(here, we use blue) with the pixels from another image.
"""


from simpleimage import SimpleImage
from PIL import Image


INTENSITY_THRESHOLD = 1.4


def bluescreen(main_filename, back_filename):
    """
    Implements the notion of "bluescreening".  That is,
    the image in the main_filename has its "sufficiently blue"
    pixels replaced with pixel from the corresponding x,y
    location in the image in the file back_filename.
    Returns the resulting "bluescreened" image.
    """
    image = SimpleImage(main_filename)
    back = SimpleImage(back_filename)

    # See if this pixel is "sufficiently" blue
    # If so, we get the corresponding pixel from the
    # back image and overwrite the pixel in
    # the main image with that from the back image.
    # Add your code hear
    for pixel in image:
        average = (pixel.red + pixel.green + pixel.blue) / 3
        if pixel.blue >= average * INTENSITY_THRESHOLD:
            back_pixel = back.get_pixel(pixel.x, pixel.y)
            pixel.red = back_pixel.red
            pixel.green = back_pixel.green
            pixel.blue = back_pixel.blue

    return image


def main():
    """
    Run your desired image manipulation functions here.
    You should store the return value (image) and then
    call .show() to visualize the output of your program.
    """
    cat = Image.open('images/blue.png')
    cat_resized = cat.resize((1200, 1500))
    cat_resized.save('images/cat_blue.png')
    
    bg = Image.open('images/background.png') 
    bg_resized = bg.resize((1200, 1500))
    bg_resized.save('images/background_small.png')
    
    original_cat = SimpleImage('images/cat_blue.png')
    original_cat.show()

    original_bg = SimpleImage('images/background_small.png')
    original_bg.show()

    cat_bg_replaced = bluescreen('images/cat_blue.png', 'images/background_small.png')
    cat_bg_replaced.show()
    cat_bg_replaced.pil_image.save('images/cat_with_new_background.png')

if __name__ == '__main__':
    main()
