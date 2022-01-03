from block import *
from sort import *

import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

from PIL import Image


class detect(object):
    def __init__(self, image_path, block_dimension):
        self.image_path = image_path
        self.block_dimension = block_dimension
        self.image_height, self.image_width = self.load_image(self.image_path)

        # algorithm's parameters from the first paper
        self.N = self.image_width * self.image_height
        self.b = self.block_dimension * self.block_dimension
        self.Nb = (self.image_width - self.block_dimension + 1) * (
            self.image_height - self.block_dimension + 1
        )
        self.Nn = 2  # amount of neighboring block to be evaluated
        self.Nf = 188  # minimum treshold of the offset's frequency
        self.Nd = 50  # minimum treshold of the offset's magnitude

        # algorithm's parameters from the second paper
        self.P = (1.80, 1.80, 1.80, 0.0125, 0.0125, 0.0125, 0.0125)
        self.t1 = 2.80
        self.t2 = 0.02

        self.feature_list = list()

    def check_image(self, image_height, image_width):
        if self.image_data != "L":
            self.is_rgb_image = True
            self.image_data = self.image_data.convert("RGB")
            rgb_image_pixels = self.image_data.load()
            self.image_gray = self.image_data.convert(
                "L"
            )  # creates a grayscale version of current image to be used later
            grayscale_image_pixels = self.image_gray.load()
            for y_coordinate in range(0, image_height):
                for x_coordinate in range(0, image_width):
                    (
                        red_pixel_value,
                        green_pixel_value,
                        blue_pixel_value,
                    ) = rgb_image_pixels[x_coordinate, y_coordinate]
                    grayscale_image_pixels[x_coordinate, y_coordinate] = (
                        int(0.299 * red_pixel_value)
                        + int(0.587 * green_pixel_value)
                        + int(0.114 * blue_pixel_value)
                    )
        else:
            self.is_rgb_image = False
            self.image_gray = self.image_data.convert("L")
        return

    def load_image(self, image_path):
        self.image_data = Image.open(self.image_path)
        image_width, image_height = self.image_data.size
        self.check_image(image_height, image_width)
        return image_height, image_width

    def compute_block(self):
        image_width_overlap = self.image_width - self.block_dimension
        image_height_overlap = self.image_height - self.block_dimension
        block_list = list()

        if self.is_rgb_image:
            for i in tqdm(range(0, image_width_overlap + 1, 1)):
                for j in range(0, image_height_overlap + 1, 1):
                    image_block_rgb = self.image_data.crop(
                        (i, j, i + self.block_dimension, j + self.block_dimension)
                    )
                    image_block_grayscale = self.image_gray.crop(
                        (i, j, i + self.block_dimension, j + self.block_dimension)
                    )
                    image_block = block(
                        image_block_grayscale,
                        image_block_rgb,
                        i,
                        j,
                        self.block_dimension,
                    )
                    block_list = image_block.compute_block()
                    self.feature_list.append(block_list)
        else:
            for i in tqdm(range(image_width_overlap + 1)):
                for j in range(image_height_overlap + 1):
                    image_block_grayscale = self.image_data.crop(
                        (i, j, i + self.block_dimension, j + self.block_dimension)
                    )
                    image_block = block(
                        image_block_grayscale, None, i, j, self.block_dimension
                    )
                    block_list = image_block.compute_block()
                    self.feature_list.append(block_list)
        return

    def lexicographic_sort(self):
        feature_list = sort(self.feature_list)
        feature_list.sample_show_list()
        feature_list.sort_features()
        # feature_list.sample_show_list()
        return

    def show_image(self):
        self.image_data.show()
        self.image_gray.show()
        return

    def show_metadata(self):
        print("Image Name : ", self.image_path)
        print("Block Dimension : ", self.block_dimension)
        print("Image Height : ", self.image_height)
        print("Image Width : ", self.image_width)
        print("N : ", self.N)
        print("B : ", self.b)
        print("Nb : ", self.Nb)
        print("Nn : ", self.Nn)
        print("Nf : ", self.Nf)
        print("Nd : ", self.Nd)
        print("P : ", self.P)
        print("T1 : ", self.t1)
        print("T2 : ", self.t2)
        return


def main():
    image_path = "Kuda Duplikat.jpg"

    detect_model = detect(image_path, 32)
    detect_model.show_image()
    detect_model.show_metadata()

    detect_model.compute_block()
    detect_model.lexicographic_sort()


if __name__ == "__main__":
    main()
