from PIL import Image

img_name = input("Enter image name:")
im1 = Image.open(img_name)
im1.show()
im1.close()