from PIL import Image

#create new image by import 
image = Image.open('cat01.jpg')

# show the picture 
# image.show('cat01.jpg ')

#alternative way to import an imange
# with Image.open('cat01.jgp') as image:
#    image.show()


#creat a new image from scratch 
# image_blank = Image.new('RGB', (1000,600))

#show the picture
# image_blank.show()

#saving this picture 
# image_blank.save()

print(image.size)
print(image.filename)
print(image.format)
print(image.format_description)