from PIL import Image
import os
import json


class ImageInfo:
    """
    A class to gather and report metadata of images in a specified directory.

    Attributes:
        images_dir (str): The directory where images are stored.
    """

    def __init__(self, images_dir):
        """
        Initializes the ImageInfo object with the directory containing images.

        Args:
            images_dir (str): The directory where images are stored.
        """
        self.images_dir = images_dir

    def get_image_metadata(self, image_path):
        """
        Retrieves metadata for a given image.

        Args:
            image_path (str): The path to the image file.

        Returns:
            dict: A dictionary containing image metadata, such as width, height, name, mode, and format.
        """
        with Image.open(image_path) as img:
            metadata = {}
            try:
                metadata['width'] = img.width
                metadata['name'] = image_path.split('/')[-1]
                metadata['height'] = img.height
                metadata['mode'] = img.mode
                metadata['format'] = img.format
            except KeyError as e:
                pass  # In case any metadata is missing or inaccessible

            return metadata

    def create_cv_report(self):
        """
        Creates a CSV report with metadata of all images in the specified directory.

        The report is saved as 'report.csv' in the current working directory.
        Each line in the CSV contains a JSON-encoded dictionary of an image's metadata.
        """
        images = os.listdir(self.images_dir)
        with open('report.csv', 'w') as file:
            for image in images:
                metadata = self.get_image_metadata(self.images_dir + '/' + image)
                print(f"Writing image info {metadata['name']} to file")
                file.write(json.dumps(metadata) + '\n')


# Example usage
image_info = ImageInfo('images')  # Initialize with the path to your images directory
image_info.create_cv_report()  # Generate the report
