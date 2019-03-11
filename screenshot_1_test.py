# import PIL.ImageGrab

# im = PIL.ImageGrab.grab()     
# im.show() 

from PIL import ImageGrab
snapshot = ImageGrab.grab()
print(type(snapshot))
save_path = "screenshot.jpg"
# snapshot.save(save_path)