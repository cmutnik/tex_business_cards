from PIL import Image
import numpy as np
from pdf2image import convert_from_path

_in_file_ = "./figs/data_scientist_simple_design_logos.pdf"
_out_file_ = "./figs/inverted_business_card.jpg"

images = convert_from_path(_in_file_)
img = np.array(images[0])
# img = Image.open(r"test.jpg")
img_arry = np.array(img)
I_max = 255
img_arry = I_max - img_arry
inverted_img = Image.fromarray(img_arry)
inverted_img.save(_out_file_)