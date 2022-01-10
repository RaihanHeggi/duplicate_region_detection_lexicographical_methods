import cv2
import numpy as np
from skimage.util import random_noise


def add_noise(img, mean=0):
    var = 0.1
    sigma = var ** 1.2
    noisy_image = np.random.normal(mean, sigma, img.shape)
    noisy_image = noisy_image.reshape(img.shape)
    noisy_image = img + noisy_image
    return noisy_image


# def sp_noise(image,prob):
#     '''
#     Add salt and pepper noise to image
#     prob: Probability of the noise
#     '''
#     output = np.zeros(image.shape,np.uint8)
#     thres = 1 - prob
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             rdn = random.random()
#             if rdn < prob:
#                 output[i][j] = 0
#             elif rdn > thres:
#                 output[i][j] = 255
#             else:
#                 output[i][j] = image[i][j]
#     return output

# image = cv2.imread('image.jpg',0) # Only for grayscale image
# noise_img = sp_noise(image,0.05)
# cv2.imwrite('sp_noise.jpg', noise_img)


def main():
    image_path = "heggi_copy.png"
    image = cv2.imread(image_path)
    i_array = np.array(image / 255)
    noisy_image = add_noise(i_array)
    # if noisy_image.min() < 0:
    #     low_clip = -1
    # else:
    #     low_clip = 0
    # noisy_image = np.clip(noisy_image, low_clip, 1.0)
    noisy_image = np.uint8(noisy_image * 255)
    cv2.imshow("Noisy_Image.png", noisy_image)
    cv2.waitKey(0)
    cv2.imwrite("Noisy_Image.png", noisy_image)


if __name__ == "__main__":
    main()
