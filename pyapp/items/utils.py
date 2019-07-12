import os
import secrets

from PIL import Image
from flask import current_app


def save_image(form_image):
    random_hex = secrets.token_hex(8)
    _, fileExtension = os.path.splitext(form_image.filename)
    image_filename = random_hex + fileExtension
    image_path = os.path.join(current_app.root_path, 'static/item_pics', image_filename)
    output_size = (768, 768)
    image = Image.open(form_image)
    image.thumbnail(output_size)
    image.save(image_path)
    return image_filename
