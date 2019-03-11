from PIL import Image
im = Image.open("screenshot.jpg")
save_img = im.rotate(45)
# wont work with images with bg transparent. so try to avoid it. Gets RGBA conversion error
# im.convert("RGBA")
# im = im.convert("RGB")
name = "rotated.jpg"
save_img.save(name)