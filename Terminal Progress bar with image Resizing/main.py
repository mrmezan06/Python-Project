from tqdm import tqdm
from PIL import Image
import os
import time
from time import sleep


def resize_image(size, image):
    if os.path.isfile(image):
        try:
            im = Image.open(image)
            im.thumbnail(size, Image.ANTIALIAS)
            im.save("resize/" + str(time.time()) + "_" + str(image))
        except Exception as e:
            print(e)


path = "./image"
# input("Enter the path of an images: ")
size = input("Enter the size of an image(Height,Width): ")
size = tuple(map(int, size.split(',')))

os.chdir(path)
list_of_images = os.listdir()
print(list_of_images)
if "resize" not in list_of_images:
    os.mkdir("resize")

for image in tqdm(list_of_images):
    resize_image(size, image)
    sleep(0.1)
print("Done")
