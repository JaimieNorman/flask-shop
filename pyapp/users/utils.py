import os
import secrets

from PIL import Image
from flask_mail import Message
from flask import url_for, current_app

from pyapp import mail


def save_image(form_image):
    random_hex = secrets.token_hex(8)
    _, fileExtension = os.path.splitext(form_image.filename)
    image_filename = random_hex + fileExtension
    image_path = os.path.join(current_app.root_path, 'static/profile_pics', image_filename)
    output_size = (125, 125)
    image = Image.open(form_image)
    image.thumbnail(output_size)
    image.save(image_path)
    return image_filename


def send_reset_email(user):
    token = user.get_reset_token()
    message = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    message.body = f''' Visit the following link to reset your password:
{url_for('reset_token', token=token, _external=True)}

If you did not make this request, ignore this email.
'''

    mail.send(message)
