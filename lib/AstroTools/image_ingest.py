# this module used to handle image ingestion using Pillow and other tools

from PIL import Image

im = Image.open("data/TestSub.tif")

print(im.format, im.size, im.mode)

