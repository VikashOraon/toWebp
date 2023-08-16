from PIL import Image
import os



def resize_to_fit(img, max_width, max_height):
    width, height = img.size
    aspect_ratio = width / height

    if width > max_width or height > max_height:
        if aspect_ratio > 1:
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
        else:
            new_height = max_height
            new_width = int(max_height * aspect_ratio)

        return img.resize((new_width, new_height), Image.LANCZOS)
    return img


def convert_jpeg_to_webp(input_path, output_path, max_width, max_height, quality=80):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for filename in os.listdir(input_path):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_path, os.path.splitext(filename)[0] + '.webp')

            img = Image.open(input_file)
            resized_img = resize_to_fit(img, max_width, max_height)
            resized_img.save(output_file, 'webp', quality=quality)
            print(f"Converted and resized {input_file} to {output_file}")

if __name__ == "__main__":
    # Replace with the path to your "images" directory
    image_directory = "images"
    # max width for resized images
    max_width = 1920
    # max height for resized images
    max_height = 1080
    # Adjust the quality as needed (0-100)
    quality = 80
    # images/[...] --> output/[...]
    for subfolder_name in os.listdir(image_directory):
        subfolder_path = os.path.join(image_directory, subfolder_name)
        if os.path.isdir(subfolder_path):
            output_directory = os.path.join("output", subfolder_name)
            convert_jpeg_to_webp(subfolder_path, output_directory, max_width, max_height, quality)
