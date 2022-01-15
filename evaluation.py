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
            if img_a[i, j].all != img_b[i, j].all:
                falsePx += 1
            else:
                truePx += 1
    return (truePx / float(truePx + falsePx)) * 100


# function to calculate TPR, FPR, ACCURACY, etc
# https://www.analyticsvidhya.com/blog/2021/06/evaluate-your-model-metrics-for-image-classification-and-detection/
def calculateEvaluationValue(tp, tn, fn, fp):
    TNR = (tn / (fp + tn)) * 100
    TPR = (tp / (tp + tn)) * 100
    FPR = (fp / (fp + tn)) * 100
    acc = ((tp + tn) / (tp + tn + fp + fn)) * 100
    return TNR, TPR, FPR, acc


# [255, 255, 255] white region (equal to 1)
# [0,0,0] black region (equal to 0)
def calculateValue(img_a, img_b):
    x, y = img_a.shape[0:2]
    truePositivePx, trueNegativePx, falseNegativePx, falsePositivePx, = 0, 0, 0, 0
    for i in range(x):
        for j in range(y):
            if sum(img_a[i, j]) == 0 and sum(img_b[i, j]) == 0:
                trueNegativePx += 1
            elif sum(img_a[i, j]) == 765 and sum(img_b[i, j]) == 765:
                truePositivePx += 1
            elif sum(img_a[i, j]) == 0 and sum(img_b[i, j]) == 765:
                falseNegativePx += 1
            elif sum(img_a[i, j]) == 765 and sum(img_b[i, j]) == 0:
                falsePositivePx += 1
    return truePositivePx, trueNegativePx, falsePositivePx, falseNegativePx


# function to check image pixel value
def checkValue(img_a, img_b):
    x, y = img_a.shape[0:2]
    truePx, falsePx = 0, 0
    for i in range(x):
        for j in range(y):
            if sum(img_a[i, j]) == 765:
                print(img_a[i, j])
                break
    return


def load_image(path_a, path_b):
    img_a = cv2.imread(path_a)
    img_b = cv2.imread(path_b)
    return img_a, img_b


def main():
    # groundtruth of dataset image
    path_a = "groundtruth_compress_80.png"
    # classification image result
    path_b = "code20220115_203210_compress_80_added.png"
    img_a, img_b = load_image(path_a, path_b)
    mse = calculate_MSE(img_a, img_b)
    print("MSE value : ", mse)
    similarity = calculateSimilarity(img_a, img_b)
    print("Similarity :", similarity)
    tp, tn, fp, fn = calculateValue(img_a, img_b)
    print("tn, tp, fp, fn : ", tn, tp, fp, fn)
    TNR, TPR, FPR, acc = calculateEvaluationValue(tp, tn, fn, fp)
    print("TNR value: ", TNR)
    print("TPR value: ", TPR)
    print("FPR value: ", FPR)
    print("Accuracy value: ", acc)


if __name__ == "__main__":
    main()
