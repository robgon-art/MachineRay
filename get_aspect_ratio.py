import numpy as np

# Initialize the x and y arrays
x = np.linspace(0, 849, 850)
y = np.empty(shape=(850))

# Read the file containing the paintings and aspect ratios
info_file = open('painting_info.txt', 'r') 
lines = info_file.readlines() 

# Loop through the lines, capturing the aspect ratio in the y array
count = 0
for line in lines: 
    parts = line.split(' ')
    if len(parts) == 2 and len(parts[1]) > 0:
      y[count] = parts[1]
    count += 1

# Sort the values
y = np.sort(y)

# Use piecewise linear interpolation
def get_aspect_ratio():
  input_x = np.random.rand(1)*850
  y_interp = np.interp(input_x, x, y)
  return y_interp[0]
