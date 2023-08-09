from PIL import Image
import os

def convert_jpeg_to_webp(input_path, output_path, new_width, new_height, quality=80):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    for filename in os.listdir(input_path):
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
            input_file = os.path.join(input_path, filename)
            output_file = os.path.join(output_path, os.path.splitext(filename)[0] + '.webp')

            img = Image.open(input_file)
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)
            resized_img.save(output_file, 'webp', quality=quality)
            print(f"Converted and resized {input_file} to {output_file}")

if __name__ == "__main__":
    # Replace with the path to your "Album" directory
    album_directory = "albums"
    # New width for resized images
    new_width = 1920
    # New height for resized images
    new_height = 1080
    # Adjust the quality as needed (0-100)
    quality = 80
    # albums/[...] --> output/[...]
    for subfolder_name in os.listdir(album_directory):
        subfolder_path = os.path.join(album_directory, subfolder_name)
        if os.path.isdir(subfolder_path):
            output_directory = os.path.join("output", subfolder_name)
            convert_jpeg_to_webp(subfolder_path, output_directory, new_width, new_height, quality)
