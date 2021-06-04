from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'https://i.ytimg.com/vi/MPV2METPeJU/maxresdefault.jpg'

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter.
    It loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixel's red component by
    :param green_scale: A number to multiply each pixel's green component by
    :param blue_scale: A number to multiply each pixel's blue component by
    Returns the newly generated patch.
    '''
    patch = SimpleImage(PATCH_NAME)
    for y in range(patch.height):
        for x in range(patch.width):
            pixel = patch.get_pixel(x, y)
            pixel.red = pixel.red * red_scale
            pixel.green = pixel.green * green_scale
            pixel.blue = pixel.blue * blue_scale
    return patch

def warhol_quilt(image, patch, x_image_order, y_image_order):
    width = patch.width
    height = patch.height
    for y in range(patch.height):
        for x in range(patch.width):
            start_x = x + width * x_image_order  
            start_y = y + height * y_image_order 
            pixel = patch.get_pixel(x, y)
            image.set_pixel(start_x, start_y, pixel)
    return image

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    # TODO: your code here
    # This is an example which should generate a pinkish patch
    pink_patch = make_recolored_patch(1.5, 0, 1.5)
    og_patch = make_recolored_patch(1, 1, 1)  
    green_patch = make_recolored_patch(1.02, 1.64, 1.24)  
    bright_patch = make_recolored_patch(1.9, 1.9, 1.9)  
    blue_patch = make_recolored_patch(.47, .97, 2.47)  
    yellow_patch = make_recolored_patch(1.5, 1.7, 0.5)  


    warhol_quilt(final_image, pink_patch, 0, 0)
    warhol_quilt(final_image, og_patch, 1, 1)
    warhol_quilt(final_image, green_patch, 1, 0)
    warhol_quilt(final_image, bright_patch, 2, 0)
    warhol_quilt(final_image, blue_patch, 2, 1)
    final_image = warhol_quilt(final_image, yellow_patch, 0, 1)
    final_image.show()

if __name__ == '__main__':
    main()+