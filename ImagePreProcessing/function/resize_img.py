from PIL import Image

def resize_img(file_name):
    width = 300
    height = 300

    img = Image.open(file_name)
    img_resize = img.resize(width, height)
    img_resize.save(file_name)
    return file_name
