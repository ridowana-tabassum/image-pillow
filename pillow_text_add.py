from PIL import Image, ImageDraw, ImageFont

# Open the image
image = Image.open("cat01.jpg")

# Create a drawing object
draw = ImageDraw.Draw(image)

# Specify the text content
text = "Stop Calling Me MR. Fluffy"

# Specify the font style and size
font = ImageFont.truetype("arial.ttf", 36)

# Specify the text position
position = (100, 30)

# Specify the text color
text_color = (255, 255, 255)  # white

# Add the text to the image
draw.text(position, text, font=font, fill=text_color)

# Save the modified image
image.save("cat01_text_output.jpg")

print("Text added to the image. Saved as output.jpg.")
