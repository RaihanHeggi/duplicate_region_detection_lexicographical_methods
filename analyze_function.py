from tqdm import tqdm
import numpy as np
import math


class analyze_function(object):
    def __init__(self, feature_list, sorted_feature_list, P, t1, t2, Nd, Nn):
        self.sorted_feature_list = sorted_feature_list
        self.feature_list = feature_list
        self.P = P
        self.t1 = t1
        self.t2 = t2
        self.Nd = Nd
        self.Nn = Nn

    # function to analyze block relations
    def analyze_block(self):
        iteration = 0
        feature_len = len(self.sorted_feature_list)
        for i in tqdm(range(feature_len - 1)):
            j = i + 1
            result = self.is_correlated(i, j)
            if result[0]:
                self.add_dictionary(
                    self.sorted_feature_list[i][0],
                    self.sorted_feature_list[j][0],
                    result[1],
                )
                z += 1
        return self.offset_dictionary

    def is_correlated(self, first_block, second_block):
        if abs(first_block - second_block) < self.Nn:
            first_feature = self.sorted_feature_list[first_block][1]
            second_feature = self.sorted_feature_list[second_block][1]

            # cek validitas menggunakan rumus robust detection, membandingkan distance block dengan probabilitas dan akhirnya melakukan perbandingan dengan nilai threshold
            # pada paper nilai P ini digunakan untuk gambar berukuran 300x400px sehingga bila menggunakan berbeda mungkin akan kurang cocok
            if abs(first_feature[0] - second_feature[0]) < self.P[0]:
                if abs(first_feature[1] - second_feature[1]) < self.P[1]:
                    if abs(first_feature[2] - second_feature[2]) < self.P[2]:
                        if abs(first_feature[3] - second_feature[3]) < self.P[3]:
                            if abs(first_feature[4] - second_feature[4]) < self.P[4]:
                                if (
                                    abs(first_feature[5] - second_feature[5])
                                    < self.P[5]
                                ):
                                    if (
                                        abs(first_feature[6] - second_feature[6])
                                        < self.P[6]
                                    ):
                                        if (
                                            abs(first_feature[0] - second_feature[0])
                                            + abs(first_feature[1] - second_feature[1])
                                            + abs(first_feature[2] - second_feature[2])
                                            < self.t1
                                        ):
                                            if (
                                                abs(
                                                    first_feature[3] - second_feature[3]
                                                )
                                                + abs(
                                                    first_feature[4] - second_feature[4]
                                                )
                                                + abs(
                                                    first_feature[5] - second_feature[5]
                                                )
                                                + abs(
                                                    first_feature[6] - second_feature[6]
                                                )
                                                < self.t2
                                            ):

                                                # mengkomputasi nilai offset kedua koordinat
                                                i_coordinate = self.sorted_feature_list[
                                                    first_block
                                                ][0]
                                                j_coordinate = self.sorted_feature_list[
                                                    second_block
                                                ][0]

                                                # Simpan nilai offset dengan menggunakan prinsip Non Absolute Robust
                                                offset = (
                                                    i_coordinate[0] - j_coordinate[0],
                                                    i_coordinate[1] - j_coordinate[1],
                                                )

                                                # Bandingkan nilai Magnitude
                                                magnitude = np.sqrt(
                                                    math.pow(offset[0], 2)
                                                    + math.pow(offset[1], 2)
                                                )
                                                if magnitude >= self.Nd:
                                                    return 1, offset
        return (0,)

    def add_dictionary(self, first_coordinate, second_coordinate, pair_offset):
        if pair_offset in self.offset_dictionary:
            self.offset_dictionary[pair_offset].append(first_coordinate)
            self.offset_dictionary[pair_offset].append(second_coordinate)
        else:
            self.offset_dictionary[pair_offset] = [first_coordinate, second_coordinate]
