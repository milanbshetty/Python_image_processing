from PIL import Image

im_rgb = Image.open('Screenshot9.png')
img_cmyk = im_rgb.convert('CMYK')
img_cmyk.save("rgb_to_cmyk.jpg") 
im_rgb.close()
img_cmyk.close()