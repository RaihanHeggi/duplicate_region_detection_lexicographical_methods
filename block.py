import numpy as np
from sklearn.decomposition import PCA


class block(object):
    def __init__(
        self, image_gray, image_rgb, x_coordinate, y_coordinate, block_dimension
    ):
        self.image_grayscale = image_gray  # block of grayscale image
        self.image_grayscale_pixels = self.image_grayscale.load()
        self.image_rgb = image_rgb
        self.image_rgb_pixels = self.image_rgb.load()
        self.coordinate = (x_coordinate, y_coordinate)
        self.block_dimension = block_dimension
