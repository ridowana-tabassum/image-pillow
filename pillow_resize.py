from PIL import Image, ImageColor

# https://pillow.readthedocs.io/en/stable/handbook/index.html

# image import
image = Image.open('cat01.jpg')


#bad example 
#resize 
# image_resize = image.resize((600,1000))
#display
# image_resize.show()

#better example
scale_factor = 2 
new_image_size = (image.size[0] * scale_factor, image.size[1] * scale_factor)
image_resize_better = image.resize(new_image_size)

#display
image_resize_better.show()

#save image
image_resize_better.save('cat01_resize_double_resolution.jpg')