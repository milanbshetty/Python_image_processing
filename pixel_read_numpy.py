from PIL import Image
import numpy as np

i = Image.open("0.1.png")
iar = np.asarray(i)
print(iar)