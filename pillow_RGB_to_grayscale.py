from PIL import Image, ImageEnhance

# Open the RGB image
rgb_image = Image.open("cat01.jpg")

# Convert the image to grayscale
grayscale_image = rgb_image.convert("L")

#Grayscale by enhancing 
# color_enchancer = ImageEnhance.Color(rgb_image) 
# enhanced_image = color_enchancer.enhance(0) 

# Save the grayscale image
grayscale_image.save("cat01_grayscale_output.jpg")