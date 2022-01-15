import os

sample_image_path = "/Users/faisalamir/PycharmProjects/tubes_duplicate_region/001_O_added.png"

print(os.path.join(os.getcwd(), "Yihee/Public/", ""))

split_arr = sample_image_path.split("/")

print(split_arr[-1])
