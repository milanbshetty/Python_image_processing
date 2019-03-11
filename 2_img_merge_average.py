from PIL import Image

im1 = Image.open('Screenshot12.png')
pixelMap1 = im1.load()
im2 = Image.open('Screenshot10.png')
pixelMap2 = im2.load()

img_new = Image.new( im1.mode, im1.size)
pixelsNew = img_new.load()
print("loded all img")
for i in range(img_new.size[0]):
    for j in range(img_new.size[1]):
            val1 = int((pixelMap1[i,j][0] + pixelMap2[i,j][0])/2), int((pixelMap1[i,j][1] + pixelMap2[i,j][1])/2), int((pixelMap1[i,j][2] + pixelMap2[i,j][2])/2)
            pixelsNew[i,j] = val1

im1.close()
im2.close()
print("closing")
img_new.save("combined_img_pixel_average.png") 
img_new.close()