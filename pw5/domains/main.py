import curses
import output as outp
import os
import zipfile

def load_file():
    file_name = "students.dat"
    if os.path.exists(file_name):
        print(f"{file_name} is extracting ...")
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(".")
        print("the extraction process is completed")
    else:
        print("not yet exist")

def save_compress():
    file_compress = ["students.txt", "courses.txt","marks.txt"]
    file_name= "students.dat"

    with zipfile.ZipFile(file_name, 'w', compression=zipfile.ZIP_DEFLATED) as zip_ref:
        for file in file_compress:
            if os.path.exists(file):
                zip_ref.write(file)

    print("Save and Extract are completed")