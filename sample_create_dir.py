# Python program to explain os.makedirs() method

# importing os module
import os

# os.makedirs() method will raise
# an OSError if the directory
# to be created already exists


# Directory
directory = "ouput_detect"

try:
    os.makedirs(directory, exist_ok=True)
    print("Directory '%s' created successfully" % directory)
except OSError as error:
    print("Directory '%s' can not be created")

print("Directory '%s' created" % directory)
