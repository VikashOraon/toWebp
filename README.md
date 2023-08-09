# Batch Image Conversion and Resizing Script

This Python script allows you to batch convert JPEG images to WEBP format while also resizing them. It processes images in sub-folders of an "Image" directory, creating corresponding output sub-folders for the resized images.

## Prerequisites

- Python 3.x
- Pillow (PIL) library

You can install the required library using the following command:
```bash
pip install Pillow
```
## Usage

1. Place your JPEG images in sub-folders within the "Image" directory.
2. Clone or download this repository to your local machine.

    https://github.com/VikashOraon/toWebp.git
3. Open a terminal and navigate to the project directory.

    `cd your-repo`
4. Customize the script parameters:

   - Modify the `new_width` and `new_height` variables to define the desired dimensions for the resized images.
   - Adjust the `quality` parameter to control the compression quality of the output WEBP images.
5. Run the script:

    `python main.py`

The script will process each sub-folder in the "Image" directory. For each sub-folder, it will create an output directory with the same name in the "output" directory. The JPEG images will be converted to WEBP format, resized, and saved in the corresponding output sub-folder.

## Example

Suppose your "Image" directory structure is as follows:

    Image/
    |-- Subfolder1/
    | |-- image1.jpg
    | |-- image2.jpg
    |
    |-- Subfolder2/
    | |-- image3.jpg
    | |-- image4.jpg

After running the script, the "output" directory structure will be:

    output/
    |-- Subfolder1/
    | |-- image1.webp
    | |-- image2.webp
    |
    |-- Subfolder2
    | |-- image3.webp
    | |-- image4.webp


