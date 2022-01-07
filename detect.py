from block import *
from sort_function import *
from analyze_function import *

import matplotlib.pyplot as plt
import numpy as np
import os
import time
import imageio

from tqdm import tqdm


from PIL import Image


class detect(object):
    def __init__(self, image_path, block_dimension):
        self.image_path = image_path
        self.block_dimension = block_dimension
        self.image_height, self.image_width = self.load_image(self.image_path)

        # algorithm's parameters from the first paper
        self.N = self.image_width * self.image_height
        # self.b = self.block_dimension * self.block_dimension
        self.b = 64
        self.Nb = (self.image_width - self.block_dimension + 1) * (
            self.image_height - self.block_dimension + 1
        )
        self.Nn = 100  # amount of neighboring block to be evaluated
        self.Nf = 128  # minimum treshold of the offset's frequency
        self.Nd = 16  # minimum treshold of the offset's magnitude

        # algorithm's parameters from the second paper
        self.P = (1.80, 1.80, 1.80, 0.0125, 0.0125, 0.0125, 0.0125)
        self.t1 = 2.80
        self.t2 = 0.02

        self.feature_list = list()
        self.offset_dictionary = dict()

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
        feature_list_sort = sort_function(self.feature_list)
        # feature_list_sort.sample_show_list()
        self.sorted_feature_list = feature_list_sort.sort_features()
        # feature_list.sample_show_list()
        return

    def analyze(self):
        analyze_func = analyze_function(
            self.feature_list,
            self.sorted_feature_list,
            self.P,
            self.t1,
            self.t2,
            self.Nd,
            self.Nn,
        )
        self.offset_dictionary = analyze_func.analyze_block()
        return

    def reconstruct(self):
        # Fungsi dibuat berdasarkan referensi nomor satu

        self.image_output_directory = os.getcwd()

        # create an array as the canvas of the final image
        groundtruth_image = np.zeros((self.image_height, self.image_width))
        lined_image = np.array(self.image_data.convert("RGB"))

        # offset yang didapatkan dilakukan sort sehingga hasilnya terbalik
        sorted_offset = sorted(
            self.offset_dictionary,
            key=lambda key: len(self.offset_dictionary[key]),
            reverse=True,
        )

        is_pair_found = False

        for key in sorted_offset:
            if len(self.offset_dictionary[key]) < self.Nf * 2:
                break

            if is_pair_found == False:
                is_pair_found = True

            print(key, len(self.offset_dictionary[key]))

            for i in range(len(self.offset_dictionary[key])):
                # The original image (grayscale)
                for j in range(
                    self.offset_dictionary[key][i][1],
                    self.offset_dictionary[key][i][1] + self.block_dimension,
                ):
                    for k in range(
                        self.offset_dictionary[key][i][0],
                        self.offset_dictionary[key][i][0] + self.block_dimension,
                    ):
                        groundtruth_image[j][k] = 255

        if is_pair_found == False:
            print("Tidak ada pasangan yang ditemukan")

        # Membuat batas x dan y berdasarkan tinggi dan lebar gambar
        for x_coordinate in range(2, self.image_height - 2):
            for y_cordinate in range(2, self.image_width - 2):
                if groundtruth_image[x_coordinate, y_cordinate] == 255 and (
                    groundtruth_image[x_coordinate + 1, y_cordinate] == 0
                    or groundtruth_image[x_coordinate - 1, y_cordinate] == 0
                    or groundtruth_image[x_coordinate, y_cordinate + 1] == 0
                    or groundtruth_image[x_coordinate, y_cordinate - 1] == 0
                    or groundtruth_image[x_coordinate - 1, y_cordinate + 1] == 0
                    or groundtruth_image[x_coordinate + 1, y_cordinate + 1] == 0
                    or groundtruth_image[x_coordinate - 1, y_cordinate - 1] == 0
                    or groundtruth_image[x_coordinate + 1, y_cordinate - 1] == 0
                ):

                    # creating the edge line, respectively left-upper, right-upper, left-down, right-down
                    if (
                        groundtruth_image[x_coordinate - 1, y_cordinate] == 0
                        and groundtruth_image[x_coordinate, y_cordinate - 1] == 0
                        and groundtruth_image[x_coordinate - 1, y_cordinate - 1] == 0
                    ):
                        lined_image[
                            x_coordinate - 2 : x_coordinate, y_cordinate, 1
                        ] = 255
                        lined_image[
                            x_coordinate, y_cordinate - 2 : y_cordinate, 1
                        ] = 255
                        lined_image[
                            x_coordinate - 2 : x_coordinate,
                            y_cordinate - 2 : y_cordinate,
                            1,
                        ] = 255
                    elif (
                        groundtruth_image[x_coordinate + 1, y_cordinate] == 0
                        and groundtruth_image[x_coordinate, y_cordinate - 1] == 0
                        and groundtruth_image[x_coordinate + 1, y_cordinate - 1] == 0
                    ):
                        lined_image[
                            x_coordinate + 1 : x_coordinate + 3, y_cordinate, 1
                        ] = 255
                        lined_image[
                            x_coordinate, y_cordinate - 2 : y_cordinate, 1
                        ] = 255
                        lined_image[
                            x_coordinate + 1 : x_coordinate + 3,
                            y_cordinate - 2 : y_cordinate,
                            1,
                        ] = 255
                    elif (
                        groundtruth_image[x_coordinate - 1, y_cordinate] == 0
                        and groundtruth_image[x_coordinate, y_cordinate + 1] == 0
                        and groundtruth_image[x_coordinate - 1, y_cordinate + 1] == 0
                    ):
                        lined_image[
                            x_coordinate - 2 : x_coordinate, y_cordinate, 1
                        ] = 255
                        lined_image[
                            x_coordinate, y_cordinate + 1 : y_cordinate + 3, 1
                        ] = 255
                        lined_image[
                            x_coordinate - 2 : x_coordinate,
                            y_cordinate + 1 : y_cordinate + 3,
                            1,
                        ] = 255
                    elif (
                        groundtruth_image[x_coordinate + 1, y_cordinate] == 0
                        and groundtruth_image[x_coordinate, y_cordinate + 1] == 0
                        and groundtruth_image[x_coordinate + 1, y_cordinate + 1] == 0
                    ):
                        lined_image[
                            x_coordinate + 1 : x_coordinate + 3, y_cordinate, 1
                        ] = 255
                        lined_image[
                            x_coordinate, y_cordinate + 1 : y_cordinate + 3, 1
                        ] = 255
                        lined_image[
                            x_coordinate + 1 : x_coordinate + 3,
                            y_cordinate + 1 : y_cordinate + 3,
                            1,
                        ] = 255

                # creating the straigh line, respectively upper, down, left, right line
                elif groundtruth_image[x_coordinate, y_cordinate + 1] == 0:
                    lined_image[
                        x_coordinate, y_cordinate + 1 : y_cordinate + 3, 1
                    ] = 255
                elif groundtruth_image[x_coordinate, y_cordinate - 1] == 0:
                    lined_image[x_coordinate, y_cordinate - 2 : y_cordinate, 1] = 255
                elif groundtruth_image[x_coordinate - 1, y_cordinate] == 0:
                    lined_image[x_coordinate - 2 : x_coordinate, y_cordinate, 1] = 255
                elif groundtruth_image[x_coordinate + 1, y_cordinate] == 0:
                    lined_image[
                        x_coordinate + 1 : x_coordinate + 3, y_cordinate, 1
                    ] = 255

        timestamp = time.strftime("%Y%m%d_%H%M%S")

        imageio.imwrite(
            self.image_output_directory + (timestamp + "_" + self.image_path),
            groundtruth_image,
        )
        imageio.imwrite(
            self.image_output_directory + (timestamp + "_lined_" + self.image_path),
            lined_image,
        )

        return self.image_output_directory + timestamp + "_lined_" + self.image_path

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
    image_path = "tank_2.jpg"

    detect_model = detect(image_path, 32)
    detect_model.show_image()
    detect_model.show_metadata()

    detect_model.compute_block()
    detect_model.lexicographic_sort()
    detect_model.analyze()
    result_path = detect_model.reconstruct()


if __name__ == "__main__":
    main()
