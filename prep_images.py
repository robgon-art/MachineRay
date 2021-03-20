import os
from PIL import Image
import numpy as np
import imgaug as ia
from imgaug import augmenters as iaa

# set up the file paths
from_path = 'art/cropped/'
to_path = 'art/resized/'

# set up some parameters
size = 1024
num_augmentations = 6

# set up the image augmenter
seq = iaa.Sequential([
    iaa.Rot90((0, 3)),
    # iaa.Fliplr(0.5),
    iaa.PerspectiveTransform(scale=(0.0, 0.05), mode='replicate'),
    iaa.AddToHueAndSaturation((-20, 20))
])

# loop through the images, resizing and augementing
path, dirs, files = next(os.walk(from_path))
for file in sorted(files):
  print(file)
  image = Image.open(path + "/" + file)
  if image.mode == "RGB":
    image.save(to_path + "/" + file)
    image_resized = image.resize((size,size), resample=Image.BILINEAR)
    image_np = np.array(image_resized)
    images = [image_np] * num_augmentations
    images_aug = seq(images=images)
    for i in range(0, num_augmentations):
      im = Image.fromarray(np.uint8(images_aug[i]))
      to_file = to_path + "/" + file[:-4] + '_' + str(i).zfill(2) + '.jpg'
      im.save(to_file) #, quality=95)
