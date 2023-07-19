from PIL import Image

# Open the JPEG image
jpeg_image = Image.open("cat01.jpg")

# Convert the image to WebP format
webp_image_path = "cat01_output.webp"
jpeg_image.save(webp_image_path, "WebP")

print("Conversion complete. WebP image saved as", webp_image_path)
