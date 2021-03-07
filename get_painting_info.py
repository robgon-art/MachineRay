from PIL import Image
import os
cropped_fie_path = "art/cropped/"

# Create a file containing the file names and aspect ratios for the paintings
info_file = open('painting_info.txt', 'w') 

# Loop through the files
path, dirs, files = next(os.walk(cropped_fie_path))
for file in sorted(files):
  image = Image.open(os.path.join(path,file))
  width, height = image.size
  aspect = width / height
  info_file.write(file + " " + str(aspect) + "\n")
  print(file, aspect)

info_file.close()
