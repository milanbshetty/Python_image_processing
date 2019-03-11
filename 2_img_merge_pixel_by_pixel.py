from PIL import Image

im1 = Image.open('Screenshot10.png')
pixelMap1 = im1.load()
im2 = Image.open('Screenshot9.png')
pixelMap2 = im2.load()

img_new = Image.new( im1.mode, im1.size)
pixelsNew = img_new.load()
print("loded all img")
for i in range(img_new.size[0]):
    for j in range(img_new.size[1]):
        if(j%2 == 0):
            val1 = pixelMap1[i,j][0], pixelMap1[i,j][1], pixelMap1[i,j][2]
        # print(val1)
        else:
            val1 = pixelMap2[i,j][0], pixelMap2[i,j][1], pixelMap2[i,j][2]
        pixelsNew[i,j] = val1

im1.close()
im2.close()
print("closing")
img_new.save("combined_img.png") 
img_new.close()