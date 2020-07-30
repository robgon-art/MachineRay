import numpy as np
from PIL import Image 
from matplotlib.pyplot import figure
from os import listdir
from scipy.spatial import distance

from_path = 'art/wikiart/'
to_path   = 'art/cropped/'

def find_left():
    left = 0
    for i in range(0, w_pad):
        r_stdev = np.std(np_img[h_pad:-h_pad,i:i+1,0:1])
        g_stdev = np.std(np_img[h_pad:-h_pad,i:i+1,1:2])
        b_stdev = np.std(np_img[h_pad:-h_pad,i:i+1,2:3])
        if r_stdev*r_stdev+g_stdev*g_stdev+b_stdev*b_stdev > thresh1:
            break

        r_med = np.median(np_img[h_pad:-h_pad,i:i+1,0:1])
        g_med = np.median(np_img[h_pad:-h_pad,i:i+1,1:2])
        b_med = np.median(np_img[h_pad:-h_pad,i:i+1,2:3])
        dst = distance.euclidean((r_med, g_med, b_med), (r_global_med, g_global_med, b_global_med))
        if dst < thresh2:
            break

        left = left+1
    return left

def find_top():
    top = 0
    for i in range(0, h_pad):
        r_stdev = np.std(np_img[i:i+1,w_pad:-w_pad,0:1])
        g_stdev = np.std(np_img[i:i+1,w_pad:-w_pad,1:2])
        b_stdev = np.std(np_img[i:i+1,w_pad:-w_pad,2:3])
        if r_stdev*r_stdev+g_stdev*g_stdev+b_stdev*b_stdev > thresh1:
            break

        r_med = np.median(np_img[i:i+1,w_pad:-w_pad,0:1])
        g_med = np.median(np_img[i:i+1,w_pad:-w_pad,1:2])
        b_med = np.median(np_img[i:i+1,w_pad:-w_pad,2:3])
        dst = distance.euclidean((r_med, g_med, b_med), (r_global_med, g_global_med, b_global_med))
        if dst < thresh2:
            break

        top = top+1
    return top

def find_right(right):
    right = w
    for i in range(0, w_pad):
        r_stdev = np.std(np_img[h_pad:-h_pad,w-i-1:w-i,0:1])
        g_stdev = np.std(np_img[h_pad:-h_pad,w-i-1:w-i,1:2])
        b_stdev = np.std(np_img[h_pad:-h_pad,w-i-1:w-i,2:3])
        if r_stdev*r_stdev+g_stdev*g_stdev+b_stdev*b_stdev > thresh1:
            break

        r_med = np.median(np_img[h_pad:-h_pad,w-i-1:w-i,0:1])
        g_med = np.median(np_img[h_pad:-h_pad,w-i-1:w-i,1:2])
        b_med = np.median(np_img[h_pad:-h_pad,w-i-1:w-i,2:3])
        dst = distance.euclidean((r_med, g_med, b_med), (r_global_med, g_global_med, b_global_med))
        if dst < thresh2:
            break

        right = right-1
    return right

def find_bottom(bottom):
    for i in range(0, h_pad):
        r_stdev = np.std(np_img[h-i-1:h-i,w_pad:-w_pad,0:1])
        g_stdev = np.std(np_img[h-i-1:h-i,w_pad:-w_pad,1:2])
        b_stdev = np.std(np_img[h-i-1:h-i,w_pad:-w_pad,2:3])
        if r_stdev*r_stdev+g_stdev*g_stdev+b_stdev*b_stdev > thresh1:
            break

        r_med = np.median(np_img[h-i-1:h-i,w_pad:-w_pad,0:1])
        g_med = np.median(np_img[h-i-1:h-i,w_pad:-w_pad,1:2])
        b_med = np.median(np_img[h-i-1:h-i,w_pad:-w_pad,2:3])
        dst = distance.euclidean((r_med, g_med, b_med), (r_global_med, g_global_med, b_global_med))
        if dst < thresh2:
            break

        bottom = bottom-1
    return bottom

for file in listdir(from_path):

    img = Image.open(from_path + '/' + file)
    print(file)

    np_img = np.asarray(img)
    print("shape = " + str(np_img.shape))

    thresh1 = 15000
    thresh2 = 30
    w = img.width
    h = img.height
    pad = 30
    w_pad = w//pad
    h_pad = h//pad

    r_global_med = np.median(np_img[h_pad:-h_pad,w_pad:-w_pad,0:1])
    g_global_med = np.median(np_img[h_pad:-h_pad,w_pad:-w_pad,1:2])
    b_global_med = np.median(np_img[h_pad:-h_pad,w_pad:-w_pad,2:3])

    left = find_left()
    top = find_top()
    right = find_right(w)
    bottom = find_bottom(h)

    print("left = " + str(left) + ", top = " + str(top) +
        ", right = " + str(right) +  ", bottom = " + str(bottom) + "\n")

    img.save(to_path  + file)                                   # save the original
    cropped_img = img.crop((left, top, right, bottom))
    cropped_img.save(to_path  + file[:-4] + "_cropped.jpg")     # and the cropped version
