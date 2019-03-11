from PIL import Image
# import sys
im = Image.open("0.1.png")
print("size is: ",im.size)
width, height = im.size
px = im.load()
pixel_line = ""
for i in range(0,width):
    for j in range(0,height):
        pixel_line = px[i,j]
        print(pixel_line, pixel_line[1])
    print("")
print("size is: ",im.size)
