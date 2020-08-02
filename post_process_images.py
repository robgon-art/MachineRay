import numpy as np
from PIL import Image
from ISR.models import RDN, RRDN

# Import the image
img = Image.open('input.png')

# Load the GAN model that will perform a 4x resize
model = RRDN(weights='gans')

# Convert to numpy image
npimg = np.array(img)
row,col,ch= npimg.shape

# Add some noise
mean = 0
var = 0.1
sigma = var**0.5
gauss = np.random.normal(mean,sigma,(row,col,ch))*24

# Reshape and clip the pixel values
gauss = gauss.reshape(row,col,ch)
noisy = np.clip(npimg + gauss, 0, 255).astype('uint8')
noisy_image = Image.fromarray(noisy)

# Do the resize
big_np = model.predict(np.array(noisy_image))

# Save the image
big_img = Image.fromarray(big_np)
big_img.save("big.jpg")
