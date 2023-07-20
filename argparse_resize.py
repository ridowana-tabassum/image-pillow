import argparse
from PIL import Image

def resize_image(input_path, output_path, new_width, new_height):
    try:
        # Open the image
        image = Image.open(input_path)

        # Resize the image
        resized_image = image.resize((new_width, new_height))

        # Save the resized image to the output path
        resized_image.save(output_path)
        print("Image resized and saved successfully.")
    except Exception as e:
        print("Error occurred while resizing the image:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Resize an image using Pillow')
    parser.add_argument('--input', type=str, required=True, help='Input image path')
    parser.add_argument('--output', type=str, required=True, help='Output image path')
    parser.add_argument('--w', type=int, required=True, help='New width for the resized image')
    parser.add_argument('--h', type=int, required=True, help='New height for the resized image')

    args = parser.parse_args()

    input_image_path = args.input
    output_image_path = args.output
    new_width = args.w
    new_height = args.h

    resize_image(input_image_path, output_image_path, new_width, new_height)
