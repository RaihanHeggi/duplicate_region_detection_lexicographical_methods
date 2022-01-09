import cv2
from matplotlib import pyplot as plt
from skimage.util import random_noise

image_path = 'Kuda Duplikat.jpg'
I = cv2.imread(image_path, 1)
gauss = random_noise(I, mode='gaussian', seed=None, clip=True)
sp = random_noise(I, mode='s&p', seed=None, clip=True)
localvar = random_noise(I, mode='localvar', seed=None, clip=True)
poison = random_noise(I, mode='poison', seed=None, clip=True)
salt = random_noise(I, mode='salt', seed=None, clip=True)
pepper = random_noise(I, mode='pepper', seed=None, clip=True)
speckle = random_noise(I, mode='speckle', seed=None, clip=True)

plt.subplot(241), plt.imshow(I), plt.title('Origin')
plt.subplot(242), plt.imshow(gauss), plt.title('Gaussian')
plt.subplot(243), plt.imshow(sp), plt.title('Salt & pepper')
plt.subplot(244), plt.imshow(localvar), plt.title('Loalvar')
plt.subplot(245), plt.imshow(poison), plt.title('Poison')
plt.subplot(246), plt.imshow(salt), plt.title('Salt')
plt.subplot(247), plt.imshow(pepper), plt.title('Pepper')
plt.subplot(248), plt.imshow(speckle), plt.title('Speckle')

plt.show()
