class sort(object):
    def __init__(self, feature_list):
        self.feature_list = feature_list
        return

    def sort_features(self):
        # melakukan sort list berdasarkan nilai characteristic dan pixel
        self.feature_list = sorted(self.feature_list, key=lambda x: (x[1], x[2]))
        return

    def sample_show_list(self):
        # fungsi untuk menampilkan isi feature list dengan  banyak sampel data 5
        for index in range(0, 5):
            print(f"Element's index: {self.feature_list[index]}")
        return

    def show_list(self):
        # fungsi menampilkan semua isi dari feature list
        count = self.feature_list.__len__()
        for index in range(0, count):
            print(f"Element's index: {index, self.feature_list[index]}")
        return
