#Modified version of original researcher's .sh file. Edited and implemented with the assistance of ChatGPT-4o

import os
import urllib.request
import tarfile
import zipfile
from tkinter import Tk, filedialog

#Hide the main tkinter window
root = Tk()
root.withdraw()

#Ask the user to select the destination folder
download_folder = filedialog.askdirectory(title="Select Destination Folder to Download Data")

#If no folder is selected, exit the script
if not download_folder:
    print("No folder selected. Exiting...")
    exit()

#Define file URLs and paths relative to the selected folder
files_info = {
    f"{download_folder}/prediction_data.tar.gz": "http://lfs.aminer.cn/misc/moocdata/data/prediction_data.tar.gz",
    f"{download_folder}/user_info.csv": "http://lfs.aminer.cn/misc/moocdata/data/user_info.csv",
    f"{download_folder}/course_info.csv": "http://lfs.aminer.cn/misc/moocdata/data/course_info.csv",
    f"{download_folder}/kddcup15.zip": "http://lfs.aminer.cn/misc/moocdata/data/kddcup15.zip",
    f"{download_folder}/kdd2_test.csv": "https://bitbucket.org/lics229/mooc-dropout-prediction/raw/8742cb34f2453955c474aa0a50df72d1d59b39f5/data/final/v5/test/FeatureVectorWithLabel.csv",
    f"{download_folder}/kdd2_train.csv": "https://bitbucket.org/lics229/mooc-dropout-prediction/raw/8742cb34f2453955c474aa0a50df72d1d59b39f5/data/final/v5/train/FeatureVectorWithLabel.csv",
}

#Create the directory if it doesn't exist
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

#Function to download a file
def download_file(url, file_path):
    print(f"Downloading {file_path}...")
    urllib.request.urlretrieve(url, file_path)
    print(f"Downloaded {file_path} successfully.")

#Function to extract a tar.gz file
def extract_tar(file_path, extract_to=download_folder):
    print(f"Extracting files from {file_path}...")
    with tarfile.open(file_path, "r:gz") as tar:
        tar.extractall(path=extract_to)
    print(f"Done extracting files from {file_path}.")

#Function to extract a zip file
def extract_zip(file_path, extract_to= download_folder):
    print(f"Extracting files from {file_path}...")
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Done extracting files from {file_path}.")

#Loop through files and check if they exist, download and extract if necessary
for file_path, url in files_info.items():
    if os.path.exists(file_path):
        print(f"{file_path} exists.")
    else:
        download_file(url, file_path)
        
        # Check for compressed file types and extract
        if file_path.endswith(".tar.gz"):
            extract_tar(file_path)
        elif file_path.endswith(".zip"):
            extract_zip(file_path)

print("All done...")
