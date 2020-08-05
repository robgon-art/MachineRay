# MachineRay
By Robert. A Gonsalves
![MachineRay Output](https://github.com/robgon-art/MachineRay/blob/master/images/big2.jpg)

For this project, I gathered images of abstract paintings from WikiArt.org, processed them, and fed them into StyleGAN2 at the size of 1024x1024.
I trained the GAN for three weeks on a GPU using Google Colab.
I then processed the output images by adjusting the aspect ratio and running them through another ANN for a super-resolution resize.
The resultant images are 4096 pixels wide or tall, depending on the aspect ratio.

You can read my article about this project on Medium here: [MachineRay: Using AI to Create Abstract Art](https://towardsdatascience.com/machineray-using-ai-to-create-abstract-art-39829438076a)

This GitHub repositoray contains the source code for the project.

The source code is released under the CC BY-NC-SA license. See License.txt for details.</br>
![CC BY-NC-SA](https://licensebuttons.net/l/by-nc-sa/3.0/88x31.png)
