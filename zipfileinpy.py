from zipfile import ZipFile
import os

directory="../anuj python"

def get_all_file_path():
    all_files=[]
    for root,d,files in os.walk(directory):
        print(root)
        for file in files:
            f=os.path.join(root,file)
            all_files.append(f)
    return all_files

file_path=get_all_file_path()
print(file_path)
with ZipFile("archive.zip","w")as zip:
    for file in file_path:
        zip.write(file)

# def extractzip():
#     filename="archive.zip"
#     with ZipFile(filename,"r") as zip:
#         zip.extractall()
extractZip()