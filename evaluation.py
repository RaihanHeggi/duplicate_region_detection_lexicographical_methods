import cv2
import numpy as np


def calculate_MSE(img_a, img_b):
    meanSquaredError = np.sum((img_a.astype("float") - img_b.astype("float")) ** 2)
    meanSquaredError = meanSquaredError / float(img_a.shape[0] * img_b.shape[0])
    return meanSquaredError


def calculateSimilarity(img_a, img_b):
    x, y = img_a.shape[0:2]
    truePx, falsePx = 0, 0
    for i in range(x):
        for j in range(y):
            if img_a[i, j] != img_b[i, j]:
                falsePx += 1
            else:
                truePx += 1
    return (truePx / float(truePx + falsePx)) * 100


def calculateValue(img_a, img_b):
    x, y = img_a.shape[0:2]
    truePx, falsePx = 0, 0
    for i in range(x):
        for j in range(y):
            if img_a[i, j] != img_b[i, j]:
                falsePx += 1
            else:
                truePx += 1
    return truePx, falsePx


def load_image(path_a, path_b):
    img_a = cv2.imread(path_a)
    img_b = cv2.imread(path_b)
    return img_a, img_b


def main():
    path_a = "code20220108_192105_heggi_copy.png"
    path_b = "heggi_copy.png"
    img_a, img_b = load_image(path_a, path_b)
    mse = calculate_MSE(img_a, img_b)
    print(mse)


if __name__ == "__main__":
    main()
