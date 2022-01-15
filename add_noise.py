import cv2
import numpy as np
import acoustics
from skimage.util import random_noise


def add_noise(img, snr_db):

    """ 
    signal: np.ndarray
    snr: float

    returns -> np.ndarray
    """

    img_mean = np.mean(img)
    avg_db = 10 * np.log10(img_mean)
    noise_avg_db = avg_db - snr_db
    snr = 10.0 ** (noise_avg_db / 10.0)

    noise = np.random.normal(0, np.sqrt(snr), img.shape)
    return img + noise

    # # Generate the noise as you did
    # #noise = acoustics.generator.white(img.size).reshape(img.shape)
    # noise =  np.random.normal(mean, sigma, img.shape)

    # snr = 10.0 ** (snr_db / 10.0)

    # # work out the current SNR
    # current_snr = np.mean(img) / np.std(noise)

    # # scale the noise by the snr ratios (smaller noise <=> larger snr)
    # noise *= current_snr / snr

    # # return the new signal with noise

    # return img + noise

    # # var = 0.1
    # # sigma = var ** 1.2
    # # noisy_image = np.random.normal(mean, sigma, img.shape)
    # # noisy_image = noisy_image.reshape(img.shape)
    # # noisy_image = img + noisy_image
    # # return noisy_image


def main():
    image_path = "195_O.png"
    image = cv2.imread(image_path)
    i_array = np.array(image / 255)
    noisy_image = add_noise(i_array, 40)
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
