from PIL import Image
im = Image.open('screenshot.jpg')
print("size is: ",im.size)
width, height = im.size
# path_1 = ".\\tutorialimages\\"
# im.crop((250, 250, 280, 280)).save(path_1 + 'Cropped_image_small1.jpeg')
im.crop((250, 250, 280, 280)).save('Cropped_image_small.jpeg')