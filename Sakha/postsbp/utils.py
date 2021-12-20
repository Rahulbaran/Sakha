import secrets, os
from PIL import Image
from flask import current_app




def save_post_pic(pic):
    random_hex = secrets.token_hex(16)
    _, ext = os.path.splitext(pic.filename)
    mod_pic = random_hex + ext
    path = os.path.join(current_app.config['UPLOAD_PATH'], 'static', 'user-images', mod_pic)

    img_size = (1000, 1000)
    img = Image.open(pic)
    img.thumbnail(img_size)
    img.save(path)
    return mod_pic