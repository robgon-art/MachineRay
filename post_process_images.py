import numpy as np
from PIL import Image
from ISR.models import RDN, RRDN

img = Image.open('input.png')
model = RRDN(weights='gans')

npimg = np.array(img)
row,col,ch= npimg.shape
mean = 0
var = 0.1
sigma = var**0.5
gauss = np.random.normal(mean,sigma,(row,col,ch))*24
gauss = gauss.reshape(row,col,ch)
noisy = np.clip(npimg + gauss, 0, 255).astype('uint8')
noisy_image = Image.fromarray(noisy)
big_np = model.predict(np.array(noisy_image))
big_img = Image.fromarray(big_np)

big_img.save("big.jpg")
