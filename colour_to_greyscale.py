from PIL import Image

im = Image.open('1deathstroke_the_terminator_by_uncannyknack-d77aghn.jpg')
pixelMap = im.load()

img_average = Image.new( im.mode, im.size)
img_lightness = Image.new( im.mode, im.size)
img_luminosity = Image.new( im.mode, im.size)
img_best = Image.new( im.mode, im.size)

pixelsNew_average = img_average.load()
pixelsNew_lightness = img_lightness.load()
pixelsNew_luminosity = img_luminosity.load()
pixelsNew_best = img_best.load()

for i in range(img_average.size[0]):
    for j in range(img_average.size[1]):
        # average mtd
        val1 = int((pixelMap[i,j][0] + pixelMap[i,j][1] + pixelMap[i,j][2])/3)
        tuple1 = (val1, val1, val1)
        pixelsNew_average[i,j] = tuple1

        # lightness mtd
        val2 = int((max(pixelMap[i,j]) + min(pixelMap[i,j]))/2)
        tuple1 = (val2, val2, val2)
        pixelsNew_lightness[i,j] = tuple1

        # luminosity mtd
        val3 = int((pixelMap[i,j][0]*0.21) + (pixelMap[i,j][1]*0.72) + (pixelMap[i,j][2]*0.07))
        tuple1 = (val3, val3, val3)
        pixelsNew_luminosity[i,j] = tuple1

        # best pixel of above 3 algo
        val_best = max((val1, val2, val3))
        tuple1 = (val_best, val_best, val_best)
        pixelsNew_best[i,j] = tuple1

im.close()
     
img_average.save("grey_average.jpg") 
img_average.close()

img_lightness.save("grey_lightness.jpg") 
img_lightness.close()

img_luminosity.save("grey_luminosity.jpg") 
img_luminosity.close()

img_best.save("grey_best.jpg") 
img_best.close()