import secrets, os
from PIL import Image
from Sakha import app




def save_post_pic(pic):
    random_hex = secrets.token_hex(16)
    _, ext = os.path.splitext(pic.filename)
    mod_pic = random_hex + ext
    path = os.path.join(app.config['UPLOAD_PATH'], 'static', 'user-images', mod_pic)

    img_size = (800, 800)
    img = Image.open(pic)
    img.thumbnail(img_size)
    img.save(path)
    return mod_pic