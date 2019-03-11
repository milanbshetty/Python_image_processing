from PIL import Image, ImageFilter

imageObject = Image.open('Screenshot9.png')

blurred = imageObject.filter(ImageFilter.BLUR)
blurred1 = imageObject.filter(ImageFilter.MinFilter(int(input("even no only: "))))

# blurred = blurred.filter(ImageFilter.BLUR)
blurred.save("blur_img.png")
blurred1.save("blur_img1.png")

imageObject.close()
blurred.close()
blurred1.close()
