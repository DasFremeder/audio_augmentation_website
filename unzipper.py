from zipfile import ZipFile
import os
import shutil
input_folder = "audio_augmentation_website/uploaded_files/user_name/"
output_folder = "audio_augmentation_website/output"

def unzip(path):
    with ZipFile(path, 'r') as object:
        object.printdir()
        object.extractall(input_folder)
    os.remove(path)

def zip_output():
    shutil.make_archive("audio_augmentation_website/output_archive",'zip',output_folder)
