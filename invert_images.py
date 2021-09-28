from pdf2image import convert_from_path
from PIL import Image
import numpy as np

_in_file_ = "./figs/data_scientist_simple_design_logos.pdf"
_out_file_ = "./figs/inverted_business_card"

images = convert_from_path(_in_file_)
img = np.array(images[0])
img_array = np.array(img)
I_max = 255 # img_array.max()
img_array = I_max - img_array
x, y = 0, img_array.shape[0]
h, w = 633, 1083
crop = img_array[y-h:y, x:x+w]

inverted_img_cropped = Image.fromarray(crop)
inverted_img_cropped.save(_out_file_ + ".jpg")

img1 = Image.open(_out_file_ + ".jpg")
im1 = img1.convert("RGB")
im1.save(_out_file_ + ".pdf")